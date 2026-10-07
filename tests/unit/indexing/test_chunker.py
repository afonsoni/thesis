import pytest

from src.rag.indexing.chunker import chunk_markdown


@pytest.mark.unit
class TestChunker:
    SAMPLE_MD = """# Programa do Partido X

## Economia

### Fiscalidade

Propomos reduzir o IRS para os escaloes mais baixos e simplificar o sistema tributario.
As empresas beneficiarao de uma reducao do IRC para promover o investimento.

### Emprego

Criacao de programas de formacao profissional para jovens desempregados.
Reforco do salario minimo nacional para 1000 euros.

## Saude

Reforco do SNS e contratacao de mais profissionais de saude.
Construcao de novos centros de saude nas areas metropolitanas.
"""

    def test_chunk_count(self):
        chunks = chunk_markdown(self.SAMPLE_MD, "ps-2024.md")
        assert len(chunks) > 0

    def test_party_metadata(self):
        chunks = chunk_markdown(self.SAMPLE_MD, "ps-2024.md")
        for chunk in chunks:
            assert chunk.party_name == "Partido Socialista"
            assert chunk.ideology == "left"
            assert chunk.year == 2024

    def test_small_chunks_filtered(self):
        tiny_md = "# Title\n\nOk\n\n## Section\n\nToo small"
        chunks = chunk_markdown(tiny_md, "test.md")
        for chunk in chunks:
            assert chunk.size > 50

    def test_windowed_splitting(self):
        long_text = "Esta e uma proposta importante. " * 200
        big_md = f"# Programa\n\n## Seccao grande\n\n{long_text}"
        chunks = chunk_markdown(big_md, "ad-2024.md", max_chunk_size=500)
        assert len(chunks) > 1
        assert any(chunk.chunk_type == "windowed" for chunk in chunks)


@pytest.mark.unit
def test_bounded_parent_keeps_small_sections_whole_and_windows_big_ones():
    from src.rag.indexing.chunker import _bounded_parent, _locate

    content = "aaaa bbbb cccc dddd eeee"
    pieces = ["aaaa bbbb", "bbbb cccc", "cccc dddd", "dddd eeee"]  # overlapping, like the splitter
    spans = _locate(content, pieces)
    assert spans == [(0, 9), (5, 14), (10, 19), (15, 24)]

    # Section fits the cap: the whole section is the parent.
    assert _bounded_parent(content, pieces, spans, 1, len, 100) == content
    # Section over the cap: the child plus neighbours, cut from the section text.
    parent = _bounded_parent(content, pieces, spans, 2, len, 14)
    assert "cccc dddd" in parent and len(parent) <= 14
    assert parent in content
    # Unlocatable pieces fall back to the child itself.
    assert _bounded_parent(content, pieces, None, 2, len, 14) == "cccc dddd"
