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

# Appended before "Perguntas reformuladas:" under RetrievalConfig.expansion_synonyms.
# No worked example on purpose: any example would be a gold-set question.
QUERY_EXPANSION_SYNONYMS = """\
Em pelo menos metade das versões, troca as palavras-chave da pergunta pelos \
sinónimos e termos formais ou técnicos que um programa eleitoral usaria."""

# ---------------------------------------------------------------------------
# Query analysis (Part 10/11 – structured query understanding)
# ---------------------------------------------------------------------------

# With what each topic covers, as the classifier sees it: from the bare names the
# analyzer cannot know that "canábis" is filed under saude and justica, and
# answered "outros" (or a wrong neighbour) where the chunks carry a real topic.
_topic_list = "\n".join(f'- "{t}": {d}' for t, d in TOPIC_CATEGORIES.items())

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

Tópicos disponíveis (e o que cada um abrange):
{_topic_list}

Analisa a pergunta do utilizador e extrai informação estruturada."""

QUERY_ANALYSIS_PROMPT = """\
Pergunta: {question}

Analisa esta pergunta e responde em JSON com os seguintes campos:
- "parties": lista de partidos a consultar, com os nomes exactos da lista acima.
  Se a pergunta se referir a um bloco em vez de nomear partidos ("os partidos de
  direita", "os conservadores", "a esquerda"), enumera os partidos desse bloco.
  Lista vazia quando a pergunta não restringe a nenhum partido em concreto.
- "unlisted_parties": partidos nomeados na pergunta que não estão na lista acima.
  Nunca substituas um partido destes por um da lista, mesmo que o nome ou a sigla
  se pareçam: vai para aqui, não para "parties". Lista vazia se não houver nenhum.
- "coverage": "exhaustive" se a resposta tiver de representar todos os partidos
  em causa (por exemplo "o que defende cada partido sobre X", "compara os
  partidos de direita quanto a Y"); "best_match" se bastarem as passagens mais
  relevantes, venham de onde vierem.
- "topics": os tópicos sob os quais estariam classificadas as passagens que
  respondem à pergunta, segundo as descrições acima. A pesquisa filtra por eles:
  um tópico errado esconde a resposta, um em falta só alarga a pesquisa, por isso
  inclui apenas os que encaixam claramente (normalmente 1 ou 2). Um tema que
  atravessa várias áreas recebe as áreas onde as medidas caem ("cuidadores
  informais" -> ["seguranca_social", "trabalho"]). Se a pergunta é sobre um tema
  de políticas que nenhum tópico cobre, usa ["outros"]. Lista vazia se a pergunta
  pede uma definição ou um dado factual ("O que é o Simplex?"), não propostas.
- "answer_shape": "per_party" se a resposta deve ser organizada partido a partido;
  "narrative" se deve ser um texto único — inclusive quando a pergunta pede um
  veredicto ("que partido propõe mais sobre habitação?"), que exige consultar
  todos os partidos mas responder de uma só vez.
- "reformulated_query": versão limpa e clara da pergunta para pesquisa semântica"""
