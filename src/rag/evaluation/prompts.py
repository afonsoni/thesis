"""
Portuguese-language prompts for the LLM-as-judge. Kept local to the evaluation
package so retrieval/generation stay independent of it.
"""

# ---------------------------------------------------------------------------
# LLM-as-judge
# ---------------------------------------------------------------------------

JUDGE_SYSTEM_PROMPT = """\
És um avaliador rigoroso e imparcial de respostas geradas por um sistema de \
perguntas e respostas sobre programas políticos portugueses. Avalias sempre numa \
escala de 1 a 5 e justificas brevemente. Responde apenas em JSON."""

# Answer relevance (reference-free): does the answer address the question?
JUDGE_RELEVANCE_PROMPT = """\
Avalia se a RESPOSTA responde diretamente à PERGUNTA (relevância e completude), \
independentemente de estar correta.

Escala:
5 = responde direta e completamente
3 = responde parcialmente ou de forma vaga
1 = não responde / foge ao tema

Indica também se a RESPOSTA se abstém: "abstained" é true se diz que os programas \
(ou o contexto) não contêm a informação pedida, ou rejeita a premissa da pergunta, \
em vez de responder; é false se responde, mesmo que só em parte.

PERGUNTA: {question}

RESPOSTA: {answer}

Responde em JSON: {{"score": <1-5>, "abstained": <true|false>, "rationale": "..."}}"""

# ---------------------------------------------------------------------------
# Claim-level judging (RAGAS-style: Es et al., EACL 2024)
# ---------------------------------------------------------------------------
# Faithfulness and correctness are not scored holistically: the text is split
# into atomic claims, and each claim is checked against evidence one by one.
# The score is the share of claims supported, which is finer than a 1-5 scale,
# says *which* claim failed, and can be checked claim by claim by a human.

CLAIMS_SYSTEM_PROMPT = """\
És um avaliador rigoroso e imparcial de respostas sobre programas políticos \
portugueses. Segues as instruções à letra e respondes apenas em JSON."""

CLAIMS_EXTRACTION_PROMPT = """\
Divide o TEXTO em afirmações atómicas: cada uma diz uma só coisa verificável, \
compreende-se sozinha (substitui pronomes pelo nome do partido ou da medida) e \
mantém os números exatos. Ignora fórmulas de cortesia e frases que não afirmam \
nada sobre os programas. Se o texto diz que os programas não referem algo, isso \
é uma afirmação.

PERGUNTA (para contexto): {question}

TEXTO:
{text}

Responde em JSON: {{"claims": ["...", "..."]}}"""

CLAIMS_VERIFICATION_PROMPT = """\
Para cada AFIRMAÇÃO numerada, decide se é suportada pelo TEXTO DE APOIO: \
"supported": true só se o texto de apoio a afirma ou implica diretamente; \
false se a contradiz ou se não a menciona. Não uses conhecimento externo. Uma \
afirmação de que algo não é referido é suportada se o texto de apoio de facto \
não o refere.

TEXTO DE APOIO:
{evidence}

AFIRMAÇÕES:
{claims}

Responde em JSON, com um veredicto por afirmação e pela mesma ordem:
{{"verdicts": [{{"index": 1, "supported": true, "reason": "..."}}]}}"""

