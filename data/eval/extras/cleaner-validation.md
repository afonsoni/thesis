# Cleaner validation (for the Proposition's cleaning TODO)

`python scripts/validate_cleaner.py`, run 2026-10-22 on the frozen code
(`code-freeze`, `0293a0b`) with `google/gemma-4-26b-a4b-it`, about 24 LLM calls.
It re-cleans the raw parser output of the four parties that were also cleaned by
hand, and compares the LLM-cleaned file with the hand-cleaned one.

| party | headers raw / clean / manual | title F1 raw → clean | title+level F1 raw → clean | title+level F1, best level shift | word recall | word precision |
|---|---|---|---|---|---|---|
| ad | 238 / 199 / 218 | 0.95 → 0.95 | 0.20 → 0.17 | 0.38 | 0.984 | 0.997 |
| livre | 159 / 101 / 60 | 0.31 → 0.30 | 0.05 → 0.06 | 0.22 | 0.998 | 0.985 |
| pcp | 301 / 178 / 224 | 0.58 → 0.28 | 0.03 → 0.17 | 0.17 | 1.000 | 0.972 |
| ps | 163 / 130 / 138 | 0.92 → 0.94 | 0.23 → 0.22 | 0.73 | 0.999 | 0.994 |

- **Word recall**: share of the hand-cleaned text's words that the LLM-cleaned
  file keeps. Low would mean the cleaner dropped programme text.
- **Word precision**: share of the LLM-cleaned file's words that the
  hand-cleaned file also has. Low would mean junk the manual pass removed is
  still there.
- **Title F1**: do both files have the same section titles? **Title+level F1**:
  …at the same depth? The best-shift column forgives a whole document being
  nested one level deeper or shallower.

## What it says

- **The text survives.** The cleaner keeps 98.4–100% of the words a human kept,
  and leaves 0.3–2.8% of words a human removed. By construction it cannot add
  words: its output is rejected if it contains any word the source did not.
- **The heading hierarchy does not match a human's.** Titles agree well for AD
  and PS (0.94–0.95) and poorly for LIVRE and PCP (0.28–0.30), and depths
  barely agree anywhere (title+level F1 0.06–0.22). For PCP the cleaner moved
  the titles further from the manual file than the raw output was (0.58 →
  0.28).
- **The manual files are one person's choices, not ground truth.** The LIVRE
  manual pass flattened the document to 60 headings, against 159 in the raw
  output and 101 after the LLM pass, so a low title F1 there partly measures how
  much the hand cleaning removed.
- For retrieval the hierarchy matters less than the text: the chunker splits on
  every heading level alike, and depth only changes the section path shown in
  chunk headers and answers.
