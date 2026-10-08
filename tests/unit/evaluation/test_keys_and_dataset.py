import os

import pytest

from src.rag.evaluation.dataset import load_dataset, save_dataset
from src.rag.evaluation.keys import chunk_key, normalize_content
from src.rag.evaluation.models import EvalDataset, EvalQuestion


@pytest.mark.unit
def test_chunk_key_stable_across_whitespace_and_form():
    a = chunk_key("O LIVRE   propõe\n\nhabitação.")
    b = chunk_key("O LIVRE propõe habitação.")
    assert a == b
    assert a.startswith("sha1:")


@pytest.mark.unit
def test_normalize_content_collapses_whitespace():
    assert normalize_content("  a\t b\n c ") == "a b c"


@pytest.mark.unit
def test_dataset_round_trip_and_curated_filter(tmp_path):
    ds = EvalDataset(questions=[
        EvalQuestion(id="q-0001", question="A?", query_type="single_party",
                     expected_parties=["LIVRE"], gold_chunk_keys=[chunk_key("abc")],
                     reference_answer="R", curated=True),
        EvalQuestion(id="q-0002", question="B?", curated=False),
    ])
    path = os.path.join(tmp_path, "ds.json")
    save_dataset(ds, path)

    loaded = load_dataset(path)
    assert len(loaded.questions) == 2
    assert loaded.questions[0].id == "q-0001"
    assert loaded.questions[0].gold_chunk_keys == [chunk_key("abc")]

    curated = loaded.curated_only()
    assert len(curated.questions) == 1 and curated.questions[0].id == "q-0001"


@pytest.mark.unit
def test_split_filter_keeps_only_that_split():
    ds = EvalDataset(questions=[
        EvalQuestion(id="q-01", question="A?", split="test"),
        EvalQuestion(id="q-02", question="B?", split="dev"),
        EvalQuestion(id="q-03", question="C?"),
    ])
    assert [q.id for q in ds.with_split("test").questions] == ["q-01"]
    assert [q.id for q in ds.with_split("dev").questions] == ["q-02"]
