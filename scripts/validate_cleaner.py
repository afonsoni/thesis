"""
Score `main.py clean` against the hand-made *-manual.md files.

For every party that has a manual file, clean its raw marker output into a
scratch directory and compare:

- header F1 (title only): did the cleaner keep the same set of section titles?
- header F1 (title + level): ... at the same depth?
- word recall: share of the manual text's words present in the clean text
  (low = the cleaner dropped programme text);
- word precision: share of the clean text's words present in the manual text
  (low = junk the manual pass removed is still there).

Usage: python scripts/validate_cleaner.py [--out-dir DIR] [--model MODEL] [--skip-clean]
"""

import argparse
import glob
import logging
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv  # noqa: E402

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

from src.rag.indexing.cleaner import _HEADER_RE, _words, clean_markdown  # noqa: E402

MD = "data/1_markdown"


def _norm(title: str) -> str:
    return " ".join(w.lower() for w in re.findall(r"\w+", re.sub(r"</?span[^>]*>", "", title)))


def headers(text: str) -> Counter:
    out = Counter()
    for line in text.split("\n"):
        m = _HEADER_RE.match(line)
        if m:
            out[(_norm(m.group(2)), len(m.group(1)))] += 1
    return out


def f1(pred: Counter, gold: Counter) -> float:
    tp = sum((pred & gold).values())
    if not tp:
        return 0.0
    p, r = tp / sum(pred.values()), tp / sum(gold.values())
    return 2 * p * r / (p + r)


def shifted_f1(pred: Counter, gold: Counter) -> float:
    """Title+level F1 under the best constant level shift (manual files nest
    one level deeper or shallower without the hierarchy being different)."""
    return max(f1(Counter({(t, lv + k): n for (t, lv), n in pred.items()}), gold) for k in range(-2, 3))


def titles(c: Counter) -> Counter:
    out = Counter()
    for (t, _), n in c.items():
        out[t] += n
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default="data/2_processed/cleaner-validation")
    ap.add_argument("--model", default=None)
    ap.add_argument("--skip-clean", action="store_true", help="Score existing outputs only")
    args = ap.parse_args()

    rows = []
    for manual_path in sorted(glob.glob(os.path.join(MD, "*", "*-manual.md"))):
        stem = os.path.basename(manual_path).replace("-manual.md", "")
        party = stem.split("-")[0]
        raw_path = os.path.join(MD, "_raw", party, f"{stem}.md")
        clean_path = os.path.join(args.out_dir, f"{stem}-clean.md")
        if not args.skip_clean:
            clean_path = clean_markdown(raw_path, out_dir=args.out_dir, model=args.model)
        elif not os.path.exists(clean_path):
            continue

        raw, clean, manual = (open(p, encoding="utf-8").read() for p in (raw_path, clean_path, manual_path))
        hc, hm, hr = headers(clean), headers(manual), headers(raw)
        wc, wm = _words(clean), _words(manual)
        rows.append((
            party,
            sum(hr.values()), sum(hc.values()), sum(hm.values()),
            f1(titles(hr), titles(hm)), f1(titles(hc), titles(hm)),
            f1(hr, hm), f1(hc, hm), shifted_f1(hc, hm),
            sum((wc & wm).values()) / sum(wm.values()),
            sum((wc & wm).values()) / sum(wc.values()),
        ))

    print("| party | headers raw/clean/manual | title F1 raw→clean | title+level F1 raw→clean | +level, best shift | word recall | word precision |")
    print("|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r[0]} | {r[1]}/{r[2]}/{r[3]} | {r[4]:.2f} → {r[5]:.2f} | {r[6]:.2f} → {r[7]:.2f} | {r[8]:.2f} | {r[9]:.3f} | {r[10]:.3f} |")


if __name__ == "__main__":
    main()
