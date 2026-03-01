"""
Prompts for political content classification.
"""

import json

# Define political topic categories
TOPIC_CATEGORIES = {
    "impostos": "Impostos, taxas, fiscalidade, tributação, política fiscal",
    "seguranca_social": "Segurança social, pensões, reformas, subsídios, proteção social",
    "trabalho": "Trabalho, emprego, salários, direitos laborais, sindicatos, desemprego",
    "economia": "Economia, crescimento económico, competitividade, desenvolvimento económico",
    "financas": "Finanças públicas, orçamento, dívida pública, gestão financeira",
    "habitacao": "Habitação, arrendamento, propriedade, habitação social, urbanismo, residências estudantis",
    "saude": "Saúde, SNS, hospitais, cuidados médicos, saúde mental, medicamentos",
    "educacao": "Educação, ensino, universidades, escolas, formação profissional, ciência",
    "seguranca": "Segurança pública, forças policiais, criminalidade, ordem pública",
    "justica": "Justiça, tribunais, sistema judicial, direitos fundamentais, corrupção, offshores",
    "politica_externa": "Política externa, relações internacionais, UE, diplomacia, offshores",
    "cultura": "Cultura, património, artes, língua portuguesa, criatividade, desporto",
    "ambiente": "Ambiente, clima, sustentabilidade, energia, proteção ambiental",
    "igualdade": "Igualdade de género, direitos humanos, inclusão, discriminação, minorias",
    "jovens": "Juventude, políticas para jovens, emancipação jovem, residências estudantis",
    "imigracao": "Imigração, integração, diversidade, comunidades estrangeiras, refugiados",
    "governacao": "Governação, administração pública, descentralização, poder local, transparência",
    "outros": "Outros temas não classificados nas categorias anteriores"
}

# System prompt for political content classification
CLASSIFICATION_PROMPT = f"""És um especialista em análise de programas políticos portugueses. 

CATEGORIAS:
{json.dumps(TOPIC_CATEGORIES, indent=2, ensure_ascii=False)}

INSTRUÇÕES:
1. Um excerto pode ter MÚLTIPLAS categorias (máximo 4)
2. Exemplos multi-tópico:
   - "residências estudantis" → ["jovens", "educacao", "habitacao"]
   - "offshores e corrupção" → ["justica", "politica_externa"]
   - "salário mínimo jovens" → ["trabalho", "jovens"]

3. Confiança (1-5): 5=muito claro, 3=razoável, 1=incerto

RESPOSTA (JSON):
{{
    "categorias": ["categoria1", "categoria2"],
    "confianca": 4,
    "palavras_chave": ["palavra1", "palavra2", "palavra3"]
}}"""