"""
Turn the hand-written candidate questions into a gold set with gold chunks.

Three steps, with ``data/eval/questions/anchoring/ANCHORING.md`` as the single
place a human reviews and edits:

  candidates  Retrieve candidate chunks for every question in CANDIDATES.md
              (dense + lexical, per expected party; per every party for
              all-party questions) into candidates.json, and render ANCHORING.md.
  render      Re-render ANCHORING.md from candidates.json, pre-ticking the keys
              and filling the reference answers given in a picks JSON
              ({"q-01": {"gold": ["sha1:..."], "reference": "..."}}). Overwrites
              ANCHORING.md: use it before review, never after.
  compile     Read ANCHORING.md (labels, ticked candidates, reference answers)
              and write golden.json. A question is ``curated`` only when it has
              a ticked chunk, a reference answer and ``reviewed: yes``. An
              ``answerable: no`` question (the manifestos do not answer it) has
              no chunk to tick and needs only the reference and the review.
              Each gold key also gets its aspect (party + manifesto header
              path, from the classified checkpoints) for ``aspect_recall``.

Labels are seeded from CANDIDATES.md plus the decisions recorded below, and can be
edited in ANCHORING.md before compiling.

Usage:
  python scripts/anchor_gold.py candidates
  python scripts/anchor_gold.py render --picks picks.json
  python scripts/anchor_gold.py compile
"""

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime
from typing import Dict, List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rag.common.models import PARTY_MAP  # noqa: E402
from src.rag.evaluation.dataset import save_dataset  # noqa: E402
from src.rag.evaluation.keys import chunk_key  # noqa: E402
from src.rag.evaluation.models import EvalDataset, EvalQuestion  # noqa: E402
from src.utils.config_loader import config  # noqa: E402

QDIR = "data/eval/questions"
CANDIDATES_MD = os.path.join(QDIR, "CANDIDATES.md")
ANCHOR_DIR = os.path.join(QDIR, "anchoring")
CANDIDATES_JSON = os.path.join(ANCHOR_DIR, "candidates.json")
ANCHORING_MD = os.path.join(ANCHOR_DIR, "ANCHORING.md")
GOLDEN = os.path.join(QDIR, "golden.json")

# "AD" -> "Aliança Democrática", ..., in PARTY_MAP order.
PARTIES = {key.split("-")[0].upper(): info["name"] for key, info in PARTY_MAP.items()}

# Decisions taken 2026-10-08 when the 51 candidates became the gold set.
# "All parties" questions asking what *each* party says need every party covered.
EXHAUSTIVE = {32, 33, 36, 38, 41, 51}
# Held-out questions for headline numbers; the rest are for tuning.
TEST = {1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 19, 20, 21, 22, 24, 26, 27, 31,
        32, 34, 35, 36, 41, 44, 50, 51, 45, 47, 48, 49}

# Lexical queries for candidate gathering. The question text itself is useless
# here: websearch_to_tsquery ANDs every word, so a full question matches almost
# no chunk (a known defect of the hybrid rung, fixed separately). Short keyword
# queries, with websearch "or", recover the passages dense search misses.
KEYWORDS = {
    1: "taxa única IRS", 2: '"salário mínimo" 1000', 3: '"IRS Jovem"',
    4: "tourada or tauromáquicos or tauromaquia", 5: "IVG or aborto or interrupção gravidez",
    6: '"prisão perpétua" or castração or reincidentes', 7: '"médico de família"',
    8: "NATO or OTAN or Euro", 9: "propinas", 10: '"saúde mental"', 11: "nuclear",
    12: "regionalização", 13: '"rendimento básico"', 14: "canábis or cannabis",
    15: "imigração or imigrantes", 16: "natalidade or PMA", 17: '"Alojamento Local"',
    18: '"sistema eleitoral" or compensação', 19: "IRS", 20: '"35 horas" or "horário de trabalho"',
    21: "creche or creches", 22: '"Alojamento Local"', 23: '"IRS Jovem"', 24: "IRC",
    25: "regionalização or descentralização", 26: "privatização or privatizações or nacionalização or \"controlo público\"",
    27: "imigração or imigrantes", 28: "animais or animal", 29: '"Administração Pública"',
    30: "pensões or pensão", 31: '"quatro dias" or "4 dias"', 32: "nuclear", 33: '"salário mínimo"',
    34: '"listas de espera" or "tempos de espera" or "tempo de espera"', 35: "rendas or renda or arrendamento",
    36: "IRC", 37: "professores", 38: "floresta or florestas or incêndios", 39: "corrupção",
    40: 'emigrantes or diáspora or "comunidades portuguesas"', 41: '"alta velocidade"',
    42: "deficiência", 43: '"inteligência artificial"', 44: '"violência doméstica"',
    45: '"IRS Jovem"', 46: 'PRR or "Plano de Recuperação"', 47: "imigrantes registo",
    48: '"herança social" or heranças', 49: '"35 horas"', 50: "IRC 12",
    51: '"morte medicamente assistida" or eutanásia',
}

PER_PARTY_NAMED = 6   # dense + lexical each, per named party
PER_PARTY_ALL = 3     # dense + lexical each, per party, for all-party questions
POOLED = 8            # extra pooled dense hits for questions naming no party


# ---------------------------------------------------------------------------
# CANDIDATES.md -> question seeds
# ---------------------------------------------------------------------------

def parse_candidates(path: str = CANDIDATES_MD) -> List[dict]:
    section, out = "", []
    for line in open(path, encoding="utf-8"):
        if line.startswith("## "):
            section = line[3:].split("(")[0].strip().lower()
            continue
        m = re.match(r"^\| (\d+) \| (.+?) \| (.+?) \| (.+?) \| (.+?) \| ([EMH]) \| (.*) \|\s*$", line)
        if not m or section.startswith("abstention"):
            continue
        n = int(m.group(1))
        raw_parties = m.group(3).strip()
        parties = [] if raw_parties in ("all", "none") else [PARTIES[p.strip()] for p in raw_parties.split(",")]
        topics = [t.strip() for t in m.group(4).split(",")]
        if section == "general":
            topics = []  # general = no party, no topic (decision 2026-10-08)
        out.append({
            "id": f"q-{n:02d}", "n": n, "question": m.group(2).strip(),
            "parties": parties, "topics": topics,
            "coverage": "exhaustive" if n in EXHAUSTIVE else "best_match",
            "split": "test" if n in TEST else "dev",
            "stresses": m.group(5).strip(), "diff": m.group(6), "note": m.group(7).strip(),
        })
    return out


# ---------------------------------------------------------------------------
# candidates: retrieval
# ---------------------------------------------------------------------------

def _hit(r) -> dict:
    return {
        "key": chunk_key(r.content), "party": r.party_name,
        "section": " > ".join(str(v) for k, v in (r.header_hierarchy or {}).items()
                              if k not in ("sub_chunk_index", "total_sub_chunks", "parent_chunk_size")),
        "content": r.content,
    }


def gather(seed: dict, store, embedder) -> List[dict]:
    q = seed["question"]
    vec = embedder.encode_query(q)
    parties = seed["parties"] or list(PARTIES.values())
    k = PER_PARTY_NAMED if seed["parties"] else PER_PARTY_ALL
    hits: Dict[str, dict] = {}
    for party in parties:
        lexical = store.lexical_search(KEYWORDS[seed["n"]], top_k=k, party_name=party)
        for r in store.similarity_search(vec, top_k=k, party_name=party) + lexical:
            hits.setdefault(chunk_key(r.content), _hit(r))
    if not seed["parties"]:
        for r in store.similarity_search(vec, top_k=POOLED):
            hits.setdefault(chunk_key(r.content), _hit(r))
    order = {p: i for i, p in enumerate(PARTIES.values())}
    return sorted(hits.values(), key=lambda h: order.get(h["party"], 99))


def cmd_candidates(_args) -> None:
    from src.rag.indexing.embedder import Embedder
    from src.rag.indexing.store import VectorStore

    store, embedder = VectorStore(), Embedder()
    store.connect()
    try:
        seeds = parse_candidates()
        for s in seeds:
            s["candidates"] = gather(s, store, embedder)
            print(f"{s['id']} {len(s['candidates']):3} candidates")
    finally:
        store.close()
    os.makedirs(ANCHOR_DIR, exist_ok=True)
    json.dump(seeds, open(CANDIDATES_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    render(seeds, {})


# ---------------------------------------------------------------------------
# render / compile: ANCHORING.md
# ---------------------------------------------------------------------------

def _one_line(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def render(seeds: List[dict], picks: Dict[str, dict]) -> None:
    out = [
        "# Gold-chunk anchoring", "",
        "Tick `[x]` every candidate that (partly) answers the question, fix the labels if",
        "needed, and write or correct the `reference` answer. Ticked chunks are shown in",
        "full; the others are cut to 400 characters. Then run",
        "`python scripts/anchor_gold.py compile` to write `golden.json`.", "",
        "Pre-ticks and draft references, where present, were proposed by Claude and must",
        "be checked. Set `reviewed: yes` once a question is right: only then does it count",
        "as curated (`eval --curated-only`).", "",
    ]
    for s in seeds:
        pick = picks.get(s["id"], {})
        gold = set(pick.get("gold", []))
        out += [
            f"## {s['id']} — {s['question']}", "",
            f"- split: {s['split']}",
            f"- coverage: {s['coverage']}",
            f"- parties: {', '.join(s['parties']) or '-'}",
            f"- topics: {', '.join(s['topics']) or '-'}",
            f"- stresses: {s['stresses']} · diff: {s['diff']}",
            f"- note: {s['note']}",
            f"- reference: {pick.get('reference', '')}",
            "- reviewed: no",
        ]
        if pick.get("flag"):
            out.append(f"- review: {pick['flag']}")
        out.append("")
        for c in s["candidates"]:
            ticked = c["key"] in gold
            body = _one_line(c["content"]) if ticked else _one_line(c["content"])[:400] + "…"
            out += [f"- [{'x' if ticked else ' '}] `{c['key']}` · **{c['party']}** · {c['section']}", f"  > {body}"]
        out.append("")
    open(ANCHORING_MD, "w", encoding="utf-8").write("\n".join(out))
    print(f"wrote {ANCHORING_MD}")


def cmd_render(args) -> None:
    seeds = json.load(open(CANDIDATES_JSON, encoding="utf-8"))
    picks = json.load(open(args.picks, encoding="utf-8")) if args.picks else {}
    unknown = {k for p in picks.values() for k in p.get("gold", [])} - {
        c["key"] for s in seeds for c in s["candidates"]}
    if unknown:
        sys.exit(f"picks reference keys that are not candidates: {sorted(unknown)[:5]}")
    render(seeds, picks)


def parse_anchoring(path: str = ANCHORING_MD) -> List[EvalQuestion]:
    questions, cur = [], None

    def flush():
        if cur:
            questions.append(_question(cur))

    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        m = re.match(r"^## (q-\d+) — (.+)$", line)
        if m:
            flush()
            cur = {"id": m.group(1), "question": m.group(2), "gold": [], "reference": "",
                   "parties": [], "topics": [], "coverage": "best_match", "split": "", "reviewed": "no",
                   "answerable": "yes"}
            continue
        if cur is None:
            continue
        m = re.match(r"^- (split|coverage|parties|topics|reference|reviewed|answerable): ?(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if key in ("parties", "topics"):
                cur[key] = [] if val in ("", "-") else [v.strip() for v in val.split(",")]
            else:
                cur[key] = val
            continue
        m = re.match(r"^- \[[xX]\] `(sha1:[0-9a-f]+)`", line)
        if m:
            cur["gold"].append(m.group(1))
    flush()
    return questions


def _question(cur: dict) -> EvalQuestion:
    from src.rag.common.models import AnalyzedQuery, Coverage

    # The route label is derived exactly as the pipeline derives it, so the gold
    # row can never contradict its own parties/coverage annotations.
    query_type = AnalyzedQuery(
        original_query=cur["question"], parties=cur["parties"],
        coverage=Coverage(cur["coverage"]), topics=cur["topics"],
    ).query_type.value
    answerable = cur["answerable"].lower() != "no"
    return EvalQuestion(
        id=cur["id"], question=cur["question"], query_type=query_type,
        coverage=cur["coverage"], expected_parties=cur["parties"],
        expected_topics=cur["topics"], gold_chunk_keys=cur["gold"],
        reference_answer=cur["reference"], answerable=answerable,
        source_party=cur["parties"][0] if len(cur["parties"]) == 1 else "",
        # Curated means a human signed it off, not merely that it is filled in:
        # ticks and references may have been proposed by a model.
        curated=bool((cur["gold"] or not answerable) and cur["reference"] and cur["reviewed"].lower() == "yes"),
        split=cur["split"],
    )


def _sections() -> Dict[str, str]:
    """Content key -> "party > header path", read from the classified checkpoints."""
    window = {"sub_chunk_index", "total_sub_chunks", "parent_chunk_size"}
    out: Dict[str, str] = {}
    for path in glob.glob(os.path.join(str(config.get("paths.processed_data")), "*-classified.json")):
        for c in json.load(open(path, encoding="utf-8"))["chunks"]:
            headers = [str(v) for k, v in (c.get("metadata") or {}).items() if k not in window]
            out[chunk_key(c["content"])] = " > ".join([c["party_name"], *headers])
    return out


def cmd_compile(_args) -> None:
    questions = parse_anchoring()
    sections = _sections()
    stale = sorted({k for q in questions for k in q.gold_chunk_keys if k not in sections})
    if stale:
        sys.exit(f"{len(stale)} gold keys match no chunk in the checkpoints (re-chunked?): {stale[:5]}")
    for q in questions:
        q.gold_aspects = {k: sections[k] for k in q.gold_chunk_keys}
    ds = EvalDataset(created_at=datetime.now().isoformat(timespec="seconds"), questions=questions)
    save_dataset(ds, GOLDEN)
    todo = [q.id for q in questions if not q.curated]
    print(f"{len(questions)} questions -> {GOLDEN}; curated {len(questions) - len(todo)}"
          + (f"; not curated yet: {', '.join(todo)}" if todo else ""))


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("candidates")
    r = sub.add_parser("render")
    r.add_argument("--picks", default=None)
    sub.add_parser("compile")
    args = ap.parse_args()
    {"candidates": cmd_candidates, "render": cmd_render, "compile": cmd_compile}[args.cmd](args)


if __name__ == "__main__":
    main()
