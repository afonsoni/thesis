import pytest

import src.rag.evaluation.metrics.generation as gen
from src.rag.evaluation.judge import ClaimVerdict, JudgeScore
from src.rag.evaluation.models import EvalQuestion, QuestionRun


def _verdicts(*flags):
    return [ClaimVerdict(index=i, supported=f) for i, f in enumerate(flags, 1)]


@pytest.fixture
def fake_judge(monkeypatch):
    calls = {"extract": []}

    def extract(question, text, model=None):
        calls["extract"].append(text)
        return {"ANSWER": ["a1", "a2", "a3"], "REF": ["r1", "r2"]}.get(text, [])

    def verify(claims, evidence, model=None):
        if evidence == "CONTEXT":   # faithfulness: 2 of 3 answer claims grounded
            return _verdicts(True, False, True)
        if evidence == "REF":       # precision vs reference: 1 of 3
            return _verdicts(True, False, False)
        if evidence == "ANSWER":    # recall: 1 of 2 reference claims covered
            return _verdicts(True, False)
        raise AssertionError(evidence)

    monkeypatch.setattr(gen, "extract_claims", extract)
    monkeypatch.setattr(gen, "verify_claims", verify)
    monkeypatch.setattr(gen, "judge_answer_relevance", lambda q, a, m=None: JudgeScore(score=5))
    return calls


@pytest.mark.unit
def test_claim_level_scores(fake_judge):
    q = EvalQuestion(id="q-01", question="Q?", reference_answer="REF")
    run = QuestionRun(question_id="q-01", variant="v", answer="ANSWER", context="CONTEXT")
    s = gen.GenerationJudgeMetric().score(run, q)
    assert s["faithfulness"] == pytest.approx(2 / 3)
    assert s["correctness_recall"] == pytest.approx(1 / 2)
    p, r = 1 / 3, 1 / 2
    assert s["correctness"] == pytest.approx(2 * p * r / (p + r))
    assert s["answer_relevance"] == 1.0
    assert [c["supported"] for c in run.judgements["faithfulness"]] == [True, False, True]


@pytest.mark.unit
def test_reference_claims_extracted_once_across_variants(fake_judge):
    metric = gen.GenerationJudgeMetric()
    q = EvalQuestion(id="q-01", question="Q?", reference_answer="REF")
    for variant in ("naive", "current"):
        metric.score(QuestionRun(question_id="q-01", variant=variant, answer="ANSWER", context="CONTEXT"), q)
    assert fake_judge["extract"].count("REF") == 1


@pytest.mark.unit
def test_no_claims_or_failed_judge_is_omitted_not_zero(fake_judge, monkeypatch):
    q = EvalQuestion(id="q-01", question="Q?")
    run = QuestionRun(question_id="q-01", variant="v", answer="sem afirmações", context="CONTEXT")
    assert "faithfulness" not in gen.GenerationJudgeMetric().score(run, q)
    monkeypatch.setattr(gen, "verify_claims", lambda *a, **k: None)
    run = QuestionRun(question_id="q-01", variant="v", answer="ANSWER", context="CONTEXT")
    assert "faithfulness" not in gen.GenerationJudgeMetric().score(run, q)


@pytest.mark.unit
def test_runner_judges_against_the_generators_own_context():
    from src.rag.common.models import AnalyzedQuery, GeneratedAnswer, RetrievalResult, SearchResult
    from src.rag.evaluation.runner import run_question
    from src.rag.retrieval.config import RetrievalConfig

    result = RetrievalResult(query=AnalyzedQuery(original_query="Q?"),
                             results=[SearchResult(id="1", content="child", parent_content="PARENT")])
    run = run_question(
        EvalQuestion(id="q-01", question="Q?"), RetrievalConfig(name="v"), [], 5,
        retrieve_fn=lambda q, c: result,
        generate_fn=lambda r: GeneratedAnswer(answer="A", context="[1] PARENT"),
    )
    assert run.context == "[1] PARENT"
