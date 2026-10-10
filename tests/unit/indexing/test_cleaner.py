import pytest

from src.rag.indexing.cleaner import (
    LineAction,
    StructurePlan,
    apply_plan,
    fix_bullets,
    prepare,
    verify,
)

RAW = """**FUTURO contrato com o**

# <span id="page-3-0"></span>Programa do LIVRE | Legislativas 2024 **Saúde**

O SNS precisa de investimento.

# **7 Assegurar a proteção social**, através de:

- medidas concretas;

**12**

## Por isso defendemos:

Texto final.
"""


def test_apply_plan_relevels_demotes_and_drops():
    lines = prepare(RAW)
    idx = {line: i for i, line in enumerate(lines)}
    title_line = next(i for i, line in enumerate(lines) if "Saúde" in line)
    plan = StructurePlan(
        actions=[
            LineAction(line=idx["**FUTURO contrato com o**"], action="drop"),
            LineAction(line=title_line, action="header", level=2, title="Saúde"),
            LineAction(line=idx["# **7 Assegurar a proteção social**, através de:"], action="body"),
            LineAction(line=idx["## Por isso defendemos:"], action="header", level=3),
        ]
    )
    clean = apply_plan(lines, plan)
    assert clean == (
        "## Saúde\n\n"
        "O SNS precisa de investimento.\n\n"
        "7. **Assegurar a proteção social**, através de:\n\n"
        "- medidas concretas;\n\n"
        "### Por isso defendemos:\n\n"
        "Texto final.\n"
    )
    verify(RAW, clean)


def test_invented_title_is_rejected_and_verify_catches_new_words():
    lines = prepare(RAW)
    i = next(i for i, line in enumerate(lines) if "Saúde" in line)
    clean = apply_plan(lines, StructurePlan(actions=[LineAction(line=i, action="header", level=2, title="Saúde Pública")]))
    assert "Pública" not in clean  # falls back to the original title
    with pytest.raises(ValueError):
        verify(RAW, clean + "\nPalavra inventada\n")
    # A cleaned title must also keep its section number.
    plan = StructurePlan(actions=[LineAction(line=0, action="header", level=3, title="25 de Abril, sempre")])
    assert apply_plan(["#### 1.1. 25 de Abril, sempre", "", "Texto."], plan).startswith("### 1.1. 25 de Abril, sempre")


def test_fix_bullets_converts_and_rejoins_wrapped_bullets():
    lines = [
        "**•Elaborar uma Estratégia Nacional para o armaze-**",
        "",
        "**namento de energia com vista à eletrificação;**",
        "",
        "**•Impedir a instalação, em áreas protegidas ou que**",
        "",
        "### **constituam habitats de espécies protegidas.**",
        "",
        "- **• Eliminar o IMT na compra de habitação**",
        "",
        "Novo parágrafo.",
    ]
    assert fix_bullets(lines) == [
        "- Elaborar uma Estratégia Nacional para o armazenamento de energia com vista à eletrificação;",
        "",
        "- Impedir a instalação, em áreas protegidas ou que constituam habitats de espécies protegidas.",
        "",
        "- Eliminar o IMT na compra de habitação",
        "",
        "Novo parágrafo.",
    ]


def test_with_deadline_abandons_a_hung_call():
    import time

    from src.rag.common.llm_client import with_deadline

    assert with_deadline(lambda: 42, 1) == 42
    with pytest.raises(TimeoutError):
        with_deadline(lambda: time.sleep(5), 0.1)
