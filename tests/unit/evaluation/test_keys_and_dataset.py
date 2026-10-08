import pytest

from src.rag.evaluation.keys import chunk_key
from src.rag.evaluation.models import EvalDataset, EvalQuestion


@pytest.mark.unit
def test_chunk_key_stable_across_whitespace_and_form():
    a = chunk_key("O LIVRE   propõe\n\nhabitação.")
    b = chunk_key("O LIVRE propõe habitação.")
    assert a == b
    assert a.startswith("sha1:")


@pytest.mark.unit
def test_split_filter_keeps_only_that_split():
    ds = EvalDataset(questions=[
        EvalQuestion(id="q-01", question="A?", split="test"),
        EvalQuestion(id="q-02", question="B?", split="dev"),
        EvalQuestion(id="q-03", question="C?"),
    ])
    assert [q.id for q in ds.with_split("test").questions] == ["q-01"]
    assert [q.id for q in ds.with_split("dev").questions] == ["q-02"]
