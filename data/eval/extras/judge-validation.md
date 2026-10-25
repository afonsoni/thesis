# Judge validation (for the Proposition's judge TODO)

Is the LLM judge (`qwen/qwen3.8-27b`, temperature 0, reasoning off) a sound
instrument? Two blind rating sheets, rated claim by claim, compared with the
judge's verdicts by `scripts/judge_validation.py score`. Done 2026-10-25.

## Setup

- **Sheet 1, the system as it runs** (`data/eval/validation/judge-sheet.md`).
  25 of the 32 judged answers of `current` in the headline test run
  (`current-20261020T044840.json`, code `0293a0b`), drawn at random (seed 0),
  with every claim the judge ruled on: 553 faithfulness claims, 535
  correctness-recall claims and 25 relevance scores.
- **Sheet 2, planted negatives** (`judge-noret-sheet.md`). On sheet 1 almost
  every claim is supported, so it cannot show whether the judge catches
  unsupported ones. Sheet 2 takes 12 closed-book answers (`no_retrieval`, same
  test run, same code), gives each the context `current` retrieved for the same
  question, and has the production judge rule on their faithfulness against it
  (`judge_validation.py borrow`). That yields 194 faithfulness claims, half of
  them unsupported, picked without looking at the judge's verdicts. Recall (257
  claims) and relevance come from the original `no_retrieval` run. All 12
  questions also appear on sheet 1.
- **Raters.** The reference labels were rated blindly by the author.
  `ratings.json` and `ratings-judge-noret.json` hold the final labels, and
  `ratings-notes.json` / `ratings-judge-noret-notes.json` hold the rater's notes
  on every borderline call.

## Agreement with the judge

| sheet | metric | claims (answers) | agreement | Cohen's κ | PABAK | answer-level ρ |
|---|---|---|---|---|---|---|
| 1 | faithfulness | 553 (25) | 98.9% | 0.57 | 0.98 | 0.65 |
| 1 | correctness recall | 535 (25) | 95.0% | 0.90 | 0.90 | 0.95 |
| 1 | relevance (1–5) | (25) | 68% exact, 100% within 1 | – | – | 0.59 |
| 2 | faithfulness | 194 (12) | 80.9% | 0.62 | 0.62 | 0.59 |
| 2 | correctness recall | 257 (12) | 92.6% | 0.67 | 0.85 | 0.66 |

Faithfulness verdicts side by side (reference label first):

| sheet | both supported | both unsupported | ref. unsupported, judge passed | ref. supported, judge flagged |
|---|---|---|---|---|
| 1 | 543 | 4 | 3 | 3 |
| 2 | 90 | 67 | 8 | 29 |

## What it says

1. **Correctness recall is a sound instrument.** κ 0.90 on the real system. The disagreements are about
   qualifiers, such as "118.000" stated without "sem contar com os
   indocumentados". In 22 of the 27 the judge says "not stated" where the rater
   says "stated", so the judge's recall (0.56) slightly underestimates the
   rater's (0.59).
2. **The judge catches unsupported claims.** On sheet 2 it flags 67 of the 75
   claims the reference marks unsupported (89%), and 67 of its 96 flags (70%)
   are ones the reference agrees with. Pooled over both sheets: 71 of 82
   (87%). Most of its extra flags reject an embellishment whose core is in the
   context ("principal motor", "progressiva", "extraordinário", "crueldade"), a
   strict reading that is often defensible.
3. **On the real system faithfulness sits at the ceiling.** Rater and judge
   both find 99% of claims supported, and 6 disagreements out of 553 give κ
   only 0.57 (the prevalence paradox; PABAK 0.98). Two consequences. The
   generator is genuinely grounded, which is a finding about the system and
   not a lenient judge (point 2). And faithfulness barely separates rungs, so
   it works as a floor, not as a ranking.
4. **The judge errs on the strict side.** Most disagreements are the judge
   being stricter than the rater: 22 of 27 on sheet 1 recall, 16 of 19 on
   sheet 2 recall, 29 of 37 on sheet 2 faithfulness (sheet 1 faithfulness
   splits 3 and 3). Generation scores are therefore, if anything, slightly
   pessimistic rather than inflated.
5. **Weak spot: claims about absence.** Sheet 1 item 3 (q-49) is a refusal, yet
   the judge credited it with the reference claim "Nenhum outro programa indica
   [2016]"; item 13 (q-47, "Nenhum outro programa indica quantos imigrantes")
   is similar, if more arguable, since that answer cites only CHEGA. On sheet 2 item 6 (q-49) the judge passed "os programas não
   indicam o ano" while its own stated reason cites PCP's 2016. This lines up
   with Limitations (c) existence questions and (e) one-sided questions.
6. **Relevance measures being on topic, not being right.** The judge gives 5 to
   22 of 25 real answers (the rater 15) and to 10 of 12 closed-book answers
   whose recall is about 0.10. Use it for `abstention` and `false_refusal`,
   which read its `abstained` flag, and never to rank rungs. Sheet 2's
   relevance agreement (8% exact) is not a fair comparison, because the
   rater marked mostly-wrong answers down, which the sheet's rubric does not
   ask for.

## Examples worth quoting

- **A slip the judge missed** (sheet 1 item 6, q-06). The manifesto lists
  "incapacidade activa para desempenho de cargos públicos ou sujeição a
  sufrágio" (barred from standing for election). The answer turned it into a
  sanction called "sujeição a sufrágio", and the judge passed it.
- **False refusals with the evidence in hand.** q-49 (PCP's 2016 reposition of
  the 35 hours is in Doc 5) and q-56 (CHEGA's professionalisation and
  recruitment proposals are in the context). This is a generation failure, not
  a retrieval one.
- **A wrong absence claim** (sheet 1 item 18, q-51). The answer says PAN does
  not mention euthanasia, while Doc 24 of its context is PAN calling for the
  law's regulation. The judge flagged it.
- **The judge misreading a number** (sheet 2 item 3, q-24). It rejected "o PCP
  propõe a redução do IRC para as PME" because, in its reason, the new 12.5%
  bracket for small firms is "an increase", when it lowers their rate.

## Caveats

- Sheet 1 is one variant (`current`). Sheet 2's context is borrowed, which is
  realistic for faithfulness (is the claim in this text?) but not a
  production situation.
- 25 + 12 answers, and the same 12 questions on both sheets.
- One rater (the author), so no inter-rater agreement can be reported.

## Reproduce

`export` and `borrow` rewrite the files in `data/eval/validation/`; only
`score` is safe to rerun as is.

```bash
python scripts/judge_validation.py export data/eval/results/current-20261020T044840.json --n 25
python scripts/judge_validation.py borrow data/eval/results/no_retrieval-20261020T055138.json \
    --context-from data/eval/results/current-20261020T044840.json --n 12
python scripts/judge_validation.py export data/eval/validation/no_retrieval-borrowed.json --n 12 --name judge-noret
python scripts/judge_validation.py score --ratings data/eval/validation/ratings.json
python scripts/judge_validation.py score --name judge-noret --ratings data/eval/validation/ratings-judge-noret.json
```

`borrow` calls the judge again, so its verdicts can drift slightly between runs;
the frozen ones are in `data/eval/validation/no_retrieval-borrowed.json` and
`judge-noret-key.json`.
