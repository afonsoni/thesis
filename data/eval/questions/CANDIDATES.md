# Gold-set candidates (51 → pick 30)

Hand-drafted 2026-09-23 from the eight 2024 manifestos in `data/1_markdown/`.
Every question was checked against the corpus (grep) so a grounding passage
exists; re-checked 2026-10-08 against the indexed files, with the BE notes rewritten
for the 2024 manifesto (the corpus previously held BE's 2022 programme); the exact `gold_chunk_keys` are assigned when the question is anchored
through the dataset tool, not here.

Columns: **Type** is the routing ground truth (`single_party` / `comparison` /
`topic_exploration` / `general`). **Stresses** names the ladder rung the
question is designed to discriminate: *routing* (party/topic detection),
*multi-query* (vocabulary mismatch between question and manifesto wording),
*hybrid* (acronyms, numbers, proper nouns where lexical search should help),
*reranker* (many near-duplicate candidates), *baseline* (easy, any rung should
get it). **Diff** is expected difficulty: E / M / H.

Pick for balance: roughly 10 single-party, 8 comparison, 7 topic, 5 general;
every party as the source of at least two questions; at least one question per
stress type per rung; a spread of E/M/H.

## Single party (18)

| # | Question (pt-PT) | Parties | Topics | Stresses | Diff | Grounding note |
|---|---|---|---|---|---|---|
| 1 | Qual é a taxa única de IRS proposta pela Iniciativa Liberal? | IL | impostos | hybrid | E | 15% acima do SMN, faseada com 15%/28% |
| 2 | Para quanto quer o PCP aumentar o Salário Mínimo Nacional? | PCP | trabalho | hybrid, baseline | E | 1000 euros em 2024 |
| 3 | O que propõe a AD para o IRS Jovem? | AD | impostos, jovens | hybrid | E | taxa máxima 15%, até aos 35 anos, redução de 2/3 |
| 4 | Qual é a posição do PAN sobre as touradas? | PAN | cultura, outros | baseline | E | abolir a tourada e espectáculos tauromáquicos |
| 5 | Que alterações quer o LIVRE fazer à lei do aborto? | LIVRE | saude, igualdade | multi-query | M | manifesto diz "IVG", não "aborto"; alargar prazo para 14 semanas |
| 6 | Que penas propõe o CHEGA para criminosos reincidentes e crimes graves? | CHEGA | justica, seguranca | routing | M | prisão perpétua revisível (42), castração química para reincidentes (41) |
| 7 | Como é que a Iniciativa Liberal pretende dar médico de família a todos? | IL | saude | baseline | E | público ou privado, todos até 2028, prioritários até 2025 |
| 8 | Qual é a posição do PCP sobre a NATO e a UE? | PCP | politica_externa | hybrid | M | "conivência com a NATO", rompendo submissão à UE, saída do Euro |
| 9 | O que diz o Bloco sobre as propinas no ensino superior? | BE | educacao | multi-query | M | "Eliminação das propinas na licenciatura, CTeSP e mestrados integrados", novo modelo de acesso sem propinas, mais bolsas |
| 10 | Que propostas tem o LIVRE para a saúde mental? | LIVRE | saude | reranker | M | 75 menções; muitos chunks candidatos, precisa dos de medidas |
| 11 | A Iniciativa Liberal é a favor da energia nuclear em Portugal? | IL | ambiente | baseline | E | "defender o nuclear na Europa, estudar a viabilidade em Portugal" |
| 12 | O que diz o PS sobre a regionalização? | PS | governacao | baseline | E | arranque do processo de regionalização, secção 2 |
| 13 | O LIVRE propõe um rendimento básico incondicional? Em que termos? | LIVRE | seguranca_social | hybrid | M | programa piloto faseado |
| 14 | Qual é a posição da Iniciativa Liberal sobre a canábis? | IL | justica, saude | baseline | E | legalização da produção e venda |
| 15 | Que medidas propõe o CHEGA para controlar a imigração? | CHEGA | imigracao | reranker | M | 34 menções, muito diagnóstico vs poucas medidas |
| 16 | O que propõe a AD para aumentar a natalidade? | AD | seguranca_social, saude | routing | M | PMA no SNS, secção "Natalidade, longevidade e bem-estar" |
| 17 | Que limites quer o Bloco de Esquerda impor ao Alojamento Local? | BE | habitacao | baseline | E | quotas máximas por freguesia; suspensão de novos empreendimentos turísticos nas zonas de pressão habitacional até 2030 |
| 18 | Que reforma do sistema eleitoral propõe a Iniciativa Liberal? | IL | governacao | hybrid | M | círculo nacional de compensação, método de Hondt |

## Comparison (13)

| # | Question (pt-PT) | Parties | Topics | Stresses | Diff | Grounding note |
|---|---|---|---|---|---|---|
| 19 | Compara as propostas de IRS da Iniciativa Liberal e do CHEGA. | IL, CHEGA | impostos | routing, hybrid | M | IL 15% única; CHEGA 15% até 39.999 e 30% acima, isenção até 1000/mês |
| 20 | PCP e Bloco de Esquerda: o que propõem sobre a redução do horário de trabalho? | PCP, BE | trabalho | routing | M | ambos 35 horas para todos; BE junta-lhes a semana de quatro dias (secção "Tempo para viver: semana de quatro dias, 35 horas, desconexão") |
| 21 | Em que diferem AD e PS nas creches? | AD, PS | educacao, seguranca_social | routing | H | ambos prometem gratuitidade universal; PS como continuidade, AD via sector social/privado; a resposta correcta é "quase o mesmo", o que testa se o sistema inventa diferenças; |
| 22 | O que propõem a IL e o Bloco de Esquerda para o Alojamento Local? | IL, BE | habitacao | routing | M | posições opostas: IL reverter as normas do Mais Habitação; BE limitar e impor quotas por zona |
| 23 | AD e PS: o que propõem para o IRS Jovem? | AD, PS | impostos, jovens | hybrid | E | AD 15% até 35 anos; PS alargar a todos independentemente da escolaridade |
| 24 | Compara as propostas de IRC do PCP e da IL. | PCP, IL | impostos, economia | hybrid | M | PCP 12,5% para MPME + derrama 14% acima de 50M; IL 12% única |
| 25 | LIVRE e PS: como querem descentralizar o poder? | LIVRE, PS | governacao | multi-query | M | LIVRE órgãos regionais eleitos; PS regionalização |
| 26 | Bloco de Esquerda e PCP: o que propõem sobre privatizações e controlo público de sectores estratégicos? | BE, PCP | economia, financas | reranker | H | BE: capítulo 7 "Controlo Público dos Setores Estratégicos" (GALP/EDP/REN, CTT, ANA, TAP, banca pública); PCP: reversão programada das privatizações, nacionalização, saída da União Bancária |
| 27 | Compara a posição do CHEGA e do PS sobre imigração. | CHEGA, PS | imigracao | routing | M | 34 vs 16 menções; CHEGA restritivo, PS regulação/integração |
| 28 | PAN e LIVRE: que medidas propõem para a proteção dos animais? | PAN, LIVRE | ambiente, outros | routing | M | PAN 111 menções vs LIVRE 39 |
| 29 | AD e Iniciativa Liberal: o que propõem para a Administração Pública? | AD, IL | governacao | reranker | H | IL 59 menções; muitos chunks parecidos |
| 30 | PCP e PS: o que propõem para as pensões? | PCP, PS | seguranca_social | routing | M | 33 vs 21 menções |
| 31 | O que dizem o Bloco de Esquerda e o LIVRE sobre a semana de quatro dias? | BE, LIVRE | trabalho | multi-query, hybrid | M | ambos a favor: LIVRE continuar a experiência e levá-la à contratação colectiva; BE propõe "um programa de estabelecimento da semana de quatro dias, sem perda salarial", ao lado das 35 horas. O LIVRE escreve "4 dias", a pergunta e o BE escrevem "quatro" |

## Topic exploration (15), no party named

| # | Question (pt-PT) | Parties | Topics | Stresses | Diff | Grounding note |
|---|---|---|---|---|---|---|
| 32 | Que partidos defendem a energia nuclear? | all | ambiente | routing | M | IL "estudar a viabilidade em Portugal"; CHEGA complementar renováveis com nuclear. LIVRE só fala de risco nuclear (Tejo/Espanha), não de produção |
| 33 | O que propõem os partidos para o salário mínimo? | all | trabalho | routing (topic) | M | PCP 1000€ em 2024; IL negociação sectorial em vez de valor único; todos mencionam |
| 34 | Que propostas existem para resolver as listas de espera no SNS? | all | saude | multi-query | M | IL médico de família; BE "salvar o SNS" |
| 35 | Que medidas há para baixar as rendas e o preço da habitação? | all | habitacao | reranker | H | 36 a 85 menções por partido |
| 36 | Quem quer baixar o IRC e para quanto? | all | impostos, economia | hybrid | M | IL 12% única; AD 21%→15% a 2 p.p./ano; CHEGA 15% interior/regiões autónomas e 18% resto; PAN 17% a 1 p.p./ano; PCP 12,5% só para MPME (sobe para grandes) |
| 37 | Que propostas existem para valorizar a carreira dos professores? | all | educacao, trabalho | routing (topic) | M | IL 35, AD 25 menções |
| 38 | O que propõem os partidos para a floresta e a prevenção de incêndios? | all | ambiente | multi-query | M | BE 45, LIVRE 47 menções |
| 39 | Que medidas de combate à corrupção são propostas? | all | justica, governacao | routing (topic) | M | AD 37, CHEGA 36, PCP 29 |
| 40 | Que propostas há para os emigrantes e a diáspora? | all | politica_externa, outros | multi-query | M | AD "diáspora" 15; CHEGA "emigra" 21 |
| 41 | O que dizem os programas sobre a alta velocidade ferroviária? | all | economia, ambiente | hybrid | M | CHEGA, PS, IL, LIVRE, PCP; PAN condiciona a linha Porto-Lisboa |
| 42 | Que apoios são propostos para pessoas com deficiência? | all | igualdade, seguranca_social | routing (topic) | M | BE 50, LIVRE 31 |
| 43 | Algum partido fala de inteligência artificial? O quê? | all | educacao, economia | hybrid | M | AD 17, PS 10; BE 0 |
| 44 | Que medidas contra a violência doméstica são propostas? | all | igualdade, justica | routing (topic) | E | PAN 21, todos mencionam |
| 50 | Que partido propõe uma taxa única de IRC de 12%? | all | impostos | routing (reverse lookup) | H | IL (taxa única de 12%, 15% para multinacionais). Rotulada `topic_exploration`: a resposta é o partido, por isso é preciso procurar em todos; nenhum outro propõe 12% (PCP 12,5% só para MPME) |
| 51 | Qual é a posição dos partidos sobre a eutanásia? | all | saude, justica | multi-query | H | os programas dizem "morte medicamente assistida", nunca "eutanásia": CHEGA revogar a Lei 22/2023 (medida 107); LIVRE acompanhar a implementação da despenalização; PAN regulamentação urgente da lei. AD, BE, IL, PCP, PS omissos |

## General (5)

| # | Question (pt-PT) | Parties | Topics | Stresses | Diff | Grounding note |
|---|---|---|---|---|---|---|
| 45 | O que é o IRS Jovem? | none | impostos, jovens | hybrid | E | definição extraível de AD ou PS |
| 46 | O que é o PRR e como pretendem os partidos aplicá-lo? | none | financas, economia | hybrid | M | AD 12, IL 11, PS 11 |
| 47 | Quantos imigrantes entraram em Portugal em 2022, segundo os programas? | none | imigracao | hybrid | H | CHEGA: 118.000; facto numérico, responde apenas um partido |
| 48 | O que é a "herança social"? | none | seguranca_social, impostos | hybrid | M | termo do LIVRE; imposto sucessório sobre grandes heranças |
| 49 | Em que ano foram repostas as 35 horas na Administração Pública? | none | trabalho | hybrid | H | PCP: 2016; facto exacto num único chunk |

## Abstention candidates (not counted in the 51)

The harness has no metric for "the manifestos do not say". These need a
`gold_chunk_keys: []` convention and a judge rubric that rewards refusal
before they can be scored. Include only if that lands.

| Question | Why it is unanswerable |
|---|---|
| O que propõe o PCP sobre a legalização da canábis? | PCP não menciona canábis |
| Qual é a posição do PAN sobre a NATO? | zero menções a NATO/OTAN no PAN (contagem com fronteira de palavra; a contagem bruta apanhava "dotando") |
| O que propõe o PS para a energia nuclear? | zero menções no PS |

## Coverage check

Source party appears in: AD 3, 16, 21, 23, 29, 45 · BE 9, 17, 20, 22, 26, 31 ·
CHEGA 6, 15, 19, 27, 47, 51 · IL 1, 7, 11, 14, 18, 19, 22, 24, 29, 50 ·
LIVRE 5, 10, 13, 25, 28, 31, 48, 51 · PAN 4, 28, 51 · PCP 2, 8, 20, 24, 26, 30, 49 ·
PS 12, 21, 23, 25, 27, 30.

PAN has three questions (4, 28, 51); if it needs more, use its animal-welfare
or IVA-on-pet-food material. IL is over-represented because its manifesto is the
most concrete on numbers; trim IL single-party questions first when cutting to 30.
