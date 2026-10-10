import scripts.judge_validation as jv


def test_cohen_kappa_known_values():
    assert jv.cohen_kappa([True, False, True, False], [True, False, True, False]) == 1.0
    # 50% observed vs 50% chance agreement -> no better than chance
    assert jv.cohen_kappa([True, True, False, False], [True, False, True, False]) == 0.0
    assert jv.cohen_kappa([True, True], [True, True]) is None


def test_parse_sheet_reads_marks_and_relevance(tmp_path):
    sheet = tmp_path / "s.md"
    sheet.write_text(
        "## item-01\n\n**faithfulness** — Is the claim supported by the CONTEXT?\n\n"
        "- [x] a\n- [n] b\n- [ ] c\n\nrelevance: 4\n"
    )
    item = jv.parse_sheet(str(sheet))[1]
    assert item["metrics"]["faithfulness"] == [True, False, None]
    assert item["relevance"] == 4
