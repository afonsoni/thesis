"""
Portuguese-language prompts for the evaluation stage: synthetic gold-set
generation and LLM-as-judge scoring. Kept local to the evaluation package so
retrieval/generation stay independent of it.
"""

# ---------------------------------------------------------------------------
# Dataset generation
# ---------------------------------------------------------------------------

GEN_SINGLE_PROMPT = """\
És um avaliador que cria perguntas de teste para um sistema de perguntas e \
respostas sobre programas políticos portugueses (eleições de 2024).

A partir do EXCERTO abaixo (do programa do partido "{party}"), cria UMA pergunta \
natural em português europeu cuja resposta esteja contida no excerto, e a \
respetiva resposta de referência (curta, factual, baseada apenas no excerto).

A pergunta deve mencionar o partido "{party}" e ser respondível só com este excerto.

EXCERTO:
{content}

Responde em JSON:
{{"question": "...", "reference_answer": "..."}}"""

GEN_GENERAL_PROMPT = """\
És um avaliador que cria perguntas de teste para um sistema de perguntas e \
respostas sobre programas políticos portugueses (eleições de 2024).

A partir do EXCERTO abaixo, cria UMA pergunta natural e geral em português \
europeu (SEM mencionar nenhum partido) cuja resposta esteja no excerto, e a \
respetiva resposta de referência curta.

EXCERTO:
{content}

Responde em JSON:
{{"question": "...", "reference_answer": "..."}}"""

GEN_TOPIC_PROMPT = """\
És um avaliador que cria perguntas de teste sobre programas políticos \
portugueses (eleições de 2024).

Cria UMA pergunta natural em português europeu sobre o tema "{topic}", do tipo \
"que partidos propõem X" ou "o que propõem os partidos sobre X", que possa ser \
respondida usando os excertos abaixo (de vários partidos). Inclui também uma \
resposta de referência curta que sintetize os excertos.

EXCERTOS:
{content}

Responde em JSON:
{{"question": "...", "reference_answer": "..."}}"""

GEN_COMPARISON_PROMPT = """\
És um avaliador que cria perguntas de teste sobre programas políticos \
portugueses (eleições de 2024).

Cria UMA pergunta natural em português europeu que COMPARE os partidos \
"{party_a}" e "{party_b}" sobre o tema "{topic}", respondível com os excertos \
abaixo. Inclui uma resposta de referência curta que contraste as duas posições.

EXCERTO ({party_a}):
{content_a}

EXCERTO ({party_b}):
{content_b}

Responde em JSON:
{{"question": "...", "reference_answer": "..."}}"""

# ---------------------------------------------------------------------------
# LLM-as-judge
# ---------------------------------------------------------------------------

JUDGE_SYSTEM_PROMPT = """\
És um avaliador rigoroso e imparcial de respostas geradas por um sistema de \
perguntas e respostas sobre programas políticos portugueses. Avalias sempre numa \
escala de 1 a 5 e justificas brevemente. Responde apenas em JSON."""

# Faithfulness / groundedness (reference-free): is the answer supported by the context?
JUDGE_FAITHFULNESS_PROMPT = """\
Avalia se a RESPOSTA é fundamentada APENAS no CONTEXTO fornecido (sem inventar \
factos que não estejam no contexto).

Escala:
5 = totalmente fundamentada no contexto
3 = parcialmente fundamentada (alguma informação não suportada)
1 = não fundamentada / contradiz o contexto

CONTEXTO:
{context}

PERGUNTA: {question}

RESPOSTA: {answer}

Responde em JSON: {{"score": <1-5>, "rationale": "..."}}"""

# Answer relevance (reference-free): does the answer address the question?
JUDGE_RELEVANCE_PROMPT = """\
Avalia se a RESPOSTA responde diretamente à PERGUNTA (relevância e completude), \
independentemente de estar correta.

Escala:
5 = responde direta e completamente
3 = responde parcialmente ou de forma vaga
1 = não responde / foge ao tema

PERGUNTA: {question}

RESPOSTA: {answer}

Responde em JSON: {{"score": <1-5>, "rationale": "..."}}"""

# Correctness (reference-based): does the answer agree with the reference answer?
JUDGE_CORRECTNESS_PROMPT = """\
Compara a RESPOSTA com a RESPOSTA DE REFERÊNCIA e avalia a correção factual.

Escala:
5 = concorda totalmente com a referência
3 = parcialmente correta
1 = incorreta / contradiz a referência

PERGUNTA: {question}

RESPOSTA DE REFERÊNCIA: {reference}

RESPOSTA: {answer}

Responde em JSON: {{"score": <1-5>, "rationale": "..."}}"""
