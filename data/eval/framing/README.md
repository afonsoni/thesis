# Framing-leakage evidence

Fixed evidence for the framing-leakage count in the thesis (Proposition,
"Grounding and neutrality"). Unlike the run files in `../results/`, these
cannot be regenerated: the annotations would come out different.

- `framing-handcount-20261015-answers.md`: the 122 answers that were annotated,
  from runs `wide-20261013T032701` (before the attribution rule) and
  `current-20261013T140724` (after), shuffled, with blind ids `b001`–`b122`.
- `framing-handcount-20261015.json`: the author's blind annotations of those
  answers against the rubric, matched back to their run and question.
- `framing-human-check.md`: the author's blind marks on a stratified sample of
  20 of them (`h01`–`h20`), with the rubric used.
- `framing-human-check-key.json`: which answer each `hNN` is (`blind_id`) and
  its label in the full count.

Result: 6 of 61 answers with a clear leak both before and after the rule.
