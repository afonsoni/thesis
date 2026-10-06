"""
Structural cleanup of parsed manifesto markdown (raw marker output -> ``*-clean.md``).

Reproduces what was done by hand for the ``*-manual.md`` files: one H1 title,
header levels that follow the manifesto's own outline, fake headers (bold
numbered measures marker promoted to ``#``) turned back into list items, and
cover/índice/running-header junk removed.

Two passes:

1. Deterministic (:func:`prepare`): images, span anchors, bare page numbers,
   ``•`` bullets turned into list items and bullets broken across paragraphs by
   PDF line wraps rejoined (PAN's main damage).
2. LLM (:func:`plan_structure`): sees only the existing header lines and returns
   keep-with-level / demote-to-body / drop for each. The hand-cleaned files never
   promoted body text to a header, so body lines are not offered. The rewrite is
   applied in code, and :func:`verify` fails if the output contains a single word
   the prepared text did not: the LLM cannot invent or paraphrase body text.
"""

import hashlib
import json
import logging
import os
import re
import threading
import time
from collections import Counter
from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, Field

from src.rag.common.llm_client import generate_structured
from src.rag.indexing.parser import strip_images
from src.utils.config_loader import config

logger = logging.getLogger(__name__)

# Small batches, as for classification: large Gemma requests time out or 500.
BATCH_SIZE = 40
CALL_DELAY_SECS = float(config.get("indexing.classification_delay", 1.0))
# Free-tier errors (429/500/503, timeouts) are transient: wait them out rather
# than fail a whole party after the transport's few quick retries.
WAIT_OUT_ATTEMPTS = 10
WAIT_OUT_BASE_SECS = 30
WAIT_OUT_MAX_SECS = 300
# Wall-clock cap on one structured call (transport retries included). Gemini can
# hold a connection open for 15+ minutes without answering, which a per-read
# socket timeout never catches.
CALL_DEADLINE_SECS = 600
MAX_DROP_RANGE_FRACTION = 0.05

_SPAN_RE = re.compile(r"</?span[^>]*>")
# Page numbers left alone on a line ("12", "**12**", "Pág. 12").
_PAGE_NUMBER_RE = re.compile(r"^[\s*_#]*(Pág\.?\s*)?\d{1,3}[\s*_]*$")
_HEADER_RE = re.compile(r"^(#{1,6})\s+(.*)$")
# "•x", "**•x**", "- **• x**", "### **•x**": a bullet, whatever marker wraps it.
_BULLET_RE = re.compile(r"^(#{1,6}\s+)?(-\s+)?(\*\*)?\s*•\s*(.*?)\s*$")
_SECTION_NUMBER_RE = re.compile(r"^\d+(\.\d+)*\.?(?=\s)")
_NUMBERED_RE = re.compile(r"^(\*\*|__)?\s*(\d+)[.)]?\s+")
_INDEX_RE = re.compile(r"\b(índice|sumário)\b", re.IGNORECASE)


# ---------------------------------------------------------------------------
# Deterministic pass
# ---------------------------------------------------------------------------

def prepare(text: str) -> List[str]:
    """Strip images, span anchors and bare page numbers, fix bullets; return the lines."""
    text = _SPAN_RE.sub("", strip_images(text))
    lines = [line for line in text.split("\n") if not _PAGE_NUMBER_RE.match(line) or not line.strip()]
    return fix_bullets(lines)


def fix_bullets(lines: List[str]) -> List[str]:
    """Turn ``•`` bullets into ``- `` list items and rejoin bullets split by PDF wraps.

    marker emits a wrapped bullet as two paragraphs (``**•Elaborar ... armaze-**``
    then ``**namento de energia ...**``), sometimes promoting either half to a
    header. A paragraph is a continuation when it follows a converted bullet that
    has no closing punctuation and starts in lowercase.
    """
    out: List[str] = []
    last_bullet: Optional[int] = None  # index in out of the last converted bullet
    for line in lines:
        s = line.strip()
        if not s:
            out.append(line)
            continue
        m = _BULLET_RE.match(line)
        if m:
            item = m.group(4)
            if m.group(3) and item.endswith("**"):
                item = item[:-2].rstrip()
            out.append(f"- {item}")
            last_bullet = len(out) - 1
            continue
        h = _HEADER_RE.match(line)
        frag = _unbold(h.group(2) if h else s)
        prev = out[last_bullet] if last_bullet is not None else ""
        only_blanks_between = last_bullet is not None and all(not x.strip() for x in out[last_bullet + 1:])
        if only_blanks_between and frag[:1].islower() and not prev.rstrip().endswith((".", ";", ":", "!", "?")):
            del out[last_bullet + 1:]
            if prev.endswith("-") and prev[-2:-1].isalpha():
                out[last_bullet] = prev[:-1] + frag
            else:
                out[last_bullet] = f"{prev} {frag}"
            continue
        out.append(line)
        last_bullet = None
    return out


def _unbold(text: str) -> str:
    return re.sub(r"\*\*|__", "", text).strip()


def find_candidates(lines: List[str]) -> List[int]:
    """Indices of header lines: the only lines whose structural role is in question."""
    return [i for i, line in enumerate(lines) if _HEADER_RE.match(line)]


# ---------------------------------------------------------------------------
# LLM structure plan
# ---------------------------------------------------------------------------

class LineAction(BaseModel):
    line: int
    action: Literal["header", "body", "drop"]
    level: Optional[int] = Field(default=None, ge=1, le=6)
    title: Optional[str] = None


class StructurePlan(BaseModel):
    actions: List[LineAction] = Field(default_factory=list)
    drop_ranges: List[List[int]] = Field(default_factory=list)


CLEANING_PROMPT = """És um editor que corrige a hierarquia de títulos de um programa eleitoral português convertido de PDF para markdown.

Recebes os títulos (linhas começadas por #) no formato `L<n> [<marcação atual>] <texto>  → <início da linha seguinte>`.
Para CADA título devolve uma ação:
- "header" (o caso normal: a maioria dos títulos são reais): indica "level" (1-6).
- "body": só se NÃO for um título: uma medida numerada transformada em título ("**7 Assegurar a proteção social**, através de:"), uma frase completa, o fim de uma frase partida, ou um item de lista.
- "drop": só lixo sem conteúdo: cabeçalho/rodapé de página repetido sem título (ex.: "PROGRAMA ELEITORAL BLOCO DE ESQUERDA"), número de página, fragmento da capa, entrada do índice impresso.

Regras:
1. Na dúvida, "header". Não transformes títulos reais em texto.
2. Não alteres o texto do título. Usa "title" APENAS quando a linha junta um cabeçalho de página e um título ("Programa do LIVRE | Legislativas 2024 **Educação**" → title "Educação"); nesse caso é "header", nunca "drop". Mantém sempre a numeração de secção ("1.1.", "3.").
3. Níveis: um único nível 1 (título do documento); partes/capítulos a 2; desce um nível por cada subdivisão, seguindo a numeração (2 > 2.1 > 2.1.1) e o índice. Títulos irmãos têm o mesmo nível.

Exemplos de programas já corrigidos à mão (segue o mesmo estilo):
AD:
# PROGRAMA SOCIAL E DE GOVERNAÇÃO DA ALIANÇA DEMOCRÁTICA
## COM AMBIÇÃO
### QUALIFICAÇÃO
#### EDUCAÇÃO E FORMAÇÃO
##### 1. Porque é preciso mudar
##### 2. Metas
##### 3. Medidas
###### MODERNIZAR O SISTEMA EDUCATIVO
###### RECONHECER A IMPORTÂNCIA DOS PROFESSORES
#### CIÊNCIA E ENSINO SUPERIOR
LIVRE:
# Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024
## Saúde
### Por isso defendemos:
#### Reforçar e Reorganizar o Serviço Nacional de Saúde
#### Investir na Saúde Mental
## Educação
(no LIVRE, "# **7 Assegurar a proteção social e laboral...**" era uma medida: "body".)

Em "drop_ranges" indica intervalos [início, fim] de linhas (inclusive) a remover por inteiro: SÓ a capa e o índice/sumário impresso. Nunca texto programático.

Partido: {party}
{index_block}{outline_block}
Títulos:
{candidates}

Responde com JSON: {{"actions": [{{"line": n, "action": "...", "level": n|null, "title": "..."|null}}], "drop_ranges": [[a, b]]}}"""


def _next_text(lines: List[str], i: int) -> str:
    for line in lines[i + 1:i + 6]:
        if line.strip():
            return line.strip()[:80]
    return ""


def _render_candidate(lines: List[str], i: int) -> str:
    m = _HEADER_RE.match(lines[i])
    marker, text = (m.group(1), m.group(2)) if m else ("texto", lines[i].strip())
    return f"L{i} [{marker}] {text[:200]}  → {_next_text(lines, i)}"


def _index_block(lines: List[str]) -> str:
    """The printed índice, if one is found near the start, as a structure hint."""
    for i, line in enumerate(lines[:400]):
        if _HEADER_RE.match(line) and _INDEX_RE.search(line):
            excerpt = "\n".join(f"L{j}: {lines[j][:150]}" for j in range(i, min(i + 80, len(lines))) if lines[j].strip())
            return f"\nÍndice impresso (referência para a hierarquia):\n{excerpt[:5000]}\n"
    return ""


def _outline_block(lines: List[str], decided: Dict[int, LineAction]) -> str:
    """Headers already placed by earlier batches, so levels stay consistent."""
    heads = [(i, a) for i, a in sorted(decided.items()) if a.action == "header"][-25:]
    if not heads:
        return ""
    rows = "\n".join(f"{'  ' * (a.level - 1)}{a.level}: {a.title or _strip_marker(lines[i])}" for i, a in heads)
    return f"\nEstrutura já decidida (últimos títulos, mantém a coerência):\n{rows}\n"


def _strip_marker(line: str) -> str:
    m = _HEADER_RE.match(line)
    return _unbold(m.group(2) if m else line)


def _with_deadline(fn, secs: float):
    """Run *fn* in a daemon thread; raise TimeoutError if it has not returned in *secs*.

    A hung call's thread is abandoned (daemon, so it cannot block exit).
    """
    box: Dict[str, object] = {}

    def run():
        try:
            box["value"] = fn()
        except BaseException as exc:  # noqa: BLE001 - re-raised in the caller's thread
            box["error"] = exc

    worker = threading.Thread(target=run, daemon=True)
    worker.start()
    worker.join(secs)
    if worker.is_alive():
        raise TimeoutError(f"no answer within {secs:.0f}s")
    if "error" in box:
        raise box["error"]  # type: ignore[misc]
    return box["value"]


def _plan_batch(prompt: str, model: str, party: str, batch_no: int) -> StructurePlan:
    for attempt in range(WAIT_OUT_ATTEMPTS):
        try:
            return _with_deadline(
                lambda: generate_structured(prompt, StructurePlan, model=model, temperature=0.0,
                                            max_tokens=4000, timeout_seconds=180),
                CALL_DEADLINE_SECS,
            )
        except Exception as exc:  # noqa: BLE001 - transport/JSON errors are retried, then raised
            if attempt == WAIT_OUT_ATTEMPTS - 1:
                raise
            wait = min(WAIT_OUT_MAX_SECS, WAIT_OUT_BASE_SECS * (attempt + 1))
            logger.warning("%s batch %d failed (%s); waiting %ds", party, batch_no, str(exc)[:120], wait)
            time.sleep(wait)
    raise AssertionError("unreachable")


def _load_cache(path: Optional[str], fingerprint: str) -> Dict[str, dict]:
    if not path or not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return data.get("batches", {}) if data.get("fingerprint") == fingerprint else {}


def _save_cache(path: Optional[str], fingerprint: str, batches: Dict[str, dict]) -> None:
    if not path:
        return
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"fingerprint": fingerprint, "batches": batches}, fh, ensure_ascii=False)


def plan_structure(
    lines: List[str], party: str, model: Optional[str] = None, cache_path: Optional[str] = None,
) -> StructurePlan:
    """Ask the LLM for an action per candidate line, in batches.

    Each batch's answer is saved to *cache_path* as it arrives, so a run killed by
    a free-tier outage resumes where it stopped. The cache is keyed on the prompt
    template, model and prepared text, so any change to those starts over.
    """
    model = model or config.get("indexing.cleaning_model", config.get("llm.openrouter.model"))
    candidates = find_candidates(lines)
    index_block = _index_block(lines)
    decided: Dict[int, LineAction] = {}
    drop_ranges: List[List[int]] = []
    fingerprint = hashlib.sha1("\0".join([CLEANING_PROMPT, str(model), *lines]).encode()).hexdigest()
    cache = _load_cache(cache_path, fingerprint)

    for start in range(0, len(candidates), BATCH_SIZE):
        batch = candidates[start:start + BATCH_SIZE]
        prompt = CLEANING_PROMPT.format(
            party=party,
            index_block=index_block,
            outline_block=_outline_block(lines, decided),
            candidates="\n".join(_render_candidate(lines, i) for i in batch),
        )
        if str(start) in cache:
            plan = StructurePlan.model_validate(cache[str(start)])
        else:
            plan = _plan_batch(prompt, model, party, start // BATCH_SIZE)
            cache[str(start)] = plan.model_dump()
            _save_cache(cache_path, fingerprint, cache)
            time.sleep(CALL_DELAY_SECS)
        wanted = set(batch)
        for action in plan.actions:
            if action.line in wanted:
                decided[action.line] = action
        drop_ranges += [r for r in plan.drop_ranges if len(r) == 2 and r[0] <= r[1]]
        missing = wanted - decided.keys()
        if missing:
            logger.warning("%s: %d candidates without an action in batch %d; kept as-is",
                           party, len(missing), start // BATCH_SIZE)
        logger.info("%s: planned %d/%d candidates", party, len(decided), len(candidates))

    return StructurePlan(actions=list(decided.values()), drop_ranges=drop_ranges)


# ---------------------------------------------------------------------------
# Apply + verify
# ---------------------------------------------------------------------------

_WORD_RE = re.compile(r"\w+", re.UNICODE)


def _words(text: str) -> Counter:
    return Counter(w.lower() for w in _WORD_RE.findall(text))


def _safe_title(original: str, proposed: Optional[str]) -> str:
    """Use the LLM's cleaned title only if it adds no word and keeps the section number."""
    if not proposed or _words(proposed) - _words(original):
        return original
    number = _SECTION_NUMBER_RE.match(original)
    if number and not proposed.strip().startswith(number.group(0)):
        return original
    return proposed.strip()


def _demote(text: str) -> str:
    """Header text back to body: numbered measures become list items."""
    m = _NUMBERED_RE.match(text)
    if m:
        bold = m.group(1) or ""
        return f"{m.group(2)}. {bold}{text[m.end():]}"
    return text


def apply_plan(lines: List[str], plan: StructurePlan) -> str:
    dropped = set()
    for a, b in plan.drop_ranges:
        # Cover + índice is a small slice of a manifesto; a wide range is the
        # model dropping programme text, which is the one thing it must not do.
        if b - a + 1 > MAX_DROP_RANGE_FRACTION * len(lines):
            logger.warning("Ignoring drop range L%d-L%d: wider than %.0f%% of the document",
                           a, b, 100 * MAX_DROP_RANGE_FRACTION)
            continue
        logger.info("Dropping L%d-L%d: %s ...", a, b, lines[a][:60] if a < len(lines) else "")
        dropped.update(range(a, b + 1))
    actions = {a.line: a for a in plan.actions}

    out: List[str] = []
    for i, line in enumerate(lines):
        if i in dropped:
            continue
        act = actions.get(i)
        if act is None:
            out.append(line)
        elif act.action == "drop":
            continue
        elif act.action == "header" and act.level:
            title = _safe_title(_strip_marker(line), act.title and _unbold(act.title))
            out.append(f"{'#' * act.level} {title}")
        else:  # body
            m = _HEADER_RE.match(line)
            out.append(_demote(m.group(2).strip()) if m else line)

    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


def verify(raw: str, clean: str) -> None:
    """Fail if the clean text contains any word the raw text does not."""
    extra = _words(clean) - _words(raw)
    if extra:
        raise ValueError(f"cleaner introduced words not in the source: {dict(extra.most_common(10))}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def clean_markdown(raw_path: str, out_dir: Optional[str] = None, model: Optional[str] = None) -> str:
    """Clean one raw markdown file into ``<markdown_data>/<party>/<stem>-clean.md``."""
    stem = os.path.splitext(os.path.basename(raw_path))[0]
    party = stem.split("-")[0]
    out_dir = out_dir or os.path.join(str(config.get("paths.markdown_data", "data/1_markdown")), party)

    with open(raw_path, encoding="utf-8") as fh:
        raw = fh.read()
    lines = prepare(raw)
    cache_path = os.path.join(
        str(config.get("paths.processed_data", "data/2_processed")), "cleaner-cache", f"{stem}-plan.json"
    )
    plan = plan_structure(lines, party, model=model, cache_path=cache_path)
    clean = apply_plan(lines, plan)
    # Against the prepared text, not the raw file: rejoining "armaze-" + "namento"
    # legitimately creates a word. The deterministic pass is covered by unit tests;
    # this check guards the LLM step.
    verify("\n".join(lines), clean)

    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{stem}-clean.md")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(clean)

    n_headers = sum(1 for line in clean.split("\n") if _HEADER_RE.match(line))
    logger.info("%s: %d -> %d lines, %d headers -> %s",
                party, len(raw.split("\n")), len(clean.split("\n")), n_headers, out_path)
    return out_path
