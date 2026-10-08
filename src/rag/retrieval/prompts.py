"""
Portuguese prompt templates for the retrieval stage: multi-query expansion and
structured query analysis.
"""

from src.rag.common.models import TOPIC_CATEGORIES, PARTY_MAP

# ---------------------------------------------------------------------------
# Multi-query expansion (Part 5 – overcome similarity search limitations)
# ---------------------------------------------------------------------------

QUERY_EXPANSION_PROMPT = """\
És um assistente que gera múltiplas reformulações de perguntas sobre \
programas políticos portugueses para melhorar a pesquisa por similaridade.

Pergunta original: {question}

Gera {n_queries} versões diferentes da pergunta, cada uma com perspetiva \
ou vocabulário diferente, para maximizar a cobertura de documentos relevantes.
Mantém todas as perguntas em português europeu.
Separa as perguntas por novas linhas. Não numeres as perguntas.

Perguntas reformuladas:"""

# ---------------------------------------------------------------------------
# Query analysis (Part 10/11 – structured query understanding)
# ---------------------------------------------------------------------------

_topic_list = ", ".join(f'"{t}"' for t in TOPIC_CATEGORIES.keys())

# Positions on the conventional economic left-right axis, stated here rather
# than left to the model's own beliefs about Portuguese politics. The analyzer
# resolves bloc language ("os partidos de direita", "os conservadores") into an
# explicit party list, so this table is what that resolution runs on: keeping it
# in one visible place makes the mapping auditable and citable — these follow
# the Chapel Hill Expert Survey's placement of the Portuguese parties — instead
# of burying a contested judgement in a metadata filter.
_party_positions = "\n".join(
    f'- "{info["name"]}": {"esquerda" if info["ideology"] == "left" else "direita"}'
    for info in PARTY_MAP.values()
)

QUERY_ANALYSIS_SYSTEM_PROMPT = f"""\
És um especialista em análise de perguntas sobre programas políticos portugueses \
para as eleições legislativas de 2024.

Partidos disponíveis (e posição no eixo esquerda-direita):
{_party_positions}

Tópicos disponíveis: {_topic_list}

Analisa a pergunta do utilizador e extrai informação estruturada."""

QUERY_ANALYSIS_PROMPT = """\
Pergunta: {question}

Analisa esta pergunta e responde em JSON com os seguintes campos:
- "parties": lista de partidos a consultar, com os nomes exactos da lista acima.
  Se a pergunta se referir a um bloco em vez de nomear partidos ("os partidos de
  direita", "os conservadores", "a esquerda"), enumera os partidos desse bloco.
  Lista vazia quando a pergunta não restringe a nenhum partido em concreto.
- "coverage": "exhaustive" se a resposta tiver de representar todos os partidos
  em causa (por exemplo "o que defende cada partido sobre X", "compara os
  partidos de direita quanto a Y"); "best_match" se bastarem as passagens mais
  relevantes, venham de onde vierem.
- "topics": lista de tópicos relevantes da lista disponível (lista vazia se nenhum)
- "answer_shape": "per_party" se a resposta deve ser organizada partido a partido;
  "narrative" se deve ser um texto único — inclusive quando a pergunta pede um
  veredicto ("que partido propõe mais sobre habitação?"), que exige consultar
  todos os partidos mas responder de uma só vez.
- "reformulated_query": versão limpa e clara da pergunta para pesquisa semântica"""
