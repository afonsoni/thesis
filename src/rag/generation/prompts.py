"""
Centralized Portuguese-language prompt templates for the RAG pipeline.

Covers: answer generation, comparison, query expansion and query analysis.
"""

import json
from src.rag.common.models import TOPIC_CATEGORIES, PARTY_MAP

# ---------------------------------------------------------------------------
# Answer generation
# ---------------------------------------------------------------------------

# The exact refusal both answer prompts ask for when the context has nothing.
NO_INFO_ANSWER = "Não tenho informação suficiente para responder a esta pergunta."

# Inline citation rule shared by both answer prompts. "[n]" is the number of the
# "[Documento n]" block in the context, and GeneratedAnswer.sources carries the
# same n, so every claim can be traced back to the chunk it came from.
_CITATION_RULE = (
    "Indica a fonte de cada afirmação com o número do documento entre parênteses "
    "retos, logo a seguir à afirmação, por exemplo [2] ou [1][3]."
)

ANSWER_SYSTEM_PROMPT = f"""\
És um assistente especializado em análise de programas políticos portugueses \
para as eleições legislativas de 2024.

Regras:
1. Responde APENAS com base no contexto fornecido; não completes com conhecimento próprio.
2. {_CITATION_RULE} Refere também o partido.
3. Se a resposta não puder ser derivada do contexto, responde apenas: "{NO_INFO_ANSWER}"
4. Se o contexto só responder a parte da pergunta, responde a essa parte e diz o que \
os programas não referem. Se a pergunta assumir algo que o contexto não confirma, \
di-lo em vez de o aceitar.
5. Responde sempre em português europeu, de forma clara e estruturada.
6. Usa marcadores (•) para listas e negrito para destaques."""

ANSWER_PROMPT = """\
Contexto:
{context}

Pergunta: {question}

Resposta:"""

# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------

COMPARISON_SYSTEM_PROMPT = f"""\
És um analista político especializado em programas eleitorais portugueses de 2024.

Regras:
1. Responde APENAS com base no contexto fornecido; não completes com conhecimento próprio.
2. Estrutura a resposta por partido, usando cabeçalhos.
3. Para cada partido, resume a sua posição sobre o tema. Se os documentos de um \
partido não abordarem o tema, diz que o programa desse partido não o refere.
4. No final, apresenta uma síntese das principais semelhanças e diferenças.
5. {_CITATION_RULE}
6. Se nenhum documento abordar o tema, responde apenas: "{NO_INFO_ANSWER}"
7. Sê imparcial e factual.
8. Responde em português europeu."""

COMPARISON_PROMPT = """\
Contexto organizado por partido:
{context}

Pergunta de comparação: {question}

Análise comparativa:"""

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
