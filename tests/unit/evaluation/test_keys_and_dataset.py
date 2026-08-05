import os

import pytest

from src.rag.evaluation.dataset import _allocate, load_dataset, save_dataset
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
def test_allocate_splits_evenly_with_remainder():
    alloc = _allocate(10, ["single_party", "comparison", "topic_exploration", "general"])
    assert sum(alloc.values()) == 10
    # remainder distributed to the first types
    assert alloc["single_party"] == 3 and alloc["general"] == 2
    assert _allocate(0, ["a"]) == {"a": 0}
    assert _allocate(5, []) == {}


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
