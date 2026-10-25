# Dev-only re-check of the decisions judged on all 61 questions

`python scripts/eval_extras/dev_only_recheck.py`. Paired differences (candidate minus
baseline) with 95% bootstrap intervals over questions, from the stored runs; `*` means
the interval excludes zero. Only answerable questions carry these metrics.

## Contextual retrieval: plain hybrid index to LLM context (524d9ea, two passes)

| metric | all 61 | dev | test |
|---|---|---|---|
| recall | +0.046* [+0.010, +0.086] (n=53) | +0.034 [-0.004, +0.074] (n=22) | +0.055 [-0.000, +0.118] (n=31) |
| mrr | +0.082* [+0.027, +0.139] (n=53) | +0.021 [-0.053, +0.104] (n=22) | +0.126* [+0.055, +0.200] (n=31) |
| ndcg | +0.057* [+0.023, +0.093] (n=53) | +0.032 [-0.003, +0.075] (n=22) | +0.075* [+0.024, +0.131] (n=31) |

## Section headers only: plain hybrid index to headers (524d9ea, two passes)

| metric | all 61 | dev | test |
|---|---|---|---|
| recall | +0.026* [+0.000, +0.049] (n=53) | +0.031 [-0.003, +0.069] (n=22) | +0.022 [-0.012, +0.057] (n=31) |
| ndcg | +0.031* [+0.007, +0.053] (n=53) | +0.038* [+0.003, +0.075] (n=22) | +0.025 [-0.005, +0.056] (n=31) |

## Wider net: 5 / 5 with the topic filter to 10 / 8 without it (b054bf8)

| metric | all 61 | dev | test |
|---|---|---|---|
| recall | +0.123* [+0.078, +0.170] (n=53) | +0.141* [+0.078, +0.219] (n=22) | +0.110* [+0.057, +0.171] (n=31) |
| ndcg | +0.067* [+0.031, +0.101] (n=53) | +0.063* [+0.023, +0.112] (n=22) | +0.069* [+0.020, +0.118] (n=31) |
| correctness | +0.041* [+0.008, +0.072] (n=53) | +0.033 [-0.018, +0.087] (n=22) | +0.047* [+0.005, +0.088] (n=31) |
| correctness_recall | +0.102* [+0.044, +0.167] (n=53) | +0.131* [+0.047, +0.230] (n=22) | +0.081* [+0.007, +0.161] (n=31) |
| faithfulness | -0.013 [-0.039, +0.008] (n=53) | +0.012 [-0.009, +0.033] (n=22) | -0.030 [-0.069, +0.000] (n=31) |

## Prompt budget: 32k to 64k (b054bf8)

| metric | all 61 | dev | test |
|---|---|---|---|
| correctness | -0.014 [-0.042, +0.016] (n=52) | -0.025 [-0.064, +0.016] (n=22) | -0.005 [-0.045, +0.034] (n=30) |
| correctness_recall | -0.015 [-0.052, +0.022] (n=53) | -0.034 [-0.083, +0.015] (n=22) | -0.002 [-0.051, +0.050] (n=31) |
| faithfulness | +0.010 [-0.012, +0.036] (n=53) | +0.003 [-0.014, +0.019] (n=22) | +0.015 [-0.019, +0.058] (n=31) |

## What it says

- **The wider net would have been chosen on dev alone**, and more clearly
  there than on test (recall +0.141 against +0.110).
- **The 64k budget loses on every split.** Note that commit `b054bf8` quoted
  correctness +0.029 for 64k: that is its gain over `shallow` (5 / 5 with the
  filter), to be read against 32k's +0.041 over the same baseline. Compared
  directly with 32k it is −0.014.
- **Contextual retrieval is the one leak.** On dev it points the same way but
  both recall and nDCG intervals touch zero; most of its all-61 significance
  came from the test questions (MRR +0.126 on test, +0.021 on dev). Its gain
  reported on test is therefore not independent of the decision.
- **q-59** (a test question, one of the four unanswerable) motivated the
  out-of-corpus refusal (`ec100e3`). A bug fix rather than tuning, but the
  abstention count on test includes it.
- Every decision not listed here (hybrid default, reranker, `lexical_wide`,
  the topic-filter diagnosis) was taken on dev runs.
