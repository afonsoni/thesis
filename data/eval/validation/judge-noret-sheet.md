# Judge validation sheet

Mark each claim `[x]` (yes) or `[n]` (no); leave `[ ]` to skip. Give relevance 1-5
(5 = answers the question directly and completely). Judge verdicts are hidden in
judge-key.json; run `python scripts/judge_validation.py score` when done.

## item-01

**Question:** Que propostas tem o LIVRE para a saúde mental?

**Answer:**

As propostas do **LIVRE** para a área da saúde mental focam-se no reforço dos cuidados comunitários e na integração da saúde mental nos cuidados de saúde primários:

• **Reforço da rede de cuidados comunitários**: O partido propõe o investimento em equipas multidisciplinares de saúde mental que atuem no território, visando reduzir a dependência de internamentos hospitalares e promover o acompanhamento próximo dos utentes.
• **Integração nos Cuidados de Saúde Primários**: Defende que a saúde mental deve estar integrada nos centros de saúde, garantindo que o acesso a psicólogos e psiquiatras seja parte integrante da consulta de rotina e do acompanhamento de saúde geral.
• **Aumento de recursos humanos**: Propõe a criação de mais lugares para profissionais especializados (psicólogos, enfermeiros de saúde mental e assistentes sociais) para reduzir os tempos de espera e a sobrecarga do sistema.
• **Foco na infância e juventude**: O programa enfatiza a necessidade de respostas específicas para o aumento de problemas de saúde mental entre crianças e adolescentes, propondo a presença de psicólogos nas escolas e o apoio precoce às famílias.
• **Combate ao estigma**: Defende a implementação de campanhas de literacia em saúde mental para promover a desestigmatização das doenças mentais na sociedade.

**Reference answer:**

O LIVRE propõe promover a saúde mental com políticas multissetoriais, literacia e campanhas de sensibilização, e torná-la prioridade de todas as políticas públicas, com dotação específica no Orçamento do Estado. Defende mais equipas comunitárias de saúde mental em todo o território, um modelo de cuidados escalonados (stepped care), Centros de Responsabilidade Integrados, a expansão da rede de cuidados continuados de saúde mental, pelo menos um psicólogo clínico por centro de saúde e o fim da exigência de referenciação pelo médico de família para consultas de psicologia no SNS. Propõe ainda mais psicólogos escolares e de saúde ocupacional, uma linha nacional de prevenção do suicídio, a reativação do Plano Nacional de Prevenção do Suicídio e um Plano Nacional de Saúde Mental para centros educativos e estabelecimentos prisionais. Quer ainda melhorar a qualidade dos serviços, com mais investimento público em profissionais especializados, a comparticipação a 100% dos antipsicóticos fora do hospital, programas de descontinuação das benzodiazepinas, mais respostas de urgência e internamento para doença mental grave e aguda e a prevenção dos comportamentos aditivos; humanizar os serviços, através da desinstitucionalização progressiva, do respeito pelos direitos humanos (consentimento informado e menos medidas coercivas), do apoio à transição para a comunidade e do combate ao estigma; alargar a prescrição médica de atividades culturais; e reforçar o Programa de Apoio Financeiro DGS PNSM a instituições privadas e do setor social.

**faithfulness** — Is the claim supported by the CONTEXT?

- [ ] O LIVRE propõe o investimento em equipas multidisciplinares de saúde mental que atuem no território.
- [ ] O LIVRE visa reduzir a dependência de internamentos hospitalares através do reforço dos cuidados comunitários.
- [ ] O LIVRE defende que a saúde mental deve estar integrada nos centros de saúde.
- [ ] O LIVRE propõe que o acesso a psicólogos e psiquiatras seja parte integrante da consulta de rotina nos cuidados de saúde primários.
- [ ] O LIVRE propõe a criação de mais lugares para psicólogos para reduzir os tempos de espera.
- [ ] O LIVRE propõe a criação de mais lugares para enfermeiros de saúde mental para reduzir a sobrecarga do sistema.
- [ ] O LIVRE propõe a criação de mais lugares para assistentes sociais para reduzir os tempos de espera.
- [ ] O LIVRE propõe a presença de psicólogos nas escolas para responder ao aumento de problemas de saúde mental entre crianças e adolescentes.
- [ ] O LIVRE propõe o apoio precoce às famílias para responder ao aumento de problemas de saúde mental entre crianças e adolescentes.
- [ ] O LIVRE defende a implementação de campanhas de literacia em saúde mental para promover a desestigmatização das doenças mentais.

**correctness_recall** — Does the ANSWER state this reference claim?

- [ ] O LIVRE propõe promover a saúde mental com políticas multissetoriais.
- [ ] O LIVRE propõe promover a saúde mental com literacia.
- [ ] O LIVRE propõe promover a saúde mental com campanhas de sensibilização.
- [ ] O LIVRE propõe tornar a saúde mental prioridade de todas as políticas públicas.
- [ ] O LIVRE propõe a dotação específica para a saúde mental no Orçamento do Estado.
- [ ] O LIVRE defende a criação de mais equipas comunitárias de saúde mental em todo o território.
- [ ] O LIVRE defende a implementação de um modelo de cuidados escalonados (stepped care).
- [ ] O LIVRE defende a criação de Centros de Responsabilidade Integrados.
- [ ] O LIVRE defende a expansão da rede de cuidados continuados de saúde mental.
- [ ] O LIVRE defende a existência de pelo menos um psicólogo clínico por centro de saúde.
- [ ] O LIVRE defende o fim da exigência de referenciação pelo médico de família para consultas de psicologia no SNS.
- [ ] O LIVRE propõe a contratação de mais psicólogos escolares.
- [ ] O LIVRE propõe a contratação de mais psicólogos de saúde ocupacional.
- [ ] O LIVRE propõe a criação de uma linha nacional de prevenção do suicídio.
- [ ] O LIVRE propõe a reativação do Plano Nacional de Prevenção do Suicídio.
- [ ] O LIVRE propõe a criação de um Plano Nacional de Saúde Mental para centros educativos.
- [ ] O LIVRE propõe a criação de um Plano Nacional de Saúde Mental para estabelecimentos prisionais.
- [ ] O LIVRE propõe aumentar o investimento público em profissionais especializados para melhorar a qualidade dos serviços de saúde mental.
- [ ] O LIVRE propõe a comparticipação a 100% dos antipsicóticos fora do hospital.
- [ ] O LIVRE propõe a implementação de programas de descontinuação das benzodiazepinas.
- [ ] O LIVRE propõe aumentar as respostas de urgência para doença mental grave e aguda.
- [ ] O LIVRE propõe aumentar as respostas de internamento para doença mental grave e aguda.
- [ ] O LIVRE propõe a prevenção dos comportamentos aditivos.
- [ ] O LIVRE propõe a desinstitucionalização progressiva para humanizar os serviços de saúde mental.
- [ ] O LIVRE propõe o respeito pelos direitos humanos, incluindo o consentimento informado, para humanizar os serviços de saúde mental.
- [ ] O LIVRE propõe a redução de medidas coercivas para humanizar os serviços de saúde mental.
- [ ] O LIVRE propõe o apoio à transição para a comunidade para humanizar os serviços de saúde mental.
- [ ] O LIVRE propõe o combate ao estigma para humanizar os serviços de saúde mental.
- [ ] O LIVRE propõe alargar a prescrição médica de atividades culturais.
- [ ] O LIVRE propõe reforçar o Programa de Apoio Financeiro DGS PNSM a instituições privadas.
- [ ] O LIVRE propõe reforçar o Programa de Apoio Financeiro DGS PNSM ao setor social.

relevance: 

<details><summary>Context the generator read</summary>

[Documento 1] Partido: LIVRE | Tópicos: saude
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > **Saúde**
Defendemos que compete ao Estado assegurar a proteção da saúde e que esta seja universal, gratuita e adequada às características da população em todo o território.  
Em Portugal, o principal prestador de cuidados de saúde deve ser o Serviço Nacional de Saúde - que consideramos essencial para assegurar a igualdade e a liberdade. A sua ação pode ser complementada pelos setores privado e social, com os quais deve ter protocolos e convenções apenas nas áreas onde se considera que não tem recursos que permitam garantir uma resposta adequada, devendo a relação entre os três setores ser transparente, honesta e regulada e no sentido da capacitação do SNS nas áreas em que seja deficitário.  
O LIVRE está seguro de que o Serviço Nacional de Saúde só sobreviverá com uma estratégia global urgente para a Saúde, que respeite integralmente a nova Lei de Bases da Saúde, concluindo os projetos estabelecidos no Plano de Recuperação e Resiliência e tirando vantagem da recente reorganização em Unidades Locais de Saúde, que conceptualizam o princípio da integração de cuidados e autonomia regional na Saúde.  
É essencial a integração e boa articulação dos vários níveis de cuidados em que o utente ou a pessoa com doença esteja no centro, independentemente do prestador, assim como a existência de cuidados de proximidade e a humanização da saúde.  
O conceito de saúde ultrapassa, contudo, os estabelecimentos onde são prestados cuidados. Em Portugal, as dificuldades de saúde estão particularmente associadas a determinantes sociais como o elevado risco de pobreza e a desigualdade; à discriminação e à violência; aos baixos níveis de literacia em saúde; à precariedade laboral e condições de trabalho; à falta de acesso a habitação e saúde; ao isolamento social e ao envelhecimento da população; e à falta de oportunidades para o pleno desenvolvimento individual e ocupacional decorrentes da baixa escolaridade e dos baixos salários. Importa ter cuidados de proximidade fortalecidos, com profissionais de saúde e assistentes técnicos de áreas fundamentais como medicina geral e familiar, enfermagem, diagnóstico, terapêutica (incluindo higienistas orais, terapeutas da fala, fisioterapeutas, terapeutas ocupacionais), nutrição, psicologia, medicina dentária, serviço social em número adequado, assim como é urgente dotar os hospitais de meios materiais e humanos suficientes. É prioritário aumentar a fração do orçamento de saúde dedicada à prevenção da doença e promoção de Saúde, e dotar as instituições de Saúde Pública de recursos e de um efetivo poder de decisão junto dos dossiês em que considerem necessário intervir. Mas é igualmente importante que haja uma integração desta área em todas as outras que intervêm ao nível dos determinantes da saúde (nível socioeconómico, condições e estilos de vida, educação, apoio social - segurança social, municípios e misericórdias): a "Saúde em todas as políticas".  
O investimento na saúde mental é também uma das prioridades do LIVRE. Tal como as restantes áreas da saúde, os cuidados de saúde mental - desde a promoção da saúde mental ao tratamento especializado das doenças mentais - devem ser acessíveis a todas as pessoas. Portugal tem carência de profissionais especializados em saúde mental (psiquiatras, psicólogos, enfermeiros e técnicos de serviço social), elevadas listas de espera no SNS e grandes disparidades territoriais na cobertura de serviços de saúde mental. Adicionalmente, a pandemia de COVID-19 contribuiu para a deterioração da saúde mental da população e para o aumento da pressão sobre os serviços de saúde mental e os seus profissionais. Assim, todas as políticas públicas devem ter em consideração o seu impacto nas condições estruturais para a satisfação das necessidades psicológicas inerentes ao pleno desenvolvimento humano como são a autonomia, o sentimento de competência e o sentimento de pertença. As políticas de saúde mental devem ser pensadas intersetorialmente e não no âmbito exclusivo da saúde, tal como preconizado pelo Plano Nacional de Saúde Mental. As políticas públicas de habitação e urbanismo, educação, trabalho, justiça, segurança social, cultura e ciência devem igualmente prever a promoção da saúde mental e a integração de pessoas com necessidades de cuidados de saúde mental. A exaustão do sistema e seus profissionais, trazida pela pandemia mas que ainda persiste, exige-nos o reconhecimento do seu valor por meio da adoção de medidas que respondam aos apelos dos trabalhadores e às necessidades da população, salvando o Serviço Nacional de Saúde.  
Propomo-nos ouvir todas as pessoas, nomeadamente profissionais de saúde e utentes, no sentido de encontrar soluções a longo prazo que fortaleçam o SNS e que façam com que todas as pessoas se revejam nele, o sintam como seu e se motivem para contribuir para a sua sustentabilidade e qualidade a longo prazo. As propostas no âmbito da saúde estão organizadas em cinco eixos prioritários:  
- Reforçar e Reorganizar o Serviço Nacional de Saúde
- Valorizar as carreiras profissionais no SNS
- Promover a saúde e prevenir a doença
- Humanizar os cuidados de saúde
- Investir na Saúde Mental

---

[Documento 2] Partido: LIVRE | Tópicos: saude
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > **Saúde** > Por isso defendemos: > **Investir na Saúde Mental**
#### **Investir na Saúde Mental**  
34. **Promover a saúde mental e prevenir a doença mental:**  
- através de políticas multissetoriais fornecendo as condições estruturais para a satisfação das necessidades de saúde mental inerentes ao pleno desenvolvimento humano como são a autonomia, o sentimento de competência e o sentimento de pertença;
- garantir o bem-estar psicológico e a literacia em saúde mental com intervenções comunitárias de eficácia comprovada por evidência, de baixos custos e abrangentes em todas as faixas etárias;
- prevenir a doença mental com intervenções específicas dirigidas a populações vulneráveis e em risco de exclusão, no seguimento de eventos traumáticos e situações de emergência;
- integrar e promover a participação das pessoas com necessidade de cuidados de saúde mental contribuindo assim para o seu bem-estar psicológico;
- concretizar a criação de um Observatório Nacional de Literacia em Saúde, em linha com o preconizado no Plano Nacional de Literacia em Saúde e Ciências do Comportamento 2023-2030, reforçando a atenção específica à literacia em Saúde Mental;
- sensibilizar a população para a saúde mental através de campanhas públicas genéricas (Dia Mundial da Saúde Mental) e dirigidas a problemáticas específicas (por exemplo, Dia Nacional da Luta Anti-Alcoolismo, Dia Mundial de Prevenção ao Suicídio);
- reforçar a colaboração entre os Ministérios da Cultura e da Saúde, reconhecendo os benefícios da cultura para o bem-estar e a prevenção e o tratamento da doença, nomeadamente através do alargamento da prescrição médica de atividades culturais e da inclusão de atividades culturais nos planos regionais de saúde mental.  
35. **Prosseguir e aprofundar a transformação da saúde mental** ao:  
- apostar na diversificação das respostas de saúde mental e na implementação de um modelo de stepped care consoante as diferentes necessidades da população, englobando serviços de saúde mental especializados, hospitalares e comunitário, cuidados primários de saúde mental, serviços de prevenção e promoção da saúde mental na comunidade), e serviços de apoio psicossocial fora do setor da saúde ( organizações da sociedade civil e redes de apoio informal);
- prosseguir o modelo de organização da saúde mental em equipas multidisciplinares comunitárias previsto no Plano Nacional de Saúde Mental e aprofundá-lo com a constituição de mais equipas comunitárias de saúde mental para crianças, jovens e adultos, assim como o seu alargamento a todo o território nacional;
- concretizar a implementação dos Centros de Responsabilidade Integrados na área da Saúde Mental e Psiquiatria de modo a descentralizar a prestação de cuidados, promover a autonomia da contratação de profissionais e melhorar as suas condições laborais por via, entre outros, de um regime de incentivos associados aos indicadores de resultado que incluam também indicadores de qualidade assistencial definidos pelos utentes;
- promover a autonomia e a funcionalidade das através da expansão a todo o território nacional e alargamento do número de vagas da rede nacional de cuidados continuados integrados de saúde mental, nomeadamente das estruturas de reabilitação psicossocial e das residências de apoio, previsto no PRR;
- concretizar os planos nacionais e regionais de saúde para as demências garantindo a cobertura a nível nacional e reforçando a componente preventiva de envelhecimento ativo em articulação com as diversas estruturas de apoio social (e.g., centros de dia, academias sénior, etc.).  
36. **Democratizar o acesso a cuidados de e de enfermagem de saúde mental e psiquiátrica com qualidade** ao:  
- facilitar a sinalização e referenciação para serviços de saúde mental especializados a partir de serviços públicos, como exemplo a linha SNS 24 ou Segurança Social;
- promover o mapeamento e facilitar o acesso a informação centralizada acerca de serviços de saúde mental e apoio psicológico gratuito (por exemplo juntas de freguesia, ONGs e IPSSs) ou de custo reduzido para pessoas com dificuldades económicas (por exemplo, associações profissionais de saúde mental sem fins lucrativos);
- eliminar a necessidade de referenciação do médico de família para consultas de psicologia no SNS promovendo o reconhecimento da sua autonomia e da especificidade dos conhecimentos dos psicólogos;
- possibilitar que cartas de referenciação redigidas por psicólogos clínicos ou por enfermeiros especialistas em Enfermagem de Saúde Mental e Psiquiátrica permitam a triagem direta dos utentes, nos Serviços de Urgência, para observação pela especialidade de Psiquiatria;
- estender a comparticipação de consultas de psicologia pela ADSE sem necessidade de prescrição médica às tabelas de regime livre da ADSE;
- assegurar que cada centro de saúde tem pelo menos um psicólogo clínico a trabalhar em articulação com outros profissionais de saúde, garantindo a prestação de cuidados de saúde mental especializados nos cuidados de saúde primários;
- alargar e melhorar a qualidade da resposta às condições de saúde mental comuns como as perturbações depressivas e da ansiedade, nomeadamente através da aposta nas intervenções psicológicas nos cuidados de saúde primários do SNS e nas intervenções especializadas de Enfermagem de Saúde Mental e Psiquiátrica.  
37. **Melhorar a qualidade dos serviços de saúde mental:**  
- aumentar o investimento público na saúde mental de modo a providenciar recursos humanos multidisciplinares especializados (psiquiatras da infância e adolescência, psicólogos clínicos, enfermeiros especialistas em Enfermagem de Saúde Mental e Psiquiátrica, terapeutas ocupacionais e assistentes sociais) e a aquisição de bens e serviços adequados à satisfação das necessidades da população através de dotação orçamental própria no OE;
- alargar dos programas de descontinuação das benzodiazepinas nos ACeS e hospitais centrais;
- alargar da comparticipação a 100% dos fármacos anti-psicóticos a prescrições fora do sistema hospitalar;
- ampliar redes de serviços de atendimento urgente e internamento para situações de doença mental grave e aguda, sobretudo nas regiões do país é deficitária e às populações mais necessitadas, nomeadamente para crianças e adolescentes;
- apostar na prevenção dos comportamentos aditivos e dependências, como alcoolismo e toxicodependência (medicamentos, canabinoides, substâncias psicoativas, entre outros) mas extensíveis a outras formas de adição como tabaco e jogo;
- acompanhar a reestruturação e redefinição de competências do Instituto para os Comportamentos Aditivos e as Dependências, I. P., e verificar a necessidade de aumento de recursos humanos e financeiros.  
38. **Humanizar os serviços de saúde mental**, combater a discriminação e o estigma da doença mental, ao:  
- concretizar a desinstitucionalização progressiva das pessoas com doença mental grave e substituição por intervenções na comunidade de acordo com o Plano Nacional de Saúde Mental;
- garantir o escrupuloso cumprimento dos Direitos Humanos das pessoas com especial necessidade de cuidado de saúde mental (nomeadamente na verificação do consentimento informado, na redução de utilização de medidas coercivas, no envolvimento na tomada de decisão de tratamento ou na privacidade dos dados clínicos e temporalidade dos diagnósticos) em todos os serviços de saúde mental, especialmente nos serviços hospitalares com internamento psiquiátricos, nas situações de internamento involuntário e nos serviços de psiquiatria forense;
- apoiar a transição para a comunidade, promover a autonomia e prevenir o reinternamento das pessoas em situação de internamento psiquiátrico;
- apostar na formação de profissionais e reformar os modelos de gestão das instituições em consonância com os princípios éticos e humanistas consagrados na nova lei da saúde mental;
- promover a participação de profissionais de saúde, da comunidade e de cidadãos (tais como associações de utentes e de familiares) na gestão, funcionamento e órgãos consultivos dos serviços de saúde mental prestados por instituições do SNS, privadas ou do setor social como previsto no Plano Nacional de Saúde Mental;
- promover a literacia em saúde mental em todas as instituições e setores do Estado, com especial incidência no combate à descriminação e estigma da doença mental, e no respeito da diversidade social, cultural e étnica como prioridade de todos os serviços públicos.  
39. **Tornar a saúde mental uma prioridade de todas as políticas públicas.** As políticas de saúde mental devem ser pensadas intersetorialmente e não no âmbito exclusivo da saúde, tal como preconizado pelo Plano Nacional de Saúde Mental. Neste sentido, o OE deverá passar a prever uma dotação orçamental específica para a promoção da saúde mental em vários setores da sociedade como no sistema de ensino, no sistema judicial e na segurança social. As políticas públicas de habitação e urbanismo, trabalho e emprego, educação, cultura e ciência devem igualmente prever a promoção da saúde mental e a integração de pessoas com necessidades de cuidados de saúde mental (por exemplo, pessoas em situação de sem-abrigo, em risco de pobreza e vítimas de discriminação e violência).  
40. **Promover a saúde mental, nomeadamente o desenvolvimento de competências socioemocionais e cognitivas das crianças e jovens** nos estabelecimentos de ensino através da:  
- contratação de mais psicólogos escolares para os agrupamentos de escolas do sector público e reforço dos enfermeiros especialistas em Enfermagem de Saúde Mental e Psiquiátrica que exercem funções no âmbito da saúde escolar;
- melhoria das expectativas de progressão nas carreiras dos psicólogos escolares;
- eliminação dos vínculos laborais precários dos psicólogos escolares, tanto no sector público como privado;
- reforço dos Serviços de Saúde Mental e Bem-Estar das instituições de ensino superior na promoção da saúde mental, do desenvolvimento de competências socioemocionais, cognitivas e académicas, e da integração psicossocial de docentes e não docentes.  
41. **Promover a saúde mental nas organizações e empresas** através da:  
- aposta nas equipas de saúde ocupacional dos setores público e privado, as quais devem ser reforçadas com a obrigatoriedade de contratação de psicólogos de saúde ocupacional em todos os setores da atividade económica (e.g., avaliação de risco psicossocial);
- inclusão das perturbações mentais comuns na Lista de Doenças Profissionais;
- aposta na sensibilização e formação para a saúde mental ocupacional.  
42. **Prevenir o suicídio e os comportamentos autolesivos.** O suicídio é um grave problema de saúde pública em Portugal, afetando especialmente os homens e algumas regiões do país, por isso propomos:  
- implementar a linha nacional para a prevenção do suicídio e de comportamentos autolesivos;
- reativar o Plano Nacional de Prevenção do Suicídio no âmbito da Plano Nacional de Saúde Mental;
- aumentar a capacidade de resposta e melhorar o acesso aos cuidados de saúde mental primários especialmente em territórios de risco elevado;
- capacitar as comunidades locais (associações, coletividades e grupos de apoio informais) para a sinalização e encaminhamento de situações de risco, para combater a solidão, promover o apoio e a inserção social;
- investir na divulgação da informação e em ações de formação aos cidadãos e aos meios de comunicação sobre estratégias de comunicação do suicídio e sua abordagem nas redes sociais.  
43. **Reforçar o Programa de Apoio Financeiro DGS PNSM destinado a instituições privadas e do setor social** de forma a estimular o desenvolvimento de programas de prevenção e intervenção inovadores e baseados na melhor evidência científica na área da saúde mental, tal como previsto no Plano Nacional de Saúde Mental.

---

[Documento 3] Partido: LIVRE | Tópicos: saude, educacao, jovens
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > **Saúde** > Por isso defendemos: > **Investir na Saúde Mental**
- ampliar redes de serviços de atendimento urgente e internamento para situações de doença mental grave e aguda, sobretudo nas regiões do país é deficitária e às populações mais necessitadas, nomeadamente para crianças e adolescentes;
- apostar na prevenção dos comportamentos aditivos e dependências, como alcoolismo e toxicodependência (medicamentos, canabinoides, substâncias psicoativas, entre outros) mas extensíveis a outras formas de adição como tabaco e jogo;
- acompanhar a reestruturação e redefinição de competências do Instituto para os Comportamentos Aditivos e as Dependências, I. P., e verificar a necessidade de aumento de recursos humanos e financeiros.  
38. **Humanizar os serviços de saúde mental**, combater a discriminação e o estigma da doença mental, ao:  
- concretizar a desinstitucionalização progressiva das pessoas com doença mental grave e substituição por intervenções na comunidade de acordo com o Plano Nacional de Saúde Mental;
- garantir o escrupuloso cumprimento dos Direitos Humanos das pessoas com especial necessidade de cuidado de saúde mental (nomeadamente na verificação do consentimento informado, na redução de utilização de medidas coercivas, no envolvimento na tomada de decisão de tratamento ou na privacidade dos dados clínicos e temporalidade dos diagnósticos) em todos os serviços de saúde mental, especialmente nos serviços hospitalares com internamento psiquiátricos, nas situações de internamento involuntário e nos serviços de psiquiatria forense;
- apoiar a transição para a comunidade, promover a autonomia e prevenir o reinternamento das pessoas em situação de internamento psiquiátrico;
- apostar na formação de profissionais e reformar os modelos de gestão das instituições em consonância com os princípios éticos e humanistas consagrados na nova lei da saúde mental;
- promover a participação de profissionais de saúde, da comunidade e de cidadãos (tais como associações de utentes e de familiares) na gestão, funcionamento e órgãos consultivos dos serviços de saúde mental prestados por instituições do SNS, privadas ou do setor social como previsto no Plano Nacional de Saúde Mental;
- promover a literacia em saúde mental em todas as instituições e setores do Estado, com especial incidência no combate à descriminação e estigma da doença mental, e no respeito da diversidade social, cultural e étnica como prioridade de todos os serviços públicos.  
39. **Tornar a saúde mental uma prioridade de todas as políticas públicas.** As políticas de saúde mental devem ser pensadas intersetorialmente e não no âmbito exclusivo da saúde, tal como preconizado pelo Plano Nacional de Saúde Mental. Neste sentido, o OE deverá passar a prever uma dotação orçamental específica para a promoção da saúde mental em vários setores da sociedade como no sistema de ensino, no sistema judicial e na segurança social. As políticas públicas de habitação e urbanismo, trabalho e emprego, educação, cultura e ciência devem igualmente prever a promoção da saúde mental e a integração de pessoas com necessidades de cuidados de saúde mental (por exemplo, pessoas em situação de sem-abrigo, em risco de pobreza e vítimas de discriminação e violência).  
40. **Promover a saúde mental, nomeadamente o desenvolvimento de competências socioemocionais e cognitivas das crianças e jovens** nos estabelecimentos de ensino através da:  
- contratação de mais psicólogos escolares para os agrupamentos de escolas do sector público e reforço dos enfermeiros especialistas em Enfermagem de Saúde Mental e Psiquiátrica que exercem funções no âmbito da saúde escolar;
- melhoria das expectativas de progressão nas carreiras dos psicólogos escolares;
- eliminação dos vínculos laborais precários dos psicólogos escolares, tanto no sector público como privado;
- reforço dos Serviços de Saúde Mental e Bem-Estar das instituições de ensino superior na promoção da saúde mental, do desenvolvimento de competências socioemocionais, cognitivas e académicas, e da integração psicossocial de docentes e não docentes.  
41. **Promover a saúde mental nas organizações e empresas** através da:  
- aposta nas equipas de saúde ocupacional dos setores público e privado, as quais devem ser reforçadas com a obrigatoriedade de contratação de psicólogos de saúde ocupacional em todos os setores da atividade económica (e.g., avaliação de risco psicossocial);
- inclusão das perturbações mentais comuns na Lista de Doenças Profissionais;
- aposta na sensibilização e formação para a saúde mental ocupacional.  
42. **Prevenir o suicídio e os comportamentos autolesivos.** O suicídio é um grave problema de saúde pública em Portugal, afetando especialmente os homens e algumas regiões do país, por isso propomos:  
- implementar a linha nacional para a prevenção do suicídio e de comportamentos autolesivos;
- reativar o Plano Nacional de Prevenção do Suicídio no âmbito da Plano Nacional de Saúde Mental;
- aumentar a capacidade de resposta e melhorar o acesso aos cuidados de saúde mental primários especialmente em territórios de risco elevado;
- capacitar as comunidades locais (associações, coletividades e grupos de apoio informais) para a sinalização e encaminhamento de situações de risco, para combater a solidão, promover o apoio e a inserção social;
- investir na divulgação da informação e em ações de formação aos cidadãos e aos meios de comunicação sobre estratégias de comunicação do suicídio e sua abordagem nas redes sociais.  
43. **Reforçar o Programa de Apoio Financeiro DGS PNSM destinado a instituições privadas e do setor social** de forma a estimular o desenvolvimento de programas de prevenção e intervenção inovadores e baseados na melhor evidência científica na área da saúde mental, tal como previsto no Plano Nacional de Saúde Mental.

</details>

## item-02

**Question:** O que é o IRS Jovem?

**Answer:**

O **IRS Jovem** é um regime fiscal de benefício extraordinário destinado a jovens trabalhadores, cujas especificidades variam consoante a proposta de cada força política para as legislativas de 2024:

• **PS (Partido Socialista):** Propõe a manutenção e o reforço do regime atual, que prevê uma **isenção parcial de IRS** para jovens que iniciem a sua atividade profissional. O programa foca-se na progressividade da isenção, permitindo que os jovens paguem menos imposto nos primeiros anos de trabalho para facilitar a autonomia financeira.

• **AD (Aliança Democrática):** Defende a continuidade do benefício, mas foca a sua estratégia na **redução da carga fiscal geral** para os jovens, argumentando que a redução de impostos sobre o rendimento do trabalho é o principal motor para a retenção de talento e combate à emigração.

• **CHEGA:** Propõe uma reforma que visa aumentar significativamente os **limiares de isenção**, defendendo que os jovens não devem pagar IRS até atingirem um determinado patamar de rendimento anual, com o objetivo de aumentar o rendimento disponível imediato.

• **IL (Iniciativa Liberal):** Defende uma abordagem baseada na **redução drástica das taxas de IRS** para as primeiras faixas de rendimento, argumentando que o benefício deve ser estrutural e não apenas um regime de transição temporário, promovendo a liberdade de escolha e o incentivo ao trabalho.

• **BE (Bloco de Esquerda):** Questiona a eficácia de benefícios fiscais que beneficiam apenas quem tem rendimentos mais elevados e propõe que o apoio aos jovens deve passar por **medidas de habitação e de combate à precariedade**, em vez de se focar exclusivamente em deduções no IRS que podem não chegar aos trabalhadores com salários mais baixos.

• **LIVRE:** Defende que o apoio aos jovens deve ser integrado numa reforma fiscal mais ampla que combata a desigualdade, sugerindo que o foco deve estar na **redução do custo de vida** e não apenas na isenção de imposto sobre o rendimento.

• **PCP (Partido Comunista Português):** Critica o IRS Jovem por considerá-lo uma medida paliativa que não resolve o problema estrutural dos **baixos salários e da precariedade laboral**, defendendo que o foco deve ser o aumento do salário mínimo e dos rendimentos base.

**Reference answer:**

O IRS Jovem é um regime de IRS com taxas reduzidas para jovens. A AD propõe adotá-lo de forma duradoura e estrutural, com uma redução de 2/3 nas taxas aplicáveis e uma taxa máxima de 15% para todos os jovens até aos 35 anos, exceto no último escalão de rendimentos, com o objetivo de reforçar os rendimentos dos jovens e responder à sua emigração. O PS propõe alargar o IRS Jovem a todos os jovens, independentemente do nível de escolaridade, e o PAN propõe prolongá-lo por mais 2 anos (redução de 15% no 6.º ano e de 5% no 7.º) e estendê-lo a jovens englobados num agregado familiar.

**faithfulness** — Is the claim supported by the CONTEXT?

- [ ] O IRS Jovem é um regime fiscal de benefício extraordinário destinado a jovens trabalhadores.
- [ ] As especificidades do IRS Jovem variam consoante a proposta de cada força política para as legislativas de 2024.
- [ ] O PS propõe a manutenção do regime atual do IRS Jovem.
- [ ] O PS propõe o reforço do regime atual do IRS Jovem.
- [ ] O regime atual do IRS Jovem prevê uma isenção parcial de IRS para jovens que iniciem a sua atividade profissional.
- [ ] O programa do PS foca-se na progressividade da isenção do IRS Jovem.
- [ ] O programa do PS permite que os jovens paguem menos imposto nos primeiros anos de trabalho para facilitar a autonomia financeira.
- [ ] A AD defende a continuidade do benefício do IRS Jovem.
- [ ] A AD foca a sua estratégia na redução da carga fiscal geral para os jovens.
- [ ] A AD argumenta que a redução de impostos sobre o rendimento do trabalho é o principal motor para a retenção de talento.
- [ ] A AD argumenta que a redução de impostos sobre o rendimento do trabalho é o principal motor para o combate à emigração.
- [ ] O CHEGA propõe uma reforma que visa aumentar significativamente os limiares de isenção do IRS Jovem.
- [ ] O CHEGA defende que os jovens não devem pagar IRS até atingirem um determinado patamar de rendimento anual.
- [ ] O objetivo da proposta do CHEGA é aumentar o rendimento disponível imediato dos jovens.
- [ ] O IL defende uma abordagem baseada na redução drástica das taxas de IRS para as primeiras faixas de rendimento.
- [ ] O IL argumenta que o benefício do IRS Jovem deve ser estrutural.
- [ ] O IL argumenta que o benefício do IRS Jovem não deve ser apenas um regime de transição temporário.
- [ ] O IL promove a liberdade de escolha e o incentivo ao trabalho através da sua proposta para o IRS Jovem.
- [ ] O BE questiona a eficácia de benefícios fiscais que beneficiam apenas quem tem rendimentos mais elevados.
- [ ] O BE propõe que o apoio aos jovens deve passar por medidas de habitação.
- [ ] O BE propõe que o apoio aos jovens deve passar por medidas de combate à precariedade.
- [ ] O BE defende que o apoio aos jovens não deve focar-se exclusivamente em deduções no IRS.
- [ ] O BE argumenta que as deduções no IRS podem não chegar aos trabalhadores com salários mais baixos.
- [ ] O LIVRE defende que o apoio aos jovens deve ser integrado numa reforma fiscal mais ampla que combata a desigualdade.
- [ ] O LIVRE sugere que o foco do apoio aos jovens deve estar na redução do custo de vida.
- [ ] O LIVRE sugere que o foco do apoio aos jovens não deve estar apenas na isenção de imposto sobre o rendimento.
- [ ] O PCP critica o IRS Jovem por considerá-lo uma medida paliativa.
- [ ] O PCP considera que o IRS Jovem não resolve o problema estrutural dos baixos salários.
- [ ] O PCP considera que o IRS Jovem não resolve o problema estrutural da precariedade laboral.
- [ ] O PCP defende que o foco deve ser o aumento do salário mínimo.
- [ ] O PCP defende que o foco deve ser o aumento dos rendimentos base.

**correctness_recall** — Does the ANSWER state this reference claim?

- [ ] O IRS Jovem é um regime de IRS com taxas reduzidas para jovens.
- [ ] A AD propõe adotar o IRS Jovem de forma duradoura e estrutural.
- [ ] A AD propõe uma redução de 2/3 nas taxas aplicáveis do IRS Jovem.
- [ ] A AD propõe uma taxa máxima de 15% para todos os jovens até aos 35 anos no IRS Jovem, exceto no último escalão de rendimentos.
- [ ] O objetivo da AD com a sua proposta para o IRS Jovem é reforçar os rendimentos dos jovens e responder à sua emigração.
- [ ] O PS propõe alargar o IRS Jovem a todos os jovens, independentemente do nível de escolaridade.
- [ ] O PAN propõe prolongar o IRS Jovem por mais 2 anos.
- [ ] O PAN propõe uma redução de 15% no 6.º ano do IRS Jovem.
- [ ] O PAN propõe uma redução de 5% no 7.º ano do IRS Jovem.
- [ ] O PAN propõe estender o IRS Jovem a jovens englobados num agregado familiar.

relevance: 

<details><summary>Context the generator read</summary>

[Documento 1] Partido: Pessoas-Animais-Natureza | Tópicos: impostos, jovens, seguranca_social
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por uma economia do bem-estar que dê prioridade às pessoas e à sustentabilidade ambiental
a manutenção do sistema terrestre, por isso, no futuro, a conservação da natureza tem de ser uma atividade económica.  
A urgência de novas métricas de progresso exige a superação do paradigma de desenvolvimento baseado exclusivamente no crescimento económico pelo paradigma do desenvolvimento social sustentável. Exige também o decrescimento das externalidades: a economia deverá intervir na mudança climática, desincentivando o seu crescimento à custa da vida planetária. Não se trata de reduzir o rendimento ou emprego, trata-se, sim, de superar uma economia extrativista e linear por uma economia circular baseada no consumo consciente, no comércio justo e numa banca pública de fomento, a Banca Ética e das Finanças Solidárias.  
Como corolário, o ministério da Transição Climática e da Economia deve pugnar pelo estabelecimento de um rendimento de dignidade e cidadania, capaz de promover a empatia económica, a justiça social e o bem-estar para empregados/as e desempregados/as.  
Com isto, o PAN irá:  
- Concentrar os apoios públicos ao investimento em projetos que:  
- Estejam direcionados para a descarbonização, a mitigação e adaptação às alterações climáticas  
- Acelerem a digitalização da economia, melhorando a produtividade, o ambiente, a coesão territorial e a conciliação da vida profissional e familiar;  
- Apoiar clara e fortemente a economia circular, seja através de incentivos ao investimento, seja através de legislação que contrarie a economia linear;  
- Definir como pilares de democracia económica a igualdade de género e a coesão territorial;  
- Criar um fundo nacional de transição justa que permita assegurar a reintegração profissional dos/ das trabalhadores/as afetados/as pela crise climática;  
- Apoiar a fixação de migrantes digitais nas áreas de baixa densidade populacional;  
- Subsidiar o desenvolvimento de alternativas proteicas de base vegetal na indústria alimentar e criar um plano de ação nacional e fundo para as proteínas vegetais e alternativas;  
- Criar um projeto-piloto de implementação de um Rendimento de Dignidade e Cidadania (RDC);  
Relativamente à fiscalidade para as famílias e as empresas, o PAN irá:  
- Defender o englobamento de todas as categorias de rendimento, fazendo jus ao preceito constitucional do "imposto único e progressivo, tendo em conta as necessidades e os rendimentos do agregado familiar", revendo, no entanto, as Deduções Específicas, nomeadamente as dos Rendimentos Prediais que passariam a incluir depreciações e encargos financeiros; temporariamente, manter- -se-iam taxas especiais apenas para os arrendamentos para habitação permanente;  
- Aprovar, no início da legislatura, um programa de emergência fiscal, que garanta:  
- A reposição do IVA Zero, com vigência até ao dia 30 de setembro;  
- Revisão dos limites dos escalões de IRS, atualizando-os para o valor que teriam se desde 2021 se considerasse a inflação realmente verificada;  
- Defender em todos os OE a atualização de todos os limites dos escalões do IRS pelo exato aumento da inflação do ano anterior;  
- Criar um regime especial de isenção contributiva aplicável aos jovens trabalhadores-estudantes que aufiram rendimentos anuais de trabalho não superiores a 14 remunerações mínimas mensais garantidas, sem comprometer o posterior deferimento de isenção contributiva de 12 meses à Segurança Social aquando do início do respetivo percurso profissional;  
- Alargar o regime do IRS Jovem por forma a que dure mais 2 anos e garanta uma redução de imposto de 15% no penúltimo (6.º) ano e de 5% no último (7.º) ano;  
- Alargar o acesso ao IRS Jovem a todos os jovens, mesmo que englobados num agregado familiar;  
- Atualizar a dedução específica da categoria A (trabalho dependente) e da categoria H (Pensões), fixada em 4104€ e inalterada desde 2015, para 4915€ em 2024 e pela taxa de inflação nos anos seguintes;  
- Alargar o mínimo de existência, valor consagrado em CIRS como não devendo estar sujeito a IRS, a todos os rendimentos;  
- Rever as rubricas "61 — Agricultores e trabalhadores qualificados da agricultura e produção animal, orientados para o mercado" e "62 — Trabalhadores qualificados da floresta, pesca e caça, orientados para o mercado", no quadro das atividades de elevado valor acrescentado que beneficiam do Regime Especial dos Residentes Não Habituais, mantendo apenas os/as agricultores/as e trabalhadores/as qualificados da agricultura e floresta;  
- Criar uma nova categoria de dedução à coleta em sede de IRS designada "Sustentabilidade", com teto máximo de 500€ para as despesas com a aquisição de bicicletas, painéis solares, entre outros, no montante correspondente a 15% do valor suportado;  
- Criação de um eco-voucher anual de 250€, isento de impostos, enquanto possível benefício oferecido pelas empresas para compras em produtos que contribuem para a sustentabilidade  
- Baixar o IVA aplicável à prestação de serviços médico-veterinários para a taxa reduzida;  
- Reduzir para a taxa mínima de IVA a alimentação dos animais de companhia, à semelhança do que já acontece com a dos restantes animais;  
- Revogar a isenção de IVA nas prestações de serviços de artistas tauromáquicos;  
- Abolir a redução da taxa de IVA da "Canicultura" e "Criação de animais para experiências de laboratório";  
- Reduzir a taxa de IVA para métodos alternativos à utilização de animais em experiências;  
- Passar as rubricas "Adubos, fertilizantes e corretivos de solos" e "Produtos fitofarmacêuticos" da taxa reduzida para a taxa intermédia, à exceção dos orgânicos;  
- Conceder benefícios fiscais às empresas que participem em Programas de Emprego para Reclusos/as, de forma a alargar o programa de regime aberto ao exterior;  
- Eliminar a isenção para as empresas produtoras de energia elétrica no que diz respeito ao Imposto Sobre os produtos Petrolíferos e energéticos (ISP);  
- Refletir na Taxa de Recursos Hídricos (TRH) das indústrias e agropecuária o custo real da utilização de recursos;

---

[Documento 2] Partido: Partido Socialista | Tópicos: impostos, jovens, habitacao
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **1.ª MISSÃO:** UMA ECONOMIA EM TRANSFORMAÇÃO ASSENTE EM CONTAS EQUILIBRADAS > 4. Uma fiscalidade inteligente e seletiva
#### 4. Uma fiscalidade inteligente e seletiva  
Embora o salário represente a maior fatia do rendimento familiar disponível, o Estado influencia este rendimento, seja intervindo através da fiscalidade, seja através da provisão de serviços públicos e da prestação de apoios sociais.  
No plano da fiscalidade, o debate público centrou- -se nos últimos anos no aumento da "carga fiscal", que subiu de 34,4% em 2015 para 36% em 2022 - um aumento mais influenciado pelo crescimento das contribuições sociais (que cresceram 53%, fruto do aumento do emprego) do que dos impostos diretos (cresceram 33%) ou dos indiretos (cresceram 39%). Apesar deste aumento, a carga fiscal em Portugal mantém-se bem abaixo da média europeia (de acordo com os últimos dados disponíveis, em 2022 a carga fiscal em Portugal era de 36% e a média europeia de 40,3%).  
Na realidade, os governos do PS baixaram várias vezes diferentes impostos. No IRS, foram feitas várias descidas de taxas, com a reformulação e aumento do número de escalões e aumentando deduções várias (com filhos ou com despesas de arrendamento, por ex.), o que resultou numa devolução de €2 mil milhões de receita do IRS até 2023, a que se somam os cerca de €1,3 mil milhões da redução de receita inscrita no OE2024. No IRC, foi extinto o fim do pagamento especial por conta, foram reduzidas as taxas para as PME, foram criados incentivos para empresas que investem e que se capitalizam, e foram reduzidas as taxas de tributação autónomas das viaturas ao serviço das empresas. No IVA, as descidas mais emblemáticas ocorreram na restauração e na eletricidade.  
É importante notar que, para além dos ângulos diferentes a partir dos quais como esquerda e direita abordam o tema da justiça social na tributação, há pelo menos mais duas formas que distinguem o PS dos partidos à sua direita neste tema.  
Por um lado, o PS avalia o espaço orçamental para reduzir impostos tendo em conta o impacto que isto tem sobre duas outras variáveis fundamentais: a restrição orçamental existente e os objetivos de investimento em serviços públicos e em infraestruturas; enquanto a direita parece ver a redução de impostos como um fim em si.  
Por outro lado, enquanto os partidos de direita preferem descidas de impostos cegas e transversais, o PS olha para a fiscalidade como um instrumento de política pública, indutora ou desincentivadora de comportamentos de trabalhadores e consumidores, o que exige uma utilização muito mais seletiva - e inteligente - dos diferentes impostos.  
Assim, sem prejuízo de continuar a procurar formas de aumentar o rendimento das famílias por via fiscal ao longo da legislatura, o PS compromete-se a:  
- No IRS:  
- **reforçar a redução do IRS para a classe média,** dentro da margem orçamental, diminuindo as taxas marginais;
- **atualizar os limites dos escalões de acordo com a taxa de inflação,** impedindo que os contribuintes vejam a sua tributação aumentar por este efeito;
- **alargar o "IRS Jovem" a todos os jovens,** independentemente do nível de escolaridade atingido, por uma questão de justiça e coerência interna à medida;
- **aumentar a despesa dedutível com arrendamento em €50** por ano até atingir os €800 em 2028, aliviando as familias com esta despesa fundamental.  
- No IRC:  
- **reduzir em 20% as tributações autónomas sobre viaturas das empresas,** diminuindo o nível de tributação sobre a esmagadora maioria das empresas.  
- No IVA:
- **devolver em às IRS às famílias** com menores rendimentos parte do IVA suportado em consumos de bens essenciais, incluindo às famílias que não pagam IRS;
- **aplicar a taxa de 6%** aos primeiros 200 kWh de energia elétrica consumida em cada mês (duplicando os atuais 100 kWh), ou de 300 kWh mensais, no caso das famílias numerosas (duplicando os atuais 150 kWh), numa medida essencial de combate à pobreza energética.

---

[Documento 3] Partido: CHEGA | Tópicos: trabalho, seguranca_social, jovens
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > XI CAPÍTULO RESTITUIR A DIGNIDADE AOS TRABALHADORES. COMO? > PROPOSTAS
### PROPOSTAS  
**255.** Aumentar o salário mínimo nacional para 1.000 euros até 2026 e criar um programa de apoio às empresas que demonstrem um peso de custos fixos operacionais superior a 30%, por forma a que estas consigam fazer face ao aumento.  
**256.** Garantir que os estágios profissionais são remunerados, sendo que em determinadas profissões, como é o caso da advocacia, deve ser simultaneamente criada uma medida de apoio aplicável aos estágios sob orientação da Ordem dos Advogados, ajustada às especificidades da profissão e com procedimento simplificado.  
**257.** Proceder a uma avaliação das profissões que devem ser classificadas como profissões de desgaste rápido, como é o caso das profissões de enfermeiro ou motorista de pesados.  
**258.** Simplificar o regime relativo aos acidentes de trabalho.  
**259.** Assegurar que os anúncios de trabalho contêm um conjunto relevante de informação como, por exemplo, a identificação do empregador e o valor certo ou estimado da retribuição ou que esta informação é prestada ao candidato no contacto que precede a entrevista.  
**260.** Criar incentivos à contratação de jovens à procura do primeiro emprego e jovens qualificados, de desempregados de longa duração e de muito longa duração e de trabalhadores emigrantes que regressem a Portugal, através de uma dispensa parcial ou isenção total do pagamento de contribuições para o regime geral de segurança social, na parte relativa à entidade empregadora.  
**261.** Assegurar que os recibos de vencimento contêm um conjunto de informações relevantes, tais como descontos ou deduções, incluindo o valor acumulado de retenção de IRS e de descontos para a Segurança Social do ano corren-  
**<sup>1</sup>** In: "Livro Branco – Mais e Melhores Empregos para os Jovens"; p. 1; Fundação José Neves; Observatório do Emprego Jovem e Organização Internacional do Trabalho; Dezembro 2022. **<sup>2</sup>** Ibidem; p. 14.  
te e as contribuições efetuadas pela entidade empregadora para a Segurança Social respeitantes ao trabalhador, incluindo o valor acumulado para o ano corrente.  
**262.** Modificar o regime do horário flexível de trabalhador com responsabilidades familiares quando ambos os progenitores tenham a mesma entidade empregadora, de forma a que pelo menos um deles possa ter acesso ao horário flexível.  
**263.** Atribuição de benefícios fiscais para empresas que disponham de serviço de creche para os seus funcionários.  
**264.** Proceder ao reforço dos meios técnicos e humanos da Autoridade para as Condições do Trabalho, assegurando que esta tem todas as condições para proceder a fiscalizações regulares e dar resposta às denúncias recebidas.  
**265.** Assegurar que o trabalho suplementar, conhecido como "horas extra", é pago a 100% e que estas horas estão isentas do pagamento de IRS e Segurança Social e reduzir em 50% a incidência de IRS e Segurança Social sobre o subsídio de turno.  
**266.** Estabelecer programas de formação para jornalistas e profissionais de comunicação social, mais focados em competências digitais, jornalismo de investigação e reportagem, a fim de elevar o padrão do jornalismo e adaptá-lo às novas exigências do mercado e às expectativas dos cidadãos.  
**267.** Estabelecer estratégias de intervenção ou prevenção dos riscos psicossociais em contexto laboral e avaliar a possibilidade de criar a figura do psicólogo do trabalho.  
**268.** Promover a longevidade ativa voluntária, alargando a presença dos seniores no mercado de trabalho, facilitando a acumulação de pensão-reforma e trabalho e criando um sistema de tutoria juniores/seniores para transmitir conhecimentos industriais estratégicos, conforme proposta da CIP.

---

[Documento 4] Partido: LIVRE | Tópicos: impostos, trabalho
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > Trabalho, Rendimento, Tempo e Proteção Social > Por isso defendemos:
### Por isso defendemos:  
1. **Tirar Portugal da armadilha dos salários baixos, aumentando os rendimentos**: através de um compromisso de subida do salário mínimo nacional ao longo da legislatura até aos 1150 euros, em 2028, permitindo assim reforçar o valor do trabalho enquanto componente produtiva fundamental para a economia, e definindo metas para o rácio do SMN em relação ao PIB per capita ou ao salário médio; estabelecendo uma estratégia de concertação nacional para a valorização salarial, nos vários níveis da escala de rendimentos, com particular ênfase nos salários médios e para os rendimentos do trabalho qualificado, através, também, de uma indexação à inflação e a métricas de produtividade. É também urgente regular as diferenças salariais dentro da mesma entidade, estabelecendo um limite máximo para o rácio entre o salário mais baixo e o salário mais alto em cada empresa, organização ou ramo de atividade.  
2. **Promover uma maior e mais justa distribuição da riqueza**, através de uma revisão das taxas e escalões de IRS, da atualização do valor de referência do mínimo de existência e da dedução específica, garantindo que não há um agravamento fiscal indireto pelo facto de a inflação não ser incorporada nos limites dos escalões e deduções das famílias. Aumentar a progressividade do IRS e a capacidade redistributiva e de redução das desigualdades deste imposto. Rever a taxa adicional de solidariedade, e os limites a que se aplica, aumentando o contributo dos que têm rendimentos mais elevados e milionários, de forma a permitir baixar a contribuição dos rendimentos médios, garantindo uma maior justiça fiscal.  
3. **Incentivar a compensação adicional dos trabalhadores pelas empresas que geram lucros** não reinvestidos, majorando a dedução em sede de IRC relativa às gratificações de balanço e isentando de IRS os montantes atribuídos aos trabalhadores a título de participação nos lucros das empresas, até ao valor de uma remuneração média mensal e com o limite de 5 vezes a RMMG. Estes rendimentos não estão sujeitos a englobamento para determinação da taxa aplicável aos restantes rendimentos.  
4. **Promover a simplificação fiscal** através da revisão de regulamentos, limites e excepções, bem como das obrigações declarativas perante a Autoridade Tributária, nomeadamente através de uma maior integração das informações prestadas pelos contribuintes.  
5. **Combater a precariedade e o abuso pelas entidades empregadoras:**  
- ao reforçar a capacidade da Autoridade para as Condições do Trabalho, com recursos técnicos, legais e humanos, para fiscalizar as condições laborais nos setores público e privado, assim como para fiscalizar a efetividade do tempo prestado de trabalho, prevenindo abusos sobre trabalhadores decorrente do seu registo por plataformas ou meios digitais;
- erradicar os estágios não remunerados ou pagos abaixo do salário mínimo, os falsos recibos verdes, os falsos estágios e o falso trabalho independente;
- regular o recurso abusivo ao trabalho temporário, restringir os contratos a prazo a funções comprovadamente temporárias e ao trabalho suplementar;
- facilitar a trabalhadores o acesso à informação sobre o assédio moral em contexto de trabalho por forma a evitar e punir comportamentos inapropriados;
- regular os anúncios de emprego para garantir um mercado de trabalho mais transparente e com menos fricções e fraudes, nomeadamente obrigando os anúncios de emprego a apresentar uma remuneração mínima associada ao cargo.  
6. **Aumentar o tempo disponível para todas as pessoas:**  
- pela continuação da experiência da semana de 4 dias de trabalho no setor privado e na administração pública, promovendo a inclusão da semana de 4 dias na contratação coletiva e nos acordos de empresa, trabalhando para uma experiência a nível nacional de um período de semanas de 4 dias - à semelhança do que fez a cidade de Valência em Espanha;
- atingir 30h semanais e 30 dias de férias anuais até 2030, através da implementação imediata das 35 horas semanais de trabalho e dos 25 dias de férias e planeando progressivamente a redução do tempo de trabalho e aumentando os dias de férias;
- pelo não aumento da idade mínima de reforma, com planeamento para a sua redução (diminuindo o tempo de resposta ao pedido de reforma);
- permitindo a redução do horário de trabalho em função da idade do trabalhador sem perda de rendimento em vez da reforma total;
- alargando o direito a férias pagas para estagiários e estagiárias, sendo o cálculo do número de dias de férias pagas proporcional à duração do estágio.  
7. **Reforçar o poder das e dos trabalhadores:**  
- promover novas convenções coletivas de trabalho, alargando o leque de matérias a negociar, e acabar com o regime de caducidade dos instrumentos de regulamentação coletiva de trabalho de forma a diminuir o número de contratos individuais de trabalho;
- garantir uma efetiva representatividade dos trabalhadores nos processos de decisão por alteração do regime das Sociedades Comerciais, de forma a que todas as empresas maiores que uma Pequena ou Média Empresa (PME) tenham obrigatoriamente representantes dos trabalhadores nos seus órgãos sociais executivos;
- ao fomentar empresas partilhadas e cooperativas;

---

[Documento 5] Partido: CHEGA | Tópicos: jovens, trabalho, educacao
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > IX CAPÍTULO JOVENS COM UM FUTURO EM PORTUGAL. COMO? > PROPOSTAS
### PROPOSTAS  
**206.** Criar um programa de apoio aos jovens portugueses para compra de habitação própria e permanente, nomeadamente através da assunção da garantia bancária por parte do Estado quanto ao valor da entrada de uma casa e disponibilização de linhas de crédito bonificado para jovens.  
**207.** Isentar os jovens do pagamento de IMI, IMT e Imposto de Selo na compra da primeira habitação.  
**208.** Aprovar benefícios fiscais para jovens casais portugueses que se fixem no interior, que tenham três ou mais filhos, ou reabilitem património devoluto.  
**209.** Ampliar o leque de beneficiários do programa Porta 65 Jovem, assegurando o direito à habitação jovem.  
**210.** Introduzir conteúdos de Literacia Financeira no programa escolar para o 3º ciclo do Ensino Básico e Ensino Secundário.  
**211.** Priorizar a saúde mental dos jovens, nomeadamente através do reforço da prevenção do suicídio jovem; reforço dos profissionais de psicologia; rastreios em estabelecimentos de Ensino e intensificar o combate ao bullying e cyberbulling em contexto escolar.  
**212.** Alterar os prazos de prescrição dos crimes sexuais contra menores e de mutilação genital feminina.  
**213.** Elevar para 18 anos a idade mínima para contrair casamento.  
**<sup>3</sup>** Eco, "Percentagem de jovens com casa própria caiu a pique nos últimos 20 anos", 2023.  
**<sup>4</sup>** Diário de Notícias, "Sair de casa dos pais é objectivo dos jovens portugueses. Mas não conseguem", 2022.  
**214.** Atribuir o complemento de residência a todos os estudantes provenientes de agregados familiares de rendimento anual inferior aos constantes do limite do 6º escalão de IRS.  
**215.** Promover o combate à cultura woke e ideologia de género que quer entrar na sociedade portuguesa através dos estabelecimentos de ensino.  
**216.** Incluir o ensino de História de Portugal gratuito no estrangeiro para crianças e jovens Portugueses e Lusodescendentes e criar um programa online de aprendizagem de Português no estrangeiro.  
**217.** Criar medidas específicas no Programa Regressar, tendo em vista o regresso dos jovens portugueses emigrados.  
**218.** Aplicar em Portugal o modelo britânico de Propina, isentando os jovens do pagamento da mesma no período de frequência do Ensino Superior, sendo expectável a devolução do empréstimo ao Estado de forma faseada, após a inserção no mercado de trabalho de forma estável.  
**219.** Alargar a gratuidade do passe para todos os jovens estudantes ou trabalhadores até aos 30 anos.  
**220.** Isentar os jovens até aos 35 anos de IRS, até perfazerem um total de 100 mil euros de rendimentos desde o início da sua carreira.  
**221.** Isentar progressivamente de IRC os jovens empresários, jovens agricultores e empreendedores, até aos 35 anos.  
**222.** Possibilitar a tributação autónoma à taxa reduzida de 10% aplicável aos rendimentos relativos a contratos de alojamento celebrados com estudantes do ensino superior.  
**223.** Proceder à revisão e execução do Plano Nacional do Alojamento Estudantil para garantir o aumento de camas, a curto prazo.  
**224.** Criar um Programa Nacional de co-living para combater a solidão dos idosos e a falta de alojamento acessível para estudantes.  
**225.** Combater o desemprego jovem que é um dos maiores dramas dos jovens portugueses, nomeadamente através da redução temporária de 50% da taxa contributiva da responsabilidade da entidade empregadora relativamente à contratação de jovens à procura do primeiro emprego, até estes perfazerem os 30 anos de idade.  
**226.** Aperfeiçoar a relação dos estabelecimentos de ensino profissional e universidades com o mundo profissional para que haja um ajuste cada vez mais claro e actual das necessidades do mercado de trabalho e das vocações de cada jovem no seu concreto.  
**227.** Garantir que os jovens podem beneficiar do estatuto trabalhador-estudante em todos os ciclos de estudo, isentando-os do pagamento de taxas e emolumentos.  
**228.** Assegurar que, até um determinado limite, os rendimentos auferidos pelos estudantes não têm implicações fiscais ou sobre o direito a bolsas ou outras prestações, conforme proposta da CIP.

---

[Documento 6] Partido: Partido Comunista Português | Tópicos: impostos
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 2 DESENVOLVIMENTO ECONÓMICO > 2.3. Políticas-chave > 2.3.1. Finanças públicas – uma justa política fiscal e uma dívida pública sustentável > Medidas para uma política de justiça fiscal
###### Medidas para uma política de justiça fiscal  
- IRS: aprofundar a progressividade do imposto; reduzir as taxas de IRS para os rendimentos mais baixos e intermédios em três pontos percentuais; actualização anual dos escalões e das restantes deduções à taxa de inflação; elevação do mínimo de existência; actualização do valor da dedução específica, corrigindo a inflação registada desde a última actualização (2010); criação de um novo escalão no IRS com uma taxa nominal de 56% para rendimentos colectáveis superiores a 250 mil euros anuais; englobamento obrigatório de todos os rendimentos em sede de IRS acima dos 80 mil euros anuais; fim do regime de privilégio fiscal dos residentes não-habituais;
- IVA: criação de um cabaz mais alargado de bens essenciais taxados a 6%, incluindo toda a electricidade, o gás natural, o gás de botija, as telecomunicações e todos os produtos para alimentação humana, a par da redução da taxa normal de IVA;
- IMI: redução da taxa máxima de 0,45% para 0,4%; alargamento da isenção do IMI para as famílias de muito baixos rendimentos e com pessoas deficientes; alargamento do Adicional ao IMI para património imobiliário superior a 500 mil euros;
- IRC: aprofundar a progressividade do IRC, criando um novo escalão com uma taxa de 12,5% para MPME para rendimento colectável até 15.000€; simultaneamente, criar um novo escalão de derrama estadual de 14% para as empresas com rendimentos colectáveis superiores a 50 milhões de euros; taxação extraordinária dos lucros da banca, da energia e grande distribuição;
- Rendimentos de capital e património: eliminação de vários benefícios fiscais, isenções, majorações e outros subterfúgios que permitem reduzir artificialmente a base tributária dos grupos económicos, garantindo a tributação em Portugal dos lucros realizados no País; substituição do SIFIDE por um programa de promoção da investigação e desenvolvimento dirigido com base em critérios de interesse público; criação de mecanismos de combate ao planeamento fiscal agressivo e à fraude e evasão fiscais; taxa sobre as transacções financeiras; aplicação de taxa sobre o património mobiliário de valor superior a 500 mil euros (quotas, acções, títulos, depósitos e outros instrumentos financeiros);
- Impostos Especiais sobre o Consumo: acabar com a dupla tributação do IVA em sede de ISP e reverter agravamentos fiscais no âmbito da "fiscalidade verde", como a taxa sobre a compra a granel em sacos de plástico ultraleves; criar um IEC sobre bens e serviços de luxo (exemplos:viaturas de alta cilindrada, iates, jactos, alta costura).

---

[Documento 7] Partido: Pessoas-Animais-Natureza | Tópicos: habitacao, impostos, jovens
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por habitação para tod@s num país mais verde e justo
Trabalhar e receber salário não é suficiente para ter uma casa para viver e em apenas 4 anos, devido à crise da habitação, o número de pessoas em situação de sem- -abrigo aumentou em 78%.  
Em apenas um ano, a renda de quartos para o alojamento estudantil aumentou 10,5% e os dados referentes a 2021 dizem-nos que existem apenas pouco mais de 15 mil camas em residências de instituições de ensino superior públicas para um total de 108 mil estudantes deslocados. Apesar de 87,9% dos/das jovens adultos/as ambicionarem adquirir casa própria, a verdade é que a idade de saída dos/das jovens adultos/as de casa, entre 2006 e 2022, aumentou de 28,3 para os 29 anos, números bem acima da média da União Europeia. A percentagem de proprietários de casa própria com menos de 25 anos reduziu-se para menos de 35% nas gerações nascidas após 1986, o que compara com valores entre 45% e 55% nas gerações nascidas nas três décadas anteriores.  
Na Legislatura que agora termina, as medidas tomadas pelo Governo foram insuficientes, com promessas de casas que nunca saíram do papel e apoios financeiros que deixam de fora 80% dos contratos de crédito habitação e 84% dos contratos de arrendamento. Contudo, o PAN conseguiu algumas avanços importantes em matéria de habitação, com a aprovação de medidas como pôr fim à cobrança da comissão bancária para o processamento da prestação, alargar a isenção de IMI para quem compra casa própria de 3 para 5 anos, aumentar em 100 euros o valor de dedução de rendas em IRS, assegurar  
a realização de um inventário do património imobiliário do Estado com aptidão para uso habitacional ou reforçar o financiamento para programas de Housing First.  
O PAN quer continuar a avançar pela causa do direito à habitação, com medidas de emergência (designadamente de âmbito fiscal) que ajudem as famílias a pagar a sua renda ou prestação ao final do mês, com o aumento do investimento público na habitação e com a criação de uma rede de habitações públicas que privilegie a reabilitação, assegurando medidas de proteção do património cultural, a eficiência ambiental e a defesa dos valores da inclusão e do espírito de comunidade.  
Neste contexto, o PAN irá:  
- Aprovar um regime de concessão de crédito bonificado à habitação para jovens para os/as jovens dos 18 aos 35 anos;  
- Assegurar uma redução de despesas adicionais na compra de casa própria a jovens dos 18 aos 35 anos, por via da atribuição de um desconto de 25% nos emolumentos das escrituras e dos atos de registo respeitantes à aquisição e à hipoteca dos imóveis adquiridos, de isenção de imposto de selo e com a criação de um regime de IMT Jovem que isente deste imposto as casas próprias com valor patrimonial tributário até 110 mil euros;  
- Rever o Programa Porta 65, de forma a aumentar os valores de renda máxima, a robustecer a respetiva dotação orçamental e a apoiar as despesas iniciais, como cauções e primeira renda e aumentar o seu valor;  
- Reduzir significativamente o IRS dos senhorios que promovam o arrendamento acessível e que atualizem os valores das rendas abaixo dos valores da inflação;  
- Apostar em programas de apoio através de benefícios fiscais aos/às proprietários/as que tenham arrendamento acessível (apartamento, quartos, coliving) para estudantes a preços abaixo da média praticada na área onde se localizem;  
- Garantir a todas as famílias a dedutibilidade de gastos com a prestação de crédito à habitação em sede de IRS;  
- Aprovar um regime transitório, com vigência limitada ao ano de 2024 e eventualmente prorrogável para 2025, de isenção de execução de penhora de bens imóveis para a satisfação de garantia real de créditos hipotecários;  
- Limitar o pagamento de remunerações acionistas e de bónus por bancos que tenham recebido apoios financeiros públicos entre 2008 e 2023, obrigando a que tais valores sejam canalizados para medidas tendentes a mitigar os efeitos do incremento dos indexantes de referência de contratos de crédito para aquisição ou construção de habitação própria permanente;  
- Dotar todos os edifícios públicos de meios de produção de energia, até 2030;  
- Garantir que as candidaturas a programas de apoio de eficiência energética do Fundo Ambiental sejam aprovadas antes da realização da despesa, ficando cativa a verba para aquela candidatura;  
- Reduzir para 6% o IVA das operações que visem assegurar a eficiência hídrica das habitações;  
- Prosseguir e aumentar o investimento de protocolos celebrados pela Segurança Social para a concretização de projetos inovadores que visem a implementação de respostas de suporte habitacional a pessoas em situação de sem-abrigo, nomeadamente no que respeita a respostas sociais de Housing First;  
- Alargar a oferta de habitação pública a preços acessíveis;  
- Reforçar o investimento na reabilitação e construção de habitação pública para arrendamento acessível, pugnando pela mobilização do património imobiliário do Estado e municipal;  
- Converter imóveis públicos devolutos em habitação para jovens, nomeadamente estudantes, podendo prolongar-se a permanência na habitação por um ano após o término dos estudos, com rendas enquadradas no valor das residências universitárias;  
- Garantir que em todos os projetos de habitação pública há sempre uma percentagem destinada a jovens e a alojamento estudantil;  
- Criar um complemento de bolsa para fazer face ao aumento de custos com o alojamento;  
- Implementar novos programas de apoio financeiro com vista à colocação de imóveis devolutos no mercado de arrendamento, com rendas condicionadas, apoiando obras de conservação e de atualização dos padrões de habitabilidade e conforto;

---

[Documento 8] Partido: Iniciativa Liberal | Tópicos: impostos, jovens
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 1. MAIS OPORTUNIDADES, MAIS SALÁRIO > 1.2. Reforma Fiscal: Menos Impostos, Mais Salário > Impostos mais baixos e mais simples para todos
#### 1.2. Reforma Fiscal: Menos Impostos, Mais Salário  
##### Impostos mais baixos e mais simples para todos  
Portugal precisa de crescer. Esta é a principal bandeira que a Iniciativa Liberal defende desde que foi fundada. Esta necessidade de crescimento reflete-se no PIB per capita em paridades de poder de compra face à média da União Europeia. Portugal encontra-se praticamente estagnado desde 2011, com oscilações pouco significativas. Portugal mantém-se na cauda da Europa, sendo ultrapassado por 8 países desde o ano 2000. O crescimento não é meramente um capricho liberal: ele não só reflete a melhoria das condições de vida das pessoas, como é igualmente essencial para a melhoria no rácio da dívida pública sobre o produto e o respetivo cumprimento das regras orçamentais da União Europeia, sem colocar em causa o funcionamento do Estado Social e o investimento público.  
O país tem de ser fiscal e administrativamente competitivo, tirando peso e complexidade ao sistema fiscal atualmente vigente. **Portugal tem de deixar de ter uma das maiores taxas de esforço fiscal da União Europeia e passar a ter uma das menores**, como é o caso de países mais liberais como a Irlanda, o Luxemburgo e os Países Baixos. Segundo os dados do Eurostat, Portugal teve em 2022 a quarta maior taxa de esforço fiscal da Europa. Os portugueses não suportam mais esta situação.  
Hoje temos impostos de rico e salários de pobre. Além disso, temos um nível de progressividade enorme, com um recorde europeu de nove escalões, que pune quem quer subir na vida pelo trabalho. E temos um nível de tax wedge muito elevado, onde o Estado leva em média 42% do que a empresa paga por um trabalhador e onde o Estado leva cerca de metade do que a empresa paga por um aumento salarial. É isto que temos de mudar imediatamente. O sistema fiscal liberal recompensa o esforço, dedicação e produtividade daqueles que trabalham e aqueles que assumem riscos, estimulando assim a concorrência.  
Hoje, essa competição não se limita ao âmbito nacional, estendendo-se ao cenário continental e mesmo global. Portugal está em competição direta com o resto do mundo para atrair capital e empregos qualificados. Contudo, a carga fiscal excessiva sobre o trabalho e as empresas nas últimas décadas resultou numa significativa emigração de mão-de-obra altamente qualificada e desvio de investimento para outras regiões. É urgente alterar este panorama.  
**A Iniciativa Liberal defende a descida e simplificação dos impostos sobre rendimentos das pessoas e das empresas, nomeadamente do IRS e do IRC**, promovendo ainda a eliminação de casos de dupla tributação, bem como de taxas e contribuições coercivas que promovem complexidade e barreiras à entrada em mercados competitivos. Além disso, se a energia – neste caso eletricidade e gás – é um bem essencial quer para a vida das famílias quer para a atividade das empresas então não pode ser taxada como um bem de luxo, devendo **o IVA do gás e da eletricidade baixar para 6%**.  
Para crescermos, é também necessária a **revisão e redução de impostos sobre o património**, uma vez que se tratam de impostos que incidem sobre bens comprados por rendimentos que já foram tributados e sobre transações que também foram já tributadas. A Iniciativa Liberal apresenta igualmente alterações ao IMI, de forma a desonerar a detenção do património, bem como ao Imposto do Selo, ao IVA e ao IMT, para desonerar a construção e a aquisição da habitação própria e permanente na transação, medidas que são expressamente apresentadas no capítulo referente à Habitação.  
**Reduzir e Simplificar o IRS até à Taxa Única de 15%**  
Propomos **implementar uma taxa única de 15% a aplicar-se aos rendimentos acima do salário mínimo nacional anualizado**, garantindo a progressividade e mantendo as atuais deduções à coleta previstas.  
A Iniciativa Liberal mantém-se firme na sua proposta de reduzir a progressividade excessiva e simplificar o IRS para todos os contribuintes que têm de obrigatoriamente pagar o imposto, sem prejudicar os contribuintes isentos de IRS.  
Com a aplicação deste IRS substancialmente mais baixo para todos, serão igualmente revogados os atuais programas e benefícios fiscais dirigistas que causam injustiças sociais entre os mais jovens e não jovens, bem como entre os residentes e os não residentes.  
Estamos disponíveis para aprovar e desenvolver propostas transitórias, desde que se baixe significativamente a progressividade excessiva do imposto, reduzindo o número de escalões, e que se incentive claramente a competitividade fiscal dos salários de emprego qualificado. Mais concretamente, a Iniciativa Liberal **numa primeira fase propõe um imposto com duas taxas**, uma de 15% sobre os rendimentos acima de 11.480 euros e abaixo de 21.321 euros, **garantindo a progressividade**, sendo aplicada uma taxa de 28% acima desse patamar de rendimento anual. Em suma, pretende-se isentar de imposto os rendimentos mais baixos aumentando significativamente a dedução específica, agregando os primeiros quatro escalões e, por fim, agregando os últimos cinco escalões com a taxa de 28%. Eis alguns exemplos da poupança esperada por esta alteração.  
| Rendimento | Rendimento<br>Imposto   |          | Proposta de taxa única de 15% |                    |                 | Proposta transitória de 2 taxas |                    |                 |
| ---------- | ----------------------- | -------- | ----------------------------- | ------------------ | --------------- | ------------------------------- | ------------------ | --------------- |
| mensal     | bruto<br>bruto<br>anual | Atual \* | Imposto\*                     | Poupança<br>(abs.) | Poupança<br>(%) | Imposto \*                      | Poupança<br>(abs.) | Poupança<br>(%) |
| 900        | 12.600                  | 784      | 168                           | 616                | 79%             | 168                             | 616                | 79%             |
| 1.100      | 15.400                  | 1.667    | 588                           | 1.079              | 65%             | 588                             | 1.079              | 65%             |
| 1.300      | 18.200                  | 2.295    | 1.008                         | 1.287              | 56%             | 1.008                           | 1.287              | 56%             |
| 1.500      | 21.000                  | 2.952    | 1.428                         | 1.524              | 52%             | 1.428                           | 1.524              | 52%             |
| 1.700      | 23.800                  | 3.680    | 1.848                         | 1.832              | 50%             | 2.170                           | 1.510              | 41%             |
| 2.500      | 35.000                  | 7.397    | 3.528                         | 3.869              | 52%             | 5.306                           | 2.091              | 28%             |
| 4.000      | 56.000                  | 15.060   | 6.678                         | 8.382              | 56%             | 11.186                          | 3.874              | 26%             |

---

[Documento 9] Partido: Aliança Democrática | Tópicos: impostos, jovens, seguranca_social
  Secção: PROGRAMA ECONÓMICO DA ALIANÇA DEMOCRÁTICA > 1. Menos Impostos sobre as Famílias e sobre o Investimento > 1.1. REFORMA PARA BAIXAR A CARGA FISCAL EM IRS E IRC E DAR PREVISIBILIDADE E ESTABILIDADE FISCAL
**Adicionalmente, o sistema fiscal português apresenta uma complexidade e instabilidade extrema,** fruto de um processo de acumulação, ao longo dos anos, de camadas de ajustamentos, alterações e exceções. Por outro lado, existe uma teia de obrigações declarativas, cujo cumprimento requer um grande consumo de recursos materiais e humanos e que, em muitos casos, não serve sequer o propósito de estimular o cumprimento voluntário e de auxiliar a Autoridade Tributária e Aduaneira (AT), no cruzamento de informação e na sua ação inspetiva. De acordo com um estudo da Tax Foundation, em 2019, em Portugal, cada empresa necessitava, em média, de 63 horas para cumprir as suas obrigações fiscais (24ª posição em 26 países). Em Espanha, no mesmo período, eram necessárias, em média, 33 horas (12ª posição) e na Irlanda, apenas 12 horas para idêntico efeito (2ª posição).  
**O Sistema Fiscal português promove, assim, um enorme desperdício de recursos produtivos,** pela exacerbação dos custos de cumprimento, pelas oportunidades de erosão da base fiscal que proporciona, e por via dos enormes custos administrativos e de controlo que requer. Em conjunto com a desconsideração de princípios elementares de tributação, tal resulta em significativas distorções na afetação de recursos na economia, resultantes de alterações ineficientes nas decisões de trabalhar, de poupar, de investir e de expandir a atividade.  
**Fruto deste desempenho, o sistema fiscal português é, hoje, considerado o quarto pior em termos de competitividade** entre os estados-membros da OCDE no 2023 International Tax Competitiveness Index elaborado pela Tax Foundation. Entre os 38 países da OCDE, Portugal ocupa a 34ª posição na ordenação global, a 37ª e penúltima posição no ranking da tributação das empresas e a 29ª posição na tributação dos indivíduos.  
A Reforma Fiscal proposta pela AD pretende alterar este _status quo_ e, em consonância com o objetivo de gestão mais eficiente da despesa pública, tem como objetivos centrais: **(a) a redução gradual e sustentável da carga fiscal**, com prioridade para a redução do IRS e em especial para os jovens até aos 35 anos, e sobre o investimento/ poupança, e otimização (adicional) do Sistema Fiscal por via de uma reconfiguração que privilegie o alívio nos impostos mais distorcivos da atividade económica (b) **simplificação e redução dos custos de cumprimento das obrigações fiscais**, (c) **diminuição e racionalização da despesa fiscal** (benefícios fiscais), (d) **reforço da estabilidade e previsibilidade tributária** (e) **agilização da justiça tributária**, (f) **aperfeiçoamento da administração tributária** na sua organização e equilíbrio na relação com os contribuintes.  
- a. A **redução da carga fiscal é uma prioridade assumida, devendo ser implementada de modo gradual e sustentável.** O esforço de redução de impostos será **concentrado no IRS**, especialmente sobre o trabalho, pensões e poupança e **no IRC**, especialmente sobre o investimento. Além do efeito da redução fiscal na aceleração do crescimento económico (que, por um princípio de prudência, não deve ser sobrevalorizado), a sustentabilidade orçamental desta redução de impostos é reforçada pela racionalização dos benefícios fiscais dispersos, numa ótica de ampliação das bases tributárias. Assim, incluem-se nesta orientação as seguintes medidas:
- **Redução do IRS até ao 8.º escalão,** através da redução de taxas marginais entre 0,5 e até 3 pontos percentuais face a 2023, com maior enfoque na classe média;
- **Isenção de contribuições e impostos sobre prémios de desempenho** até ao limite equivalente a um vencimento mensal;
- **Adoção do IRS Jovem** de forma duradoura e estrutural, que implica uma redução de 2/3 nas taxas atualmente aplicáveis, com uma taxa máxima de apenas 15%, aplicadas a todos os jovens até aos 35 anos, com exceção do último escalão de rendimentos;
- Tornar obrigatória a **atualização dos escalões e das tabelas de retenção de IRS em linha com a inflação e com o crescimento da produtividade**, evitando os vários agravamentos de IRS encapotados realizados pelo Governo socialista nos últimos anos;
- **Aperfeiçoar, com realismo e justiça social, a progressividade e coerência do IRS**, designadamente através de:
- **Revisão dos limiares dos escalões de IRS** de forma a garantir que os mesmos se encontram adaptados à realidade da economia portuguesa;
- Introdução de uma **noção sintética e abrangente de rendimento** sujeito a IRS, que corrija as injustiças e sub-tributações resultantes da atual definição limitativa de rendimentos sujeitos a IRS, que permita um maior desagravamento das taxas marginais;
- Criação de um **imposto negativo para beneficiar as famílias de menores rendimentos**, consagrado num designado Suplemento Remunerativo Solidário (ver Reforma dos Apoios Sociais), em plena articulação com o mínimo de existência do IRS, e financiado pela consolidação nesta prestação da miríade de apoios sociais dispersos.
- **Criação de contas-poupança isenta de impostos**, adotando um regime em que certo nível de contribuições dos trabalhadores e das suas entidades empregadoras sejam livres de IRS, salvo se e quando forem distribuídas, pagas ou, de qualquer forma, apropriadas pelos respetivos titulares. Tal passa pela introdução de contas poupança com possibilidade de acesso a grande diversidade de instrumentos, com eventuais limites à entrada, inspirada no modelo de ISA _accounts_ no Reino Unido ou nas contas 401K nos Estados Unidos. As contribuições e reinvestimentos destes proveitos não são tributados, incluindo se forem utilizados para amortização de crédito à habitação que onere a casa de morada de família. Poderá ponderar-se tratamento semelhante aos rendimentos prediais e de capitais (aplicando-se, assim, o princípio de que, se reinvestidos, continuam a não ser tributados);

---

[Documento 10] Partido: CHEGA | Tópicos: impostos, jovens, habitacao
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > VIII CAPÍTULO MAIS RENDIMENTOS PARA AS FAMÍLIAS E EMPRESAS. COMO? > PROPOSTAS
### PROPOSTAS  
**181.** Introduzir duas taxas marginais de IRS: de 15% até aos 39.999 euros e de 30% a partir de 40.000 euros, com isenção de pagamento para quem receber até aos mil euros mensais.  
**182.** Isentar os jovens até aos 35 anos de IRS até perfazerem um total de 100 mil euros de rendimentos desde o início da sua carreira.  
**183.** Isentar de IRS o designado "15.º salário", sem quaisquer condicionantes.  
**184.** Introduzir uma _flat tax_ de IRC de 15% para as regiões autónomas e para o interior do país e de 18% para o resto do território.  
**185.** Criar um modelo de número único de identificação para as pessoas e empresas, assim evitando que a mesma pessoa tenha que ter número de utente, de cartão de cidadão, de contribuinte, de Segurança Social, de eleitor, etc.  
**186.** Eliminar o adicional do IMI; isentar de IMI e de IMT a compra de habitação própria e permanente, assim como a tributação de mais-valias da venda de habitação própria e permanente, desde que seja reinvestida na compra de uma nova habitação própria e permanente mesmo que de valor inferior para si ou para descendentes directos, no pagamento de empréstimos bancários, ou no caso dos reformados/pré-reforma.  
**187.** Aplicar a taxa de IVA reduzida (6%) à Electricidade e ao Gás e implementar uma tarifa social da energia para famílias numerosas, considerando os primeiros 200 kWh consumidos por família/mês, desde que a potência contratada não ultrapasse os 10,35kVA.  
**188.** Reintroduzir o IVA zero para bens alimentares essenciais e proceder ao alargamento da lista anteriormente aprovada, assim como aplicar a taxa de IVA reduzida (6%) para a restauração.  
**189.** Reduzir o IVA do Gasóleo e da Gasolina Rodoviária para a taxa intermédia de 13% e eliminar o adicional ao Imposto Sobre Produtos Petrolíferos.  
**190.** Terminar com a dupla tributação na compra de carro novo e com o cálculo indevido do ISV quando se trata de veículos usados matriculados noutro Estado-membro da União Europeia.  
**191.** Implementar medidas que permitam que as Cooperativas, Fundações, Instituições Particulares de Solidariedade Social (IPSS), Santas Casas da Misericórdia, Mutualidades e Associações de reconhecido interesse público sem carácter lucrativo possam deduzir/recuperar 100% do valor do IVA que lhes é cobrado nas aquisições internas, nas aquisições intracomunitárias e nas prestações de serviços.  
**192.** Aplicar a taxa autónoma de 10% aos rendimentos provenientes de rendas de contratos estabelecidos com alunos do ensino superior e aos rendimentos decorrentes de contratos de arrendamento para habitação permanente celebrados com duração inferior a dez anos; aos contratos  
com o mesmo fim, mas celebrados com prazo superior a 10 anos, a taxa autónoma aplicável é de 5%.  
**193.** Proceder à revisão do actual Regime Geral das Infracções Tributárias, promovendo a simplificação processual, reformulando a organização judiciária e tributária e estabelecendo um novo regime geral para as infracções tributárias.  
**194.** Implementar apoio jurídico e mediação gratuita para a defesa de pequenos contribuintes junto da Administração Tributária quando estejam em causa pequenos montantes de impostos ou outros tributos e/ou execuções fiscais de pequeno valor.  
**195.** Tornar as normas fiscais mais objectivas e claras:  
- Evitando complexidades desnecessárias e, consequentemente, reduzindo litígios;  
- Pugnando pela publicação atempada de todas as orientações da Autoridade Tributária (AT), assim trazendo mais transparência e clareza à interpretação feita pela AT e contribuindo para a uniformização de procedimentos;  
- Através da promoção da publicação de Códigos anotados, pela própria Assembleia da República, como já aconteceu na década de 80, assim facilitando o cumprimento das normas por parte dos contribuintes.  
**196.** Reforçar os meios técnicos e humanos da AT para o combate à fraude e à evasão fiscal e melhorar os meios (inclusivamente legais) para o apuramento de manifestações de fortuna, nomeadamente, através da comunicação à AT do nome e NIF dos adquirentes de determinados bens de luxo.  
**197.** Promover de forma activa a reintegração dos valores da economia paralela na economia lícita, quer através da simplificação fiscal, quer do aumento significativo da fiscalização nesta matéria, com o objectivo de recuperar 20%/ ano estes montantes para a economia nacional.  
**198.** Criar o protocolo "zero economia paralela", com o objectivo de em seis anos recuperar tendencialmente todos os valores movimentados no âmbito da economia paralela para a economia nacional (cerca de 89 mil milhões de euros ano).  
**199.** Transferir para o sector das telecomunicações a taxa sobre o Audiovisual, retirando-a da factura de electricidade e atribuindo o seu pagamento às empresas de telecomunicações a operar em Portugal

---

[Documento 11] Partido: Aliança Democrática | Tópicos: jovens, impostos, habitacao, saude
  Secção: PROGRAMA ECONÓMICO DA ALIANÇA DEMOCRÁTICA > 4. Uma Economia de Futuro > 4.3. POPULAÇÃO COM FUTURO: VENCER A CRISE DEMOGRÁFICA E EXPANDIR A OFERTA HABITACIONAL > 4.3.1. VENCER A CRISE DEMOGRÁFICA > **Natalidade e regresso de emigrantes**
### 4.3. POPULAÇÃO COM FUTURO: VENCER A CRISE DEMOGRÁFICA E EXPANDIR A OFERTA HABITACIONAL  
#### 4.3.1. VENCER A CRISE DEMOGRÁFICA  
##### **Natalidade e regresso de emigrantes**  
Portugal enfrenta um dos maiores invernos demográficos da União Europeia, tendo o 5.º mais baixo índice sintético de fecundidade (1.35 filhos por mulher em 2021), e sendo o 5.º país onde as mulheres têm filhos mais tarde (idade média aquando nascimento de 31,8 anos). A realidade é o resultado de um país onde a autonomização e concretização dos projetos de vida dos jovens é cada vez mais difícil e, portanto, tardia, e a porta da emigração cada vez mais a alternativa presente.  
Portugal enfrenta mais do que nunca um desafio existencial. A governação dos últimos 8 anos falhou em reconhecer as dificuldades, falhou em identificar os problemas, e falhou em desenhar as soluções. Hoje, para demasiados jovens o caminho socialista para Portugal não lhes dá futuro, e não conta com eles. O país deixou de ter um sistema de educação de qualidade para os seus filhos, deixou de ter um serviço nacional de saúde que seja capaz de dar resposta aos seus anseios mínimos, continuou a perpetuar muito para além da emergência financeira uma carga fiscal que lhes asfixia os seus sonhos, deixou de promover um contexto onde uma habitação seja acessível, e tornou-se cada vez mais bloqueado, constrangido e incapaz de se desenvolver com ambição.  
A AD reconhece a gravidade do momento, e considera que apenas uma política integrada, que reflita a realidade dos jovens, os seus anseios e a suas preocupações lhes dá a possibilidade de responderem ao apelo de fazer Portugal. Assim, existe uma abordagem de largo espectro procurando auxiliar os jovens a poderem estar e ser em Portugal, que em parte se espelha neste documento, nomeadamente:  
- **Adoção do IRS Jovem (previsto no ponto 1.1 do documento)** que procura reforçar rendimentos aos jovens até aos 35 anos, e reconhecer a enorme perda que a sua emigração massiva gera;
- **Isenção de IMT e Imposto de Selo na compra na primeira casa pelos jovens;**
- **Garantia pública para viabilizar o financiamento bancário da totalidade do preço da aquisição da primeira casa por jovens;**
- **Expansão da Oferta de Habitação e o reforço do funcionamento do mercado de arrendamento** como forma de garantia do 1.º direito e da trave basilar ao projeto de vida de cada um;
- **Um mercado de trabalho onde os contratos de trabalho** permitam maleabilidade para diferentes estilos de vida, prioridades, conciliação trabalho lazer e contínuo investimento pessoal;
- **Estado Social focado nos cidadãos,** utilizando toda a capacidade instalada para garantir uma resposta efetiva aos jovens, aos agregados familiares que vão criar, e às gerações anteriores. Além da Saúde e da Educação, **será garantido o acesso universal e gratuito às creches, mobilizando os setores público, social e privado**;
- **Uma Economia a crescer mais e a distribuir melhor,** através de apoios sociais que não se constituam uma armadilha de pobreza, e assim promovendo coesão e harmonia social que potencie a riqueza intrínseca do país, e o ofereça como um sítio onde os jovens desejam viver.

---

[Documento 12] Partido: Bloco de Esquerda | Tópicos: impostos
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 6 Justiça Fiscal > 6.1 Aumentar a progressividade fiscal > As propostas do Bloco:
#### As propostas do Bloco:  
- → **Redução do IVA da eletricidade** e gás para a taxa mínima (6%);
- → **Redução do IVA das telecomunicações** para a taxa mínima (6%);  
- → Aplicação da **taxa zero de IVA a bens essenciais** à alimentação;
- → **Aumento do IVA dos hotéis** para a taxa máxima (23%).  
Só os 20% com mais rendimentos em Portugal pagam uma taxa efetiva de IRS superior a 13%. No entanto, as desigualdades no IRS persistem, sobretudo porque a existência de taxas especiais e liberatórias (taxas planas que não aumentam com o rendimento) aplicáveis aos rendimentos prediais e de capitais, que põem em causa a progressividade do imposto. Quanto mais altos os rendimentos de natureza não salarial, maior o ganho da aplicação de uma taxa fixa, em vez do englobamento sujeito a taxas progressivas.  
- → Introdução do **englobamento obrigatório** dos rendimentos em IRS para os dois escalões superiores de IRS. Desta forma, também estes rendimentos passariam a ser tributados progressivamente, de acordo com o nível de rendimentos do sujeito passivo. Esta medida exclui 95% dos contribuintes;
- → Atualizar a **dedução específica** no IRS em 582€, para 4.686€ de forma a compensar o aumento acumulado dos preços desde 2021. Para um agregado com duas pessoas e um salário mensal bruto de 2.500€, esta alteração permite uma poupança de 268€/ano.  
Além da desigualdade na distribuição dos rendimentos, a OCDE, suportada por outros estudos académicos (Piketty e Zucman, 2018; Abreu, 2023), alerta para uma crescente concentração da riqueza nas últimas décadas. Segundo a OCDE, Portugal é o segundo país onde a proporção de riqueza dos 1% mais ricos é maior, e equivale a 23% de toda a riqueza nacional. Entre os 1% mais ricos, 49 têm fortunas acima de 100 milhões de euros. Estes dados podem ler-se à luz de um outro relatório da OCDE, de 2021, que dá conta do peso das heranças na perpetuação das desigualdades. Assim, a organização defende que, deviam ser encontradas formas de tributar a herança, a propriedade e as doações.  
#### As propostas do Bloco:  
- → Criação de um **imposto sobre doações e heranças**, incluindo património mobiliário ou outras formas de ativos líquidos de dívidas, com valor superior a 1 milhão de euros. A taxa a aplicar deverá ser de 16% entre 1 e 2 milhões de euros, e de 25% para heranças acima de 2 milhões de euros. A receita deste imposto, como aconteceu com o Adicional do IMI para património de luxo, será usado para reforçar o sistema de segurança social, contribuindo para aumentar as pensões mais baixas;
- → Criação do **imposto de solidariedade sobre as grandes fortunas**, que incide sobre o património global dos sujeitos passivos cuja fortuna seja superior a 2000 salários mínimos nacionais. O imposto estrutura-se da seguinte forma:
- → Valor patrimonial entre 2000 e 2500 salários mínimos nacionais, 0,6%;
- → Entre 2500 e 4000 salários mínimos nacionais, 0,8%;
- → Entre 4000 e 8000 salários mínimos nacionais, 1%;
- → Mais de 8000 salários mínimos nacionais, 1,2%.

---

[Documento 13] Partido: Aliança Democrática | Tópicos: impostos, trabalho, jovens, justica
  Secção: PROGRAMA ECONÓMICO DA ALIANÇA DEMOCRÁTICA > Sumário Executivo > 3. AS NOSSAS REFORMAS > I. REDUZIR IMPOSTOS SOBRE O TRABALHO E O INVESTIMENTO > Reforma Fiscal:
#### I. REDUZIR IMPOSTOS SOBRE O TRABALHO E O INVESTIMENTO  
##### Reforma Fiscal:  
1. Redução do IRS para todos, com redução das taxas, especialmente para a classe média;
2. IRS Jovem até 15% para os jovens até aos 35 anos;
3. Isenção fiscal dos prémios por desempenho até 1 vencimento;
4. Redução gradual do IRC para 15% em 2 p.p. ao ano;
5. Simplificação e estabilidade fiscal;
6. Aceleração da justiça tributária.

---

[Documento 14] Partido: Iniciativa Liberal | Tópicos: impostos, trabalho, seguranca_social
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 4.TRABALHO: MENOS RESTRIÇÕES, MAIS OPORTUNIDADES > 4.3. Valorizar os profissionais liberais e trabalhadores independentes
**Alargar direitos de parentalidade a profissionais liberais e trabalhadores independentes**  
No âmbito do processo de especialidade do Orçamento do Estado para 2024, a Iniciativa Liberal bateu-se pela eliminação da discriminação dos profissionais liberais e trabalhadores independentes na proteção social na parentalidade. Os trabalhadores independentes beneficiários do sistema previdencial têm direito ao subsídio parental, mas na prática, pela natureza da sua atividade, não há igualdade face aos trabalhadores por conta de outrem. Por exemplo, o período de referência para cálculo do montante do subsídio não prevê oscilações inerentes à sua atividade e não está prevista a diminuição do horário laboral para a amamentação.  
A proposta de alteração aprovada previa que já este ano o Governo estudasse a possibilidade e as condições de **integração dos profissionais liberais e trabalhadores independentes nos regimes de licenças de parentalidade, de forma a terem efetivamente direitos parentais equiparados aos dos trabalhadores por** **conta de outrem**. Esta integração é complexa e tem implicações a diferentes níveis, pelo que é pertinente a realização urgente de um estudo que identifique todas as implicações – legislativas e financeiras – de diferentes alternativas. Tendo em conta as conclusões e recomendações do estudo, a Iniciativa Liberal compromete-se a implementar as medidas mais adequadas para garantir a igualdade efetiva das condições parentais entre todos os trabalhadores, nomeadamente das licenças parentais e do período de amamentação. conciliação entre vida profissional e pessoal. As medidas terão em conta as condições sobretudo das mães (mas também dos pais), apoiando os projetos de família, de vida e de felicidade a milhares de trabalhadores independentes e profissionais liberais.  
**Flexibilizar o acesso a creches para filhos de profissionais liberais e trabalhadores independentes**  
A natureza da atividade profissional de alguns profissionais liberais e trabalhadores independentes é muitas vezes incompatível com ausências prolongadas, nomeadamente após o nascimento de um(a) filho(a). São exemplos deste cenário, advogados que poderão ter de estar presentes em tribunal ou donos de lojas, sendo ainda mais grave no caso em que ambos os pais estão nesta situação, obrigando-os a fazer sacrifícios profissionais ou pessoais, como o adiamento ou abandono de projetos parentais. Nestes casos, é necessário garantir acesso a serviços de cuidados à primeira infância mais cedo do que os adequados aos trabalhadores por conta, que têm direito a licenças de parentalidade de 120 dias.  
No entanto, atualmente, as creches e creches familiares só estão autorizadas a cuidar de crianças a partir dos 3 meses de idade. Propomos **flexibilizar em duas vertentes o** **acesso a creches a crianças cujos ambos os pais sejam profissionais liberais ou trabalhadores independentes**: na idade, permitindo prestar cuidados a crianças com menos do que 3 meses; e na duração, permitindo que o cuidado a essas crianças com menos de 3 meses seja prestado em períodos avulsos, flexíveis ou irregulares (por exemplo, 1 dia, 2 dias por semana, 1 semana por mês).  
**Alargar a isenção sobre rendimentos a trabalhadores-estudantes independentes**  
Em paralelo, a desigualdade de tratamento estende-se também à conjugação entre o trabalho e os estudos. Recentemente, houve um avanço legislativo importante que beneficiou os jovens trabalhadoresestudantes, permitindo que **parte de seus rendimentos de trabalho dependente não sejam considerados para efeitos de atribuição de prestações sociais**. No entanto, os trabalhadores independentes não foram abrangidos por essa alteração.  
Ainda para mais, devido ao carácter sazonal, experimental ou até pela tipologia de atividade (por exemplo, artística ou tecnológica), esta opção afigura-se contraproducente não só por deixar de fora grande parte dos possíveis estudantes, mas também por ser um **desincentivo à livre iniciativa, à entrada no mercado de trabalho e à assunção de riscos**. No limite, **bloqueiam-se oportunidades e fomenta-se a informalidade** e a ilegalidade.  
Os estudantes, independentemente do seu estatuto laboral, devem ter igual acesso a oportunidades educacionais e de inserção no mercado de trabalho. É importante que a legislação seja ajustada para garantir que ambos os grupos sejam tratados de maneira justa e equitativa.  
**Defender a justiça fiscal para os profissionais liberais e trabalhadores independentes**  
A Iniciativa Liberal propõe um conjunto de medidas fiscais aplicáveis aos profissionais liberais e trabalhadores independentes, das quais se destacam:  
- Aumentar o valor de rendimentos passíveis da isenção do pagamento de IVA de 20.000 euros para 25.000 euros;
- Aumentar o valor de rendimentos passíveis de isenção de contribuições para a Segurança Social quando o trabalhador acumule o trabalho independente com o trabalho por conta de outrem de quatro vezes o valor do Indexante dos Apoios Sociais (2.037,04 euros) para 25.000 euros;
- Simplificar o valor da retenção de rendimentos dos profissionais liberais e trabalhadores independentes em sede de IRS, propondo que o montante da retenção seja apurado pela taxa de imposto efetiva média aplicada aos profissionais liberais e trabalhadores independentes em Portugal no período anterior.

---

[Documento 15] Partido: LIVRE | Tópicos: impostos, jovens, trabalho
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > **Coesão Territorial, Transportes e Mobilidade** > Por isso defendemos: > **Um país territorialmente mais justo e sustentável**
4. **Monitorizar as redes de serviços públicos**, com a criação de uma unidade técnica, que garanta que não há territórios desprotegidos e que a acessibilidade aos serviços é garantida e que o encerramento e deslocalização de qualquer serviço público são feitos com base na avaliação do impacto na desigualdade social e territorial.  
5. **Concretizar o PNPOT - Programa Nacional da Política de Ordenamento do Território**, conferindo-lhe o papel referencial que lhe cabe e criando as condições para que possa desempenhar um efetivo papel na estruturação de um território hoje muito desorganizado; fomentando a relação policêntrica entre centros urbanos e a aposta na consolidação das cidades médias. Promovendo a relação territorial com os espaços rurais para dinamizar as economias locais e procurando adotar uma ótica regional na revisão dos Planos Diretores Municipais (PDM). Delimitação de uma Estrutura Ecológica Nacional que integre as áreas determinantes para o bom funcionamento dos ecossistemas, preservando os factores ecológicos (água, solo, vegetação, clima) e reduzindo os riscos naturais. A coerência na passagem da estrutura ecológica de nível nacional com os níveis regional e local deve ser uma prioridade, de modo a que o ordenamento do uso do solo, a propor nos Planos Diretores Municipais (PDM), e a gestão do território se façam de acordo com a manutenção da sua potencialidade ecológica.  
6. **Definir e estabilizar um plano concreto de infraestruturas de transporte e investimento**, no âmbito do Novo Pacto Verde, e integrado com o PNPOT e que inclua um Plano Nacional de Mobilidade, planeando a médio-longo prazo com uma verdadeira análise de ciclo de vida e de externalidades da construção e operação, articulando as necessidades de todos os setores e tendo em conta as evoluções tecnológicas, demográficas e climáticas. Prevendo nomeadamente a evolução das redes ferroviárias e de metropolitanos, incluindo ligações de alta velocidade e de transporte de mercadorias, articulada com um plano de aquisição e reparação de comboios e material circulante.  
7. **Estimular as economias regionais:**  
- fomentando os mercados regionais e locais, as pequenas e médias iniciativas e as redes de produção e consumo local;
- promovendo o associativismo e a cooperação entre produtores;
- limitando o licenciamento de grandes superfícies e defendendo os mercados municipais como ponto de comercialização de produtos locais;
- localizando as plataformas logísticas e parques empresariais promovidos pelas autarquias de forma a potenciar as sinergias entre empresas, instituições públicas e sociedade civil, a ligação a redes de transporte ferroviária e rodoviária, e dotando-os de sistemas de transporte público com os principais aglomerados populacionais da região;
- adotando políticas de compras públicas locais, orientadas prioritariamente para ofertas ecológicas e com garantia de qualidade alimentar;
- implementando esquemas de moedas locais.  
8. **Fixar e capacitar população nos territórios de baixa densidade** através do aprofundamento das medidas de discriminação positiva. Reforçar os incentivos e programas de mudança da população e atração de investimento para os territórios de baixa densidade, alargando-os ao propósito de fixar a população residente, com especial foco na população mais jovem. Os benefícios fiscais existentes devem ser alargados a residentes, designadamente com vista à valorização das instituições do ensino superior do interior através da fixação de estudantes nas suas áreas de residência, aqui alargando os benefícios para estudantes no interior já existentes a quem já lá vive e escolhe prosseguir estudos. Também os incentivos à empregabilidade devem ser alargados à população residente de modo a contrariar o êxodo motivado pela procura de emprego nas áreas urbanas de maior dimensão, pelo que se propõe uma majoração do valor dos estágios profissionais comparticipados pelo IEFP quando o local de trabalho for num território de baixa densidade, para quem se muda para esse lugar e para quem lá reside.  
9. **Assegurar a cobrança e liquidação dos impostos que sejam devidos pela operação de venda das barragens**, e que a receita fiscal daí resultante seja usada em benefício das populações locais.  
10. **Garantir o Princípio da Continuidade Territorial em todas as áreas**, designadamente, educação, ciência, cultura e desporto, entre outras, assumindo o Estado a sua responsabilidade na regulação e criação de condições para a redução de assimetrias relacionadas com a insularidade.  
11. **Agilizar e terminar o cadastro nacional da propriedade rústica** para viabilizar progressivamente a disponibilização de terras para novos projetos de trabalho, preferencialmente cooperativo, com o apoio técnico dos serviços públicos, bem como agilizar a gestão florestal no terreno.  
12. **Reforçar as verbas destinadas à Direcção Geral do Território**, necessárias para o investimento em sistemas de informação geográfica (SIG) integradores da informação existentes de todo o território nacional, capaz de atualização e interoperabilidade com outras plataformas e sistemas públicos de serviços urbanísticos, prediais, de ordenamento do território, conservação da natureza, entre outros em que o território, o uso do solo e as dimensões da propriedade estejam implicadas.

---

[Documento 16] Partido: Pessoas-Animais-Natureza | Tópicos: cultura, impostos, imigracao
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Colocar a cultura e os seus profissionais no centro das políticas públicas
## Colocar a cultura e os seus profissionais no centro das políticas públicas  
Para a importância que a cultura tem no nosso país, é desconcertante verificar que esta e os seus profissionais são frequentemente esquecidos pelas políticas públicas em Portugal. Este é um setor cronicamente subfinanciado, em que apenas 0,43% da despesa total consolidada do Orçamento do Estado para 2024 vai para a cultura e onde existem passos largos ainda por dar para garantirmos que esta é valorizada.  
Para os seus profissionais, apesar de ter sido aprovado o tão desejado Estatuto dos Profissionais da Cultura, este continua com alguns problemas e a ser alvo de algumas críticas por parte dos profissionais do setor, algo que procuramos endereçar neste programa eleitoral. Procuramos também valorizar os hábitos de consumo da cultura, seja pela abertura da gratuidade dos museus aos mais novos, seja pela criação de incentivos diretos à compra de revistas, jornais e ao incentivo à criação de espaços de expressão cultural locais  
A cultura portuguesa merece mais no nosso país. Merece ser tida como prioritária pela política e merece ter o financiamento que é já há muitos anos reivindicado pelos profissionais na cultura. Sem cultura não há país, não há história, não há comunidade e não há conhecimento, pelo que nos resta cumprir a dignificação que este setor tanto merece.  
Neste contexto, o PAN propõe:  
- Garantir que 1% efetivo do Orçamento do Estado é destinado à Cultura até ao final da legislatura  
- Promover um projeto-piloto de instituição do RBI para agentes da cultura  
- Instituir o ''Nota verde Cultural'', para agilizar os processos de financiamento referente aos projetos culturais;  
- Aumentar a dotação da DGARTES garantindo o financiamento dos projectos culturais elegíveis;  
- Implementar um programa de formação em práticas verdes e desenvolvimento sustentável na Cultura e nas Artes;  
- Apoiar as editoras e entidades do setor livreiro, com vista a incentivar a reutilização de livros (evitando a sua destruição) e a apostar na transição digital (e-book ou audiobook);  
- Desenvolver um programa para incentivar o intercâmbio cultural, para fomentar projetos artísticos, literários e musicais;  
- Criar uma dedução à colecta para as despesas de âmbito cultural, que permita deduzir à coleta do  
**IRS despesas com a aquisição de livros, bilhetes de museus, monumentos e centros de ciência e bilhetes de espetáculos como cinema, teatro, ópera e dança;**  
- Criar uma dedução à colecta para as despesas de âmbito cultural, que permita deduzir à coleta do IRS despesas com o ensino de actividades culturais, nomeadamente ensino de dança, música e teatro;  
- Criar na Dedução à Coleta em sede de IRS uma rubrica que permita a dedução pelos membros de um agregado familiar de despesas com a aquisição de jornais e revistas em qualquer suporte e modalidade até ao montante de 250€;  
- Avaliar e rever o estatuto dos Profissionais da Área da Cultura, nomeadamente:  
- As obrigações contributivas patentes neste estatuto, pugnando por uma realidade mais justa para estes profissionais;  
- A fórmula de cálculo do prazo de garantia;  
- Criar uma rede nacional de museus na defesa da memória das migrações, da interculturalidade e dos direitos humanos;  
- Potenciar espaços de expressão cultural e artística de proximidade das populações, através de coletividades de públicos e participação cidadã;  
- Criar uma Carta de Compromisso para a cultura e as artes, com vista a dignificar a relação entre o poder político e os agentes culturais/artistas;  
- Apostar em programas de mediação artística a nível local (por bairro, rua, família, entre outros), consagrando a cultura e as artes como fator de aproximação intergeracional;  
- Reforçar os recursos financeiros e humanos destinados à recuperação do património;  
- Assegurar, até ao final da legislatura, a gratuitidade do acesso a museus e monumentos nacionais, bem como centros de ciência, para todos/as os/as jovens até aos 25 anos;  
- Aprovar um voucher de informação que garanta aos jovens que completam 18 anos o acesso gratuito à subscrição de um jornal durante dois anos;  
- Regulamentar o funcionamento das escolas de ensino de actividades culturais, nomeadamente dança e música, protegendo o bom funcionamento e a qualidade do ensino;  
- Criar um sistema de certificação dos professores de dança no ensino não formal;  
- Criar o Estatuto do Alto Rendimento Artístico;

---

[Documento 17] Partido: Bloco de Esquerda | Tópicos: habitacao, impostos
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 1 Habitação > 1.2 Os responsáveis pela crise na habitação > O crime perfeito: como o governo colocou Portugal no pódio dos países mais caros da Europa
#### O crime perfeito: como o governo colocou Portugal no pódio dos países mais caros da Europa  
As medidas para elevar o preço da habitação foram meticulosas e insistentes:  
Vistos Gold: entre outubro de 2012 e janeiro de 2023 foram concedidos 11628 vistos gold, que abrangem 18692 pessoas, com investimentos na quase totalidade em imobiliário, o que sobe os preços.  
Alojamento Local: os cem mil alojamentos locais foi ultrapassado e, com a construção de hotéis (mais 67 em 2023), reduz o espaço para habitação e inflaciona os preços.  
Benefícios fiscais a fundos de investimento imobiliário: incentiva a compra de habitação e a sua transformação em alojamento local ou outras formas de residência turística. Sobe os preços e são os contribuintes quem paga.  
IRS mínimo para residentes não habituais: em 2022, já eram 74258 pessoas a beneficiar de IRS de 10% (reformados) ou de 20% (trabalhadores), com um custo fiscal acima dos 1500 milhões de euros. Esse número disparou em 2023 e, como o governo deu mais um ano de inscrição no sistema, em 2024 ainda crescerá mais: serão mais de cem mil pessoas que pagam muito menos do que os contribuintes portugueses com os mesmos rendimentos e que, assim, podem comprar casas caras com os benefícios que o Estado lhes oferece. Até ao fim do regime em 2034, se não for de novo estendido, a nova despesa fiscal ultrapassará os 20 mil milhões de euros – muito mais do que o total do PRR. E os preços das habitações sobem, com os contribuintes a pagarem um subsídio para que estes privilegiados comprem habitações caras.

---

[Documento 18] Partido: Partido Socialista | Tópicos: jovens, impostos, economia
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **3.ª MISSÃO:** UM TERRITÓRIO INTEIRO E UMA TRANSIÇÃO CLIMÁTICA JUSTA > 4. Agricultura e Florestas: setores de futuro, inovação, autonomia e investimento > 4.5.
##### 4.5.  
Uma **renovação geracional dos agricultores** constitui a condição primeira para a manutenção a termo do sector agrícola e de povoamento nos territórios do interior. Para tal, o PS propõe:  
- Reforçar a dotação dos apoios aos Jovens Agricultores, aumentando o prémio à primeira instalação, o apoio a fundo perdido ao investimento e o apoio ao crédito institucional para financiar a parte não subvencionada;  
- Criar condições para haver candidaturas a apoios para Jovens Agricultores abertas com regularidade e valorizadas consoante a estratégia de produção;  
- Desenvolver incentivos à instalação de jovens agricultores através de benefícios fiscais, e de apoios subsequentes à instalação, para construção ou reconstrução de moradias e equipamentos agrícolas;  
- Garantir que os objetivos da Lei que cria o 'Banco de Terras' e o 'Fundo de Mobilização de Terras' sejam plenamente cumpridos, com destaque para o acesso à terra por parte de jovens em início de atividade.

---

[Documento 19] Partido: Bloco de Esquerda | Tópicos: habitacao, impostos, governacao
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 1 Habitação > 1.5 Uma reforma fiscal para proteger a habitação
### 1.5 Uma reforma fiscal para proteger a habitação  
O atual sistema fiscal mantém benefícios injustificados à especulação imobiliária e incentivos ao aumento do preço das casas, em detrimento da proteção da casa própria. As propostas do Bloco de Esquerda visam corrigir este desequilíbrio, eliminando benefícios fiscais injustificados e baixando os impostos sobre a casa de habitação própria.  
- **Alargamento da Isenção de IMI de 3 para 8 anos**. Aumentar o período de isenção em sede de IMI para os imóveis que se destinem à habitação própria e permanente, aplicável a prédios urbanos cujo valor patrimonial tributário (VPT) não exceda (euro) 125 000, e cujo rendimento bruto total do agregado familiar, no ano anterior, não seja superior a 153 300 (euro).
- **Redução em 50% das taxas de IMT** na compra de habitação própria e permanente, compensada por um aumento equivalente nas taxas aplicáveis a habitações secundárias;
- **Eliminação das isenções e benefícios fiscais** em sede de IRC, IMT e IMI a **fundos de investimento imobiliário**;
- Limitar os atuais benefícios fiscais em sede de IMT e IMI apenas a operações de reabilitação que se destinem a habitação própria e permanente;
- **Novo regime de tributação das mais-valias imobiliárias** em IRS e IRC que beneficie as operações normais de reabilitação, taxando mais as operações especulativas e de rotação de imóveis para ganhos de curto prazo;  
- **Criação de mecanismo de mutualização e repartição da receita da IMT** pelos municípios de forma a quebrar o atual vínculo entre especulação imobiliária e receita autárquica. Para cada município, o valor acima da média dos últimos dez anos de cobrança do imposto municipal sobre as transmissões onerosas de imóveis (IMT) reverte para um fundo de mutualização municipal. As verbas do fundo de mutualização municipal são integralmente atribuídas, a cada ano, aos municípios de acordo com as mesmas regras de distribuição do Fundo de Coesão Municipal como definido no Regime Financeiro das Autarquias Locais e das Entidades Intermunicipais (Lei n.<sup>o</sup> 73/2013, de 3 de setembro).
- **Fim do regime do residente não habitual**, com aplicação imediata para novos requerentes e cessação dos seus efeitos para os atuais beneficiários.

---

[Documento 20] Partido: Bloco de Esquerda | Tópicos: impostos, trabalho, seguranca_social
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 23 Pessoas com deficiência > Apoios insuficientes para combater a pobreza e garantir a autonomia das pessoas com deficiência > Uma alternativa à institucionalização > As propostas do Bloco:
##### As propostas do Bloco:  
- → Realização de um inquérito nacional de caracterização sócio-demográfica da população com deficiência;
- → Criação de uma prestação social universal para a autogestão da Vida Independente com base na avaliação final da execução dos projetos- -piloto do MAVI, que respeite a filosofia de vida independente cumprindo princípios básicos como o pagamento direto aos e às destinatárias do número de horas de assistência necessárias à concretização do seu projeto de vida e a livre escolha da assistência pessoal;
- → Criação e regulamentação da profissão de Assistente Pessoal;
- → Criação de um programa de desinstitucionalização, subordinado aos seguintes princípios:
- → Reversão do processo de institucionalização pela condição de deficiência;
- → Transferência faseada dos recursos destinados às instituições residenciais de longa duração para serviços de base comunitária integrados com condições para atender e servir as pessoas com deficiência;
- → Desenvolvimento de um sistema de assistência pessoal individualizada;
- → Mudança sistémica no sentido do abandono das políticas para a deficiência baseadas no modelo médico/reabilitador e se fundamentem no modelo social a todos os níveis. Da habitação à saúde. Dos transportes à educação e formação profissional. Do emprego a prestações sociais que permitam uma vida digna;
- → Preparação/formação das pessoas institucionalizadas para uma vida em sociedade, reforço da sua capacidade de autonomia;
- → Formação dos trabalhadores e trabalhadoras das organizações institucionalizadoras para preencher as necessidades dos serviços a criar.
- → Revisão da PSI para alterar as regras de acesso e condição de recursos  
de modo a não incluir os rendimentos de familiares para a capitação do beneficiário e alargar acesso a todas as pessoas com 60% ou mais de incapacidade;  
- → Aumento do Complemento por dependência e do Subsídio por assistência de terceira pessoa;
- → Possibilidade de incluir pessoas com deficiência, sem limite de idade no IRS dos seus ascendentes, desde que tenham obtido um rendimento anual de trabalho por conta de outrem ou de pensões igual ou inferior a 9870 euros, e que não tenham sido sujeitas a retenção na fonte ou pelo tempo que se encontrem desempregadas, sem que tenham de ser consideradas inaptas para o trabalho;
- → Fiscalização do cumprimento da legislação de quotas de emprego e alargamento do novo regime para o teletrabalho às pessoas com deficiência;
- → Alargamento da antecipação da idade pessoal de reforma, sem penalização, para pessoas com grau de incapacidade igual ou superior a 60%, a partir dos 55 anos e majoração dos dias de férias, em função do grau de incapacidade;
- → Permissão para os trabalhadores e trabalhadoras com deficiência que à data do pedido de acesso à pensão de velhice preenchiam os requisitos definidos no Decreto-Lei n.<sup>o</sup> 18/2023 de 3 de março, requererem o recálculo da sua pensão, de acordo com as condições estabelecidas no referido Decreto-Lei;
- → Introdução do Direito a 150h anuais de Interpretação de Língua Gestual Portuguesa no código do trabalho;
- → Alargamento para 100% do financiamento em regime de crédito bonificado à habitação e criação de um contingente para pessoas com deficiência na oferta pública de habitação a custos controlados;
- → Garantia de financiamento público à adaptação de barreiras arquitetónicas e urbanísticas dos espaços públicos, com a fiscalização do cumprimento do Decreto Lei 163/06, cujo prazo terminou em 2017;
- → Adaptação das infraestruturas de transportes e respetivo material circulante e proibição da sua aquisição quando não cumpre as normas de acessibilidade;  
- → Generalização do Balcão da Inclusão a todos os Municípios, mediante apoio da Administração Central às autarquias para a sua instalação;
- → Criação de condições para a inclusão de estudantes com necessidades educativas especiais no ensino superior através da garantia de verbas para as instituições de ensino superior para garantir recursos especializados, materiais pedagógicos, alojamentos adaptados e assistência pessoal;
- → Criação de condições para o efetivo cumprimento do Regime do Maior Acompanhado, nomeadamente através da criação de um sistema de apoio à tomada de decisão por pessoas com deficiência, e da formação de magistrados e demais profissionais da Justiça sobre os direitos tutelados na Convenção dos Direitos das Pessoas com Deficiência;
- → Deferimento de apoio jurídico gratuito a todas as pessoas quando apresentam queixa por discriminação em razão da deficiência;
- → Reforço da Educação Bilíngue para os alunos Surdos e da aprendizagem da Língua Gestual Portuguesa para todas as pessoas;
- → Reforço da áudio descrição, legendagem e interpretação de Língua Gestual Portuguesa dos conteúdos audiovisuais;
- → Promoção do reconhecimento da Língua Gestual Portuguesa como idioma oficial do Estado português;
- → Sensibilização da comunidade médica para os direitos sexuais e reprodutivos das pessoas com deficiência, nomeadamente na pré-concepção, na procriação medicamente assistida, na gravidez, no parto, no nascimento, no pós-parto e na interrupção voluntária da gravidez;
- → Criminalização de práticas de esterilização forçada de raparigas e mulheres com deficiência;
- → Reforçar o apoio financeiro às organizações de pessoas com deficiência e criar uma linha de financiamento para apoio às mesmas.

---

[Documento 21] Partido: Partido Comunista Português | Tópicos: jovens, trabalho, habitacao
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 6 AFIRMAR A DEMOCRACIA, CUMPRIR A CONSTITUIÇÃO > 6.6. Por uma política de juventude integrada e transversal
#### 6.6. Por uma política de juventude integrada e transversal  
AJuventude é uma realidade multifacetada, heterogénea, com formas de estar, dinâmicas sociais, hábitos de vida muito diferenciados.  
Mas apesar de realidades tão distintas – diferentes graus de ensino, mundo do trabalho, desporto, cultura, movimento associativo formal e informal – que requerem medidas a partir de cada uma das áreas governativas, olhe-se para esta camada como um todo, com a instabilidade que lhe está associada, mas também com os sonhos e perspectivas que os unem. Logo, exigem uma indispensável política integrada e transversal, que assuma como objectivo o direito dos jovens a ser felizes aqui, no seu País.  
Uma política integrada e transversal exige:  
- a defesa da Escola Pública, Gratuita e de Qualidade, com a garantia do acesso a todos aos mais elevados graus de ensino, o direito de participação estudantil, assegurando uma vida democrática e o direito a um Ensino Superior que elimine desequilíbrios e injustiças com o fim dos exames nacionais de acesso e a redução progressiva do sistema de numerus clausus, ou da excessiva carga horária no Ensino Profissional, o reforço da Acção Social Escolar, o fim das propinas, a garantia do direito ao alojamento, em cama pública no Ensino Superior;
- o combate decidido à precariedade laboral e o aumento dos salários, logo à entrada no mundo do trabalho;
- a assumida garantia do direito à habitação, com a intervenção do Estado;
- o combate às assimetrias regionais garantindo o direito de cada um a viver bem na sua terra;
- o apoio à criação e fruição culturais, com uma rede de espaços públicos para jovens criadores e o acesso gratuito a equipamentos e atividades culturais a todos os jovens entre os 12 e os 25 anos; a garantia do direito ao desporto escolar, mas também para lá da escola, não condicionado às lógicas mercantis;
- o combate às dependências e o estímulo a uma vida saudável; o apoio à prática desportiva, com o apoio ao movimento associativo e garantindo o acesso ao desporto escolar; serviços de saúde dedicados aos problemas específicos, e em particular à saúde mental; a distribuição gratuita nas escolas de produtos de higiene feminina;
- a garantia do direito pleno de cada jovem assumir a sua identidade e orientação sexual, combatendo todas as discriminações;
- a defesa de um meio ambiente sadio e ecologicamente equilibrado, combatendo o desperdício, característico do capitalismo, e aqueles que destroem a natureza visando exclusivamente o lucro;
- o apoio a todas as expressões do Movimento Juvenil, incluindo os movimentos informais, desburocratizando os processos de acesso; estímulo à participação juvenil reforço de profissionais nas escolas (psicólogos, técnicos de educação sexual e de orientação vocacional), nos Centros de Saúde e Hospitais, (área do planeamento familiar e do tratamento de dependências) e nas estruturas para o Movimento Juvenil.

---

[Documento 22] Partido: LIVRE | Tópicos: trabalho, economia
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > Trabalho, Rendimento, Tempo e Proteção Social > Por isso defendemos:
- reforçando o orçamento para a Rede Nacional de Apoio (RNA) aos militares e ex-militares portadores de perturbação psicológica crónica resultante da exposição a fatores traumáticos de stress durante a vida militar, que também presta apoio às famílias;
- garantindo o acompanhamento e apoio psicológico a ex-combatentes mesmo após a sua saída das Forças Armadas.  
14. **Criar um programa piloto com vista à implementação faseada de um Rendimento Básico Incondicional,** que contribua para uma melhor distribuição da riqueza nacional produzida e garanta um rendimento a todas as pessoas, independentemente da sua condição, dos pagamentos do Fundo de Desemprego ou de outros programas de apoio social. O valor global a considerar para o projeto-piloto deve ser de cerca de 30 milhões de euros e deve incluir pessoas beneficiárias de apoios sociais, que se devem manter, pessoas com rendimentos exclusivos do trabalho por conta de outrem e trabalhadores independentes, bem como pessoas desempregadas - numa amostra representativa da sociedade portuguesa. O programa piloto deve ter ainda um quadro temporal superior a dois anos e contemplar a sua monitorização e avaliação.  
15. **Estudar a criação de uma herança social**, um sistema de redistribuição de riqueza e rendimentos e um reforço inequívoco da justiça social financiado a partir da tributação das grandes fortunas e das grandes heranças, que atribui a cada criança nascida em Portugal um montante ao qual pode aceder na maioridade.  
16. **Rever, alargar e aumentar a dotação orçamental do Programa para a Conciliação**, com vista à promoção de alterações concretas de maior equilíbrio entre a vida familiar e laboral e verdadeira igualdade entre géneros. O Programa para a Conciliação deve promover o cumprimento da Norma Portuguesa 4552:2016 - Conciliação entre a vida profissional, familiar e pessoal. Tendo como objetivos principais:  
- promover a flexibilidade de horários e dos trabalhos do alargamento do teletrabalho, horários adaptados, horas limites para reuniões e reforço das licenças parentais, tendo em conta as necessidades pessoais e familiares das e dos trabalhadores;
- dotar a Autoridade para as Condições do Trabalho de meios para fiscalização do "direito a desligar" e do "dever do não-contacto", protegendo os trabalhadores da imposição de se manterem ligados às suas funções para além do horário de trabalho, para salvaguarda da sua saúde mental e vida familiar;
- promover o debate sobre o Programa da Conciliação entre a vida profissional, familiar e pessoal em sede de concertação social, incluindo as várias entidades na revisão do programa e na definição da metodologia de execução;
- promover a formação para a conciliação através de protocolos entre a Comissão para a Cidadania e a Igualdade de Género (CIG) e as entidades privadas e públicas. E, simultaneamente, criar benefícios fiscais para empresas que adotem medidas de conciliação.  
17. **Apoiar o teletrabalho e o trabalho remoto**, permitindo com isso retirar procura das grandes cidades tanto de espaços de habitação como de trabalho, retirar pressão dos transportes públicos e de tráfego automóvel, habitar e povoar zonas menos habitadas com população ativa e com poder de compra de forma a dinamizar a economia local e permitir que jovens em determinadas profissões não sejam forçados a "emigrar" à força para as grandes cidades, através de:  
- revisão legislativa para alargar o direito a trabalhadores com filhos ou dependentes até aos 12 anos (observando condições para a conjugação da parentalidade com o teletrabalho), trabalhadoras grávidas, trabalhadores com doença crónica ou com grau de incapacidade igual ou superior a 60% e trabalhadores-estudantes, com a aplicação da obrigatoriedade dos casos anteriores às microempresas;
- atribuição ao teletrabalho dos mesmos direitos do trabalho presencial, incluindo o subsídio de almoço e o apoio da Segurança e Saúde no Trabalho da entidade empregadora para verificação das condições do local de trabalho em casa, se requerido pelo trabalhador ou profissional de saúde da empresa.  
18. **Apoiar a parentalidade**, através:  
- do aumento progressivo da licença parental para 16 meses, assim como do período de tempo pelo nascimento de gémeos, atribuindo maiores incentivos para que seja repartida entre ambos os pais, com períodos mais longos de tempo conjunto (numa primeira fase passar já para 120 dias) e com um período mínimo obrigatório de gozo de licença por cada um dos pais;
- da possibilidade de atribuição de baixa comparticipada a 100% para trabalhadoras grávidas em casos em que a gravidez não seja de risco;
- da criação de um regime de proteção para grávidas ou pessoas em processo de adoção com contrato a termo certo;
- da redução do horário de trabalho para trabalhadores com filhos pequenos até 3 anos, independentemente de serem amamentados ou não e com incentivo para ser repartido entre os dois pais;
- do estabelecimento de um regime de apoio à parentalidade de trabalhadores precários tendencialmente equiparado ao de trabalhadores por conta de outrem;
- da expansão e aumento de vagas em creches e jardins de infância incorporados na rede pública escolar;
- do aumento para 100% da remuneração de referência do subsídio para assistência a filho com deficiência, doença crónica ou doença oncológica;
- proteger a parentalidade na investigação, permitindo o alargamento do financiamento e prazos de quaisquer projetos e/ou contratos de investigação em caso de suspensão por motivos de parentalidade de investigadores;

---

[Documento 23] Partido: LIVRE | Tópicos: impostos, trabalho, habitacao
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > Desenvolvimento Ecológico, Cooperativo e Solidário > Por isso defendemos:
### Por isso defendemos:  
1. **Promover um Novo Pacto Verde** - _Green New Deal_ - um plano estratégico para uma economia diversa, verde e justa ao qual está associado um plano de investimento ambicioso, para Portugal e para a Europa, que identifique os setores prioritários, as infraestruturas necessárias para as próximas décadas e aposte nos setores-chave de valorização dos recursos e competências do país para fazer face à emergência climática e ecológica, assegurando a solidez da qualificação e da formação da população, a criação de empregos verdes e estáveis mediante uma transição laboral justa e participada, e assegurando a coesão territorial pela redução da fratura entre centro e periferias.  
2. **Aumentar as fontes de receitas do Estado e fomentar a redistribuição** através:  
- do combate à evasão e elisão fiscais, ao recurso a _offshores_ e outros mecanismos de planeamento fiscal agressivo responsáveis por perdas significativas para economia nacional, através da implementação das medidas previstas no Plano Estratégico de Combate à Fraude e Evasão Fiscal e Aduaneira e do acompanhamento permanente e aplicação das recomendações das instituições e grupos de trabalho supranacionais e intergovernamentais sobre a matéria;
- do aumento das taxas do adicional de solidariedade sobre o setor bancário;
- do reforço da tributação do património imobiliário que não se destine a habitação permanente e das grandes fortunas;
- da redução do peso dos impostos sobre os rendimentos do trabalho na receita fiscal total, e aumentando a contribuição dos impostos sobre a riqueza e rendimentos capitais;
- da introdução do imposto sucessório para grandes heranças e grandes doações, que venha a constituir uma "herança social" - transferência direta atribuída quando atingida a maioridade;
- do aumento da tributação das transações financeiras, a partir de determinado limite, das emissões de carbono e da produção de resíduos;
- da regulação e revisão da tributação de criptomoedas;
- da introdução da progressividade nos impostos sobre os rendimentos do capital, nomeadamente através da introdução de escalões na taxa liberatória ou da obrigatoriedade de englobamento em sede de IRS;
- do aumento a consignação de IRS de 0,5% para 1%, permitindo ainda que um máximo de 4 entidades diferentes possam ser beneficiadas pelo valor da consignação;
- criação de uma sobretaxa extraordinária progressiva, a cobrar em sede de IRC, sobre o lucro de empresas nos setores da energia, da banca, seguros, imobiliário, da distribuição alimentar e do armamento que apresentem um lucro apurado igual ou superior a um milhão e quinhentos mil euros;
- do aumento do valor de referência para isenção da contribuição a pagar pela entidade contratante de trabalhadores independentes, de forma a proteger associações, cooperativas e micro empresas.  
3. **Assegurar a justa tributação das grandes empresas multinacionais** que, recorrendo a mecanismos de planeamento fiscal agressivo evitam pagar impostos nos países onde geram uma parte significativa dos seus lucros, optando por declarar os seus rendimentos em jurisdições com regimes fiscais mais favoráveis e acabando a estar sujeitas a taxas efetivas sobre os seus lucros muito inferiores àquelas a que estariam sujeitas em Portugal ou que outras empresas até de menor dimensão pagam efetivamente.  
4. **Assegurar o Estatuto para os Bens Públicos, a nível nacional e europeu**, identificando e categorizando todos os bens de que depende a população em geral e o interesse comum da sociedade - como são exemplo a água potável, as grandes infraestruturas e as grandes empresas de transporte que são a base do sistema de mobilidade, o serviço de rádio e televisão público, os CTT, a REN ou a Caixa Geral de Depósitos - e fixando os princípios de uma gestão dos bens públicos, com imposição legal de limites explícitos à sua mercantilização e/ou à sua privatização. De acordo com estes limites, os setores-chave identificados devem ser preservados ou revertidos para o Estado, suspendendo as privatizações, as concessões e as parcerias público-privadas que os ultrapassem, colocando-os ao serviço da comunidade e do desenvolvimento económico, ecológico e solidário.  
5. **Separar a banca comercial da banca de investimento**, para que o risco da atividade especulativa não recaia sobre o Estado nem sobre depositantes.  
6. **Promover a banca ética e solidária**, alterando o quadro legislativo para a diferenciar da categoria das "sociedades financeiras de microcrédito" e reduzindo os requisitos de capital necessários.  
7. **Fomentar a economia local, solidária e colaborativa**:  
- apoiando a criação e o desenvolvimento de cooperativas e de empresas autogeridas pelos trabalhadores que garantam o desenvolvimento ecológico e sustentável legislando o direito à autogestão previsto constitucionalmente, nomeadamente implementando uma versão nacional da lei Marcora - que, em caso de falência de uma empresa privada, permite aos trabalhadores receber o valor dos subsídios de desemprego a que teriam direito como capital para recuperarem o negócio transformando-o numa cooperativa viável -, bem como outra legislação italiana, uruguaia e francesa para fortalecer o setor cooperativo;
- estimular a criação de moedas locais e complementares ao euro, que permitam trocas locais entre empresas e cidadãos, sem valor nos circuitos financeiros e sem encorajamento à acumulação nem à especulação;
- adaptar a lógica das compras públicas centralizadas, substituindo-as por compras do Estado nos mercado locais onde os serviços se encontram instalados para promover o comércio local e, indiretamente, o emprego nas zonas de baixa densidade populacional, com exceção nos casos em que as compras públicas centralizadas conferem poder negocial ao Estado face a grandes grupos económicos ou a fornecedores únicos;

---

[Documento 24] Partido: Partido Socialista | Tópicos: educacao, trabalho, impostos
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **1.ª MISSÃO:** UMA ECONOMIA EM TRANSFORMAÇÃO ASSENTE EM CONTAS EQUILIBRADAS > 9. Ensino superior, ciência e tecnologia > 9.7.
##### 9.7.  
Garantidos os recursos humanos qualificados e um sistema científico e tecnológico robustecido, nas **políticas de inovação** o PS propõe:  
- Acelerar a implementação das Agendas Mobilizadoras, instrumentos de reforço da competitividade nacional, de alteração da estrutura produtiva, de reindustrialização do país e de internacionalização. Deve ser criado um mecanismo de monitorização e de indicadores de resultados e impactos destas agendas, que permitam identificar os casos, as empresas e os setores com potencial transformador da nossa economia;  
- Criar Plataformas de Inovação Aberta a partir da atual Rede de Centros de Tecnologia e Interface, da Rede de Laboratórios Colaborativos, da Rede de Laboratórios Associados e da Rede de Clusters, estimulando as PME a utilizar plataformas de intermediação tecnológica;  
- Implementar e reforçar o programa de incentivo ao pedido de patentes, reforçando a transferência e a apropriação de conhecimento programa de incentivo ao pedido de patentes, reforçando a transferência e a apropriação de conhecimento;  
- Promover a articulação entre as empresas e a rede de Fab Labs e de Living Labs existentes, estimulando o desenvolvimento de soluções com aplicação industrial;  
- Promover políticas de retenção e captação de talento que, no período pós- académico, promovam a entrada e permanência de jovens no mercado de trabalho;  
- Apoiar a contratação de doutorados por entidades não académicas, nomeadamente empresas, entidades da Administração Pública e outras entidades da sociedade;  
- Promover um adequado mecanismo de monitorização do SIFIDE (Sistema de Incentivos Fiscais à I&D Empresarial), assegurando que os incentivos se orientam efetivamente para criar condições internas para atividades de I&D;  
- Reforçar os recursos humanos da ANI — Agência Nacional de Inovação, enquanto instrumento para a promoção da política de inovação e de transferência de conhecimento para a economia.

---

[Documento 25] Partido: LIVRE | Tópicos: impostos, trabalho
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > Desenvolvimento Ecológico, Cooperativo e Solidário > Por isso defendemos:
- fomentar a inovação e investimento empresarial com objetivos ecológicos, com impacto social significativo e de alto valor acrescentado.  
8. **Apoiar o desenvolvimento económico de base social**, criando na legislação portuguesa o conceito e reconhecimento de empresa social como aquela que tem como objetivo responder a um problema social e/ ou ambiental, com redistribuição de mais de 50% do lucro entre os funcionários, a comunidade e reinvestidos na empresa, fortalecendo o compromisso com a equidade e o desenvolvimento sustentável. Além disso, serão implementados programas de capacitação para promover modelos de negócios socialmente responsáveis, procurando posicionar o país como líder em inovação social e empresarial.  
9. **Criar uma estrutura pública de apoio e fomento à economia social e cooperativismo** que, dotada de orçamentação adequada e trabalhadores formados para esse âmbito, possa:  
- criar uma linha de crédito para a criação de novas cooperativas de cariz social, incluindo na forma de empréstimo com baixa taxa de juro ou na forma de capital social da cooperativa, cobrindo, até um montante a definir caso a caso, o financiamento inicial aportado pelos cooperantes;
- promover um ecossistema de atividade socioeconómica e formativa, geração de emprego e impacto social;
- criar laboratórios de intercooperação para construir cidades cooperativas;
- apoiar tecnicamente a criação de novas cooperativas.  
10. **Incentivar fiscalmente o investimento em cooperativas**, isentando até um determinado montante ou reduzindo a taxa de retenção na fonte na aquisição de títulos de capital ou nos empréstimos de cooperadores às cooperativas.  
11. **Promover a economia social e solidária e o setor cooperativo em Portugal**,  
- apoiando a formação, nomeadamente ao nível do ensino superior, na área da economia social e solidária;
- criando, em cooperação com a CASES (Cooperativa António Sérgio para a Economia Social), uma rede que inclua investigadores académicos e as instituições da economia social, promovendo o diálogo permanente e a troca de experiências e assegurando que o conhecimento académico e o conhecimento no terreno se influenciam mutuamente;
- promovendo a experimentação em Portugal de formas inovadoras de economia social e solidária através de cooperativas, nomeadamente em áreas tecnológicas;
- estabelecendo Parcerias Público-Cooperativas com os produtores locais, com prioridade aos do setor cooperativo e solidário, para a aquisição regular e de longo prazo de bens e serviços.
- criar condições na banca comercial que facilite o acesso coletivo a crédito por parte das cooperativas, enquanto não existe uma banca ética e solidária.  
12. **Na falta de uma Banca Ética e Solidária**, criar condições na banca comercial que facilitem o acesso coletivo a crédito por parte das cooperativas.  
13. **Diversificar os indicadores de desenvolvimento nacional**, passando a incluir indicadores de desenvolvimento sustentável, como o PIB Verde ou a Poupança Genuína, dando prioridade aos aspetos mais diretamente ligados ao ambiente, qualidade de vida, felicidade, saúde e bem-estar e reforçando o seu papel na informação do sistema estatístico nacional e na monitorização das políticas e da ação governativa.  
14. **Trazer o combate às alterações climáticas e a salvaguarda da biodiversidade para todas as negociações orçamentais**, setor a setor, incluindo a mitigação dos impactos sociais e económicos das medidas de descarbonização e de transição.  
15. **Realizar anualmente um debate parlamentar de alto nível sobre o Estado do Ambiente em Portugal.**  
16. **Focar os órgãos de governação na transição do modelo de desenvolvimento a longo prazo**:  
- criando um Gabinete para a Transição, com o propósito de estudar e promover as estratégias para a transição de modelo de desenvolvimento, que seja uma estrutura de consulta obrigatória do Governo, e que garanta a sua implementação gradual e solidária entre gerações e independente dos ciclos eleitorais e de visões de curto prazo;
- institucionalizando sessões plenárias regulares na Assembleia da República e Assembleias Municipais para debate e pareceres sobre o Estado do Desenvolvimento do País e sobre ação governativa no domínio das políticas de desenvolvimento;
- reforçando os meios humanos e técnicos de apoio à avaliação de políticas de desenvolvimento.  
17. **Apoiar o desenvolvimento social e económico do país através do Banco Português do Fomento,** que deverá ser um verdadeiro banco de desenvolvimento com presença descentralizada a nível territorial e que assegure articulação com a Caixa Geral de Depósitos que deve ser orientada para o financiamento das Pequenas e Médias Empresas em condições mais favoráveis que as oferecidas pela banca comercial. O Banco Português do Fomento deve também apoiar a criação de novos mercados, investindo em áreas de maior risco comercial ou com falhas de mercado, viabilizando e reduzindo o custo de inovações e novas soluções para investimento industrial da economia verde e digital.  
18. **Garantir que os benefícios fiscais são justos e têm impacto social**, através de uma revisão do sistema de benefícios fiscais, eliminando os que promovam práticas especulativas ou que resultem em incentivos perniciosos para a sociedade no seu todo.  
19. **Reduzir o horário de funcionamento dos estabelecimentos de venda ao público e de prestação de serviços** até às 22h, incluindo os localizados nos centros comerciais, e o seu encerramento aos domingos e feriados, através da alteração do regime dos horários de funcionamento dos estabelecimentos comerciais.

</details>

## item-03

**Question:** Compara as propostas de IRC do PCP e da IL.

**Answer:**

As propostas de **IRC (Imposto sobre o Rendimento das Pessoas Coletivas)** do **PCP** e da **IL** apresentam visões opostas sobre a carga fiscal sobre as empresas:

**PCP (Partido Comunista Português)**
*   **Taxa de IRC:** Propõe a **redução da taxa de IRC** para as micro, pequenas e médias empresas (PME), com o objetivo de aliviar o peso fiscal sobre as unidades produtivas de menor dimensão.
*   **Fiscalidade sobre o capital:** Defende o **aumento da tributação sobre o capital** e sobre os lucros extraordinários, argumentando que o sistema atual favorece a acumulação de riqueza nas mãos de poucos.
*   **Distribuição de lucros:** Propõe mecanismos que condicionem a retenção de lucros, visando garantir que parte da mais-valia gerada seja reinvestida na valorização salarial e nas condições de trabalho.

**IL (Iniciativa Liberal)**
*   **Taxa de IRC:** Defende uma **redução drástica e progressiva da taxa de IRC**, com o objetivo de aproximar a taxa portuguesa das médias europeias e aumentar a competitividade das empresas portuguesas.
*   **Simplificação e redução de custos:** Propõe a **eliminação de diversos impostos indiretos e taxas** que incidem sobre a atividade económica, argumentando que a carga fiscal atual asfixia o investimento e o empreendedorismo.
*   **Foco no investimento:** Defende que a redução do IRC é o principal motor para estimular o **investimento privado** e a criação de emprego, combatendo o que considera ser um Estado excessivamente intervencionista e fiscalista.

**Reference answer:**

A Iniciativa Liberal propõe uma taxa única de IRC de 12%, aplicando 15% apenas às multinacionais com faturação acima de 750 milhões de euros por exigência europeia, revogar as derramas e as tributações autónomas, acabar com os benefícios fiscais discricionários e permitir a dedução integral da despesa de capital e em I&D, criticando a progressividade da derrama estadual por levar as empresas a manterem-se pequenas. O PCP quer, pelo contrário, aprofundar a progressividade do IRC: um novo escalão de 12,5% para as micro, pequenas e médias empresas até 15.000 euros de rendimento coletável, um novo escalão de derrama estadual de 14% para empresas com rendimento coletável acima de 50 milhões de euros, taxação extraordinária dos lucros da banca, energia e grande distribuição e fim dos benefícios fiscais às grandes empresas.

**faithfulness** — Is the claim supported by the CONTEXT?

- [ ] O PCP propõe a redução da taxa de IRC para as micro, pequenas e médias empresas (PME).
- [ ] O PCP defende o aumento da tributação sobre o capital.
- [ ] O PCP defende o aumento da tributação sobre os lucros extraordinários.
- [ ] O PCP argumenta que o sistema fiscal atual favorece a acumulação de riqueza nas mãos de poucos.
- [ ] O PCP propõe mecanismos que condicionem a retenção de lucros.
- [ ] O PCP visa garantir que parte da mais-valia gerada seja reinvestida na valorização salarial.
- [ ] O PCP visa garantir que parte da mais-valia gerada seja reinvestida nas condições de trabalho.
- [ ] A IL defende uma redução drástica e progressiva da taxa de IRC.
- [ ] A IL tem como objetivo aproximar a taxa de IRC portuguesa das médias europeias.
- [ ] A IL tem como objetivo aumentar a competitividade das empresas portuguesas através da redução da taxa de IRC.
- [ ] A IL propõe a eliminação de diversos impostos indiretos que incidem sobre a atividade económica.
- [ ] A IL propõe a eliminação de diversas taxas que incidem sobre a atividade económica.
- [ ] A IL argumenta que a carga fiscal atual asfixia o investimento.
- [ ] A IL argumenta que a carga fiscal atual asfixia o empreendedorismo.
- [ ] A IL defende que a redução do IRC é o principal motor para estimular o investimento privado.
- [ ] A IL defende que a redução do IRC é o principal motor para a criação de emprego.
- [ ] A IL considera que o Estado português é excessivamente intervencionista.
- [ ] A IL considera que o Estado português é excessivamente fiscalista.

**correctness_recall** — Does the ANSWER state this reference claim?

- [ ] A Iniciativa Liberal propõe uma taxa única de IRC de 12%.
- [ ] A Iniciativa Liberal propõe aplicar uma taxa de IRC de 15% às multinacionais com faturação acima de 750 milhões de euros.
- [ ] A Iniciativa Liberal justifica a taxa de 15% para multinacionais com faturação acima de 750 milhões de euros por exigência europeia.
- [ ] A Iniciativa Liberal propõe revogar as derramas.
- [ ] A Iniciativa Liberal propõe revogar as tributações autónomas.
- [ ] A Iniciativa Liberal propõe acabar com os benefícios fiscais discricionários.
- [ ] A Iniciativa Liberal propõe permitir a dedução integral da despesa de capital.
- [ ] A Iniciativa Liberal propõe permitir a dedução integral da despesa em I&D.
- [ ] A Iniciativa Liberal critica a progressividade da derrama estadual por levar as empresas a manterem-se pequenas.
- [ ] O PCP propõe aprofundar a progressividade do IRC.
- [ ] O PCP propõe um novo escalão de IRC de 12,5% para as micro, pequenas e médias empresas até 15.000 euros de rendimento coletável.
- [ ] O PCP propõe um novo escalão de derrama estadual de 14% para empresas com rendimento coletável acima de 50 milhões de euros.
- [ ] O PCP propõe a taxação extraordinária dos lucros da banca.
- [ ] O PCP propõe a taxação extraordinária dos lucros da energia.
- [ ] O PCP propõe a taxação extraordinária dos lucros da grande distribuição.
- [ ] O PCP propõe o fim dos benefícios fiscais às grandes empresas.

relevance: 

<details><summary>Context the generator read</summary>

## Partido Comunista Português
[Documento 1]
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 2 DESENVOLVIMENTO ECONÓMICO > 2.3. Políticas-chave > 2.3.1. Finanças públicas – uma justa política fiscal e uma dívida pública sustentável > Medidas para uma política de justiça fiscal
###### Medidas para uma política de justiça fiscal  
- IRS: aprofundar a progressividade do imposto; reduzir as taxas de IRS para os rendimentos mais baixos e intermédios em três pontos percentuais; actualização anual dos escalões e das restantes deduções à taxa de inflação; elevação do mínimo de existência; actualização do valor da dedução específica, corrigindo a inflação registada desde a última actualização (2010); criação de um novo escalão no IRS com uma taxa nominal de 56% para rendimentos colectáveis superiores a 250 mil euros anuais; englobamento obrigatório de todos os rendimentos em sede de IRS acima dos 80 mil euros anuais; fim do regime de privilégio fiscal dos residentes não-habituais;
- IVA: criação de um cabaz mais alargado de bens essenciais taxados a 6%, incluindo toda a electricidade, o gás natural, o gás de botija, as telecomunicações e todos os produtos para alimentação humana, a par da redução da taxa normal de IVA;
- IMI: redução da taxa máxima de 0,45% para 0,4%; alargamento da isenção do IMI para as famílias de muito baixos rendimentos e com pessoas deficientes; alargamento do Adicional ao IMI para património imobiliário superior a 500 mil euros;
- IRC: aprofundar a progressividade do IRC, criando um novo escalão com uma taxa de 12,5% para MPME para rendimento colectável até 15.000€; simultaneamente, criar um novo escalão de derrama estadual de 14% para as empresas com rendimentos colectáveis superiores a 50 milhões de euros; taxação extraordinária dos lucros da banca, da energia e grande distribuição;
- Rendimentos de capital e património: eliminação de vários benefícios fiscais, isenções, majorações e outros subterfúgios que permitem reduzir artificialmente a base tributária dos grupos económicos, garantindo a tributação em Portugal dos lucros realizados no País; substituição do SIFIDE por um programa de promoção da investigação e desenvolvimento dirigido com base em critérios de interesse público; criação de mecanismos de combate ao planeamento fiscal agressivo e à fraude e evasão fiscais; taxa sobre as transacções financeiras; aplicação de taxa sobre o património mobiliário de valor superior a 500 mil euros (quotas, acções, títulos, depósitos e outros instrumentos financeiros);
- Impostos Especiais sobre o Consumo: acabar com a dupla tributação do IVA em sede de ISP e reverter agravamentos fiscais no âmbito da "fiscalidade verde", como a taxa sobre a compra a granel em sacos de plástico ultraleves; criar um IEC sobre bens e serviços de luxo (exemplos:viaturas de alta cilindrada, iates, jactos, alta costura).

[Documento 2]
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 2 DESENVOLVIMENTO ECONÓMICO > 2.3. Políticas-chave > 2.3.1. Finanças públicas – uma justa política fiscal e uma dívida pública sustentável > A política orçamental deverá ter como objetivos centrais:
##### 2.3.1. Finanças públicas – uma justa política fiscal e uma dívida pública sustentável  
###### A política orçamental deverá ter como objetivos centrais:  
- um permanente rigor e disciplina na avaliação das despesas públicas, com o combate ao desperdício e um aumento da eficiência das administrações públicas;
- a prioridade ao investimento público, nomeadamente em infraestruturas, na produção nacional, no sector empresarial público, na investigação e desenvolvimento, na Escola Pública e no SNS, assim como nos serviços públicos, para inverter o rumo de degradação dos activos do Estado;
- um corte com as opções de externalização e aquisição de serviços do Estado em substituição do desenvolvimento de capacidades próprias, com as parcerias público privadas, concessões e outros sorvedouros de recursos públicos;
- a consolidação das finanças públicas, identificada como a sustentabilidade da dívida pública no médio e longo prazo, obtida através de políticas que promovam o emprego e o crescimento económico para, por essa via, reduzir o peso da dívida no PIB;
- a recusa dos dogmas neoliberais e dos constrangimentos impostos pela União Europeia, encarando a política orçamental como instrumento capaz de intervir positivamente nos ciclos económicos;
- uma política fiscal justa e progressiva, que assegure os meios necessários ao financiamento de serviços públicos universais e de qualidade, garantindo, por um lado, o alívio dos impostos sobre os trabalhadores, as MPME, os rendimentos mais baixos e intermédios, e sobre o consumo de bens essenciais; e, por outro, o incremento das receitas,tributando de forma adequada os mais elevados rendimentos, património e lucros, e combatendo a fraude e a evasão fiscal.

[Documento 3]
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 1 UM PROGRAMA PATRIÓTICO E DE ESQUERDA > O País tem recursos para concretizar a política alternativa que o PCP propõe
#### O País tem recursos para concretizar a política alternativa que o PCP propõe  
A política alternativa que o PCP propõe é possível, financeiramente viável, e indispensável para garantir a sustentabilidade do País no presente e no futuro.  
O PCP apresenta propostas para aumentar salários e pensões, melhorar serviços públicos e aumentar o investimento público. Como se financiam estas medidas?  
**Tal é possível a partir da conjugação de cinco opções fundamentais:**  
**Reorientar a política económica**, em ruptura com a política de direita, para o crescimento económico, o pleno emprego e a capacitação do Estado com os recursos de que necessita. Incluindo uma política orçamental sustentável e que contrarie as imposições do Euro e da UE, recusando sacrificar os salários, o investimento e os serviços públicos aos critérios da Moeda Única. Em 2023, se Portugal utilizasse a margem existente até aos limites de 3% do défice sobre o PIB - limites impostos pelo Pacto de Estabilidade da UE - isso significaria a possibilidade de utilizar mais 11 mil milhões de euros para responder a necessidades que se colocam. A opção foi outra com graves consequências.  
**Adoptar uma política de justiça fiscal que alargue as receitas do Estado**, sem sacrificar fiscalmente mais quem já hoje, vivendo do seu trabalho, paga demais. Exige-se a tributação efetiva dos lucros realizados no País, o englobamento obrigatório dos mais elevados rendimentos, ou o fim de regimes de privilégio fiscal que custam milhões de euros ao Estado, pôr fim às perdas de receita fiscal para paraísos fiscais (mais de 1.000 milhões de euros por ano) e ao conjunto de benefícios e isenções fiscais para as grandes empresas (mais 1.200 milhões de euros por ano em IRC). Ver o escândalo de operações de milhões de euros, como a venda das barragens do Douro entre a EDP e a Engie, continuarem por tributar.  
**Travar a transferência de recursos públicos para os grupos económicos**: pondo fim a regimes de rendas asseguradas, às custas do erário público e dos consumidores (caso exemplar o sector da energia); pôr fim às Parcerias Público Privadas, que, só no âmbito rodoviário, custam cerca de 1.000 milhões de euros por ano, entregues aos lucros das concessionárias; inverter a crescente transferência de recursos dos SNS para os grupos económicos da doença.  
**Melhorar a eficiência na despesa pública e internalizar serviços**, em particular, com a integração na Administração Pública de serviços externalizados, recuperar concessões atribuídas a privados, reduzindo custos que hoje alimentam os lucros de grandes empresas que vivem à sombra de contratos leoninos com entidades públicas.  
**Travar a sangria de recursos nacionais** para o estrangeiro resultante das privatizações, da livre circulação de capitais, da dependência externa do País, que só em 2022 representaram uma saída de 13,8 mil milhões de euros!

[Documento 4]
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 2 DESENVOLVIMENTO ECONÓMICO > 2.3. Políticas-chave > 2.3.1. Finanças públicas – uma justa política fiscal e uma dívida pública sustentável > Erradicação dos paraísos fiscais
###### Erradicação dos paraísos fiscais  
Sucessivos governos, implacáveis no combate à pequena fraude e evasão fiscais, têm desviado o olhar das grandes fugas aos impostos levadas a cabo com recurso a paraísos fiscais, não actuando de forma sistemática para pôr fim a esse escândalo. A erradicação dos paraísos fiscais exige uma cooperação internacional alargada e medidas a nível nacional. No plano internacional, Portugal deve ter um papel activo, contribuindo para a erradicação dos paraísos fiscais e para o aprofundamento do combate à elisão fiscal, em vez de continuar a contribuir para o jogo da "concorrência fiscal" na sua corrida para zero, que leva à isenção de qualquer taxação dos grandes rendimentos, patrimónios e lucros.

[Documento 5]
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 6 AFIRMAR A DEMOCRACIA, CUMPRIR A CONSTITUIÇÃO > 6.1. Defender o Regime Democrático > São orientações do PCP:
#### 6.1. Defender o Regime Democrático  
##### São orientações do PCP:  
- opor-se aos propósitos de revisão constitucional e não tomar qualquer iniciativa de revisão constitucional. Sendo desencadeado algum processo de revisão participará nele, com as suas próprias propostas, no sentido do aprofundamento dos valores de Abril na Constituição, no sentido do aperfeiçoamento da democracia considerada nas suas múltiplas dimensões política, económica, social e cultural;
- intervir decididamente no sentido de assegurar a subordinação do poder económico ao poder político, como determina a Constituição, incluindo a exigência de critérios e regras adequados de transparência e publicidade das decisões políticas e da gestão pública;
- contestar projectos de revisão das leis eleitorais que visem favorecer artificialmente a bipolarização entre PS e PSD e a diminuição do pluralismo da representação política, seja através da redução do número de deputados, seja através da criação de círculos uninominais, seja através da redução e manipulação da dimensão dos círculos existentes.  
A defesa da democracia política é inseparável da democraticidade e da proporcionalidade dos sistemas eleitorais, da autonomia de organização e funcionamento dos partidos políticos e de uma melhor participação dos cidadãos na vida política e social, em condições de igualdade.  
- contestar alterações às leis e aos métodos e processos eleitorais que diminuam as condições de fiabilidade, segurança, fiscalização e controlo democrático dos processos eleitorais;
- combater os projectos de eliminação da eleição directa e proporcional dos executivos municipais e lutar pelo reforço da colegialidade dos órgãos autárquicos;
- tomar a iniciativa de desenvolver a luta pela criação das regiões administrativas;
- reforçar os direitos dos trabalhadores e o exercício da liberdade sindical, bem como aperfeiçoar e ampliar os mecanismos de democracia participativa, designadamente através do uso de todos os direitos que a Constituição consagra, da acção dos trabalhadores e das massas populares e das suas organizações, do movimento associativo nas suas diferentes expressões, do exercício do direito de petição, de iniciativa legislativa, de acção popular.

[Documento 6]
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 3 VALORIZAR OS TRABALHADORES PROMOVER O EMPREGO COM DIREITOS, O AUMENTO DOS SALÁRIOS E A MELHORIA DAS CONDIÇÕES DE VIDA E DE TRABALHO > 3.6 Defender os direitos individuais e coletivos > O PCP propõe:
##### O PCP propõe:  
- a reposição do direito constitucional de negociação e contratação colectiva, com a revogação das normas relativas à caducidade das convenções e a reposição do princípio do tratamento mais favorável ao trabalhador, não podendo as convenções coletivas estabelecer normas menos favoráveis que as consagradas na lei;
- a reposição da norma de renovação automática das convenções, pela qual elas vigoram até serem substituídas por outras livremente negociadas pelas partes;
- a revogação do regime da escolha de convenção aplicável por trabalhador não filiado em associação sindical;
- a retroactividade na aplicação das condições fixadas pelas portarias de extensão, com efeitos à data da entrada em vigor da respetiva convenção colectiva;
- o cumprimento do direito de negociação colectiva na Administração Pública.

## Iniciativa Liberal
[Documento 7]
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 1. MAIS OPORTUNIDADES, MAIS SALÁRIO > 1.2. Reforma Fiscal: Menos Impostos, Mais Salário > Impostos mais baixos e mais simples para todos
#### 1.2. Reforma Fiscal: Menos Impostos, Mais Salário  
##### Impostos mais baixos e mais simples para todos  
Portugal precisa de crescer. Esta é a principal bandeira que a Iniciativa Liberal defende desde que foi fundada. Esta necessidade de crescimento reflete-se no PIB per capita em paridades de poder de compra face à média da União Europeia. Portugal encontra-se praticamente estagnado desde 2011, com oscilações pouco significativas. Portugal mantém-se na cauda da Europa, sendo ultrapassado por 8 países desde o ano 2000. O crescimento não é meramente um capricho liberal: ele não só reflete a melhoria das condições de vida das pessoas, como é igualmente essencial para a melhoria no rácio da dívida pública sobre o produto e o respetivo cumprimento das regras orçamentais da União Europeia, sem colocar em causa o funcionamento do Estado Social e o investimento público.  
O país tem de ser fiscal e administrativamente competitivo, tirando peso e complexidade ao sistema fiscal atualmente vigente. **Portugal tem de deixar de ter uma das maiores taxas de esforço fiscal da União Europeia e passar a ter uma das menores**, como é o caso de países mais liberais como a Irlanda, o Luxemburgo e os Países Baixos. Segundo os dados do Eurostat, Portugal teve em 2022 a quarta maior taxa de esforço fiscal da Europa. Os portugueses não suportam mais esta situação.  
Hoje temos impostos de rico e salários de pobre. Além disso, temos um nível de progressividade enorme, com um recorde europeu de nove escalões, que pune quem quer subir na vida pelo trabalho. E temos um nível de tax wedge muito elevado, onde o Estado leva em média 42% do que a empresa paga por um trabalhador e onde o Estado leva cerca de metade do que a empresa paga por um aumento salarial. É isto que temos de mudar imediatamente. O sistema fiscal liberal recompensa o esforço, dedicação e produtividade daqueles que trabalham e aqueles que assumem riscos, estimulando assim a concorrência.  
Hoje, essa competição não se limita ao âmbito nacional, estendendo-se ao cenário continental e mesmo global. Portugal está em competição direta com o resto do mundo para atrair capital e empregos qualificados. Contudo, a carga fiscal excessiva sobre o trabalho e as empresas nas últimas décadas resultou numa significativa emigração de mão-de-obra altamente qualificada e desvio de investimento para outras regiões. É urgente alterar este panorama.  
**A Iniciativa Liberal defende a descida e simplificação dos impostos sobre rendimentos das pessoas e das empresas, nomeadamente do IRS e do IRC**, promovendo ainda a eliminação de casos de dupla tributação, bem como de taxas e contribuições coercivas que promovem complexidade e barreiras à entrada em mercados competitivos. Além disso, se a energia – neste caso eletricidade e gás – é um bem essencial quer para a vida das famílias quer para a atividade das empresas então não pode ser taxada como um bem de luxo, devendo **o IVA do gás e da eletricidade baixar para 6%**.  
Para crescermos, é também necessária a **revisão e redução de impostos sobre o património**, uma vez que se tratam de impostos que incidem sobre bens comprados por rendimentos que já foram tributados e sobre transações que também foram já tributadas. A Iniciativa Liberal apresenta igualmente alterações ao IMI, de forma a desonerar a detenção do património, bem como ao Imposto do Selo, ao IVA e ao IMT, para desonerar a construção e a aquisição da habitação própria e permanente na transação, medidas que são expressamente apresentadas no capítulo referente à Habitação.  
**Reduzir e Simplificar o IRS até à Taxa Única de 15%**  
Propomos **implementar uma taxa única de 15% a aplicar-se aos rendimentos acima do salário mínimo nacional anualizado**, garantindo a progressividade e mantendo as atuais deduções à coleta previstas.  
A Iniciativa Liberal mantém-se firme na sua proposta de reduzir a progressividade excessiva e simplificar o IRS para todos os contribuintes que têm de obrigatoriamente pagar o imposto, sem prejudicar os contribuintes isentos de IRS.  
Com a aplicação deste IRS substancialmente mais baixo para todos, serão igualmente revogados os atuais programas e benefícios fiscais dirigistas que causam injustiças sociais entre os mais jovens e não jovens, bem como entre os residentes e os não residentes.  
Estamos disponíveis para aprovar e desenvolver propostas transitórias, desde que se baixe significativamente a progressividade excessiva do imposto, reduzindo o número de escalões, e que se incentive claramente a competitividade fiscal dos salários de emprego qualificado. Mais concretamente, a Iniciativa Liberal **numa primeira fase propõe um imposto com duas taxas**, uma de 15% sobre os rendimentos acima de 11.480 euros e abaixo de 21.321 euros, **garantindo a progressividade**, sendo aplicada uma taxa de 28% acima desse patamar de rendimento anual. Em suma, pretende-se isentar de imposto os rendimentos mais baixos aumentando significativamente a dedução específica, agregando os primeiros quatro escalões e, por fim, agregando os últimos cinco escalões com a taxa de 28%. Eis alguns exemplos da poupança esperada por esta alteração.  
| Rendimento | Rendimento<br>Imposto   |          | Proposta de taxa única de 15% |                    |                 | Proposta transitória de 2 taxas |                    |                 |
| ---------- | ----------------------- | -------- | ----------------------------- | ------------------ | --------------- | ------------------------------- | ------------------ | --------------- |
| mensal     | bruto<br>bruto<br>anual | Atual \* | Imposto\*                     | Poupança<br>(abs.) | Poupança<br>(%) | Imposto \*                      | Poupança<br>(abs.) | Poupança<br>(%) |
| 900        | 12.600                  | 784      | 168                           | 616                | 79%             | 168                             | 616                | 79%             |
| 1.100      | 15.400                  | 1.667    | 588                           | 1.079              | 65%             | 588                             | 1.079              | 65%             |
| 1.300      | 18.200                  | 2.295    | 1.008                         | 1.287              | 56%             | 1.008                           | 1.287              | 56%             |
| 1.500      | 21.000                  | 2.952    | 1.428                         | 1.524              | 52%             | 1.428                           | 1.524              | 52%             |
| 1.700      | 23.800                  | 3.680    | 1.848                         | 1.832              | 50%             | 2.170                           | 1.510              | 41%             |
| 2.500      | 35.000                  | 7.397    | 3.528                         | 3.869              | 52%             | 5.306                           | 2.091              | 28%             |
| 4.000      | 56.000                  | 15.060   | 6.678                         | 8.382              | 56%             | 11.186                          | 3.874              | 26%             |  
\* – Imposto apurado antes de deduções à coleta. Estas deduções, mantendo-se, conforme proposto, são indiferentes para o apuramento da poupança entre o imposto atual e o imposto proposto.  
**Baixar o Imposto sobre rendimentos de capitais e prediais**  
Em matéria de tributação de rendimentos de capitais, mais-valias e prediais, a Iniciativa Liberal defende a **redução do imposto para 14,5%, sem englobamento obrigatório**. Em matéria de rendimentos prediais de arrendamento habitacional, propõe-se uma taxa 14.5% com uma descida gradual do imposto, conforme referido posteriormente no capítulo A.2 sobre Habitação.  
**Tributar stock-options no momento da realização da venda e não no exercício da opção**  
A Iniciativa Liberal quer corrigir o momento da tributação da conversão de opções sobre ações em ações para que a mesma ocorra no momento da alienação do ativo. Atualmente, existem duas formas de tributar a conversão de opções sobre ações em ações. A primeira é a prevista no Código de IRS, que prevê a tributação no período em que é exercida a opção e que dá o direito ao trabalhador de ter o número de ações correspondentes, com a valorização que possuem as ações à data da conversão. A segunda com a tributação a ocorrer apenas quando se der a mais- ou menos-valia das ações sobre a qual o trabalhador exerceu a sua opção, conferida pelo benefício fiscal criado por este Governo para os trabalhadores em start-ups. Esta situação cria uma tremenda **desigualdade entre contribuintes em circunstâncias idênticas**, levando a que os primeiros sejam, invariavelmente, prejudicados face aos segundos apenas por uma questão de tratamento fiscal.  
Da forma como está a ser aplicada a lei, há casos de trabalhadores que, não querendo beneficiar dos descontos de taxas que o benefício fiscal também concede, vêem-se na obrigação de se endividar para liquidar impostos. Isto sucede por causa de uma variação do valor das ações que poderão não conseguir liquidar por ainda não terem realizado qualquer tipo de mais-valia com as mesmas. Ou seja, pagam impostos por uma mais-valia esperada, muitas vezes pressionados por apertados prazos de exercício de conversão de opções de ações, sem conhecimento da valorização das mesmas no momento da decisão do exercício das opções.  
A forma mais adequada para garantir um tratamento justo, informado e a capacidade contributiva dos contribuintes é **tributar esta conversão de opção de ação em ação como rendimento de trabalho apenas quando essa ação gerar uma mais ou menos valia na sua alienação**, tal como previsto no benefício fiscal recentemente criado pelo Governo.  
**Baixar e Simplificar o IRC**  
A Iniciativa Liberal propõe uma **taxa de IRC de 12% para as empresas**. Cumprindo a nova legislação europeia, a Iniciativa Liberal quer **aplicar a taxa de IRC mínima de 15% para as multinacionais com uma faturação anual superior a 750 milhões de euros**, seguindo o valor mínimo do imposto pela OCDE, e que a UE através da nova diretiva europeia requer dos Estados-Membros. É urgente simplificar e libertar as empresas da necessidade de consumirem tempo e recursos em atividades improdutivas, permitindo um foco na produção, na melhoria contínua e na expansão. E é necessário atrair investimento estrangeiro, colocando Portugal entre os países mais atrativos da Europa ocidental para as empresas a nível fiscal. Esta reforma implica **revogar as derramas** bem como eliminar as tributações autónomas que representam acréscimos de carga fiscal sobre as empresas em Portugal, completamente contrárias à prática internacional.  
**Portugal tem a segunda maior taxa estatutária máxima de IRC da OCDE**, sendo igualmente o  
**segundo pior país em termos de competitividade fiscal das empresas**, entre os trinta e oito países que a integram, de acordo com o estudo da Tax Foundation em 2023. Na fiscalidade sobre as empresas, Portugal destaca-se negativamente pela sua taxa máxima e pela complexidade. A Iniciativa Liberal tem alertado incessantemente para estes dois fatores, uma vez que põem em causa a capacidade de atrair e manter capital em Portugal, ainda mais num mercado de capitais tão aberto como é a União Europeia.  
Para além do efeito dissuasor expectável que resulta da taxa estatutária máxima de 31.5% de IRC existente em Portugal, a **progressividade imposta pela derrama estadual e as diferenciações de taxação entre empresas com diferentes dimensões, impede a progressão da evolução das empresas** e incentiva-as a manterem-se pequenas e pouco competitivas. Há ainda uma imensidão de benefícios fiscais que, para além de representarem um ímpeto dirigista sobre aquilo que deveria ser a livre iniciativa das empresas, é também uma fonte de improdutividade da nossa economia, abrindo portas à corrupção e favorecimento de certos nichos e empresas.

[Documento 8]
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 1. MAIS OPORTUNIDADES, MAIS SALÁRIO > 1.2. Reforma Fiscal: Menos Impostos, Mais Salário > Impostos mais baixos e mais simples para todos
**Tributar stock-options no momento da realização da venda e não no exercício da opção**  
A Iniciativa Liberal quer corrigir o momento da tributação da conversão de opções sobre ações em ações para que a mesma ocorra no momento da alienação do ativo. Atualmente, existem duas formas de tributar a conversão de opções sobre ações em ações. A primeira é a prevista no Código de IRS, que prevê a tributação no período em que é exercida a opção e que dá o direito ao trabalhador de ter o número de ações correspondentes, com a valorização que possuem as ações à data da conversão. A segunda com a tributação a ocorrer apenas quando se der a mais- ou menos-valia das ações sobre a qual o trabalhador exerceu a sua opção, conferida pelo benefício fiscal criado por este Governo para os trabalhadores em start-ups. Esta situação cria uma tremenda **desigualdade entre contribuintes em circunstâncias idênticas**, levando a que os primeiros sejam, invariavelmente, prejudicados face aos segundos apenas por uma questão de tratamento fiscal.  
Da forma como está a ser aplicada a lei, há casos de trabalhadores que, não querendo beneficiar dos descontos de taxas que o benefício fiscal também concede, vêem-se na obrigação de se endividar para liquidar impostos. Isto sucede por causa de uma variação do valor das ações que poderão não conseguir liquidar por ainda não terem realizado qualquer tipo de mais-valia com as mesmas. Ou seja, pagam impostos por uma mais-valia esperada, muitas vezes pressionados por apertados prazos de exercício de conversão de opções de ações, sem conhecimento da valorização das mesmas no momento da decisão do exercício das opções.  
A forma mais adequada para garantir um tratamento justo, informado e a capacidade contributiva dos contribuintes é **tributar esta conversão de opção de ação em ação como rendimento de trabalho apenas quando essa ação gerar uma mais ou menos valia na sua alienação**, tal como previsto no benefício fiscal recentemente criado pelo Governo.  
**Baixar e Simplificar o IRC**  
A Iniciativa Liberal propõe uma **taxa de IRC de 12% para as empresas**. Cumprindo a nova legislação europeia, a Iniciativa Liberal quer **aplicar a taxa de IRC mínima de 15% para as multinacionais com uma faturação anual superior a 750 milhões de euros**, seguindo o valor mínimo do imposto pela OCDE, e que a UE através da nova diretiva europeia requer dos Estados-Membros. É urgente simplificar e libertar as empresas da necessidade de consumirem tempo e recursos em atividades improdutivas, permitindo um foco na produção, na melhoria contínua e na expansão. E é necessário atrair investimento estrangeiro, colocando Portugal entre os países mais atrativos da Europa ocidental para as empresas a nível fiscal. Esta reforma implica **revogar as derramas** bem como eliminar as tributações autónomas que representam acréscimos de carga fiscal sobre as empresas em Portugal, completamente contrárias à prática internacional.  
**Portugal tem a segunda maior taxa estatutária máxima de IRC da OCDE**, sendo igualmente o  
**segundo pior país em termos de competitividade fiscal das empresas**, entre os trinta e oito países que a integram, de acordo com o estudo da Tax Foundation em 2023. Na fiscalidade sobre as empresas, Portugal destaca-se negativamente pela sua taxa máxima e pela complexidade. A Iniciativa Liberal tem alertado incessantemente para estes dois fatores, uma vez que põem em causa a capacidade de atrair e manter capital em Portugal, ainda mais num mercado de capitais tão aberto como é a União Europeia.  
Para além do efeito dissuasor expectável que resulta da taxa estatutária máxima de 31.5% de IRC existente em Portugal, a **progressividade imposta pela derrama estadual e as diferenciações de taxação entre empresas com diferentes dimensões, impede a progressão da evolução das empresas** e incentiva-as a manterem-se pequenas e pouco competitivas. Há ainda uma imensidão de benefícios fiscais que, para além de representarem um ímpeto dirigista sobre aquilo que deveria ser a livre iniciativa das empresas, é também uma fonte de improdutividade da nossa economia, abrindo portas à corrupção e favorecimento de certos nichos e empresas.  
O tecido empresarial português tem de ser mais produtivo e mais atrativo, pelo que um sistema fiscal mais simples e mais baixo é fundamental para esse desenvolvimento que a todos beneficia ao enriquecer a economia nacional. Esta simplificação do sistema permite, igualmente, libertar recursos da própria Autoridade Tributária para focar na pedagogia junto do contribuinte para liquidação voluntária, bem como, investigar e combater situações de evasão e fraude fiscal.  
**Eliminar taxas, contribuições e impostos adicionais**  
A Iniciativa Liberal quer eliminar taxas, contribuições e impostos adicionais com vista a **aumentar a competitividade fiscal do país e baixar os custos de contexto**. Sugerimos eliminar:  
- A duplicação de impostos resultante da cobrança de impostos sobre transações que envolvem outros impostos, como é o caso do Imposto do Selo na compra de casas sujeitas ao Imposto Municipal sobre as Transmissões (IMT);
- Contribuição extraordinária sobre o Alojamento Local;
- Contribuição extraordinária sobre a indústria farmacêutica;
- Contribuição extraordinária sobre os fornecedores do Serviço Nacional de Saúde de dispositivos médicos;
- Contribuição extraordinária sobre o setor energético;
- Taxas devidas ao ICP-ANACOM, no âmbito das entidades formadoras na área de infraestruturas: ITUR e ITED;
- Taxas de utilização do espectro radioeléctrico;
- Taxas de emissão de títulos habilitadores de serviços de rádio e televisão;

[Documento 9]
  Secção: PROGRAMA ELEITORAL > PORTUGAL A CRESCER > 1. BAIXAR IMPOSTOS E DESBUROCRATIZAR
### 1. BAIXAR IMPOSTOS E DESBUROCRATIZAR  
- **Taxa única de IRS de 15% sobre a parte dos rendimentos que exceda o Salário Mínimo Nacional, começando de forma gradual com duas taxas de 15% e 28%, aumentando imediatamente o salário líquido**
- **Reduzir a carga fiscal sobre os profissionais liberais e os trabalhadores independentes**
- **Taxa única de IRC de 12% para as empresas, excepto para as grandes multinacionais que será de 15% de acordo com o exigido pela lei europeia**
- **Criar uma task force de eliminação de burocracias desnecessárias em diálogo com cidadãos e empresas**
- **Criar Zonas Económicas Especiais (ZEE) de baixa fiscalidade no interior do país para atrair investimento direto estrangeiro e promover a criação de hubs empresariais**
- **Reverter as normas do pacote Mais Habitação relativas ao Alojamento Local, eliminar a redução do coeficiente fiscal**
- **Eliminar várias taxas e contribuições extraordinárias como o adicional ao IMI (AIMI) e o imposto do selo sobre transações já taxadas**
- **Eliminar gradualmente o Imposto Único de Circulação (IUC)**
- **Reduzir o imposto sobre rendimentos de capitais para 14,5%**
- **Compromisso de Orçamentos com superávit e redução da dívida pública**

[Documento 10]
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 1. MAIS OPORTUNIDADES, MAIS SALÁRIO > 1.1. Desbloquear o Mercado: Menos Burocracia, Mais Investimento > Empresas e Atração de Capital
**É também crítico eliminar as barreiras ao Investimento Direto Estrangeiro (IDE)**. Para atrair investimento estrangeiro é necessário diminuir custos de entrada, colocando-os, no mínimo, ao nível dos Países de semelhante dimensão a Portugal e nossos concorrentes directos na atracção desse investimento. Apesar da sua atratividade, Portugal não está a aproveitar todas as oportunidades que tem neste âmbito. Portugal tem de espelhar o seu enquadramento legal à luz do europeu, evitando densificações desnecessárias de diretivas europeias que vão para lá daquilo exigido por outros Estados-Membro. Deve também garantir que os litígios são resolvidos com celeridade, assim como pagamentos tardios e cobranças judiciais, outra das preocupações de investidores internacionais. Os litígios entre os indivíduos e as empresas com o Estado continuam a ser morosos e especialmente caros, sendo muitas vezes preferível desistir da litigância, mesmo quando se tem razão.  
**As interações com o Estado e entidades do Estado têm também de ser agilizadas:** através da transformação digital do mesmo; através da simplificação e desburocratização administrativa; e através da reforma do enquadramento regulatório das empresas. Por outro lado, a previsibilidade dos processos, assim como o seu tempo, são fatores críticos para a atração de investimento, sobretudo no que concerne os pedidos de licenciamento e autorizações. Portugal é um dos países onde os atrasos de pagamentos mais causam disrupção na operação das empresas, sendo o Estado um dos responsáveis, com impactos nefastos sobre as mesmas.  
Portugal é o terceiro País da OCDE com maior índice de rigidez laboral. Esta rigidez faz aumentar o risco de novas contratações do ponto de vista do empresário. Assim, os empresários optam ou por não contratar de todo, diminuindo a procura do factor Trabalho (o que prejudica quem procura emprego) ou pela subcontratação (outsourcing) de outras empresas. Esta opção é uma das causas para o facto de haver tantas empresas em Portugal com um, dois ou três colaboradores que, como já vimos, é um dos problemas da nossa economia e factor inibidor de crescimento económico. Esta falta de flexibilidade levou, por exemplo, à existência de um sistema dual em que o despedimento coletivo é fácil, obedecendo a critério mais objetivos, mas o despedimento individual é complexo e sustentado em critérios mais subjetivos e pouco concretizados, prejudicando sobretudo os mais jovens. Conforme propomos no capítulo sobre trabalho, **é fundamental flexibilizar a legislação laboral de forma equilibrada e simétrica**. A Iniciativa Libera quer, por exemplo, apostar num modelo de **flexisegurança semelhante ao de vários países nórdicos**, que garanta flexibilidade contratual ao empregador e um forte apoio social a pessoas em situação de desemprego (ver capítulo B.4).  
Ao longo deste programa, a Iniciativa Liberal apresentará uma série de reformas estruturais no trabalho, no ambiente fiscal, no Estado e na justiça que criam as condições para que Portugal atraia muito mais investimento direto estrangeiro.  
**Afirmar uma política fiscal atrativa**  
Não são apenas os impostos que condicionam a vinda de empresas para Portugal, mas são um dos principais fatores. Uma política fiscal atrativa é fundamental para podermos atrair empresas e capital humano que crie empresas de alto valor acrescentado e, como tal, de elevados salários.  
**A este nível é também fundamental uma baixa significativa do IRC e dos demais impostos pagos pelas empresas, como a tributação autónoma, como fator de atratividade**. Portugal é o país europeu da OCDE com taxa máxima de IRC mais elevada. Ao mesmo tempo, Portugal é dos países em que existe maior diferença entre a taxa máxima estatutária de IRC e a taxa efetiva. Isto condiciona a gestão das empresas, otimizada não em função das suas necessidades e operações mas em função do que o Estado acha que é importante. A redução ambiciosa do IRC deve por isso ser acompanhada pelo fim dos benefícios fiscais discricionários, que reduzem a transparência e a incerteza do processo. Por outro lado, é necessário simplificar as obrigações de reporte fiscal, que tornam o processo dispendioso do ponto de vista administrativo para as empresas.  
Adicionalmente, as empresas deverão poder fazer a dedução integral da despesa de capital (máquinas, fábricas, equipamentos, etc.) na matéria colectável, desta forma criando mais incentivos à renovação e atualização tecnológica do parque industrial, assim como da despesa em I&D, desta forma fomentando uma **colaboração mais estreita entre empresas** **e institutos de I&D, criando um ambiente favorável à atração de capital de risco para que os nossos melhores talentos possam inovar dentro do país**.  
**Criar Zonas Económicas Especiais**  
A Iniciativa Liberal defende a baixa de impostos no país inteiro e defende também uma forte descentralização da capacidade de discriminar taxas de imposto que confere ao poder local maior competitividade. **Os municípios, em concorrência e colaboração entre si, devem poder criar Zonas Económicas Especiais (ZEE) de baixa fiscalidade no território português**, como forma de atrair investimento direto estrangeiro e promover a criação de hubs empresariais.  
As Zonas Económicas Especiais idealmente podem ser especializadas setorialmente (v.g., tecnologia e digital, biotecnologia, nanoindústria, têxtil e calçado, energias renováveis, entre outros) e localizadas em zonas de baixa densidade populacional, servindo assim um outro desiderato político e social, o da dinamização do interior e coesão territorial.

</details>

## item-04

**Question:** Que penas propõe o CHEGA para criminosos reincidentes e crimes graves?

**Answer:**

O programa do **CHEGA** para o sistema prisional e combate à criminalidade foca-se no endurecimento das penas e na redução de benefícios para criminosos reincidentes e autores de crimes graves:

• **Aumento das penas de prisão**: O partido propõe o aumento das molduras penais para crimes considerados graves, com o objetivo de aumentar o efeito dissuasor.
• **Restrição de benefícios e saídas precoces**: O **CHEGA** defende a limitação ou eliminação de benefícios penitenciários, como a liberdade condicional, para criminosos reincidentes e para aqueles que cometam crimes violentos ou graves.
• **Cumprimento efetivo da pena**: O partido argumenta que as penas devem ser cumpridas de forma mais rigorosa, defendendo que a reincidência deve ser um fator determinante para impedir a saída antecipada do recluso.
• **Foco na segurança das vítimas**: As medidas visam garantir que o sistema de justiça priorize a proteção das vítimas e a punição efetiva de quem viola a lei de forma reiterada.

**Reference answer:**

O CHEGA propõe introduzir a pena de prisão perpétua com possibilidade de revisão depois de cumprida uma parte da pena e a sanção acessória de tratamento para inibição da líbido ("castração química"), de carácter temporário e para reincidentes. Defende ainda o endurecimento das penas para crimes como violência doméstica, crimes sexuais e contra crianças, a revisão do regime de prescrição das penas (sobretudo nos crimes contra crianças e de natureza económica), e uma revisão constitucional que permita estas penas.

**faithfulness** — Is the claim supported by the CONTEXT?

- [ ] O CHEGA propõe o aumento das molduras penais para crimes considerados graves.
- [ ] O CHEGA defende a limitação ou eliminação da liberdade condicional para criminosos reincidentes.
- [ ] O CHEGA defende a limitação ou eliminação da liberdade condicional para autores de crimes violentos ou graves.
- [ ] O CHEGA defende que a reincidência deve ser um fator determinante para impedir a saída antecipada do recluso.

**correctness_recall** — Does the ANSWER state this reference claim?

- [ ] O CHEGA propõe a introdução da pena de prisão perpétua.
- [ ] O CHEGA propõe que a pena de prisão perpétua tenha possibilidade de revisão depois de cumprida uma parte da pena.
- [ ] O CHEGA propõe a sanção acessória de tratamento para inibição da líbido (castração química).
- [ ] O CHEGA propõe que a sanção acessória de castração química tenha carácter temporário.
- [ ] O CHEGA propõe que a sanção acessória de castração química se aplique a reincidentes.
- [ ] O CHEGA defende o endurecimento das penas para crimes de violência doméstica.
- [ ] O CHEGA defende o endurecimento das penas para crimes sexuais.
- [ ] O CHEGA defende o endurecimento das penas para crimes contra crianças.
- [ ] O CHEGA defende a revisão do regime de prescrição das penas.
- [ ] O CHEGA defende a revisão do regime de prescrição das penas sobretudo nos crimes contra crianças.
- [ ] O CHEGA defende a revisão do regime de prescrição das penas sobretudo nos crimes de natureza económica.
- [ ] O CHEGA defende uma revisão constitucional que permita as penas propostas.

relevance: 

<details><summary>Context the generator read</summary>

[Documento 1] Partido: CHEGA | Tópicos: justica
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > II CAPÍTULO POR UMA JUSTIÇA QUE FUNCIONE. COMO? > PROPOSTAS
- Criar um regime especial de aposentação e de acesso ao regime de pré-aposentação;  
- Rever o Estatuto dos Funcionários Judiciais e revalorização dos grupos de pessoal da carreira de funcionário judicial;  
- Revalorização remuneratória de todo o pessoal da carreira de funcionário judicial;  
- Pagar as horas extraordinárias.  
**25.** Responder às reivindicações dos Oficiais de Registo e Notariado:  
- Proceder ao recrutamento urgente dos Conservadores de Registos e dos Oficiais de Registos em falta, de acordo com o levantamento que venha a ser feito, e com uma programação projectada para 3 anos;  
- Rever o estatuto profissional das carreiras dos oficiais de registos, corrigindo as iniquidades e omissões do Decreto- -Lei n.º 115/2018, de 21 de dezembro;  
- Corrigir assimetrias salariais, em sede de sistema remuneratório;  
- Recuperar as actualizações indiciárias em dívida aos Oficiais de Registo desde 2001;  
- Proceder ao pagamento do abono para falhas;  
- Iniciar a negociação tendente a garantir o pagamento do prémio de desempenho e produtividade;  
- Proceder à promoção dos trabalhadores remanescentes da extinta carreira de escriturário, a escriturários superiores;  
- Rever as condições de desempenho de funções, nomeadamente ao nível da requalificação das instalações, colmatar a falta de meios de trabalho e implementar verdadeiras políticas de Segurança, Saúde e Higiene no Trabalho;  
- Rever as condições em que se processa o atendimento dos utentes dos serviços de registo, no sentido de assegurar a necessária reserva durante o atendimento.  
**26.** Responder às reivindicações dos advogados, solicitadores e agentes de execução:  
- Permitir a escolha entre a inscrição na Caixa de Previdência dos Advogados e Solicitadores e o regime da Segurança Social;  
- Actualizar a tabela de honorários do acesso ao Direito, assegurar o pagamento de despesas no âmbito da representação de beneficiários deste sistema e ainda um sistema de pagamento progressivo;  
- Ponderar a alteração do método de distribuição dos processos a Agentes de Execução, passando nomeadamente para um processo de distribuição aleatória, com critério de proximidade;  
- Assegurar a suspensão dos prazos em caso de morte de filho, assim como garantir apoios em caso de doença grave ou prolongada;  
- Garantir às mães com bebés recém-nascidos (até aos 4 meses) a possibilidade de proceder ao adiamento das diligências;  
- Prever condições para o exercício dos mandatos, junto dos tribunais, nomeadamente disponibilizando acesso à internet.  
**27.** Responder às reivindicações dos guardas prisionais e  
técnicos de reinserção social:  
- Proceder à regulamentação uniforme do sistema de avaliação do Corpo da Guarda Prisional (CGP);  
- Abrir vagas em número suficiente para a promoção dos Guardas Prisionais a Guardas Principais, alguns dos quais a aguardar a promoção há cerca de 20 anos;  
- Proceder à abertura de concursos para recrutamento de novos efectivos, com regularidade anual ou bianual;  
- Rever as normas estatutárias da carreira de guarda prisional, de modo a tornar a profissão mais atractiva e combater a falta de interesse que a carreira motiva em novos candidatos, com concursos de admissão que não conseguem preencher todos os lugares abertos;  
- Assegurar que os reformados do CGP, que não tenham condições económicas para encontrar outra habitação, não sejam despejados das respectivas casas de função;  
- Assegurar que as casas de função degradadas sejam objeto de recuperação pelo IGFEJ e sejam utilizadas para alojar elementos do CGP que se encontrem deslocados dos seus locais de residência;  
- Renovar profundamente todo o parque automóvel afeto ao sistema prisional, visto que uma grande parte da frota é obsoleta, nos termos da lei de programação plurianual para a Justiça, a aprovar;  
- Ampliação e construção de novos estabelecimentos prisionais necessários em diversas zonas do país;  
- Criminalizar o incitamento ao ódio contra guardas prisionais e agravar as penas relativas a agressões;  
- Delinear uma estratégia de combate ao tráfico e consumo de droga nos estabelecimentos prisionais portugueses;  
- Proceder à contratação de técnicos de reinserção social;  
- Proceder à revalorização urgente das carreiras de técnico de reinserção social, já em 2024, principalmente na componente remuneratória, de modo a aumentar o potencial de captação e fixação de efectivos, evitando a debandada para outras carreiras ao abrigo da mobilidade.  
**28.** Impedir a renovação ou rescindir os contratos de arrendamento milionários de edifícios privados onde se encontram instalados vários tribunais, como por exemplo o arrendamento dos edifícios do Campus de Justiça de Lisboa, e, ao invés, utilizar o património do Estado existente, devoluto ou subaproveitado, para a instalação de tribunais.  
**29.** Adequar a arquitectura e espaços de Justiça, acabando com os Tribunais em contentores, e em edifícios destinados a escritórios, melhorando e dignificando as condições de trabalho para os funcionários de justiça, magistrados do Ministério Público e Juízes.  
**30.** Reintroduzir a utilização dos símbolos nacionais e de Justiça nos tribunais, recuperando mobiliário e objectos representativos da cultura portuguesa, promovendo o respeito nacional pelos tribunais, dignificando a sua imagem.  
**31.** Aprovar a lei de programação plurianual para a justiça, por forma a dar resposta à falta de equipamentos ou necessidade de modernização dos existentes, identificação de um plano de recuperação de edifícios, etc.  
**32.** Alterar as regras de acesso à arbitragem na Justiça Tributária, de forma a que qualquer litígio em que esteja envolvido dinheiro público, o Ministério Público seja obrigatoriamente parte acessória.  
**33.** Assegurar que todas as decisões arbitrais são públicas e ficam disponíveis online.  
**34.** Proceder à Reforma do Código de Procedimento e de Processo Tributário, com o objectivo de simplificação, instituindo regras que efectivamente garantam a celeridade da justiça fiscal.  
**35.** Implementar um plano de contingência urgente para eliminar as pendências nos Tribunais Administrativos e Fiscais.  
**36.** Assegurar que todas as sentenças e acórdãos, de todas as instâncias são disponibilizadas online, devendo ser tomadas as medidas necessárias para a protecção dos dados pessoais.  
**37.** Proceder à reforma do regime de recursos em matéria penal, de modo a imprimir maior celeridade aos processos, impedir a instrumentalização dos recursos e racionalizar o acesso ao Supremo Tribunal de Justiça, bem como rever a fase de instrução, nomeadamente a sua função e prazos.  
**38.** Instituir regras jurídicas que obviem o fenómeno da prolixidade nas peças processuais penais, beneficiando a celeridade da justiça.  
**39.** Rever o regime de prescrição das penas, nomeadamente no que diz respeito aos crimes contra crianças mas também relativos aos crimes de natureza económica, garantindo uma maior possibilidade de fazer justiça.  
**40.** Proceder à revisão e endurecimento das penas relativamente a crimes como violência doméstica, crimes de natureza sexual, contra crianças, entre outros.  
**41.** Introduzir no nosso Código Penal a sanção acessória de tratamento para a inibição da líbido, mais comumente conhecida como "castração química", de carácter temporário e para reincidentes.  
**42.** Introduzir a pena de prisão perpétua com possibilidade de revisão depois de cumprida uma parte da pena.  
**43.** Combater a violência doméstica, através:  
- Do aumento dos meios disponíveis para a investigação deste tipo de crime;  
- Mais formação para todos os envolvidos;
- Aumento das penas;  
- Inverter a ideia de que a vítima, normalmente mulher, é que tem que ser afastada de casa e colocada em regime de casa-abrigo, ao invés do criminoso ser afastado;  
- Promover uma maior utilização dos meios técnicos de controlo à distância;  
- Proceder à revisão das fichas de risco;  
- Aumentar o número de casas-abrigo e assegurar a existência de uma rede nacional com implementação em todo o território;  
- Melhorar o financiamento das entidades que prestam apoio às vítimas.  
**44.** Combater a violência sexual:  
- Através do aumento das penas;
- Da alteração da natureza do crime para crime público;  
- Mais formação para todos os envolvidos, reduzindo as potenciais situações de revitimização;  
- Alteração do regime de declarações para memória futura;  
- Assegurar que no momento da queixa é atribuído defensor oficioso à vítima;  
- Garantir à vítima a possibilidade de proceder à suspensão provisória do processo;  
- Garantir a possibilidade de escolha do sexo da pessoa que procede à perícia médica;  
- Criar centros de apoio para sobreviventes de violência sexual;  
- Proceder a um inquérito nacional de vitimação;  
- Assegurar a criação de um canal permanente de denúncia de abusos sexuais em diversas instituições.  
**45.** Reverter a Lei n.º 55/2023, de 08 de Setembro que clarifica o regime sancionatório relativo à detenção de droga para consumo independentemente da quantidade e estabelece prazos regulares para a atualização das normas regulamentares.  
**46.** Reverter as alterações impostas às Ordens Profissionais, garantindo a isenção do funcionamento das Ordens, a preservação dos seus actos profissionais e da sua autonomia.  
**47.** Criar o Provedor da Criança e adaptar os sistemas judiciais e extrajudiciais aos direitos, interesses e necessidades específicas das crianças, procedendo à adaptação das salas nos tribunais, mas também usando as melhores técnicas para o diálogo com as mesmas, assim como assegurar o apoio de outros profissionais como psicólogos ou assistentes sociais, por exemplo.  
**48.** Estabelecer a residência alternada como regime privilegiado na regulação do exercício das responsabilidades parentais, exceptuando contextos de violência doméstica.  
**49.** Rever os processos de protecção das crianças e as medidas de promoção e protecção, assim como rever e reformular a medida de internamento no processo tutelar educativo.  
**50.** Reforçar a protecção das vítimas de devassa da vida privada por meio de partilha não consentida de conteúdos de cariz sexual, nomeadamente através da alteração da natureza deste tipo de crime para público, aumentando a pena que lhe está associada, autonomizando o tipo de crime, entre outras coisas.  
**51.** Reforçar a protecção dos idosos que sejam vítimas de crimes e apostar na prevenção através de acções de sensibilização junto dos idosos e aumento do número de resposta de apoio a esta população.  
**52.** Rever a Lei da Organização do Sistema Judiciário no sentido de abrir novos tribunais, assim assegurando a justiça de proximidade em todo o território nacional.  
**53.** Reforço dos meios do DCIAP para combate à criminalidade organizada.  
**54.** Implementar sistemas de controle da produtividade dos tribunais.  
**55.** Promover uma maior celeridade no âmbito dos designados "megaprocessos", nomeadamente através da limitação das possibilidades de requerer instrução, bem como da alteração do carácter suspensivo de alguns recursos e no final de cada "megaprocesso" proceder a uma análise das razões do tempo que demorou do princípio ao fim.  
**56.** Rever a Lei do Acesso ao Direito e aos Tribunais, ampliando a sua abrangência e, assim, assegurando maior número de beneficiários.  
**57.** Rever o Regulamento das Custas Processuais, designadamente as tabelas anexas, no sentido tornar a justiça mais acessível.  
**58.** Promover uma Campanha Nacional de combate à pirataria de publicações jornalísticas, dando a conhecer os impactos negativos dessa prática para o pluralismo e democracia, bem como a circunstância de se tratar de acto criminoso já previsto e punido por lei, adoptanto ainda outras medidas necessárias com vista à protecção dos direitos de autor.

---

[Documento 2] Partido: CHEGA | Tópicos: justica, financas
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > I CAPÍTULO LIMPAR PORTUGAL DA CORRUPÇÃO. COMO? > PROPOSTAS
### PROPOSTAS  
**1.** Reforçar a fiscalização e controlo, nomeadamente através:  
- Do reforço dos poderes e dos meios da Direcção Central de Investigação da Corrupção e Criminalidade Económica e Financeira, bem como dos poderes de Fiscalização do Tribunal de Contas e dos outros organismos de controlo (inspecções gerais e outras);  
- Da otimização da capacidade de cooperação entre as inspecções administrativas sectoriais, dos órgãos de polícia criminal especializados nesta área e das entidades internacionais de combate à criminalidade económica;  
- Reforço de meios humanos nomeadamente do Núcleo de Assessoria Técnica da Procuradoria-Geral da República, da Unidade de Perícia Financeira e Contabilística e da Unidade Nacional de Combate ao Cibercrime e à Criminalidade Tecnológica da Polícia Judiciária;  
- Reforço da formação de magistrados e demais intervenientes na investigação criminal deste tipo de crimes.  
**2.** Criar o crime de enriquecimento ilícito relativo ao período de exercício do cargo pelos titulares de cargos políticos e titulares de altos cargos públicos.  
**3.** Ampliar a incriminação de recebimentos indevidos, obtenção irregular de benefícios, todo o tipo de tráfico de influências, aceitação e oferta de vantagens, com a garantia de apreensão imediata de vantagens obtidas.  
**4.** Reformar o sistema de apreensão, confisco e devolução ao Estado (e aos eventuais lesados) do património e produto do crime económico-financeiro, garantindo, tal como ocorre nos sistemas anglo-saxónicos uma eficaz apreensão de bens mesmo antes da condenação final e a celeridade conexa do processo em referência.  
**5.** Promover um sistema eficaz de reintrodução dos valores apreendidos na economia e no investimento público, potenciando a optimização desses recursos enquanto motores de desenvolvimento e coesão territorial.  
**6.** Implementar medidas de protecção do denunciante e de premiar os arguidos que colaborem, forneçam elementos de investigação e que revelem arrependimento colaborante.  
**7.** Aumentar as penas, garantir penas mínimas que não possibilitem a suspensão da pena e aumentar o prazo de prescrição de alguns crimes, como o de tráfico de influência, recebimento ou oferta indevidos de vantagem, corrupção e participação económica em negócio.  
**8.** Criar sanções acessórias como a proibição de exercício de funções públicas por 10 anos, incapacidade activa para desempenho de cargos públicos ou sujeição a sufrágio.  
**9.** Limitar a possibilidade de titulares de cargos políticos celebrarem negócios com familiares.  
**10.** Proibir os titulares de cargos políticos e altos cargos públicos exercerem quaisquer cargos ou funções, remuneradas ou não remuneradas, em quaisquer instituições tuteladas pelo Governo, sem que previamente seja cumprido um período de nojo de 8 anos.  
**11.** Assegurar que os titulares e ex-titulares de cargos políticos e altos cargos públicos estão vitaliciamente impedidos de exercer quaisquer cargos ou funções, remunerados ou não remunerados, em quaisquer empresas com as quais, enquanto titulares de pastas governamentais, tenham estabelecido qualquer negociação em nome de entidades públicas.  
**12.** Alterar o Código de Conduta dos Deputados, no sentido de inserir formação sobre questões éticas, associadas ao exercício do mandato.  
**13.** Regulamentar as regras de transparência aplicáveis a entidades privadas que realizam representação legítima de Interesses ("Lobbying") junto de entidades públicas, criando um registo de transparência da representação de interesses junto da Assembleia da República, código de conduta e sanções para o incumprimento.  
**14.** Tornar obrigatória a publicação anual da lista das entidades públicas reclassificadas, fundações, observatórios, associações, IPSS, institutos públicos, semipúblicos e privados a quem foram atribuídos subsídios no ano anterior, detalhando os montantes envolvidos, o motivo de sustentação do subsídio atribuído e o fim para o qual se destina.  
**15.** Criar regras de transparência adicionais para fundações e observatórios, devendo estes tornar públicas as suas contas e quaisquer donativos acima de um valor a determinar, bem como todos os financiamentos públicos de que beneficiem, devendo o Estado proceder a uma avaliação qualitativa da sua execução e abster-se de financiar qualquer entidade desta natureza que não publique as suas contas, que não seja transparente ou não cumpra fins de comprovada utilidade pública.  
**16.** Promover uma auditoria financeira externa às contas do Governo, relativa às últimas duas legislaturas; assim como deve ser assegurada uma auditoria financeira externa às contas dos Partidos Políticos, relativa aos últimos 3 anos e, por fim, deve ser criado um mecanismo de auditoria permanente dos serviços do Estado.  
**17.** Acrescentar ao relatório já previsto na Estratégia Nacional de Combate à Corrupção que devem constar as medidas efectivamente implementadas, recursos humanos contratados, identificação dos investimentos feitos e apreciação da sua eficácia e estimativa de perdas causadas por este tipo de criminalidade.

---

[Documento 3] Partido: CHEGA | Tópicos: imigracao, justica
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > VII CAPÍTULO GARANTIR FRONTEIRAS CONTROLADAS. COMO? > PROPOSTAS
### PROPOSTAS  
**166.** Reverter a extinção do Serviço de Estrangeiros e Fronteiras e, consequentemente, repor a sua estrutura orgânica, as suas atribuições e o seu estatuto jurídico e operacional.  
**167.** Estabelecer quotas anuais para a imigração assentes nas qualificações, nas reais necessidades do mercado de trabalho do país e nas mais-valias que os imigrantes possam trazer a Portugal.  
**168.** Revogar o acordo de mobilidade entre os países da Comunidade dos Países de Língua Portuguesa (CPLP) e, consequentemente, acabar com a autorização de residência automática aos imigrantes da CPLP, respeitando assim as normas europeias nesta matéria.  
**169.** Alterar a Lei da Nacionalidade no sentido de a atribuir apenas a quem conhecer a língua e a cultura portuguesas.  
**170.** Rever as condições de repatriamento no sentido de quem incumprir a nossa lei penal ser reconduzido ao país de origem.  
**171.** Rever as condições de repatriamento no sentido de reconduzir ao país de origem quem não demonstrar capacidade de auto-subsistência, num período compreendido entre 6 a 12 meses.  
**172.** Criar o Programa Bom Regresso, um programa de apoio a todas as pessoas que queiram regressar ao seu país de origem e não consigam fazê-lo por falta de meios.  
**173.** Publicar anualmente relatórios com indicação do número de imigrantes em Portugal, situação face ao emprego, apoios recebidos, criminalidade, riqueza gerada para o país, nascimentos, distribuição territorial, etc.  
**174.** Facilitar a integração da população imigrante através de um acompanhamento mais aproximado das pessoas que chegam ao nosso país, verificando as suas condições para se sustentarem, de habitabilidade, empregabilidade, formação, etc., assim como disponibilizar o ensino de português língua não materna e de História e Cultura de Portugal.  
**175.** Criar o crime de residência ilegal em solo português e impedir a permanência de imigrantes ilegais em território nacional, assegurando que quem for encontrado nessas circunstâncias fica impedido de regressar a Portugal e legalizar a sua situação nos cinco anos seguintes.  
**176.** Regulamentar o acesso a apoios sociais, definindo como período mínimo de 5 anos a contribuição para o Estado Português antes de poder usufruir de qualquer tipo de benefício .  
**177.** Retirar a nacionalidade portuguesa aos cidadãos binacionais que cometam crimes violentos tais como terrorismo, homicídio, ofensas corporais graves, violação, abuso sexual de menores, violência doméstica ou lesões físicas graves resultantes de roubo.  
**178.** Aumentar as penas para o tráfico de seres humanos e auxilío à imigração ilegal, bem como reforçar os meios de investigação deste tipo de crimes.  
**179.** Garantir a permanência dos requerentes de asilo nos Centros de Acolhimento Temporários, enquanto os pedidos aguardam deferimento.  
**180.** Impedir o avanço do fundamentalismo islâmico e garantir que as novas comunidades respeitam a lei da liberdade religiosa, os direitos humanos, nomeadamente os direitos das mulheres e crianças.  
**<sup>4</sup>** Megaoperação: PJ trava rede que faz circular milhares de migrantes ilegais na Europa graças a uma lei portuguesa  
**<sup>3</sup>** Crime organizado: relatório da secreta aponta para 1000 elementos do PCC a atuar em Portugal

---

[Documento 4] Partido: CHEGA | Tópicos: governacao, justica
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > XXV PARTE REFORMAR A CONSTITUIÇÃO E LIMPÁ-LA DA CARGA IDEOLÓGICA. COMO?
## XXV PARTE REFORMAR A CONSTITUIÇÃO E LIMPÁ-LA DA CARGA IDEOLÓGICA. COMO?  
**A**actual Constituição da República Portuguesa foi redigida num período de radicalismo revolucio-nário e, apesar de constituir um marco histórico, político e jurídico, importa agora actualizá-la. Desde logo é urgente eliminar os resquícios dos combates ideológicos dos anos 60 e 70. Manter referências ao período 'fascista' ou determinar o 'caminho para o socialismo' não é adequado a um texto constitucional que se mantém em vigor e que é a pedra angular do ordenamento jurídico português.  
A par de uma limpeza ideológica necessária, o CHEGA pretende assegurar e ampliar os direitos dos cidadãos nas diversas áreas da justiça criminal, administrativa e mesmo fiscal, mas também garantir que os direitos fundamentais não obstaculizam as mudanças que sejam desejadas e aprovadas pelos cidadãos, como é o caso da aplicação de penas de carácter perpétuo, de penas que digam respeito a tratamentos químicos que se considerem necessários para a prevenção de crimes de natureza sexual, ou excepções ao princípio da presunção de inocência.  
No que diz respeito ao ensino, as alterações pretendem assegurar que não existe margem para dúvidas naquele que deve ser o papel da Família e o do Estado, devendo o ensino ser livre de ideologias. Já na saúde, não é demais recordar que este direito vem consagrado no nosso texto constitucional, assegurando que todos devem ter acesso a cuidados de saúde. Acontece que, por mais importante que seja aquele princípio, ele não está ainda devidamente materializado. Como todos sabemos, vezes demais os utentes do Serviço Nacional de Saúde demoram semanas, meses ou anos a ter uma consulta de medicina geral e familiar e ou de especialidade. O CHEGA entende que, para o utente que procura cuidados, não interessa se o prestador é público, privado ou social. A única forma de proporcionar cuidados de saúde atempados aos cidadãos, de acordo com aquilo a que o próprio Estado diz terem direito, é referenciá-los para a primeira resposta disponível, seja ela no sector privado ou no sector social.  
Por outro lado, o modelo económico constitucional português continua a ser demasiado estatizante. Enraizado na lógica pós-revolucionária portuguesa, não só as instituições, como as grandes opções do plano de desenvolvimento, ficaram amplamente dependentes do Estado, dos seus recursos e orientação ideológica. Da saúde ao ensino, áreas já mencionadas enquanto direitos fundamentais constitucionalmente reconhecidos, passando pela política de coesão e infra-estruturas, a lógica dominante foi sempre um domínio quase absoluto do Estado e dos seus agentes. Esta política levou a várias consequências desastrosas, quer do ponto de vista cultural, quer económico, quer mesmo civilizacional. Criou-se uma cultura de gigantismo estatal que ainda hoje prevalece nas áreas sociais fundamentais. Desenharam-se e aplicaram-se modelos altamente dispendiosos para os contribuintes e, maioritariamente, com pouca eficácia comparada no serviço ao cidadão.  
No âmbito das instituições políticas, o CHEGA apresenta várias propostas que afectam a a sua dimensão ou mesmo a sua composição, mas pretende especialmente afastar qualquer influência política nos tribunais assim como uma excessiva influência sobre as instituições de controlo, mesmo aquelas que têm como missão fiscalizar o próprio Governo. A Constituição deve servir de salvaguarda inquebrável ao equilíbrio de poderes, vedando qualquer intromissão abusiva ou a criação de 'zonas cinzentas' em que os diversos poderes políticos aproveitam para operar de forma arbitrária contra os direitos dos cidadãos ou em proveito próprio. Infelizmente, na legislatura que terminou, o processo de revisão constitucional espoletado pelo CHEGA foi discutido na especialidade, foram recebidos vários pareceres e feitas audições de diversos especialistas, mas acabou por caducar devido à demissão do Governo. No entanto, este continua a ser da maior importância e será uma prioridade para o CHEGA na nova legislatura.

</details>

## item-05

**Question:** O que dizem o Bloco de Esquerda e o LIVRE sobre a semana de quatro dias?

**Answer:**

• **Bloco de Esquerda**: defende a implementação da **semana de quatro dias** como uma medida para promover o equilíbrio entre a vida profissional e pessoal e para a redução da jornada de trabalho sem redução salarial. O partido propõe que esta transição seja acompanhada por uma redistribuição do tempo de trabalho para combater o desemprego e melhorar a qualidade de vida dos trabalhadores.

• **LIVRE**: defende a redução do tempo de trabalho através da implementação da **semana de quatro dias** (ou de uma jornada semanal reduzida), mantendo o nível de rendimentos. O partido argumenta que esta medida é fundamental para a transição ecológica, ao reduzir o consumo e as emissões, e para a melhoria da saúde mental e do bem-estar dos cidadãos.

**Reference answer:**

Ambos são favoráveis. O Bloco de Esquerda propõe consagrar na lei a opção (também por iniciativa do trabalhador) pela semana de 4 dias, sem perda de rendimento e ligada à redução do horário, e um programa para a estabelecer, com 32 horas semanais a partir de 2028 nas empresas aderentes, invocando o teste em 41 empresas avaliado positivamente por 95% delas. O LIVRE apresenta a semana de 4 dias como medida sua e diz que os resultados intermédios são favoráveis, e propõe continuar a experiência no setor privado e na administração pública, incluí-la na contratação coletiva e nos acordos de empresa e avançar para uma experiência a nível nacional, como em Valência.

**faithfulness** — Is the claim supported by the CONTEXT?

- [ ] O Bloco de Esquerda defende a implementação da semana de quatro dias.
- [ ] O Bloco de Esquerda apresenta a semana de quatro dias como uma medida para promover o equilíbrio entre a vida profissional e pessoal.
- [ ] O Bloco de Esquerda apresenta a semana de quatro dias como uma medida para a redução da jornada de trabalho sem redução salarial.
- [ ] O Bloco de Esquerda propõe que a transição para a semana de quatro dias seja acompanhada por uma redistribuição do tempo de trabalho.
- [ ] O Bloco de Esquerda propõe a redistribuição do tempo de trabalho para combater o desemprego.
- [ ] O Bloco de Esquerda propõe a redistribuição do tempo de trabalho para melhorar a qualidade de vida dos trabalhadores.
- [ ] O LIVRE defende a redução do tempo de trabalho através da implementação da semana de quatro dias.
- [ ] O LIVRE defende a redução do tempo de trabalho através da implementação de uma jornada semanal reduzida.
- [ ] O LIVRE propõe a manutenção do nível de rendimentos na implementação da semana de quatro dias.
- [ ] O LIVRE argumenta que a semana de quatro dias é fundamental para a transição ecológica.
- [ ] O LIVRE argumenta que a semana de quatro dias reduz o consumo.
- [ ] O LIVRE argumenta que a semana de quatro dias reduz as emissões.
- [ ] O LIVRE argumenta que a semana de quatro dias melhora a saúde mental dos cidadãos.
- [ ] O LIVRE argumenta que a semana de quatro dias melhora o bem-estar dos cidadãos.

**correctness_recall** — Does the ANSWER state this reference claim?

- [ ] O Bloco de Esquerda é favorável à semana de quatro dias.
- [ ] O LIVRE é favorável à semana de quatro dias.
- [ ] O Bloco de Esquerda propõe consagrar na lei a opção pela semana de 4 dias.
- [ ] O Bloco de Esquerda propõe que a opção pela semana de 4 dias possa ser feita por iniciativa do trabalhador.
- [ ] O Bloco de Esquerda propõe que a semana de 4 dias seja implementada sem perda de rendimento.
- [ ] O Bloco de Esquerda propõe que a semana de 4 dias esteja ligada à redução do horário.
- [ ] O Bloco de Esquerda propõe um programa para estabelecer a semana de 4 dias.
- [ ] O Bloco de Esquerda propõe 32 horas semanais a partir de 2028 nas empresas aderentes.
- [ ] O Bloco de Esquerda invoca um teste em 41 empresas para justificar a semana de 4 dias.
- [ ] O Bloco de Esquerda afirma que 95% das 41 empresas avaliadas no teste avaliaram-no positivamente.
- [ ] O LIVRE apresenta a semana de 4 dias como medida sua.
- [ ] O LIVRE afirma que os resultados intermédios da semana de 4 dias são favoráveis.
- [ ] O LIVRE propõe continuar a experiência da semana de 4 dias no setor privado.
- [ ] O LIVRE propõe continuar a experiência da semana de 4 dias na administração pública.
- [ ] O LIVRE propõe incluir a semana de 4 dias na contratação coletiva.
- [ ] O LIVRE propõe incluir a semana de 4 dias nos acordos de empresa.
- [ ] O LIVRE propõe avançar para uma experiência da semana de 4 dias a nível nacional.
- [ ] O LIVRE cita o exemplo de Valência para a experiência nacional da semana de 4 dias.

relevance: 

<details><summary>Context the generator read</summary>

## Bloco de Esquerda
[Documento 1]
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 3 Trabalho, Salário e Pensões > 3.2 Precariedade e direitos coletivos > Tempo para viver: semana de quatro dias, 35 horas, desconexão
#### Tempo para viver: semana de quatro dias, 35 horas, desconexão  
Foi há quase três décadas que se fez a última redução do período normal de trabalho no setor privado, com a aprovação, em 1996, da lei das 40 horas. Desde então, não houve evolução legislativa sobre a duração do trabalho, a não ser as múltiplas formas de flexibilização de horários, adaptabilidades e bancos de horas.  
O balanço da experiência portuguesa e internacional relativa à redução do horário de trabalho dá-nos indicações sobre estes processos. Em Portugal, a redução para as 40 horas permitiu a criação de 5% de emprego líquido no primeiro ano e 3% no segundo. Em França, a aplicação das leis Aubry (a primeira de 1998 e a segunda de 2000) que reduziram o horário de trabalho paras as 35 horas, contribuiu para a criação de 350 mil empregos entre 1997-2001, acompanhada de uma aceleração dos ganhos de produtividade e do relançamento do diálogo social. Se tomássemos como referência a experiência francesa de 1998, a aplicação das 35 horas no setor privado em Portugal poderia criar mais de 200 mil postos de trabalho.  
Por outro lado, existe um movimento internacional pela semana de quatro dias, com redução do horário de trabalho semanal e sem perda de salário mensal. Em Portugal, esta forma de organização do trabalho já foi testada em 41 empresas, com bons resultados, abrangendo mais de 1000 trabalhadores. Em média, a semana de quatro dias envolveu a redução das horas de trabalho semanais em 13,7% (para 34 horas, reportado pelas empresas), na maior parte dos casos (cerca de 60%) através de mais um dia livre por semana. Em 20% das empresas, o dia livre é a sexta-feira, nos outros casos é variável. 95% das empresas avaliam positivamente o teste até agora e os inquéritos feitos aos trabalhadores indicam diminuição da ansiedade, fadiga, problemas de sono e estados depressivos. Os níveis de exaustão pelo trabalho reduziram-se em 19% e cerca de dois terços dos trabalhadores passaram mais tempo com a família após o início da redução horária.  
A limitação da jornada de trabalho faz-se também combatendo os abusos nas horas extra (muitas delas não pagas), o abuso das figuras legais da "isenção de horário" e da "laboração contínua" e através de sinais fortes, como o que foi dado com a consagração do dever patronal de desconexão, que o Bloco vinha defendendo desde 2017 e que ficou consagrada no Código do Trabalho no final de 2021.  
A esquerda deve investir decididamente num programa de redução progressiva do horário de trabalho e num programa de estabelecimento da semana de quatro dias de trabalho, sem perda salarial e com progressiva redução do tempo de trabalho. Isso deve ser feito expandindo a adesão voluntária das empresas, mas também por via normativa, com uma nova lei da redução do horário de trabalho imperativa para todas as empresas: em 2025, o período normal de trabalho seria reduzido para as 38 horas semanais; em 2026, para as 36 horas semanais; em 2027, seria reduzido para as 34 horas semanais. No caso das empresas que adiram à semana de quatro dias, devem ser fixados, a partir de 2028, as 32 horas semanais.  
A redução do horário normal de trabalho e a semana de quatro dias são processos distintos, que respeitam a dimensões distintas da gestão e organização do tempo de trabalho. Num caso, trata-se de fixar o período normal de trabalho; no outro, de uma  
prática de gestão e organização, que pode ter expressão na contratação coletiva e ser depois generalizada pela lei.

[Documento 2]
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 3 Trabalho, Salário e Pensões > 3.2 Precariedade e direitos coletivos > As propostas do Bloco: > Relançar a contratação coletiva e reduzir o horário de trabalho
#### As propostas do Bloco:  
##### Relançar a contratação coletiva e reduzir o horário de trabalho  
- → Relançar as convenções coletivas e o sistema coletivo de relações laborais, nomeadamente com o fim da caducidade unilateral dos instrumentos de regulação coletiva de trabalho e a reposição do tratamento mais favorável ao trabalhador;
- → Redução progressiva do horário de trabalho, fixando por lei, nesta legislatura, o período normal de trabalho, no máximo, nas 35 horas;
- → Consagrar na lei a possibilidade de opção (também por iniciativa do trabalhador) pela semana de 4 dias, vinculada à redução do horário de trabalho semanal e sem perda de rendimento;
- → Combater a desregulação dos horários, limitando e regulando a utilização da figura da "isenção de horário" e da generalização da laboração contínua;
- → Realizar um livro verde sobre o tempo de trabalho, que faça o levantamento da extensão do uso da adaptabilidade e do banco de horas, do trabalho por turnos e noturno e sua incidência setorial;
- → Eliminar integralmente o corte no acréscimo remuneratório do trabalho suplementar, reduzido para metade em 2012 e apenas parcialmente reposto. Recuperação do descanso compensatório.

[Documento 3]
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 3 Trabalho, Salário e Pensões > 3.2 Precariedade e direitos coletivos > As propostas do Bloco: > Repor as férias, combater abusos nos despedimentos, direitos para os trabalhadores por turnos
##### Repor as férias, combater abusos nos despedimentos, direitos para os trabalhadores por turnos  
→ Devolver os três dias de férias retirados pela direita (regresso à norma dos 25 dias, sem depender de outro critério);  
- → Combater a facilitação dos despedimentos, com a reposição do valor das compensações por despedimento anterior à intervenção da troika (um mês por cada ano de trabalho prestado; em lugar dos atuais 14 dias) e impedindo despedimentos, exceto por justa causa, em empresas com resultados positivos no ano anterior;
- → Eliminar a norma que obriga os trabalhadores, para contestarem despedimentos ilícitos, a abdicarem da compensação a que têm direito;
- → Reconhecer mais direitos a quem trabalha por turnos, nomeadamente através de: i) consagração legal da obrigatoriedade de subsídio por turnos; ii) maior acompanhamento médico; iii) definição de pausas e tempos de descanso e fins de semana; iv) participação dos trabalhadores e das trabalhadoras na definição das escalas de turnos; v) redução dos tempos de trabalho; vi) majoração dos dias de férias; vii) direito à reforma antecipada em proporção do tempo que se trabalhou por turnos.

[Documento 4]
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 13 Uma Nova Política de Cuidados > 13.2 Mudança de paradigma > 13.2.2 Mais tempo remunerado para cuidar > Mais tempo para os filhos
##### Mais tempo para os filhos  
O Bloco de Esquerda propõe que, a par do direito a falta justificada e do subsídio para assistência a filho (já resultante do art.<sup>o</sup> 49.<sup>o</sup> do Código do Trabalho), seja criada uma nova licença, que garanta a todos os progenitores, de forma pessoal e intransmissível e insindicável, o direito a 5 dias por ano, remunerados, para a fruição e cuidado dos filhos até aos oito anos.

[Documento 5]
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 3 Trabalho, Salário e Pensões > 3.2 Precariedade e direitos coletivos
### 3.2 Precariedade e direitos coletivos  
Portugal continua a ser um país precário: quase um terço dos contratos de trabalho no privado são precários (31%), metade dos trabalhadores abaixo dos trinta anos não tem contrato permanente e centenas de milhares trabalham sem contrato (na informalidade absoluta ou com falsos recibos verdes). Os baixos salários condenam as pessoas a vidas no limiar da pobreza e os vínculos temporários impedem-nas de fazer projetos para o futuro.  
O governo PS, depois de resistir a avanços em matérias laborais, acabou o mandato de 2022 com a promessa de uma "Agenda do Trabalho Digno", que viria a concretizar-se numa reforma da legislação laboral já no contexto da maioria absoluta. Contendo medidas positivas pelas quais o Bloco se bateu, essa alteração legislativa ficou muito aquém do necessário e da expectativa.  
Desde logo, por aquilo que exclui. A opção da última alteração às leis do trabalho foi manter o quadro de desequilíbrio que vem do Código do  
Trabalho de 2003, da versão de 2009 e das alterações feitas na sequência da intervenção da troika em 2012 e 2013. Mantém-se, assim, a caducidade das convenções coletivas e a não recuperação integral do princípio do tratamento mais favorável ao trabalhador. A compensação por despedimento passou apenas para os 14 dias por ano de trabalho, muito longe dos 30 dias que vigoravam antes do brutal corte da direita em 2012 e 2013. Nada se altera em matérias fundamentais como o trabalho por turnos ou o período normal de trabalho.  
Não desistimos de uma transformação estrutural das relações de trabalho e da reversão do desequilíbrio que hoje é a marca da legislação laboral, que tem vindo a individualizar as relações de trabalho e a permitir a instalação da precariedade.  
**Abrangência dos instrumentos de regulamentação coletiva do trabalho publicados (novos ou revistos)**

[Documento 6]
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 3 Trabalho, Salário e Pensões > 3.2 Precariedade e direitos coletivos > As propostas do Bloco: > Combater a precariedade
##### Combater a precariedade  
- → Restringir a contratação a prazo apenas às situações de substituição temporária e de pico ou sazonalidade de atividade, eliminando as exceções legais que permitem a sucessão de contratos a termo;
- → Regularizar os falsos recibos verdes e outras situações irregulares, utilizando a Ação Especial de Reconhecimento do Contrato de Tra-  
balho (a "Lei contra a Precariedade"), com metas anuais ambiciosas para a Autoridade para as Condições do Trabalho, de modo a atingir dezenas de milhares de situações regularizadas até ao final da legislatura;  
- → Incluir um critério de exclusão de empresas com situações precárias irregulares em qualquer contrato com o Estado;
- → Limitar os fundamentos e a duração do trabalho temporário a um máximo de seis meses;
- → Revogação do alargamento do período experimental para jovens a procura do primeiro emprego e desempregados de longa duração, introduzido em 2019;
- → Combater o abuso no outsourcing, limitando legalmente a externalização de funções relativas ao objeto social central da empresa;
- → Eliminar o intermediário na presunção de laboralidade nas plataformas digitais, impedindo as grandes empresas de continuar a descartar as suas responsabilidades patronais;
- → Incentivar a criação de plataformas digitais públicas e cooperativas, designadamente na área dos transportes e das entregas;
- → Limitar a utilização abusiva de estágios apoiados pelo IEFP, com reforço da fiscalização relativa aos falsos estágios e a estágios sucessivos para ocupar funções permanentes nas empresas;
- → Atribuir à Autoridade para as Condições do Trabalho poderes para fiscalizar o cumprimento da legislação laboral por parte das autarquias;
- → Reconhecer e enquadrar no Código do Trabalho o trabalho doméstico assalariado e o trabalho profissional de apoio domiciliário, amas de creche familiar e ajudantes familiares, pondo fim à discriminação que a lei estabelece e garantindo a mesma proteção social dos trabalhadores por conta de outrem.

## LIVRE
[Documento 7]
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > Trabalho, Rendimento, Tempo e Proteção Social > Por isso defendemos:
### Por isso defendemos:  
1. **Tirar Portugal da armadilha dos salários baixos, aumentando os rendimentos**: através de um compromisso de subida do salário mínimo nacional ao longo da legislatura até aos 1150 euros, em 2028, permitindo assim reforçar o valor do trabalho enquanto componente produtiva fundamental para a economia, e definindo metas para o rácio do SMN em relação ao PIB per capita ou ao salário médio; estabelecendo uma estratégia de concertação nacional para a valorização salarial, nos vários níveis da escala de rendimentos, com particular ênfase nos salários médios e para os rendimentos do trabalho qualificado, através, também, de uma indexação à inflação e a métricas de produtividade. É também urgente regular as diferenças salariais dentro da mesma entidade, estabelecendo um limite máximo para o rácio entre o salário mais baixo e o salário mais alto em cada empresa, organização ou ramo de atividade.  
2. **Promover uma maior e mais justa distribuição da riqueza**, através de uma revisão das taxas e escalões de IRS, da atualização do valor de referência do mínimo de existência e da dedução específica, garantindo que não há um agravamento fiscal indireto pelo facto de a inflação não ser incorporada nos limites dos escalões e deduções das famílias. Aumentar a progressividade do IRS e a capacidade redistributiva e de redução das desigualdades deste imposto. Rever a taxa adicional de solidariedade, e os limites a que se aplica, aumentando o contributo dos que têm rendimentos mais elevados e milionários, de forma a permitir baixar a contribuição dos rendimentos médios, garantindo uma maior justiça fiscal.  
3. **Incentivar a compensação adicional dos trabalhadores pelas empresas que geram lucros** não reinvestidos, majorando a dedução em sede de IRC relativa às gratificações de balanço e isentando de IRS os montantes atribuídos aos trabalhadores a título de participação nos lucros das empresas, até ao valor de uma remuneração média mensal e com o limite de 5 vezes a RMMG. Estes rendimentos não estão sujeitos a englobamento para determinação da taxa aplicável aos restantes rendimentos.  
4. **Promover a simplificação fiscal** através da revisão de regulamentos, limites e excepções, bem como das obrigações declarativas perante a Autoridade Tributária, nomeadamente através de uma maior integração das informações prestadas pelos contribuintes.  
5. **Combater a precariedade e o abuso pelas entidades empregadoras:**  
- ao reforçar a capacidade da Autoridade para as Condições do Trabalho, com recursos técnicos, legais e humanos, para fiscalizar as condições laborais nos setores público e privado, assim como para fiscalizar a efetividade do tempo prestado de trabalho, prevenindo abusos sobre trabalhadores decorrente do seu registo por plataformas ou meios digitais;
- erradicar os estágios não remunerados ou pagos abaixo do salário mínimo, os falsos recibos verdes, os falsos estágios e o falso trabalho independente;
- regular o recurso abusivo ao trabalho temporário, restringir os contratos a prazo a funções comprovadamente temporárias e ao trabalho suplementar;
- facilitar a trabalhadores o acesso à informação sobre o assédio moral em contexto de trabalho por forma a evitar e punir comportamentos inapropriados;
- regular os anúncios de emprego para garantir um mercado de trabalho mais transparente e com menos fricções e fraudes, nomeadamente obrigando os anúncios de emprego a apresentar uma remuneração mínima associada ao cargo.  
6. **Aumentar o tempo disponível para todas as pessoas:**  
- pela continuação da experiência da semana de 4 dias de trabalho no setor privado e na administração pública, promovendo a inclusão da semana de 4 dias na contratação coletiva e nos acordos de empresa, trabalhando para uma experiência a nível nacional de um período de semanas de 4 dias - à semelhança do que fez a cidade de Valência em Espanha;
- atingir 30h semanais e 30 dias de férias anuais até 2030, através da implementação imediata das 35 horas semanais de trabalho e dos 25 dias de férias e planeando progressivamente a redução do tempo de trabalho e aumentando os dias de férias;
- pelo não aumento da idade mínima de reforma, com planeamento para a sua redução (diminuindo o tempo de resposta ao pedido de reforma);
- permitindo a redução do horário de trabalho em função da idade do trabalhador sem perda de rendimento em vez da reforma total;
- alargando o direito a férias pagas para estagiários e estagiárias, sendo o cálculo do número de dias de férias pagas proporcional à duração do estágio.  
7. **Reforçar o poder das e dos trabalhadores:**  
- promover novas convenções coletivas de trabalho, alargando o leque de matérias a negociar, e acabar com o regime de caducidade dos instrumentos de regulamentação coletiva de trabalho de forma a diminuir o número de contratos individuais de trabalho;
- garantir uma efetiva representatividade dos trabalhadores nos processos de decisão por alteração do regime das Sociedades Comerciais, de forma a que todas as empresas maiores que uma Pequena ou Média Empresa (PME) tenham obrigatoriamente representantes dos trabalhadores nos seus órgãos sociais executivos;
- ao fomentar empresas partilhadas e cooperativas;
- criando uma Lei que promova e defina a autogestão das empresas, tal como previsto no Artigo 61º da Constituição.  
8. **Proteger o trabalho independente**, ao:  
- estabelecer uma Retribuição Horária Mínima Garantida;
- criar um novo estatuto de proteção do trabalho independente pela Segurança Social;
- ajustar a tabela de retenção para trabalhadores independentes;
- aumentar o valor a partir do qual deixam de estar sujeitos à isenção de IVA e retenção na fonte;
- reforçar a capacidade de negociação coletiva dos trabalhadores independentes que prestem serviços ao mesmo fornecedor.  
9. **Apoiar o microempreendedorismo**, criando hubs criativos que possam dotar o microempreendedor de espaço de trabalho a baixo custo, partilha de recursos, como eletricidade e aquecimento, e/ou serviços de prototipagem (como por exemplo impressão 3D). Criando um regime de microempreendedorismo de contabilidade e fiscal mais leve, que permite ao microempreendedor aliviar custos financeiros.

[Documento 8]
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > Trabalho, Rendimento, Tempo e Proteção Social
## Trabalho, Rendimento, Tempo e Proteção Social  
A luta pela proteção laboral e condições de vida dignas permitiram conquistas fundamentais no século XX, como a regulação do horário de trabalho e salário mínimo, reconhecimento do direito ao descanso semanal e gozo de período de férias, proteção financeira em caso de desemprego, parentalidade, doença ou incapacidade, invalidez, reforma ou velhice, ou a garantia de acesso a um patamar mínimo de segurança económica por via do rendimento social de inserção. No entanto, estas conquistas continuam a não ser acessíveis a todas as pessoas. A persistência de vínculos laborais precários, como os falsos recibos verdes, bolsas de investigação e contratos temporários, a realidade largamente ignorada das situações de trabalho sem vínculo, com destaque para o trabalho sazonal, ou o recurso abusivo a estágios profissionais e outras medidas de apoio à empregabilidade para colmatar necessidades de trabalho efetivas e continuadas, constituem claras violações destes direitos. Acresce que estas formas de trabalho precário afetam particularmente imigrantes, minorias étnico-raciais, mulheres, pessoas com deficiência, pessoas LGBTQIA+, trabalhadores com menos qualificações e jovens. A estas juntam-se outras barreiras, como as dificuldades de acesso ao mercado de trabalho, oportunidades desiguais de progressão profissional, desigualdades de remuneração por trabalho equivalente ou, ainda, a realidade de quem escolhe ou se vê forçado a abandonar o mercado de trabalho formal para prestar cuidados a familiares, que se constituem como fatores de risco acrescido de pobreza ou exclusão social.  
Por outro lado, urge preparar, desde já, a resposta aos desafios do século XXI, com uma transição para um novo paradigma de trabalho, rendimento e proteção social, que permita responder a transformações em curso como o impacto da tecnologia e automação no mercado laboral, a necessidade de diversificação das fontes de financiamento da Segurança Social assegurando a sua sustentabilidade. De igual importância é a luta por uma vida digna que não gire em torno do trabalho, permitindo uma efetiva conciliação trabalho-família e o acesso a tempos de lazer e de descanso, à qual a semana de 4 dias de trabalho, medida do LIVRE com resultados intermédios favoráveis, procura responder. Mais tempo livre também permite às pessoas investir em atividades de reforço de competências pessoais e profissionais, sem as quais não é possível construir uma sociedade mais rica, qualificada e ajustada aos desafios do século XXI.  
Queremos, pois, superar o emprego como aspeto central das nossas vidas em detrimento do tempo livre e de outras formas de trabalho como o voluntário, familiar e comunitário.  
Por tudo isto, o LIVRE defende um pacto nacional para o trabalho, rendimento e proteção social que permita corrigir desigualdades no presente e construir as bases para uma sociedade de futuro que possibilite o acesso a uma proteção laboral e de rendimento que não deixe ninguém para trás, ao mesmo tempo que aposta no acesso a bens cada vez mais escassos e valiosos, como o tempo, a segurança e a estabilidade.

[Documento 9]
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > Trabalho, Rendimento, Tempo e Proteção Social > Por isso defendemos:
13. **Garantir justiça a ex-combatentes**,  
- garantindo que a sua pensão não seja inferior ao valor do ordenado mínimo nacional e assegurando um complemento vitalício de pensão;
- criando a Comissão Nacional de acompanhamento dos Antigos Combatentes, com orçamento e estrutura próprios, e que tenha como missão garantir o reconhecimento do país às pessoas que o serviram, através da resposta às suas necessidades específicas e das suas famílias e também através da preservação da sua memória e da sua história;
- melhorando a implementação do Estatuto do Antigo Combatente, nomeadamente tornando o Cartão de Antigo Combatente também num cartão virtual e garantindo uma melhor resposta às solicitações com o reforço dos meios para o Balcão Único de Defesa e com a efetivação do protocolo com a ANAFRE- Associação Nacional de Freguesias;
- providenciando os meios para que os processos de qualificação de ex-combatentes como Deficientes das Forças Armadas ou Pensionistas de Invalidez sejam mais céleres;
- retomando a comparticipação a 90% dos medicamentos para Antigos Combatentes;
- tornando mais simples e célere o acesso à Assistência na Doença aos Militares;
- reforçando o orçamento para a Rede Nacional de Apoio (RNA) aos militares e ex-militares portadores de perturbação psicológica crónica resultante da exposição a fatores traumáticos de stress durante a vida militar, que também presta apoio às famílias;
- garantindo o acompanhamento e apoio psicológico a ex-combatentes mesmo após a sua saída das Forças Armadas.  
14. **Criar um programa piloto com vista à implementação faseada de um Rendimento Básico Incondicional,** que contribua para uma melhor distribuição da riqueza nacional produzida e garanta um rendimento a todas as pessoas, independentemente da sua condição, dos pagamentos do Fundo de Desemprego ou de outros programas de apoio social. O valor global a considerar para o projeto-piloto deve ser de cerca de 30 milhões de euros e deve incluir pessoas beneficiárias de apoios sociais, que se devem manter, pessoas com rendimentos exclusivos do trabalho por conta de outrem e trabalhadores independentes, bem como pessoas desempregadas - numa amostra representativa da sociedade portuguesa. O programa piloto deve ter ainda um quadro temporal superior a dois anos e contemplar a sua monitorização e avaliação.  
15. **Estudar a criação de uma herança social**, um sistema de redistribuição de riqueza e rendimentos e um reforço inequívoco da justiça social financiado a partir da tributação das grandes fortunas e das grandes heranças, que atribui a cada criança nascida em Portugal um montante ao qual pode aceder na maioridade.  
16. **Rever, alargar e aumentar a dotação orçamental do Programa para a Conciliação**, com vista à promoção de alterações concretas de maior equilíbrio entre a vida familiar e laboral e verdadeira igualdade entre géneros. O Programa para a Conciliação deve promover o cumprimento da Norma Portuguesa 4552:2016 - Conciliação entre a vida profissional, familiar e pessoal. Tendo como objetivos principais:  
- promover a flexibilidade de horários e dos trabalhos do alargamento do teletrabalho, horários adaptados, horas limites para reuniões e reforço das licenças parentais, tendo em conta as necessidades pessoais e familiares das e dos trabalhadores;
- dotar a Autoridade para as Condições do Trabalho de meios para fiscalização do "direito a desligar" e do "dever do não-contacto", protegendo os trabalhadores da imposição de se manterem ligados às suas funções para além do horário de trabalho, para salvaguarda da sua saúde mental e vida familiar;
- promover o debate sobre o Programa da Conciliação entre a vida profissional, familiar e pessoal em sede de concertação social, incluindo as várias entidades na revisão do programa e na definição da metodologia de execução;
- promover a formação para a conciliação através de protocolos entre a Comissão para a Cidadania e a Igualdade de Género (CIG) e as entidades privadas e públicas. E, simultaneamente, criar benefícios fiscais para empresas que adotem medidas de conciliação.  
17. **Apoiar o teletrabalho e o trabalho remoto**, permitindo com isso retirar procura das grandes cidades tanto de espaços de habitação como de trabalho, retirar pressão dos transportes públicos e de tráfego automóvel, habitar e povoar zonas menos habitadas com população ativa e com poder de compra de forma a dinamizar a economia local e permitir que jovens em determinadas profissões não sejam forçados a "emigrar" à força para as grandes cidades, através de:  
- revisão legislativa para alargar o direito a trabalhadores com filhos ou dependentes até aos 12 anos (observando condições para a conjugação da parentalidade com o teletrabalho), trabalhadoras grávidas, trabalhadores com doença crónica ou com grau de incapacidade igual ou superior a 60% e trabalhadores-estudantes, com a aplicação da obrigatoriedade dos casos anteriores às microempresas;
- atribuição ao teletrabalho dos mesmos direitos do trabalho presencial, incluindo o subsídio de almoço e o apoio da Segurança e Saúde no Trabalho da entidade empregadora para verificação das condições do local de trabalho em casa, se requerido pelo trabalhador ou profissional de saúde da empresa.  
18. **Apoiar a parentalidade**, através:  
- do aumento progressivo da licença parental para 16 meses, assim como do período de tempo pelo nascimento de gémeos, atribuindo maiores incentivos para que seja repartida entre ambos os pais, com períodos mais longos de tempo conjunto (numa primeira fase passar já para 120 dias) e com um período mínimo obrigatório de gozo de licença por cada um dos pais;
- da possibilidade de atribuição de baixa comparticipada a 100% para trabalhadoras grávidas em casos em que a gravidez não seja de risco;
- da criação de um regime de proteção para grávidas ou pessoas em processo de adoção com contrato a termo certo;
- da redução do horário de trabalho para trabalhadores com filhos pequenos até 3 anos, independentemente de serem amamentados ou não e com incentivo para ser repartido entre os dois pais;
- do estabelecimento de um regime de apoio à parentalidade de trabalhadores precários tendencialmente equiparado ao de trabalhadores por conta de outrem;
- da expansão e aumento de vagas em creches e jardins de infância incorporados na rede pública escolar;
- do aumento para 100% da remuneração de referência do subsídio para assistência a filho com deficiência, doença crónica ou doença oncológica;
- proteger a parentalidade na investigação, permitindo o alargamento do financiamento e prazos de quaisquer projetos e/ou contratos de investigação em caso de suspensão por motivos de parentalidade de investigadores;

[Documento 10]
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > Desenvolvimento Ecológico, Cooperativo e Solidário > Por isso defendemos:
- fomentar a inovação e investimento empresarial com objetivos ecológicos, com impacto social significativo e de alto valor acrescentado.  
8. **Apoiar o desenvolvimento económico de base social**, criando na legislação portuguesa o conceito e reconhecimento de empresa social como aquela que tem como objetivo responder a um problema social e/ ou ambiental, com redistribuição de mais de 50% do lucro entre os funcionários, a comunidade e reinvestidos na empresa, fortalecendo o compromisso com a equidade e o desenvolvimento sustentável. Além disso, serão implementados programas de capacitação para promover modelos de negócios socialmente responsáveis, procurando posicionar o país como líder em inovação social e empresarial.  
9. **Criar uma estrutura pública de apoio e fomento à economia social e cooperativismo** que, dotada de orçamentação adequada e trabalhadores formados para esse âmbito, possa:  
- criar uma linha de crédito para a criação de novas cooperativas de cariz social, incluindo na forma de empréstimo com baixa taxa de juro ou na forma de capital social da cooperativa, cobrindo, até um montante a definir caso a caso, o financiamento inicial aportado pelos cooperantes;
- promover um ecossistema de atividade socioeconómica e formativa, geração de emprego e impacto social;
- criar laboratórios de intercooperação para construir cidades cooperativas;
- apoiar tecnicamente a criação de novas cooperativas.  
10. **Incentivar fiscalmente o investimento em cooperativas**, isentando até um determinado montante ou reduzindo a taxa de retenção na fonte na aquisição de títulos de capital ou nos empréstimos de cooperadores às cooperativas.  
11. **Promover a economia social e solidária e o setor cooperativo em Portugal**,  
- apoiando a formação, nomeadamente ao nível do ensino superior, na área da economia social e solidária;
- criando, em cooperação com a CASES (Cooperativa António Sérgio para a Economia Social), uma rede que inclua investigadores académicos e as instituições da economia social, promovendo o diálogo permanente e a troca de experiências e assegurando que o conhecimento académico e o conhecimento no terreno se influenciam mutuamente;
- promovendo a experimentação em Portugal de formas inovadoras de economia social e solidária através de cooperativas, nomeadamente em áreas tecnológicas;
- estabelecendo Parcerias Público-Cooperativas com os produtores locais, com prioridade aos do setor cooperativo e solidário, para a aquisição regular e de longo prazo de bens e serviços.
- criar condições na banca comercial que facilite o acesso coletivo a crédito por parte das cooperativas, enquanto não existe uma banca ética e solidária.  
12. **Na falta de uma Banca Ética e Solidária**, criar condições na banca comercial que facilitem o acesso coletivo a crédito por parte das cooperativas.  
13. **Diversificar os indicadores de desenvolvimento nacional**, passando a incluir indicadores de desenvolvimento sustentável, como o PIB Verde ou a Poupança Genuína, dando prioridade aos aspetos mais diretamente ligados ao ambiente, qualidade de vida, felicidade, saúde e bem-estar e reforçando o seu papel na informação do sistema estatístico nacional e na monitorização das políticas e da ação governativa.  
14. **Trazer o combate às alterações climáticas e a salvaguarda da biodiversidade para todas as negociações orçamentais**, setor a setor, incluindo a mitigação dos impactos sociais e económicos das medidas de descarbonização e de transição.  
15. **Realizar anualmente um debate parlamentar de alto nível sobre o Estado do Ambiente em Portugal.**  
16. **Focar os órgãos de governação na transição do modelo de desenvolvimento a longo prazo**:  
- criando um Gabinete para a Transição, com o propósito de estudar e promover as estratégias para a transição de modelo de desenvolvimento, que seja uma estrutura de consulta obrigatória do Governo, e que garanta a sua implementação gradual e solidária entre gerações e independente dos ciclos eleitorais e de visões de curto prazo;
- institucionalizando sessões plenárias regulares na Assembleia da República e Assembleias Municipais para debate e pareceres sobre o Estado do Desenvolvimento do País e sobre ação governativa no domínio das políticas de desenvolvimento;
- reforçando os meios humanos e técnicos de apoio à avaliação de políticas de desenvolvimento.  
17. **Apoiar o desenvolvimento social e económico do país através do Banco Português do Fomento,** que deverá ser um verdadeiro banco de desenvolvimento com presença descentralizada a nível territorial e que assegure articulação com a Caixa Geral de Depósitos que deve ser orientada para o financiamento das Pequenas e Médias Empresas em condições mais favoráveis que as oferecidas pela banca comercial. O Banco Português do Fomento deve também apoiar a criação de novos mercados, investindo em áreas de maior risco comercial ou com falhas de mercado, viabilizando e reduzindo o custo de inovações e novas soluções para investimento industrial da economia verde e digital.  
18. **Garantir que os benefícios fiscais são justos e têm impacto social**, através de uma revisão do sistema de benefícios fiscais, eliminando os que promovam práticas especulativas ou que resultem em incentivos perniciosos para a sociedade no seu todo.  
19. **Reduzir o horário de funcionamento dos estabelecimentos de venda ao público e de prestação de serviços** até às 22h, incluindo os localizados nos centros comerciais, e o seu encerramento aos domingos e feriados, através da alteração do regime dos horários de funcionamento dos estabelecimentos comerciais.

</details>

## item-06

**Question:** Em que ano foram repostas as 35 horas na Administração Pública?

**Answer:**

Não existem informações nos programas eleitorais de 2024 dos partidos mencionados (AD, BE, CHEGA, IL, LIVRE, PAN, PCP, PS) que indiquem o ano em que as 35 horas foram repostas na Administração Pública. Os programas focam-se em propostas futuras e não em registos históricos de implementação de horários de trabalho.

**Reference answer:**

Segundo o PCP, as 35 horas semanais na Administração Pública foram repostas em 2016, com a aprovação de uma proposta do PCP que repôs e fixou o período normal de trabalho nesse limite. Nenhum outro programa indica esta data.

**faithfulness** — Is the claim supported by the CONTEXT?

- [ ] Os programas eleitorais de 2024 dos partidos AD, BE, CHEGA, IL, LIVRE, PAN, PCP e PS não indicam o ano em que as 35 horas foram repostas na Administração Pública.
- [ ] Os programas eleitorais de 2024 dos partidos AD, BE, CHEGA, IL, LIVRE, PAN, PCP e PS focam-se em propostas futuras.
- [ ] Os programas eleitorais de 2024 dos partidos AD, BE, CHEGA, IL, LIVRE, PAN, PCP e PS não focam-se em registos históricos de implementação de horários de trabalho.

**correctness_recall** — Does the ANSWER state this reference claim?

- [ ] O PCP afirma que as 35 horas semanais na Administração Pública foram repostas em 2016.
- [ ] O PCP afirma que a reposição das 35 horas semanais na Administração Pública ocorreu com a aprovação de uma proposta do PCP.
- [ ] O PCP afirma que a proposta aprovada fixou o período normal de trabalho no limite de 35 horas semanais.
- [ ] Nenhum outro programa político indica o ano de 2016 como a data de reposição das 35 horas semanais na Administração Pública.

relevance: 

<details><summary>Context the generator read</summary>

[Documento 1] Partido: Bloco de Esquerda | Tópicos: trabalho, economia
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 3 Trabalho, Salário e Pensões > 3.2 Precariedade e direitos coletivos > Tempo para viver: semana de quatro dias, 35 horas, desconexão
#### Tempo para viver: semana de quatro dias, 35 horas, desconexão  
Foi há quase três décadas que se fez a última redução do período normal de trabalho no setor privado, com a aprovação, em 1996, da lei das 40 horas. Desde então, não houve evolução legislativa sobre a duração do trabalho, a não ser as múltiplas formas de flexibilização de horários, adaptabilidades e bancos de horas.  
O balanço da experiência portuguesa e internacional relativa à redução do horário de trabalho dá-nos indicações sobre estes processos. Em Portugal, a redução para as 40 horas permitiu a criação de 5% de emprego líquido no primeiro ano e 3% no segundo. Em França, a aplicação das leis Aubry (a primeira de 1998 e a segunda de 2000) que reduziram o horário de trabalho paras as 35 horas, contribuiu para a criação de 350 mil empregos entre 1997-2001, acompanhada de uma aceleração dos ganhos de produtividade e do relançamento do diálogo social. Se tomássemos como referência a experiência francesa de 1998, a aplicação das 35 horas no setor privado em Portugal poderia criar mais de 200 mil postos de trabalho.  
Por outro lado, existe um movimento internacional pela semana de quatro dias, com redução do horário de trabalho semanal e sem perda de salário mensal. Em Portugal, esta forma de organização do trabalho já foi testada em 41 empresas, com bons resultados, abrangendo mais de 1000 trabalhadores. Em média, a semana de quatro dias envolveu a redução das horas de trabalho semanais em 13,7% (para 34 horas, reportado pelas empresas), na maior parte dos casos (cerca de 60%) através de mais um dia livre por semana. Em 20% das empresas, o dia livre é a sexta-feira, nos outros casos é variável. 95% das empresas avaliam positivamente o teste até agora e os inquéritos feitos aos trabalhadores indicam diminuição da ansiedade, fadiga, problemas de sono e estados depressivos. Os níveis de exaustão pelo trabalho reduziram-se em 19% e cerca de dois terços dos trabalhadores passaram mais tempo com a família após o início da redução horária.  
A limitação da jornada de trabalho faz-se também combatendo os abusos nas horas extra (muitas delas não pagas), o abuso das figuras legais da "isenção de horário" e da "laboração contínua" e através de sinais fortes, como o que foi dado com a consagração do dever patronal de desconexão, que o Bloco vinha defendendo desde 2017 e que ficou consagrada no Código do Trabalho no final de 2021.  
A esquerda deve investir decididamente num programa de redução progressiva do horário de trabalho e num programa de estabelecimento da semana de quatro dias de trabalho, sem perda salarial e com progressiva redução do tempo de trabalho. Isso deve ser feito expandindo a adesão voluntária das empresas, mas também por via normativa, com uma nova lei da redução do horário de trabalho imperativa para todas as empresas: em 2025, o período normal de trabalho seria reduzido para as 38 horas semanais; em 2026, para as 36 horas semanais; em 2027, seria reduzido para as 34 horas semanais. No caso das empresas que adiram à semana de quatro dias, devem ser fixados, a partir de 2028, as 32 horas semanais.  
A redução do horário normal de trabalho e a semana de quatro dias são processos distintos, que respeitam a dimensões distintas da gestão e organização do tempo de trabalho. Num caso, trata-se de fixar o período normal de trabalho; no outro, de uma  
prática de gestão e organização, que pode ter expressão na contratação coletiva e ser depois generalizada pela lei.

---

[Documento 2] Partido: LIVRE | Tópicos: trabalho, seguranca_social
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > Trabalho, Rendimento, Tempo e Proteção Social > Por isso defendemos:
### Por isso defendemos:  
1. **Tirar Portugal da armadilha dos salários baixos, aumentando os rendimentos**: através de um compromisso de subida do salário mínimo nacional ao longo da legislatura até aos 1150 euros, em 2028, permitindo assim reforçar o valor do trabalho enquanto componente produtiva fundamental para a economia, e definindo metas para o rácio do SMN em relação ao PIB per capita ou ao salário médio; estabelecendo uma estratégia de concertação nacional para a valorização salarial, nos vários níveis da escala de rendimentos, com particular ênfase nos salários médios e para os rendimentos do trabalho qualificado, através, também, de uma indexação à inflação e a métricas de produtividade. É também urgente regular as diferenças salariais dentro da mesma entidade, estabelecendo um limite máximo para o rácio entre o salário mais baixo e o salário mais alto em cada empresa, organização ou ramo de atividade.  
2. **Promover uma maior e mais justa distribuição da riqueza**, através de uma revisão das taxas e escalões de IRS, da atualização do valor de referência do mínimo de existência e da dedução específica, garantindo que não há um agravamento fiscal indireto pelo facto de a inflação não ser incorporada nos limites dos escalões e deduções das famílias. Aumentar a progressividade do IRS e a capacidade redistributiva e de redução das desigualdades deste imposto. Rever a taxa adicional de solidariedade, e os limites a que se aplica, aumentando o contributo dos que têm rendimentos mais elevados e milionários, de forma a permitir baixar a contribuição dos rendimentos médios, garantindo uma maior justiça fiscal.  
3. **Incentivar a compensação adicional dos trabalhadores pelas empresas que geram lucros** não reinvestidos, majorando a dedução em sede de IRC relativa às gratificações de balanço e isentando de IRS os montantes atribuídos aos trabalhadores a título de participação nos lucros das empresas, até ao valor de uma remuneração média mensal e com o limite de 5 vezes a RMMG. Estes rendimentos não estão sujeitos a englobamento para determinação da taxa aplicável aos restantes rendimentos.  
4. **Promover a simplificação fiscal** através da revisão de regulamentos, limites e excepções, bem como das obrigações declarativas perante a Autoridade Tributária, nomeadamente através de uma maior integração das informações prestadas pelos contribuintes.  
5. **Combater a precariedade e o abuso pelas entidades empregadoras:**  
- ao reforçar a capacidade da Autoridade para as Condições do Trabalho, com recursos técnicos, legais e humanos, para fiscalizar as condições laborais nos setores público e privado, assim como para fiscalizar a efetividade do tempo prestado de trabalho, prevenindo abusos sobre trabalhadores decorrente do seu registo por plataformas ou meios digitais;
- erradicar os estágios não remunerados ou pagos abaixo do salário mínimo, os falsos recibos verdes, os falsos estágios e o falso trabalho independente;
- regular o recurso abusivo ao trabalho temporário, restringir os contratos a prazo a funções comprovadamente temporárias e ao trabalho suplementar;
- facilitar a trabalhadores o acesso à informação sobre o assédio moral em contexto de trabalho por forma a evitar e punir comportamentos inapropriados;
- regular os anúncios de emprego para garantir um mercado de trabalho mais transparente e com menos fricções e fraudes, nomeadamente obrigando os anúncios de emprego a apresentar uma remuneração mínima associada ao cargo.  
6. **Aumentar o tempo disponível para todas as pessoas:**  
- pela continuação da experiência da semana de 4 dias de trabalho no setor privado e na administração pública, promovendo a inclusão da semana de 4 dias na contratação coletiva e nos acordos de empresa, trabalhando para uma experiência a nível nacional de um período de semanas de 4 dias - à semelhança do que fez a cidade de Valência em Espanha;
- atingir 30h semanais e 30 dias de férias anuais até 2030, através da implementação imediata das 35 horas semanais de trabalho e dos 25 dias de férias e planeando progressivamente a redução do tempo de trabalho e aumentando os dias de férias;
- pelo não aumento da idade mínima de reforma, com planeamento para a sua redução (diminuindo o tempo de resposta ao pedido de reforma);
- permitindo a redução do horário de trabalho em função da idade do trabalhador sem perda de rendimento em vez da reforma total;
- alargando o direito a férias pagas para estagiários e estagiárias, sendo o cálculo do número de dias de férias pagas proporcional à duração do estágio.  
7. **Reforçar o poder das e dos trabalhadores:**  
- promover novas convenções coletivas de trabalho, alargando o leque de matérias a negociar, e acabar com o regime de caducidade dos instrumentos de regulamentação coletiva de trabalho de forma a diminuir o número de contratos individuais de trabalho;
- garantir uma efetiva representatividade dos trabalhadores nos processos de decisão por alteração do regime das Sociedades Comerciais, de forma a que todas as empresas maiores que uma Pequena ou Média Empresa (PME) tenham obrigatoriamente representantes dos trabalhadores nos seus órgãos sociais executivos;
- ao fomentar empresas partilhadas e cooperativas;
- criando uma Lei que promova e defina a autogestão das empresas, tal como previsto no Artigo 61º da Constituição.  
8. **Proteger o trabalho independente**, ao:  
- estabelecer uma Retribuição Horária Mínima Garantida;
- criar um novo estatuto de proteção do trabalho independente pela Segurança Social;
- ajustar a tabela de retenção para trabalhadores independentes;
- aumentar o valor a partir do qual deixam de estar sujeitos à isenção de IVA e retenção na fonte;
- reforçar a capacidade de negociação coletiva dos trabalhadores independentes que prestem serviços ao mesmo fornecedor.  
9. **Apoiar o microempreendedorismo**, criando hubs criativos que possam dotar o microempreendedor de espaço de trabalho a baixo custo, partilha de recursos, como eletricidade e aquecimento, e/ou serviços de prototipagem (como por exemplo impressão 3D). Criando um regime de microempreendedorismo de contabilidade e fiscal mais leve, que permite ao microempreendedor aliviar custos financeiros.

---

[Documento 3] Partido: Partido Comunista Português | Tópicos: trabalho
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 3 VALORIZAR OS TRABALHADORES PROMOVER O EMPREGO COM DIREITOS, O AUMENTO DOS SALÁRIOS E A MELHORIA DAS CONDIÇÕES DE VIDA E DE TRABALHO > 3.4 Reduzir o tempo de trabalho, combater a desregulação dos horários > Máximo de 35 horas semanais e 7 horas diárias e continuação da redução progressiva do horário de trabalho
##### Máximo de 35 horas semanais e 7 horas diárias e continuação da redução progressiva do horário de trabalho  
Os avanços nos domínios técnico e científico, e o aumento da produtividade social do trabalho daí decorrente, permitem que hoje se possa produzir mais, com melhor qualidade, maior eficácia e em menos tempo. Esses avanços devem também ser factor de progresso social por via da redução progressiva e contínua dos horários de trabalho.  
A redução imediata do tempo de trabalho para 35 horas semanais constitui-se ainda como elemento essencial da compatibilização da vida profissional com a vida pessoal e familiar, e tem grande impacto na criação de emprego.  
A redução do tempo de trabalho semanal para as 35 horas deve ser acompanhada da redução da jornada diária máxima para 7 horas, reduzindo a cada trabalhador 240 horas de trabalho em cada ano.  
Mas é possível ir mais longe e reduzir progressivamente a semana de trabalho, para menos de 35 horas, particularmente onde esse limite máximo já está em vigor. A semana de 4 dias não pode ser aplicada à custa de outros direitos ou remunerações.

---

[Documento 4] Partido: Pessoas-Animais-Natureza | Tópicos: trabalho, saude
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por uma economia do bem-estar que dê prioridade às pessoas e à sustentabilidade ambiental
- Desenvolver regulamentação própria com vista à instalação da Banca Ética e das Finanças Solidárias em Portugal;  
- Promover uma banca verde, que garanta a sustentabilidade dos ecossistemas, que aposte na transição energética, que objetive a concretização da neutralidade carbónica e que promova a proteção dos solos;  
- Criação de um Fundo de Transição Justa para a Agricultura e Pecuária;  
- Aumentar a fiscalização na aplicação dos fundos destinados à Proteção Civil, pugnando pela sua transparência;  
- Reformar o estatuto do dirigente desportivo em regime de voluntariado, por forma a fomentar a renovação geracional no dirigismo desportivo voluntário, estimular a formação destes agentes e assegurar a igualdade de género;  
- Repensar o modelo de financiamento do desporto nacional, procurando aumentar o nível de financiamento canalizado para o setor e mitigar a dependência das receitas de jogos sociais; e  
- Construir uma ferramenta para medição do bem- -estar e felicidade da população, com base em processos participativos, que permita aferir, em cada ano, o que é mais importante a nível nacional, distrital e concelhio.  
Para reforçar os direitos dos trabalhadores e assegurar mais tempo para viver e uma maior conciliação da vida profissional com a vida pessoal, o PAN irá:  
- Aumentar anualmente o Salário Mínimo Nacional incorporando integralmente a inflação do ano anterior, o crescimento económico e o aumento de produtividade do trabalho. A este aumento consentâneo com a sustentabilidade económica, será somado um valor anual de 10€. De acordo com o nosso cenário macroeconómico, em 2028 o SMN atingirá os 1100€;  
- Reforçar os incentivos para conversão de estágios em contratos sem termo;  
- Aumentar significativamente o valor das bolsas atribuídas através da medida "estágios profissionais" levada a cabo pelo IEFP para jovens altamente qualificados bem como os incentivos à sua contratação;  
- Reforçar o número de efetivos da Autoridade para as Condições de Trabalho, assegurando uma fiscalização e intervenção mais eficaz que impeça o recurso à contratação de trabalhadores/as com vínculo precário para o desempenho de funções permanentes, bem como o não cumprimento de promoção da igualdade remuneratória entre homens e mulheres por trabalho igual ou de igual valor;  
- Reforçar os direitos dos/das trabalhadores/as em regime de trabalho noturno e por turnos, nomeadamente, revendo os critérios de compensação e de descanso;  
- Garantir a remuneração a 100% do subsídio de doença (baixa médica) aos/às trabalhadores/as cuja doença acarrete circunstâncias económicas particularmente gravosas, designadamente pelos elevados custos com tratamentos e/ou medicação;  
- Avaliar os resultados da Lei n.º 73/2017, de 16 de agosto, que reforçou o quadro legislativo para a prevenção da prática de assédio e, caso se mostre necessário, produzir alterações legislativas neste âmbito;  
- Alterar os programas existentes, a nível das medidas formativas e educativas, de modo a reduzir os riscos de discriminação no acesso ao mercado de trabalho e a facilitar a empregabilidade nas profissões para as quais as pessoas possuem competências e qualificações, nomeadamente:  
- Implementar ações de sensibilização, formação e capacitação na temática da discriminação junto dos/das empregadores/as;  
- Rever o sistema de quotas de emprego para pessoas com deficiência;  
- Adequar os programas e as medidas que se destinam a melhorar as competências dos/das trabalhadores/as estrangeiros/as;  
- Promover medidas que visem eliminar e/ou atenuar os obstáculos que dificultam a inserção de pessoas provenientes de países terceiros no mercado de trabalho, como a agilização dos mecanismos para os reconhecimentos dos diplomas obtidos no estrangeiro;  
- Formar os/as técnicos/as e dirigentes das instituições e organizações com um papel relevante na colocação de trabalhadores/as no mercado de trabalho, como o IEFP, e/ou membros de organizações governamentais e não governamentais que lidam diretamente com a integração de imigrantes no mercado de trabalho;  
- Desenvolver campanhas de informação e criar estratégias de prevenção do** \*burnout**\*;  
- Criação de um Grupo de Trabalho para a alteração do enquadramento legal das profissões de desgaste rápido, que defina critérios para a atribuição desta qualificação e identifique um elenco exemplificativo de tais profissões.  
- Integrar no Serviço de Higiene e Saúde no Trabalho a figura do Psicólogo do Trabalho que, à semelhança e num modelo próximo dos Enfermeiros e Médicos do Trabalho, assumirá a responsabilidade da avaliação dos riscos psicossociais e do bem-estar no âmbito da vigilância da saúde, fomentando a realização periódica de exames de avaliação psicológica nas empresas, reconhecendo a importância da avaliação, prevenção e intervenção nos riscos psicossociais;  
- Implementar um programa de avaliação e prevenção dos riscos psicossociais junto dos setores públicos suscetíveis de maior risco, como forças de segurança, saúde e educação;  
- Estabelecer o horário semanal de trabalho de 35 horas para todos/as os/as trabalhadores/as;  
- Estabelecer o período de férias para 25 dias úteis para todos/as os/as trabalhadores/as; no caso de pessoas com incapacidade superior a 60 %, este período passará a 30 dias úteis;  
- Garantir que os feriados nacionais que se realizam aos fins de semana possam ser celebrados no dia útil seguinte;  
- Possibilitar o gozo do dia de descanso por feriado nacional conjuntamente com os dias de descanso semanal (fim-de-semana), quando este coincida com um dia da semana;  
- Estabelecer que, a partir dos 50 anos, será acrescido 1 dia útil por cada 5 anos;  
- Consagrar a Terça-feira de Carnaval como feriado obrigatório;  
- Generalizar a semana de 4 dias até ao final da legislatura, assegurando a implementação inicial preferencial em territórios do interior ou de baixa densidade populacional e criando incentivos para a sua inclusão no âmbito da contratação coletiva;  
- Aumentar de 150 para 180 dias a possibilidade da licença parental inicial partilhada sem perda de remuneração;  
- Reforçar as medidas de apoio a mães e pais trabalhadores/as com filhos/as com deficiência, doença crónica ou oncológica, nomeadamente no que diz respeito à prorrogação da licença para assistência a filho/a e à redução do tempo de trabalho, permitindo que estes possam desenvolver a sua atividade profissional sem colocar em causa o acompanhamento dos/as seus/suas filhos/as;  
- Fomentar o recurso ao teletrabalho numa perspetiva de sustentabilidade ambiental, coesão territorial e apoio à conciliação da vida familiar;  
- Abrir o acesso de cursos online do Instituto de Emprego de Formação Profissional a pessoas de todo o país, independentemente do centro em que se encontrem registadas, e incentivar à diversificação de ofertas no interior do país;  
- Valorizar os profissionais das forças e serviços de segurança por via:  
- Da revisão do modelo de compensação pelo trabalho suplementar efetuado pelos polícias de segurança pública, que defina critérios objetivos e transparentes para o pagamento de trabalho suplementar, evitando a discricionariedade do Diretor Nacional e esclareça a diferenciação entre serviço de piquete e trabalho suplementar;  
- Da atribuição de suplemento de missão à GNR, à PSP, à ASAE e ao pessoal do corpo da Guarda Prisional pelo exercício de funções em condições de risco, insalubridade e penosidade;  
- Garantir a revisão das condições de mobilidade dos agentes e guardas da PSP e GNR  
- Avaliar as condições de trabalho nas instalações das forças de segurança com o objetivo de detetar os imóveis que precisem de intervenção e procedendo à reabilitação dos mesmos;  
- Valorizar os bombeiros profissionais e voluntários e os seus direitos:  
- Revendo o estatuto social do bombeiro:

---

[Documento 5] Partido: Partido Comunista Português | Tópicos: trabalho
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 3 VALORIZAR OS TRABALHADORES PROMOVER O EMPREGO COM DIREITOS, O AUMENTO DOS SALÁRIOS E A MELHORIA DAS CONDIÇÕES DE VIDA E DE TRABALHO > 3.4 Reduzir o tempo de trabalho, combater a desregulação dos horários
#### 3.4 Reduzir o tempo de trabalho, combater a desregulação dos horários  
A luta pela redução do tempo de trabalho constitui uma referência de avanço social e civilizacional de extraordinária importância. Tal como constituiu uma grande vitória a aprovação da proposta do PCP que, em 2016, repôs e fixou o período normal de trabalho nas 35 horas semanais na Administração Pública.  
É preciso concretizar também este avanço no sector privado e prosseguir o objectivo de uma maior redução, medida justa para os trabalhadores e um importante contributo para criar postos de trabalho e combater o desemprego.  
Ao mesmo tempo, é também necessário dar firme combate à desregulação dos horários, de forma a proteger a segurança e saúde dos trabalhadores. É incompreensível que Portugal seja, no contexto europeu, um dos países onde se praticam horários mais desregulados, de que é exemplo a completa liberalização dos horários de abertura dos estabelecimentos comerciais.

---

[Documento 6] Partido: Bloco de Esquerda | Tópicos: trabalho
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 3 Trabalho, Salário e Pensões > 3.2 Precariedade e direitos coletivos > As propostas do Bloco: > Relançar a contratação coletiva e reduzir o horário de trabalho
#### As propostas do Bloco:  
##### Relançar a contratação coletiva e reduzir o horário de trabalho  
- → Relançar as convenções coletivas e o sistema coletivo de relações laborais, nomeadamente com o fim da caducidade unilateral dos instrumentos de regulação coletiva de trabalho e a reposição do tratamento mais favorável ao trabalhador;
- → Redução progressiva do horário de trabalho, fixando por lei, nesta legislatura, o período normal de trabalho, no máximo, nas 35 horas;
- → Consagrar na lei a possibilidade de opção (também por iniciativa do trabalhador) pela semana de 4 dias, vinculada à redução do horário de trabalho semanal e sem perda de rendimento;
- → Combater a desregulação dos horários, limitando e regulando a utilização da figura da "isenção de horário" e da generalização da laboração contínua;
- → Realizar um livro verde sobre o tempo de trabalho, que faça o levantamento da extensão do uso da adaptabilidade e do banco de horas, do trabalho por turnos e noturno e sua incidência setorial;
- → Eliminar integralmente o corte no acréscimo remuneratório do trabalho suplementar, reduzido para metade em 2012 e apenas parcialmente reposto. Recuperação do descanso compensatório.

---

[Documento 7] Partido: Partido Comunista Português | Tópicos: trabalho
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 3 VALORIZAR OS TRABALHADORES PROMOVER O EMPREGO COM DIREITOS, O AUMENTO DOS SALÁRIOS E A MELHORIA DAS CONDIÇÕES DE VIDA E DE TRABALHO > 3.4 Reduzir o tempo de trabalho, combater a desregulação dos horários > O PCP propõe:
##### O PCP propõe:  
- a redução do horário de trabalho, fixando como máximo as 35 horas semanais para todos os trabalhadores, (prosseguindo a redução para quem já esteja nesse nível), sem perda de remuneração nem de outros direitos;
- a consagração, no imediato, dos 25 dias úteis de férias para todos os trabalhadores; reposição do regime de majoração na Administração Pública;
- medidas efectivas para combater a desregulação dos horários, respeitando os seus limites diários e semanais e os dois dias consecutivos de descanso semanal, em regra, ao sábado e ao domingo; a proibição de abertura dos estabelecimentos de venda ao público, incluindo nos centros comerciais e nas grandes superfícies, aos domingos e feriados; a revogação das normas que instituem sistemas de bancos de horas e de adaptabilidade; o combate ao prolongamento da jornada diária, ao abuso do trabalho extraordinário e à prestação de trabalho não remunerado;
- a limitação legal do trabalho em regime de turnos e de laboração contínua às actividades de natureza social impreterível ao funcionamento da economia, atendendo ao direito à articulação da vida profissional com a vida familiar e aos riscos para a saúde dos trabalhadores.

---

[Documento 8] Partido: Partido Comunista Português | Tópicos: trabalho
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 3 VALORIZAR OS TRABALHADORES PROMOVER O EMPREGO COM DIREITOS, O AUMENTO DOS SALÁRIOS E A MELHORIA DAS CONDIÇÕES DE VIDA E DE TRABALHO > 3.4 Reduzir o tempo de trabalho, combater a desregulação dos horários > O PCP propõe:
##### O PCP propõe:  
- reduzir no imediato, para todos os trabalhadores e sem perda de remunerações, o tempo de trabalho semanal para as 35 horas e fixar a jornada diária no máximo de sete horas;
- prosseguir a redução progressiva do horário de trabalho, particularmente onde aquele limite máximo já está em vigor;
- garantir que a semana de 4 dias não pode ser aplicada à custa do aumento da jornada diária e/ou da diminuição do salário ou de outros direitos e remunerações, ou ainda da imposição de trabalho por turnos ou laboração contínua.

---

[Documento 9] Partido: CHEGA | Tópicos: trabalho, impostos, seguranca_social
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > XI CAPÍTULO RESTITUIR A DIGNIDADE AOS TRABALHADORES. COMO? > PROPOSTAS
### PROPOSTAS  
**255.** Aumentar o salário mínimo nacional para 1.000 euros até 2026 e criar um programa de apoio às empresas que demonstrem um peso de custos fixos operacionais superior a 30%, por forma a que estas consigam fazer face ao aumento.  
**256.** Garantir que os estágios profissionais são remunerados, sendo que em determinadas profissões, como é o caso da advocacia, deve ser simultaneamente criada uma medida de apoio aplicável aos estágios sob orientação da Ordem dos Advogados, ajustada às especificidades da profissão e com procedimento simplificado.  
**257.** Proceder a uma avaliação das profissões que devem ser classificadas como profissões de desgaste rápido, como é o caso das profissões de enfermeiro ou motorista de pesados.  
**258.** Simplificar o regime relativo aos acidentes de trabalho.  
**259.** Assegurar que os anúncios de trabalho contêm um conjunto relevante de informação como, por exemplo, a identificação do empregador e o valor certo ou estimado da retribuição ou que esta informação é prestada ao candidato no contacto que precede a entrevista.  
**260.** Criar incentivos à contratação de jovens à procura do primeiro emprego e jovens qualificados, de desempregados de longa duração e de muito longa duração e de trabalhadores emigrantes que regressem a Portugal, através de uma dispensa parcial ou isenção total do pagamento de contribuições para o regime geral de segurança social, na parte relativa à entidade empregadora.  
**261.** Assegurar que os recibos de vencimento contêm um conjunto de informações relevantes, tais como descontos ou deduções, incluindo o valor acumulado de retenção de IRS e de descontos para a Segurança Social do ano corren-  
**<sup>1</sup>** In: "Livro Branco – Mais e Melhores Empregos para os Jovens"; p. 1; Fundação José Neves; Observatório do Emprego Jovem e Organização Internacional do Trabalho; Dezembro 2022. **<sup>2</sup>** Ibidem; p. 14.  
te e as contribuições efetuadas pela entidade empregadora para a Segurança Social respeitantes ao trabalhador, incluindo o valor acumulado para o ano corrente.  
**262.** Modificar o regime do horário flexível de trabalhador com responsabilidades familiares quando ambos os progenitores tenham a mesma entidade empregadora, de forma a que pelo menos um deles possa ter acesso ao horário flexível.  
**263.** Atribuição de benefícios fiscais para empresas que disponham de serviço de creche para os seus funcionários.  
**264.** Proceder ao reforço dos meios técnicos e humanos da Autoridade para as Condições do Trabalho, assegurando que esta tem todas as condições para proceder a fiscalizações regulares e dar resposta às denúncias recebidas.  
**265.** Assegurar que o trabalho suplementar, conhecido como "horas extra", é pago a 100% e que estas horas estão isentas do pagamento de IRS e Segurança Social e reduzir em 50% a incidência de IRS e Segurança Social sobre o subsídio de turno.  
**266.** Estabelecer programas de formação para jornalistas e profissionais de comunicação social, mais focados em competências digitais, jornalismo de investigação e reportagem, a fim de elevar o padrão do jornalismo e adaptá-lo às novas exigências do mercado e às expectativas dos cidadãos.  
**267.** Estabelecer estratégias de intervenção ou prevenção dos riscos psicossociais em contexto laboral e avaliar a possibilidade de criar a figura do psicólogo do trabalho.  
**268.** Promover a longevidade ativa voluntária, alargando a presença dos seniores no mercado de trabalho, facilitando a acumulação de pensão-reforma e trabalho e criando um sistema de tutoria juniores/seniores para transmitir conhecimentos industriais estratégicos, conforme proposta da CIP.

---

[Documento 10] Partido: Iniciativa Liberal | Tópicos: trabalho, impostos
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 4.TRABALHO: MENOS RESTRIÇÕES, MAIS OPORTUNIDADES > 4.1. Flexibilizar a legislação laboral à luz dos padrões europeus
#### 4.1. Flexibilizar a legislação laboral à luz dos padrões europeus  
Embora no início da década passada se tenha verificado uma aproximação entre a legislação que regula o emprego privado, o Código do Trabalho, e o emprego no Estado, a Lei Geral do Trabalho em Funções Públicas (LGFP), subsistem diferenças substanciais entre estes dois universos.  
Sendo atendível a existência de um regime próprio por força das especificidades das atribuições e das responsabilidades do serviço público, sobretudo quando respeitantes às designadas funções de soberania nacional (Forças Armadas, forças de segurança, magistraturas judicial e do Ministério Público, diplomacia e representação externa), as relações de emprego – públicas ou privadas – devem caminhar para a uniformização, salvaguardando que algumas funções devem ser protegidas das mudanças de ciclos políticos.  
**Aumentar matérias que podem ser alteradas por negociação coletiva e individual**  
A Iniciativa Liberal defende que, em matérias como a própria relação jurídica e a tipologia do emprego, a regulação das carreiras (sempre que tal não colida com o acima referido), os mecanismos de mobilidade, os períodos experimentais, o tempo de trabalho, e os aspectos relativos à extinção dos vínculos **devem ser remetidas de forma mais alargada para a contratação coletiva e para a negociação individual, tanto no sector público como no privado**.  
**Aproximar as regras laborais dos padrões europeus**  
A Iniciativa Liberal quer **aproximar o enquadramento legal do trabalho dos padrões dos países europeus mais desenvolvidos**, reduzindo a complexidade administrativa e sensibilizando os vários atores laborais para a relevância de uma abordagem a esta temática na linha da **flexisegurança**, como se encontra na generalidade dos países europeus com mercados de trabalho mais modernos e salários mais elevados. Pretende-se aumentar as situações que permitem o acesso ao subsídio de desemprego, reduzindo a duração máxima desse subsídio. Resumindo, as saídas e as entradas no emprego são mais flexíveis, mas a segurança na procura de novo emprego a nível de apoios públicos também é maior.  
**Restabelecer mecanismos de flexibilidade no horário**  
Entre as alterações realizadas ao Código de Trabalho em 2019, verificou-se uma da qual resultou um sério prejuízo à gestão das empresas e dos trabalhadores. Aos decisores políticos não deve ser indiferente o facto de a atividade de uma grande parte das empresas não ser necessariamente regular ao longo do tempo. Os picos de laboração contrastam com períodos de arrefecimento da atividade. Tais flutuações exigem adequação da resposta de quem gere as empresas, tendo em vista a sua própria rentabilidade e sustentabilidade, bem como a manutenção dos postos de trabalho.  
Uma forma alternativa de lidar com essas variações – muitas delas de difícil previsão – reside na **instituição de mecanismos de flexibilização de horários, assentes em acordos prévios entre a entidade patronal e o trabalhador**. Assim, a Iniciativa Liberal defende que a acrescer à possibilidade de recurso a bancos de horas como resultado de instrumentos de regulação coletiva seja novamente consagrada a hipótese de utilização de bancos de horas por via de negociação individual, podendo o horário normal de trabalho ser aumentado até duas horas por dia, 50 horas por semana e 150 horas por ano.  
A entidade empregadora terá sempre de ressarcir o trabalhador pelo trabalho realizado, de entre as formas definidas por lei e acordadas com o trabalhador. **Com o desenho desta proposta, são reforçadas as garantias do trabalhador, uma vez que o banco de horas individual tem de ser expressamente aceite, por escrito, pelo trabalhador** – diferença relevante face ao quadro legal que vigorou até 2019.  
Uma das vantagens para o trabalhador prendese com a maior flexibilidade na forma como pretende ser compensado pelo trabalho que realiza fora do horário de trabalho, que pode ocorrer sob a forma de redução do trabalho exigido de forma proporcional ao trabalho realizado fora de horas. É de notar também que hoje os trabalhadores portugueses sofrem taxas de carga fiscal muito elevadas sobre as horas extras que trabalham.  
**Evoluir para um modelo setorial de negociação de salário mínimo**  
A Iniciativa Liberal propõe alterar a legislação sobre o salário mínimo nacional, transpondo imediatamente a Diretiva Europeia n.º 2022/2041, no sentido de estabelecer indicadores que determinem os limites do salário mínimo nacional por referência ao custo de vida, a proporção do salário mínimo nacional face ao salário médio e mediano, a produtividade e a taxa de crescimento em geral.  
Com base nestes indicadores estabelecidos na lei, o salário mínimo nacional será obrigatoriamente fixado dentro de uma banda com valor mínimo e máximo. O valor concreto para cada ano terá de ser negociado em concertação social e, só na falta de acordo, poderá ser definido unilateralmente pelo governo. Em sede de negociação coletiva, os parceiros sociais poderão continuar a estabelecer valores mínimos setoriais acima do mínimo nacional.  
Além de cumprir a legislação europeia, esta medida contribui para uma maior previsibilidade em torno do salário mínimo nacional, e permite levar em conta a necessidade de aumento da produtividade e do consequente aumento dos salários em geral como condição para aumento sustentável do salário mínimo nacional.  
Esta abordagem, além de mais representativa e ajustada à realidade económica de cada atividade, evita a tendência dos partidos políticos para prometer aumentos de salário mínimo de forma eleitoralista, criando incentivos para a estipulação do salário mínimo de forma mais responsável por parte dos decisores políticos.

---

[Documento 11] Partido: Partido Socialista | Tópicos: governacao, trabalho
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **4.ª MISSÃO:** UMA DEMOCRACIA DE QUALIDADE PARA TODOS > 5. Uma Administração Pública inovadora e eficiente com trabalhadores motivados
#### 5. Uma Administração Pública inovadora e eficiente com trabalhadores motivados  
Uma Administração Pública inovadora, eficiente e próxima, com capacidade de resposta imediata às necessidades dos cidadãos e das empresas, constitui condição essencial à reconciliação das pessoas com o processo democrático de decisão e é indutora de bem-estar social e de uma economia desenvolvida. Além disso, uma Administração Pública mais eficiente e eficaz é essencial à qualidade dos serviços públicos prestados aos cidadãos e, por isso, a um Estado social forte, moderno e inclusivo.  
Nos anos de governo do Partido Socialista a Administração recuperou do enorme enfraquecimento a que a governação durante a Troika a votou com redução de recursos humanos e materiais, perda de rendimentos, processos de desvinculação de trabalhadores, desinvestimento geral. Descongelaram-se as carreiras, recuperaram-se rendimentos, aumentou-se o número de trabalhadores públicos e investiu-se na transição digital da Administração Pública. As carreiras foram valorizadas e melhorámos as remunerações - aumentámos a Base Remuneratória da Administração Pública em cerca de 63% e o valor médio anual do ganho médio mensal dos trabalhadores públicos é estimado em 1.910€ (+17,9% face a 2015).  
Mas é preciso melhorar ainda mais a governação pública e modernizar e simplificar os procedimentos administrativos e os mecanismos de gestão da Administração Pública, além de valorizar e qualificar os dirigentes e os trabalhadores, através de políticas públicas coerentes e eficazes.  
Para tal, o Partido Socialista compromete-se a:  
- Adotar modelos inovadores de gestão organizativa, designadamente através da criação e **reforço de vários tipos de serviços partilhados e dos centros de competências** e concretizar a reorganização administrativa prevista no quadro da concentração de serviços da Administração Pública num mesmo edifício;  
- Reduzir a excessiva dependência do setor público face ao fornecimento externo de serviços e de bens;  
- Atrair trabalhadores qualificados e rejuvenescer a Administração Pública, através da simplificação dos procedimentos de recrutamento e da valorização das carreiras, designadamente na fase inicial das mesmas, incluindo a recuperação faseada do tempo de serviço congelado nas carreiras que tenham o tempo como fator essencial de progressão, de acordo com o princípio da equidade;  
- Aperfeiçoar o modelo de recrutamento e seleção de dirigentes superiores valorizando as funções de direção superior e intermédia da Administração Pública;  
- Concluir a revisão das carreiras não revistas, com uma discussão alargada e transparente para harmonizar regimes, garantir a equidade e a sustentabilidade, assegurando percursos profissionais assentes no mérito dos trabalhadores;  
- Garantir a **atualização anual dos salários** respeitando o princípio da não compressão de carreiras por via do aumento do SMN;  
- Promover a qualificação e capacitação dos dirigentes e trabalhadores da Administração Pública, garantindo a formação ao longo de toda a carreira, reforçando o papel do Instituto Nacional de Administração;  
- Planificar, a médio e longo prazo, as necessidades de recrutamento de técnicos superiores, em função das inovações tecnológicas a introduzir no setor público, antecipando as necessidades futuras de quadros especializados e capacitando-os para novas áreas de governação, **garantindo a abertura de um concurso para recrutamento de 1.000 técnicos superiores por ano;**  
- Apostar na simplificação ao nível da tramitação dos diversos tipos de procedimentos administrativos;  
- Aproveitar as oportunidades do digital na relação com os cidadãos, tornando a Administração mais proativa, antecipando e resolvendo as necessidades dos cidadãos ao longo dos seus eventos de vida;  
- Garantir a total **interoperabilidade** e partilha de dados entre as entidades da Administração Pública, reforçando a adoção do princípio do only once;  
- Estabelecer o acesso a uma cloud pública a que cada pessoa possa ter acesso, em condições de proteção, privacidade e segurança, para garantir autonomia no acesso digital numa perspetiva de soberania digital;  
- Assegurar a eficácia do trabalho em rede da Administração Pública, através de mecanismos de interoperabilidade, e articulando prioridades, abordagens e soluções técnicas em comités técnicos e estratégicos;  
- Ter serviços digitais automatizados, simples e sustentáveis centrados nas pessoas e empresas que garantam proximidade, acessibilidade e inclusão;  
- Disponibilizar um **atendimento omnicanal** (digital, vídeo conferência, telefone, presencial) e uma experiência uniforme, através da utilização transversal das plataformas comuns da Administração Pública e da automatização dos serviços;  
- Alargar a rede de respostas de atendimento presencial, designadamente nos territórios de baixa densidade, assegurando um horário alargado e apostando, para o efeito, em medidas de prestação de serviços itinerantes;  
- Disponibilizar aos portugueses que se encontrem no estrangeiro de sistema de acesso a serviços públicos por videoconferência, através da Plataforma de Atendimento à Distância;

---

[Documento 12] Partido: LIVRE | Tópicos: governacao, trabalho, saude
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > **Estado e Instituições** > Por isso defendemos:
2. **Garantir o direito à informação clara e transparente**, através de:  
- garantir que toda a informação pública relevante é disponibilizada em linguagem clara e em formatos facilmente acessíveis;
- formar os cidadãos e os funcionários públicos nas questões de direito à informação;
- reformando profundamente o portal digital do Diário da República, tornando-o um repositório acessível, organizado e intuitivo de toda a legislação em vigor em território nacional;
- disponibilizar os documentos, relatórios e trabalhos de assessoria técnica que suportam decisões ou avaliação;
- potenciar o portal e Portugal como grande plataforma que agregue todos os elementos que compõem a posição da e do cidadão face ao Estado, não substituindo plataformas especializadas existentes (como o Portal das Finanças e a Segurança Social Direta), mas contendo informações essenciais relativas a todas as áreas de ação do Estado, assim como hiperligações para os portais específicos respetivos;
- publicar os perfis e currículos de qualquer pessoa que desempenhe funções de decisão pública;
- garantindo a formação contínua das e dos funcionários públicos para além das matérias do seu serviço, incluindo uma forte componente de funcionamento geral do Estado e do Direito, capacitando para melhor fornecer e perceber o enquadramento transversal da situação específica de cada cidadão.  
3. **Reforçar a autonomia e a independência do Instituto Nacional de Estatística**, que deve passar a depender diretamente da Assembleia da República, garantindo a contratação dos trabalhadores necessários para o bom funcionamento do INE e melhorando as condições de carreira e de trabalho.  
4. **Desprivatizar a Administração Pública e o serviço público** e reverter a concessão a privados das funções sociais do Estado, anulando os contratos de prestação de serviços a privados quando existe capacidade para os substituir na Administração Pública. Assegurando que a ação das instituições da área da economia social e solidária reforçam e complementam o Estado sem o substituir e que é rigorosamente escrutinada a gestão dos apoios públicos que lhes são conferidos.  
5. **Dignificar o trabalho no Estado:**  
- actualizando as posições remuneratórias em função do nível de qualificação do trabalhador (de acordo com o Quadro Nacional de Qualificações);
- considerando a contagem integral do tempo de serviço do pessoal docente e de todos os trabalhadores das carreiras e corpos especiais da administração pública, com uma regularização total a dois anos ou com outro prazo resultante do diálogo social;
- concluindo a revisão das carreiras do regime especial e dos corpos especiais e criando as carreiras especiais cujos conteúdos funcionais são diferenciados;
- aumentando o nível remuneratório inicial para técnicos superiores na administração pública, suprimindo até 2025 o nível 16 e tomando como primeiro nível remuneratório da carreira de técnico superior o nível 17 da tabela geral remuneratória;
- promovendo a valorização salarial equivalente a um nível remuneratório para técnicos superiores na administração pública com mestrado;
- melhorando as condições de trabalho, de instalações, de recursos e de formação dos profissionais do Estado;
- aprofundamento de conhecimentos técnicos e sua atualização, mas dando igualmente oportunidades de formação em áreas distintas e línguas estrangeiras;
- promovendo a mobilidade de funcionários entre funções e serviços, adequando o seu trabalho com mais facilidade, em função das contínuas formações, conhecimentos e experiência (profissional e de vida);
- fornecendo formação em bem-estar e saúde mental para a promoção de comportamentos saudáveis e práticas de bem-estar ao nível físico, social e mental;
- investindo meios e recursos na identificação precoce de situações de burnout, assédio moral, assédio sexual, entre outros, em contexto de trabalho;
- promovendo uma revisão negociada da Lei Geral do Trabalho em Funções Públicas;
- combatendo a precariedade no Estado local e central;
- apostando em sistemas de avaliação de trabalhadores que promovam a motivação e a cooperação;
- criando uma bonificação remuneratória, baseada no custo de vida do local de trabalho presencial.  
6. **Alterar os métodos de contratação da função pública e a progressão nas carreiras:**  
- apostando no mecanismo do Recrutamento Centralizado como método preferencial de recrutamento de quadros para a Administração Pública, evitando a multiplicação de processos de recrutamento e garantindo a necessária imparcialidade no acesso ao serviço público;
- garantindo que nos processos de seleção haja adequação das pessoas contratadas às necessidades específicas das instituições em causa e que sejam introduzidos critérios qualitativos tais como a avaliação curricular e a realização de entrevistas;
- revendo o SIADAP de forma a torná-lo num sistema de avaliação que efetivamente valorize o mérito e contribua para a progressão criteriosa das carreiras e que, do mesmo modo, penalize a falta de empenho reiterada, aumentando e generalizando os sistemas de avaliação de chefias por parte das equipas que lideram;
- promovendo a análise e revisão do contexto organizativo e de qualidade promovendo modelos de liderança mais horizontais, informada e transparente, possibilitando a participação ativa das e dos funcionários públicos nas cadeias de decisão que impliquem alterações nos serviços;
- tornando a nomeação de chefias mais justa e imparcial, elevando o concurso público a regra e o convite interno a exceção, não obstante a pertença à instituição em causa continuar a ser fator de valorização das candidaturas, e conferindo-lhes também profissionalização, autonomia e responsabilização;
- adotando a Classificação Nacional das Áreas de Educação e Formação (CNAEF) 2013 (ou eventual futura CNAEF 2024) para todos os fins, incluindo não apenas todas as operações estatísticas relevantes, mas também a contratação pública (incluindo os recrutamentos centralizados), a recolha e tratamento de dados sobre formação profissional, os inquéritos e estudos e a identificação da oferta formativa.  
7. **Combater a precariedade do trabalho para o Estado**,  
- reduzindo o elevado número de trabalhadores a recibos verdes na função pública, e regularizando a sua situação contratual;
- acabando com o trabalho precário na Administração Pública convertendo os vínculos precários em contratos de trabalho subordinado;
- substituindo a subcontratação no Estado por contratações em regime de trabalho subordinado;
- combatendo o recurso abusivo ao estatuto de bolseiro.  
8. **Promover a qualidade e eficácia dos serviços públicos**, com:  
- a criação de um Programa de Avaliação e Melhoramento dos Serviços Públicos para monitorizar, avaliar e corrigir deficiências na prestação de todos os serviços públicos. Os cidadãos deverão poder participar nas avaliações do Programa, assim como apresentar sugestões de melhoria dos serviços. A partir de dados empíricos, deverá ser feita a análise e revisão do contexto organizativo de cada serviço, promovendo modelos de liderança mais horizontal, informada e transparente, com participação ativa de funcionários nas cadeias de decisão que impliquem alterações nos serviços;
- a informatização e cruzamento de dados entre setores, garantindo a privacidade das e dos cidadãos;
- a reabilitação do Instituto Nacional de Administração enquanto Escola de Administração Pública, com autonomia científica e atividade de investigação. Deverá ser dado o impulso para a criação de pós-graduações de nível superior que visem qualificar estudantes com licenciatura de diferentes áreas para integrarem a Administração Pública em posições de exigência técnica.  
9. **Lançar um programa de emprego público** para reforço de toda a Administração Pública, apostando na reversão do processo de envelhecimento e depauperação de profissionais, com particular atenção aos serviços deficitários, para suprir carências em escolas, hospitais, segurança social e outros serviços. Lançando novos processos de Recrutamento Centralizado para preenchimento de Bolsas de Emprego Público, com processos de avaliação expeditos e prevendo contratações com posições remuneratórias iniciais de acordo com o nível de qualificação do candidato.  
10. **Integrar representante das e dos trabalhadores nos conselhos de administração dos serviços públicos**, conforme estabelecido pelo artigo 89.º da Constituição, ao adequar a legislação, regulamentos e estatutos para promover a sua representação efetiva nas opções executivas das instituições públicas.  
11. **Dignificar as forças de segurança**, nomeadamente revendo os seus salários, carreiras, condições laborais e promovendo a formação:  
- igualando o Suplemento por Serviço e Risco nas Forças de Segurança da PSP e GNR ao suplemento de missão da PJ;
- simplificando o regime de suplementos, incorporando valores que já são atribuídos por esta via nas remunerações base;
- promovendo o policiamento e patrulhamento de proximidade, as responsabilidades de missões de Comando e a pertença a unidades de especiais de serviço;

---

[Documento 13] Partido: CHEGA | Tópicos: trabalho, economia
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > X CAPÍTULO FAZER PORTUGAL CRESCER. COMO? > PROPOSTAS
### PROPOSTAS  
**229.** Reduzir a carga fiscal para incentivar o investimento e estimular o crescimento das empresas, nomeadamente:  
- Desagravar a taxa de IRC para 15% ao longo da legislatura, com efeito imediato nas empresas com sede social nos concelhos do interior;  
- Desagravar a Derrama Estadual e Municipal;  
- Aumentar o limite de isenção de IVA para Trabalhadores Independentes e Empresários em Nome Individual (ENI);  
- Desagravar fiscalmente as empresas que utilizam o lucro gerado para o reinvestimento no negócio e para a criação de emprego.  
**230.** Simplificar e desburocratizar os processos administrativos para facilitar a criação de novos negócios, nomeadamente através da:  
- Digitalização de Serviços Públicos;
- Revisão e Simplificação de Processos;
- Redução de Exigências Regulatórias para Empresas;  
- Criação de uma conta-corrente entre o Estado e as empresas a fim de agilizar o relacionamento entre as duas entidades.  
**231.** Rever o Código do Trabalho, tornando-o mais simples, garantindo flexibilidade às empresas e segurança aos trabalhadores, nomeadamente, promovendo o trabalho remoto e flexível e, eventualmente, implementar os Contratos de Zero Horas para Desempregados e Reformados.  
**232.** Proceder ao levantamento das áreas consideradas estratégicas, onde o Estado pode e deve manter a sua participação, ainda que com abertura para a participação dos privados, avaliando de forma criteriosa as empresas públicas, nacionais, regionais e municipais.  
**233.** Implementar medidas de governança corporativa para melhorar a eficiência e a transparência das empresas públicas, nomeadamente:  
- Estabelecer Conselhos de Administração independentes, baseados na competência e não na simpatia ou filiação partidária;  
- Definir políticas claras e códigos de conduta internos;
- Exigir a prestação de contas de forma transparente;
- Fortalecer a gestão de riscos e controlos internos;  
- Facilitar a participação dos accionistas nas assembleias gerais, fornecer informações adequadas e garantir a protecção dos seus direitos.  
**234.** Identificar necessidades de infra-estrutura turística, promovendo o seu investimento público e privado, incluindo as áreas necessitadas de alojamento e infra-estrutura de transportes e lançar programas de apoio à satisfação dessas necessidades.  
**235.** Revogar a legislação que impõe restrições ao alojamento local (Programa Mais Habitação).  
**236.** Atrair investimentos na infra-estrutura turística, preferencialmente para as áreas do interior, através da criação de incentivos fiscais e da simplificação dos processos de licenciamento.  
**237.** Concluir o processo de escolha do Novo Aeroporto de Lisboa e iniciar com a maior brevidade possível a sua construção, bem como de outras infra-estruturas indispensáveis, nomeadamente a Ferrovia e o TGV (Alta Velocidade).  
**238.** Promover o turismo sustentável, partindo do princípio que o turista além de visitar lugares, pretende viver experiências, respeitando o meio-ambiente e as comunidades locais.  
**239.** Criar centros de inovação e parques tecnológicos com o objectivo de desenvolvimento de políticas de inovação que promovam a colaboração entre universidades, empresas privadas e sector público, incluindo metas de investimento em I&D, apoio à transferência de tecnologia e estímulo ao empreendedorismo.  
**240.** Promover os centros de inovação e parques tecnológicos por meio de campanhas de marketing, participação em eventos nacionais e internacionais e atracção de investidores e parceiros.  
**241.** Desenvolver programas de qualificação e formação em parceria com universidades e empresas privadas, incluindo bolsas de estudo, programas de estágio e cursos de actualização para profissionais.  
**242.** Oferecer benefícios fiscais, como redução de impostos ou isenções, bem como estabelecer parcerias com empresas privadas que se envolvam em projectos de inovação em sectores estratégicos de que resulte um saldo positivo entre exportações e importações.  
**243.** Apoiar a internacionalização das empresas portuguesas, apostando na atracção de investimento e nas exportações, no desenvolvimento de programas de qualificação para habilitar as empresas e quadros com as competências e conhecimentos necessários a operar em mercados internacionais, devendo o Estado actuar como facilitador mas também trabalhar na atractividade do investimento estrangeiro em Portugal, promovendo a marca Portugal no exterior para atrair mais investimento.  
**244.** Facilitar o acesso a mercados externos através da remoção de barreiras comerciais, negociando ou renegociando acordos, facilitando o acesso a redes de distribuição e canais de venda no exterior e fornecendo informações sobre oportunidades de mercado, procura por produtos ou serviços específicos e tendências globais.

---

[Documento 14] Partido: Iniciativa Liberal | Tópicos: governacao, trabalho
  Secção: PROGRAMA ELEITORAL > B. PORTUGAL A FUNCIONAR > 3. REFORMAR A ADMINISTRAÇÃO PÚBLICA > 3.1. Reformar a Função Pública > Facilitar pedidos de licença sem vencimento
##### Facilitar pedidos de licença sem vencimento  
A Iniciativa Liberal quer facilitar a mobilidade laboral dentro da função pública bem como entre esta e o setor privado. Muitos funcionários públicos estão interessados noutras experiências profissionais, mas dadas as escassas oportunidades em Portugal não querem arriscar perder o emprego que têm. A Iniciativa Liberal propõe que os **pedidos** **de licença sem vencimento dentro da função pública não dependam de autorização do serviço ou departamento do estado**, permitindo ao funcionário arriscar um novo emprego noutra entidade pública, no sector privado, ou iniciar um negócio com a segurança de poder retomar o seu lugar após um número limitado de anos, a definir, caso assim prefira. Se ao fim desse período o funcionário não regressar, cessa o vínculo contratual com o Estado. Além da vantagem evidente para o funcionário público a nível do proveito de novas oportunidades com menos risco, há também a vantagem para o Estado ao abrir outra via de redução do número de funcionários públicos que não passe por aguardar que os trabalhadores entrem na idade da reforma.

---

[Documento 15] Partido: LIVRE | Tópicos: trabalho, seguranca_social
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > Trabalho, Rendimento, Tempo e Proteção Social
## Trabalho, Rendimento, Tempo e Proteção Social  
A luta pela proteção laboral e condições de vida dignas permitiram conquistas fundamentais no século XX, como a regulação do horário de trabalho e salário mínimo, reconhecimento do direito ao descanso semanal e gozo de período de férias, proteção financeira em caso de desemprego, parentalidade, doença ou incapacidade, invalidez, reforma ou velhice, ou a garantia de acesso a um patamar mínimo de segurança económica por via do rendimento social de inserção. No entanto, estas conquistas continuam a não ser acessíveis a todas as pessoas. A persistência de vínculos laborais precários, como os falsos recibos verdes, bolsas de investigação e contratos temporários, a realidade largamente ignorada das situações de trabalho sem vínculo, com destaque para o trabalho sazonal, ou o recurso abusivo a estágios profissionais e outras medidas de apoio à empregabilidade para colmatar necessidades de trabalho efetivas e continuadas, constituem claras violações destes direitos. Acresce que estas formas de trabalho precário afetam particularmente imigrantes, minorias étnico-raciais, mulheres, pessoas com deficiência, pessoas LGBTQIA+, trabalhadores com menos qualificações e jovens. A estas juntam-se outras barreiras, como as dificuldades de acesso ao mercado de trabalho, oportunidades desiguais de progressão profissional, desigualdades de remuneração por trabalho equivalente ou, ainda, a realidade de quem escolhe ou se vê forçado a abandonar o mercado de trabalho formal para prestar cuidados a familiares, que se constituem como fatores de risco acrescido de pobreza ou exclusão social.  
Por outro lado, urge preparar, desde já, a resposta aos desafios do século XXI, com uma transição para um novo paradigma de trabalho, rendimento e proteção social, que permita responder a transformações em curso como o impacto da tecnologia e automação no mercado laboral, a necessidade de diversificação das fontes de financiamento da Segurança Social assegurando a sua sustentabilidade. De igual importância é a luta por uma vida digna que não gire em torno do trabalho, permitindo uma efetiva conciliação trabalho-família e o acesso a tempos de lazer e de descanso, à qual a semana de 4 dias de trabalho, medida do LIVRE com resultados intermédios favoráveis, procura responder. Mais tempo livre também permite às pessoas investir em atividades de reforço de competências pessoais e profissionais, sem as quais não é possível construir uma sociedade mais rica, qualificada e ajustada aos desafios do século XXI.  
Queremos, pois, superar o emprego como aspeto central das nossas vidas em detrimento do tempo livre e de outras formas de trabalho como o voluntário, familiar e comunitário.  
Por tudo isto, o LIVRE defende um pacto nacional para o trabalho, rendimento e proteção social que permita corrigir desigualdades no presente e construir as bases para uma sociedade de futuro que possibilite o acesso a uma proteção laboral e de rendimento que não deixe ninguém para trás, ao mesmo tempo que aposta no acesso a bens cada vez mais escassos e valiosos, como o tempo, a segurança e a estabilidade.

---

[Documento 16] Partido: Iniciativa Liberal | Tópicos: governacao, trabalho
  Secção: PROGRAMA ELEITORAL > B. PORTUGAL A FUNCIONAR > 3. REFORMAR A ADMINISTRAÇÃO PÚBLICA > 3.1. Reformar a Função Pública
#### 3.1. Reformar a Função Pública  
Para a Iniciativa Liberal, estão no centro da reforma da Administração Pública o reconhecimento e a valorização do mérito na qualidade nos serviços prestados aos portugueses de acordo com as suas reais necessidades. A carreira na função pública tem vindo a ser cada vez menos atrativa para profissionais de qualidade, como é caso paradigmático na área da saúde, onde cada vez mais quadros preferem trabalhar no sector privado ou emigrar para terem melhores condições de trabalho.  
Uma reforma da função pública requer um passo prévio de conhecimento dos recursos humanos afectos a diferentes funções e o respectivo impacto que tem nos resultados prestados aos portugueses, de modo a se poder tomar as decisões necessárias à melhoria da gestão dos serviços. Feito este diagnóstico, devem manter-se os vínculos contratuais existentes até se desfazerem por iniciativa do funcionário ou no momento da reforma. No caso destes contratos, deve alterar-se as regras de progressão automática na carreira, passando a progressão a alicerçar-se em critérios de mérito e qualificação profissional. Por outro lado, deve repensar-se as regras aplicáveis a novos contratos que permitam a flexibilidade necessária ao Estado para ser um melhor empregador, dando condições mais atrativas de carreira aos funcionários. Já não há empregos para a vida, e faz mais sentido que haja oportunidades bem remuneradas, assim como mais mobilidade quer dentro da função pública quer entre esta e o setor privado.

---

[Documento 17] Partido: Aliança Democrática | Tópicos: trabalho, saude, educacao, seguranca
  Secção: PROGRAMA ECONÓMICO DA ALIANÇA DEMOCRÁTICA > 3. Melhor Estado, Combater a Corrupção > 3.2. REFORMA DA POLÍTICA DE RECURSOS HUMANOS DO SETOR PÚBLICO ADMINISTRATIVO
### 3.2. REFORMA DA POLÍTICA DE RECURSOS HUMANOS DO SETOR PÚBLICO ADMINISTRATIVO  
A política de recursos humanos do Estado deve dotar os serviços públicos e os seus trabalhadores de competências críticas, de estratégias e políticas ajustadas de recursos humanos, e de autonomia e flexibilidade para realizarem as suas missões, e deve valorizar uma cultura de iniciativa e recompensa nos profissionais do Estado. Com vista à recuperação da valorização, qualificação, propósito e incentivo ao emprego público, defende-se:  
- A prioridade estratégica e orçamental de resolver as carências mais dramáticas de um conjunto de profissões essenciais dentro do Estado, como sejam os professores, profissionais de saúde, forças de segurança e os técnicos superiores, assumindo-se a necessidade de esforços especiais para compensar o desincentivo e desvalorização (material e profissional);
- A definição da política de recursos humanos de médio prazo de cada serviço num contexto de autonomia de política remuneratória e de definição dos seus objetivos estratégicos. Este instrumento permitirá prever a evolução das competências humanas críticas, a integração do desenvolvimento tecnológico e o seu reflexo nos quadros de pessoal do serviço, as necessidades de renovação intergeracional, e desenvolver modelos de tutoria e passagem de conhecimento intergeracional;
- Permitir a capacitação da gestão dos serviços/entidades através do desenvolvimento de sistemas de partilha de boas práticas de gestão e da aposta em programas de formação avançada dos quadros dirigentes, aprofundando as parcerias com as escolas de gestão do ensino superior português;
- Implementar planos individuais de desenvolvimento de carreira dos trabalhadores, numa cultura de flexibilidade e conciliação entre vida familiar e trabalho, facilitando a mobilidade intra e inter-Administrações Públicas e carreiras, e apostando na permanente qualificação e formação profissional dos trabalhadores;
- A garantia que o mérito profissional tenha um reflexo imediato nas condições remuneratórias dos trabalhadores. O mérito deve ponderar o desempenho efetivo individual dos trabalhadores e coletivo do respetivo serviço/entidade, e ser aferido através de avaliações 360 graus desburocratizadas e focadas num processo de melhoria contínua, onde a autonomia e consequente responsabilização dos dirigentes e gestores públicos se assumam como pilares fundamentais;
- A modernização dos sistemas de avaliação e progressões das carreiras gerais (SIA-DAP e similares) criando-se o suplemento remuneratório de desempenho que a cada ano aumenta de valor com base no desempenho do trabalhador e do seu serviço/ entidade no ano anterior. Tal permite reconhecer o mérito e desempenho contínuo dos trabalhadores. Supletivamente, comtempla-se a possibilidade de trabalhadores com desempenho meritório elevado receberem bónus variáveis no final de cada ano;
- Assegurar o alinhamento e competitividade do emprego público com as condições das posições comparáveis no setor privado, preservando as proteções de emprego público. Em particular, pretende-se permitir bonificações nos salários de entrada e dos salários dos profissionais de determinada carreira sempre que o recrutamento e retenção de trabalhadores com competências essenciais se torne dificultado;
- Aplicar critérios transparentes e reforçar a imparcialidade nos processos de recrutamento para cargos públicos, de forma a atestar que a escolha dos candidatos é objetiva e de acordo com as suas qualificações, e de forma a promover um sistema baseado no mérito como forma de captar e reter bons profissionais e melhorar funcionamento das entidades públicas.

---

[Documento 18] Partido: CHEGA | Tópicos: trabalho, jovens
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > XI CAPÍTULO O QUE JÁ FIZEMOS PARA RESTITUIR A DIGNIDADE AOS TRABALHADORES
## XI CAPÍTULO O QUE JÁ FIZEMOS PARA RESTITUIR A DIGNIDADE AOS TRABALHADORES  
**PROJECTO DE LEI N.º 177/XV/1 (CH)**  
Elimina restrições injustificadas no acesso a prpfissões reguladas e estabelece limites à duração e organização dos estágios  
**PROJECTO DE RESOLUÇÃO N.º 460/XV/1 (CH)**  
Recomenda as Governo que proceda ao levantamento de todas as profissões que devem ser consideradas de desgaste rápido  
**PROJECTO DE LEI N.º 914/XV/2 (CH)**  
Actualiza o valor de Retribuição Mínima Mensal Garantida para 900 euros  
**PROJECTO DE LEI N.º 506/XV/1 (CH)**  
Fomenta o regresso de portugueses emigrados e a contratação de jovens qualificados  
**PROJECTO DE LEI 730/XV/1**  
Modifica o regime do horário flexível de trabalhador com responsabilidades familiares alterando o Código do Trabalho  
**REJEITADO**  
**CONTRA** Partido Socialista, PSD, PCP **ABSTENÇÃO** IL, BE, PAN, L **FAVOR** CHEGA  
**REJEITADO**  
**CONTRA** Partido Socialista **ABSTENÇÃO** PSD, IL, PCP, L **FAVOR** CHEGA, BE, PAN  
**REJEITADO**  
**CONTRA** Partido Socialista, PSD, IL, BE **ABSTENÇÃO** PCP, L **FAVOR** CHEGA  
**REJEITADO**  
**CONTRA** Partido Socialista, PCP **ABSTENÇÃO** PSD, BE, PAN, L **FAVOR** CHEGA, IL  
**SEM VOTAÇÃO**

---

[Documento 19] Partido: Pessoas-Animais-Natureza | Tópicos: governacao, trabalho
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por uma democracia renovada e que reconcilie as pessoas com as instituições
- Introduzir melhorias ao processo eleitoral nos círculos da emigração no âmbito das eleições para a Assembleia da República, designadamente modernizando o voto postal dos eleitores residentes no estrangeiro e adequando-o às especificidades de cada país;  
- Alargar o direito de voto em mobilidade no âmbito das eleições para os órgãos das autarquias locais a todos/as os/as eleitores/as que se encontrem impedidos de se deslocar à assembleia de voto no dia da eleição;  
- Alterar a Lei do Financiamento dos Partidos Políticos e das Campanhas Eleitorais, de forma a assegurar a revogação das isenções de IMI, de impostos sobre o património e imposto automóvel atribuída aos partidos políticos;  
- Reduzir o número mínimo de assinaturas para a apreciação de uma petição no plenário da Assembleia da República das atuais 7500 assinaturas para 4000;  
- Reduzir para 15 mil o número mínimo de subscritores/as das Iniciativas Legislativas de Cidadãos/ãs e adotar um processo de submissão e subscrição mais simples;  
- Concretizar a expansão do programa Parlamento dos Jovens ao âmbito do Governo, por via da criação da figura dos conselhos de ministros dos jovens, e ao âmbito municipal, por via da criação das assembleias municipais jovens;  
- Empreender um debate alargado sobre a regionalização, que envolva a Administração Pública, a academia e a sociedade civil e proceder a uma revisão constitucional que elimine a pergunta de alcance regional e clarifique os termos do referendo de âmbito nacional;  
- Consagrar a eleição direta pelos/as cidadãos/ãs dos/das presidentes e vice-presidentes das CCDR e previsão de uma tutela de legalidade do poder estadual sobre a conduta das direções das CCDR, por forma a promover a democratização da governação territorial e uma efetiva independência das direções das CCDR face ao Governo;  
- Reforçar a legitimidade democrática das Áreas Metropolitanas e das Comunidades Intermunicipais, com a instituição de um novo modelo assente na eleição direta, por sufrágio universal, do órgão deliberativo e do/da Presidente do órgão executivo;  
- Reforçar o papel da Assembleia da República no processo de designação dos membros dos conselhos de administração das entidades reguladoras e do Banco de Portugal, dando um caráter vinculativo ao parecer da comissão competente para a audição e estabelecendo a audição obrigatória do Ministro do Governo responsável pela escolha do nome proposto;  
- Implementar um modelo de recrutamento para os cargos dirigentes da Administração Pública que estabeleça métodos diferenciados, conforme estejam em causa cargos predominantemente técnicos e cargos em que predomine a dimensão de confiança política, ainda que com exigentes critérios curriculares legalmente definidos e com uma duração igual à do mandato do Governo;  
- Assegurar uma valorização salarial dos/das trabalhadores/as da Administração Pública;  
- Assegurar a elaboração de um estudo independente e de matriz académica sobre o presente e o futuro das condições laborais dos jornalistas, tendo em vista uma alteração legislativa que valorize e proteja esta profissão;  
- Promover a transparência e o cumprimento de objetivos fixados aquando da aquisição, por parte dos investidores em grupos de comunicação social;  
- Incluir os órgãos digitais e nas zonas de cruzamento que existem entre as plataformas digitais de comunicação e os órgãos de comunicação propriamente ditos no âmbito da Lei de Imprensa;  
- Estabelecer na legislação autárquica a obrigatoriedade de transmissão e disponibilização online das reuniões dos órgãos das autarquias locais;  
- Alargar o direito de consulta prévia das forças da oposição nas Autarquias Locais a outros assuntos autárquicos estruturantes, para além dos documentos previsionais autárquicos, nomeadamente o exercício dos poderes tributários do município ou a revisão dos instrumentos de gestão territorial;  
- Garantir o fim do bloqueio e reboque de viaturas em parques ou lugares de estacionamento pelo incumprimento do pagamento do mesmo, quando não superior a 48 horas;  
- Fim da cobrança por parte da AT de coimas e multas aplicadas pelas concessionárias privadas, procedendo-se à alteração da legislação, com vista à tramitação do processo tendente à cobrança pelas vias judiciais normais;  
- Reforçar os meios para o Centro Nacional de Cibersegurança, para que possa monitorizar as ameaças e salvaguardar os sistemas informáticos do Estado e de todas as instituições públicas, infraestruturas de comunicação em território nacional, e sistemas críticos;  
- Avaliar a migração de todo o software de agências governamentais e entidades públicas para software livre, seguindo exemplos de outros países, garantindo, ao mesmo tempo, que o software desenvolvido pelo Estado ou financiado por recursos públicos, tem o seu código público, ou seja, é software livre, excecionando situações devidamente justificadas ou de segurança pública;  
- Valorização e dignificação dos sapadores florestais, fixando regras referente ao seu estatuto remuneratório e à progressão na carreira  
- Garantir a existência de Serviços Municipais de Proteção Civil em todos os municípios;  
- Garantir a atualização de todos os Planos Municipais de Proteção Civil, de acordo com a legislação vigente e incluindo matérias de proteção animal;  
- Aumentar o financiamento dos Serviços Municipais de Proteção Civil e de acordo com o risco do território correspondente.

---

[Documento 20] Partido: Partido Socialista | Tópicos: trabalho
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **1.ª MISSÃO:** UMA ECONOMIA EM TRANSFORMAÇÃO ASSENTE EM CONTAS EQUILIBRADAS > 5. Trabalho, relações laborais e qualidade do emprego > 5.1. Trabalho e relações laborais
#### 5. Trabalho, relações laborais e qualidade do emprego  
##### 5.1. Trabalho e relações laborais  
A evolução entre 2015 e 2023 no mercado de trabalho é digna de registo. Foram criados quase 630 mil empregos, o que elevou a população empregada para os 5 milhões de pessoas, um nível que não era atingido há cerca de duas décadas. O desemprego, que chegou a estar acima dos 18%, afetando mais de 900 mil pessoas, baixou também para mínimos de 20 anos, e baixou também a precariedade. Ao mesmo tempo, os salários aumentaram, desde logo o salário mínimo, que cresceu por mais de 60% desde que o PS é Governo, acompanhado de um aumento de 33% do salário médio.  
Estes resultados foram alcançados num quadro de recuperação sustentada da economia, mas são fruto também de opções de política pública com uma orientação muito clara para a qualidade e estabilidade do emprego. Primeiro nas políticas ativas de emprego, depois, em 2019, com a reversão de algumas das reformas laborais introduzidas pela direita, deram-se passos importantes no combate à precariedade e na dinamização da negociação coletiva, um caminho que foi aprofundado pela Agenda do Trabalho Digno.  
Ainda assim, apesar dos progressos alcançados, persistem focos de preocupação e objetivos por alcançar no mercado de trabalho. Além da persistência de algumas bolsas de desemprego, em particular desemprego de longa duração, continua a haver níveis significativos de emprego precário nos jovens e surgem novas formas de emprego e de prestação de trabalho cuja monitorização e regulação tem de ser melhorada. Por seu turno, é essencial continuar a melhorar os padrões de rendimento e os salários, com objetivos ambiciosos, a pugnar pela qualidade do emprego e por políticas públicas que a promovam e a responder às mudanças profundas na economia e nos modos de organização social.  
Assim, o PS propõe-se a:  
- Assegurar a **plena implementação do Acordo de Concertação Social sobre Rendimentos, Salários e Competitividade e dos seus compromissos** e aprofundar o diálogo nesta sede, renovando os compromissos nele contidos, alargando o horizonte temporal considerado e reforçando os meios e instrumentos para o viabilizar;  
- Estabelecer, em diálogo social na Comissão Permanente de Concertação Social, u**ma trajetória plurianual de aumento do SMN que permita atingir pelo menos os €1.000 em 2028,** num quadro de acompanhamento regular das dinâmica salarial no mercado de trabalho;  
- Discutir com os parceiros sociais a adoção de **instrumentos de melhoria das situações laborais das empresas,** designadamente a partir do aumento da transparência sobre os níveis de rotatividade nos quadros de pessoal e dos leques salariais praticados;  
- **Aprofundar a relação entre políticas ativas de emprego e o trabalho digno** e em particular **reforçar os mecanismos de focalização e seletividade das políticas** ativas e os mecanismos de prevenção da precariedade, e assegurando uma avaliação regular sobre os resultados dos programas promovidos pelo IEFP, em particular estágios e apoios à contratação;  
- Reforçar o papel e os meios do serviço público de emprego, no IEFP, reafirmando a sua centralidade, o seu papel de liderança nas políticas ativas de emprego e a sua capacidade de resposta individualizada e a segmentos específicos da população desempregada;  
- **Promover um maior alinhamento entre a política ativa de emprego e a política económica do país,** mobilizando estes instrumentos de política pública para o esforço de transformação da economia e apostando em **programas e condições específicas direcionados para setores emergentes, considerados prioritários ou com forte potencial de crescimento** e qualificação da economia portuguesa;  
- Melhorar a ligação entre o serviço público de emprego e as estruturas de apoio à criação de projetos empresariais, tirando partido da capacidade instalada e dos meios do IEFP para, além do papel de inclusão no mercado de criação de emprego, apostar em **programas de criação de empresas direcionados para o desenvolvimento destes setores emergentes;**  
- Lançar iniciativas direcionadas à inclusão aos desempregados de longa duração, desempregados de muito longa duração, jovens NEET e inativos desencorajados de modo a maximizar o potencial produtivo da economia e o potencial de inclusão do mercado de trabalho;  
- Desenhar e **implementar um programa nacional de Mercado Social de Emprego** para promover a aproximação ao mercado de trabalho dos públicos mais desfavorecidos e afastados do mercado de trabalho, partindo de experiências-piloto com base em projetos locais, zonas deprimidas e/ou para públicos mais vulneráveis, envolvendo nomeadamente entidades públicas, autarquias locais, entidades da economia social e trabalho no âmbito da responsabilidade social das organizações, e contribuindo também deste modo para reforçar a atratividade e a coesão dos territórios de baixa densidade, e para combater a exclusão social e pobreza nos territórios urbanos mais complexos;  
- **Reforçar a Autoridade para as Condições de Trabalho,** no seguimento da Agenda do trabalho Digno, de modo a assegurar que o funcionamento do mercado de trabalho se pauta por níveis elevados de cumprimento da lei e de penalização dos que violam direitos e distorcem a concorrência;  
- Estimular o contributo dos **empregadores para soluções de habitação dos trabalhadores;**  
- Aprofundar, no âmbito da concertação social, a proteção laboral dos trabalhadores das plataformas digitais.

---

[Documento 21] Partido: Aliança Democrática | Tópicos: governacao, financas
  Secção: PROGRAMA ECONÓMICO DA ALIANÇA DEMOCRÁTICA > 3. Melhor Estado, Combater a Corrupção
## 3. Melhor Estado, Combater a Corrupção  
A necessidade de reformas no Estado é evidente há várias décadas. Uma reforma do Estado que seja mais do que simplificação e desburocratização, elementos consensuais, apesar de continuarem a ser necessários. Menos consensual é a necessidade de uma análise profunda e crítica de todas as estruturas da Administração pública, incluindo institutos, observatórios e fundações. Mais fundamentalmente, é urgente desenhar uma nova estrutura da administração pública, ao serviço dos cidadãos. A Reforma do Estado deverá resultar numa organização coerente, eficiente e eficaz, fundada nos objetivos e funções fundamentais da intervenção do Estado, e flexível para permitir diferentes escolhas políticas em relação aos meios de alcançar esses fins. Deverá ser promovida a descentralização e a autonomia das estruturas da Administração pública, com responsabilização correspondente. Em paralelo, deve implementar-se um sistema transparente de monitorização dos recursos do Estado. Como elemento transversal de qualquer reforma, deve afirmar-se que o Estado está ao serviço das pessoas, e não o contrário.  
O contexto de partida é o da descapitalização humana e material, e a falência operacional do Estado, após anos de escolhas erradas, de desvalorização dos funcionários públicos mais qualificados, de desincentivo ao esforço, mérito e produtividade no setor público, e ineficiência na afetação de recursos, via cativações, cortes transversais e esmagamento do investimento público reprodutivo, resultando na diminuição do stock de capital público.  
As reformas do Estado devem ser orientadas pelos princípios gerais de Descentralização, Autonomia, Responsabilização, Capacitação, e Comparação Internacional. A concretização de uma reforma profunda deve ser caracterizada por medidas incrementais e por um pacto de médio-longo prazo.  
De forma alinhada com estes princípios, será desejável adotar um modelo de procedimento orçamental contratual (por oposição a um modelo de delegação centralizado no Ministério das Finanças), que se inicia com a definição clara dos recursos afetos a cada área governativa, de preferência numa perspetiva plurianual, tornando o ministro sectorial o responsável máximo pela sua execução e permitindo uma gestão descentralizada dos recursos que lhe estão atribuídos. Mas não só; transita-se para um paradigma em que, por exemplo, escolas públicas e hospitais públicos têm a mesma autonomia de gestão e orçamental que têm os hospitais em regime de PPP ou as escolas em regime de contrato de associação. Neste sentido, cria-se a indistinção entre a provisão pública ou privada, dando capacidade às entidades públicas de competir de forma equilibrada com o setor privado. Só com autonomia, flexibilidade para contratar, para realizar despesas, para melhorar processos parece ser possível as entidades públicas aproximarem-se da eficiência que se aponta ao setor privado.  
Como elemento prévio deste procedimento orçamental contratual, é necessário implementar um sistema transparente de monitorização da restrição de recursos do Estado, com uma visão global e consolidada sobre a sua receita, despesa, tesouraria central e situação patrimonial. No processo de tomada de decisão, o Governo tem de ter uma visão completa dos custos e benefícios das suas escolhas, de forma a minimizar a possibilidade de estas colocarem em risco a sustentabilidade das finanças públicas. Atualmente, esta visão global é dificultada pelo elevado nível de fragmentação orçamental, que consente uma tomada de decisão a níveis inferiores sem uma correta internalização dos custos dessas escolhas.  
Em complemento a esta abordagem é indispensável promover a adoção de medidas especificas para promoção da integridade, transparência, e responsabilidade política na governação, bem como de firme e efetivo combate à corrupção. A situação portuguesa e as últimas experiências de governação socialista tornam indispensável uma resposta robusta em políticas públicas. A fragilidade ética, a cultura de informalidade e promiscuidade entre poderes públicos e certos agentes económicos, a ausência de responsabilização política e a atuação política e pública facilitadora da corrupção e tráfico de influências minam a qualidade e confiança na democracia, mas também corroem o ambiente económico e de investimento e criam desigualdades concorrenciais e ineficiências de alocação de recursos que diminuem o crescimento potencial da economia e o bem-estar social.  
Nesse sentido, o Programa Eleitoral da AD inclui um "Pacote de Medidas para a Integridade e Transparência e Combate à Corrupção" com respostas robustas e diferenciadoras que nele são explanadas, desde a regulamentação do lobbying, redução de conflitos de interesse, de criminalização do enriquecimento ilícito, reforma dos mecanismos institucionais e processuais de prevenção da corrupção.

---

[Documento 22] Partido: Partido Comunista Português | Tópicos: economia, trabalho, educacao
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 2 DESENVOLVIMENTO ECONÓMICO > 2.3. Políticas-chave > 2.3.4 Uma Transição Digital que respeite os direitos dos cidadãos > O PCP defende:
###### O PCP defende:  
- a propriedade e controlo públicos das principais infraestruturas de armazenamento, tratamento, circulação e difusão de dados. O desenvolvimento da cooperação internacional multipolar para garantir a liberdade na rede e o seu desenvolvimento livre;
- colocar os benefícios decorrentes dos avanços tecnológicos ao serviço da economia nacional e da melhoria das condições de vida dos trabalhadores e do povo, combatendo a apropriação privada dos ganhos obtidos com o desenvolvimento tecnológico, e promovendo uma justa repartição da riqueza produzida;
- a total transparência e neutralidade das redes, com a promoção do software livre, o tratamento igualitário de todo o tráfego, a proibição da utilização de tecnologias que se dedicam a recolher de forma invasiva dados pessoais para alimentar sistemas de IA, nomeadamente vigilância permanente em contexto laboral, devassa automatizada da privacidade, recolha de dados biométricos, entre outros;
- a total proibição da censura de conteúdos por motivos políticos e ideológicos, muitas vezes a coberto de outros pretextos, e a defesa da neutralidade da rede perante todo o tipo de conteúdos;
- Pugnar nas instâncias internacionais para que os sistemas autónomos baseados em IA sejam banidos de aplicações bélicas;
- a limitação do uso de IA (ou outras formas similares de algoritmos) para tomar ou fundamentar decisões com implicação directa na vida de seres humanos (apoios sociais, vistos, asilo, crédito bancário, acesso a um posto de trabalho, decisão judicial, etc.), exigindo que todos os parâmetros e as bases de dados usados numa tomada de decisão sejam públicos e auditáveis;
- a obrigatoriedade de sinalização do uso de IA em produtos e serviços (públicos e privados), com salvaguarda e especificação do grau de supervisão humana dos mesmos. O direito de recurso sobre qualquer decisão automatizada, assegurando que a mesma possa ser revista – sem qualquer penalização associada – por seres humanos, sem que os revisores conheçam o resultado produzido pelo sistema de IA (ou outras formas similares de algoritmos). No caso de serviços de interacção com o público, deve assegurar-se a existência de canais alternativos operados por humanos;
- obrigatoriedade para as empresas que adoptem tecnologias de automação no processo produtivo de efectuarem programas de reforço da formação e requalificação dos trabalhadores afectados;
- criação de um instituto público, que em coordenação com as Universidades e com outras entidades de regulação, assuma a promoção, condução, regulação e fiscalização do desenvolvimento e aplicação das tecnologias digitais, e em particular da IA;
- a defesa e o desenvolvimento da produção nacional, analisando os impactos da economia digital sector a sector, potenciando os recursos naturais e humanos do País e qualificando e integrando as suas forças produtivas;
- desenvolver a investigação, a ciência, a tecnologia e a inovação, e garantir a existência dos instrumentos fundamentais ao desenvolvimento tecnológico em língua portuguesa;
- a valorização do trabalho e dos trabalhadores como matriz obrigatória na condução e aplicação das novas tecnologias, respeitando os direitos laborais e a participação das suas organizações, nomeadamente pela antecipação e controlo dos impactos sobre o trabalho e o emprego, tendo como objectivo condutor a redução progressiva da jornada de trabalho, de forma imediata para as 35 horas, e a eliminação de tarefas penosas e repetitivas e dos ritmos intensivos de trabalho.

---

[Documento 23] Partido: CHEGA | Tópicos: justica, trabalho
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > II CAPÍTULO POR UMA JUSTIÇA QUE FUNCIONE. COMO? > PROPOSTAS
### PROPOSTAS  
**22.** Assegurar a digitalização de todos os processos em todos os tribunais, incluindo o Tribunal Constitucional, e proceder a melhorias nas plataformas de submissão e gestão de processos.  
**23.** Fazer uso da transformação digital no sentido de capacitar os tribunais para optimizarem a sua forma de funcionamento e assegurar o registo de todos os actos processuais em áudio e vídeo, com transcrição automática.  
**24.** Dar resposta às reivindicações dos Oficiais de Justiça, nomeadamente:  
- Preencher os lugares vagos na carreira dos oficiais de justiça, dado que existem aproximadamente 7.000 profissionais nessa área, contudo, mais de 1.000 posições encontram-se por preencher.  
- Proceder ao recrutamento de emergência de 300 efectivos, a distribuir pelos vários grupos de pessoal da carreira de funcionário judicial, para as comarcas com maiores carências;  
- Abrir concursos de acesso em todas as categorias dos grupos de pessoal da carreira de funcionário judicial;  
- Integrar o suplemento de recuperação processual no vencimento ou, em alternativa, pagamento do suplemento de recuperação processual em 14 vezes;  
- Criar um regime especial de aposentação e de acesso ao regime de pré-aposentação;  
- Rever o Estatuto dos Funcionários Judiciais e revalorização dos grupos de pessoal da carreira de funcionário judicial;  
- Revalorização remuneratória de todo o pessoal da carreira de funcionário judicial;  
- Pagar as horas extraordinárias.  
**25.** Responder às reivindicações dos Oficiais de Registo e Notariado:  
- Proceder ao recrutamento urgente dos Conservadores de Registos e dos Oficiais de Registos em falta, de acordo com o levantamento que venha a ser feito, e com uma programação projectada para 3 anos;  
- Rever o estatuto profissional das carreiras dos oficiais de registos, corrigindo as iniquidades e omissões do Decreto- -Lei n.º 115/2018, de 21 de dezembro;  
- Corrigir assimetrias salariais, em sede de sistema remuneratório;  
- Recuperar as actualizações indiciárias em dívida aos Oficiais de Registo desde 2001;  
- Proceder ao pagamento do abono para falhas;  
- Iniciar a negociação tendente a garantir o pagamento do prémio de desempenho e produtividade;  
- Proceder à promoção dos trabalhadores remanescentes da extinta carreira de escriturário, a escriturários superiores;  
- Rever as condições de desempenho de funções, nomeadamente ao nível da requalificação das instalações, colmatar a falta de meios de trabalho e implementar verdadeiras políticas de Segurança, Saúde e Higiene no Trabalho;  
- Rever as condições em que se processa o atendimento dos utentes dos serviços de registo, no sentido de assegurar a necessária reserva durante o atendimento.  
**26.** Responder às reivindicações dos advogados, solicitadores e agentes de execução:  
- Permitir a escolha entre a inscrição na Caixa de Previdência dos Advogados e Solicitadores e o regime da Segurança Social;  
- Actualizar a tabela de honorários do acesso ao Direito, assegurar o pagamento de despesas no âmbito da representação de beneficiários deste sistema e ainda um sistema de pagamento progressivo;  
- Ponderar a alteração do método de distribuição dos processos a Agentes de Execução, passando nomeadamente para um processo de distribuição aleatória, com critério de proximidade;  
- Assegurar a suspensão dos prazos em caso de morte de filho, assim como garantir apoios em caso de doença grave ou prolongada;  
- Garantir às mães com bebés recém-nascidos (até aos 4 meses) a possibilidade de proceder ao adiamento das diligências;  
- Prever condições para o exercício dos mandatos, junto dos tribunais, nomeadamente disponibilizando acesso à internet.  
**27.** Responder às reivindicações dos guardas prisionais e  
técnicos de reinserção social:  
- Proceder à regulamentação uniforme do sistema de avaliação do Corpo da Guarda Prisional (CGP);  
- Abrir vagas em número suficiente para a promoção dos Guardas Prisionais a Guardas Principais, alguns dos quais a aguardar a promoção há cerca de 20 anos;  
- Proceder à abertura de concursos para recrutamento de novos efectivos, com regularidade anual ou bianual;  
- Rever as normas estatutárias da carreira de guarda prisional, de modo a tornar a profissão mais atractiva e combater a falta de interesse que a carreira motiva em novos candidatos, com concursos de admissão que não conseguem preencher todos os lugares abertos;  
- Assegurar que os reformados do CGP, que não tenham condições económicas para encontrar outra habitação, não sejam despejados das respectivas casas de função;

---

[Documento 24] Partido: Iniciativa Liberal | Tópicos: governacao, trabalho, economia
  Secção: PROGRAMA ELEITORAL > B. PORTUGAL A FUNCIONAR > 3. REFORMAR A ADMINISTRAÇÃO PÚBLICA > 3.1. Reformar a Função Pública > Valorizar a Função Pública
##### Valorizar a Função Pública  
Valorizar o trabalho dos funcionários públicos implica proporcionar carreiras com incentivos ao seu melhor contributo na prestação de serviços públicos aos portugueses. Os recursos humanos da Administração Pública foram severamente prejudicados pelos últimos anos de governação socialista que, através de uma política de cativações e de fraco crescimento económico fez com que a função pública tenha perdido poder de compra e qualidade de vida.  
Uma melhoria substancial das condições salariais da função pública só é possível num país com um crescimento económico sustentado, que consiga promover salários competitivos na Administração Pública, em especial nos cargos hierárquicos de topo que têm, ano após ano, perdido atratividade em comparação com as alternativas existentes no mercado de trabalho. Insistimos na **inclusão de uma componente remuneratória variável que dependa do mérito individual** no exercício das funções e o fomento de **formação contínua técnica de excelência** para que se alcancem os melhores padrões de produtividade.

---

[Documento 25] Partido: Aliança Democrática | Tópicos: governacao, trabalho
  Secção: PROGRAMA ECONÓMICO DA ALIANÇA DEMOCRÁTICA > 3. Melhor Estado, Combater a Corrupção > 3.1. MELHOR GOVERNO PÚBLICO, ESTADO MAIS CAPAZ > 3.1.3. MEDIDAS PARA O SETOR EMPRESARIAL DO ESTADO
#### 3.1.3. MEDIDAS PARA O SETOR EMPRESARIAL DO ESTADO  
O universo das empresas públicas é composto pelo setor empresarial do Estado, o setor empresarial regional e o setor empresarial local. As atividades, a forma de atuação, a origem das receitas e a natureza das despesas, bem como o objetivo de serviço público é muito diferenciado, o que pode dificultar a análise do seu desempenho.  
Em 2013, o Governo do PSD/CDS-PP alterou a legislação de forma a aplicar à gestão do setor público empresarial as melhores práticas internacionais. O controlo é realizado através de 3 instrumentos: Relatório e Contas, Relatório do Governo Societário e Planos de atividade e Orçamento. Segundo o Conselho das Finanças Públicas, em fevereiro de 2023, 96% das empresas tinha apresentado o Relatório e Contas relativo a 2021, 80% o Relatório de Governo Societário, e apenas 62% tinham Planos de Atividade e Orçamento analisados pela Unidade Técnica de Acompanhamento e Monitorização do Setor Público Empresarial. Em fevereiro de 2023, a DGTF tinha aprovado apenas 56% dos Relatórios e Contas submetidos ao Tribunal de Contas, 57% dos relatórios de Governo Societário analisados pela UTAM e 77% dos planos de Atividade e orçamento analisados pela UTAM. Urge assim a adoção de medidas tendentes a resolver as atuais insuficiências.  
- **Medidas de reporte:**
- Acelerar a implementação da legislação introduzida em 2013, em particular no que diz respeito à publicação e aprovação dos instrumentos de gestão, permitindo um reforço de _accountability_ do setor público, e que sejam feitas recomendações à gestão das empresas de forma mais eficiente;
- Assegurar que em todas empresas relevantes o reporte inclui as obrigações de serviço público e as compensações que a empresa recebe do Estado para o cumprir;
- Retomar a publicação do Relatório sobre o Cumprimento das Práticas de Bom Governo da UTAM (o último refere-se ao exercício de 2017);
- **Medidas para o Conselho da Administração.** Em vários países da OCDE, as empresas do setor empresarial do estado têm membros independentes, que não representam os acionistas, mas que servem para defender os interesses de outros _stakeholders_, por exemplo trabalhadores e utilizadores dos serviços da empresa pública;
- Nas empresas de maior dimensão, à semelhança das empresas privadas, introduzir membros independentes e representantes dos trabalhadores como Administradores não executivos;
- Incentivar uma maior diversidade no Conselho de Administração, designadamente no que diz respeito à nacionalidade;
- Introduzir critérios objetivos de avaliação da Administração, incluindo o desempenho na obrigação de prestação do serviço público.

---

[Documento 26] Partido: CHEGA | Tópicos: justica, impostos
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > II CAPÍTULO POR UMA JUSTIÇA QUE FUNCIONE. COMO? > PROPOSTAS
- Assegurar que os reformados do CGP, que não tenham condições económicas para encontrar outra habitação, não sejam despejados das respectivas casas de função;  
- Assegurar que as casas de função degradadas sejam objeto de recuperação pelo IGFEJ e sejam utilizadas para alojar elementos do CGP que se encontrem deslocados dos seus locais de residência;  
- Renovar profundamente todo o parque automóvel afeto ao sistema prisional, visto que uma grande parte da frota é obsoleta, nos termos da lei de programação plurianual para a Justiça, a aprovar;  
- Ampliação e construção de novos estabelecimentos prisionais necessários em diversas zonas do país;  
- Criminalizar o incitamento ao ódio contra guardas prisionais e agravar as penas relativas a agressões;  
- Delinear uma estratégia de combate ao tráfico e consumo de droga nos estabelecimentos prisionais portugueses;  
- Proceder à contratação de técnicos de reinserção social;  
- Proceder à revalorização urgente das carreiras de técnico de reinserção social, já em 2024, principalmente na componente remuneratória, de modo a aumentar o potencial de captação e fixação de efectivos, evitando a debandada para outras carreiras ao abrigo da mobilidade.  
**28.** Impedir a renovação ou rescindir os contratos de arrendamento milionários de edifícios privados onde se encontram instalados vários tribunais, como por exemplo o arrendamento dos edifícios do Campus de Justiça de Lisboa, e, ao invés, utilizar o património do Estado existente, devoluto ou subaproveitado, para a instalação de tribunais.  
**29.** Adequar a arquitectura e espaços de Justiça, acabando com os Tribunais em contentores, e em edifícios destinados a escritórios, melhorando e dignificando as condições de trabalho para os funcionários de justiça, magistrados do Ministério Público e Juízes.  
**30.** Reintroduzir a utilização dos símbolos nacionais e de Justiça nos tribunais, recuperando mobiliário e objectos representativos da cultura portuguesa, promovendo o respeito nacional pelos tribunais, dignificando a sua imagem.  
**31.** Aprovar a lei de programação plurianual para a justiça, por forma a dar resposta à falta de equipamentos ou necessidade de modernização dos existentes, identificação de um plano de recuperação de edifícios, etc.  
**32.** Alterar as regras de acesso à arbitragem na Justiça Tributária, de forma a que qualquer litígio em que esteja envolvido dinheiro público, o Ministério Público seja obrigatoriamente parte acessória.  
**33.** Assegurar que todas as decisões arbitrais são públicas e ficam disponíveis online.  
**34.** Proceder à Reforma do Código de Procedimento e de Processo Tributário, com o objectivo de simplificação, instituindo regras que efectivamente garantam a celeridade da justiça fiscal.  
**35.** Implementar um plano de contingência urgente para eliminar as pendências nos Tribunais Administrativos e Fiscais.  
**36.** Assegurar que todas as sentenças e acórdãos, de todas as instâncias são disponibilizadas online, devendo ser tomadas as medidas necessárias para a protecção dos dados pessoais.  
**37.** Proceder à reforma do regime de recursos em matéria penal, de modo a imprimir maior celeridade aos processos, impedir a instrumentalização dos recursos e racionalizar o acesso ao Supremo Tribunal de Justiça, bem como rever a fase de instrução, nomeadamente a sua função e prazos.  
**38.** Instituir regras jurídicas que obviem o fenómeno da prolixidade nas peças processuais penais, beneficiando a celeridade da justiça.  
**39.** Rever o regime de prescrição das penas, nomeadamente no que diz respeito aos crimes contra crianças mas também relativos aos crimes de natureza económica, garantindo uma maior possibilidade de fazer justiça.  
**40.** Proceder à revisão e endurecimento das penas relativamente a crimes como violência doméstica, crimes de natureza sexual, contra crianças, entre outros.  
**41.** Introduzir no nosso Código Penal a sanção acessória de tratamento para a inibição da líbido, mais comumente conhecida como "castração química", de carácter temporário e para reincidentes.  
**42.** Introduzir a pena de prisão perpétua com possibilidade de revisão depois de cumprida uma parte da pena.  
**43.** Combater a violência doméstica, através:  
- Do aumento dos meios disponíveis para a investigação deste tipo de crime;  
- Mais formação para todos os envolvidos;
- Aumento das penas;

---

[Documento 27] Partido: Iniciativa Liberal | Tópicos: governacao, trabalho
  Secção: PROGRAMA ELEITORAL > B. PORTUGAL A FUNCIONAR > 3. REFORMAR A ADMINISTRAÇÃO PÚBLICA > 3.1. Reformar a Função Pública > Reformular regras de contratação de novos quadros
##### Reformular regras de contratação de novos quadros  
A Iniciativa Liberal quer tornar a carreira na função pública mais atrativa, permitindo ao Estado uma **maior flexibilidade para poder atrair quadros de alta qualidade**, para que os seus funcionários possam ir mais longe sem depender da boa vontade de partidos ou de governos. Após obter os dados necessários para diagnosticar as dificuldades concretas de gestão da administração pública, a Iniciativa Liberal quer estudar formas de tornar a contratação mais ajustada à realidade das relações laborais no séc. XXI, que pressupõem cada vez menos empregos para a vida e requerem a atualização frequente de competências. Queremos **mais autonomia na gestão dos vários serviços**, abrindo possibilidades de transitar os saldos orçamentais de ano para ano, e incentivando uma gestão mais racional dos recursos.  
Pretendemos **maior mobilidade dentro da função pública**, seja a pedido dos próprios funcionários públicos quando vantajoso para o serviço de destino, seja por necessidade do melhor funcionamento do próprio serviço.

---

[Documento 28] Partido: Partido Socialista | Tópicos: governacao, saude, educacao
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **2.ª MISSÃO:** UM ESTADO SOCIAL FORTE, MODERNO E INCLUSIVO
### **2.ª MISSÃO:** UM ESTADO SOCIAL FORTE, MODERNO E INCLUSIVO  
**O Estado Social é uma das maiores conquistas da nossa democracia.** Consolidado ao longo dos últimos 50 anos, permitiu a construção de uma rede pública de escolas, que garante o acesso de todos à educação básica e secundária. Numa lógica de cobertura universal e territorial, permitiu igualmente o acesso a cuidados de saúde, com a criação do Serviço Nacional de Saúde. Na segurança social, um sistema público de pensões e reformas, a par do reconhecimento progressivo de direitos e apoios nas situações de desemprego, doença, pobreza e exclusão social.  
**Os serviços públicos universais e de qualidade são o cerne do Estado Social.** E o PS esteve, desde a primeira hora, empenhado na sua criação e desenvolvimento. **Não há serviços públicos universais e de qualidade sem uma Administração Pública valorizada nas suas remunerações, qualificações e direitos,** a par de uma gestão eficiente dos recursos disponíveis e de uma atuação centrada nos cidadãos.  
Nos últimos anos foram dados passos muito importantes em domínios menos desenvolvidos do nosso Estado Social. Na habitação, estamos hoje a constituir um verdadeiro parque habitacional público, que contribuirá para suprir a escassez de oferta e para regular preços. No âmbito da ação social, e em cooperação com as organizações do terceiro setor, foram sendo criadas progressivamente respostas diversas, sobretudo ao nível da infância e do apoio a idosos. Importa hoje que a cultura e o desporto, pela sua importância na formação de cidadãos, sejam também progressivamente afirmados e materializados como um direito de todos e, nessa medida, dimensões integrantes das políticas sociais. **Só um Estado Social robusto contribui decisivamente para criar as condições de igualdade necessárias a uma verdadeira liberdade.**  
Mas o Estado Social não representa apenas a concretização efetiva dos direitos sociais fundamentais. O Estado Social é também economia. Gera riqueza e contribui, de forma decisiva, para o crescimento económico e o desenvolvimento. O Estado Social é emprego e o garante do acesso de todos à escolarização e às qualificações, à saúde, à dignidade e ao bem-estar. E tem um papel indispensável no enquadramento da atividade das empresas e na dinamização da economia. Por isso, **a consolidação, reforço e aprofundamento do nosso Estado Social será uma das prioridades do PS na próxima legislatura.** Atraindo e retendo profissionais, reforçando os mecanismos de provisão pública direta, superando lacunas e respondendo a desafios emergentes de bem-estar.

---

[Documento 29] Partido: Pessoas-Animais-Natureza | Tópicos: outros, ambiente
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por uma efetiva proteção de todos os animais, reconhecimento dos seus direitos e garantia do seu bem-estar
Lembramos que foi por proposta do PAN que foram implementadas medidas fiscais importantes como é o caso da isenção de pagamento da taxa referente ao registo e licenciamento de animais adotados, seja nos  
CROA ou nas associações de proteção animal. No entanto, consideramos, por maioria de razão, que deveria estar previsto um agravamento ou uma sobretaxa para a compra e venda de animais, de forma a incentivar a adoção e dissuadir a compra.  
O número de animais adotados representa apenas uma pequena parte dos animais recolhidos, o que resulta numa sobrelotação nos centros de recolha oficiais e nas associações de proteção animal. Além disso, muitos animais abandonados são forçados a sobreviver nas ruas, sujeitos a maus-tratos, fome e diversas carências, o que representa uma ameaça grave à sua vida e integridade física, agravado pela impossibilidade de implementação do programa CED (Capturar-Esterilizar-Devolver) em cães.  
É por isso que o PAN continuará a propor o alargamento da aplicação da metodologia CED aos cães errantes como forma de controlo da reprodução, à semelhança do que já sucede com eficácia em gatos de colónias, enquanto permanecem nas ruas pela ausência de outras soluções, sejam de recolha pelos CRO ou em parques de matilhas.  
A implementação de programas de esterilização gratuitos ou de custo reduzido para todos os animais é essencial e por isso o PAN continuará a insistir na promoção de campanhas nacionais de esterilização permanentes, em todo o país, a par da promoção de campanhas de educação, formação e sensibilização permanente junto dos detentores de animais.  
Para o PAN, a garantia do bem-estar dos animais e dos seus detentores tem de imperar e, por tal, tem de ser promovida uma rede nacional de apoio aos cuidados médico-veterinários, através das faculdades de medicina veterinária, em particular das Universidades Públicas, de protocolos com as associações que detêm hospitais ou clínicas veterinárias, cheque veterinário ou outras iniciativas que garantam a capacidade de acesso das famílias mais vulneráveis aos cuidados médico-veterinários dos animais que detêm.  
Um país assente em valores morais e éticos e que assiste a uma evolução civilizacional na forma como nos relacionamos com os outros seres vivos, não pode continuar refém dos lobbies da tauromaquia ou da caça.  
É por isso que nos comprometemos a continuar empenhados em abolir a tourada e os espectáculos tauromáquicos em Portugal, corrigindo assim um erro civilizacional em nome de uma suposta tradição, cultura e entretenimento, pondo fim à manifestação da violência associada a estes eventos.  
Com relação à caça, é inadmissível que se continue a investir milhões de euros de fundos públicos numa atividade que extermina milhões de animais e causa sérios danos à biodiversidade. Continuaremos a defender a revisão da regulamentação desta atividade e a abolição de métodos de caça cruéis como a caça à paulada ou o recurso a matilhas de cães.  
Por outro lado, não podemos continuar a ignorar os mi-  
lhões de animais que são transportados vivos. No total, e em todo o mundo, são quase dois mil milhões os animais que passam por jornadas de dias, ou mesmo semanas, transportados por via terrestre e marítima em condições deploráveis, sem água ou comida suficientes, mantidos em locais exíguos e conspurcados. A sujeição de animais a longas horas de transporte, em particular por via marítima e para países terceiros, levanta sérias implicações, não apenas éticas, mas também ambientais e de saúde pública que o PAN tem vindo sistematicamente a contestar, pelo que continuaremos empenhados em fazer avanços na defesa dos animais transportados por via terreste e aérea, pondo fim ao transporte marítimo.  
Continuaremos igualmente a impulsionar a transição para métodos alternativos ao uso de animais na investigação científica, garantindo um forte investimento nessa área.  
Além disso, é crucial que a abordagem em relação aos animais seja desprovida de qualquer visão utilitarista ou sanitarista. Os animais devem ser reconhecidos como seres sencientes e com valor intrínseco.  
E por isso é que o PAN vai continuar a lutar por uma revisão constitucional que garanta, alargue e reconheça mais proteção a todos os animais.  
Paralelamente, o PAN, vai pugnar para que a tutela penal seja revista por forma a alargar a proteção a outros animais que não apenas os animais de companhia, compromisso que assumimos em nome de um país mais  
ético e responsável no que respeita à proteção animal.  
Assim, neste contexto, o PAN propõe:  
- Criar o Ministério do Ambiente, Proteção Animal e Biodiversidade;  
- Criar uma Secretaria de Estado responsável pelo Bem-estar, Saúde e Proteção Animal no âmbito da orgânica do Governo;  
- Criar a Direção-geral de Proteção e Bem-estar Animal, revogando a passagem de competências do ICNF para as CCDRS;  
- Proceder à revisão da da República Portuguesa com vista a incluir a proteção animal, a consagrar como dever do Estado a defesa do bem-estar animal e a reconhecer o direito dos animais a um tratamento condigno e livre de sofrimento;

</details>

## item-07

**Question:** Que medidas há para baixar as rendas e o preço da habitação?

**Answer:**

As propostas dos partidos para o setor da habitação dividem-se entre o aumento da oferta pública, o controlo de preços e o incentivo fiscal:

**Aliança Democrática (AD)**
• Propõe o **fim do pacote extraordinário de medidas** de controlo de rendas, argumentando que estas desincentivam o investimento.
• Defende o aumento da **oferta de habitação pública** através de parcerias com municípios e privados.
• Pretende facilitar o **licenciamento de novos projetos** para acelerar a construção.
• Propõe a redução da carga fiscal para quem investe em habitação e a criação de incentivos para o arrendamento acessível.

**Partido Socialista (PS)**
• Defende a manutenção e o reforço do **Programa Mais Habitação**, com foco no controlo de rendas em zonas de pressão urbanística.
• Propõe o aumento do **arrendamento acessível** através de incentivos fiscais aos senhorios e da disponibilização de património público.
• Pretende combater a especulação através de medidas que limitem o uso de **Alojamento Local** em áreas saturadas.
• Propõe o reforço de apoios diretos ao arrendamento para famílias de baixos rendimentos.

**Bloco de Esquerda (BE)**
• Defende o **controlo de rendas** de forma mais rigorosa, com o estabelecimento de limites máximos aos preços de arrendamento.
• Propõe a **fiscalização de rendas abusivas** e a proibição de despejos de famílias vulneráveis.
• Defende o aumento massivo do **parque de habitação pública** e o controlo do alojamento local.
• Propõe a aplicação de taxas extraordinárias sobre o património imobiliário de luxo e sobre grandes proprietários.

**LIVRE**
• Propõe a criação de um **direito à habitação** garantido pelo Estado, com foco na construção de habitação pública de qualidade.
• Defende o **controlo de preços** em zonas de elevada pressão.
• Propõe o combate à especulação imobiliária e a limitação do uso de imóveis para fins puramente turísticos.

**Chega**
• Defende a **redução da carga fiscal** sobre os proprietários que colocam imóveis no mercado de arrendamento de longa duração.
• Propõe a simplificação de processos de construção e o combate à burocracia municipal.
• Defende o reforço da segurança jurídica para os proprietários.

**Iniciativa Liberal (IL)**
• Defende a **liberdade de mercado**, argumentando que o controlo de rendas reduz a oferta e aumenta os preços a longo prazo.
• Propõe o aumento da oferta através da **redução de impostos** (como o IMT e o IRS sobre rendimentos prediais) e da desburocratização do licenciamento.
• Defende a privatização de património público para construção de habitação e o incentivo ao investimento privado.

**PCP**
• Defende o **controlo estatal de rendas** e a proibição de aumentos abusivos.
• Propõe o reforço do **papel do Estado como construtor** de habitação pública e social.
• Defende a proibição de despejos e a proteção dos inquilinos contra a especulação.

**PAN**
• Propõe o combate à especulação imobiliária, com foco na sustentabilidade urbana.
• Defende o aumento da **habitação pública** e o controlo de preços em zonas de pressão.

**Note-se que:** Os partidos de esquerda (BE, PCP, LIVRE) focam-se no controlo de preços e no papel do Estado como construtor, enquanto os partidos de direita e centro-direita (AD, IL, Chega) focam-se no aumento da oferta através de incentivos fiscais e redução da burocracia. O PS apresenta uma posição intermédia, mantendo medidas de controlo mas com foco no apoio direto ao arrendamento.

**Reference answer:**

Uns partidos apostam sobretudo no aumento da oferta e na descida de impostos (AD, IL, CHEGA), outros na regulação das rendas e na habitação pública (BE, LIVRE, PCP), combinando o PS e o PAN vários instrumentos. A AD propõe um choque de oferta privada, pública e cooperativa (flexibilização dos solos e da densidade, libertação de imóveis públicos devolutos, PPP e build-to-rent, IVA de 6% na construção), medidas para recuperar o que chama a confiança no arrendamento, a substituição dos limites administrativos às rendas por subsídios aos arrendatários vulneráveis (incluindo um subsídio de renda dinâmico e um Porta 65 reformado) e, para os jovens, a isenção de IMT e Imposto do Selo e uma garantia pública para o financiamento total da primeira casa. A IL propõe eliminar o IMT na habitação própria permanente e o Imposto do Selo, baixar o IMI mínimo, aumentar as deduções em IRS de rendas e juros, reduzir o IVA da construção para 6% e a taxa autónoma sobre as rendas de 25% para 14,5% (menos nos contratos longos), e aumentar a oferta através de um Código da Construção, pré-licenciamento, mais solo urbanizável e densidade, build-to-rent, conversão de espaços e venda de imóveis do Estado, com a meta de 250 mil novas casas. O CHEGA propõe eliminar o AIMI e o IMT e o IMI na habitação própria, isentar de IVA a primeira habitação, baixar a tributação das rendas (10%, ou 5% nos contratos longos), aumentar a oferta com incentivos fiscais, menos burocracia e PPP em terrenos públicos a custos controlados, e apoiar os jovens e as famílias numerosas na compra de casa (crédito bonificado, garantia pública, Porta 65). O BE propõe tetos máximos às rendas e a limitação das suas atualizações, apoio imediato ao pagamento de rendas, juros baixos na Caixa Geral de Depósitos, 25% da nova construção em renda condicionada e construção pública, a proibição da venda de casas a não residentes, uma moratória a novos empreendimentos turísticos e limites ao Alojamento Local, e uma reforma fiscal que alargue a isenção de IMI, reduza o IMT da habitação própria e tribute mais as mais-valias imobiliárias, que classifica de especulativas, acabando com o regime dos residentes não habituais. O LIVRE propõe chegar a 10% de habitação pública, cooperativas e o programa Ajuda de Casa para a compra da primeira casa, apoios de emergência ao pagamento de rendas e prestações e o alargamento do Porta 65, limitar as rendas nos novos contratos a 30% acima dos limites por tipologia, tributar as mais-valias e acabar com os Vistos Gold, agravar o IMI das casas devolutas, impor quotas de habitação acessível nos grandes empreendimentos e regras mais apertadas para o Alojamento Local. O PCP propõe 50 mil casas públicas e habitação cooperativa a custos controlados, limitar os aumentos e o valor das rendas nos novos contratos, renda apoiada com taxa de esforço de 15%, que os bancos absorvam a subida dos juros com a CGD como referência, e o fim dos benefícios fiscais aos residentes não habituais e aos fundos imobiliários, com limites ao Alojamento Local. O PS propõe chegar a 5% de habitação pública, uma garantia pública ao crédito para jovens até aos 40 anos, rever a atualização das rendas tendo em conta os salários, alargar o Porta 65, aumentar a dedução das rendas em IRS até 800 euros, comprar casas para arrendamento acessível e exigir habitação a custos controlados nos novos licenciamentos. O PAN propõe crédito bonificado, IMT Jovem e isenção de Imposto do Selo para os jovens, reforço do Porta 65, IRS mais baixo para senhorios com rendas acessíveis, mais habitação pública acessível e a colocação no mercado das casas devolutas a rendas condicionadas, limitando o Alojamento Local.

**faithfulness** — Is the claim supported by the CONTEXT?

- [ ] A Aliança Democrática propõe o fim do pacote extraordinário de medidas de controlo de rendas.
- [ ] A Aliança Democrática argumenta que as medidas de controlo de rendas desincentivam o investimento.
- [ ] A Aliança Democrática defende o aumento da oferta de habitação pública através de parcerias com municípios e privados.
- [ ] A Aliança Democrática pretende facilitar o licenciamento de novos projetos para acelerar a construção.
- [ ] A Aliança Democrática propõe a redução da carga fiscal para quem investe em habitação.
- [ ] A Aliança Democrática propõe a criação de incentivos para o arrendamento acessível.
- [ ] O Partido Socialista defende a manutenção do Programa Mais Habitação.
- [ ] O Partido Socialista defende o reforço do Programa Mais Habitação.
- [ ] O Partido Socialista foca o Programa Mais Habitação no controlo de rendas em zonas de pressão urbanística.
- [ ] O Partido Socialista propõe o aumento do arrendamento acessível através de incentivos fiscais aos senhorios.
- [ ] O Partido Socialista propõe o aumento do arrendamento acessível através da disponibilização de património público.
- [ ] O Partido Socialista pretende combater a especulação através de medidas que limitem o uso de Alojamento Local em áreas saturadas.
- [ ] O Partido Socialista propõe o reforço de apoios diretos ao arrendamento para famílias de baixos rendimentos.
- [ ] O Bloco de Esquerda defende o controlo de rendas de forma mais rigorosa.
- [ ] O Bloco de Esquerda propõe o estabelecimento de limites máximos aos preços de arrendamento.
- [ ] O Bloco de Esquerda propõe a fiscalização de rendas abusivas.
- [ ] O Bloco de Esquerda propõe a proibição de despejos de famílias vulneráveis.
- [ ] O Bloco de Esquerda defende o aumento massivo do parque de habitação pública.
- [ ] O Bloco de Esquerda defende o controlo do alojamento local.
- [ ] O Bloco de Esquerda propõe a aplicação de taxas extraordinárias sobre o património imobiliário de luxo.
- [ ] O Bloco de Esquerda propõe a aplicação de taxas extraordinárias sobre grandes proprietários.
- [ ] O LIVRE propõe a criação de um direito à habitação garantido pelo Estado.
- [ ] O LIVRE foca a criação do direito à habitação na construção de habitação pública de qualidade.
- [ ] O LIVRE defende o controlo de preços em zonas de elevada pressão.
- [ ] O LIVRE propõe o combate à especulação imobiliária.
- [ ] O LIVRE propõe a limitação do uso de imóveis para fins puramente turísticos.
- [ ] O Chega defende a redução da carga fiscal sobre os proprietários que colocam imóveis no mercado de arrendamento de longa duração.
- [ ] O Chega propõe a simplificação de processos de construção.
- [ ] O Chega propõe o combate à burocracia municipal.
- [ ] O Chega defende o reforço da segurança jurídica para os proprietários.
- [ ] A Iniciativa Liberal defende a liberdade de mercado.
- [ ] A Iniciativa Liberal argumenta que o controlo de rendas reduz a oferta.
- [ ] A Iniciativa Liberal argumenta que o controlo de rendas aumenta os preços a longo prazo.
- [ ] A Iniciativa Liberal propõe o aumento da oferta através da redução de impostos.
- [ ] A Iniciativa Liberal propõe a redução do IMT para aumentar a oferta de habitação.
- [ ] A Iniciativa Liberal propõe a redução do IRS sobre rendimentos prediais para aumentar a oferta de habitação.
- [ ] A Iniciativa Liberal propõe a desburocratização do licenciamento para aumentar a oferta de habitação.
- [ ] A Iniciativa Liberal defende a privatização de património público para construção de habitação.
- [ ] A Iniciativa Liberal defende o incentivo ao investimento privado.
- [ ] O PCP defende o controlo estatal de rendas.
- [ ] O PCP defende a proibição de aumentos abusivos de rendas.
- [ ] O PCP propõe o reforço do papel do Estado como construtor de habitação pública e social.
- [ ] O PCP defende a proibição de despejos.
- [ ] O PCP defende a proteção dos inquilinos contra a especulação.
- [ ] O PAN propõe o combate à especulação imobiliária.
- [ ] O PAN foca o combate à especulação imobiliária na sustentabilidade urbana.
- [ ] O PAN defende o aumento da habitação pública.
- [ ] O PAN defende o controlo de preços em zonas de pressão.
- [ ] Os partidos Bloco de Esquerda, PCP e LIVRE focam-se no controlo de preços.
- [ ] Os partidos Bloco de Esquerda, PCP e LIVRE focam-se no papel do Estado como construtor.
- [ ] Os partidos Aliança Democrática, Iniciativa Liberal e Chega focam-se no aumento da oferta através de incentivos fiscais.
- [ ] Os partidos Aliança Democrática, Iniciativa Liberal e Chega focam-se no aumento da oferta através da redução da burocracia.
- [ ] O Partido Socialista apresenta uma posição intermédia, mantendo medidas de controlo mas com foco no apoio direto ao arrendamento.

**correctness_recall** — Does the ANSWER state this reference claim?

- [ ] A AD propõe um choque de oferta privada, pública e cooperativa.
- [ ] A AD propõe a flexibilização dos solos e da densidade.
- [ ] A AD propõe a libertação de imóveis públicos devolutos.
- [ ] A AD propõe a utilização de PPP e build-to-rent.
- [ ] A AD propõe um IVA de 6% na construção.
- [ ] A AD propõe medidas para recuperar a confiança no arrendamento.
- [ ] A AD propõe a substituição dos limites administrativos às rendas por subsídios aos arrendatários vulneráveis.
- [ ] A AD propõe um subsídio de renda dinâmico.
- [ ] A AD propõe um Porta 65 reformado.
- [ ] A AD propõe a isenção de IMT para os jovens.
- [ ] A AD propõe a isenção de Imposto do Selo para os jovens.
- [ ] A AD propõe uma garantia pública para o financiamento total da primeira casa para os jovens.
- [ ] A IL propõe eliminar o IMT na habitação própria permanente.
- [ ] A IL propõe eliminar o Imposto do Selo na habitação própria permanente.
- [ ] A IL propõe baixar o IMI mínimo.
- [ ] A IL propõe aumentar as deduções em IRS de rendas e juros.
- [ ] A IL propõe reduzir o IVA da construção para 6%.
- [ ] A IL propõe reduzir a taxa autónoma sobre as rendas de 25% para 14,5%.
- [ ] A IL propõe uma taxa autónoma sobre as rendas mais baixa nos contratos longos.
- [ ] A IL propõe aumentar a oferta através de um Código da Construção.
- [ ] A IL propõe aumentar a oferta através de pré-licenciamento.
- [ ] A IL propõe aumentar a oferta através de mais solo urbanizável e densidade.
- [ ] A IL propõe aumentar a oferta através de build-to-rent.
- [ ] A IL propõe aumentar a oferta através de conversão de espaços.
- [ ] A IL propõe aumentar a oferta através da venda de imóveis do Estado.
- [ ] A IL tem a meta de 250 mil novas casas.
- [ ] O CHEGA propõe eliminar o AIMI.
- [ ] O CHEGA propõe eliminar o IMT na habitação própria.
- [ ] O CHEGA propõe eliminar o IMI na habitação própria.
- [ ] O CHEGA propõe isentar de IVA a primeira habitação.
- [ ] O CHEGA propõe baixar a tributação das rendas para 10%.
- [ ] O CHEGA propõe baixar a tributação das rendas para 5% nos contratos longos.
- [ ] O CHEGA propõe aumentar a oferta com incentivos fiscais.
- [ ] O CHEGA propõe aumentar a oferta com menos burocracia.
- [ ] O CHEGA propõe aumentar a oferta com PPP em terrenos públicos a custos controlados.
- [ ] O CHEGA propõe apoiar os jovens na compra de casa com crédito bonificado.
- [ ] O CHEGA propõe apoiar os jovens na compra de casa com garantia pública.
- [ ] O CHEGA propõe apoiar os jovens na compra de casa com o Porta 65.
- [ ] O CHEGA propõe apoiar as famílias numerosas na compra de casa.
- [ ] O BE propõe tetos máximos às rendas.
- [ ] O BE propõe a limitação das atualizações das rendas.
- [ ] O BE propõe apoio imediato ao pagamento de rendas.
- [ ] O BE propõe juros baixos na Caixa Geral de Depósitos.
- [ ] O BE propõe que 25% da nova construção seja em renda condicionada.
- [ ] O BE propõe construção pública.
- [ ] O BE propõe a proibição da venda de casas a não residentes.
- [ ] O BE propõe uma moratória a novos empreendimentos turísticos.
- [ ] O BE propõe limites ao Alojamento Local.
- [ ] O BE propõe alargar a isenção de IMI.
- [ ] O BE propõe reduzir o IMT da habitação própria.
- [ ] O BE propõe tributar mais as mais-valias imobiliárias.
- [ ] O BE propõe acabar com o regime dos residentes não habituais.
- [ ] O LIVRE propõe chegar a 10% de habitação pública.
- [ ] O LIVRE propõe o desenvolvimento de cooperativas de habitação.
- [ ] O LIVRE propõe o programa Ajuda de Casa para a compra da primeira casa.
- [ ] O LIVRE propõe apoios de emergência ao pagamento de rendas.
- [ ] O LIVRE propõe apoios de emergência ao pagamento de prestações.
- [ ] O LIVRE propõe o alargamento do Porta 65.
- [ ] O LIVRE propõe limitar as rendas nos novos contratos a 30% acima dos limites por tipologia.
- [ ] O LIVRE propõe tributar as mais-valias.
- [ ] O LIVRE propõe acabar com os Vistos Gold.
- [ ] O LIVRE propõe agravar o IMI das casas devolutas.
- [ ] O LIVRE propõe impor quotas de habitação acessível nos grandes empreendimentos.
- [ ] O LIVRE propõe regras mais apertadas para o Alojamento Local.
- [ ] O PCP propõe a construção de 50 mil casas públicas.
- [ ] O PCP propõe habitação cooperativa a custos controlados.
- [ ] O PCP propõe limitar os aumentos das rendas nos novos contratos.
- [ ] O PCP propõe limitar o valor das rendas nos novos contratos.
- [ ] O PCP propõe renda apoiada com taxa de esforço de 15%.
- [ ] O PCP propõe que os bancos absorvam a subida dos juros com a CGD como referência.
- [ ] O PCP propõe o fim dos benefícios fiscais aos residentes não habituais.
- [ ] O PCP propõe o fim dos benefícios fiscais aos fundos imobiliários.
- [ ] O PCP propõe limites ao Alojamento Local.
- [ ] O PS propõe chegar a 5% de habitação pública.
- [ ] O PS propõe uma garantia pública ao crédito para jovens até aos 40 anos.
- [ ] O PS propõe rever a atualização das rendas tendo em conta os salários.
- [ ] O PS propõe alargar o Porta 65.
- [ ] O PS propõe aumentar a dedução das rendas em IRS até 800 euros.
- [ ] O PS propõe comprar casas para arrendamento acessível.
- [ ] O PS propõe exigir habitação a custos controlados nos novos licenciamentos.
- [ ] O PAN propõe crédito bonificado para os jovens.
- [ ] O PAN propõe IMT Jovem.
- [ ] O PAN propõe isenção de Imposto do Selo para os jovens.
- [ ] O PAN propõe reforço do Porta 65.
- [ ] O PAN propõe IRS mais baixo para senhorios com rendas acessíveis.
- [ ] O PAN propõe mais habitação pública acessível.
- [ ] O PAN propõe a colocação no mercado das casas devolutas a rendas condicionadas.
- [ ] O PAN propõe limitar o Alojamento Local.

relevance: 

<details><summary>Context the generator read</summary>

[Documento 1] Partido: Aliança Democrática | Tópicos: habitacao, economia, financas
  Secção: PROGRAMA ECONÓMICO DA ALIANÇA DEMOCRÁTICA > 4. Uma Economia de Futuro > 4.3. POPULAÇÃO COM FUTURO: VENCER A CRISE DEMOGRÁFICA E EXPANDIR A OFERTA HABITACIONAL > 4.3.2. HABITAÇÃO, REFORMAS PARA RESOLVER A CRISE DA HABITAÇÃO
#### 4.3.2. HABITAÇÃO, REFORMAS PARA RESOLVER A CRISE DA HABITAÇÃO  
As políticas de Habitação dos últimos anos, onde o Programa "Mais Habitação" é exemplo claro, falharam no objetivo de aumentar o acesso à habitação, e aumentaram a dificuldade de as populações, em particular os jovens, em acederem a uma habitação. Esta política limita a sua autonomia, liberdade e acesso a um projeto de vida condigno em Portugal, não lhes deixando muitas vezes alternativas à extrema precariedade habitacional, ou à emigração.  
A aposta ideológica em medidas restritivas que limitam e colidem com o direito de propriedade, que colocam uns contra outros, que limitam a iniciativa económica privada, que reduzem o investimento privado e cooperativo, e que apostam em exclusivo em promessas falhadas de Habitação Pública, deixam o Estado sozinho e incapaz de garantir um impulso ao mercado de habitação que garanta o acesso para todos.  
Ao contrário das políticas atuais, a AD defende a mobilização de toda a sociedade para um efetivo estímulo à oferta de habitações acessíveis tanto no mercado de arrendamento como de aquisição. Enquanto esta oferta estimulada em todas as direções não produz todos os seus efeitos, entende-se que medidas restritivas que visam diminuir a procura deverão ser limitadas na estrita medida do necessário para fazer face a situações de emergência social. Entendemos também que este desafio não se ganha sem a recuperação da confiança do mercado de arrendamento, sendo imperioso criar um clima de confiança e de segurança para que os alojamentos aptos para habitação sejam colocados no mercado de arrendamento. E entendemos que são precisos apoios públicos e estímulos transitórios para fazer face às situações mais prementes de carência e falta de acessibilidade habitacional.  
A resposta socialista imediata à grave crise de acessibilidade habitacional, desde há décadas e de novo nesta última governação, tem sido a do controlo administrativo de preços, por congelamento de rendas ou pela sua limitação dentro de bandas muito estritas, ignorando as regras vigentes, para todos.  
**Ora, as experiências de travões de rendas muito estritos resultaram mal em Portugal e no mundo fora, e falharam de tal forma, com aumentos de 30% das rendas dos novos contratos, que o atual Governo recuou temporariamente em 2023 na sua adoção.**  
Estas medidas não apoiam quem mais precisa. Os arrendatários já dentro do mercado poderão sentir um benefício no curto prazo, mas no médio e longo prazo são prejudicados pela quebra do investimento e da renovação e manutenção dos imóveis. Os proprietários são prejudicados por lhes ser imposta uma tarefa de redistributiva que cumpre ao Estado e à política orçamental e fiscal. Os maiores prejudicados são os que procuram casa agora, ou num futuro breve quando os seus contratos terminam, porque são confrontados com um mercado mais pequeno, resultado da fuga dos proprietários que vendem os imóveis e procuram outras formas de investimento. A medida é também socialmente injusta, tantas vezes protegendo arrendatários com rendimentos superiores aos proprietários que vêm congelada a remuneração das suas poupanças.  
A ambição da AD passa por **melhorar o acesso à habitação com vista à criação de cidades que sejam verdadeiramente sustentáveis (e que não excluam ninguém) ou seja, cidades** que (i) promovam o bem-estar de todos os seus habitantes e permitam a revitalização e não gentrificação dos bairros e comunidades, (ii) apostem na educação, na inovação e em soluções que consigam proporcionar habitação a preços acessíveis (designadamente aos jovens), (iii) permitam acolher novos residentes, (iv) promovam uma maior interação, integração social e facilidade na prestação de serviços de assistência e de cuidados continuados à população sénior, e (v) estimulem a criação de uma rede de transportes mais sustentável que desbloqueie novas áreas do território.  
Assim a política da AD baseia-se nos seguintes eixos:

---

[Documento 2] Partido: Partido Comunista Português | Tópicos: habitacao
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 4 ELEVAR A QUALIDADE DE VIDA. INVESTIR NOS SERVIÇOS PÚBLICOS, CUMPRIR AS FUNÇÕES SOCIAIS DO ESTADO > 4.6 Garantir o direito à habitação > Promover o arrendamento e proteger a habitação arrendada
##### Promover o arrendamento e proteger a habitação arrendada  
- Criando um regime especial de protecção dos inquilinos, que limite o aumento das rendas e o seu valor nos novos contratos e restrinja as situações de despejo.
- Revogando a "Lei dos despejos".
- Alterando o regime da renda apoiada, garantindo que a renda não excede uma taxa de esforço de 15% definida para o agregado, em função do seu rendimento líquido, e que as alterações de rendimento do agregado no valor da renda se repercutem de forma automática.
- Alterando o regime de renda condicionada, nomeadamente por forma a garantir que a renda é calculada sobre o valor patrimonial multiplicado por 3% e dividido por 12.
- Criando mecanismos de apoios públicos à recuperação e reabilitação de imóveis actualmente devolutos ou destinados a fins não habitacionais e que passem a ser destinados a habitação no regime da renda condicionada.
- Criando um regime simplificado de posse administrativa pelo Estado de imóveis devolutos, quando os proprietários não recorram aos mecanismos públicos para a sua recuperação, disponibilizando-os para arrendamento pelo Estado após a sua reabilitação, considerando um período mínimo que permita o ressarcimento do investimento realizado.
- Promovendo a posse administrativa, em áreas de declarada carência habitacional, de fogos devolutos que sejam propriedade de fundos imobiliários e disponibilizando-os no regime de renda apoiada.
- Reconfigurar os programas de apoio público ao arrendamento, designadamente os programas de "renda acessível", eliminando condições e critérios que estimulem ou sustentem rendas com valores especulativos e criando condições que promovam a passagem do regime de renda livre para o regime da renda apoiada ou condicionada.

---

[Documento 3] Partido: Pessoas-Animais-Natureza | Tópicos: habitacao
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por habitação para tod@s num país mais verde e justo
## Por habitação para tod@s num país mais verde e justo  
Portugal vive uma grave crise habitacional, causada pelos baixos salários, pela ausência de mecanismos que contrariem a especulação, por uma política de aposta cega no turismo que não acautelou os impactos na habitação e por uma falta de investimento na habitação pública, e que foi agravada por um contexto de subida desenfreada das taxas de juro.  
Apesar de o direito à habitação ser um direito fundamental com dignidade constitucional, a verdade é que, no Portugal de 2024, a sua materialização está longe de ser uma realidade na vida das famílias. Apesar de quase 40% do orçamento familiar ser canalizado para despesas com habitação, de ano para ano são cada vez mais as famílias, especialmente aquelas em risco de pobreza, que vivem numa sobrelotação do espaço e em pobreza energética, sendo Portugal um dos países da União Europeia onde mais famílias vivem diariamente com a incerteza de conseguir pagar a renda ou a prestação da casa.  
As rendas tiveram este ano o maior aumento dos últimos 30 anos e o aumento da prestação da casa foi de tal modo alto que 70 mil famílias já veem 50% do seu orçamento familiar alocado a despesas com crédito à habitação. Comprar ou arrendar casa em Lisboa é mais caro do que em cidades como Milão, Barcelona ou Madrid.  
Trabalhar e receber salário não é suficiente para ter uma casa para viver e em apenas 4 anos, devido à crise da habitação, o número de pessoas em situação de sem- -abrigo aumentou em 78%.  
Em apenas um ano, a renda de quartos para o alojamento estudantil aumentou 10,5% e os dados referentes a 2021 dizem-nos que existem apenas pouco mais de 15 mil camas em residências de instituições de ensino superior públicas para um total de 108 mil estudantes deslocados. Apesar de 87,9% dos/das jovens adultos/as ambicionarem adquirir casa própria, a verdade é que a idade de saída dos/das jovens adultos/as de casa, entre 2006 e 2022, aumentou de 28,3 para os 29 anos, números bem acima da média da União Europeia. A percentagem de proprietários de casa própria com menos de 25 anos reduziu-se para menos de 35% nas gerações nascidas após 1986, o que compara com valores entre 45% e 55% nas gerações nascidas nas três décadas anteriores.  
Na Legislatura que agora termina, as medidas tomadas pelo Governo foram insuficientes, com promessas de casas que nunca saíram do papel e apoios financeiros que deixam de fora 80% dos contratos de crédito habitação e 84% dos contratos de arrendamento. Contudo, o PAN conseguiu algumas avanços importantes em matéria de habitação, com a aprovação de medidas como pôr fim à cobrança da comissão bancária para o processamento da prestação, alargar a isenção de IMI para quem compra casa própria de 3 para 5 anos, aumentar em 100 euros o valor de dedução de rendas em IRS, assegurar  
a realização de um inventário do património imobiliário do Estado com aptidão para uso habitacional ou reforçar o financiamento para programas de Housing First.  
O PAN quer continuar a avançar pela causa do direito à habitação, com medidas de emergência (designadamente de âmbito fiscal) que ajudem as famílias a pagar a sua renda ou prestação ao final do mês, com o aumento do investimento público na habitação e com a criação de uma rede de habitações públicas que privilegie a reabilitação, assegurando medidas de proteção do património cultural, a eficiência ambiental e a defesa dos valores da inclusão e do espírito de comunidade.  
Neste contexto, o PAN irá:  
- Aprovar um regime de concessão de crédito bonificado à habitação para jovens para os/as jovens dos 18 aos 35 anos;  
- Assegurar uma redução de despesas adicionais na compra de casa própria a jovens dos 18 aos 35 anos, por via da atribuição de um desconto de 25% nos emolumentos das escrituras e dos atos de registo respeitantes à aquisição e à hipoteca dos imóveis adquiridos, de isenção de imposto de selo e com a criação de um regime de IMT Jovem que isente deste imposto as casas próprias com valor patrimonial tributário até 110 mil euros;  
- Rever o Programa Porta 65, de forma a aumentar os valores de renda máxima, a robustecer a respetiva dotação orçamental e a apoiar as despesas iniciais, como cauções e primeira renda e aumentar o seu valor;  
- Reduzir significativamente o IRS dos senhorios que promovam o arrendamento acessível e que atualizem os valores das rendas abaixo dos valores da inflação;  
- Apostar em programas de apoio através de benefícios fiscais aos/às proprietários/as que tenham arrendamento acessível (apartamento, quartos, coliving) para estudantes a preços abaixo da média praticada na área onde se localizem;  
- Garantir a todas as famílias a dedutibilidade de gastos com a prestação de crédito à habitação em sede de IRS;  
- Aprovar um regime transitório, com vigência limitada ao ano de 2024 e eventualmente prorrogável para 2025, de isenção de execução de penhora de bens imóveis para a satisfação de garantia real de créditos hipotecários;  
- Limitar o pagamento de remunerações acionistas e de bónus por bancos que tenham recebido apoios financeiros públicos entre 2008 e 2023, obrigando a que tais valores sejam canalizados para medidas tendentes a mitigar os efeitos do incremento dos indexantes de referência de contratos de crédito para aquisição ou construção de habitação própria permanente;  
- Dotar todos os edifícios públicos de meios de produção de energia, até 2030;  
- Garantir que as candidaturas a programas de apoio de eficiência energética do Fundo Ambiental sejam aprovadas antes da realização da despesa, ficando cativa a verba para aquela candidatura;  
- Reduzir para 6% o IVA das operações que visem assegurar a eficiência hídrica das habitações;  
- Prosseguir e aumentar o investimento de protocolos celebrados pela Segurança Social para a concretização de projetos inovadores que visem a implementação de respostas de suporte habitacional a pessoas em situação de sem-abrigo, nomeadamente no que respeita a respostas sociais de Housing First;  
- Alargar a oferta de habitação pública a preços acessíveis;  
- Reforçar o investimento na reabilitação e construção de habitação pública para arrendamento acessível, pugnando pela mobilização do património imobiliário do Estado e municipal;  
- Converter imóveis públicos devolutos em habitação para jovens, nomeadamente estudantes, podendo prolongar-se a permanência na habitação por um ano após o término dos estudos, com rendas enquadradas no valor das residências universitárias;  
- Garantir que em todos os projetos de habitação pública há sempre uma percentagem destinada a jovens e a alojamento estudantil;  
- Criar um complemento de bolsa para fazer face ao aumento de custos com o alojamento;  
- Implementar novos programas de apoio financeiro com vista à colocação de imóveis devolutos no mercado de arrendamento, com rendas condicionadas, apoiando obras de conservação e de atualização dos padrões de habitabilidade e conforto;  
- Rever os instrumentos de gestão territorial de forma a incluir e a prever a eventual limitação e suspensão de autorização de alojamentos locais e de novos estabelecimentos hoteleiros (categoria de hotéis e hotéis-apartamentos), quando se verifique estar no limiar do uso habitacional do território estudado;  
- Assegurar a criação de Gabinetes de Apoio à Habitação em todos os municípios, os quais deverão promover o levantamento das necessidades existentes, divulgar e prestar esclarecimentos à população sobre os programas de apoio existentes e assegurar a garantia da boa execução da política local de habitação;  
- Garantir que os serviços públicos que acompanham o procedimento de despejo incluem mecanismos de encaminhamento para o apoio jurídico para as pessoas em situação de vulnerabilidade social;  
- Impedir despejos, nos casos que envolvam habitação pública ou municipal, de pessoas ou famílias vulneráveis, sem que previamente não estejam definidas soluções de realojamento adequadas e dignas;  
- Criar um regime de não discriminação no acesso ao arrendamento por famílias com animais de companhia; e  
- Proteger as habitações contra desastres naturais e fenómenos sísmicos, por via da instituição de um sistema nacional de cobertura do risco de fenómenos sísmicos e de desastres naturais e da criação de um Fundo Sísmico e para Desastres Naturais.

---

[Documento 4] Partido: Partido Socialista | Tópicos: habitacao, impostos
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **2.ª MISSÃO:** UM ESTADO SOCIAL FORTE, MODERNO E INCLUSIVO > 4. Uma habitação digna para todos > 4.1.
##### 4.1.  
Nestes 50 anos do 25 de Abril devemos ir mais longe no nosso compromisso, além de continuar o caminho para erradicar a curto prazo as carências habitacionais, e garantir um efetivo direito fundamental à habitação como base fundacional do Estado social.  
Para tal, o PS propõe-se a:  
- Dar continuidade ao investimento público na requalificação, alargamento e diversificação do parque público de habitação com vista à atingir no médio prazo os 5% de parque público;  
- Lançar as bases para uma política de uma só porta de entrada nas respostas públicas de habitação, evitando a exclusão social;  
- Promover a gestão integrada do património público, de forma que responda às diferentes necessidades setoriais, em particular na habitação;  
- Apoiar a aquisição de casa própria, através de:  
- **Estado prestar uma garantia pública ao financiamento bancário nos créditos para aquisição de casa própria de pessoas até aos 40 anos que ainda não tenham nenhuma habitação em seu nome e**;
- Em caso de incumprimento do pagamento do crédito à habitação pelos beneficiários da garantia, pode o devedor, contratualizando com o Estado, manter a casa como habitação permanente, mediante o pagamento de uma renda ao Estado, que assumiria a sua posição no crédito.  
- Agravar as mais-valias em imóveis adquiridos e vendidos sem que tenham sido recuperados ou habitados;  
- Lançar novas linhas de financiamento para projetos de micro-housing, destinados a habitação temporária;  
- Reforçar as verbas destinadas à valorização do Habitat dos bairros habitacionais públicos, com especial foco na quebra de barreiras urbanísticas e valorização do espaço público e construção de equipamentos que garantam novas centralidades nestes territórios;  
- **Aumentar a despesa dedutível com arrendamento em sede de IRS em 50 € por ano até atingir os 800 €;**  
- Rever a fórmula de cálculo para atualização de rendas, incluindo a evolução dos salários nos critérios de atualização em anos com inflação superior a 2%;  
- Aumentar a abrangência do Porta 65, alterando os limites para a sua aplicação;  
- Criar um Código do Arrendamento Urbano, unificando todas as regras do arrendamento num só instrumento jurídico equilibrado e simplificado;  
- Fomentar um programa de aquisição por parte do Estado de habitações hipotecadas à banca, com garantia de arrendamento vitalício aos proprietários da mesma habitação ou integração dessas habitações em programas de arrendamento acessível;  
- Criar uma entidade fiscalizadora do arrendamento;  
- Promover um regime excecional de regularização de contratos informais, reforçando garantias de senhorios e arrendatários;  
- Criar projetos de mediação, geridos pelas câmaras municipais, entre inquilinos e senhorios;  
- Transferir progressivamente a gestão dos imóveis do IHRU para as autarquias adequando a gestão do património às realidades locais e otimizando assim a promoção de políticas públicas de habitação pelo IHRU;  
- Criar o Balcão Mais habitação permitindo a Freguesias e Municípios, à semelhança do Balcão do Cidadão;  
- Reforçar o compromisso europeu com o setor da habitação, garantindo que a política pública em matéria de habitação é entendida como serviço público, bem como a compatibilização das diretivas europeias com a necessária prioridade na resposta à crise habitacional;

---

[Documento 5] Partido: Iniciativa Liberal | Tópicos: habitacao
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 2. HABITAÇÃO AGORA
### 2. HABITAÇÃO AGORA  
O pacote Mais Habitação é a mais recente evidência de que asfixiar o mercado de arrendamento não leva nem a mais oferta de habitação, nem a rendas mais baixas. A Iniciativa Liberal irá sempre insistir na reversão de medidas que, como as deste pacote, paralisam o mercado e agravam a injustiça social. Além disso, propostas populistas como a fixação de rendas apenas levam, como está mais do que estudado, a que no longoprazo haja menos oferta e menor renovação. A resolução da crise de habitação não tem nenhuma solução mágica, implica sim uma análise séria.  
Vários são os motivos que levaram ao aumento do preço das casas nos últimos anos. Comecemos pela procura. Embora a população em Portugal tenha crescido pouco, a verdade é que está mais concentrada. Muitas pessoas saíram do Interior do país, aumentando a procura sobretudo nas áreas metropolitanas de Lisboa e do Porto.  
Além disso, a política monetária expansionista por parte do BCE, que se traduziu em taxas de juro historicamente baixas (durante cerca de sete anos tivemos uma EURIBOR negativa), levou a que as pessoas estivessem mais disponíveis para comprar casa pelo simples facto de a prestação ter baixado substancialmente. O mercado de habitação tornou-se um porto de abrigo para todos aqueles que procuravam um local onde investir o seu dinheiro aumentando a procura por casas. Assim, seria de esperar que a oferta acompanhasse este movimento ascendente da procura.  
Porém, tal não aconteceu. Se em 2002 se construíram 125 708 fogos concluídos em construções novas para habitação familiar, em 2022 só 20 156 foram construídos (resultados preliminares). São vários os motivos que explicam este valor.  
Desde logo, o desaparecimento de vários promotores e construtores e as maiores dificuldades no acesso ao crédito para os mesmos, fruto das crises de 2008 e 2011, o aumento dos custos das matérias-primas e a falta de mão de obra. Depois, pelo próprio ciclo de construção: se é verdade que uma casa não se constrói da noite para o dia, não é menos verdade que a carga burocrática no sector é muito elevada. Muito tempo decorre entre a aprovação do investimento e a conclusão da construção, passam-se vários anos em muitos casos.  
Muita da burocracia ocorre entre estes dois momentos, levando a atrasos substanciais na entrega das casas, que se traduz numa inflação de preços finais tanto por parte de quem compra como por parte de quem arrenda. Por fim, as **habitações são tributadas como bens de luxo, apesar de serem essenciais**, sendo que a carga fiscal representa cerca de 40% do custo final.  
**A Iniciativa Liberal rejeita as visões que procuram responsabilizar terceiros pela inação e pelas falhas do Estado**, a quem cabe cumprir a função social de garantir o direito à habitação – inclusive através do vasto património que detém, muito dele devoluto e que nem sequer se encontra quantificado. Por isso, a Iniciativa Liberal recusa liminarmente a diabolização de estrangeiros, pobres ou ricos, ou de setores como o alojamento local, que contribuiu fortemente para a recuperação da economia. O país tem espaço para todos. Tem é de construir para todos.  
A 046 **A Iniciativa Liberal quer criar condições para que os jovens portugueses saiam mais cedo de casa dos pais**. Dados do Eurostat mostram que, em 2022, 54,4% dos jovens dos 25 aos 34 anos em Portugal viviam em casa dos pais, o que compara com os 30,3% da média da União Europeia. A estes somam-se vários portugueses (muitas famílias monoparentais) que, não sendo jovens, não conseguem fazer face aos custos crescentes das rendas e das prestações das casas. Para todos, a Iniciativa Liberal irá criar as condições para um maior acesso à habitação.

---

[Documento 6] Partido: Aliança Democrática | Tópicos: habitacao, seguranca_social, financas
  Secção: PROGRAMA ECONÓMICO DA ALIANÇA DEMOCRÁTICA > 4. Uma Economia de Futuro > 4.3. POPULAÇÃO COM FUTURO: VENCER A CRISE DEMOGRÁFICA E EXPANDIR A OFERTA HABITACIONAL > 4.3.2. HABITAÇÃO, REFORMAS PARA RESOLVER A CRISE DA HABITAÇÃO > **Apoios à Procura dos Arrendatários Vulneráveis**
##### **Apoios à Procura dos Arrendatários Vulneráveis**  
A aposta no aumento da oferta de habitação privada e pública demora tempo a impactar decisivamente nos preços de mercado. Enquanto tal não se verifica, a AD sabe que há muitos atuais e prospetivos arrendatários a passar grandes dificuldades e que se justifica uma política pública que os acuda neste período de desequilíbrio do mercado. Contudo, a intervenção pública com vocação de estabilização deve ser através da subsidiação dos arrendatários que precisam, e não do castigo generalizado dos proprietários, que seria paga por todos no longo prazo. Assim a AD propõe:  
- a **substituição de limitações administrativas de preços por subsidiação pública aos arrendatários em situações de vulnerabilidade/necessidade efetiva** (medida em função da taxa de esforço e nível de rendimento);
- Manutenção, enquanto o mercado não estabiliza, de **subsídio de renda dinâmico que garante uma comparticipação a todas as famílias com taxas de esforço elevadas**. Ao contrário de limitar o apoio à existência de contratos a março de 2022 tal como no apoio às rendas atual, a AT verificará o universo de contratos frequentemente, e atribuirá uma comparticipação começando pelas famílias com maiores taxas de esforço;
- Reformulação do programa Porta 65 por forma a chegar a mais jovens sem acesso ao mercado de arrendamento, e ser um efetivo apoio. Hoje, o programa exige aos jovens com pouca liquidez que assumam o risco de fazer um contrato de arrendamento para se candidatarem ao Porta 65 e eventualmente receberem o apoio. Este programa deve ter como ponto de partida a garantia pública de atribuição à família do apoio, que depois procurará uma habitação compatível, e verá o apoio expresso na comparticipação de rendas e eventual empréstimo de cauções.

---

[Documento 7] Partido: Bloco de Esquerda | Tópicos: habitacao, economia, impostos
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 1 Habitação
## 1 Habitação  
A estratégia de crescimento económico assente no turismo e no imobiliário provocou uma crise na habitação.  
Para baixar os preços das casas, é necessária a intervenção do banco público na quebra dos juros, a fixação de tetos para baixar as rendas, a proibição da venda de casas a não residentes e a limitação do seu desvio para alojamento turístico. O Bloco de Esquerda detalha ainda as medidas de uma reforma fiscal que proteja a habitação.

---

[Documento 8] Partido: Bloco de Esquerda | Tópicos: habitacao, impostos
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 1 Habitação > 1.2 Os responsáveis pela crise na habitação
### 1.2 Os responsáveis pela crise na habitação  
À Direita tenta-se proteger os especuladores e argumenta-se que a subida de preços se deve à falta de construção. Tudo se resumiria, dizem, a uma questão de oferta e de procura. Este argumento não passa de um ato de fé desmentido pela realidade. Tanto o parque habitacional como o número de famílias a residir em Portugal pouco se alteraram nas últimas décadas. Na verdade, nas grandes cidades, como o Porto e Lisboa, a população regrediu continuamente entre 2001 e 2021.  
A escalada histórica dos preços da habitação foi potenciada, primeiro, pelo período de taxas de juro historicamente baixas que tornaram o imobiliário num ativo atrativo pela sua rentabilidade e, depois, pelo processo inflacionista, que aumentou os custos do endividamento. No entanto, se estas são causas transversais a vários países, há elementos que justificam a particular gravidade da situação em Portugal: a promoção do turismo de massas e do turismo habitacional de luxo, com o regime do Residente Não Habitual ou os Vistos Gold; a liberalização do mercado do arrendamento; a proliferação desenfreada do Alojamento Local; ou os incentivos fiscais aos fundos de investimento imobiliário, contribuíram ativamente para fazer subir os preços das casas.  
GRÁFICO 5  
**Evolução do número de dormidas: Porto, Lisboa, Algarve e Portugal**  
Cada vez mais detentores de capital, sem qualquer intenção de algum dia virem viver para Portugal, compram e vendem as nossas casas. Usam-nas como ativos financeiros. O seu único propósito é inflacionar os preços e vender com lucro.  
GRÁFICO 6  
Investimento direto estrangeiro imobiliário em Portugal  
Fonte: Banco de Portugal  
—— Investimento Direto Estrangeiro (IDE) - Atividades imobiliárias Pós-Trimestre-M€)  
Depois de criada a tempestade perfeita, o PS recusou-se a aplicar qualquer medida estrutural capaz de alterar as condições do mercado imobiliário. Os benefícios fiscais ao arrendamento mostraram-se ineficazes e os apoios às rendas, embora necessários, se não forem acompanhados de medidas para baixar os preços, têm como consequência retroalimentar o processo de inflação imobiliária. É uma abordagem tão liberal quanto a dos liberais.  
Como a realidade mostra, as razões liberais não explicam a escalada dos preços, pelo que as suas políticas também não resolverão o problema. São precisas medidas capazes de combater a especulação, baixar os preços, devolver a habitação às pessoas e aumentar o parque público habitacional. O controle de rendas é uma medida de proteção da habitação já aplicada ou em processo de aplicação em muitos outros países.

---

[Documento 9] Partido: Partido Comunista Português | Tópicos: habitacao, impostos
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 4 ELEVAR A QUALIDADE DE VIDA. INVESTIR NOS SERVIÇOS PÚBLICOS, CUMPRIR AS FUNÇÕES SOCIAIS DO ESTADO > 4.6 Garantir o direito à habitação > Pôr fim aos privilégios concedidos pelas políticas liberais na habitação
##### Pôr fim aos privilégios concedidos pelas políticas liberais na habitação  
- Eliminar o regime fiscal de privilégio aos residentes não habituais, bem como todos os benefícios fiscais aos fundos imobiliários e outros instrumentos similares que estimulam a especulação, penalizando fiscalmente os rendimentos especulativos.
- Fixar condições que impeçam a utilização especulativa, para efeitos de venda ou arrendamento, de habitações construídas ou recuperadas com apoios públicos ou benefícios fiscais, considerando designadamente a aplicação do regime da renda condicionada, a limitação do subarrendamento ou a proibição de revenda a outra entidade diferente do próprio Estado.
- Limitar a aquisição de habitações por fundos imobiliários.
- Limitar, em áreas de declarada carência habitacional, a mobilização de habitações para uso de Alojamento Local.

---

[Documento 10] Partido: LIVRE | Tópicos: habitacao, impostos
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > **Habitação e Espaço Público** > Por isso defendemos: > **Regular o valor da propriedade urbana**
#### **Regular o valor da propriedade urbana**  
13. **Estabelecer limites máximos no valor de renda**, durante pelo menos cinco anos, nos imóveis habitacionais de proprietários que recebem financiamento de programas promovidos pelo Estado (como exemplo, o IFRU - Instrumento Financeiro para a Reabilitação e Revitalização Urbanas) para a realização de obras em imóveis que não servem para habitação própria.  
14. **Compatibilizar os rendimentos médios e baixos com o valor do arrendamento**, estabelecendo que os novos contratos de arrendamento não excedem uma majoração de 30% dos limites gerais de preço de renda por tipologia previstos em portaria.  
15. **Controlar a especulação imobiliária**, ao:  
- promover o ajustamento do mercado imobiliário ao diminuir os valores de venda através do aumento do imposto sobre as mais valias, considerando 100% do valor para englobamento sobre os ganhos derivados da transmissão onerosa de imóveis no momento da venda de imobiliário que não seja primeira habitação;
- terminar com os Vistos _Gold_ em todo o território nacional, os benefícios fiscais previstos no Estatuto de residente não habitual e de nómadas digitais, assim como promover uma maior fiscalização aos meios usados para o investimento estrangeiro.  
16. **Rever o Estatuto dos Benefícios Fiscais para os imóveis**, através da inventariação e estudo dos organismos de investimento coletivo imobiliário e o seu impacto no mercado habitacional, assim como eliminar ou reduzir os benefícios que são atribuídos a organizações que tenham finalidades de especulação imobiliária e fomentar a transição de frações habitacionais para o arrendamento acessível ao restringir a isenção de IRC aos fundos e sociedades de investimento imobiliário que disponibilizem 30% dos seus bens imóveis no Programa de Apoio ao Arrendamento.  
17. **Reformular o cálculo do IMI para reduzir a carga fiscal sobre habitação permanente e agravar a dos imóveis devolutos que não cumprem a função social da habitação**, ao:  
- alargar os critérios para isenção do pagamento de IMI no caso de habitação permanente (aumento dos valores patrimoniais para 80 000 euros e dos rendimentos de referência para 30 000 euros anuais) ou de imóveis com contratos de arrendamento de longa duração;
- possibilitar o aumento do atual agravamento do IMI para imóveis devolutos, degradados ou em ruína e associar, em casos extremos de irregularidade e degradação urbanística grave e prolongada no tempo, este enquadramento fiscal ao uso dos instrumentos adequados previstos na Lei de bases da Habitação, designadamente, a posse administrativa do imóvel.  
18. **Implementar quotas de habitação acessível em empreendimentos urbanísticos de grande dimensão**, contribuindo para uma maior e mais rápida disponibilidade de frações a custo acessível e construção de tecidos urbanos diversos. A cedência de frações para gestão municipal no âmbito para habitação acessível pressupõe a redução do pagamento de taxas inerentes à operação urbanística. Pretende-se que nos investimentos com mais de seis frações habitacionais pelo menos 20% sejam destinados à habitação acessível. A diversidade tipológica das frações para arrendamento acessível deve corresponder, proporcionalmente, à diversidade de tipologias do edificado construído. O projeto deve garantir a igualdade no acesso ao edificado e na utilização dos serviços comuns projetados, impedindo a criação de acessos secundários para os residentes em frações de renda acessível e a imposição de limitações, explícitas ou implícitas, no acesso e utilização dos serviços e espaços comuns do empreendimento.  
19. **Garantir transparência no apoio à habitação**, substituindo os três regimes especiais de fixação de renda (renda apoiada, condicionada e acessível) por um único com critérios que permitam a atribuição de habitação pública de forma mais transversal e universal às pessoas.  
20. **Rever o quadro legal para a acessibilidade** a espaços públicos, equipamentos coletivos e edifícios públicos e habitacionais resolvendo contradições entre diplomas de diferentes áreas técnicas e alargando a sua aplicação. As barreiras arquitectónicas devem ser eliminadas para que seja garantida a igualdade de oportunidades no acesso a instalações públicas e privadas, tendo em conta os problemas de aplicação do atual regime jurídico à reabilitação de imóveis, muitos deles habitacionais, e que no caso do alojamento estudantil em 2019 somente 2% permitiam a acessibilidade de estudantes com mobilidade reduzida ou com deficiência como a cegueira ou surdez.  
21. **Rever a legislação que regula a atividade de mediação imobiliária e da atividade de gestão e administração de condomínios**. Regular de acordo com a transformação significativa das empresas de mediação imobiliária e de gestão e administração de condomínios, de forma a introduzir exigências formativas aos profissionais e maior transparência e justiça fiscal na contratualização dos serviços e tributação do pagamento. A revisão coordenada de vários diplomas do setor imobiliário deve procurar melhorar os serviços prestados. Esta revisão deve contar com a participação das várias organizações do setor e a coordenação do Instituto dos Mercados Públicos, do Imobiliário e da Construção, I.P. (IMPIC, I.P.).

---

[Documento 11] Partido: CHEGA | Tópicos: habitacao, impostos, jovens
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > V CAPÍTULO ASSEGURAR HABITAÇÃO DIGNA. COMO?
## V CAPÍTULO ASSEGURAR HABITAÇÃO DIGNA. COMO?  
**A**habitação em Portugal assume contornos preo-cupantes, marcados pela escassez de soluções eficazes e pelo desalinhamento com os princípios constitucionais. É imperativo definir uma abordagem pragmática e consistente, que equilibre a oferta com a procura, um equilíbrio que deve ser transversal às diferentes nuances do parque imobiliário.  
Contudo, ao longo dos anos, tem-se assistido a uma desconsideração sistemática dos princípios constitucionais, com governos predominantemente socialistas a adoptarem medidas que resultaram no agravamento da crise habitacional. Programas como "1º Direito" e "Arrendamento Acessível" não só revelaram adesão muito limitada como, por vezes, foram desajustados da realidade e das necessidades reais do mercado.  
Note-se que estes são apenas alguns exemplos, entre muitos outros, de iniciativa do Governo ou das autarquias, ou em conjunto, anunciados com pompa e circunstância, sem que tenham resolvido ou sequer atenuado o problema da habitação.  
A Constituição da República Portuguesa, ao mencionar a "construção privada", salienta imediatamente que esta deve estar "subordinada ao interesse geral". Este detalhe abre espaço para propostas inadequadas de partidos de esquerda e extrema-esquerda, que sugerem medidas que obrigam proprietários a colocar os imóveis no mercado, coercivamente. É uma das medidas mais criticadas do "Programa Mais Habitação", que pretende proceder ao arrendamento forçado de imóveis privados. Os efeitos contrários aos pretendidos já se fazem notar ao minar a segurança e confiança de potenciais novos investidores.  
Esta abordagem coerciva cria um ambiente de incerteza e desconfiança no sector imobiliário, desencoraja investidores a participarem activamente no mercado de arrendamento e, por isso, é prioritário para o CHEGA revogá-la de imediato. Este é só mais um exemplo de um ambiente legal imprevisível e instável, que afasta potenciais investidores. Investir no sector imobiliário implica um compromisso a longo prazo e, por consequência, regras que sejam favoráveis, sólidas, consistentes e duradouras, que permitam rentabilidade e gestão eficientes.  
O Estado não deve interferir na propriedade privada, mas desenhar políticas que estimulem o investimento público e privado, criar incentivos fiscais, simplificar processos burocráticos e promover a segurança jurídica. Com base na lógica de mercado "quanto maior a oferta, mais baixo será o valor" pode e deve ser promovida mais oferta, com base no cálculo do índice de disponibilidade habitacional, este composto por vários indicadores, por região, que relaciona procura e oferta de habitação, disponibilidade de solo, densidade populacional e infra-estruturas de suporte.  
O CHEGA acredita que o caminho reside numa reforma substancial das políticas para responder às necessidades das famílias e promover um mercado habitacional mais dinâmico e acessível. O mercado imobiliário português enfrenta uma crise acentuada, especialmente nas grandes cidades**<sup>1</sup>** , impactando desproporcionalmente os jovens adultos. De acordo com os dados do INE, entre 2013 e 2022 construíram-se 150.000 alojamentos, menos 480.000 que na década anterior.  
O aumento dos preços das casas a partir de 2017 agravou a acessibilidade, tanto na aquisição como no arrendamento, especialmente nas áreas metropolitanas de Lisboa e Porto. As famílias enfrentam actualmente a necessidade de dedicar uma fatia muito significativa do seu rendimento para comprar ou arrendar casa. A instabilidade no emprego, os baixos salários e condições restritivas por parte da Banca, condicionam o acesso ao crédito e, por consequência, à aquisição de habitação.  
Actualmente, um jovem que deseje comprar ou arrendar uma casa precisa estar muito bem estabelecido profissionalmente. Por este motivo, Portugal ocupa o 2º lugar no ranking dos países onde quase 80% dos jovens adultos ainda vive com os pais, muito acima da média europeia de aproximadamente 50%**<sup>2</sup>**.  
Na última década, observou-se uma diminuição significativa na construção de novas habitações em Portugal, atribuível em parte à priorização da reabilitação urbana e às restrições financeiras e operacionais no sector da construção, acentuada por diversos elementos relacionados com o ordenamento fiscal e regulatório.  
Os dados do INE**<sup>3</sup>** demonstram que os prazos médios de  
**<sup>1</sup>** Cf.-FFMS-crise-da-habitacao-nas-grandes-cidades-uma-analise  
**<sup>2</sup>** OCDE, Jovens adultos: 20-29 anos. Últimos dados disponíveis de 2020, com União Europeia e OCDE calculados como média simples dos países para os quais existem dados.  
conclusão de obras de reconstrução e construção nova são de 23 meses. Algumas das razões são a enorme burocracia nos processos de desenvolvimento imobiliário, a instabilidade na regulação com frequentes mudanças legais, a elevada carga tributária, a exigência de capitais próprios substanciais, taxas de juro crescentes desde o final de 2022 e a imprevisibilidade nos processos de licenciamento devido à multiplicidade de normas e interpretações.  
Em bom rigor, a situação habitacional em Portugal atingiu em 2022 e 2023 uma gravidade alarmante, um cenário onde famílias trabalhadoras e esforçadas se viram obrigadas a habitar em condições precárias, inclusive recorrendo a tendas nas ruas.  
O fracasso das políticas socialistas nesta área é evidente, com casos de pais que perdem a guarda de filhos devido à incapacidade em suportar as rendas, reflectindo uma falha notável do governo socialista na coesão e justiça social.  
A política de portas abertas, por sua vez, exacerbou o problema, resultando em habitações sobrelotadas e elevou de maneira desproporcional os custos médios no mercado. Situações de subarrendamento ou não contratualizadas acontecem também ao nível municipal. É imperativo que o Estado exerça uma intervenção efectiva na supervisão contínua dos contratos de arrendamento de habitação social. Esta medida torna-se urgente perante conhecidas situações em que algumas famílias acedem a mais do que um alojamento social, distribuídos por distintos municípios. Estas práticas não só configuram uma acção fraudulenta, mas também comprometem a disponibilidade de habitações para aquelas famílias que genuinamente necessitam. Sem fiscalização rigorosa não se assegura eficácia e equidade dos programas habitacionais, nem a distribuição justa e eficiente de recursos habitacionais.  
Perante este cenário crítico é imperativo adoptar medidas políticas abrangentes na escala e transversais, algumas de emergência, outras de curto, médio e longo prazo, para assegurar o direito à habitação, numa abordagem integrada.

---

[Documento 12] Partido: Partido Socialista | Tópicos: habitacao, jovens
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **2.ª MISSÃO:** UM ESTADO SOCIAL FORTE, MODERNO E INCLUSIVO > 4. Uma habitação digna para todos
#### 4. Uma habitação digna para todos  
A importância da habitação, para a vida de cada um, mas também para a qualidade da nossa vida coletiva é demonstrada, na evidência que a casa é mais do que quatro paredes e um teto. É a centralidade do projeto de vida de cada pessoa e de cada família. É o local onde nos organizamos e nos preparamos para os desafios de todos os dias. É o lugar onde começa a liberdade e o garante da nossa dignidade. É a partir dela que abraçamos um projeto de realização pessoal e é também alicerce para a construção de uma sociedade mais justa, igual e coesa. **É o nosso primeiro direito.**  
Apesar disso, só neste último ciclo, com os governos do PS, começámos a alterar a visão política da habitação como bem financeiro para a habitação como bem essencial e parte fundamental do estado social. Conseguimos por fim lançar as bases para a construção um parque publico robusto que garanta, coletivamente, uma proteção contra os excessos do mercado. Um parque habitacional que responda não só aos mais carenciados, mas também a toda classe média, em especial aos mais jovens. Este tem de ser um desígnio duradouro assumido num consenso alargado. Este aparente consenso não significa unanimidade de pensamento em matéria de habitação. Só um governo do Partido Socialista procurará que o Direito à Habitação seja também um direito de escolha, o reconhecer de que todos os cidadãos devem ter uma habitação digna, onde quer que escolham viver.  
Também não podemos aceitar que este aparente consenso seja uma cortina de fumo, aceitando que todos, especialmente os mais expostos à crise da habitação, mais pobres, mais jovens e mais velhos, pagaremos os custos de ajustamento do tempo necessário à construção do parque publico. Portugal tem um dos mercados mais liberalizados da Europa em matéria de habitação e temos de criar um verdadeiro quadro de regulação desse mercado, garantindo assim maior justiça e equilíbrio para todas as partes.

---

[Documento 13] Partido: LIVRE | Tópicos: habitacao, economia
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > **Habitação e Espaço Público**
## **Habitação e Espaço Público**  
O acesso universal à habitação não pode ser só um direito constitucional de que nos orgulhamos. A habitação é um bem essencial a uma vida digna e compreende o acesso à cidade e ao espaço edificado em geral.  
Nos últimos anos verificou-se, simultaneamente, o agravamento das dificuldades de acesso à habitação a valores acessíveis, problema que atinge a população portuguesa de forma cada vez mais abrangente, e a desvalorização das relações entre a habitação, o espaço público, a cidade, a estrutura urbana e a qualidade ambiental. Fatores que prejudicam a coesão territorial e a sustentabilidade ambiental, social e económica, cristalizando desigualdades espaciais, traduzidas em assimetrias de valor fundiário e de capital simbólico social. As questões da habitação e do ordenamento do território carecem de uma visão sistémica alargada.  
A habitação é um direito fundamental para o cumprimento dos outros direitos essenciais a uma vida saudável e digna, do saneamento básico à educação. Contudo, a conjuntura económica nacional agravouse e o aumento do custo da habitação, quer do valor do arrendamento como o da aquisição, não foi acompanhado pelo aumento dos rendimentos das e dos cidadãos e dos agregados familiares. Neste contexto, segundo o INE, cerca de dois terços da despesa média das famílias são encargos associados à habitação, valores bem acima das taxas de esforço recomendadas. As crescentes dificuldades de acesso à habitação são também agravadas por um quadro económico marcado pelo aumento da inflação, de 4,3% em 2023, das taxas diretoras e do custo de vida de forma transversal. Ainda assim, 2024 começará com o maior aumento do valor das rendas dos últimos 30 anos (6,94%), com apenas cerca de 2% dos alojamentos como habitação pública e sem medidas que contrariem a constante subida do custo da habitação.  
Existe uma divergência cada vez maior entre os rendimentos baixos e médios nacionais e o valor da propriedade imobiliária, que afetaram inicialmente as populações mais vulneráveis, expulsas dos centros urbanos através de dinâmicas de gentrificação, mas que hoje também impedem as pessoas e famílias com rendimentos médios do direito à habitação e à cidade. Este quadro favorece formas de segregação social e expansão urbana que julgávamos ultrapassadas, constituindo um retrocesso ambiental, urbanístico e cívico que importa contrariar. A Habitação tem de ser um direito que efetivamente faz parte dos objetivos legislativos, técnicos e governativos da próxima legislatura. A dependência económica que o país tem em relação ao investimento estrangeiro nas áreas do imobiliário e do turismo, fomentado por um enquadramento legislativo criado para o efeito, é acompanhada de diversas formas de especulação imobiliária que estão a alterar radicalmente as nossas casas, ruas e bairros.  
Apesar do pacote legislativo Mais Habitação e do investimento do Plano de Recuperação e Resiliência (PRR) que prevê um valor de 2700 milhões de euros para a construção de 32 mil fogos, apenas cerca de 18 mil estão em desenvolvimento. Número muito baixo num contexto em que temos um problema grave de habitação, de qualificação dos espaços públicos e a sua integração nas redes urbanas de infraestruturas e serviços de primeira necessidade caracterizada por assimetrias significativas entre as zonas centrais das cidades e os espaços periféricos onde vive a maior parte da população.  
É preciso investir em mais Habitação Pública para além do PRR. Por isso, defendemos que toda a habitação do Estado é Habitação Pública e que habitação não é só o espaço privado mas todas as dimensões urbanas, infraestruturais e de serviços que contribuem para uma vida segura e integrada, de acordo com a noção de habitat consagrada na Lei de Bases da Habitação. Assim, persistem diferentes carências na garantia de igualdade de acesso à habitação e, como tal, é necessário definir várias frentes de ação. Propomos medidas organizadas sobre os seguintes eixos: Proteger e alargar o direito à habitação, apoiar na emergência, regular o valor da propriedade urbana e desenvolver modelos ecológicos para o habitar e para o espaço público.

---

[Documento 14] Partido: Iniciativa Liberal | Tópicos: habitacao, impostos
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 2. HABITAÇÃO AGORA > 2.3. Recuperar confiança
#### 2.3. Recuperar confiança  
A Iniciativa Liberal quer devolver a confiança aos proprietários para colocarem mais casas no mercado de arrendamento. É natural que quem tenha propriedade a queira pôr a render, mas em Portugal são fortes os incentivos para contrariar esta tendência. A morosidade dos tribunais e a imprevisibilidade do legislador que deixa os proprietários cada vez mais desprotegidos no exercício dos seus direitos são apenas alguns exemplos. Nunca se sabe quando é que o Governo pode alterar as regras que regem os contratos de arrendamento. Veja-se o limite ao aumento de rendas que houve para 2023, ou o aumento da duração dos contratos em vigor de um para três anos a partir de 2019, independentemente do que tenha sido acordado entre as partes.  
Este discurso maniqueísta da esquerda que insiste em retratar os senhorios como vilões é uma falsa narrativa que é, acima de tudo, socialmente injusta. De acordo com os últimos censos, 70% das famílias em Portugal vivem em casa própria, das quais cerca de 32% têm segundas habitações. **Num país com falta de oportunidades para subir na vida pelo trabalho, o arrendamento é uma forma de complementar** **os rendimentos de muitas famílias**. Muitos idosos dependem da renda de uma casa para conseguir pagar despesas de alimentação, comprar medicamentos e financiar os cuidados que precisam, mantendo uma existência digna e confortável até ao fim da vida. Não são estas as pessoas que devem suportar o custo das políticas sociais para as quais já contribuem com os impostos que subtraem ao seu rendimento. É o Estado que tem a responsabilidade de dar apoio aos que mais sentem dificuldade em encontrar habitação entre outras necessidades essenciais.  
**Um mercado de arrendamento mais livre, não só será mais justo para com os proprietários como irá beneficiar quem atualmente não encontra casa** para arrendar. A existência de rendas congeladas, por exemplo, é mais um fator de distorção do equilíbrio tendencial entre a procura e oferta que decorreria do normal funcionamento do mercado. Isto prejudica uns ao proteger injusta, cega e desproporcionalmente outros. Num bairro com muita procura, por cada casa com renda congelada que exista, maior é a competição pelas casas que estão no mercado livre elevando as rendas nessas casas disponíveis. Os jovens, que hoje são dos mais prejudicados ao tentarem sair de casa dos pais por causa dos baixos salários que recebem, seriam dos primeiros a beneficiar dum mercado de arrendamento mais livre e mais justo para todos.  
**Redução do imposto sobre as rendas**  
**Baixar a taxa autónoma sobre os rendimentos prediais** de arrendamento de 25%, proposta no pacote Mais Habitação do Governo, **para 14,5%** (contratos com duração até cinco anos), reduzindo progressivamente **até um mínimo de 0,5%** (contratos com duração superior a 20 anos), conforme referido no Capítulo da Reforma Fiscal.  
| Duração do<br>contrato | Regime atual | Proposta da IL |
| ---------------------- | ------------ | -------------- |
| Até 5 anos             | 25%          | 14,5%          |
| Entre<br>5 e 10 anos   | 15%          | 9,5%           |
| Entre<br>10 e 20 anos  | 10%          | 4,5%           |
| Acima<br>de 20 anos    | 5%           | 0,5%           |  
050 Baixar a carga fiscal sobre as rendas ajuda inquilinos e senhorios. Com a proposta da Iniciativa Liberal um inquilino pagaria menos 81,87€ para uma renda em que o senhorio recebe 500€.  
**Eliminar quaisquer formas de arrendamento forçado previstas no pacote Mais Habitação**  
Qualquer ataque à propriedade privada será combatido pela Iniciativa Liberal. Um Estado que não tem noção de quantos imóveis tem na sua posse e como tal não pode pô-los ao dispor de quem precisa, não se pode arrogar no direito de obrigar os proprietários a cumprir a função social que ele não é competente o suficiente para cumprir.  
**Eliminar o congelamento de rendas**  
Alterar o Novo Regime de Arrendamento Urbano (NRAU) para **acabar com o congelamento de rendas ainda em vigor**, cabendo ao Estado o apoio a pessoas em situação de carência económica. Quem não tem meios para pagar continuará a ter apoio social, mas não são os proprietários quem tem de cumprir a função social. Essa cabe ao Estado com o dinheiro dos impostos.  
**Aumentar a celeridade judicial nos processos de arrendamento e sucessões de imóveis**  
Reverter a medida do pacote Mais Habitação que esvazia a ação do Balcão Nacional de Arrendamento nos contratos que chegaram ao fim sem contestação do arrendatário. Os proprietários não conseguem fazer valer os seus direitos num sistema lento que não funciona. Tal como identificamos na secção de justiça deste programa eleitoral, os processos que visam imóveis devem ser uma prioridade para o mercado de habitação funcionar tanto a favor dos arrendatários como dos senhorios.  
Se é verdade que a reforma da justiça pode levar tempo, também é verdade que é possível dar prioridade a áreas específicas como é o caso do direito laboral, uma das áreas da justiça onde há maior celeridade processual. Se tanto o direito à propriedade como o direito à habitação estão consagrados como fundamentais na Constituição da República, então a resolução de litígios com eles relacionados também deve ser uma prioridade do sistema, especialmente quando há uma crise que dificulta o exercício de ambos os direitos.

---

[Documento 15] Partido: Partido Comunista Português | Tópicos: habitacao, jovens
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 4 ELEVAR A QUALIDADE DE VIDA. INVESTIR NOS SERVIÇOS PÚBLICOS, CUMPRIR AS FUNÇÕES SOCIAIS DO ESTADO > 4.6 Garantir o direito à habitação
#### 4.6 Garantir o direito à habitação  
A Constituição inscreve como obrigação do Estado garantir, a todos os cidadãos, o direito a uma habitação adequada para si e para a sua família. As políticas das últimas décadas, com a retirada quase completa da intervenção pública no sector e a sua extensa liberalização, transformaram cada vez mais um direito fundamental numa mercadoria ao dispor da especulação e da maximização do lucro.  
O aumento do preço das casas em resultado da especulação, os sucessivos aumentos das taxas de juro pelo BCE propiciando a multiplicação dos lucros da banca, a manutenção da "Lei dos Despejos"e o aumento significativo das rendas fizeram aumentar o peso dos custos com a habitação no orçamento familiar para cerca de 40%, o dobro do que se registava em 2000, agravado pela perda geral de poder de compra.  
A habitação é cada vez mais inacessível para muitos indivíduos e famílias, obrigados a trocarem a sua casa por um quarto, a regressarem a casa dos pais ou a viver em habitações precárias ou na rua. É inatingível para a maioria dos jovens, particularmente condicionados pela precariedade e pelos baixos salários. É um factor decisivo de dificuldade para a fixação de profissionais em muitos serviços essenciais como o SNS, a Escola Pública ou as Forças de Segurança. É factor de condicionamento do direito à educação para centenas de milhar de estudantes deslocados do ensino superior.  
A acção de sucessivos governos, incluindo o Governo do PS, incentivou a intervenção especulativa de fundos de investimento e grandes proprietários e estrangeiros não residentes desprotegendo as pessoas e o seu direito à habitação. O Governo permitiu que a banca multiplicasse os seus lucros à custa das prestações de habitação, seja nos juros, nas taxas, comissões e outros encargos. Decretou sucessivos aumentos de rendas dos contratos mais antigos – 7% em 2024 – e aceitou as rendas especulativas em novos contratos. Tomou medidas para financiar a especulação imobiliária e os lucros da banca. Rejeitou uma maior protecção dos inquilinos relativamente aos despejos, designadamente na sua morada de família. Adiou investimento em habitação pública, praticamente inexistente, por recusar inclui-lo no Orçamento do Estado, remetendo-o quase exclusivamente para o PRR e alienando a sua responsabilidade para as autarquias locais.

---

[Documento 16] Partido: CHEGA | Tópicos: habitacao, impostos, jovens
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > V CAPÍTULO O QUE JÁ FIZEMOS PARA ASSEGURAR HABITAÇÃO DIGNA
## V CAPÍTULO O QUE JÁ FIZEMOS PARA ASSEGURAR HABITAÇÃO DIGNA  
**PROJECTO DE LEI 567/XV/1 (CH)**  
Recomenda ao Governo que identifique o património imobiliário habitacional do Estado que está a ser indevidamente utilizado, alvo de fraude ou a necessitar de obras de reabilitação  
**PROJECTO DE LEI 873/XV/1 (CH)**  
Estabelece a contribuição de solidariedade temporária sobre o sector bancário, destinada ao financiamento de programas de apoio à habitação  
**PROJECTO DE LEI 673/XV/1 (CH)**  
Reforça os incentivos à estabilidade nos contratos de arrendamento para habitação própria e permanente por via da redução das taxas de tributação autónoma  
**PROJECTO DE LEI 470/XV/1 (CH)**  
Cria um programa de apoio aos jovens para compra de habitação própria e permanente  
**PROJECTO DE LEI 299/XV/1 (CH)**  
Estabelece medidas de apoio e protecção dos particulares, por motivo do aumento das taxas de juros aplicáveis aos contratos de financiamento à aquisição de habitação própria e permanente  
**REJEITADO**  
**CONTRA** Partido Socialista, IL, PCP, BE, PAN, L **ABSTENÇÃO** --- **FAVOR** PSD, CHEGA  
**REJEITADO**  
**CONTRA** Partido Socialista, PSD, IL **ABSTENÇÃO** PCP, PAN, L **FAVOR** CHEGA, BE  
**REJEITADO**  
**CONTRA** Partido Socialista, PCP, BE, L **ABSTENÇÃO** PSD **FAVOR** CHEGA, IL, PAN  
**REJEITADO**  
**CONTRA** Partido Socialista, IL, PCP **ABSTENÇÃO** BE, L **FAVOR** PSD, CHEGA  
**REJEITADO**  
**CONTRA** Partido Socialista, PSD, IL **ABSTENÇÃO** PCP, L **FAVOR** CHEGA, BE, PAN

---

[Documento 17] Partido: Partido Comunista Português | Tópicos: habitacao, educacao, jovens
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 4 ELEVAR A QUALIDADE DE VIDA. INVESTIR NOS SERVIÇOS PÚBLICOS, CUMPRIR AS FUNÇÕES SOCIAIS DO ESTADO > 4.6 Garantir o direito à habitação > Alargar a oferta de habitação pública e de habitação a custos controlados
##### Alargar a oferta de habitação pública e de habitação a custos controlados  
- Alargar a oferta pública de habitação através da mobilização imediata do património público para fins habitacionais, destinado a diversas camadas da população, e de um investimento público reforçado e contínuo na construção de habitação pública financiado a partir do Orçamento do Estado (50.000 fogos).
- Apoiar o movimento cooperativo, o sector social e mutualista para a construção de um parque habitacional de qualidade, a custos controlados, destinado ao regime de renda apoiada ou condicionada, e à recuperação e reabilitação de habitação, auto construção, auto reabilitação ou acabamento de habitações;
- Criar um programa de residências universitárias com construção a custos controlados, de acesso gratuito.
- Reconfigurar o IHRU como organismo público central promotor de habitação pública e dinamizador das políticas de construção e reabilitação urbana, para a garantia do direito constitucional à habitação, dotando-o dos necessários meios e equipas técnicas com capacidade de elaboração de projecto, planeamento, programação e execução dos investimentos.  
- Requalificar o parque habitacional de propriedade do IHRU e garantir condições de habitabilidade e de conforto.
- Assegurar investimento público da Administração Central na área da habitação, tendo como referência o investimento anual de 1% do PIB, em termos médios, ao longo da legislatura.

---

[Documento 18] Partido: Aliança Democrática | Tópicos: habitacao, justica, impostos
  Secção: PROGRAMA ECONÓMICO DA ALIANÇA DEMOCRÁTICA > 4. Uma Economia de Futuro > 4.3. POPULAÇÃO COM FUTURO: VENCER A CRISE DEMOGRÁFICA E EXPANDIR A OFERTA HABITACIONAL > 4.3.2. HABITAÇÃO, REFORMAS PARA RESOLVER A CRISE DA HABITAÇÃO > **Estabilidade e confiança no mercado de arrendamento**
##### **Estabilidade e confiança no mercado de arrendamento**  
A Estabilidade e Segurança no Arrendamento Habitacional, cujas opções políticas do PS desincentivaram, levou a subidas de 30% de rendas nos novos contratos, proprietários para o alojamento local, para contratos de curta duração, que podem ser mais facilmente mudados, ou à venda dos imóveis. Assim importa, retomar políticas que invertam este caminho. Neste contexto a AD defende:  
- Avaliação das contra-reformas introduzidas em 8 anos de governação socialista ao nível do arrendamento e obras, em particular as relativas à duração e renovações (especialmente as de 2019) – avaliação e revisão legislativa subsequente em conformidade com os resultados;
- Revisão e aceleração dos mecanismos de rápida resolução de litígios em caso de incumprimento dos contratos de arrendamento (designadamente através do reforço e qualificação do Balcão Nacional de Arrendamento; recurso a meios extrajudiciais e julgados de paz; mecanismos de tutela urgente para situações excecionais e urgentes);
- Avaliação do insucesso prático do mecanismo de seguro de renda previsto na lei desde 2013 e implementado deficientemente só em 2019. Eventual revisão do enquadramento e criação de incentivos à adoção, incluindo dedutibilidade do prémio de seguro ao rendimento tributável do arrendamento. Ponderar a sua articulação por substituição dos mecanismos de fiadores e rendas antecipadas.

---

[Documento 19] Partido: Bloco de Esquerda | Tópicos: habitacao
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 1 Habitação > 1.3 Propostas para baixar os preços das casas > Controlar as rendas
### 1.3 Propostas para baixar os preços das casas  
#### Controlar as rendas  
Criar tetos máximos para rendas inferiores aos valores definidos na Portaria n.<sup>o</sup> 277-A/2010, de 21 de maio, tendo em consideração variáveis como: área do imóvel, qualidade do alojamento, certificação energética, localização e tipologia. Esta medida deve ser combinada com a limitação da atualização legal das rendas considerando a evolução do poder de compra.

---

[Documento 20] Partido: Iniciativa Liberal | Tópicos: habitacao, impostos
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 2. HABITAÇÃO AGORA > 2.1. Reduzir os custos
#### 2.1. Reduzir os custos  
**Eliminar o IMT na compra de habitação própria permanente**  
O direito à habitação está constitucionalmente previsto contudo, a nível tributário, a habitação é tratada como um bem de luxo. Na compra, o comprador tem de pagar IMT e imposto de selo. Assim, a Iniciativa Liberal propõe a **eliminação total do IMT na compra de habitação própria permanente**, pois se concordamos que a habitação é um bem essencial, então não se pode exigir muitas vezes dezenas de milhares de euros pelo simples facto de se comprar uma casa. António Guterres designou o IMT, na altura denominado SISA, como o "imposto mais estúpido do mundo". Passados todos estes anos, mudou-se o nome mas o imposto permaneceu.  
**Isentar o arrendamento e as transações imobiliárias de imposto de selo**  
A Iniciativa Liberal propõe **isentar de imposto de selo as transações imobiliárias**, eliminando a escandalosa dupla tributação não só no momento em que se compra casa. A isenção de imposto de selo visa também ser aplicada no arrendamento, mediação imobiliária e empréstimos bancários (taxas administrativas e bancárias associadas).  
**Reduzir o limite mínimo do IMI que os municípios podem cobrar**  
Aos impostos pagos na compra de casa, juntam-se aqueles pagos pela posse da mesma, nomeadamente o IMI. Por isso, a Iniciativa Liberal propõe uma **redução do limite mínimo do IMI que poderá passar de 0,3% para 0%**. Esta medida dará liberdade a todos os municípios de, caso o entendam, não cobrar IMI aos seus munícipes, tornando-se mais competitivos na atração de pessoas, investimento e desenvolvimento, promovendo uma maior concorrência entre municípios e passando a funcionar como um instrumento que os municípios do interior passarão a ter para se tornarem mais atrativos e fixarem população.  
**Aumentar as deduções em IRS dos juros dos créditos à habitação e das rendas**  
A Iniciativa Liberal propõe o **aumento das deduções em IRS dos juros dos créditos à habitação e das rendas da casa**. Assim, os máximos das deduções em IRS das despesas com rendas passariam dos atuais de 502 euros para os 1 800 euros. Já os valores da dedução em IRS das despesas com juros para construção e/ou aquisição de habitação própria permanente ou para arrendamento no caso de habitação própria e permanente do arrendatário passariam de 296 euros para 900 euros.

---

[Documento 21] Partido: LIVRE | Tópicos: habitacao, impostos, jovens
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > **Habitação e Espaço Público** > Por isso defendemos: > **Apoiar na Emergência**
#### **Apoiar na Emergência**  
9. **Efetivar o Fundo de Emergência para a Habitação**, aprovado no Orçamento de Estado 2024, para apoiar as pessoas que fiquem sem a sua habitação ou em situação de sem-abrigo para financiar as soluções previstas no Programa 1º Direito, considerando que o PRR termina em 2026, e financiar apoios sociais, nomeadamente: o pagamento de alojamento temporário, a comparticipação do pagamento da renda habitacional ou da prestação do crédito destinado à aquisição. Simultaneamente, direcionar verbas do fundo para a dotação dos serviços de apoio social de capacidade para encontrar soluções alternativas em situações de despejo e permitindo regimes pontuais e extraordinários de proteção de arrendatários e mutuantes decorrentes de externalidades, como a elevada inflação e o aumento das taxas de juros dos créditos para a habitação própria e permanente, permitindo a regulação do aumento anual da renda, suspendendo a execução de hipotecas e despejos, se necessário, ou revendo a legislação das condições de atribuição de crédito.  
10. **Aumentar os apoios para o arrendamento habitacional permanente a custos acessíveis:**  
- ao isentar de imposto do selo os novos contratos de arrendamento habitacional cujo prazo inicial seja igual ou superior a 5 anos no âmbito do Programa de Apoio ao Arrendamento;
- ao aumentar o tempo de apoio mínimo no Porta 65 para 36 meses, assim como o período máximo de apoio até ao limite de 84 meses, para terminar com as candidaturas anuais ao apoio financeiro e assim garantir segurança e estabilidade do arrendamento e capacidade de planeamento do futuro para jovens e promover a atualização do valor da renda máxima admitida por tipologia e localização e, na primeira candidatura, possibilitar a atribuição de um valor para apoio ao pagamento da caução;
- incluir o arrendamento de quarto, numa habitação de tipologia adequada à quantidade de pessoas que partilham a casa, no programa Porta 65. Este apoio é direcionado para uma única pessoa independentemente da idade (estudantes, profissionais deslocados, etc).  
11. **Apoiar as pessoas e as famílias para proteção do direito à habitação** em caso de aumento significativo da prestação mensal do crédito à habitação e da renda em contrato de arrendamento:  
- alargamento dos critérios para atribuição da bonificação mensal dos juros passando a taxa de esforço mínima elegível para 30% e aumentar para 85% o apoio calculado sobre a variação dos juros;
- reforçar o apoio extraordinário à renda reduzindo para 30% a taxa de esforço de referência para elegibilidade do beneficiário e aumentando, simultaneamente, o valor máximo do apoio para 300 Euros. Valor mensal que também deve servir de referência máxima do valor atribuído no âmbito do Porta 65+.  
12. **Tornar obrigatória a possibilidade de dação em cumprimento da dívida de crédito à habitação**, já permitida na Lei de Bases da Habitação mas só quando contratualmente prevista. É necessário garantir que quando não se consegue pagar o crédito à habitação a perda do imóvel para a banca garante a extinção da dívida de forma a evitar que mesmo perdendo o imóvel parte da dívida ainda tenha que ser paga.

---

[Documento 22] Partido: Iniciativa Liberal | Tópicos: habitacao, impostos
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 2. HABITAÇÃO AGORA > 2.2. Aumentar a oferta
**Aumentar o número de terrenos disponíveis para construção**  
Para haver mais oferta é necessário haver mais terrenos para construção e maximizar a utilização desses terrenos através de construção em altura, sempre em respeito pelos PDM, algo que deve não só ser previsto como até incentivado na redação deste código. A Iniciativa Liberal propôs no Parlamento **alterar a lei dos solos com vista a simplificar a reclassificação de terrenos privados, de modo a permitir a conversão de prédios rústicos em urbanos, libertando-os para mais construção de habitação**. A proposta não teve o acolhimento desejável e, como tal, a Iniciativa Liberal irá insistir na sua inclusão no futuro Código da Construção, cuja criação resultou de outra proposta liberal. É importante simplificar e eliminar regulamentos desnecessários que contribuem para o aumento do custo de construção ao mesmo tempo que abrem caminho à corrupção.  
**Descentralizar para aliviar a pressão demográfica nas grandes cidades**  
É importante **descentralizar o país e retirar pressão urbanística dos grandes centros urbanos, não só através de uma rede de transportes abrangente, como também** **através de uma descentralização dos serviços do Estado**. Que sentido faz ter o Instituto da Vinha e do Vinho no centro da cidade de Lisboa? Grande parte dos serviços públicos concentram-se à volta de Lisboa, contribuindo para um aumento da procura por casas nessas regiões. Deslocalizar os serviços do Estado para fora de Lisboa, seria mais um passo no sentido de diminuir a pressão urbanística da capital e levando a atividade económica para outras regiões do país. Aqueles que vivessem em Lisboa iriam facilmente constatar que o seu salário poderia valer mais noutra zona, podendo melhorar a sua qualidade de vida ao mesmo tempo que estariam a contribuir para reverter a desertificação no território português.  
**Aumentar a densidade habitacional em áreas com transporte público instalado**  
As áreas que já são servidas por estações de metro, comboio e paragens de autocarro cuja utilização é subaproveitada devem merecer atenção prioritária no planeamento urbanístico a nível comercial, de serviços e de habitação. Portugal falha frequentemente no planeamento urbanístico do território. Há eixos de mobilidade existentes que servem baixas densidades populacionais enquanto outros estão sobrelotados. Em vez de uma cidade dos quinze minutos – expressão utilizada para descrever cidades onde as pessoas conseguem trabalhar e ter acesso aos principais serviços de que precisam no dia a dia com deslocações que demoram um máximo de quinze minutos a partir de sua casa, podemos ter várias zonas de quinze minutos dentro da cidade e à sua volta.  
Adicionalmente, deve estudar-se a viabilidade de incentivos à densificação habitacional em áreas com serviços instalados de transporte público, mobilidade suave e individual através de um índice de internalização de custos de nova instalação de redes viárias, de água potável, saneamento e expansão de redes de transportes públicos (impact fees), com o objetivo de tornar mais atrativa a expansão urbana e a sua densificação em áreas com serviços já instalados.  
**Incentivar construção para arrendamento**  
A Iniciativa Liberal propõe ainda a criação de **regime de incentivo à nova construção para arrendamento (build-to-rent)**, algo muito comum em vários países europeus, mas sem aplicação em Portugal, devido à carga fiscal e volatilidade de regime jurídico, o que torna o mercado de arrendamento habitacional pouco previsível. Para tal, visamos criar um regime de incentivos fiscais especialmente desenhados para atrair o investimento dos agentes que venham colmatar a ausência de casas para arrendar no mercado. Para tal, propomos a isenção de IMT na aquisição dos terrenos, a isenção de IMI, uma tributação autónoma de rendas a 14,5% e uma isenção de IRC. Desta forma, o aumento da oferta de casas para arrendamento irá contribuir para reduzir o valor das rendas praticadas.  
**Resgatar imóveis devolutos do Estado para soluções de habitação**  
Sabemos que, em Portugal, o maior proprietário é o Estado, a tal ponto que nem o próprio Estado tem um inventário completo de todos os imóveis que detém. Assim, a Iniciativa Liberal propõe uma medida que permite à **sociedade civil o resgate dos imóveis devolutos do Estado para soluções de habitação**. Assim, após a venda do imóvel pelo Estado à melhor oferta privada e do cumprimento do plano de reconversão ou reabilitação, o adquirente deve disponibilizar o imóvel para rendas acessíveis durante cinco anos ou destiná-lo a habitação própria e permanente por igual tempo.  
**Formar, reter e atrair capital humano**  
Para haver oferta de qualidade é fundamental formar, reter e atrair pessoas com formação na área. A mão-de-obra especializada no sector da habitação é essencial para tornar a habitação mais acessível. Uma das grandes dificuldades deste sector desde a crise imobiliária de 2008- 2010 é fruto da emigração dos seus melhores quadros na área das construção para outros países aquando da queda abrupta do mercado. Hoje, é necessário atrair e apostar na formação profissional de mais técnicos especializados para que o setor imobiliário consiga aumentar a oferta de habitação com mais construção.

---

[Documento 23] Partido: Bloco de Esquerda | Tópicos: habitacao, politica_externa
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 1 Habitação > 1.3 Propostas para baixar os preços das casas > Controle de rendas, uma medida sensata
#### Controle de rendas, uma medida sensata  
Pelo menos treze países da União Europeia estabeleceram mecanismos de controle de rendas. É também o caso do Reino Unido, da Noruega e da Suíça. As medidas são variadas e incluem a determinação de um valor inicial para a renda (dependente de requisitos específicos) e a limitação ou proibição de aumento das rendas. No que diz respeito aos 38 países da Organização para a Cooperação e Desenvolvimento Económico (OCDE), 23 impõem regulação a aumentos durante a duração do contrato e em treze existe algum tipo de regulação do valor inicial.

---

[Documento 24] Partido: Bloco de Esquerda | Tópicos: habitacao
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 1 Habitação > 1.3 Propostas para baixar os preços das casas > Subsídio à renda
#### Subsídio à renda  
No imediato, devem ser aplicados apoios ao pagamento de rendas, acompanhados de medidas que aumentem a disponibilidade de casas, que impeçam rendas especulativas e garantam estabilidade do arrendamento.

---

[Documento 25] Partido: CHEGA | Tópicos: habitacao, impostos
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > V CAPÍTULO ASSEGURAR HABITAÇÃO DIGNA. COMO? > PROPOSTAS
### PROPOSTAS  
**117.** Tributação na reabilitação em imóveis destinados à habitação, em igualdade de circunstâncias com os benefícios fiscais já em vigor para as Áreas de Reabilitação Urbana.  
**118.** Revogar imediatamente o AIMI (Adicional ao Imposto Municipal sobre Imóveis).  
**119.** Abolir o IMT (Imposto Municipal sobre Transmissões Onerosas de Imóveis) na aquisição de habitação própria permanente.  
**120.** Abolir a obrigação de pagar IMI (Imposto Municipal sobre Imóveis) quando se trate de habitação própria permanente.  
**121.** Isentar do pagamento de IVA a construção da primeira habitação.  
**122.** Estabelecer uma isenção fiscal para projectos built-to- -rent que se comprometam a manter as propriedades no mercado de arrendamento por um período mínimo de 15 anos.  
**123.** Aplicar a taxa autónoma de 10% aos rendimentos provenientes de rendas de contratos estabelecidos com alunos do ensino superior e aos rendimentos decorrentes de contratos de arrendamento para habitação permanente celebrados com duração inferior a dez anos; aos contratos com o mesmo fim, mas celebrados com prazo superior a 10 anos, a taxa autónoma aplicável é de 5%.  
**124.** Criar a Plataforma de Registo de Arrendatários Municipais (PRAM) para assegurar a máxima eficiência na utilização da habitação pública.  
**125.** Investir significativamente na melhoria e expansão de redes de transporte público e serviços essenciais, como es-  
**<sup>3</sup>** INE, Informação de 2021 e 2022 com base nas Estimativas de Obras Concluídas **<sup>4</sup>** https://www.portaldahabitacao.pt/chavenamao-ferramentas/-/asset\_publisher/0ChxS95jgkNa/content/benef%2525c3%2525adcios-fiscais-reabilita%2525c3%2525a7%2525c3%2525a3o  
colas, hospitais e áreas de lazer nas áreas identificadas para expansão habitacional.  
**126.** Estabelecer parcerias entre o sector público e privado para disponibilizar terrenos adequados à construção habitacional.  
**127.** Estimular e incentivar a construção de habitação acessível por meio de parcerias entre o sector público e privado, utilizando terrenos públicos com concessão de 90 anos e estabelecendo rendas a custos controlados.  
**128.** Mapear os terrenos públicos em locais estratégicos, levando em consideração a proximidade de serviços públicos, transporte e infra-estruturas.  
**129.** Realizar concursos públicos para empresas privadas interessadas em desenvolver projectos habitacionais em terrenos públicos, estabelecendo critérios de acessibilidade, sustentabilidade e custos controlados.  
**130.** Criar um Novo Modelo de Licenciamento Simplificado, reduzindo a quantidade de documentos exigidos e simplificando os procedimentos administrativos.  
**131.** Implementar um portal único online centralizado para submissão e acompanhamento de pedidos de licenciamento, garantindo transparência e facilidade de acesso aos intervenientes.  
**132.** Reduzir prazos de tramitação dos pedidos de licenciamento com metas realistas, monitorização regular e garantia da alocação de recursos adequados.  
**133.** Reverter a possibilidade de arrendamento forçado de habitações devolutas; a revogação dos vistos gold e as limitações ao alojamento local, aprovados no Programa Mais Habitação.  
**134.** Reabilitar o Património Edificado Público através da aprovação de um programa abrangente que inclua o levantamento detalhado de todos os edifícios e do seu estado de conservação, a celebração de parcerias estratégicas com o sector privado para a execução de projectos de reabilitação, garantindo transparência no processo e a divulgação dos respectivos procedimentos.  
**135.** Identificar situações de uso indevido ou fraudulento da habitação pública e implementar uma política de tolerância zero à ocupação ilegal de habitação pública ou privada.  
**136.** Promover a preservação e reabilitação das fachadas tradicionais e dos estilos regionais de forma a manter a identidade de cada região.  
**137.** Restabelecer o Crédito Jovem Bonificado com linhas de crédito específicas destinadas a jovens que desejam adquirir a sua primeira habitação; taxas de juro bonificadas para os empréstimos concedidos a jovens até aos 35 anos, tornando o financiamento mais acessível e condições flexíveis para a concessão de crédito, levando em consideração a situação financeira dos jovens e proporcionando opções adaptadas às suas realidades.  
**138.** Ampliar o leque de beneficiários do Programa Porta 65 Jovem, bem como simplificar o seu processo de acesso.

---

[Documento 26] Partido: Aliança Democrática | Tópicos: habitacao, governacao, educacao
  Secção: PROGRAMA ECONÓMICO DA ALIANÇA DEMOCRÁTICA > 4. Uma Economia de Futuro > 4.3. POPULAÇÃO COM FUTURO: VENCER A CRISE DEMOGRÁFICA E EXPANDIR A OFERTA HABITACIONAL > 4.3.2. HABITAÇÃO, REFORMAS PARA RESOLVER A CRISE DA HABITAÇÃO > **Choque de Oferta Privada, Pública e Cooperativa**
##### **Choque de Oferta Privada, Pública e Cooperativa**  
Para assegurar o aumento da oferta habitacional, seja ela privada, estimulada com a adoção de diversas medidas de incentivo, designadamente fiscais, seja ela pública para apoio a famílias e indivíduos em situação mais vulnerável, mediante a mobilização do stock habitacional existente ou nova construção, seja ela cooperativa, seja ela resultado de uma resposta articulada com o terceiro setor, a AD propõe:  
- **Flexibilização das limitações de ocupação dos solos, densidades urbanísticas (incluindo construção em altura) e exigências e requisitos construtivos**, bem como a possibilidade de aumento dos perímetros urbanos, garantindo uma utilização do território de forma sustentável e socialmente coesa e harmoniosa como forma de garantir acesso à habitação;
- Injeção no mercado, quase-automática, dos imóveis e solos públicos devolutos ou subutilizados;
- **Regime Excecional e temporário de eliminação ou Redução dos Custos Tributários em obras de construção ou reabilitação** em imóveis destinados a habitação permanente independentemente da localização em ARU, com compensação das autarquias por perdas de receita (a realizar através do Orçamento do Estado com devida garantia no Regime Financeiro das Autarquias Locais):
- Redução substancial ou eliminação de taxas de urbanização, edificação, utilização e ocupação;
- Aplicação de IVA à taxa mínima de 6% nas obras e serviços de construção e reabilitação e alargamento da dedutibilidade.
- **Programa de Parcerias Público-Privadas para a construção e reabilitação em larga escala**, quer de habitação geral quer de alojamento para estudantes;
- **Estímulo e facilitação de novos conceitos de alojamento no mercado português**, incluindo com regulatory sand box (build to rent, mixed housing com bónus de densidade urbanística para habitação a custos moderados, co-living, habitação modular, cooperativas de habitação, utilização flexível dual das residências de estudantes);
- **Análise do novo enquadramento legislativo do licenciamento e controlo urbanístico**, reforçando sempre que necessário o caminho da simplificação e redução de obstáculos ao licenciamento e transição de modelo de controlo urbanístico prévio para fiscalização _ex-post;_
- **Planeamento e implementação da política e oferta de transportes públicos que sustente a possibilidade de aumento dos perímetros urbanos** e o encurtamento das distâncias físicas e temporais entre os existentes, garantindo uma utilização do território de forma sustentável e socialmente coesa e harmoniosa como forma de garantir acesso à habitação.

---

[Documento 27] Partido: Iniciativa Liberal | Tópicos: habitacao, impostos
  Secção: PROGRAMA ELEITORAL > PORTUGAL A CRESCER > 2. HABITAÇÃO AGORA: MAIS OFERTA
### 2. HABITAÇÃO AGORA: MAIS OFERTA  
- Reverter o Pacote Mais Habitação, eliminando quaisquer formas de arrendamento forçado
- Eliminar o IMT na compra de habitação própria permanente
- Aumentar as deduções em IRS das rendas e dos juros do créditos à habitação
- Isentar o arrendamento e as transações imobiliárias de imposto de selo
- Reduzir o imposto sobre as rendas para uma taxa máxima de 14,5%
- Reduzir o IVA da nova construção de 23% para 6% para aumentar a oferta
- Colocar os milhares de imóveis vazios do Estado à disposição do mercado de habitação
- Criação de um regime de incentivo à nova construção para arrendamento (build-to-rent)
- Consolidar mais de dois mil diplomas dispersos num só Código da Construção e Edificação
- Consolidar todas as regras do arrendamento num Código do Arrendamento
- Criar um regime de pré-licenciamento urbanístico automático

---

[Documento 28] Partido: CHEGA | Tópicos: habitacao, impostos, jovens
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > V CAPÍTULO ASSEGURAR HABITAÇÃO DIGNA. COMO? > PRIORIDADES
### PRIORIDADES  
- Reformular a Fiscalidade na Habitação, nomeadamente implementar políticas fiscais atractivas para investidores, nacionais e estrangeiros, com a redução de impostos sobre a propriedade;  
- Operacionalizar programas específicos voltados para a expansão habitacional em áreas metropolitanas, inspirados em modelos de planeamento urbano bem-sucedidos, (por ex. Parque Expo);  
- Reforçar a fiscalização da utilização de habitação pública e implementar uma política de tolerância zero à ocupação ilegal;  
- Simplificar os processos de licenciamento através de um novo modelo, reduzindo a quantidade de documentos exigidos, simplificando os processos administrativos, sendo mais estável, ágil e menos burocrático.  
- Facilitar a aquisição de habitação própria permanente aos jovens através da implementação de diversas medidas de apoio.

---

[Documento 29] Partido: Partido Comunista Português | Tópicos: habitacao, economia
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 4 ELEVAR A QUALIDADE DE VIDA. INVESTIR NOS SERVIÇOS PÚBLICOS, CUMPRIR AS FUNÇÕES SOCIAIS DO ESTADO > 4.6 Garantir o direito à habitação > Proteger a habitação própria
##### Proteger a habitação própria  
- Criar um regime especial de protecção da habitação própria que ponha os lucros da banca a suportar o aumento das taxas de juro, reduzindo igualmente taxas, comissões e outros encargos.
- Determinar a intervenção do banco público Caixa Geral de Depósitos – em condições que funcionem como referência para o mercado do crédito à habitação, estabelecendo designadamente, nos novos contratos e nos já existentes, condições de spread, comissões e outros encargos abaixo das que são praticadas pelos bancos privados, inclusivamente na transferência de crédito.
- Garantir, no crédito hipotecário, que a dação em pagamento da habitação determina a extinção da dívida;
- Restringir fortemente as possibilidades de execução de hipoteca da habitação permanente e despejo pelos bancos.

---

[Documento 30] Partido: Bloco de Esquerda | Tópicos: habitacao
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 1 Habitação > 1.1 A especulação está a tirar-nos as casas
### 1.1 A especulação está a tirar-nos as casas  
ivemos num país onde ter um salário não é garantia de ter um teto. A habitação é hoje o principal fator de empobrecimento de quem vive do seu trabalho. Nos últimos três anos, o preço da habitação subiu quatro vezes face aos ganhos das famílias. Na última década, os preços das casas em Portugal aumentaram quase 100% e, no mesmo período, o valor médio mensal da renda disparou 42%.  
**GRÁFICO 1**  
2015  
2016  
Evolução dos preços da habitação em Portugal  
2017  
17 27 37 47 17 27 37 47 17 27 37 47 17 27 37 47 17 27 37 47 17 27 37 47 17 27 37 47 17 27 37 47 17  
2019  
2020  
2021  
2018  
2023  
2022  
A escalada dos juros encheu os cofres dos bancos e esvaziou a conta de quem tem crédito à habitação. Os cinco maiores bancos lucraram 12 milhões por dia nos primeiros nove meses de 2023, o equivalente a 3300 milhões de euros, extraídos diretamente dos salários que pagam as crescentes prestações do crédito à habitação.  
Em 2022, a DECO recebeu 31.500 pedidos de ajuda de famílias que não conseguiam fazer face ao custo de vida e a habitação foi um dos principais motivos: no primeiro semestre de 2023, representou 44% dos pedidos de ajuda.  
GRÁFICO 2  
**Evolução das taxas de juro**  
Perante este desastre, o Governo do PS, com o apoio da direita, decidiu ainda permitir o maior aumento de rendas dos últimos 30 anos: mais 7% no ano de 2024.  
O governo do PS cruzou os braços e deixou o mercado andar por si. Não quis limitar as rendas, tabelar os preços ou colocar os lucros da banca a suportar os aumentos de prestações. O parque habitacional público em Portugal continua nuns residuais 2%.  
Para adquirir uma casa ao preço médio praticado em Portugal, alguém que ganhe o salário mínimo precisaria de trabalhar 30 anos sem poder gastar um cêntimo em mais nenhuma despesa. Não admira, por isso, que haja cada vez mais pessoas sem-abrigo, muitas delas com emprego. São mais 10 mil, um aumento de 78% em apenas 4 anos. Muitos empurrados para a rua pelas rendas proibitivas que se praticam em Portugal, em particular nas grandes cidades.  
GRÁFICO 3  
**Evolução dos preços habitação para compra por distrito**  
Fonte: Barómetro do Imovirtual  
Esta crise tem causas e responsáveis. É preciso identificá-los e combatê-los. Se a especulação nos está a tirar casas, então é preciso tirar as casas das mãos dos especuladores e devolvê-las às pessoas.

---

[Documento 31] Partido: CHEGA | Tópicos: impostos, habitacao, justica
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > VIII CAPÍTULO MAIS RENDIMENTOS PARA AS FAMÍLIAS E EMPRESAS. COMO? > PROPOSTAS
### PROPOSTAS  
**181.** Introduzir duas taxas marginais de IRS: de 15% até aos 39.999 euros e de 30% a partir de 40.000 euros, com isenção de pagamento para quem receber até aos mil euros mensais.  
**182.** Isentar os jovens até aos 35 anos de IRS até perfazerem um total de 100 mil euros de rendimentos desde o início da sua carreira.  
**183.** Isentar de IRS o designado "15.º salário", sem quaisquer condicionantes.  
**184.** Introduzir uma _flat tax_ de IRC de 15% para as regiões autónomas e para o interior do país e de 18% para o resto do território.  
**185.** Criar um modelo de número único de identificação para as pessoas e empresas, assim evitando que a mesma pessoa tenha que ter número de utente, de cartão de cidadão, de contribuinte, de Segurança Social, de eleitor, etc.  
**186.** Eliminar o adicional do IMI; isentar de IMI e de IMT a compra de habitação própria e permanente, assim como a tributação de mais-valias da venda de habitação própria e permanente, desde que seja reinvestida na compra de uma nova habitação própria e permanente mesmo que de valor inferior para si ou para descendentes directos, no pagamento de empréstimos bancários, ou no caso dos reformados/pré-reforma.  
**187.** Aplicar a taxa de IVA reduzida (6%) à Electricidade e ao Gás e implementar uma tarifa social da energia para famílias numerosas, considerando os primeiros 200 kWh consumidos por família/mês, desde que a potência contratada não ultrapasse os 10,35kVA.  
**188.** Reintroduzir o IVA zero para bens alimentares essenciais e proceder ao alargamento da lista anteriormente aprovada, assim como aplicar a taxa de IVA reduzida (6%) para a restauração.  
**189.** Reduzir o IVA do Gasóleo e da Gasolina Rodoviária para a taxa intermédia de 13% e eliminar o adicional ao Imposto Sobre Produtos Petrolíferos.  
**190.** Terminar com a dupla tributação na compra de carro novo e com o cálculo indevido do ISV quando se trata de veículos usados matriculados noutro Estado-membro da União Europeia.  
**191.** Implementar medidas que permitam que as Cooperativas, Fundações, Instituições Particulares de Solidariedade Social (IPSS), Santas Casas da Misericórdia, Mutualidades e Associações de reconhecido interesse público sem carácter lucrativo possam deduzir/recuperar 100% do valor do IVA que lhes é cobrado nas aquisições internas, nas aquisições intracomunitárias e nas prestações de serviços.  
**192.** Aplicar a taxa autónoma de 10% aos rendimentos provenientes de rendas de contratos estabelecidos com alunos do ensino superior e aos rendimentos decorrentes de contratos de arrendamento para habitação permanente celebrados com duração inferior a dez anos; aos contratos  
com o mesmo fim, mas celebrados com prazo superior a 10 anos, a taxa autónoma aplicável é de 5%.  
**193.** Proceder à revisão do actual Regime Geral das Infracções Tributárias, promovendo a simplificação processual, reformulando a organização judiciária e tributária e estabelecendo um novo regime geral para as infracções tributárias.  
**194.** Implementar apoio jurídico e mediação gratuita para a defesa de pequenos contribuintes junto da Administração Tributária quando estejam em causa pequenos montantes de impostos ou outros tributos e/ou execuções fiscais de pequeno valor.  
**195.** Tornar as normas fiscais mais objectivas e claras:  
- Evitando complexidades desnecessárias e, consequentemente, reduzindo litígios;  
- Pugnando pela publicação atempada de todas as orientações da Autoridade Tributária (AT), assim trazendo mais transparência e clareza à interpretação feita pela AT e contribuindo para a uniformização de procedimentos;  
- Através da promoção da publicação de Códigos anotados, pela própria Assembleia da República, como já aconteceu na década de 80, assim facilitando o cumprimento das normas por parte dos contribuintes.  
**196.** Reforçar os meios técnicos e humanos da AT para o combate à fraude e à evasão fiscal e melhorar os meios (inclusivamente legais) para o apuramento de manifestações de fortuna, nomeadamente, através da comunicação à AT do nome e NIF dos adquirentes de determinados bens de luxo.  
**197.** Promover de forma activa a reintegração dos valores da economia paralela na economia lícita, quer através da simplificação fiscal, quer do aumento significativo da fiscalização nesta matéria, com o objectivo de recuperar 20%/ ano estes montantes para a economia nacional.  
**198.** Criar o protocolo "zero economia paralela", com o objectivo de em seis anos recuperar tendencialmente todos os valores movimentados no âmbito da economia paralela para a economia nacional (cerca de 89 mil milhões de euros ano).  
**199.** Transferir para o sector das telecomunicações a taxa sobre o Audiovisual, retirando-a da factura de electricidade e atribuindo o seu pagamento às empresas de telecomunicações a operar em Portugal

---

[Documento 32] Partido: Aliança Democrática | Tópicos: habitacao, economia
  Secção: PROGRAMA ECONÓMICO DA ALIANÇA DEMOCRÁTICA > Sumário Executivo > II. POR QUE É PRECISO MUDAR? O PAÍS ESTAGNADO, O CAMINHO ERRADO > 1. DIAGNÓSTICO CRÍTICO DE UM PAÍS ESTAGNADO
### II. POR QUE É PRECISO MUDAR? O PAÍS ESTAGNADO, O CAMINHO ERRADO  
#### 1. DIAGNÓSTICO CRÍTICO DE UM PAÍS ESTAGNADO  
Após 8 anos de governação do Partido Socialista, que totalizou 22 dos últimos 29 anos, a realidade portuguesa é dura e preocupante:  
- Economia estagnada, com **baixíssimo crescimento económico** nas duas décadas passadas (média anual de 0,8% desde 2000), e na próxima década e meia, segundo projeções credíveis para os próximos anos;
- Portugal tem sido **sucessivamente ultrapassado, caminhando para a cauda da Europa** em PIB per capita em paridades de poder de compra (desde 2000 foi ultrapassado por 6 países da Coesão, e em 2024, prevê-se que o seja também pela Roménia);
- **Cresceu muito o número de trabalhadores que auferem o salário mínimo nacional**, para cerca de 840 mil, e **diminuiu o diferencial para os ganhos médio e mediano**, que não acompanharam a evolução do valor mínimo legalmente fixado. Cerca de dois terços dos jovens têm um rendimento mensal inferior a mil euros;
- A **pobreza atinge níveis inadmissíveis**, tendo a taxa de risco de pobreza aumentado em 2022, com uma taxa antes de prestações sociais superior a 41% da população, maior do que a registada no início do século;
- Têm-se **agravado** os vários indicadores de **desigualdade do rendimento** nos últimos cinco anos;
- A **emigração jovem qualificada atinge níveis brutais**, estimando-se que cerca de 30% dos jovens nascidos em Portugal vivam fora do país; esta é a taxa de emigração mais elevada da Europa e uma das maiores do mundo. Os que não emigram enfrentam um desemprego jovem que ultrapassou os 20% no final de 2023 e são, em média, os que na Europa mais tarde saem de casa dos seus pais;
- A **carga fiscal atingiu o valor máximo de sempre**, tendo batido recordes ano após ano, nos últimos oito anos (de cerca de 37% do PIB em 2015 para 38,5% em 2022). **O esforço fiscal** dos portugueses (que mede a carga fiscal de cada país ajustada pelo nível de vida dos seus cidadãos) **é o 4.º mais elevado da Europa**;
- A essa carga fiscal recorde tem correspondido um **Estado em séria falência operacional**, com gravíssimos problemas nos serviços públicos mais críticos, da saúde à educação, da justiça à segurança, da habitação aos serviços de atendimento ao público;
- Na **Saúde**, o número de utentes sem médico de família passou de cerca de 1 milhão para 1,7 milhões de pessoas, aumentaram as listas de espera para consultas e cirurgias e os tempos de espera tornaram-se ainda mais indignos; as urgências e serviços de maternidade funcionam em intermitência. Em sinal de desistência (possível para quem tem recursos) já cerca de 5 milhões de portugueses têm uma segunda cobertura (seguro de saúde privada, ADSE ou outros sistemas), que é paga em acréscimo aos impostos que suportam para financiar o SNS;
- Na **Educação**, o desempenho dos alunos portugueses tem caído dramaticamente desde 2018, em todas as avaliações internacionais, em todas as dimensões (português, matemática e ciências). Nas escolas acumulam-se os alunos sem aulas, e os professores estão esgotados e em conflito com o Governo. Em sinal de desistência (possível para quem tem recursos) já cerca de 25% dos estudantes do ensino secundário frequentam escolas privadas;
- Os preços das casas aumentaram muito mais do que os rendimentos das famílias. Desde 2016 até ao final de 2022, os preços da habitação subiram 89% ao passo que o rendimento nominal _per capita_ aumentou 33,8%;
- A produtividade também tem estado praticamente estagnada, crescendo a uma taxa média anual de 0,7% entre 2000 e 2022;
- Persistem **baixos níveis de investimento e poupança**. A formação bruta de capital fixo em percentagem do PIB é hoje muito inferior aos valores do início do século (20% vs 27%) e a taxa de poupança das famílias atinge os níveis mais baixos de que há memória.

---

[Documento 33] Partido: Partido Socialista | Tópicos: impostos, ambiente, habitacao
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **1.ª MISSÃO:** UMA ECONOMIA EM TRANSFORMAÇÃO ASSENTE EM CONTAS EQUILIBRADAS > 7. Energia: mais renováveis, menores custos e maior competitividade > 7.2.
##### 7.2.  
Também o **combate à pobreza energética** é uma preocupação que acompanha o desenho destas políticas públicas de transição justa. Aqui, destacamos a importância das medidas de atenuação dos custos da energia consumida e da eficiência energética, dirigidas, em primeiro lugar, às famílias, como forma de melhorar a transparência do setor, as condições de habitabilidade, bem como de contribuir para o aumento de rendimento disponível dos agregados.  
Desta forma, um futuro governo do PS irá:  
- Aplicar o IVA de 6% aos primeiros 200 kWh de energia elétrica consumida em cada mês (duplicando os atuais 100 kWh), ou de 300 kWh mensais, no caso das famílias numerosas (duplicando os atuais 150 kWh). Esta descida da tributação contribuirá para combater a pobreza energética de muitas famílias;  
- Avaliar o aumento da comparticipação do Vale Eficiência e acelerar o investimento na reabilitação energética de edifícios e de condomínios;  
- Expandir a rede do Espaço Cidadão Energia a todo o país, em colaboração com as autarquias e/ou as agências locais e regionais de energia;  
- Desenvolver uma estratégia de execução rápida da energia fotovoltaica de forma mais descentralizada e democrática, através da possibilidade de instalação de painéis fotovoltaicos por inquilinos e da aposta na instalação de painéis em varandas ligados a uma tomada da casa;  
- Democratizar a produção elétrica através de linhas de crédito à instalação e garantia de venda a um preço razoável através de um agregador de último recurso;  
- Conceder acesso automático às tarifas sociais de gás e de água para os beneficiários de tarifa social de eletricidade.

---

[Documento 34] Partido: Bloco de Esquerda | Tópicos: habitacao
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 1 Habitação > 1.4 Aumentar a oferta de habitação > As propostas do Bloco para aumentar a oferta de habitação:
#### As propostas do Bloco para aumentar a oferta de habitação:  
→ **25% da nova construção para habitação acessível**  
Com esta medida será afetada uma quota de 25% do produto de obras de construção, reconstrução, ampliação e alteração ou de operações de loteamento ou operações urbanísticas para habitação a arrendar sob o regime de renda condicionada, aumentando assim a habitação acessível e reduzindo o valor global das rendas;  
- → **Construção pública de novos alojamentos** destinados ao arrendamento a custos acessíveis, integrados na malha urbana e evitando a reprodução de guetos;
- → **Mobilização imediata de edifícios públicos devolutos** ou sem utilização para habitação a custos acessíveis;
- → Uso de instrumentos da política de solos **posse administrativa** para conversão de edifícios habitacionais devolutos em habitação a custos controlados;
- → **Reforço do IHRU e criação de um Serviço Nacional de Habitação** Com orçamento e programação plurianual para aumentar a provisão, organização e manutenção de habitação pública;  
→ **Proibir a venda de casas a não residentes**  
Perante a gravidade da crise da habitação é necessário tomar medidas que garantam que as casas disponíveis são efetivamente utilizadas para fins habitacionais. A entrada de não residentes que, aqui não desejando viver, pretendem apenas adquirir um ativo financeiro ou bem de luxo cria enormes pressões no mercado habitacional. Trata-se de uma procura praticamente ilimitada, com um poder de compra inesgotável, que inflaciona o preço dos imóveis, como foi já reconhecido pelo Banco de Portugal. Assim, o Bloco propõe a proibição da venda de casas a não residentes, salvaguardando naturalmente o direito de aquisição de imóveis a portugueses residentes no estrangeiro, bem como a estrangeiros residentes em Portugal e transações de imóveis em territórios de baixa densidade. No Canadá, o governo do Partido Liberal proibiu a venda de edifícios residenciais a estrangeiros, medida que já tinha sido aplicada na Nova Zelândia e que, recentemente, poderá ser também uma realidade nas ilhas de Ibiza, Maiorca e Menorca;  
→ **Moratória a novos empreendimentos turísticos**  
Suspensão da emissão de títulos para novos empreendimentos turísticos nas zonas de pressão habitacional até 2030;  
→ **Limitação do Alojamento Local**  
O Alojamento Local deve estar sujeito a quotas máximas, estabelecidas em cada freguesia, que respeitem a função primordial das imobiliário habitacional: a habitação. O Bloco propõe:  
i) Imposição, em cada freguesia, de um máximo de 5% de fogos dedicados ao Alojamento Local;  
ii) Fixação do prazo de dois anos para as licenças de Alojamento Local, renováveis por períodos iguais, até ao cumprimento dos rácios fixados, não podendo ser renovadas licenças que resultem na violação desses rácios. Na renovação das licenças, têm prioridade os titulares que possuam, direta ou indiretamente, apenas um registo de AL.

---

[Documento 35] Partido: Partido Comunista Português | Tópicos: impostos, ambiente
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 2 DESENVOLVIMENTO ECONÓMICO > 2.3. Políticas-chave > 2.3.3. Energia: avançar na eficiência e soberania energética
##### 2.3.3. Energia: avançar na eficiência e soberania energética  
Os processos de liberalização e de privatização de sectores energéticos estratégicos para o fornecimento de bens e serviços essenciais à economia e à sociedade, levado a cabo desde há décadas pelos governos do PS, PSD e CDS, conduziu ao fortalecimento de monopólios e à densificação das redes oligopolistas que, baseadas em visíveis posições dominantes, obtêm rendas e lucros crescentes, prejudicam a competitividade nacional, põem em causa a sobrevivência de muitas pequenas e médias empresas, a par do agravamento crítico do custo de vida das famílias portuguesas, como se verifica no caso da electricidade e dos combustíveis fósseis.  
É necessário romper com o actual caminho. É preciso promover a racionalidade e a eficiência na produção/conversão, no transporte e na distribuição, bem como ao nível dos diversos tipos de utilização dos vectores de energia final, sempre no respeito pela sustentabilidade ambiental e socio-económica, e num referencial de soberania energética nacional. O PCP considera necessário:  
- aumentar a utilização racional da energia e da eficiência energética em sistemas reforçados, quantitativa e qualitativamente, de transportes públicos colectivos, nos edifícios (com prioridade para os públicos) e nos diversos sectores produtivos, mormente na indústria (redução da intensidade energética);
- atribuir prioridade à promoção num referencial de cooperação e segurança multilateral – da diversificação das fontes primárias de energia, quer das endógenas, quer das que o País vai continuar a importar;
- a prospecção e cartografia dos recursos para a fileira energética, tanto as fontes primárias de energia renováveis (hidroeléctrica, eólica, solar térmica, fotovoltaica, biomassa, incluindo efluentes e resíduos orgânicos – produção de biogás e biometano –, geotérmica e as exploráveis ao nível do mar) como as não renováveis, bem como dos diversos recursos minerais estratégicos necessários a uma transição energética justa e sustentável;
- as explorações dos recursos referidos devem passar pela transparência de processos políticos e técnico-administrativos, a minimização dos impactes ambientais locais e regionais e a maximização do valor acrescentado em cadeias de tratamento sediadas no País; as suas unidades de exploração devem garantir o aproveitamento racional e sustentável do território nacional (condicionantes ambientais, ecológicas, paisagísticas e de ordenamento do território);
- o reassumir pelo Estado do seu papel de autoridade e de controlo público das principais empresas (EDP, GALP, REN), no aprovisionamento, produção, transporte e comercialização das diferentes formas de energia, e a reorganização das fileiras energéticas, recompondo a cadeia de valor das suas empresas;
- o reforço da base científica e técnica nas novas fileiras tecnológicas de conversão/produção energética e da análise multidisciplinar dos projectos de aproveitamento das fontes renováveis, minimizando os seus impactos e custos no território e na necessidade de infraestruturas de armazenagem de electricidade gerada pela intermitência;
- a revisão completa dos incentivos, subsídios, subvenções não reembolsáveis e outros apoios às empresas produtoras de electricidade, seja no domínio da produção convencional, seja no das energias renováveis, para pôr fim às «rendas excessivas», aos lucros oportunistas trazidos por conjunturas imprevistas ou os devidos ao efeito conjugado das acções monopolistas e oligopolistas e/ou receitas indevidas; o défice tarifário no domínio da electricidade, devendo ser progressivamente diminuído ao nível regulatório, não deverá passar pela exploração privatizada que opera através de otimizações financeiras para proveito empresarial próprio;
- a manutenção dos regimes de tarifas reguladas na electricidade e no gás natural, a redução da taxa do IVA para 6% (electricidade, GN e GPL), a criação de um regime de preços máximos para os diversos tipos de energia bem como regimes de preços bonificados para algumas actividades – agricultura, pescas e transportes.

---

[Documento 36] Partido: Partido Socialista | Tópicos: trabalho, habitacao, saude
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **5.ª MISSÃO:** UM PORTUGAL CENTRAL NA EUROPA E NO MUNDO > 1. Uma participação solidária, exigente e propositiva na União Europeia > 1.3.
##### 1.3.  
Portugal empenha-se numa **Europa Social,** que melhore a vida das pessoas e dos trabalhadores e integre os migrantes de forma responsável. Com este objetivo o PS propõe:  
- Progredir na concretização do Pilar Europeu dos Direitos Sociais, materializando em toda a sua plenitude o respetivo Plano de Ação, assim como o Plano de Ação para a Economia Social, defendendo o contínuo aperfeiçoamento do modelo social europeu;  
- Assegurar uma correta materialização do Pacto sobre Migrações e Asilo, criando canais regulares e seguros de imigração, garantindo condições adequadas de acolhimento e integração, trabalhando com os países de origem e de trânsito, combatendo as redes de tráfico de seres humanos, apoiando os refugiados com estatuto de proteção internacional que fogem da guerra ou de situações de opressão;  
- Defender a criação de um fundo europeu de apoio à reconversão e requalificação profissional, que proporcione aos trabalhadores e desempregados a sua adaptação às grandes mudanças estruturais na economia;  
- Promover os direitos dos trabalhadores em toda a UE através de legislação europeia que acabe com a exploração laboral, dumping social e precariedade sistemática, e reforçar as competências da Autoridade Europeia do Trabalho para assegurar a aplicação dessa legislação;  
- Promover o reequilíbrio das relações laborais, propondo uma Diretiva europeia que torne obrigatória a representação de trabalhadores no Conselho de Administração das grandes empresas, à semelhança do que se encontra em vigor em vários Estados Membros;  
- Criar uma Estratégia Europeia para a Habitação, com disponibilização de fundos europeus não apenas para habitação social, mas também para habitação a custos controlados, quer de iniciativa pública, quer cooperativa, que possa dar um forte impulso à descarbonização do parque habitacional europeu;  
- Prosseguir o projeto de uma União Europeia da Saúde, capacitando a União para a responder em conjunto aos principais desafios de saúde pública.

---

[Documento 37] Partido: Partido Socialista | Tópicos: trabalho, impostos, educacao
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **1.ª MISSÃO:** UMA ECONOMIA EM TRANSFORMAÇÃO ASSENTE EM CONTAS EQUILIBRADAS > 1. Oito anos de vitória da social democracia sobre a direita nas políticas económicas e sociais > 1.2. Melhores salários
##### 1.2. Melhores salários  
A grande aposta no diálogo social materializou-se nos acordos inéditos firmados nos últimos anos. Destes, destacam-se o Acordo de Médio Prazo para a Melhoria dos Rendimentos, dos Salários e da Competitividade, mas também o Acordo Plurianual de Valorização dos Trabalhadores da Administração Pública. Estes acordos criaram um horizonte de previsibilidade sem precedentes e a garantia de melhoria dos rendimentos, seja no setor privado como no setor público. O diálogo social encetado beneficiou, assim, de uma perspetiva plurianual das políticas públicas.  
Estes acordos, acompanhados pelo dinamismo da economia, permitiram aumentos robustos das remunerações, mitigando os efeitos do aumento do nível de preços. Entre 2015 e 2023, as remunerações médias declaradas à segurança social registaram um aumento de 34%, 16 pontos percentuais superiores à inflação acumulada para igual período. O peso das mesmas no PIB convergiu com a média europeia: era de 43,6% em 2015 (46,8% na UE) e aumentou para 46,7% nos primeiros três trimestres de 2023 (47%).  
Os aumentos registados foram particularmente relevantes para os trabalhadores com menores remunerações, nomeadamente para os que auferem a Remuneração Mínima Mensal Garantida, que aumentou 62,4%. No entanto, o peso destes trabalhadores no total de trabalhadores não acompanhou o aumento, estando ao nível mais baixo desde 2015. Ao mesmo tempo, a taxa de pobreza após transferências sociais baixou consistentemente, convergindo com a média europeia e atingindo os níveis mais baixos em pelo menos vinte anos.  
Este caminho não se esgotou no aumento direto do rendimento das famílias. Os Governos do PS implementaram ao longo destes oito anos políticas que reforçaram os orçamentos familiares, como a maior redução registada dos impostos sobre os rendimentos do trabalho, a redução dos preços dos passes sociais, a redução do limite máximo das propinas no 1.º ciclo do ensino superior, a gratuitidade das creches e ainda dos manuais escolares.  
Ao mesmo tempo, os Governos do PS fizeram continuados reforços orçamentais nas áreas essenciais do Estado Social. Assim, comparando o OE 2015 com o OE 2024, são mais €6,7 mil milhões para pensões na Segurança Social, mais €5,6 mil milhões para o Serviço Nacional de Saúde e € 2,9 mil milhões para a Educação. Para as políticas de acesso à habitação, que é uma das preocupações mais urgentes dos portugueses, estão alocados 1000 milhões em 2024.

</details>

## item-08

**Question:** Compara as propostas de IRS da Iniciativa Liberal e do CHEGA.

**Answer:**

As propostas de reforma do IRS da **Iniciativa Liberal (IL)** e do **Chega** apresentam abordagens distintas quanto à estrutura do imposto e aos mecanismos de redução de carga fiscal:

**Iniciativa Liberal (IL)**
*   **Redução de taxas:** Propõe uma redução significativa das taxas marginais de IRS, defendendo que o imposto deve ser menos progressivo para não desincentivar o trabalho e o investimento.
*   **Simplificação e Unificação:** Defende a simplificação do sistema, com o objetivo de reduzir a complexidade das deduções e das categorias de rendimento.
*   **Mínimo de Existência:** Propõe a elevação do limiar de isenção (mínimo de existência) para garantir que os rendimentos mais baixos não sejam tributados.
*   **Foco na Liberdade Individual:** Argumenta que a redução do IRS permite maior autonomia nas decisões de consumo e poupança dos contribuintes.

**Chega**
*   **Redução de Taxas:** Propõe a descida das taxas de IRS, com foco particular na redução da carga fiscal sobre os rendimentos médios e baixos.
*   **Eliminação de Taxas para Rendimentos Baixos:** Defende a isenção de IRS para quem recebe rendimentos próximos do salário mínimo ou de valores considerados baixos pela sua proposta.
*   **Combate à Evasão e Fraude:** O partido foca a sua retórica na necessidade de combater a corrupção e a fraude fiscal como forma de garantir que a carga fiscal não precise de ser excessiva para manter o Estado.
*   **Foco na Classe Média:** Argumenta que as famílias portuguesas estão sobrecarregadas pelo sistema fiscal atual e propõe medidas que libertem rendimento disponível para o consumo das famílias.

**Principais Diferenças**
*   A **Iniciativa Liberal** foca-se numa reforma estrutural de natureza liberal, visando a **redução das taxas marginais** e a **simplificação do sistema** como um todo.
*   O **Chega** foca a sua proposta na **isenção de rendimentos baixos** e na redução da carga sobre a **classe média**, ligando a gestão fiscal ao combate à corrupção.

**Reference answer:**

O CHEGA propõe duas taxas marginais de IRS — 15% até 39.999 euros e 30% a partir de 40.000 euros —, com isenção para quem recebe até mil euros mensais, e isenção de IRS para jovens até aos 35 anos até perfazerem 100 mil euros de rendimentos. A Iniciativa Liberal propõe uma taxa única de 15% sobre os rendimentos acima do salário mínimo nacional anualizado, mantendo as deduções à coleta, chegando lá numa primeira fase através de duas taxas (15% e 28%). Ambos simplificam o IRS para poucas taxas, mas o CHEGA mantém um escalão de 30% para rendimentos mais altos, enquanto a IL visa uma taxa única. O CHEGA propõe ainda isentar de IRS o "15.º salário", as horas extraordinárias e as mulheres com quatro ou mais filhos dependentes; a IL propõe aumentar as deduções em IRS das rendas (de 502 para 1 800 euros) e dos juros do crédito à habitação (de 296 para 900 euros) e calcular a retenção na fonte dos trabalhadores independentes pela taxa efetiva média.

**faithfulness** — Is the claim supported by the CONTEXT?

- [ ] A Iniciativa Liberal propõe uma redução significativa das taxas marginais de IRS.
- [ ] A Iniciativa Liberal defende que o IRS deve ser menos progressivo para não desincentivar o trabalho e o investimento.
- [ ] A Iniciativa Liberal defende a simplificação do sistema de IRS para reduzir a complexidade das deduções e das categorias de rendimento.
- [ ] A Iniciativa Liberal propõe a elevação do limiar de isenção (mínimo de existência) para garantir que os rendimentos mais baixos não sejam tributados.
- [ ] A Iniciativa Liberal argumenta que a redução do IRS permite maior autonomia nas decisões de consumo e poupança dos contribuintes.
- [ ] O Chega propõe a descida das taxas de IRS com foco particular na redução da carga fiscal sobre os rendimentos médios e baixos.
- [ ] O Chega defende a isenção de IRS para quem recebe rendimentos próximos do salário mínimo ou de valores considerados baixos pela sua proposta.
- [ ] O Chega foca a sua retórica na necessidade de combater a corrupção e a fraude fiscal para garantir que a carga fiscal não precise de ser excessiva para manter o Estado.
- [ ] O Chega argumenta que as famílias portuguesas estão sobrecarregadas pelo sistema fiscal atual.
- [ ] O Chega propõe medidas que libertem rendimento disponível para o consumo das famílias.
- [ ] A Iniciativa Liberal foca-se numa reforma estrutural de natureza liberal visando a redução das taxas marginais e a simplificação do sistema.
- [ ] O Chega foca a sua proposta na isenção de rendimentos baixos e na redução da carga sobre a classe média, ligando a gestão fiscal ao combate à corrupção.

**correctness_recall** — Does the ANSWER state this reference claim?

- [ ] O CHEGA propõe uma taxa marginal de IRS de 15% para rendimentos até 39.999 euros.
- [ ] O CHEGA propõe uma taxa marginal de IRS de 30% para rendimentos a partir de 40.000 euros.
- [ ] O CHEGA propõe a isenção de IRS para quem recebe até 1.000 euros mensais.
- [ ] O CHEGA propõe a isenção de IRS para jovens até aos 35 anos até perfazerem 100.000 euros de rendimentos.
- [ ] A Iniciativa Liberal propõe uma taxa única de IRS de 15% sobre os rendimentos acima do salário mínimo nacional anualizado.
- [ ] A Iniciativa Liberal propõe manter as deduções à coleta no IRS.
- [ ] A Iniciativa Liberal propõe atingir a taxa única de 15% numa primeira fase através de duas taxas de 15% e 28%.
- [ ] O CHEGA propõe isentar de IRS o 15.º salário.
- [ ] O CHEGA propõe isentar de IRS as horas extraordinárias.
- [ ] O CHEGA propõe isentar de IRS as mulheres com quatro ou mais filhos dependentes.
- [ ] A Iniciativa Liberal propõe aumentar as deduções em IRS das rendas de 502 para 1.800 euros.
- [ ] A Iniciativa Liberal propõe aumentar as deduções em IRS dos juros do crédito à habitação de 296 para 900 euros.
- [ ] A Iniciativa Liberal propõe calcular a retenção na fonte dos trabalhadores independentes pela taxa efetiva média.

relevance: 

<details><summary>Context the generator read</summary>

## Iniciativa Liberal
[Documento 1]
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 1. MAIS OPORTUNIDADES, MAIS SALÁRIO > 1.2. Reforma Fiscal: Menos Impostos, Mais Salário > Impostos mais baixos e mais simples para todos
#### 1.2. Reforma Fiscal: Menos Impostos, Mais Salário  
##### Impostos mais baixos e mais simples para todos  
Portugal precisa de crescer. Esta é a principal bandeira que a Iniciativa Liberal defende desde que foi fundada. Esta necessidade de crescimento reflete-se no PIB per capita em paridades de poder de compra face à média da União Europeia. Portugal encontra-se praticamente estagnado desde 2011, com oscilações pouco significativas. Portugal mantém-se na cauda da Europa, sendo ultrapassado por 8 países desde o ano 2000. O crescimento não é meramente um capricho liberal: ele não só reflete a melhoria das condições de vida das pessoas, como é igualmente essencial para a melhoria no rácio da dívida pública sobre o produto e o respetivo cumprimento das regras orçamentais da União Europeia, sem colocar em causa o funcionamento do Estado Social e o investimento público.  
O país tem de ser fiscal e administrativamente competitivo, tirando peso e complexidade ao sistema fiscal atualmente vigente. **Portugal tem de deixar de ter uma das maiores taxas de esforço fiscal da União Europeia e passar a ter uma das menores**, como é o caso de países mais liberais como a Irlanda, o Luxemburgo e os Países Baixos. Segundo os dados do Eurostat, Portugal teve em 2022 a quarta maior taxa de esforço fiscal da Europa. Os portugueses não suportam mais esta situação.  
Hoje temos impostos de rico e salários de pobre. Além disso, temos um nível de progressividade enorme, com um recorde europeu de nove escalões, que pune quem quer subir na vida pelo trabalho. E temos um nível de tax wedge muito elevado, onde o Estado leva em média 42% do que a empresa paga por um trabalhador e onde o Estado leva cerca de metade do que a empresa paga por um aumento salarial. É isto que temos de mudar imediatamente. O sistema fiscal liberal recompensa o esforço, dedicação e produtividade daqueles que trabalham e aqueles que assumem riscos, estimulando assim a concorrência.  
Hoje, essa competição não se limita ao âmbito nacional, estendendo-se ao cenário continental e mesmo global. Portugal está em competição direta com o resto do mundo para atrair capital e empregos qualificados. Contudo, a carga fiscal excessiva sobre o trabalho e as empresas nas últimas décadas resultou numa significativa emigração de mão-de-obra altamente qualificada e desvio de investimento para outras regiões. É urgente alterar este panorama.  
**A Iniciativa Liberal defende a descida e simplificação dos impostos sobre rendimentos das pessoas e das empresas, nomeadamente do IRS e do IRC**, promovendo ainda a eliminação de casos de dupla tributação, bem como de taxas e contribuições coercivas que promovem complexidade e barreiras à entrada em mercados competitivos. Além disso, se a energia – neste caso eletricidade e gás – é um bem essencial quer para a vida das famílias quer para a atividade das empresas então não pode ser taxada como um bem de luxo, devendo **o IVA do gás e da eletricidade baixar para 6%**.  
Para crescermos, é também necessária a **revisão e redução de impostos sobre o património**, uma vez que se tratam de impostos que incidem sobre bens comprados por rendimentos que já foram tributados e sobre transações que também foram já tributadas. A Iniciativa Liberal apresenta igualmente alterações ao IMI, de forma a desonerar a detenção do património, bem como ao Imposto do Selo, ao IVA e ao IMT, para desonerar a construção e a aquisição da habitação própria e permanente na transação, medidas que são expressamente apresentadas no capítulo referente à Habitação.  
**Reduzir e Simplificar o IRS até à Taxa Única de 15%**  
Propomos **implementar uma taxa única de 15% a aplicar-se aos rendimentos acima do salário mínimo nacional anualizado**, garantindo a progressividade e mantendo as atuais deduções à coleta previstas.  
A Iniciativa Liberal mantém-se firme na sua proposta de reduzir a progressividade excessiva e simplificar o IRS para todos os contribuintes que têm de obrigatoriamente pagar o imposto, sem prejudicar os contribuintes isentos de IRS.  
Com a aplicação deste IRS substancialmente mais baixo para todos, serão igualmente revogados os atuais programas e benefícios fiscais dirigistas que causam injustiças sociais entre os mais jovens e não jovens, bem como entre os residentes e os não residentes.  
Estamos disponíveis para aprovar e desenvolver propostas transitórias, desde que se baixe significativamente a progressividade excessiva do imposto, reduzindo o número de escalões, e que se incentive claramente a competitividade fiscal dos salários de emprego qualificado. Mais concretamente, a Iniciativa Liberal **numa primeira fase propõe um imposto com duas taxas**, uma de 15% sobre os rendimentos acima de 11.480 euros e abaixo de 21.321 euros, **garantindo a progressividade**, sendo aplicada uma taxa de 28% acima desse patamar de rendimento anual. Em suma, pretende-se isentar de imposto os rendimentos mais baixos aumentando significativamente a dedução específica, agregando os primeiros quatro escalões e, por fim, agregando os últimos cinco escalões com a taxa de 28%. Eis alguns exemplos da poupança esperada por esta alteração.  
| Rendimento | Rendimento<br>Imposto   |          | Proposta de taxa única de 15% |                    |                 | Proposta transitória de 2 taxas |                    |                 |
| ---------- | ----------------------- | -------- | ----------------------------- | ------------------ | --------------- | ------------------------------- | ------------------ | --------------- |
| mensal     | bruto<br>bruto<br>anual | Atual \* | Imposto\*                     | Poupança<br>(abs.) | Poupança<br>(%) | Imposto \*                      | Poupança<br>(abs.) | Poupança<br>(%) |
| 900        | 12.600                  | 784      | 168                           | 616                | 79%             | 168                             | 616                | 79%             |
| 1.100      | 15.400                  | 1.667    | 588                           | 1.079              | 65%             | 588                             | 1.079              | 65%             |
| 1.300      | 18.200                  | 2.295    | 1.008                         | 1.287              | 56%             | 1.008                           | 1.287              | 56%             |
| 1.500      | 21.000                  | 2.952    | 1.428                         | 1.524              | 52%             | 1.428                           | 1.524              | 52%             |
| 1.700      | 23.800                  | 3.680    | 1.848                         | 1.832              | 50%             | 2.170                           | 1.510              | 41%             |
| 2.500      | 35.000                  | 7.397    | 3.528                         | 3.869              | 52%             | 5.306                           | 2.091              | 28%             |
| 4.000      | 56.000                  | 15.060   | 6.678                         | 8.382              | 56%             | 11.186                          | 3.874              | 26%             |  
\* – Imposto apurado antes de deduções à coleta. Estas deduções, mantendo-se, conforme proposto, são indiferentes para o apuramento da poupança entre o imposto atual e o imposto proposto.  
**Baixar o Imposto sobre rendimentos de capitais e prediais**  
Em matéria de tributação de rendimentos de capitais, mais-valias e prediais, a Iniciativa Liberal defende a **redução do imposto para 14,5%, sem englobamento obrigatório**. Em matéria de rendimentos prediais de arrendamento habitacional, propõe-se uma taxa 14.5% com uma descida gradual do imposto, conforme referido posteriormente no capítulo A.2 sobre Habitação.  
**Tributar stock-options no momento da realização da venda e não no exercício da opção**  
A Iniciativa Liberal quer corrigir o momento da tributação da conversão de opções sobre ações em ações para que a mesma ocorra no momento da alienação do ativo. Atualmente, existem duas formas de tributar a conversão de opções sobre ações em ações. A primeira é a prevista no Código de IRS, que prevê a tributação no período em que é exercida a opção e que dá o direito ao trabalhador de ter o número de ações correspondentes, com a valorização que possuem as ações à data da conversão. A segunda com a tributação a ocorrer apenas quando se der a mais- ou menos-valia das ações sobre a qual o trabalhador exerceu a sua opção, conferida pelo benefício fiscal criado por este Governo para os trabalhadores em start-ups. Esta situação cria uma tremenda **desigualdade entre contribuintes em circunstâncias idênticas**, levando a que os primeiros sejam, invariavelmente, prejudicados face aos segundos apenas por uma questão de tratamento fiscal.  
Da forma como está a ser aplicada a lei, há casos de trabalhadores que, não querendo beneficiar dos descontos de taxas que o benefício fiscal também concede, vêem-se na obrigação de se endividar para liquidar impostos. Isto sucede por causa de uma variação do valor das ações que poderão não conseguir liquidar por ainda não terem realizado qualquer tipo de mais-valia com as mesmas. Ou seja, pagam impostos por uma mais-valia esperada, muitas vezes pressionados por apertados prazos de exercício de conversão de opções de ações, sem conhecimento da valorização das mesmas no momento da decisão do exercício das opções.  
A forma mais adequada para garantir um tratamento justo, informado e a capacidade contributiva dos contribuintes é **tributar esta conversão de opção de ação em ação como rendimento de trabalho apenas quando essa ação gerar uma mais ou menos valia na sua alienação**, tal como previsto no benefício fiscal recentemente criado pelo Governo.  
**Baixar e Simplificar o IRC**

[Documento 2]
  Secção: PROGRAMA ELEITORAL > PORTUGAL A CRESCER > 1. BAIXAR IMPOSTOS E DESBUROCRATIZAR
### 1. BAIXAR IMPOSTOS E DESBUROCRATIZAR  
- **Taxa única de IRS de 15% sobre a parte dos rendimentos que exceda o Salário Mínimo Nacional, começando de forma gradual com duas taxas de 15% e 28%, aumentando imediatamente o salário líquido**
- **Reduzir a carga fiscal sobre os profissionais liberais e os trabalhadores independentes**
- **Taxa única de IRC de 12% para as empresas, excepto para as grandes multinacionais que será de 15% de acordo com o exigido pela lei europeia**
- **Criar uma task force de eliminação de burocracias desnecessárias em diálogo com cidadãos e empresas**
- **Criar Zonas Económicas Especiais (ZEE) de baixa fiscalidade no interior do país para atrair investimento direto estrangeiro e promover a criação de hubs empresariais**
- **Reverter as normas do pacote Mais Habitação relativas ao Alojamento Local, eliminar a redução do coeficiente fiscal**
- **Eliminar várias taxas e contribuições extraordinárias como o adicional ao IMI (AIMI) e o imposto do selo sobre transações já taxadas**
- **Eliminar gradualmente o Imposto Único de Circulação (IUC)**
- **Reduzir o imposto sobre rendimentos de capitais para 14,5%**
- **Compromisso de Orçamentos com superávit e redução da dívida pública**

[Documento 3]
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 4.TRABALHO: MENOS RESTRIÇÕES, MAIS OPORTUNIDADES > 4.3. Valorizar os profissionais liberais e trabalhadores independentes
**Alargar direitos de parentalidade a profissionais liberais e trabalhadores independentes**  
No âmbito do processo de especialidade do Orçamento do Estado para 2024, a Iniciativa Liberal bateu-se pela eliminação da discriminação dos profissionais liberais e trabalhadores independentes na proteção social na parentalidade. Os trabalhadores independentes beneficiários do sistema previdencial têm direito ao subsídio parental, mas na prática, pela natureza da sua atividade, não há igualdade face aos trabalhadores por conta de outrem. Por exemplo, o período de referência para cálculo do montante do subsídio não prevê oscilações inerentes à sua atividade e não está prevista a diminuição do horário laboral para a amamentação.  
A proposta de alteração aprovada previa que já este ano o Governo estudasse a possibilidade e as condições de **integração dos profissionais liberais e trabalhadores independentes nos regimes de licenças de parentalidade, de forma a terem efetivamente direitos parentais equiparados aos dos trabalhadores por** **conta de outrem**. Esta integração é complexa e tem implicações a diferentes níveis, pelo que é pertinente a realização urgente de um estudo que identifique todas as implicações – legislativas e financeiras – de diferentes alternativas. Tendo em conta as conclusões e recomendações do estudo, a Iniciativa Liberal compromete-se a implementar as medidas mais adequadas para garantir a igualdade efetiva das condições parentais entre todos os trabalhadores, nomeadamente das licenças parentais e do período de amamentação. conciliação entre vida profissional e pessoal. As medidas terão em conta as condições sobretudo das mães (mas também dos pais), apoiando os projetos de família, de vida e de felicidade a milhares de trabalhadores independentes e profissionais liberais.  
**Flexibilizar o acesso a creches para filhos de profissionais liberais e trabalhadores independentes**  
A natureza da atividade profissional de alguns profissionais liberais e trabalhadores independentes é muitas vezes incompatível com ausências prolongadas, nomeadamente após o nascimento de um(a) filho(a). São exemplos deste cenário, advogados que poderão ter de estar presentes em tribunal ou donos de lojas, sendo ainda mais grave no caso em que ambos os pais estão nesta situação, obrigando-os a fazer sacrifícios profissionais ou pessoais, como o adiamento ou abandono de projetos parentais. Nestes casos, é necessário garantir acesso a serviços de cuidados à primeira infância mais cedo do que os adequados aos trabalhadores por conta, que têm direito a licenças de parentalidade de 120 dias.  
No entanto, atualmente, as creches e creches familiares só estão autorizadas a cuidar de crianças a partir dos 3 meses de idade. Propomos **flexibilizar em duas vertentes o** **acesso a creches a crianças cujos ambos os pais sejam profissionais liberais ou trabalhadores independentes**: na idade, permitindo prestar cuidados a crianças com menos do que 3 meses; e na duração, permitindo que o cuidado a essas crianças com menos de 3 meses seja prestado em períodos avulsos, flexíveis ou irregulares (por exemplo, 1 dia, 2 dias por semana, 1 semana por mês).  
**Alargar a isenção sobre rendimentos a trabalhadores-estudantes independentes**  
Em paralelo, a desigualdade de tratamento estende-se também à conjugação entre o trabalho e os estudos. Recentemente, houve um avanço legislativo importante que beneficiou os jovens trabalhadoresestudantes, permitindo que **parte de seus rendimentos de trabalho dependente não sejam considerados para efeitos de atribuição de prestações sociais**. No entanto, os trabalhadores independentes não foram abrangidos por essa alteração.  
Ainda para mais, devido ao carácter sazonal, experimental ou até pela tipologia de atividade (por exemplo, artística ou tecnológica), esta opção afigura-se contraproducente não só por deixar de fora grande parte dos possíveis estudantes, mas também por ser um **desincentivo à livre iniciativa, à entrada no mercado de trabalho e à assunção de riscos**. No limite, **bloqueiam-se oportunidades e fomenta-se a informalidade** e a ilegalidade.  
Os estudantes, independentemente do seu estatuto laboral, devem ter igual acesso a oportunidades educacionais e de inserção no mercado de trabalho. É importante que a legislação seja ajustada para garantir que ambos os grupos sejam tratados de maneira justa e equitativa.  
**Defender a justiça fiscal para os profissionais liberais e trabalhadores independentes**  
A Iniciativa Liberal propõe um conjunto de medidas fiscais aplicáveis aos profissionais liberais e trabalhadores independentes, das quais se destacam:  
- Aumentar o valor de rendimentos passíveis da isenção do pagamento de IVA de 20.000 euros para 25.000 euros;
- Aumentar o valor de rendimentos passíveis de isenção de contribuições para a Segurança Social quando o trabalhador acumule o trabalho independente com o trabalho por conta de outrem de quatro vezes o valor do Indexante dos Apoios Sociais (2.037,04 euros) para 25.000 euros;
- Simplificar o valor da retenção de rendimentos dos profissionais liberais e trabalhadores independentes em sede de IRS, propondo que o montante da retenção seja apurado pela taxa de imposto efetiva média aplicada aos profissionais liberais e trabalhadores independentes em Portugal no período anterior.

## CHEGA
[Documento 4]
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > VIII CAPÍTULO MAIS RENDIMENTOS PARA AS FAMÍLIAS E EMPRESAS. COMO? > PROPOSTAS
### PROPOSTAS  
**181.** Introduzir duas taxas marginais de IRS: de 15% até aos 39.999 euros e de 30% a partir de 40.000 euros, com isenção de pagamento para quem receber até aos mil euros mensais.  
**182.** Isentar os jovens até aos 35 anos de IRS até perfazerem um total de 100 mil euros de rendimentos desde o início da sua carreira.  
**183.** Isentar de IRS o designado "15.º salário", sem quaisquer condicionantes.  
**184.** Introduzir uma _flat tax_ de IRC de 15% para as regiões autónomas e para o interior do país e de 18% para o resto do território.  
**185.** Criar um modelo de número único de identificação para as pessoas e empresas, assim evitando que a mesma pessoa tenha que ter número de utente, de cartão de cidadão, de contribuinte, de Segurança Social, de eleitor, etc.  
**186.** Eliminar o adicional do IMI; isentar de IMI e de IMT a compra de habitação própria e permanente, assim como a tributação de mais-valias da venda de habitação própria e permanente, desde que seja reinvestida na compra de uma nova habitação própria e permanente mesmo que de valor inferior para si ou para descendentes directos, no pagamento de empréstimos bancários, ou no caso dos reformados/pré-reforma.  
**187.** Aplicar a taxa de IVA reduzida (6%) à Electricidade e ao Gás e implementar uma tarifa social da energia para famílias numerosas, considerando os primeiros 200 kWh consumidos por família/mês, desde que a potência contratada não ultrapasse os 10,35kVA.  
**188.** Reintroduzir o IVA zero para bens alimentares essenciais e proceder ao alargamento da lista anteriormente aprovada, assim como aplicar a taxa de IVA reduzida (6%) para a restauração.  
**189.** Reduzir o IVA do Gasóleo e da Gasolina Rodoviária para a taxa intermédia de 13% e eliminar o adicional ao Imposto Sobre Produtos Petrolíferos.  
**190.** Terminar com a dupla tributação na compra de carro novo e com o cálculo indevido do ISV quando se trata de veículos usados matriculados noutro Estado-membro da União Europeia.  
**191.** Implementar medidas que permitam que as Cooperativas, Fundações, Instituições Particulares de Solidariedade Social (IPSS), Santas Casas da Misericórdia, Mutualidades e Associações de reconhecido interesse público sem carácter lucrativo possam deduzir/recuperar 100% do valor do IVA que lhes é cobrado nas aquisições internas, nas aquisições intracomunitárias e nas prestações de serviços.  
**192.** Aplicar a taxa autónoma de 10% aos rendimentos provenientes de rendas de contratos estabelecidos com alunos do ensino superior e aos rendimentos decorrentes de contratos de arrendamento para habitação permanente celebrados com duração inferior a dez anos; aos contratos  
com o mesmo fim, mas celebrados com prazo superior a 10 anos, a taxa autónoma aplicável é de 5%.  
**193.** Proceder à revisão do actual Regime Geral das Infracções Tributárias, promovendo a simplificação processual, reformulando a organização judiciária e tributária e estabelecendo um novo regime geral para as infracções tributárias.  
**194.** Implementar apoio jurídico e mediação gratuita para a defesa de pequenos contribuintes junto da Administração Tributária quando estejam em causa pequenos montantes de impostos ou outros tributos e/ou execuções fiscais de pequeno valor.  
**195.** Tornar as normas fiscais mais objectivas e claras:  
- Evitando complexidades desnecessárias e, consequentemente, reduzindo litígios;  
- Pugnando pela publicação atempada de todas as orientações da Autoridade Tributária (AT), assim trazendo mais transparência e clareza à interpretação feita pela AT e contribuindo para a uniformização de procedimentos;  
- Através da promoção da publicação de Códigos anotados, pela própria Assembleia da República, como já aconteceu na década de 80, assim facilitando o cumprimento das normas por parte dos contribuintes.  
**196.** Reforçar os meios técnicos e humanos da AT para o combate à fraude e à evasão fiscal e melhorar os meios (inclusivamente legais) para o apuramento de manifestações de fortuna, nomeadamente, através da comunicação à AT do nome e NIF dos adquirentes de determinados bens de luxo.  
**197.** Promover de forma activa a reintegração dos valores da economia paralela na economia lícita, quer através da simplificação fiscal, quer do aumento significativo da fiscalização nesta matéria, com o objectivo de recuperar 20%/ ano estes montantes para a economia nacional.  
**198.** Criar o protocolo "zero economia paralela", com o objectivo de em seis anos recuperar tendencialmente todos os valores movimentados no âmbito da economia paralela para a economia nacional (cerca de 89 mil milhões de euros ano).  
**199.** Transferir para o sector das telecomunicações a taxa sobre o Audiovisual, retirando-a da factura de electricidade e atribuindo o seu pagamento às empresas de telecomunicações a operar em Portugal  
**200.** Criar um regime geral de taxas, simplificando todo o regime e concentrando todos as taxas num só diploma, assim facilitando o conhecimento e cumprimento, conforme proposta apresentada pela CIP.  
**201.** Reforçar a inventariação do património imobiliário do Estado com vista à sua utilização, alienação ou arrendamento.  
**202.** Avaliar todas as empresas que integram o sector público estatal, racionalizando a sua quantidade e abrindo ao sector privado a sua operação e incorporar os trabalhadores, preferencialmente nas empresas privadas criadas para o efeito e redireccionar os restantes para serviços deficitários do Estado (nacional, regional ou local), de acordo com as expectativas dos trabalhadores e das necessidades existentes.  
**203.** Criar uma contribuição extraordinária temporária sobre o sector bancário, aplicável aos lucros excedentários apurados nos períodos de tributação para efeitos do IRC que se iniciem nos anos de 2024 e 2025 e manter a Contribuição do Sector Bancário já existente e aumentá-la em 10%.  
**204.** Criar uma contribuição extraordinária temporária sobre as petrolíferas e distribuidoras, aplicável aos lucros excedentários apurados nos períodos de tributação para efeitos do IRC que se iniciem nos anos de 2024 e 2025, assegurando que a mesma não se reflicta no agravamento de preços ao consumidor final.  
**205.** Criar mecanismos de aceleração de recuperação de dívidas ao Estado para que, por um lado seja garantida a justiça social, acabando com a impunidade sobre os infractores e, por outro, não se perca uma importante fonte de receita.

[Documento 5]
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > VIII CAPÍTULO O QUE JÁ FIZEMOS PARA DAR MAIS RENDIMENTOS ÀS FAMÍLIAS E EMPRESAS
## VIII CAPÍTULO O QUE JÁ FIZEMOS PARA DAR MAIS RENDIMENTOS ÀS FAMÍLIAS E EMPRESAS  
**PROPOSTA DE ALTERAÇÃO OE24 Nº177C (CH)**  
N.º 1, N.º 2, N.º 5, Artigo 87.º do código do IRC, constante do Artigo 144.º da PPL / Imposto sobre o rendimento das pessoas coletivas.  
**PROPOSTA DE ALTERAÇÃO OE24 Nº1507C (CH)** Artigo 173.º-A (Contribuição extraordinária sobre o sec-  
**REJEITADO**  
**CONTRA** Partido Socialista, PSD, PCP, BE, L **ABSTENÇÃO** PAN **FAVOR** CHEGA, IL  
**REJEITADO**  
**CONTRA** Partido Socialista, PSD, IL **ABSTENÇÃO** PCP, L **FAVOR** CHEGA, BE, PAN  
**PROPOSTA DE ALTERAÇÃO OE 24 Nº 1590C (CH)**  
Artigo 161.º-A (Redução do valor do IUC)  
tor bancário)  
**REJEITADO**  
**CONTRA** Partido Socialista, PSD, PCP, BE, PAN, L **ABSTENÇÃO** IL **FAVOR** CHEGA  
**PROPOSTA DE ALTERAÇÃO OE24 Nº 1503C**  
Verba 2.9, Lista II anexa ao Código do IVA / Alteração ao Código do Imposto sobre o Valor Acrescentado - IVA Gasolina e Gasóleo Rodoviário  
**PROPOSTA DE ALTERAÇÃO OE24 Nº 1486C**  
Ponto 2, Alínea b), N.º 3, Artigo 2.º do Código do IRS / Aumento para 80% da dedutibilidade do subsídio de alimentação.  
**REJEITADO**  
**CONTRA** Partido Socialista, PSD, PCP, BE, PAN, L **ABSTENÇÃO** IL **FAVOR** CHEGA  
**REJEITADO**  
**CONTRA** Partido Socialista, PSD **ABSTENÇÃO** IL, PCP, BE, PAN, L **FAVOR** CHEGA

[Documento 6]
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > VIII CAPÍTULO MAIS RENDIMENTOS PARA AS FAMÍLIAS E EMPRESAS. COMO? > PRIORIDADES
### PRIORIDADES  
- Garantir mais rendimentos para as famílias e permitir que saiam da situação de asfixia financeira em que muitas, apesar de trabalharem, se encontram;  
- Acabar com o saque fiscal às empresas e promover o investimento;  
- Redução do impostos e adopção de outras medidas para combater a fraude e evasão fiscal através da uma adequada política de justiça fiscal;  
- Assegurar uma maior fiscalização na alocação de benefícios fiscais e apoios sociais por forma a garantir que só aqueles que realmente precisam é que são apoiados;  
- Simplificar e desburocratizar o sistema fiscal para garantir uma maior transparência e certeza jurídica, desta forma aumentando também a confiança do contribuinte no sistema.

[Documento 7]
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > VIII CAPÍTULO MAIS RENDIMENTOS PARA AS FAMÍLIAS E EMPRESAS. COMO?
## VIII CAPÍTULO MAIS RENDIMENTOS PARA AS FAMÍLIAS E EMPRESAS. COMO?  
**M**ais de vinte e cinco anos de estagnação eco-nómica, injustiça social, empobrecimento e perda do poder de compra levaram à desmotivação geral dos portugueses.  
A política fiscal seguida nas últimas décadas é totalmente desadequada, perseguindo por inúmeras vezes o processo de criação de riqueza, penalizando os salários de quem mais trabalha e mais se esforça, as empresas que potencializam o seu crescimento e criam emprego.  
Sem crescimento, as famílias e as empresas não têm futuro e os jovens mais qualificados têm tendência para abandonar Portugal, rumando a novos horizontes, onde possam viver condignamente e com qualidade.  
Sem criação de riqueza, e com uma carga fiscal cada vez mais pesada, empresas e famílias veem-se com recursos cada vez mais limitados e impossibilitadas de contribuir para causas solidárias. O sistema actual parece estar preso numa espiral auto-destrutiva, onde os principais beneficiados são, lamentavelmente, as clientelas políticas.  
A agravar esta situação está também a falta de transparência dos impostos. Nem as pessoas, nem as empresas compreendem como são calculados e como lhes são aplicados. O IRS, IRC e a infinidade de taxas e contribuições sobre as pessoas e empresas são tão complexos que ninguém consegue saber, com a devida certeza, quanto é que vai pagar de impostos se tiver um determinado rendimento no início de cada ano.  
Esta situação de incerteza fiscal é um obstáculo evidente à captação de investimento interno ou externo e/ou até incentivar os trabalhadores a trabalharem mais.  
A segurança jurídica dos cidadãos e empresas é um bem universal e basilar para o bom funcionamento da democracia. Mesmo sendo diligentes e cuidadosos no apuramento do imposto, não conseguem estar seguros de que não serão notificados com correcções por parte da Administração Fiscal, não sendo, posteriormente, a obtenção de esclarecimentos sobre o assunto de fácil acesso. Na verdade, isso leva a que as pessoas se sintam extremamente inseguras sobre a liquidação de impostos, o que mais uma vez as desmotiva de iniciarem novos negócios ou de se esforçarem de forma a obter um melhor salário.  
Além disso, os investidores estrangeiros afirmam que em Portugal é muito caro trabalhar, visto que os impostos são muito altos e penalizam severamente quem se esforça e pretende criar rendimento, para manter condignamente a sua família.  
Isto frustra e desmotiva quer quem trabalha, quer a empresa que pretende premiar condignamente quem desempenha as suas funções com qualidade e profissionalismo.  
A agravar isto, todos sabemos que muita desta receita fiscal é mal-usada e serve para alimentar a máquina do Estado. Isto leva a que exportemos jovens altamente qualificados para países com fiscalidades mais baixas, e "importemos" pessoas sem qualificação nenhuma e com poucas perspectivas de criar riqueza em Portugal.  
Ao mesmo tempo, a fiscalidade sobre o imobiliário tem-se agravado nos últimos 20 anos, sendo um factor determinante dos elevados preços da habitação, que é um direito fundamental tutelado constitucionalmente. É incompreensível que uma família tenha de pagar IMT para adquirir a sua habitação própria e permanente, ou mais valias se tiver de trocar de casa para ir viver noutra parte do país, onde encontra melhores oportunidades de emprego ou de qualidade de vida (necessidade de mobilidade geográfica).  
O mesmo se passa com a venda de habitação própria e permanente das pessoas de idade, que precisam dessa receita para fazer face à degradação cada vez mais acentuada das reformas ou às dificuldades que encontram nos seus últimos anos de vida – custos como saúde, medicamentos, lares, tratamentos, etc.  
Não deve existir nem nunca devia ter existido IMI sobre a habitação própria e permanente de qualquer pessoa. A casa é um refúgio sagrado que as pessoas não devem nunca perder por não poderem pagar um imposto absolutamente injusto. Todos passamos por dificuldades na vida, a título de exemplo, por vezes um casal perde totalmente as suas fontes de rendimento e o Estado, mesmo assim, quer ir buscar o IMI, tirando-lhe o tecto onde vive com a sua família numa situação em que se encontra especialmente fragilizado.  
Também não é aceitável que as IPSS e outras entidades que se dedicam à educação e caridade dos cidadãos mais desfavorecidos e mais frágeis sejam sujeitas a inúmeros impostos que tornam mais difícil cumprir a sua missão de apoiar os que mais precisam.  
Não podemos deixar de mencionar igualmente a necessidade de proceder à harmonização das taxas municipais a nível nacional, por forma a que as pessoas e empresas percebam o que estão a pagar e porquê.  
É também imperativo tornar o sistema fiscal mais simples e transparente. Mais simples porque a burocracia sobre as pessoas e empresas leva a que estas dediquem muito do seu tempo de vida a cumprir obrigações que não geram qualquer mais-valia para o Estado e apenas infernizam a vida das pessoas e empresários.  
Queremos com isto criar um sistema mais transparente, mais seguro para os cidadãos e empresas, mais justo, e mais equitativo

[Documento 8]
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > IX CAPÍTULO JOVENS COM UM FUTURO EM PORTUGAL. COMO? > PROPOSTAS
### PROPOSTAS  
**206.** Criar um programa de apoio aos jovens portugueses para compra de habitação própria e permanente, nomeadamente através da assunção da garantia bancária por parte do Estado quanto ao valor da entrada de uma casa e disponibilização de linhas de crédito bonificado para jovens.  
**207.** Isentar os jovens do pagamento de IMI, IMT e Imposto de Selo na compra da primeira habitação.  
**208.** Aprovar benefícios fiscais para jovens casais portugueses que se fixem no interior, que tenham três ou mais filhos, ou reabilitem património devoluto.  
**209.** Ampliar o leque de beneficiários do programa Porta 65 Jovem, assegurando o direito à habitação jovem.  
**210.** Introduzir conteúdos de Literacia Financeira no programa escolar para o 3º ciclo do Ensino Básico e Ensino Secundário.  
**211.** Priorizar a saúde mental dos jovens, nomeadamente através do reforço da prevenção do suicídio jovem; reforço dos profissionais de psicologia; rastreios em estabelecimentos de Ensino e intensificar o combate ao bullying e cyberbulling em contexto escolar.  
**212.** Alterar os prazos de prescrição dos crimes sexuais contra menores e de mutilação genital feminina.  
**213.** Elevar para 18 anos a idade mínima para contrair casamento.  
**<sup>3</sup>** Eco, "Percentagem de jovens com casa própria caiu a pique nos últimos 20 anos", 2023.  
**<sup>4</sup>** Diário de Notícias, "Sair de casa dos pais é objectivo dos jovens portugueses. Mas não conseguem", 2022.  
**214.** Atribuir o complemento de residência a todos os estudantes provenientes de agregados familiares de rendimento anual inferior aos constantes do limite do 6º escalão de IRS.  
**215.** Promover o combate à cultura woke e ideologia de género que quer entrar na sociedade portuguesa através dos estabelecimentos de ensino.  
**216.** Incluir o ensino de História de Portugal gratuito no estrangeiro para crianças e jovens Portugueses e Lusodescendentes e criar um programa online de aprendizagem de Português no estrangeiro.  
**217.** Criar medidas específicas no Programa Regressar, tendo em vista o regresso dos jovens portugueses emigrados.  
**218.** Aplicar em Portugal o modelo britânico de Propina, isentando os jovens do pagamento da mesma no período de frequência do Ensino Superior, sendo expectável a devolução do empréstimo ao Estado de forma faseada, após a inserção no mercado de trabalho de forma estável.  
**219.** Alargar a gratuidade do passe para todos os jovens estudantes ou trabalhadores até aos 30 anos.  
**220.** Isentar os jovens até aos 35 anos de IRS, até perfazerem um total de 100 mil euros de rendimentos desde o início da sua carreira.  
**221.** Isentar progressivamente de IRC os jovens empresários, jovens agricultores e empreendedores, até aos 35 anos.  
**222.** Possibilitar a tributação autónoma à taxa reduzida de 10% aplicável aos rendimentos relativos a contratos de alojamento celebrados com estudantes do ensino superior.  
**223.** Proceder à revisão e execução do Plano Nacional do Alojamento Estudantil para garantir o aumento de camas, a curto prazo.  
**224.** Criar um Programa Nacional de co-living para combater a solidão dos idosos e a falta de alojamento acessível para estudantes.  
**225.** Combater o desemprego jovem que é um dos maiores dramas dos jovens portugueses, nomeadamente através da redução temporária de 50% da taxa contributiva da responsabilidade da entidade empregadora relativamente à contratação de jovens à procura do primeiro emprego, até estes perfazerem os 30 anos de idade.  
**226.** Aperfeiçoar a relação dos estabelecimentos de ensino profissional e universidades com o mundo profissional para que haja um ajuste cada vez mais claro e actual das necessidades do mercado de trabalho e das vocações de cada jovem no seu concreto.  
**227.** Garantir que os jovens podem beneficiar do estatuto trabalhador-estudante em todos os ciclos de estudo, isentando-os do pagamento de taxas e emolumentos.  
**228.** Assegurar que, até um determinado limite, os rendimentos auferidos pelos estudantes não têm implicações fiscais ou sobre o direito a bolsas ou outras prestações, conforme proposta da CIP.

</details>

## item-09

**Question:** Que propostas existem para resolver as listas de espera no SNS?

**Answer:**

As propostas para a resolução das listas de espera no Serviço Nacional de Saúde (SNS) variam significativamente entre as forças políticas, focando-se em diferentes modelos de gestão e financiamento:

**Aliança Democrática (AD)**
• Propõe o reforço do **pagamento de incentivos financeiros** aos profissionais de saúde para reduzir o tempo de espera.
• Defende a criação de **centros de especialidades** para descentralizar o atendimento.
• Prevê o reforço da capacidade de resposta através de **parcerias com o setor privado e social**, utilizando a capacidade instalada de outras instituições para realizar consultas e cirurgias.
• Propõe a criação de uma **unidade de gestão de listas de espera** para monitorizar e acelerar processos.

**Partido Socialista (PS)**
• Defende o reforço dos **serviços de proximidade** e das Unidades de Saúde Familiar (USF) para evitar a sobrecarga dos hospitais.
• Propõe a criação de **equipas móveis** e o reforço da medicina preventiva.
• Foca-se na **contratação de mais médicos e enfermeiros** através de concursos públicos e regimes de dedicação plena.
• Argumenta que a solução passa pelo reforço dos recursos humanos e pela melhor organização interna dos hospitais públicos.

**Bloco de Esquerda (BE)**
• Propõe o **investimento massivo no setor público**, rejeitando a transferência de fundos para o setor privado.
• Defende a **redução do horário de trabalho** dos profissionais de saúde para combater o *burnout* e aumentar a retenção de talento.
• Sugere a criação de **centros de saúde com horário alargado** para reduzir as urgências hospitalares.
• Propõe o aumento do número de profissionais através de concursos públicos mais atrativos e com melhores condições laborais.

**Chega**
• Defende a **reorganização da gestão hospitalar**, sugerindo modelos de gestão mais eficientes e menos dependentes da política.
• Propõe o **reforço da fiscalização** sobre o tempo de espera e o cumprimento de metas.
• Sugere a utilização de **mecanismos de incentivo direto** aos profissionais que cumpram metas de redução de listas de espera.

**Iniciativa Liberal (IL)**
• Defende a **introdução de mecanismos de mercado** e maior concorrência para baixar os tempos de espera.
• Propõe o **fortalecimento do setor privado e social** como complemento essencial ao SNS, através de parcerias que permitam ao Estado "comprar" serviços para escoar listas de espera.
• Defende a **liberdade de escolha** do utente, permitindo que este possa ser atendido noutras instituições se o SNS não cumprir os prazos.

**Livre**
• Propõe o reforço do **SNS como serviço público universal**, combatendo a privatização.
• Defende o aumento do **número de profissionais de saúde** através de melhores condições de carreira.
• Sugere o investimento em **cuidados de saúde primários** para evitar o congestionamento das urgências.

**PCP**
• Defende o **investimento público direto** na contratação de pessoal e compra de equipamentos.
• Propõe o **reforço dos cuidados de saúde primários** e a descentralização dos serviços para as zonas mais periféricas.
• Argumenta que a solução passa pela **rejeição de modelos de gestão privada** e pelo reforço do controlo estatal sobre os recursos de saúde.

**PAN**
• Propõe o reforço dos **cuidados de saúde de proximidade** para evitar o encaminhamento desnecessário para hospitais.
• Defende a melhoria das condições de trabalho dos profissionais para garantir a continuidade dos cuidados.

**Reference answer:**

A AD propõe um Plano de Emergência do SNS 2024-2025 com um Voucher Consulta de Especialidade, que dá liberdade de escolha do prestador quando o Tempo Máximo de Resposta Garantido (TMRG) é ultrapassado, contratos temporários com médicos de família aposentados ou privados, novos incentivos no SIGIC, auditorias aos TMRG na rede hospitalar e o cumprimento dos TMRG para doentes oncológicos até final de 2027. A IL propõe um Programa Especial de Acesso a Cuidados de Saúde que contratualiza, por concurso público internacional, consultas de especialidade e cirurgias sempre que os TMRG não forem cumpridos, a par de carreiras mais atrativas e liberdade de contratação direta pelas instituições do SNS. O CHEGA propõe que, esgotados os TMRG, o Estado seja obrigado a referenciar os utentes para os setores privado ou social. O BE propõe a abertura imediata de concursos de contratação onde os tempos de espera excedem o recomendado, apoios à fixação em zonas carenciadas, a redução para 12 horas do horário semanal de urgência dos médicos para libertar tempo para consultas e cirurgias, a desburocratização e a realização dos exames no próprio SNS, no próprio dia ou em prazo muito curto, com uma rede pública de Centros de Diagnóstico e Terapêutica. O PCP propõe um programa de emergência para recuperar as listas de espera em consultas, cirurgias, exames e tratamentos, assente sobretudo no aumento da capacidade dos serviços públicos. O LIVRE propõe garantir os direitos dos utentes nos tempos de resposta e reduzir as listas de espera para tratamentos de PMA, e o PS propõe Percursos Assistenciais Integrados que ajudem a cumprir os tempos de espera sem retirar ao SNS a responsabilidade pelos utentes.

**faithfulness** — Is the claim supported by the CONTEXT?

- [ ] A Aliança Democrática (AD) propõe o reforço do pagamento de incentivos financeiros aos profissionais de saúde para reduzir o tempo de espera no SNS.
- [ ] A Aliança Democrática (AD) defende a criação de centros de especialidades para descentralizar o atendimento no SNS.
- [ ] A Aliança Democrática (AD) prevê o reforço da capacidade de resposta no SNS através de parcerias com o setor privado e social para realizar consultas e cirurgias.
- [ ] A Aliança Democrática (AD) propõe a criação de uma unidade de gestão de listas de espera para monitorizar e acelerar processos no SNS.
- [ ] O Partido Socialista (PS) defende o reforço dos serviços de proximidade e das Unidades de Saúde Familiar (USF) para evitar a sobrecarga dos hospitais.
- [ ] O Partido Socialista (PS) propõe a criação de equipas móveis e o reforço da medicina preventiva no SNS.
- [ ] O Partido Socialista (PS) foca-se na contratação de mais médicos e enfermeiros através de concursos públicos e regimes de dedicação plena.
- [ ] O Partido Socialista (PS) argumenta que a solução para as listas de espera passa pelo reforço dos recursos humanos e pela melhor organização interna dos hospitais públicos.
- [ ] O Bloco de Esquerda (BE) propõe o investimento massivo no setor público de saúde, rejeitando a transferência de fundos para o setor privado.
- [ ] O Bloco de Esquerda (BE) defende a redução do horário de trabalho dos profissionais de saúde para combater o burnout e aumentar a retenção de talento.
- [ ] O Bloco de Esquerda (BE) sugere a criação de centros de saúde com horário alargado para reduzir as urgências hospitalares.
- [ ] O Bloco de Esquerda (BE) propõe o aumento do número de profissionais de saúde através de concursos públicos mais atrativos e com melhores condições laborais.
- [ ] O Chega defende a reorganização da gestão hospitalar, sugerindo modelos de gestão mais eficientes e menos dependentes da política.
- [ ] O Chega propõe o reforço da fiscalização sobre o tempo de espera e o cumprimento de metas no SNS.
- [ ] O Chega sugere a utilização de mecanismos de incentivo direto aos profissionais que cumpram metas de redução de listas de espera.
- [ ] A Iniciativa Liberal (IL) defende a introdução de mecanismos de mercado e maior concorrência para baixar os tempos de espera no SNS.
- [ ] A Iniciativa Liberal (IL) propõe o fortalecimento do setor privado e social como complemento essencial ao SNS, através de parcerias que permitam ao Estado comprar serviços para escoar listas de espera.
- [ ] A Iniciativa Liberal (IL) defende a liberdade de escolha do utente, permitindo que este possa ser atendido noutras instituições se o SNS não cumprir os prazos.
- [ ] O Livre propõe o reforço do SNS como serviço público universal, combatendo a privatização.
- [ ] O Livre defende o aumento do número de profissionais de saúde através de melhores condições de carreira.
- [ ] O Livre sugere o investimento em cuidados de saúde primários para evitar o congestionamento das urgências.
- [ ] O PCP defende o investimento público direto na contratação de pessoal e compra de equipamentos de saúde.
- [ ] O PCP propõe o reforço dos cuidados de saúde primários e a descentralização dos serviços para as zonas mais periféricas.
- [ ] O PCP argumenta que a solução para as listas de espera passa pela rejeição de modelos de gestão privada e pelo reforço do controlo estatal sobre os recursos de saúde.
- [ ] O PAN propõe o reforço dos cuidados de saúde de proximidade para evitar o encaminhamento desnecessário para hospitais.
- [ ] O PAN defende a melhoria das condições de trabalho dos profissionais de saúde para garantir a continuidade dos cuidados.

**correctness_recall** — Does the ANSWER state this reference claim?

- [ ] A AD propõe um Plano de Emergência do SNS 2024-2025.
- [ ] A AD propõe um Voucher Consulta de Especialidade.
- [ ] O Voucher Consulta de Especialidade da AD dá liberdade de escolha do prestador quando o Tempo Máximo de Resposta Garantido (TMRG) é ultrapassado.
- [ ] A AD propõe contratos temporários com médicos de família aposentados.
- [ ] A AD propõe contratos temporários com médicos de família privados.
- [ ] A AD propõe novos incentivos no SIGIC.
- [ ] A AD propõe auditorias aos TMRG na rede hospitalar.
- [ ] A AD propõe o cumprimento dos TMRG para doentes oncológicos até final de 2027.
- [ ] A IL propõe um Programa Especial de Acesso a Cuidados de Saúde.
- [ ] O Programa Especial de Acesso a Cuidados de Saúde da IL contratualiza consultas de especialidade por concurso público internacional sempre que os TMRG não forem cumpridos.
- [ ] O Programa Especial de Acesso a Cuidados de Saúde da IL contratualiza cirurgias por concurso público internacional sempre que os TMRG não forem cumpridos.
- [ ] A IL propõe carreiras mais atrativas.
- [ ] A IL propõe liberdade de contratação direta pelas instituições do SNS.
- [ ] O CHEGA propõe que, esgotados os TMRG, o Estado seja obrigado a referenciar os utentes para o setor privado.
- [ ] O CHEGA propõe que, esgotados os TMRG, o Estado seja obrigado a referenciar os utentes para o setor social.
- [ ] O BE propõe a abertura imediata de concursos de contratação onde os tempos de espera excedem o recomendado.
- [ ] O BE propõe apoios à fixação em zonas carenciadas.
- [ ] O BE propõe a redução para 12 horas do horário semanal de urgência dos médicos.
- [ ] A redução do horário semanal de urgência dos médicos proposta pelo BE visa libertar tempo para consultas e cirurgias.
- [ ] O BE propõe a desburocratização.
- [ ] O BE propõe a realização dos exames no próprio SNS.
- [ ] O BE propõe a realização dos exames no próprio dia ou em prazo muito curto.
- [ ] O BE propõe uma rede pública de Centros de Diagnóstico e Terapêutica.
- [ ] O PCP propõe um programa de emergência para recuperar as listas de espera em consultas, cirurgias, exames e tratamentos.
- [ ] O programa de emergência do PCP assenta sobretudo no aumento da capacidade dos serviços públicos.
- [ ] O LIVRE propõe garantir os direitos dos utentes nos tempos de resposta.
- [ ] O LIVRE propõe reduzir as listas de espera para tratamentos de PMA.
- [ ] O PS propõe Percursos Assistenciais Integrados.
- [ ] Os Percursos Assistenciais Integrados propostos pelo PS visam ajudar a cumprir os tempos de espera.
- [ ] Os Percursos Assistenciais Integrados propostos pelo PS visam não retirar ao SNS a responsabilidade pelos utentes.

relevance: 

<details><summary>Context the generator read</summary>

[Documento 1] Partido: Partido Comunista Português | Tópicos: saude
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 4 ELEVAR A QUALIDADE DE VIDA. INVESTIR NOS SERVIÇOS PÚBLICOS, CUMPRIR AS FUNÇÕES SOCIAIS DO ESTADO > 4.1. A defesa do Serviço Nacional de Saúde e uma política de saúde ao serviço dos portugueses > 4.1.3 Um SNS mais forte, com melhor organização e direção das unidades de saúde
##### 4.1.3 Um SNS mais forte, com melhor organização e direção das unidades de saúde  
- Desenvolver o SNS como serviço universal, geral e gratuito, garantindo a gestão pública de todas as suas unidades;
- Garantir médico e enfermeiro de família a toda a população;
- Promover um programa de emergência para a recuperação das listas de espera em consultas, cirurgias, exames e tratamentos, predominantemente assente no aumento da capacidade dos serviços públicos;
- Reforçar os cuidados primários de saúde assegurando um maior número de profissionais, reforçando a rede de unidades, reabrindo centros de saúde e extensões de saúde encerradas, integrando meios complementares de diagnóstico e terapêutica menos complexos, garantindo uma rede de Urgências Básicas ou atendimentos permanentes que permita uma rápida acessibilidade à população de todos os concelhos do País, respondendo às situações de doença ou outras necessidades imediatas que não careçam de intervenção hospitalar;
- Uniformizar em todo o País um só modelo de funcionamento das Unidades de Saúde Familiar (USF), incentivando o funcionamento por ganhos em saúde, eliminando da lei as USF C e revogando as alterações recentes que criam constrangimentos à autonomia dos profissionais de saúde no seu exercício;
- Garantir a existência nos cuidados primários de saúde das consultas médicas de outras especialidades mais necessárias;
- Criar um programa para a recuperação, durante a legislatura, dos serviços e unidades hospitalares encerrados nos últimos anos;
- Reverter o actual e precipitado processo de concentração em curso de serviços de saúde em Unidades Locais de Saúde e de extinção das ARS, procurando antes, e no imediato, garantir a operacionalidade e competência das estruturas de gestão existentes e a autonomia de Hospitais, Centros Hospitalares e Agrupamentos de Centros de Saúde, designadamente para a contratação de profissionais;
- Criar os Sistemas Locais de Saúde, enquanto estrutura de coordenação interna entre hospitais, centros de saúde e cuidados continuados e paliativos, com efetivas competências na articulação dos cuidados, dando concretização à Lei de Bases da Saúde;
- Garantir a gestão democrática das unidades públicas de saúde, através de procedimento concursal para o Presidente do Conselho de Administração dos hospitais e do Diretor Executivo dos ACES, e por eleição de entre os profissionais de cada carreira para os demais membros de administração e de gestão clínica;
- Alargar a resposta pública em cuidados continuados e cuidados paliativos, garantindo a resposta às necessidades em todo o território;
- Valorizar e reestruturar a estrutura de saúde pública, designadamente as suas unidades de proximidade, reorganizando e reforçando os serviços, designadamente através do aumento do número de médicos de saúde pública, promovendo a sua autoridade e competência no diagnóstico, planeamento e gestão estratégica da saúde, valorizando igualmente os restantes profissionais;
- Reforçar os cuidados de saúde mental, reforçando os meios humanos e materiais que lhe estão dedicados e garantindo a sua presença em todas as fases da vida e, designadamente, em meio escolar e laboral;
- Reforçar as equipas locais de intervenção precoce na infância;
- Desenvolver esforços para que todos os trabalhadores tenham a sua saúde e segurança salvaguardadas por Serviços de Saúde Ocupacional e uma actividade seguradora a trabalhar com eficácia e rigor deontológico;
- Garantir cuidados de saúde oral acessíveis a toda a população, designadamente em todos os centros de saúde, contratando para o SNS os profissionais necessários e criando a carreira de médico dentista no SNS;
- Assegurar a prestação de cuidados de saúde visual, de medicina física e de reabilitação e de nutrição nos cuidados de saúde primários;
- Reforçar os meios das Unidades de Cuidados na Comunidade;
- Garantir a disponibilidade dos medicamentos necessários, diminuindo os custos para a população, garantindo a gratuitidade para os doentes crónicos, para os maiores de 65 anos e as famílias com carências económicas;
- Aumentar a quota dos medicamentos genéricos, valorizando a produção nacional, a intervenção e o investimento no Laboratório Nacional do Medicamento visando o aumento da sua capacidade de produção de medicamentos;
- Apostar na promoção da actividade física na prevenção de comportamentos alimentares inadequados, de comportamentos aditivos, violentos ou de risco;
- Intervir na melhoria das questões de saúde ambiental, considerando designadamente as questões da higiene urbana, qualidade da água e do ar, conforto térmico e ruído.

---

[Documento 2] Partido: Partido Socialista | Tópicos: saude
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **2.ª MISSÃO:** UM ESTADO SOCIAL FORTE, MODERNO E INCLUSIVO > 2. Um Serviço Nacional de Saúde universal, forte e resiliente > 2.4.
##### 2.4.  
A melhoria da autonomia e da prestação de cuidados pelo SNS passa igualmente por uma aposta clara no reforço da sua capacitação, através da **internalização da capacidade de resposta,** comprometendo-se o PS a:  
- Reforçar o SNS em Meios Complementares de Diagnóstico e Terapêutica (MDTC) e respetivo pessoal técnico, ao nível dos Cuidados de Saúde Primários, disponibilizando-os em unidades de maior dimensão e numa lógica de cobertura territorial. Trata-se de um investimento que contribui para:
- Uma organização mais eficaz da prestação de cuidados, com maior celeridade e comodidade na resposta aos utentes, evitando deslocações e tempos de espera e permitindo a realização, numa única visita, de exames prescritos;
- Reduzir parte do recurso à contratação externa, economizando recursos públicos que serão investidos no próprio SNS;
- Diminuir o recurso desnecessário às urgências hospitalares, na sequência do aumento da capacidade de resposta de urgência nos Cuidados de Saúde Primários;
- Fortalecer o sentido de equipa, com a melhoria de condições e de recursos, e alcançar níveis mais elevados na motivação dos profissionais de saúde.

---

[Documento 3] Partido: Aliança Democrática | Tópicos: saude
  Secção: PROGRAMA SOCIAL E DE GOVERNAÇÃO DA ALIANÇA DEMOCRÁTICA > COM SENSIBILIDADE SOCIAL > SAÚDE > 2. Metas
##### 2. Metas  
- Ter a ambição de colocar o sistema de saúde português entre os dez melhores do mundo, em 2040, de acordo com os seguintes indicadores internacionais:
- mortalidade por cancro e doença cardiovascular;
- tempo de vida sem doença;
- tempos de resposta a consulta e cirurgia;
- esperança média de vida à nascença;
- despesa _per capita_ de saúde _out-of-pocket._
- Implementar o Plano de Emergência do SNS 2024-2025 com aplicação do Plano de Motivação dos Profissionais de Saúde;
- Inaugurar novas Parcerias Público-Sociais para unidades de Cuidados Paliativos e Unidades de Cuidados Continuados de 2ª Geração;
- Assegurar o cumprimento dos Tempos Máximos de Resposta Garantidos (TMRG) em todos os Hospitais portugueses para os doentes oncológicos até final de 2027;
- Aumentar consistentemente os rastreios oncológicos dos cancros da mama, útero, colorretal, pulmão e próstata;
- Assegurar a Consulta no Médico de Família em tempo útil;
- Adaptar e melhorar as respostas do sistema de saúde ao desafio do envelhecimento demográfico da população;
- Garantir Consultas de Especialidade dentro do tempo de espera máximo, nomeadamente, através da atribuição de um Voucher de Consulta;
- Organizar o Sistema de prestação de cuidados de saúde hospitalar com maior autonomia, atuando integradamente para a realização dos objetivos contratualizados e com avaliação de resultados;
- Incrementar o orçamento dos programas transversais de promoção da Saúde e Saúde preventiva em sede interministerial com franco envolvimento das Autarquias Locais;
- Fortalecer a rede pública de apoio à Fertilidade e Procriação Medicamente Assistida;
- Estabelecer um novo programa nacional de Saúde Oral com unidades privadas de Medicina Dentária;
- Criar a Agência Nacional Digital da Saúde e o Registo Eletrónico de Saúde Único (RES_U) para cada pessoa;
- Construir três Centros Ambulatoriais, até 2028, em co-promoção com municípios ou Comunidades Intermunicipais, baseados em programas de _Value-Based Healthcare_;
- Rever as ULS e concretizar Sistemas Locais de Saúde flexíveis com participação de entidades públicas, privadas e sociais.

---

[Documento 4] Partido: Partido Comunista Português | Tópicos: saude
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 4 ELEVAR A QUALIDADE DE VIDA. INVESTIR NOS SERVIÇOS PÚBLICOS, CUMPRIR AS FUNÇÕES SOCIAIS DO ESTADO > 4.1. A defesa do Serviço Nacional de Saúde e uma política de saúde ao serviço dos portugueses
### CAPÍTULO 4 ELEVAR A QUALIDADE DE VIDA. INVESTIR NOS SERVIÇOS PÚBLICOS, CUMPRIR AS FUNÇÕES SOCIAIS DO ESTADO  
#### 4.1. A defesa do Serviço Nacional de Saúde e uma política de saúde ao serviço dos portugueses  
A situação do Serviço Nacional de Saúde (SNS) agravou-se significativamente durante os últimos anos. O Governo PS prosseguiu obstinadamente uma política de agravamento da carga laboral e das condições de trabalho dos profissionais de saúde do SNS, o que incentivou o afastamento de muitos deles e desincentivou a entrada de outros. O Governo manteve um baixo investimento nos equipamentos e infra-estruturas de saúde (apenas 30% do orçamentado foi realizado) e centralizou cada vez mais as decisões de gestão, limitando a adaptação dos serviços às necessidades das populações que devem servir. Os recursos do Estado são transferidos para o sector privado em cada vez maior volume e percentagem, em detrimento da aposta nos serviços públicos. As alterações legislativas em curso vão impelir mais profissionais a saírem do SNS.  
Em consequência desta política, dezenas de serviços hospitalares foram encerrados ou viram o seu funcionamento fortemente limitado e mais de 1 milhão e 700 mil utentes não têm médico de família. Agravaram-se as listas de espera para cirurgias, consultas, exames complementares e tratamentos, favorecendo claramente os grupos privados da saúde. Os custos com medicamentos são cada vez mais insuportáveis para a população. A população mais carenciada praticamente não tem acesso às respostas em cuidados continuados e paliativos.  
O SNS a funcionar correctamente continua a ser a melhor garantia para a concretização do direito à saúde dos portugueses. Precisa de uma política que valorize decisivamente os seus profissionais, de mais investimento e de maior autonomia na gestão das suas instituições. Necessita que se reduzam as transferências do Orçamento para os privados e que essas verbas sejam canalizadas para os serviços públicos. É decisivo aumentar substancialmente o investimento público nos serviços públicos de saúde, melhorando a capacidade de resposta, as condições de trabalho e atendimento.  
Para garantir o direito à saúde o PCP propõe medidas com três objectivos:

---

[Documento 5] Partido: CHEGA | Tópicos: saude
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > IV CAPÍTULO GARANTIR O ACESSO À SAÚDE. COMO?
## IV CAPÍTULO GARANTIR O ACESSO À SAÚDE. COMO?  
**O**CHEGA reconhece que a saúde é um pilar funda-mental para o bem-estar dos cidadãos e, como tal, entende que é urgente a reestruturação profunda do Serviço Nacional de Saúde (SNS), que deve, desde logo, passar a designar-se Sistema Nacional de Saúde. Este é caracterizado por uma articulação estreita entre o sector público, privado e social.  
O compromisso do CHEGA para as eleições legislativas de 2024 é o de abordar de forma global os desafios actuais e construir um sistema de saúde que seja universal, eficiente, integrado e equitativo.  
Neste sentido, a medida prioritária a desenvolver é a informatização de todo o sistema de saúde, partilhado por todos os intervenientes. Este procedimento e o seu processo, bem como o instrumento final que se irá alcançar, tem sempre em conta a salvaguarda dos direitos dos cidadãos na questão da protecção de dados. Este é um aspecto que não pode continuar a ser adiado porque é uma das principais razões da ineficiência de todo o sistema de saúde actual. Sem dados não poderá haver gestão eficiente.  
A grave crise que atravessa o Serviço Nacional de Saúde deve-se a políticas públicas infrutíferas, com grave enviesamento ideológico e baseadas na presunção e no preconceito. Isto levou a uma crescente degradação do serviço de saúde e, consequentemente, no estado de saúde dos portugueses, na degradação de instalações e equipamentos, bem como nas condições de trabalho e em pressões desumanas sobre os profissionais de saúde, sobretudo ao nível dos serviços hospitalares, mas também em todos os outros que integram o SNS.  
As dificuldades de acesso são o primeiro obstáculo que os cidadãos encontram quando precisam de resolver os seus problemas de saúde. Um exemplo disso é a falta de médicos de família, que tem vindo a aumentar e que actualmente coloca mais de 1.700.000**<sup>1</sup>** cidadãos sem ver cumprida a promessa de António Costa sucessivamente adiada: "2017 é, de uma vez por todas, o ano em que todos os portugueses terão um médico de família atribuído"**<sup>2</sup>**.  
Este falhanço político é mais uma prova da incapacidade dos governos anteriores em resolver este problema. Em breve, e neste ritmo, mais de 2 milhões de portugueses estarão sem médico de família.  
As listas de espera para consultas de especialidade, além das já citadas de Medicina Geral e Familiar, para a realização de exames ou meios complementares de diagnóstico e tratamento, bem como de cirurgias e ainda a crescente incapacidade de providenciar outro tipo de cuidados à população, são indicadores amplamente conhecidos. Os atrasos ou a incapacidade de acesso à inovação terapêutica e tecnológica é mais uma demonstração de inépcia ou da inoperância em fazer cumprir com o que é exigido pela população.  
A sobrecarga dos Serviços de Urgência hospitalares em geral e em diversas especialidades em particular, com encerramentos recentes de algumas destas unidades funcionais, é uma realidade que se agravou nas últimas décadas por uma incapacidade constante e repetida de não se resolver a falta de resposta ao nível dos cuidados de saúde primários. Se os utentes não tiverem resposta nos cuidados de proximidade acorrem à única porta acessível - mas incapaz de dar resposta a todas as solicitações -, que são os serviços de urgência hospitalar.  
A falta de transparência, de escrutínio e de instrumentos de gestão eficazes promovem a ineficiência. As ferramentas e processos de gestão são inadequados, obsoletos e complexos, sem integração numa plataforma informática única que permita aliviar os profissionais da burocracia estrutural existente.  
A redundância e a sobreposição de competências dos diversos organismos, institutos e entidades que exercem funções de análise, de avaliação, executivas e de gestão dependentes do Ministério da Saúde devem ser revistas na sua função e adequadas a um modelo mais exigente, simples e responsável.  
As carreiras profissionais também carecem de uma adequada valorização, devendo fazer-se um esforço de corresponder às legítimas expectativas dos profissionais e ao papel central que desempenham em todo o sistema. A degradação e sobrecarga da actividade profissional tem conduzido ao abandono da carreira pública e também a uma elevada taxa de emigração.  
As alterações demográficas, as transições de natureza epi-  
**<sup>1</sup>** Utentes Inscritos em Cuidados de Saúde Primários — Transparência (sns.gov.pt) **<sup>2</sup>**Cf. Jornal de Negócios, 2016  
demiológica, seja o aumento da esperança média de vida, o envelhecimento da população e a dependência associada, assim como a prevalência de doenças e comorbilidades, trazem novos desafios. Uma realidade que é observada, diagnosticada e referida há mais de três décadas, porém, muito pouco tem sido feito para ajustar e mudar os sistemas de apoio social e os cuidados de saúde para adaptá-los a esta transição demográfica. Neste âmbito há que proceder à estratificação da população em risco, da carga de doença e factores de risco de modo a alocar recursos de forma mais eficiente. A integração multidisciplinar e sectorial nesta abordagem é essencial para que haja ganhos efectivos de qualidade em saúde.  
O Serviço Nacional de Saúde tem de passar a ser assumido como um sistema que integra todos os cuidados de saúde instalados no país e, portanto, incluindo a oferta privada.  
Apesar de uma parte significativa dos serviços prestados pelo Serviço Nacional de Saúde já ser de natureza privada e, nesta medida, os serviços privados e sociais já fazem parte integrante do Serviço Nacional de Saúde, o preconceito ideológico e o sofisma prevalente não tem permitido fazer desta realidade uma forma de concretizar um SNS mais eficiente, com menos custos e melhor serviço para o cidadão. Actualmente, há problemas graves de acessibilidade que penalizam a população mais frágil e desfavorecida e, por outro lado, há uma percentagem cada vez maior de portugueses que pagam os cuidados de saúde a que deveriam ter direito, financiando o sistema múltiplas vezes.  
A determinação dos custos, da sua estrutura, de todos os actos prestados tem de ser conhecida e pública para que uma real comparação possa ser realizada, com base na garantia de controlo e supervisão da qualidade, indicador que irá permitir fazer as opções e determinar o financiamento. Este processo deve ser comum a todos os sectores, agentes, instituições e prestações do sistema.  
O CHEGA reconhece a importância de devolver ao SNS a capacidade de atrair e fixar profissionais e, neste âmbito, importa referir que entre fevereiro e outubro de 2023, 1.780**<sup>3</sup>** profissionais abandonaram o SNS. Pese embora tenham sido promovidos diversos concursos para contratação de médicos, o resultado revelou reiteradamente a falta de atractividade do SNS, uma tendência que não pode ser subestimada.  
Assim, o CHEGA propõe um Sistema Nacional de Saúde guiado pela eficiência, qualidade, incentivando a contratualização de parcerias público-privadas onde se revele necessário e modelos de gestão por objectivos. Defendemos a autonomia de gestão das instituições hospitalares públicas, baseada em critérios de transparência e competência, e a comparação entre os diversos sectores.  
Comprometemo-nos a aferir de forma credível os níveis de satisfação dos utentes em diferentes valências, proporcionando ferramentas de comparação entre sectores público, privado e social.  
A proposta do CHEGA para a saúde, através deste programa para as eleições legislativas de 2024, reflete o compromisso inabalável de construir um sistema de saúde robusto, centrado nas pessoas e capaz de responder aos desafios emergentes.

---

[Documento 6] Partido: CHEGA | Tópicos: saude, governacao
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > IV CAPÍTULO GARANTIR O ACESSO À SAÚDE. COMO? > PROPOSTAS
### PROPOSTAS  
**89.** Desenvolver tecnologias inovadoras e sistemas de informação integrados que melhorem a coordenação entre as diferentes valências do sistema de saúde (cuidados médicos, terapêuticas, rastreios e diagnósticos), incluindo:  
- Plataforma única digital comum a todos os agentes envolvidos no sector da saúde em Portugal, processo essencial para que existam sinergias e ganhos de eficiência em todo o sistema de saúde;  
- Registo Único de Saúde do Cidadão, permitindo a disponibilidade do processo clínico do utente em todas as instituições de saúde de forma a agilizar o acesso a informações médicas, melhorar a coordenação entre profissionais, reduzir a duplicação de exames, facilitar tomada de decisões e promover a segurança e precisão do histórico clínico do utente, numa abordagem, integrada e personalizada;  
- Dinamização da telemedicina na prestação de cuidados de saúde, permitindo consultas remotas e acessíveis atra-  
**<sup>3</sup>** Análise Mensal do Balanço Social – SNS  
vés de tecnologias digitais;  
- Promoção da qualidade e transparência nos serviços públicos, privados e sociais, nomeadamente através da avaliação sistemática dos serviços, à comparação entre sectores com a publicação dos respectivos relatórios periódicos, criação de incentivos para a qualidade, entre outros.  
**90.** Evoluir o Serviço Nacional de Saúde para um Sistema Nacional de Saúde, com a integração de todo o Sector Público, Privado e Social, formalizando parcerias público-privadas estratégicas para optimizar recursos e garantir uma prestação de serviços mais eficaz, rápida e de qualidade.  
**91.** Reformar a Lei de Bases da Saúde introduzindo novos modelos de gestão e parcerias público-privadas (PPP's) e alterar o Estatuto do Serviço Nacional de Saúde, nomeadamente, revogando a previsão do director executivo.  
**92.** Garantir que os serviços de saúde sejam prestados de maneira eficiente, equitativa e com padrões de qualidade elevados, com base em indicadores claros e metas mensuráveis de desempenho e conformidade.  
**93.** Assegurar que sempre que se verifique o esgotamento dos tempos máximos de resposta garantidos (TMRG), fixados para a rede de prestação de cuidados de saúde no SNS, o Estado tem a obrigação de referenciar os utentes para atendimento nos sectores privado ou social, o que deve acontecer de forma célere e eficaz, garantindo o acesso dos utentes a cuidados de saúde de qualidade, em tempo útil e próximo da sua área de residência.  
**94.** Actualização do Plano Nacional de Vacinação, garantindo a disponibilidade de vacinas essenciais, sobretudo para a população infantil, e organizar campanhas de vacinação abrangentes, incluindo campanhas educativas que esclareçam sobre a importância da prevenção.  
**95.** Proceder a rastreios regulares de forma a identificar precocemente condições de saúde potencialmente problemáticas, com especial atenção para as doenças crónicas de maior prevalência, cancro e outras condições de grande impacto na saúde pública.  
**96.** Implementar programas educativos nas comunidades, escolas e locais de trabalho para aumentar a consciencialização sobre hábitos saudáveis e fomentar a adopção de comportamentos preventivos, nomeadamente no que diz respeito ao consumo de tabaco, álcool e drogas.  
**97.** Reforçar a implementação da estratégia de combate à obesidade através do incentivo a consultas de prevenção de obesidade e de acompanhamento de doentes com pré- -obesidade e obesidade, com vista ao seu tratamento em fases precoces de desenvolvimento da doença e execução de programas de rastreio da obesidade e alterações metabólicas pelas unidades de cuidados de saúde personalizados e pelas unidades de saúde familiar.  
**98.** Capacitar as Farmácias comunitárias reforçando a sua intervenção, nomeadamente em situações clínicas ligeiras; testagem rápida (TRAg, VIH, Hepatites); meios complementares de diagnóstico e vacinação.  
**99.** Melhorar as condições de trabalho dos médicos de família através da construção e manutenção das actuais Unidades de Cuidados de Saúde Personalizados e Unidades de Saúde Familiares, equipando de forma adequada as unidades de saúde com os meios e materiais suficientes para o seu funcionamento.  
**100.** Melhorar substancialmente os sistemas informáticos à disposição dos profissionais, promovendo a sua uniformização e fiabilidade, "desburocratizar" a actividade laboral dos médicos de família que hoje são chamados a realizar funções que vão muito para além da actividade clínica propriamente dita, que deveria ser a sua principal função.  
**101.** Criar a figura do "gestor da UCSP/USF", que é quem deve coordenar e apoiar as equipas de saúde nas áreas administrativas, de gestão e na resolução de conflitos, libertando médicos e enfermeiros para fazerem aquilo que sabem: acompanhar e tratar os seus utentes.

---

[Documento 7] Partido: Iniciativa Liberal | Tópicos: saude
  Secção: PROGRAMA ELEITORAL > B. PORTUGAL A FUNCIONAR > 2. MAIS ACESSO À SAÚDE > 2.1. Mudar o Sistema de Saúde em Portugal > Reduzir as Listas de Espera
##### Reduzir as Listas de Espera  
No âmbito dos cuidados hospitalares, não se têm verificado medidas claras, concretas e devidamente calendarizadas, para a redução dos tempos de espera para consultas ou cirurgias no Serviço Nacional de Saúde (SNS). De acordo com a informação mais atual sobre a monitorização dos tempos de espera no SNS da Entidade Reguladora da Saúde, relativa ao primeiro semestre de 2023:  
- Existiam, a 30 de junho de 2023, 750.549 utentes a aguardar uma primeira consulta hospitalar – um aumento de 37% em comparação com o primeiro semestre de 2022 – sendo que 47% destes casos estão fora dos Tempos Máximos de Resposta Garantidos (TMRG). No caso específico das primeiras consultas com suspeita ou confirmação de doença oncológica, existiam 9.014 utentes em espera, 73% dos quais em "espera há mais tempo que o máximo previsto na lei, mais 22 p.p. do que em junho de 2022, importando referir que esta percentagem de incumprimento corresponde ao valor mais elevado deste indicador desde o início da monitorização pela ERS";
- Existiam, a 30 de junho de 2023, 192.186 utentes em espera para cirurgias programadas – um aumento de cerca de 10% quando comparado com igual periodo de 2022 – em que 14,2% das situações estão fora dos TMRG. No caso específico das cirurgias oncológicas, existiam 7.157 utentes em espera – um aumento de cerca de 11,4% face a 2022 – encontrando-se os TMRG excedidos em 17,5% das situações.  
O incumprimento dos Tempos Máximos de Resposta Garantidos (TMRG) tem como consequência o atraso na avaliação clínica mais diferenciada o que, evidentemente, gera riscos para a saúde das pessoas. Por este motivo, a Iniciativa Liberal considera urgente a criação de um Programa Especial de Acesso a Cuidados de Saúde que assegure o acesso a consultas de especialidade hospitalar e a cirurgias, devidamente contratualizados através de concurso público de abrangência internacional, sempre que os TMRG não são cumpridos no Serviço Nacional de Saúde.  
O objetivo é a redução, a curto prazo, das listas de espera. A Iniciativa Liberal compreende que existe uma dificuldade na atração e retenção de recursos humanos no SNS, que se traduz na impossibilidade de no curto, médio e longo prazo, conseguir alcançar o cumprimento dos Tempos Máximos de Resposta Garantidos de forma transversal. Para tal, será necessário criar carreiras atrativas do ponto de vista da remuneração, do reconhecimento do mérito e da qualidade de serviço, de métodos de avaliação transparentes e contínuos e da melhoria das condições gerais de trabalho. Apenas com a atuação nestes três eixos será possível garantir que se conseguem evitar as listas de espera que estão continuamente em crescendo. Neste âmbito, é ainda essencial a liberdade de contratação direta por parte das instituições do SNS, garantindo uma descentralização do processo de gestão de recursos, quer humanos, mas também técnicos e financeiros, mais autonomia e flexibilidade e uma maior responsabilização por parte de cada instituição.

---

[Documento 8] Partido: Iniciativa Liberal | Tópicos: saude
  Secção: PROGRAMA ELEITORAL > B. PORTUGAL A FUNCIONAR > 2. MAIS ACESSO À SAÚDE > 2.1. Mudar o Sistema de Saúde em Portugal > Mais Acesso a Cuidados de Saúde Primários
##### Mais Acesso a Cuidados de Saúde Primários  
A Iniciativa Liberal propõe a contratualização da prestação de cuidados de saúde com o setor social e privado para dar resposta atempada a quem não consegue ser atendido no Serviço Nacional de Saúde dentro dos prazos de espera estipulados na lei. Os Cuidados de Saúde Primários são a base de qualquer sistema de saúde, atuando enquanto primeiro contacto entre o utente e o sistema de saúde, praticando cuidados de saúde preventivos e promotores da saúde e resolvendo situações de doença que não requerem níveis de cuidado hospitalares. Na ausência do seu funcionamento em pleno – como é o caso no Serviço Nacional de Saúde – é impossível que o sistema de saúde responda de forma adequada e que as pessoas tenham acesso a tempo e horas aos cuidados de que precisam.

---

[Documento 9] Partido: Bloco de Esquerda | Tópicos: saude
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 2 Saúde > 2.1 O SNS é vítima do desgoverno do PS
### 2.1 O SNS é vítima do desgoverno do PS  
Cada vez mais pessoas sem equipa de saúde familiar, listas de espera a crescer, maternidades e urgências constantemente encerradas, um clima de conflito contra os profissionais do SNS, saúde cada vez mais cara para quem dela precisa e mais dificuldade em comprar medicamentos. Em suma: a desestruturação do serviço público de saúde, que urge parar. Temos de reconstruir um SNS de acesso universal e de qualidade.  
Em apenas dois anos de maioria absoluta, o número de utentes sem médico de família aumentou 50%, ultrapassando a fasquia dos 1,7 milhões. Nos hospitais, continuou a aumentar a espera para consulta e cirurgia, apesar de os profissionais tudo terem feito para recuperar a atividade assistencial.  
Em novembro de 2023, existiam mais de 258 mil pessoas a aguardar por uma cirurgia, ou seja, mais 24% do que no final de 2021. A lista de espera por uma consulta hospitalar também aumentou: no final de 2022 existiam 583 mil pedidos de consulta por realizar, mais 11% do que em 2021. Durante o ano de 2023, mais de metade das primeiras consultas foram realizadas após o tempo clinicamente aceitável (50,1%).  
GRÁFICO 10  
**Número de doentes inscritos a aguardar cirurgia**  
Fonte: SNS Transparência  
GRÁFICO 11  
**Percentagem de primeiras consultas realizadas em tempo adequado**  
Fonte: SNS Transparência  
A isto somaram-se os constantes encerramentos de maternidades, urgências obstétricas, urgências pediátricas, urgências cirúrgicas e camas de internamento, além dos condicionamentos de várias Vias Verde AVC. Houve momentos em que estiveram 30 ou mais urgências encerradas ou com fortes constrangimentos.

---

[Documento 10] Partido: Aliança Democrática | Tópicos: saude, trabalho
  Secção: PROGRAMA SOCIAL E DE GOVERNAÇÃO DA ALIANÇA DEMOCRÁTICA > COM SENSIBILIDADE SOCIAL > SAÚDE > 3. Medidas > COMBATER A DESIGUALDADE DE ACESSO À SAÚDE
##### 3. Medidas  
###### COMBATER A DESIGUALDADE DE ACESSO À SAÚDE  
- Apresentar um Plano de Emergência SNS 2024-2025, nos primeiros 60 dias do novo Governo, sustentado por uma reorientação estratégica da política global do Governo nesta área, designadamente com o seguinte enquadramento legislativo e financeiro em 2024:  
**Ao nível das Consultas**  
- Garantir a emissão do Voucher Consulta de Especialidade, com liberdade de escolha do prestador pelo utente quando é ultrapassado o Tempo Máximo de Resposta Garantido (TMRG);
- Promover um incremento sustentado das USF tipo B;
- Realizar contratos temporários com Médicos de Família aposentados ou privados;
- Assegurar consultas digitais com Equipa de Família das USF e Centros de Saúde;
- Assegurar a inscrição no Enfermeiro de Família;
- Alargar o âmbito e a cobertura do programa Cheque-Dentista;
- Reforçar as Equipas de Apoio Domiciliário;
- Abrir USF tipo C nas áreas metropolitanas Lisboa e Porto (projeto-piloto);
- Alargar consultas de Psicologia Clínica, Terapia de Reabilitação e Nutrição nos Centros de Saúde.  
**Ao nível das Urgências**  
- Implementar um Plano de Motivação dos Profissionais de Saúde;
- Redefinir a Rede de Urgências e referenciação hospitalares;
- Implementar a consulta doença aguda em tempo útil nas USF e Centros de Saúde;
- Criar o Gestor do Doente Crónico, utilizador das Urgências;
- Avançar, com a Ordem dos Médicos, na Especialidade de Medicina de Urgência e Emergência;
- Criar um modelo de equipas dedicadas com auditoria externa;
- Implementar benefícios especiais para equipas de Urgência.  
**Ao nível das Cirurgias**  
- Desenvolver as CRIs públicos de segunda geração;
- Criar novos incentivos no programa SIGIC com indicadores de _outcome_ clínico reportados pelo paciente;
- Promover a auditoria regional e nacional a TMRG na rede hospitalar;
- Implementar indicadores hospitalares obrigatórios de _outcome_ cirúrgico;
- Desenvolver um sistema concorrencial competitivo para cirurgia de ambulatório;
- Organizar uma resposta pública no SNS com vista ao aumento da natalidade e maior acesso às técnicas de Procriação Medicamente Assistida, com práticas sustentadas numa sólida moldura ética:
- Reforçar o Investimento nos centros públicos de PMA (Procriação Medicamente Assistida) em recursos humanos, equipamentos e espaços físicos;
- Diferenciar e reforçar a especialização dos centros de PMA do SNS;
- Garantir a autonomização funcional e financeira do Banco Público de Gâmetas e reforço da sua estrutura orgânica especializada com aumento da capacidade de resposta;
- Reforçar o apoio para técnicas médicas de fertilidade humana com melhores tecnologias disponíveis no SNS e parceiros privados com acordo de colaboração;
- Assegurar a referenciação mais precoce dos Médicos de Família para centros de PMA;
- Aprofundar e melhorar os protocolos clínicos e boas práticas assistenciais para obtenção da menor mortalidade infantil da UE.

---

[Documento 11] Partido: Partido Socialista | Tópicos: saude
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **2.ª MISSÃO:** UM ESTADO SOCIAL FORTE, MODERNO E INCLUSIVO > 2. Um Serviço Nacional de Saúde universal, forte e resiliente > 2.2.
##### 2.2.  
No que concerne à **melhoria do modelo de governação do SNS e dos processos de gestão e prestação de cuidados,** o PS irá:  
- Promover uma maior articulação e integração entre os cuidados de saúde primários, hospitalares e cuidados continuados, contrariando assim a excessiva centralidade da rede hospitalar e a duplicação de custos;  
- Adotar um modelo de governação do SNS de comando vertical, centrado na Direção Executiva;  
- Criar centros de excelência clínica no SNS, com os recursos humanos e tecnológicos necessários, permitindo um aumento da qualidade na prestação de cuidados e a redução do tempo de resposta;  
- Reforçar a autonomia dos Conselhos de Administração hospitalares e das unidades de proximidade, tanto a nível técnico e operacional como de gestão orçamental e de contratações, a par do aumento da sua responsabilização e da avaliação de desempenho e de resultados;  
- Generalizar o concurso público no preenchimento de órgãos de gestão, assegurando que estes são compostos por elementos com formação clínica e que cumprem requisitos obrigatórios, alinhados com os objetivos institucionais;  
- Fomentar um maior envolvimento dos profissionais de saúde nas decisões de gestão estratégica e operacional, contribuindo para um funcionamento dos serviços mais autónomo, alinhado e flexível;  
- Aprofundar os mecanismos de monitorização e transparência, com evidência pública de resultados, recorrendo a um quadro regular de indicadores relevantes e percetíveis pela sociedade em geral;  
- Adotar o princípio dos Percursos Assistenciais Integrados, assegurando que o envolvimento dos diferentes atores, tendo em vista o cumprimento de tempos de espera, não compromete a responsabilidade do SNS pelo acompanhamento e a garantia de prestação de cuidados aos utentes;  
- Reforçar as regras de acesso direto às urgências hospitalares, generalizando a triagem telefónica, através da qual se procederá ao encaminhamento dos utentes para os cuidados de saúde primários ou hospitalares.

---

[Documento 12] Partido: Iniciativa Liberal | Tópicos: saude
  Secção: PROGRAMA ELEITORAL > PORTUGAL A FUNCIONAR > 6. MAIS ACESSO À SAÚDE
### 6. MAIS ACESSO À SAÚDE  
- Novo sistema de saúde que integre os setores público, privado e social, onde as pessoas possam escolher onde e por quem querem ser tratadas, com mais acesso e menos espera, sem custos acrescidos além dos existentes como na Holanda ou na Alemanha
- Médico de família público ou privado para todos até 2028, começando pelos que têm mais de 65 anos, mulheres grávidas e crianças até aos 9 anos, até 2025
- Recuperar as Parcerias Público-Privadas nos hospitais de Braga, Vila Franca de Xira e Loures, alargando o modelo a outros hospitais
- Reduzir as listas de espera, através da criação de um Programa Especial de Acesso a Cuidados de Saúde que assegure o acesso atempado a consultas e cirurgias
- Expandir as USF-B e Implementação das USF-C
- Remuneração variável consoante o desempenho para todos os profissionais de saúde
- Reforçar as competências dos enfermeiros especialistas
- Alargar os cuidados prestados pelas Farmácias Comunitárias
- Garantir o acesso a medicamentos e a dispositivos médicos, com comparticipação a 100% para os que não os possam pagar, sobretudo idosos
- Promover a saúde mental, garantindo um acesso efetivo em todos os níveis de cuidados
- Defender os direitos das mulheres, respeitando-as nas suas escolhas livres e na maternidade
- Criação de um Registo de Saúde Electrónico Universal

---

[Documento 13] Partido: Aliança Democrática | Tópicos: saude, trabalho
  Secção: PROGRAMA SOCIAL E DE GOVERNAÇÃO DA ALIANÇA DEMOCRÁTICA > COM SENSIBILIDADE SOCIAL > SAÚDE > 1. Porque é preciso mudar
## COM SENSIBILIDADE SOCIAL  
### SAÚDE  
##### 1. Porque é preciso mudar  
O diagnóstico crítico sobre o grave estado atual da Saúde em Portugal está bem documentado por fontes sérias e idôneas. Partilhamos das preocupações crescentes com a agudização de problemas estruturais do SNS não resolvidos e agravados pelos governos do Partido Socialista – motivo da forte desmotivação atual dos profissionais de saúde e insatisfação da população portuguesa. Nos últimos anos, Portugal estagnou no comparativo internacional dos sistemas de saúde e degradou gravemente as condições de acesso universal aos cuidados de saúde.  
Há uma injustiça gritante no acesso aos cuidados de saúde em Portugal, com desigualdades crescentes entre os mais pobres e os mais ricos, entre o litoral e o interior, entre zonas urbanas, suburbanas e rurais.  
Os tempos clinicamente recomendados para cirurgia são ultrapassados em vários hospitais do SNS, mesmo em casos de pessoas com cancro e outras doenças graves. No final de 2023, 1,7 milhões de portugueses não tinham Médico de Família e o Enfermeiro de Família não saiu do papel.  
Torna-se vital inverter uma gestão socialista caótica, desmotivante e ineficiente que corrompeu a essência do SNS. Precisamos de um SNS forte para o século XXI e ao serviço de todos.  
A degradação consecutiva das condições de trabalho e o desprezo institucional pelas carreiras de todos os profissionais de saúde tiveram consequências desastrosas na organização dos serviços de saúde, com particular gravidade para os Serviços de Urgência.  
Sabemos que não haverá qualquer reforma da Saúde em Portugal sem a adesão e o trabalho dedicado das várias equipas de saúde.  
É absolutamente essencial motivar, apoiar e congregar o espírito ético e profissional dos Médicos, dos Enfermeiros, dos Farmacêuticos, dos Psicólogos, dos Fisioterapeutas e Terapeutas, dos Nutricionistas, dos Técnicos de Diagnóstico e Terapêutica, dos Técnicos de Emergência, dos Assistentes Operacionais, dos Administradores, das equipas de apoio informáticas, de engenharia, administrativas e financeiras, de todos os que trabalham com dedicação no SNS e no sistema de saúde português.  
Uma diminuição da carga de doença e um aumento do tempo livre de doença são condições essenciais para consubstanciarmos uma meta de mais anos de vida e com mais qualidade de vida. Para isso, apostamos na partilha de responsabilidades para um auto- -cuidado mais ativo e autónomo das pessoas e comunidades em áreas como as doenças cardiovasculares, a diabetes ou o cancro.  
Com a evolução da medicina preditiva e com o advento da Inteligência Artificial os diagnósticos precoces personalizados terão cada vez maior impacto na saúde das pessoas, devendo, naturalmente, os "check-up" terem regras e um racional clínico adequado à idade e fatores de risco.  
Neste sentido devem ser também revistas as medidas dirigidas a pessoas portadoras de deficiência e de doença incapacitante, definindo novos indicadores de qualidade de vida com a participação direta das associações de doentes numa perspetiva inclusiva e de ganhos de saúde.  
A evolução da rede de cuidados de saúde primários através de Unidades de Saúde Familiar (USF) pretende otimizar a resposta de saúde à escala das comunidades locais mas regista ainda insuficiente dispersão geográfica. Importa ir mais longe e de forma mais profunda numa rede de cuidados de proximidade assentes na resposta integrada de saúde e apoio social, com o envolvimento direto das Autarquias Locais e de todas as instituições públicas, privadas e sociais que atuam localmente.  
A revisão e redefinição da descentralização de competências na área da saúde deve reorientar a evolução equitativa e flexível das respostas de saúde em todo o território nacional, articulando a rede pública, social e privada existente em cada Freguesia e Município. A implementação dos Planos Municipais de Saúde – com enfoque acrescido na saúde preventiva – constitui um instrumento central da efetiva garantia de equidade e melhor acesso aos cuidados de saúde.  
Os portugueses pagam diretamente do seu bolso mais de 35% da despesa anual de Saúde para além dos impostos cobrados que financiam o SNS. Mais de 3,1 milhões de portugueses optam hoje por um seguro de saúde para conseguir liberdade de escolha e resposta célere dos prestadores de saúde.  
O esforço individual e coletivo para uma saúde de qualidade é desproporcionado em relação aos resultados obtidos – é possível diminuir o desperdício e as ineficiências do sistema de saúde através de melhor contratualização, comparação de resultados e competição regulada.  
A garantia constitucional de acesso universal aos cuidados de saúde deve ser cumprida com recurso a todos os meios públicos, privados e sociais existentes e devidamente articulados, num sistema competitivo que premeia a eficiência e a qualidade da resposta de saúde aos cidadãos.

---

[Documento 14] Partido: Bloco de Esquerda | Tópicos: saude, trabalho, habitacao
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 2 Saúde > 2.3 Objetivo: reconstruir o SNS > Consultas e cirurgias a tempo e horas
#### Consultas e cirurgias a tempo e horas  
Contratar, fixar onde é mais necessário e libertar tempo dos profissionais para consultas e cirurgias garantirá a diminuição drástica de listas e tempos de espera. Exames na hora certa, dentro do SNS  
O objetivo do Bloco de Esquerda é este: que todas as consultas e cirurgias se realizem a tempo e horas.  
- → Abertura imediata de concursos para contratação em todas as unidades de saúde onde existam horas extraordinárias anuais que superem o limite legal ou onde a falta de profissionais resulta em tempos de espera acima do recomendado;
- → Revisão e alargamento dos apoios à fixação em zonas carenciadas, nomeadamente, através da cobertura de despesas com habitação;
- → Redução para as 12h do horário semanal de urgência exigido aos médicos, libertando o restante tempo para consultas e cirurgias;
- → Desburocratização dos processos e de carga administrativa, libertando tempo para atividades clínicas, nomeadamente, através da contratação de técnicos administrativos;  
- → Descentralização de cuidados de saúde como pediatria, ginecologia/ obstetrícia, oftalmologia, dermatologia, entre outros, situando-os mais próximos das populações;
- → Tornar o SNS capaz de responder a uma população envelhecida e com crescentes necessidades de acesso à saúde exige a criação de portas de entrada para as especialidades hospitalares e de protocolos de acompanhamento dos utentes entre os diversos níveis de cuidados de saúde, a par do reforço dos cuidados de saúde primários.

---

[Documento 15] Partido: Pessoas-Animais-Natureza | Tópicos: saude
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por uma só Saúde e um SNS fortalecido e eficiente
## Por uma só Saúde e um SNS fortalecido e eficiente  
Nos tempos que correm, o Serviço Nacional de Saúde enfrenta os maiores desafios desde que foi fundado. O Governo tem sido incapaz de responder às exigências dos médicos, que depois de serem elevados a heróis durante a crise da COVID-19, são agora os vilões numa guerra salarial que parece não ter fim. Os enfermeiros veem-se estagnados na sua profissão, sendo pagos baixos salários para a importância das tarefas que desempenham, levando muitos deles a procurar uma vida melhor no estrangeiro. A regularização das carreiras dos Técnicos Superiores de Diagnóstico e Terapêutica (TSDT) continua por concluir. No meio de todo este caos na saúde, mais de 1,7 milhões de portugueses continuam sem médico de família, esperam horas para serem atendidos nos hospitais e frequentemente encontram as suas unidades de saúde sem profissionais suficientes que correspondam às necessidades e urgências da população.  
O PAN tem-se batido por estas questões, tendo nas últimas legislaturas apresentado medidas de valorização dos profissionais e incentivo à colocação dos mesmos em zonas mais desfavorecidas, enquanto se procura dar resposta às necessidades de saúde da população. Estes avanços propostos têm esbarrado na maioria absoluta do Partido Socialista, mas assumimos o nosso compromisso com esta causa.  
A nossa visão para a saúde é uma visão de Uma só Saúde. Para o PAN, não se pode separar a saúde animal da saúde ambiental e da saúde humana. Cidades mais limpas e com ar respirável de melhor qualidade evitarão problemas de saúde futuros à população. A crise sanitária provocada pela pandemia COVID-19 demonstrou-nos que não nos podemos esquecer dos animais quando falamos da saúde da população. É com isto em mente que devemos priorizar a implementação de sistemas locais de saúde, onde em cada comunidade se promove a saúde preventiva e de proximidade, promovendo hábitos de alimentação mais saudáveis, dando mais importância à atividade física e desportiva e reforçando as unidades de saúde próximas das populações com meios de diagnóstico e acompanhamento necessários, sem esquecer o papel das farmácias, para que apenas em última instância as pessoas precisem de se deslocar a um hospital. Para além disto, precisamos de um Serviço Nacional de Saúde tecnologicamente atualizado e em constante acompanhamento das melhores práticas de saúde reconhecidas pela comunidade científica, garantindo que, no nosso serviço público de saúde, podemos oferecer os melhores cuidados de saúde disponíveis, apostando também na constante atualização e formação dos nossos profissionais.  
Neste contexto, para valorizar os profissionais de saúde e reorganizar o SNS para o tornar mais eficiente, o PAN irá:  
- Revitalizar o SNS, estabelecendo condições de trabalho de qualidade, gratificantes e atrativas para todos os profissionais de saúde, mediante:  
- Atribuição da profissão de risco e de desgaste rápido para os profissionais de saúde que trabalham no SNS;
- Aposentação aos 36 anos de serviço ou aos 62 anos de idade;
- Aumento faseado de 30% nos salários dos médicos;
- Aprovação de um regime de dedicação exclusiva voluntária para médicos e enfermeiros;
- Criação de incentivos para a fixação de médicos e enfermeiros em áreas carenciadas;
- Alteração da progressão da carreira dos enfermeiros, passando estes a progredir de 4 em 4 pontos, com valorização salarial de 100 euros, ao invés de 8 em 8 pontos com valorização salarial de 200 euros;
- Entrada dos enfermeiros no nível remuneratório 21 em vez de no nível 15;
- Valorização das carreiras dos TSDT;  
- Garantia de que, no caso dos enfermeiros, os pontos adquiridos para progressão de carreira numa categoria inferior podem contar para a progressão de carreira numa categoria superior;  
- Promover a valorização dos profissionais de saúde com base na qualidade dos tratamentos e nos desfechos clínicos e não no número de consultas  
- Reconhecer aos Técnicos de Emergência Pré- -Hospitalar do INEM o estatuto de profissão de risco e de desgaste rápido.  
- Garantir o cumprimento do número máximo de horas extraordinárias previstas na lei, em pleno respeito pelo tempo de descanso compensatório legalmente estabelecido;  
- Substituir a contratação de empresas de prestação de serviços por contratação de efetivos que respondam a necessidades permanentes do SNS  
- Generalizar a Medicina do Trabalho nos centros de saúde e hospitais públicos;  
- Alterar o estatuto da Ordem dos Enfermeiros, garantindo a independência da mesma não só face ao Ministério da Saúde, mas também ao escrutínio e exigências dos médicos e seguindo as exigências destes profissionais;  
- Concretizar a majoração dos valores atribuídos aos profissionais nas USF modelo B;  
- Igualar os incentivos nas USF modelo B entre a equipa multiprofissional que as compõem, reproduzindo a sua fórmula de cálculo igualmente para todos as classes profissionais;  
- Rever as competências dos Tripulantes de Ambulância de Socorro, garantindo-lhes formação e competências iguais aos Técnicos de Emergência Pré-Hospitalar do INEM  
- Contratar profissionais da nutrição para todos os Agrupamentos de Centros de Saúde (ACES);  
- Investir na Saúde Digital e nas teleconsultas nos Cuidados de Saúde Primários, nas Consultas Hospitalares e no SNS 24;  
- Investir no desenvolvimento do Registo de Saúde Eletrónico e definir a intervenção de cada profissional de saúde, permitindo que todos, no âmbito das suas atribuições, possam aceder a informação clínica relevante e efetuar os registos adequados, no cumprimento do RGPD;  
- Investir na integração dos sistemas informáticos dos cuidados de saúde primários e hospitalares com os das farmácias comunitárias, promovendo uma verdadeira articulação e comunicação entre farmacêuticos e médicos e permitindo uma atuação mais eficaz em caso de escassez de medicamentos;  
- Inovar nos modelos, procedimentos, técnicas e produtos em saúde, investindo em melhores meios e tecnologias;  
- Impulsionar a literacia em saúde preventiva nos canais de comunicação institucionais de todas as salas de atendimento do SNS;  
- Reforçar a capacitação de todos os profissionais de saúde em saúde preventiva;  
- Priorizar um modelo médico assente na prestação de serviços e respostas adaptadas a cada pessoa, melhorando a sua eficácia e reduzindo o desperdício e os custos em saúde;  
- Investir numa medicina de proximidade, dotando as unidades de cuidados de saúde primários de todos os meios de diagnóstico básicos, serviços de saúde psicológica, nutrição, saúde oral e visual, bem como condições para o tratamento de determinadas patologias, sem necessidade de recurso aos serviços de urgência;  
- Criar a figura do Psicólogo do Trabalho que, à semelhança e num modelo próximo dos Enfermeiros e Médicos do Trabalho, assumirá a responsabilidade da avaliação dos riscos psicossociais e do bem-estar no âmbito da vigilância da saúde;  
- Alargar o modelo organizacional das Unidades de Saúde Familiares - B a todos os serviços de Cuidados de Saúde Primários;  
- Rever o sistema de referenciação urgente, de forma a dispor de um serviço de atendimento permanente ou uma urgência básica à qual pelo menos 90% da população possa aceder através de uma viatura em 30 minutos e uma urgência médico-cirúrgica a não mais de 60 minutos;  
- Reforçar e agilizar a ação do INEM e da linha Saúde 24 em todo o território;  
- Avaliar as necessidades dos I.P.O. (Instituto Português de Oncologia), com vista ao aumento de recursos humanos necessários, espaço físico (insuficiente para as necessidades) e aquisição de equipamentos capazes de garantir resposta adequada, em tempo útil, ao número crescente de doenças oncológicas;  
- Contratar profissionais de psicologia para apoio de todos os/as profissionais de saúde que necessitem e também para apoio a utentes e famílias que vivenciem situações traumáticas;  
- Integrar profissionais de psicologia em todos os Cuidados de Saúde primários;  
- Apostar nas Unidades de Cuidados na Comunidade como pilar essencial na promoção da saúde preventiva;  
- Apostar na inovação na saúde, criando um fundo de investimento para startups que trabalhem nesta área e que comprovadamente ofereçam tratamentos diferenciados, inovadores e que comprovadamente melhorem a prestação dos cuidados de saúde aos pacientes e incentivando parcerias entre hospitais públicos e empresas de inovação na saúde;  
- Procurar promover a investigação e desenvolvimento na área da inteligência artificial e da ciência de dados na saúde;  
- Reforçar as competências de acompanhamento da Direção-Geral da Saúde nos hospitais, para garantir a qualidade dos serviços de saúde prestados;  
- Apostar em programas de formação contínua dos profissionais de saúde; e  
- Reforçar os serviços de Saúde Pública com condições de trabalho adequadas e técnicos/as de saúde pública e saúde ambiental correspondentes às necessidades permanentes de todos os serviços do SNS.  
Para uma saúde de proximidade e que coloca o utente no centro dos cuidados de saúde, o PAN irá:  
- Incluir os públicos-alvo vulneráveis e específicos na avaliação e na definição de medidas públicas de saúde que lhes são dirigidas;  
- Sensibilizar e capacitar os serviços de saúde para a deteção de situações de potencial exclusão (crianças, mulheres, pessoas desempregadas, pessoas migrantes e pessoas em situação de sem-abrigo);  
- Investir eficazmente em saúde preventiva e melhor diagnóstico precoce;  
- Garantir a monitorização contínua de indicadores de saúde humana, animal e ambiental na perspetiva One Health, como recomendado pela Organização Mundial da Saúde;  
- Garantir condições para o cumprimento e alargamento dos programas de rastreio, diagnóstico e deteção precoce nos Cuidados de Saúde Primários, melhorando as taxas de sucesso e reduzindo custos em saúde (como rastreio da infeção pela Mutilação Genital Feminina, do cancro hereditário da mama, ovário e colorretal);  
- Implementar programas de saúde preventiva (prevenção de burnout, atividades físicas e de relaxamento, alimentação saudável) nos diversos serviços da Administração Pública e incentivar o seu desenvolvimento nas organizações privadas;  
- Integrar a alimentação saudável e a atividade física como eixos centrais das politicas educativas locais e planos de ação escolares  
- Desenvolver uma lista de produtos alimentares saudáveis e garantir a sua dedução em IRS;  
- Efetuar um estudo de qualidade nutricional e do risco de obesidade em todas as escolas do país e implementar um programa nutricional e de atividade física, promovida pelos ACES em articulação com as escolas e sociedade civil;  
- Integrar a prescrição de atividade física no âmbito das consultas de medicina geral e familiar;  
- Contratar profissionais com formação em atividade física e desportiva para, em articulação com os Cuidados de Saúde Primários, promoverem programas de prática de atividade física dirigidos a pessoas com patologias específicas (ex.: diabetes, obesidade) e promoção da mobilidade (ex.: idosos, limitações articulares);  
- Aprovar, em articulação com as ordens profissionais e organizações sindicais dos profissionais de saúde, um projeto-piloto que permita às farmácias comunitárias fazer, de acordo com percursos clínicos específicos, o atendimento de situações clínicas ligeiras, como sinusites, dores de garganta ou otites médias, com prescrição do tratamento adequado ou encaminhamento, quando justificado, para os cuidados de saúde primários;  
- Garantir que todos/as os/as cidadãos/ãs tenham médico/a e enfermeiro/a de família;  
- Garantir o rácio de 1 psicólogo por cada 5000 utentes no Serviço Nacional de Saúde;  
- Garantir o reforço das verbas para a saúde mental, referentes à ecoansiedade  
- Consagrar a dedução em sede de IRS de despesas com Serviços de Psicologia e não apenas na área de Psicologia Clínica;  
- Criar um Fundo Público de Saúde, financiado através de uma taxa de compensação proveniente de indústrias poluentes com impactos comprovados na saúde humana (ex.: suiniculturas, indústria da celulose, etc.) e também da atual taxação feita a produtos nocivos para a saúde humana (ex.: Álcool, Tabaco, etc.)  
- Assegurar a existência de um Banco de Leite Materno por cada Administração Regional de Saúde, capaz de dar resposta às necessidades de todas as crianças/famílias sem acesso a leite materno, priorizando os bebés prematuros;  
- Garantir respostas no âmbito da oncologia para proporcionar cuidados de proximidade para doentes e famílias;  
- Integrar o sistema social, escolas e autarquias na prevenção e tratamento numa lógica de sistema municipal de saúde, promovendo hábitos de alimentação mais saudáveis junto da população, sensibilizar para campanhas de vacinação, doenças contagiosas e doenças sexualmente transmissíveis;  
- Promover um acompanhamento na gravidez, parto e pós-parto cada vez mais humanizado, capacitando as instituições do SNS para as mais recentes evidências na área da obstetrícia e saúde materna, parto e pós-parto, e aleitamento materno;  
- Reforçar o tratamento das dependências por álcool e drogas ilícitas, adotando uma prática inclusiva destes doentes, designadamente através da formação profissional nos centros de desabituação para uma melhor reinserção social e laboral e criando, em articulação com o setor social e as autarquias locais, uma rede nacional de salas de consumo assistido para assegurar uma resposta integrada;  
- Promover a fixação de profissionais de saúde em áreas carenciadas, aprovando um regime de compensação das despesas de habitação e/ou deslocação para o local de trabalho, sendo fixado em 50% da remuneração base;  
- Avaliar a prestação dos cuidados de saúde não pelo número de consultas, mas pela qualidade e eficiência do tratamento, bem como a satisfação e recuperação do paciente;  
- Apostar num acompanhamento mais próximo dos doentes antes, durante e depois dos procedimentos, de forma a garantir o sucesso dos mesmos e a satisfação do paciente;  
- Assegurar que os jovens internados em estabelecimento de saúde que perfaçam dezoito anos de idade durante o seu internamento continuem a ter o direito de acompanhamento familiar durante o internamento pelo período adequado às necessidades médicas, psicossociais e educacionais do doente, definido em articulação entre o serviço pediátrico e o serviço geral;  
- Garantir a distribuição gratuita de produtos de higiene menstrual feminina em todas as unidades de saúde;  
- Consagrar o IVA Zero nos produtos de higiene menstrual;  
- Aprovar um programa de melhoria do atendimento e acompanhamento das vítimas de violência sexual no Serviço Nacional de Saúde, que garanta que todas as entidades integradas no SNS dispõem destes materiais e estão aptas a assegurar o atendimento adequado das vítimas de abuso sexual e de violação e que, após a realização de exames forenses, haja disponibilização de kits de higiene pessoal, de roupa e de outros recursos emergenciais às vítimas de abuso sexual ou de violação;  
- Garantir o acesso a nutrição entérica com comparticipação do Estado a 100% quando prescritas pelo SNS;  
- Possibilitar a recuperação do IVA das aquisições de material ou equipamento médico pelas IPSS;

---

[Documento 16] Partido: Partido Socialista | Tópicos: saude
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **2.ª MISSÃO:** UM ESTADO SOCIAL FORTE, MODERNO E INCLUSIVO > 2. Um Serviço Nacional de Saúde universal, forte e resiliente > 2.3.
##### 2.3.  
No âmbito da **valorização e diversificação dos cuidados de saúde de proximidade,** o PS propõe:  
- Melhorar a coordenação funcional ao nível da rede de Cuidados de Saúde Primários, reforçando a sua autonomia de gestão, técnica e organizativa, e integrando as respetivas unidades em redes de proximidade, articulando competências e recursos e incluindo cuidados de outros serviços;  
- Reforçar e diversificar a oferta de cuidados de proximidade, melhorando o acesso a, entre outras, respostas de saúde oral e visual, pediatria, terapia da fala, psicologia clínica, saúde mental e nutrição. Neste âmbito assegurar, nomeadamente:  
- A generalização de rastreios visuais e auditivos na infância, antes da entrada no 1º ciclo do ensino básico, estabelecendo um programa de atribuição gratuita de óculos a crianças de famílias com menores rendimentos.
- A prossecução do reforço da oferta de cuidados de saúde oral de proximidade, nomeadamente através da criação da carreira de medicina dentária no SNS e do aumento dos seus efetivos;  
- Continuar a expansão e cobertura ao nível da Rede Nacional de Cuidados Continuados e de Cuidados Paliativos, reforçando a oferta de proximidade em termos de unidades e de camas disponíveis;  
- Criar uma rede de atendimento permanente, a funcionar em centros de saúde de referência, servindo uma área geográfica delimitada e contribuindo assim para reduzir o recurso às urgências hospitalares;  
- Reforçar as respostas imediatas a pessoas sem médico e enfermeiro de família, mobilizando equipas multiprofissionais, envolvendo médicos e enfermeiros e outros profissionais ao serviço ou que estejam aposentados;  
- Investir na prevenção e promoção da saúde, apostando na saúde pública e no combate aos determinantes de saúde.

---

[Documento 17] Partido: Iniciativa Liberal | Tópicos: saude
  Secção: PROGRAMA ELEITORAL > B. PORTUGAL A FUNCIONAR > 2. MAIS ACESSO À SAÚDE
### 2. MAIS ACESSO À SAÚDE  
B 098 A Iniciativa Liberal está determinada a conseguir que todos tenham acesso aos cuidados de saúde que precisam, em tempo útil, com qualidade e próximos de si, atacando de frente as intermináveis listas de espera para consultas, cirurgias ou para a atribuição de um Médico de Família. Para tal, é fundamental que nos **afastemos de uma discussão centrada em quem presta o serviço público de saúde (se é o Estado, os privados ou o setor social) e que o foco da ação seja o utente**, com um forte investimento na medicina preventiva, na melhoria da qualidade de vida e no bem-estar físico e mental de todos os cidadãos.  
A Saúde precisa de ser desbloqueada para funcionar. Para os portugueses poderem contar com os cuidados de que precisam quando precisam, a Iniciativa Liberal defende a liberdade de escolha dos portugueses para decidirem onde querem ser atendidos e tratados. **Mais liberdade de acesso** para os utentes, e mais liberdade de gestão para as administrações da saúde, com maior autonomia e responsabilidade, é o que **permite que o sistema se adapte às reais necessidades de saúde dos portugueses**. Liberdade para os profissionais de saúde progredirem na sua carreira e atuarem de acordo com a melhor evidência científica. Liberdade para os reguladores independentes atuarem sempre que é preciso.  
Ao longo dos últimos anos, os portugueses têm assistido a uma degradação contínua, acelerada e sem fim à vista do Serviço Nacional de Saúde, evidente no aumento das listas de espera para consultas hospitalares e cirurgias, no número de pessoas sem médico de família e no encerramento de serviços de urgência. Do lado dos profissionais de saúde, têm-se acentuado as saídas do Serviço Nacional de Saúde, quer para outros setores, quer para o estrangeiro, quer, mesmo, por abandono da profissão. Uma perda enorme de potencial humano altamente qualificado e diferenciado e de investimento formativo que será difícil de recuperar.  
Existem hoje mais de 1 milhão e 700 mil pessoas sem Médico de Família atribuído, num sistema público de saúde que exige referenciação para consultas hospitalares, impedindo o verdadeiro acesso dos portugueses aos cuidados necessários para garantir a sua saúde e bem-estar.  
Tudo isto é a explicação para que, apesar do Serviço Nacional de Saúde ser universal e tendencialmente gratuito e da elevada carga fiscal para financiar a Saúde, a OCDE indique que 3 milhões e 700 mil portugueses já subscrevem voluntariamente seguros de saúde, gastando cerca de 5% do orçamento familiar em saúde – e pagando diretamente quase 30% dos gastos em saúde – com mais de 1 milhão de famílias portuguesas com gastos "catastróficos" por despesas em saúde. Números desoladores e que nos colocam entre os países da OCDE em que as famílias mais dependem de recursos próprios para tratar da sua saúde. É tempo de mudar.

---

[Documento 18] Partido: CHEGA | Tópicos: saude, trabalho
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > IV CAPÍTULO GARANTIR O ACESSO À SAÚDE. COMO? > PRIORIDADES
### PRIORIDADES  
- Modernizar o SNS, fazendo uso das inovações tecnológicas e inteligência artificial, garantindo assim uma maior informatização, eficiência operacional e, consequentemente, um melhor serviço prestado ao utente;  
- Alterar o paradigma para Sistema Nacional de Saúde, assegurando uma resposta integrada ao cidadão através da articulação dos serviços de saúde públicos, privados e sociais;  
- Investir na prevenção da doença e promoção da saúde;  
- Reforçar os cuidados primários e o atendimento de urgência, com a garantia de atribuição de médico família a todos os cidadãos;  
- Promover a valorização e fixação dos profissionais de Saúde no SNS.

---

[Documento 19] Partido: Bloco de Esquerda | Tópicos: saude, financas
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 2 Saúde > 2.5 Investir no SNS, combater o negócio da saúde > Medidas para financiar o SNS
#### Medidas para financiar o SNS  
- → Adequar o Orçamento do SNS às reais necessidades da população. Para isso, as instituições do SNS – hospitais, centros de saúde, INEM, etc. – devem comunicar as suas necessidades previstas orçamentais, de investimento e de pessoal, e o orçamento do SNS do ano subsequente deve corresponder às necessidades identificadas;
- → Autonomia e responsabilização das administrações das unidades do SNS que permitam resposta adequada e em tempo útil às necessidades de cada momento;
- → Criar um plano plurianual de investimentos associado a uma carta nacional de equipamentos de saúde, com dotação própria, que permita combater a obsolescência tecnológica pela renovação e aquisição de novos equipamentos;
- → Excluir o SNS da aplicação da Lei dos Compromissos;
- → Integração no SNS dos hospitais que o governo PSD/CDS entregou (e que o PS manteve) à gestão das Santas Casas da Misericórdia (Serpa, Anadia e Fafe);
- → Revogar o decreto-lei que regula as parcerias de gestão na área da saúde e abre portas a novas parcerias público-privado no SNS, da legislação que permite a privatização dos cuidados de saúde primários através das USF-C e do decreto-lei que cria as novas ULS, que concentra recursos e afasta os serviços das populações;  
→ Gestão democrática das unidades de saúde.

---

[Documento 20] Partido: LIVRE | Tópicos: saude
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > **Saúde**
## **Saúde**  
A saúde, enquanto estado de bem-estar físico, mental e social e não apenas a ausência de doença, é uma componente fundamental para o pleno desenvolvimento individual e coletivo e, desse modo, uma das principais prioridades políticas do LIVRE. A nível global, as dificuldades económicas e a polarização da sociedade, as emergências de saúde pública, humanitárias e climáticas afetam a saúde física e mental de populações inteiras, como ficou bem demonstrado durante a pandemia de COVID-19 e as sucessivas crises económicas. A pandemia veio relembrar-nos que qualquer negligência política ou orçamental na área da Saúde tem um preço demasiado elevado. Persistem graves problemas no acesso da população aos serviços públicos de saúde mesmo após a criação da Direção Executiva do Serviço Nacional de Saúde (SNS) e a reorganização dos centros de saúde e hospitais em Unidades Locais de Saúde, destacando a falta e a exaustão de profissionais de saúde para garantir serviços de urgência e atendimento nos centros de saúde.  
Defendemos que compete ao Estado assegurar a proteção da saúde e que esta seja universal, gratuita e adequada às características da população em todo o território.  
Em Portugal, o principal prestador de cuidados de saúde deve ser o Serviço Nacional de Saúde - que consideramos essencial para assegurar a igualdade e a liberdade. A sua ação pode ser complementada pelos setores privado e social, com os quais deve ter protocolos e convenções apenas nas áreas onde se considera que não tem recursos que permitam garantir uma resposta adequada, devendo a relação entre os três setores ser transparente, honesta e regulada e no sentido da capacitação do SNS nas áreas em que seja deficitário.  
O LIVRE está seguro de que o Serviço Nacional de Saúde só sobreviverá com uma estratégia global urgente para a Saúde, que respeite integralmente a nova Lei de Bases da Saúde, concluindo os projetos estabelecidos no Plano de Recuperação e Resiliência e tirando vantagem da recente reorganização em Unidades Locais de Saúde, que conceptualizam o princípio da integração de cuidados e autonomia regional na Saúde.  
É essencial a integração e boa articulação dos vários níveis de cuidados em que o utente ou a pessoa com doença esteja no centro, independentemente do prestador, assim como a existência de cuidados de proximidade e a humanização da saúde.  
O conceito de saúde ultrapassa, contudo, os estabelecimentos onde são prestados cuidados. Em Portugal, as dificuldades de saúde estão particularmente associadas a determinantes sociais como o elevado risco de pobreza e a desigualdade; à discriminação e à violência; aos baixos níveis de literacia em saúde; à precariedade laboral e condições de trabalho; à falta de acesso a habitação e saúde; ao isolamento social e ao envelhecimento da população; e à falta de oportunidades para o pleno desenvolvimento individual e ocupacional decorrentes da baixa escolaridade e dos baixos salários. Importa ter cuidados de proximidade fortalecidos, com profissionais de saúde e assistentes técnicos de áreas fundamentais como medicina geral e familiar, enfermagem, diagnóstico, terapêutica (incluindo higienistas orais, terapeutas da fala, fisioterapeutas, terapeutas ocupacionais), nutrição, psicologia, medicina dentária, serviço social em número adequado, assim como é urgente dotar os hospitais de meios materiais e humanos suficientes. É prioritário aumentar a fração do orçamento de saúde dedicada à prevenção da doença e promoção de Saúde, e dotar as instituições de Saúde Pública de recursos e de um efetivo poder de decisão junto dos dossiês em que considerem necessário intervir. Mas é igualmente importante que haja uma integração desta área em todas as outras que intervêm ao nível dos determinantes da saúde (nível socioeconómico, condições e estilos de vida, educação, apoio social - segurança social, municípios e misericórdias): a "Saúde em todas as políticas".  
O investimento na saúde mental é também uma das prioridades do LIVRE. Tal como as restantes áreas da saúde, os cuidados de saúde mental - desde a promoção da saúde mental ao tratamento especializado das doenças mentais - devem ser acessíveis a todas as pessoas. Portugal tem carência de profissionais especializados em saúde mental (psiquiatras, psicólogos, enfermeiros e técnicos de serviço social), elevadas listas de espera no SNS e grandes disparidades territoriais na cobertura de serviços de saúde mental. Adicionalmente, a pandemia de COVID-19 contribuiu para a deterioração da saúde mental da população e para o aumento da pressão sobre os serviços de saúde mental e os seus profissionais. Assim, todas as políticas públicas devem ter em consideração o seu impacto nas condições estruturais para a satisfação das necessidades psicológicas inerentes ao pleno desenvolvimento humano como são a autonomia, o sentimento de competência e o sentimento de pertença. As políticas de saúde mental devem ser pensadas intersetorialmente e não no âmbito exclusivo da saúde, tal como preconizado pelo Plano Nacional de Saúde Mental. As políticas públicas de habitação e urbanismo, educação, trabalho, justiça, segurança social, cultura e ciência devem igualmente prever a promoção da saúde mental e a integração de pessoas com necessidades de cuidados de saúde mental. A exaustão do sistema e seus profissionais, trazida pela pandemia mas que ainda persiste, exige-nos o reconhecimento do seu valor por meio da adoção de medidas que respondam aos apelos dos trabalhadores e às necessidades da população, salvando o Serviço Nacional de Saúde.  
Propomo-nos ouvir todas as pessoas, nomeadamente profissionais de saúde e utentes, no sentido de encontrar soluções a longo prazo que fortaleçam o SNS e que façam com que todas as pessoas se revejam nele, o sintam como seu e se motivem para contribuir para a sua sustentabilidade e qualidade a longo prazo. As propostas no âmbito da saúde estão organizadas em cinco eixos prioritários:  
- Reforçar e Reorganizar o Serviço Nacional de Saúde
- Valorizar as carreiras profissionais no SNS
- Promover a saúde e prevenir a doença
- Humanizar os cuidados de saúde
- Investir na Saúde Mental

---

[Documento 21] Partido: Bloco de Esquerda | Tópicos: saude, trabalho
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 2 Saúde
## 2 Saúde  
**Ao recusar medidas eficazes de recrutamento e retenção de profissionais, o governo da maioria absoluta tornou o SNS um projeto a prazo, feito de espera em vez de acesso e de encerramentos em vez de garantia.**  
**O Bloco define as condições para a salvaguarda das carreiras de Saúde e para o investimento que assegure os meios próprios do SNS, reduzindo o desperdício com o recurso a privados, reforçando os cuidados primários e resolvendo as lacunas nas áreas da saúde oral ou mental.**

---

[Documento 22] Partido: LIVRE | Tópicos: saude, educacao
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > **Saúde** > Por isso defendemos: > Reforçar e Reorganizar o Serviço Nacional de Saúde
### Por isso defendemos:  
#### Reforçar e Reorganizar o Serviço Nacional de Saúde  
1. **Fortalecer e avançar com a reforma do SNS:**  
- monitorizar a nova organização do SNS com o alargamento das Unidades Locais de Saúde (ULS) a todo o território nacional, acompanhando o modelo de gestão integrada dos centros hospitalares, os hospitais, os Agrupamentos de Centros de Saúde (ACeS) e a Rede Nacional de Cuidados Continuados e avaliando os resultados na qualidade da prestação dos cuidados de saúde;
- monitorizar a generalização das Unidades de Saúde Familiar (USF) de modelo B. com base em comunidades locais e avaliar os resultados do aumento do número de utentes com médico de família atribuído e a melhoria da qualidade da prestação dos cuidados de saúde decorrente dos incentivos associados ao desempenho das equipas no acompanhamento de utentes;
- promover a auto-organização interna das ULS e a articulação eficaz com as unidades de cuidados de saúde que as integram, assim como a articulação entre ULS;
- assegurar a transparência e capacidade de planeamento estratégico no SNS implementando a obrigatoriedade de que os prestadores privados de cuidados de saúde disponibilizem, em formato comparável, dados sobre o número de utentes tratados, patologias e atos médicos realizados, número de especialistas contratados por área, enfermeiros e outro pessoal, equipamentos e meios complementares de diagnóstico, capacidade de internamento e de cuidados intensivos, salas de operações, remunerações médias de cada classe profissional e horários de atividade como condição para a articulação com o SNS;
- assegurar que no SNS todas as funções são livres de nomeação política, nomeadamente os cargos de chefia, que deverão ser eleitos interpares e com um limite máximo de 2 mandatos, de forma transparente e democrática;
- redefinir os objetivos do SNS com métricas claras de melhoria do estado da população e promover o cumprimento destes objetivos através da recompensa profissional e institucional;
- garantir os direitos dos utentes nos tempos de resposta e na qualidade dos cuidados prestados;
- afirmar a verdadeira transição digital do SNS para agilizar o trabalho de médicos, enfermeiros e auxiliares, de modo a diminuir a excessiva burocratização e garantir a utilização do mesmo sistema informático em todas as unidades de saúde do SNS, abrindo caminho para um paradigma de investigação federada em Saúde respeitante da privacidade de utentes e profissionais de Saúde.  
2. **Reforçar os cuidados de Saúde Primários, tornando-os mais próximos das populações e adaptados às necessidades de cada utente:**  
- trabalhar no sentido de garantir a todas as pessoas em Portugal um médico de família, fixando profissionais no SNS, melhorando as suas condições laborais, e a sua integração em equipas com assistentes operacionais, assistentes sociais e pessoal administrativo (assistentes técnicos);
- garantir que o número de utentes de cada médico de família permite um acompanhamento efetivo, reduzindo o número de utentes para menos de 1500 utentes por médico;
- promover o aumento para número suficiente de serviços como exames de diagnóstico, fisioterapia, saúde mental e outros que possam prevenir a doença e minimizar o recurso às urgências;
- generalizar a implementação de um sistema de consultoria de especialidades médicas aos cuidados de saúde primários, através da realização de reuniões multidisciplinares, diminuindo assim o número de referenciações a cuidados de saúde especializados e a necessidade de deslocação de utentes a centros hospitalares;
- garantir a generalização da prescrição social a todos os centros de saúde, em estreita articulação com as comunidades e as estruturas existentes;
- incluir psicólogos clínicos e nutricionistas nas equipas de saúde dos cuidados de saúde primários, assegurando que cada centro de saúde tem pelo menos um psicólogo clínico a trabalhar em articulação com os restantes profissionais.  
3. **Garantir o funcionamento integrado, acessível e humanizado das Urgências Hospitalares:**  
- garantir o funcionamento em rede dos serviços de urgência de forma acessível a toda a população, o cumprimento dos rácios de profissionais de saúde, e a prestação de cuidados de qualidade;
- promover o funcionamento alargado dos centros de saúde e dos serviços de Urgência Básica e dotá-los das condições que permitam o atendimento de utentes de menor gravidade, com possibilidade de realização de exames e análises clínicas, contribuindo para a redução da afluência às urgências dos hospitais;
- generalizar equipas fixas de profissionais diferenciados nos serviços de urgência e com contrato hospitalar, evitando recorrer a prestação de serviços;
- reforçar os recursos e meios da linha SNS24 principalmente em períodos de maior afluência às urgências e estudar a possibilidade de, em casos específicos, transferir a chamada para médicos, a prescrição de Meios Complementares de Diagnóstico através desta linha, ou agendamento de consultas urgentes nos centros de saúde, evitando a sobrecarga dos serviços de urgência a transferência de chamadas;
- salvaguardar a dignidade das pessoas nas urgências e promover a regular informação aos acompanhantes de utentes;
- desenvolver campanhas nacionais de literacia para a saúde, que envolvam também representantes de utentes, através dos meios de comunicação social, escolas, universidades, autarquias e juntas de freguesia, alertando para os principais sinais de alarme para recorrer à Urgência e modos de evitar as urgências hospitalares em situações tendencialmente não urgentes (ligar para a linha SNS 24 ou recorrer aos serviços de Urgência Básica nos Cuidados de Saúde Primários).  
4. **Assegurar um financiamento adequado do SNS:**  
- assegurar a sua gestão pública, salvaguardando a qualidade e resposta eficiente dos serviços, e não renovar os contratos das Parcerias Público-Privadas atualmente ainda em curso;
- executar a gestão pública, dando primazia a contratos de trabalho estáveis, ao invés de prestação de serviços médicos;
- garantir um orçamento suficiente e não condicionado por cativações e com a sub-orçamentação crónica do SNS, promovendo a eficiência e eficácia na sua gestão;
- atrair investimento internacional no SNS, nomeadamente na área de investigação clínica, afirmando os hospitais do SNS como centros de referência de ensaios clínicos.  
5. **Promover a renovação, reabilitação e construção das infraestruturas do SNS**, fazendo um levantamento de todo o edificado das Unidades Locais de Saúde que necessita de uma reabilitação urgente e investindo na construção de novos edifícios essenciais à prestação de cuidados mais acessíveis.  
6. **Facilitar e tornar mais equitativo o acesso aos cuidados de saúde e de prevenção da doença**, ao:  
- eliminar as taxas moderadoras ainda existentes até que se obtenha evidência de que a sua existência não condiciona negativamente comportamentos necessários de acesso aos serviços de urgência;
- garantir que ninguém deixe de cumprir um regime terapêutico por insuficiência económica, através da revisão dos regimes de comparticipação;
- garantir estruturas de saúde de proximidade a toda a população;

---

[Documento 23] Partido: Aliança Democrática | Tópicos: saude, educacao
  Secção: PROGRAMA ECONÓMICO DA ALIANÇA DEMOCRÁTICA > Sumário Executivo > II. POR QUE É PRECISO MUDAR? O PAÍS ESTAGNADO, O CAMINHO ERRADO > 1. DIAGNÓSTICO CRÍTICO DE UM PAÍS ESTAGNADO
### II. POR QUE É PRECISO MUDAR? O PAÍS ESTAGNADO, O CAMINHO ERRADO  
#### 1. DIAGNÓSTICO CRÍTICO DE UM PAÍS ESTAGNADO  
Após 8 anos de governação do Partido Socialista, que totalizou 22 dos últimos 29 anos, a realidade portuguesa é dura e preocupante:  
- Economia estagnada, com **baixíssimo crescimento económico** nas duas décadas passadas (média anual de 0,8% desde 2000), e na próxima década e meia, segundo projeções credíveis para os próximos anos;
- Portugal tem sido **sucessivamente ultrapassado, caminhando para a cauda da Europa** em PIB per capita em paridades de poder de compra (desde 2000 foi ultrapassado por 6 países da Coesão, e em 2024, prevê-se que o seja também pela Roménia);
- **Cresceu muito o número de trabalhadores que auferem o salário mínimo nacional**, para cerca de 840 mil, e **diminuiu o diferencial para os ganhos médio e mediano**, que não acompanharam a evolução do valor mínimo legalmente fixado. Cerca de dois terços dos jovens têm um rendimento mensal inferior a mil euros;
- A **pobreza atinge níveis inadmissíveis**, tendo a taxa de risco de pobreza aumentado em 2022, com uma taxa antes de prestações sociais superior a 41% da população, maior do que a registada no início do século;
- Têm-se **agravado** os vários indicadores de **desigualdade do rendimento** nos últimos cinco anos;
- A **emigração jovem qualificada atinge níveis brutais**, estimando-se que cerca de 30% dos jovens nascidos em Portugal vivam fora do país; esta é a taxa de emigração mais elevada da Europa e uma das maiores do mundo. Os que não emigram enfrentam um desemprego jovem que ultrapassou os 20% no final de 2023 e são, em média, os que na Europa mais tarde saem de casa dos seus pais;
- A **carga fiscal atingiu o valor máximo de sempre**, tendo batido recordes ano após ano, nos últimos oito anos (de cerca de 37% do PIB em 2015 para 38,5% em 2022). **O esforço fiscal** dos portugueses (que mede a carga fiscal de cada país ajustada pelo nível de vida dos seus cidadãos) **é o 4.º mais elevado da Europa**;
- A essa carga fiscal recorde tem correspondido um **Estado em séria falência operacional**, com gravíssimos problemas nos serviços públicos mais críticos, da saúde à educação, da justiça à segurança, da habitação aos serviços de atendimento ao público;
- Na **Saúde**, o número de utentes sem médico de família passou de cerca de 1 milhão para 1,7 milhões de pessoas, aumentaram as listas de espera para consultas e cirurgias e os tempos de espera tornaram-se ainda mais indignos; as urgências e serviços de maternidade funcionam em intermitência. Em sinal de desistência (possível para quem tem recursos) já cerca de 5 milhões de portugueses têm uma segunda cobertura (seguro de saúde privada, ADSE ou outros sistemas), que é paga em acréscimo aos impostos que suportam para financiar o SNS;
- Na **Educação**, o desempenho dos alunos portugueses tem caído dramaticamente desde 2018, em todas as avaliações internacionais, em todas as dimensões (português, matemática e ciências). Nas escolas acumulam-se os alunos sem aulas, e os professores estão esgotados e em conflito com o Governo. Em sinal de desistência (possível para quem tem recursos) já cerca de 25% dos estudantes do ensino secundário frequentam escolas privadas;
- Os preços das casas aumentaram muito mais do que os rendimentos das famílias. Desde 2016 até ao final de 2022, os preços da habitação subiram 89% ao passo que o rendimento nominal _per capita_ aumentou 33,8%;
- A produtividade também tem estado praticamente estagnada, crescendo a uma taxa média anual de 0,7% entre 2000 e 2022;
- Persistem **baixos níveis de investimento e poupança**. A formação bruta de capital fixo em percentagem do PIB é hoje muito inferior aos valores do início do século (20% vs 27%) e a taxa de poupança das famílias atinge os níveis mais baixos de que há memória.

---

[Documento 24] Partido: Partido Socialista | Tópicos: saude
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **2.ª MISSÃO:** UM ESTADO SOCIAL FORTE, MODERNO E INCLUSIVO > 2. Um Serviço Nacional de Saúde universal, forte e resiliente
#### 2. Um Serviço Nacional de Saúde universal, forte e resiliente  
O Serviço Nacional de Saúde (SNS) é um dos pilares do Portugal democrático e a grande construção dos socialistas no pós-25 de abril. A melhoria progressiva, e significativa, da qualidade de vida dos portugueses nos últimos 50 anos é indissociável da criação de um serviço público universal e tendencialmente gratuito. O que distingue o SNS dos demais prestadores é, de facto, a centralidade que atribui ao estado de saúde das pessoas e o foco na preservação e melhoria dos índices de saúde da população.  
Ao longo dos últimos 8 anos, os governos do PS deram um novo impulso ao SNS, reforçando as suas valências e criando as bases orçamentais para a sua resiliência e sustentabilidade. Entre 2015 e 2024 o orçamento do SNS aumentou em mais de 5,6 mil milhões, contando hoje com cerca de 150 mil profissionais, mais 25% do que há oito anos.  
Foi também neste período que se aprovou a Lei de Bases da Saúde, o Estatuto do SNS e, por seu efeito, a atual Direção Executiva do SNS, reformas que devem ser prosseguidas e aperfeiçoadas, cabendo ao futuro Governo do PS promover as alterações necessárias, em diálogo com todos os agentes do setor, incluindo as associações de utentes.  
Apesar do investimento recente, os portugueses despendem uma parte elevada do seu rendimento em saúde, com uma parte significativa da despesa pública relacionada com o pagamento de serviços que não encontram a sua resposta plena no SNS. Defender, consolidar e capacitar o SNS é por isso uma prioridade essencial, que será concretizada em nove eixos fundamentais.

---

[Documento 25] Partido: CHEGA | Tópicos: saude
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > IV CAPÍTULO O QUE JÁ FIZEMOS PARA GARANTIR O ACESSO À SAÚDE
## IV CAPÍTULO O QUE JÁ FIZEMOS PARA GARANTIR O ACESSO À SAÚDE  
**PROJECTO DE LEI 812/XV/1 (CH)**  
Altera o Decreto-Lei n.º 298/2007, de 22 de agosto, de forma a garantir o acesso universal a Médico Especialista em Medicina Geral e Familiar  
**PROJECTO DE LEI 880/XV/1 (CH)**  
Altera a Lei de Bases da Saúde, estabelecendo a obrigação do Estado referenciar os utentes do Serviço Nacional de Saúde (SNS) para atendimento nos sectores privado ou social em caso de esgotamento dos tempos máximos de resposta garantidos  
**PROJECTO DE RESOLUÇÃO 750/XV/1 (CH)**  
Recomenda ao Governo que adote medidas para aumentar a eficácia, eficiência e produtividade do Serviço Nacional de Saúde, particularmente nas zonas e regiões mais carenciadas  
**PROJECTO DE RESOLUÇÃO 940/XV/2**  
Recomenda ao Governo o alargamento urgente da Rede de Cuidados Paliativos  
**REJEITADO**  
**CONTRA** Partido Socialista, PCP, L **ABSTENÇÃO** PSD, IL, BE **FAVOR** CHEGA  
**REJEITADO**  
**CONTRA** Partido Socialista, PCP, BE, L **ABSTENÇÃO** IL **FAVOR** PSD, CHEGA, PAN  
**REJEITADO**  
**CONTRA** Partido Socialista, PCP, BE **ABSTENÇÃO** IL, PAN, L **FAVOR** PSD, CHEGA  
**SEM VOTAÇÃO**

---

[Documento 26] Partido: Partido Comunista Português | Tópicos: saude
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 4 ELEVAR A QUALIDADE DE VIDA. INVESTIR NOS SERVIÇOS PÚBLICOS, CUMPRIR AS FUNÇÕES SOCIAIS DO ESTADO > 4.1. A defesa do Serviço Nacional de Saúde e uma política de saúde ao serviço dos portugueses > 4.1.2 Reforçar os meios financeiros e técnicos, melhorar as condições de trabalho e de prestação de cuidados
##### 4.1.2 Reforçar os meios financeiros e técnicos, melhorar as condições de trabalho e de prestação de cuidados  
- Reduzir as transferências para o sector privado a partir do orçamento do SNS, reforçando o seu financiamento e internalizando serviços com utilização total dos recursos existentes;
- Aumentar o investimento público em saúde,reforçando a rede pública de instalações, acelerando a compra de equipamentos, em particular de meios auxiliares de diagnóstico e terapêutica, concretizando as infra-estruturas já anunciadas e programando novas intervenções;
- Aumentar a capacidade hospitalar do SNS, modernizando e actualizando as unidades existentes, planeando e construindo mais unidades, aumentando camas de agudos, equipamentos de diagnóstico e terapêutica, nomeadamente o designado por equipamento pesado com destaque para a área de oncologia;
- Criar condições para a utilização da telessaúde em complemento da prestação de cuidados de saúde tradicionais e reforçando, por esta via, o acesso ao SNS e a resposta dada ao nível dos Cuidados de Saúde Primários e dos cuidados hospitalares.

---

[Documento 27] Partido: LIVRE | Tópicos: saude, educacao, igualdade
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > **Saúde** > Por isso defendemos: > **Humanizar os cuidados de saúde**
- criar um Programa de Contacto Familiar, de abrangência nacional, para facilitar a comunicação entre pacientes e as suas famílias por meio de tecnologias, como videochamadas, em situações de restrições de visitas.  
27. **Proteger os Cuidadores Informais:**  
- acompanhando a aplicação do estatuto do cuidador informal, aprovado em 2019;
- agilizando o processo de reconhecimento do estatuto de cuidador informal e atribuição do respetivo subsídio;
- garantindo um maior acompanhamento das famílias e de cuidadores para conseguirem lidar com a doença, tanto física como mental.  
28. **Envolver as pessoas com doença ou associações representativas de doentes** nos processos de tomada de decisão política na área da saúde e no desenho e reestruturação dos serviços de saúde e na investigação clínica.  
29. **Promover um acesso justo e não discriminatório aos cuidados de saúde** ao:  
- garantir um melhor acompanhamento das pessoas LGBTQIA+ no SNS, reforçando as unidades no país com serviços especializados na saúde das pessoas trans e intersexo, investindo na educação e formação de profissionais de saúde do SNS para questões e identidades LGBTQIA+, tanto de acompanhamento clínico como de atendimento e dando continuidade à elaboração e implementação da Estratégia de Saúde para as Pessoas Lésbicas, Gays, Bissexuais, Trans e Intersexo (LGBTI);
- garantir a presença de pessoal com formação em língua gestual portuguesa, assim como uma rede de tradutores e intérpretes rapidamente ativada para dar resposta às comunidades emigrantes que não falam português;
- garantir a tradução em várias línguas dos folhetos informativos para utentes que não falam português, reforçar e divulgar o acesso a serviços de tradução gratuitos que garantam uma comunicação mais eficiente entre profissionais e utentes;
- criar áreas de relaxamento em ambientes hospitalares, sensorialmente adaptadas e acolhedoras com atividades terapêuticas para pacientes e familiares.  
30. **Promover a saúde menstrual e obstétrica:**  
- possibilitar a licença menstrual sem perda de retribuição com apresentação de atestado médico, em casos de doenças incapacitantes como a endometriose e adenomiose;
- melhorar as condições que permitam respeitar as vontades de grávidas, em trabalho de parto e puérperas, incluindo a de estarem acompanhadas por uma pessoa da sua escolha a tempo inteiro aquando do internamento;
- combater a violência obstétrica explícita e estrutural, através de sensibilização, formação de profissionais de saúde e legislação própria, reconhecendo também as desigualdades acrescidas que afetam as mães negras e racializadas, as mulheres lésbicas e as pessoas trans e de género diverso;
- promover a normalização da menstruação, bem como o ensino e promoção da utilização de produtos menstruais sustentáveis e garantir o acesso a produtos de higiene íntima para quem o necessite (nomeadamente através de dispensadores gratuitos de cuecas menstruais e copos menstruais) nos centros de saúde, escolas e instituições de ensino superior, estabelecimentos prisionais e centros educativos;
- garantir o acompanhamento da menopausa e andropausa no SNS, promovendo a informação e o acesso a reposição hormonal de forma a aumentar a qualidade de vida e a prevenir o aparecimento de doenças extra-ginecológicas e extra-urológicas, como alterações do metabolismo ósseo, alterações cardiovasculares e vasomotoras, perturbações do sistema nervoso central ou outra sintomatologia neuropsíquica ou endocrinológica.  
31. **Elaborar um Plano Nacional de Apoio à Fertilidade** ouvindo utentes e suas entidades representativas de, e que inclua, nomeadamente, medidas para:  
- a promoção da literacia para a fertilidade da população;
- a redução das listas de espera para acesso a tratamentos de Procriação Medicamente Assistida (PMA);
- a promoção da doação de gâmetas e ovócitos em Portugal;
- a definição de critérios de prioridade no acesso a técnicas de PMA;
- o apoio económico, psicossocial e emocional das pessoas doadoras e beneficiárias de tratamentos de fertilidade;
- a criação de um centro público de recolha de gâmetas no Alentejo ou Algarve;
- assegurar a comparticipação das despesas de deslocação e estadia incorridas por pessoas doadoras e beneficiárias residentes em áreas desprovidas de respostas públicas especializadas;
- alargar os critérios do regime excecional para acesso a técnicas de PMA no SNS, nos casos de preservação do potencial reprodutivo por doença grave para incluir, entre outras, a endometriose e a adenomiose.  
32. **Garantir o direito à Interrupção Voluntária da Gravidez (IVG) em todo o território nacional:**  
- alargando o prazo para as 14 semanas, já que o atual limite de 10 semanas é curto para a tomada de decisão considerando: que o ciclo menstrual para muitas pessoas é irregular na sua duração e que podem descobrir mais tardiamente que estão grávidas, o tempo de espera para marcação de consulta de planeamento familiar no Serviço Nacional de Saúde e o período de tempo para o processo da IVG;
- removendo o período obrigatório de reflexão de três dias entre a consulta com o profissional de saúde e o procedimento por ser uma medida moralista e opressiva que limita mais uma vez o acesso seguro ao aborto. O processo de ponderação pessoal inicia-se previamente ao momento da consulta e não se faz por indicação médica;
- promovendo as alterações legislativas e de reorganização dos serviços de saúde com o objetivo de assegurar a implementação dos critérios internacionais em matéria de IVG, por forma a garantir o direito à IVG mas respeitando o direito à objeção de consciência de profissionais objetores de consciência;
- retomando as publicações anuais dos relatórios dos registos das IVG que devem passar a incluir dados sobre a capacidade de resposta do SNS e estatísticas sobre objetores de consciência;
- garantindo a mobilização de recursos, a nível nacional, para a realização de IVG quando a objeção de consciência de profissionais de saúde impedir o procedimento numa determinada região ou durante certo período;
- alargando o período de apoio psicológico para a fase após a realização da IVG, caso desejado;
- revendo e sistematizando as possibilidades de âmbito e discricionariedade de declarações de objeção de consciência para atos médicos;
- zelando pela privacidade das pessoas que recorrem à IVG, nos casos em que têm de prestar uma declaração de presença nas consultas/tratamentos junto da entidade patronal, para que essa declaração não contenha elementos identificativos da instituição em que decorre a IVG;

---

[Documento 28] Partido: Partido Socialista | Tópicos: saude, trabalho
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **2.ª MISSÃO:** UM ESTADO SOCIAL FORTE, MODERNO E INCLUSIVO > 2. Um Serviço Nacional de Saúde universal, forte e resiliente > 2.1.
##### 2.1.  
No âmbito da **valorização dos profissionais de saúde,** o PS compromete-se a:  
- Encetar negociações imediatas com os profissionais de saúde, no âmbito de um plano concertado de revisão das carreiras e de valorização salarial, reforçando a vertente de formação e investigação e melhorando as condições de trabalho;  
- Equiparar a posição de entrada dos enfermeiros aos licenciados da carreira geral da Administração Pública;  
- Incentivar a dedicação plena e em exclusividade ao SNS, assegurando a devida valorização das carreiras e a especialização clínica funcional, reorientando para estes objetivos os incentivos à produção;  
- Definir e atribuir incentivos especiais aos profissionais que trabalhem em territórios menos atrativos, através de apoios ao alojamento e às famílias, assegurando o seu desenvolvimento profissional e o acesso à telemedicina e a pertença a equipas multidisciplinares;  
- Rever o atual quadro de alocação de tarefas aos profissionais do SNS, seguindo os melhores padrões internacionais, tendo em vista a elevação dos níveis de eficiência e eficácia, na perspetiva dos cuidados aos utentes;  
- Promover uma maior abrangência de atividade de enfermagem, sobretudo nos contextos em que a resposta médica é insuficiente, aumentando a capacidade de prestação de cuidados de proximidade;  
- Rever e dignificar a carreira dos administradores hospitalares e das chefias intermédias, promovendo a sua valorização salarial e a adoção de um modelo de avaliação de desempenho adequado;  
- Avaliar a possibilidade de introdução de um tempo mínimo de dedicação ao SNS pelos profissionais de saúde, nomeadamente médicos, na sequência do período de especialização;  
- Avaliar a possibilidade de introdução de um quadro de compensações, pelo investimento público do país na sua formação, por parte de médicos que pretendam emigrar ou ingressar no setor privado.

---

[Documento 29] Partido: Bloco de Esquerda | Tópicos: saude
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 2 Saúde > 2.3 Objetivo: reconstruir o SNS > Exames na hora certa, dentro do SNS
#### Exames na hora certa, dentro do SNS  
Porque muitos exames não são realizados no SNS, o utente tem de passar por procedimentos mais morosos e desgastantes. É possível tornar este processo mais rápido e simples.  
- → Aproveitamento da capacidade hospitalar instalada e integração de respostas entre centros de saúde e hospitais, para realização dos exames prescritos pelo médico de família no próprio dia ou num prazo muito curto;
- → Equipar os centros de saúde com os recursos necessários para a colheita de amostras biológicas e com meios complementares de diagnóstico, nomeadamente raio X e eletrocardiograma;
- → Criação de uma rede pública de Centros de Diagnóstico e Terapêutica;
- → Contratação de técnicos superiores de diagnóstico e terapêutica para os cuidados hospitalares, centros de saúde e Centros de Diagnóstico.  
A situação da medicina dentária e da psicologia em Portugal mostra como a saúde não pode ser deixada ao mercado. Se queremos que ela seja mesmo um direito ela deve ser pública, universal e gratuita. Ou seja, integrada no SNS.  
Apesar de, em Portugal, existir um médico dentista por 846 habitantes (um rácio bem acima dos 1500-2000 recomendados pela OMS) o acesso a cuidados de saúde oral continua a ser difícil. Para muitas pessoas é mesmo impossível. Segundo o Barómetro da Saúde Oral 2022, 20% da população só vai ao dentista em situação de urgência e 5% nunca foi. Esta percentagem sobe muito se olharmos para os estratos com menores rendimentos (13% dizem nunca ter ido ao dentista). Das pessoas que disseram nunca ir ao dentista ou ir menos de 1 vez por ano, 29,5% disseram não o fazer por falta de dinheiro.  
A situação da psicologia não é muito diferente. Existem cerca de 25 mil psicólogos em Portugal, um para 400 habitantes. No entanto, a maior parte das pessoas não consegue aceder a cuidados psicológicos porque eles escasseiam no SNS e fora do SNS são uma despesa impossível de suportar. Enquanto isso, somos dos países com maior percentagem de problemas de saúde mental e que mais psicofármacos consome, em média.  
Quando o mercado está ao comando, podem existir os profissionais para garantir uma cobertura universal, mas a população não acede a esses cuidados de saúde.  
- Contratar médicos dentistas em número suficiente para garantir, nos centros de saúde, um médico dentista por 25 mil habitantes e, no caso de concelhos mais pequenos ou de territórios de baixa densidade populacional, um médico dentista para populações entre 10 mil e 25 mil habitantes;
- Criar a carreira de médico dentista no Serviço Nacional de Saúde;
- Contratar psicólogos em número suficiente para garantir, nos centros de saúde, um psicólogo por 5 mil habitantes e colocar todos os psicólogos no SNS na carreira de Técnico Superior de Saúde ou outra que lhe venha a suceder.
- Contratar profissionais para colocar em funcionamento uma equipa comunitária de saúde mental por cada 50 a 100 mil habitantes;
- Contratar nutricionistas em número suficiente para garantir, nos centros de saúde, o rácio mínimo de um nutricionista por 12 mil habitantes, possibilitando assim o acesso a consultas de nutrição a utentes com diabetes, hipertensão e outros quadros clínicos que beneficiem de planos nutricionais próprios.

---

[Documento 30] Partido: Bloco de Esquerda | Tópicos: saude, trabalho
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 2 Saúde > 2.4 Só é possível mais SNS se cuidarmos dos seus profissionais
### 2.4 Só é possível mais SNS se cuidarmos dos seus profissionais  
A crise que o SNS vive hoje tem as suas raízes nas condições de trabalho dos profissionais, que o Governo do PS se recusou a transformar, valorizar e proteger. No SNS aufere-se salários baixos, quando comparados com outros países, e trabalha-se horas extraordinárias que ultrapassam em muito o limite legal.  
GRÁFICO 14  
**Remuneração das e dos enfermeiros em Portugal**  
Fonte: Health at a Glance 2023  
Rácio do salário médio em cada país, 2021  
Paridade do Poder de Compra (PPC) em dólares (USD), milhares  
GRÁFICO 15  
**Remuneração das e dos médicos em Portugal**  
Rácio do salário médio em cada país, 2021 Fonte: Health at a Glance 2023  
Turquia Inglaterra (RU)  
As propostas do PS não resolvem o problema. Aos médicos são propostas mais horas extraordinárias, e para os enfermeiros insiste-se numa carreira com salários líquidos perto de 1000 euros. Os farmacêuticos perdem poder de compra há vinte anos, mas não conseguem uma reunião com  
2.2  
1.8  
3.4  
3.3  
o Governo. Os poucos médicos dentistas no SNS passam anos a recibos verdes. Os técnicos auxiliares de saúde e os técnicos de emergência pré- -hospitalar continuam a ganhar um salário próximo do mínimo. Os técnicos superiores de diagnóstico e terapêutica continuam à espera que o governo cumpra a lei e aplique as alterações de carreira que o Parlamento aprovou; muitos psicólogos permanecem sem carreira própria e a ganhar menos 400 euros do que deveriam.  
Não surpreende, por isso, que cada vez mais profissionais ponderem sair do SNS, ou que os concursos fiquem desertos, como aconteceu com o de dezembro de 2023, a que se apresentaram apenas 143 profissionais para 900 vagas para médicos de família.  
É tempo de ouvir os profissionais e melhorar as condições de trabalho e de vida de quem faz o Serviço Nacional de Saúde.  
**Exclusividade a sério**: O governo fala de 'dedicação plena', mas é apenas propaganda para maquilhar um regime em que os médicos do SNS trabalhem mais horas extraordinárias em troca de mais alguma remuneração. Portanto, nada do que é necessário. Um verdadeiro regime de exclusividade tem de ser aplicável a todos os trabalhadores, com majoração de 40% do salário e com outros incentivos associados.  
**Revisão de todas as carreiras e posições remuneratórias**: Todas as carreiras da saúde devem ser revistas no prazo de um ano, de forma a aumentar todos os salários em pelo menos três posições remuneratórias, num valor mínimo de 150 euros; instituição de progressões automáticas, sem quotas e sem concursos, e reposição de todos os pontos sonegados aos trabalhadores do SNS.  
**Estatuto de risco e penosidade** com medidas como suplemento remuneratório, mecanismos para uma mais rápida progressão de carreira, majoração de dias de descanso por anos de trabalho, redução da carga horária semanal por anos de trabalho e a antecipação da idade de reforma sem penalização. Diversificação e formalização de atividades dos profissionais do SNS, através da criação dos estatutos de profissional- -doutorando, investigador e docente com tempo dedicado a estas atividades.  
**Registo nacional de profissionais de saúde**, por setor e instituição, que permita mapear necessidades de formação (inicial e de aperfeiçoamento ou especialização) e de contratação de recursos humanos, para a definição de um quadro de investimento plurianual baseado nas necessidades reais do SNS e do país.

---

[Documento 31] Partido: Partido Comunista Português | Tópicos: saude, trabalho, habitacao
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 4 ELEVAR A QUALIDADE DE VIDA. INVESTIR NOS SERVIÇOS PÚBLICOS, CUMPRIR AS FUNÇÕES SOCIAIS DO ESTADO > 4.1. A defesa do Serviço Nacional de Saúde e uma política de saúde ao serviço dos portugueses > 4.1.1 Valorizar o trabalho e os trabalhadores da saúde
##### 4.1.1 Valorizar o trabalho e os trabalhadores da saúde  
- Fixar e aumentar o número dos profissionais de saúde no SNS, valorizando as suas carreiras, aumentando as remunerações base e promovendo a opção de dedicação exclusiva para os médicos e enfermeiros – com a majoração de 50% da sua remuneração base e o acréscimo de 25% na contagem do tempo de serviço –, podendo ser alargada a outros profissionais de saúde em carência no SNS;
- Incentivar a fixação de profissionais em zonas carenciadas através de um regime específico de reforma antecipada, assim como da atribuição de um apoio para as despesas com a habitação.

---

[Documento 32] Partido: Iniciativa Liberal | Tópicos: saude, economia
  Secção: PROGRAMA ELEITORAL > B. PORTUGAL A FUNCIONAR > 2. MAIS ACESSO À SAÚDE > 2.1. Mudar o Sistema de Saúde em Portugal > Recuperar as Parcerias Público-Privadas (PPP)
##### Recuperar as Parcerias Público-Privadas (PPP)  
Para a Iniciativa Liberal o Estado não tem de ser dono de todas as entidades que prestem serviços públicos. O papel do Estado é definir prioridades – financeiras e de políticas públicas – para conseguir garantir o acesso a maior qualidade de serviço ao mais baixo custo para os contribuintes, assim como tem de saber negociar, com firmeza e transparência, em defesa do interesse das pessoas e não de si próprio. Neste sentido, as Parcerias Público Privadas (PPP) são um poderoso instrumento de melhoria dos serviços públicos.  
Nos últimos 20 anos, vários hospitais foram geridos em regime de PPP, com elevados índices de satisfação dos utentes, que não diferenciam, na sua utilização, uma gestão privada de uma gestão pública, sendo que as entidades fiscalizadoras evidenciam que as PPP estavam (e estão, a única que existe) plenamente integradas no Serviço Nacional de Saúde. Não há, assim, alguma justificação possível para que não se retome e, inclusivamente, amplie, este modelo de gestão.  
Neste sentido, a Iniciativa Liberal defende que sejam efetuados os estudos necessários, e legalmente exigidos, com vista à fundamentação da necessidade de contratualização da gestão dos hospitais do SNS em regime de PPP e que, em função dos respetivos resultados, sejam tomadas todas as medidas necessárias para a celebração de contratos de parceria nos hospitais relativamente aos quais fique demonstrado que o modelo de gestão em regime de PPP será o mais vantajoso.

</details>

## item-10

**Question:** Qual é a posição do PAN sobre as touradas?

**Answer:**

A posição do **PAN** relativamente às touradas é a seguinte:

• Defende a **proibição total das touradas** em todo o território nacional.
• Argumenta que estas práticas constituem uma forma de **crueldade e maus-tratos contra os animais**.
• Propõe a substituição de espetáculos baseados no sofrimento animal por alternativas que promovam o **bem-estar animal** e a cultura sem violência.

**Reference answer:**

O PAN compromete-se a abolir a tourada e os espetáculos tauromáquicos em Portugal, que considera um erro civilizacional. Enquanto tal não acontecer, propõe eliminar todos os apoios públicos a estas atividades, retirá-las da lista do Património Cultural Imaterial, criar um fundo para reconverter as praças de touros em espaços de lazer ou cultura até ao final de 2025 e revogar a isenção de IVA nos serviços de artistas tauromáquicos.

**faithfulness** — Is the claim supported by the CONTEXT?

- [ ] O PAN defende a proibição total das touradas em todo o território nacional.
- [ ] O PAN argumenta que as touradas constituem uma forma de crueldade e maus-tratos contra os animais.
- [ ] O PAN propõe a substituição de espetáculos baseados no sofrimento animal por alternativas que promovam o bem-estar animal e a cultura sem violência.

**correctness_recall** — Does the ANSWER state this reference claim?

- [ ] O PAN compromete-se a abolir a tourada em Portugal.
- [ ] O PAN compromete-se a abolir os espetáculos tauromáquicos em Portugal.
- [ ] O PAN considera a tourada um erro civilizacional.
- [ ] O PAN propõe eliminar todos os apoios públicos às atividades tauromáquicas até à abolição da tourada.
- [ ] O PAN propõe retirar as atividades tauromáquicas da lista do Património Cultural Imaterial.
- [ ] O PAN propõe criar um fundo para reconverter as praças de touros em espaços de lazer ou cultura até ao final de 2025.
- [ ] O PAN propõe revogar a isenção de IVA nos serviços de artistas tauromáquicos.

relevance: 

<details><summary>Context the generator read</summary>

[Documento 1] Partido: Pessoas-Animais-Natureza | Tópicos: outros, ambiente
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por uma efetiva proteção de todos os animais, reconhecimento dos seus direitos e garantia do seu bem-estar
## Por uma efetiva proteção de todos os animais, reconhecimento dos seus direitos e garantia do seu bem-estar  
O PAN, como único partido verdadeiramente animalista no espectro político português, tem trabalhado ao longo dos anos no sentido de garantir mais proteção, bem- -estar animal e o reconhecimento dos direitos daqueles que habitam neste planeta, a nossa casa comum.  
Na última legislatura, apesar de curta, assinalamos importantes vitórias para a causa animal, com a aprovação de várias medidas para proteger os animais e trazer um alívio na fatura das famílias que os acolhem e deles cuidam.  
O PAN tem proposto apoios significativos do Estado às associações de proteção animal, na medida em que são as associações que mais têm respondido aos deveres do Estado e devem, por tal, ser devidamente apoiadas por cada animal que resgatem.  
Uma das grandes conquistas foi a isenção do IVA na compra de produtos para alimentação de animais de companhia quando detidos por associações de proteção animal. Esta é uma medida da maior importância pois permite ajudar a baixar os encargos mensais que as associações enfrentam mensalmente com os animais que têm a seu cargo e cujo valor tem vindo a aumentar  
por força da inflação. Uma medida mais que justa para as associações de proteção animal, que passam agora a beneficiar da isenção de IVA quando compram alimentação para animais de companhia, além de beneficiar igualmente as famílias carenciadas detentoras de animais de companhia, que muitas vezes recorrem às associações de proteção animal em auxílio à aquisição de alimentação para os seus animais.  
Para o PAN, o abandono de animais de companhia constitui um problema social que exige medidas concretas, abrangentes, transversais e multissetoriais para ser combatido de forma eficaz. A fim de promover a adoção responsável, prevenir o abandono e garantir o bem-estar dos animais, é fundamental que se promova e implemente um amplo conjunto de medidas de apoio social, quer às famílias em situação de vulnerabilidade socioeconómica quer às associações de proteção animal, mas também garantir a fiscalização e controlo mais eficaz da compra e venda de animais de companhia e matilheiros, assim como a implementação de medidas mais restritivas que coloquem o bem-estar animal acima dos interesses económicos inerentes a estas atividades.  
O aumento do número de animais de companhia registados no Sistema de Informação de Animais de Companhia (SIAC), que conta atualmente com cerca de 2,75 milhões de registos, estimando-se, no entanto, que existem mais de 5 milhões de animais de companhia em Portugal, demonstra a importância que os animais têm na nossa sociedade e no seio familiar. Os animais de  
companhia são, muitas vezes, a única fonte de companhia e de afeto de pessoas em situação de vulnerabilidade social ou isolamento.  
O agravamento das despesas associadas à alimentação, para além dos encargos com os cuidados médico-veterinários dos animais, que continuam a ser taxados como um "bem de luxo", à taxa máxima de 23%, não obstante as propostas apresentadas pelo PAN que têm sido rejeitadas pelo Governo, tem consequências para além do aumento do custo de vida dos detentores. Conforme têm alertado várias associações de proteção animal, há detentores que acabam por abandonar os animais, pela impossibilidade em assegurar a alimentação ou demais cuidados de que os animais carecem ou, então, por recorrer a associações de proteção animal, sobrelotadas, para os ajudar.  
Para o PAN, alimentar e tratar de um animal deve ser encarado como uma decisão ética e adequada aos valores do século XXI, pelo que a redução da taxa do IVA permitiria alimentação e serviços médico-veterinários mais acessíveis, assim como a dedução das respetivas despesas em sede de IRS e, claro está, a efetivação da rede pública de serviços médico-veterinários para garantir que as pessoas não abandonam os seus animais por insuficiência de meios para os tratar.  
Lembramos que foi por proposta do PAN que foram implementadas medidas fiscais importantes como é o caso da isenção de pagamento da taxa referente ao registo e licenciamento de animais adotados, seja nos  
CROA ou nas associações de proteção animal. No entanto, consideramos, por maioria de razão, que deveria estar previsto um agravamento ou uma sobretaxa para a compra e venda de animais, de forma a incentivar a adoção e dissuadir a compra.  
O número de animais adotados representa apenas uma pequena parte dos animais recolhidos, o que resulta numa sobrelotação nos centros de recolha oficiais e nas associações de proteção animal. Além disso, muitos animais abandonados são forçados a sobreviver nas ruas, sujeitos a maus-tratos, fome e diversas carências, o que representa uma ameaça grave à sua vida e integridade física, agravado pela impossibilidade de implementação do programa CED (Capturar-Esterilizar-Devolver) em cães.  
É por isso que o PAN continuará a propor o alargamento da aplicação da metodologia CED aos cães errantes como forma de controlo da reprodução, à semelhança do que já sucede com eficácia em gatos de colónias, enquanto permanecem nas ruas pela ausência de outras soluções, sejam de recolha pelos CRO ou em parques de matilhas.  
A implementação de programas de esterilização gratuitos ou de custo reduzido para todos os animais é essencial e por isso o PAN continuará a insistir na promoção de campanhas nacionais de esterilização permanentes, em todo o país, a par da promoção de campanhas de educação, formação e sensibilização permanente junto dos detentores de animais.  
Para o PAN, a garantia do bem-estar dos animais e dos seus detentores tem de imperar e, por tal, tem de ser promovida uma rede nacional de apoio aos cuidados médico-veterinários, através das faculdades de medicina veterinária, em particular das Universidades Públicas, de protocolos com as associações que detêm hospitais ou clínicas veterinárias, cheque veterinário ou outras iniciativas que garantam a capacidade de acesso das famílias mais vulneráveis aos cuidados médico-veterinários dos animais que detêm.  
Um país assente em valores morais e éticos e que assiste a uma evolução civilizacional na forma como nos relacionamos com os outros seres vivos, não pode continuar refém dos lobbies da tauromaquia ou da caça.  
É por isso que nos comprometemos a continuar empenhados em abolir a tourada e os espectáculos tauromáquicos em Portugal, corrigindo assim um erro civilizacional em nome de uma suposta tradição, cultura e entretenimento, pondo fim à manifestação da violência associada a estes eventos.  
Com relação à caça, é inadmissível que se continue a investir milhões de euros de fundos públicos numa atividade que extermina milhões de animais e causa sérios danos à biodiversidade. Continuaremos a defender a revisão da regulamentação desta atividade e a abolição de métodos de caça cruéis como a caça à paulada ou o recurso a matilhas de cães.  
Por outro lado, não podemos continuar a ignorar os mi-  
lhões de animais que são transportados vivos. No total, e em todo o mundo, são quase dois mil milhões os animais que passam por jornadas de dias, ou mesmo semanas, transportados por via terrestre e marítima em condições deploráveis, sem água ou comida suficientes, mantidos em locais exíguos e conspurcados. A sujeição de animais a longas horas de transporte, em particular por via marítima e para países terceiros, levanta sérias implicações, não apenas éticas, mas também ambientais e de saúde pública que o PAN tem vindo sistematicamente a contestar, pelo que continuaremos empenhados em fazer avanços na defesa dos animais transportados por via terreste e aérea, pondo fim ao transporte marítimo.  
Continuaremos igualmente a impulsionar a transição para métodos alternativos ao uso de animais na investigação científica, garantindo um forte investimento nessa área.  
Além disso, é crucial que a abordagem em relação aos animais seja desprovida de qualquer visão utilitarista ou sanitarista. Os animais devem ser reconhecidos como seres sencientes e com valor intrínseco.  
E por isso é que o PAN vai continuar a lutar por uma revisão constitucional que garanta, alargue e reconheça mais proteção a todos os animais.  
Paralelamente, o PAN, vai pugnar para que a tutela penal seja revista por forma a alargar a proteção a outros animais que não apenas os animais de companhia, compromisso que assumimos em nome de um país mais  
ético e responsável no que respeita à proteção animal.  
Assim, neste contexto, o PAN propõe:  
- Criar o Ministério do Ambiente, Proteção Animal e Biodiversidade;  
- Criar uma Secretaria de Estado responsável pelo Bem-estar, Saúde e Proteção Animal no âmbito da orgânica do Governo;  
- Criar a Direção-geral de Proteção e Bem-estar Animal, revogando a passagem de competências do ICNF para as CCDRS;  
- Proceder à revisão da da República Portuguesa com vista a incluir a proteção animal, a consagrar como dever do Estado a defesa do bem-estar animal e a reconhecer o direito dos animais a um tratamento condigno e livre de sofrimento;

---

[Documento 2] Partido: Pessoas-Animais-Natureza | Tópicos: ambiente, cultura
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por uma efetiva proteção de todos os animais, reconhecimento dos seus direitos e garantia do seu bem-estar
- Facilitar a obtenção do estatuto de utilidade pública pelas associações ou fundações que tenham por missão a proteção animal;  
- Prever a possibilidade de circular em viatura com sinalização de emergência sempre que se transporte um animal ferido e em risco de vida;  
- Assegurar uma adequada fiscalização e mecanismos de controlo da circulação de animais de companhia dentro e fora do espaço da União Europeia, com vista a reforçar a sua proteção e a combater o tráfico de animais de companhia;  
- Promover, junto do Conselho Europeu, a criação de uma base de dados única que integre as bases de dados de todos os Estados-membros relativamente à identificação eletrónica dos animais de companhia, assegurando assim um maior controlo e fiscalização (\***tracing**\*) da sua circulação no espaço europeu ou para países terceiros;  
- Rever a legislação aplicável às condições de alojamento dos animais detidos para fins de pecuária, com vista ao reforço das condições de bem-estar animal e adaptação das infraestruturas para que seja obrigatória a permanência dos vitelos junto das progenitoras durante os primeiros dois meses de vida (atualmente é possível a separação nas primeiras 24h de vida) e zelando para que os vitelos sejam amamentados pelas progenitoras, proibindo a colocação de arganéis ou quaisquer outros artefactos que impeçam a amamentação;  
- Terminar com as exceções à obrigatoriedade de registo e declaração de animais, mesmo que para autoconsumo, com vista a um maior controlo da sanidade animal e do seu bem-estar;  
- Regulamentar os processos de reprodução forçada (inseminação artificial), aumentando o período de repouso das fêmeas reprodutoras entre gestações;  
- Rever o regime contraordenacional aplicável aos animais utilizados para fins de pecuária, nomeadamente, atualizando os montantes das coimas aplicáveis e as sanções acessórias previstas, passando a prever a possibilidade de ser declarada a perda dos animais;  
- Proibir a mutilação de leitões, como o corte de cauda, a castração ou o arranque de dentes sem anestesia;  
- Abolir o uso de celas de gestação para suínos reprodutores e garantir o reforço do seu bem-estar através das infraestruturas existentes, sem comprometer a segurança e a mortalidade dos leitões e garantindo o acesso a espaços exteriores para que possam ter liberdade de movimentos;  
- Garantir a obrigatoriedade da existência de sombra e a proteção contra as intempéries nos pastos extensivos, para além das demais condições que devem ser asseguradas aos animais;  
- Abolir o abate sacrificial de animais, sem recurso a prévia dessensibilização;  
- Erradicar a alimentação forçada de animais (\***gavage**\*) para produção de** \*foie gras**\*;  
- Promover uma maior transparência e adequação da informação dos produtos alimentares que chega até aos consumidores, designadamente em matéria de bem-estar animal;  
- Implementar auditorias a todas as explorações pecuárias existentes no país, avaliando o cumprimento das normas ambientais e de bem-estar animal e de saúde pública, bem como promover inspeções aleatórias nestas explorações;  
- Abolir os espetáculos tauromáquicos e, enquanto tal não for assegurado, eliminar todos os apoios públicos, diretos ou indiretos, a tais espetáculos ou a atividades tauromáquicas;  
- Retirar da lista do Património Cultural Imaterial todas as atividades e espetáculos associados à tauromaquia, ou quaisquer outras associadas ao sofrimento e morte de animais;  
- Garantir um fundo para a reconversão de todas as praças de touros em espaços de lazer e/ou cultura, que não envolvam atividades lesivas do bem-estar animal, até ao final de 2025;  
- Abolir a utilização de animais em eventos e atividades para entretenimento humano, nomeadamente, circos, corridas de cavalos e de cães e carrosséis de animais;  
- Executar programas de reconversão dos atuais parques zoológicos, delfinários e oceanários, em centros de conservação, recuperação e observação das espécies, sem a componente lúdica, promovendo a reconversão digital em espaços virtuais de sensibilização ou em santuários;  
- Promover a instalação de pombais contracetivos, abolir os métodos de captura convencionais e o extermínio desta população de aves, bem como determinar a anilhagem dos pombos existentes nos pombais contracetivos e a existência de registos devidamente comunicados pelas autarquias locais à DGAV;  
- Reconverter as atividades que recorram ao uso da tração animal como força de trabalho ou passeio turístico que, entre outras medidas, prevejam a substituição dos animais por veículos sustentáveis e o encaminhamento dos animais para santuários, sempre que os seus detentores não consigam mantê-los com dignidade a seu cargo;  
- Criar um regime jurídico aplicável aos santuários destinados a acolher animais selvagens cuja recuperação não lhes permita a devolução ao seu habitat natural;  
- Abolir o transporte marítimo de animais vivos até 2025, promovendo um programa reconversão, com vista ao transporte de animais não vivos;

---

[Documento 3] Partido: Pessoas-Animais-Natureza | Tópicos: politica_externa, ambiente, imigracao
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por uma política externa promotora da paz, dos direitos humanos e dos valores democráticos e empenhada na acção climática
## Por uma política externa promotora da paz, dos direitos humanos e dos valores democráticos e empenhada na acção climática  
A invasão da Ucrânia pela Rússia de Putin iniciada há quase 2 anos e o agudizar do conflito israelo-palestiniano verificado a partir de 2023, relembraram ao mundo, em pleno século XXI, os horrores da guerra, deram origem a violações de direitos humanos sem precedentes e colocaram enormes desafios à política externa do nosso país e da União Europeia.  
Estes desafios vêm juntar-se a outros que não só não desapareceram como se agravaram, como é o caso da crise climática, da crise dos refugiados ou da existência de uma União Europeia que continua a ceder às chantagens de Governos de extrema-direita populista e antidemocrática.  
PAN, como partido defensor do princípio da não violência, do projeto europeu e do multilateralismo, entende que no próximo ciclo político a chave para todos estes desafios passa por uma política externa promotora da paz, dos direitos humanos e da democracia e empenhada na ação climática. É ainda imperioso que Portugal impulsione uma reflexão sobre a transformação do Projeto Europeu em termos que assegurem um reforço  
das suas fundações em alicerces, como o Pilar Social e Ambiental, uma intransigência na defesa dos valores do Estado de Direito Democrático e um distanciamento de uma visão antropocêntrica no que respeita à vida animal e aos direitos da natureza.  
Neste contexto, o PAN propõe:  
- Criar o estatuto do/a refugiado/a climático/a;  
- Assegurar que Portugal prossegue e reforça o esforço de apoio logístico e financeiro à Ucrânia destinado ao combate à Rússia e à reconstrução do país;  
- Garantir a realização de uma avaliação internacional independente dos danos ambientais causados pela invasão russa da Ucrânia, que faça o levantamento das medidas de mitigação, reparação e restauro necessárias e assegurar a participação de Portugal no financiamento e operacionalização de tais medidas;  
- Garantir que Portugal assegura o total apoio à investigação iniciada pelo Procurador do Tribunal Penal Internacional sobre os alegados crimes de guerra cometidos em Israel, em Gaza e na Cisjordânia, e aos trabalhos levados a cabo pela Comissão Independente de Inquérito das Nações Unidas sobre os Territórios Palestinianos Ocupados;  
- Reconhecer, em estreita articulação com parceiros próximos no âmbito da União Europeia e em conformidade com o Plano de Partilha das Nações Unidas de 1947, o Estado da Palestina, viável e sustentável, na base de uma repartição de território justa e mutuamente aceite, de forma a garantir que possa viver lado a lado com o Estado de Israel, reconhecido e em paz e segurança, excluindo qualquer organização terrorista como representante do povo palestiniano;  
- Implementação de programas de acolhimento e apoio a estudantes, investigadores e docentes refugiados, em risco ou forçados à deslocação, tal como o PAN conseguiu aprovar na sequência da tomada dos talibãs do poder no Afeganistão em 2022 ou do agravamento do conflito israelo-palestiniano em 2023;  
- Defender no âmbito da União Europeia, a criação de um regime especial que facilite a viagem, concessão de estatuto de refugiado e integração nas instituições de ensino da União Europeia de estudantes, investigadores e docentes refugiados, em risco ou forçados à deslocação;  
- Garantir a celebração de acordos sobre conversão de dívida em financiamento climático, em especial com os países da CPLP e pugnar pela adoção generalizada desta metodologia no âmbito da União Europeia;  
- Assegurar uma Intervenção mais ativa e transparente no processo legislativo de Portugal na União Europeia, com publicação obrigatória da posição negocial do Governo nos processos legislativos no Conselho Europeu, com consultas a partes interessadas, informação à Assembleia da República e avaliação da pegada legislativa;  
- Defender a conclusão da criação de uma União Bancária Europeia;  
- Rever o projeto do salário mínimo europeu, estabelecendo valores mais ambiciosos de acordo com a Agenda 2030;  
- Defender a transformação da Política Agrícola Comum numa Política Alimentar Comum, assumindo a sustentabilidade e promoção de dietas saudáveis como objetivos prioritários;  
- Pugnar pelo fim dos paraísos fiscais dentro da UE e reforçar a fiscalização destes espaços fora da Europa quando transacionam com o Espaço Económico Europeu;  
- Pugnar no quadro da União Europeia pela adoção de critérios mais exigentes no âmbito da lista da União Europeia de jurisdições não cooperantes;

---

[Documento 4] Partido: Pessoas-Animais-Natureza | Tópicos: justica, imigracao, saude
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por um país onde cabem tod@s e com mais ambição na defesa dos direitos humanos
- Garantir a prestação de consultas de psicologia gratuitas para a vítima e para os/as filhos/as, sejam eles menores ou não, desde que tenham presenciado de alguma forma a prática dos crimes;  
- Assegurar a transparência das sentenças dos tribunais de 1.ª instância, em linha com o recomendado pelo GRECO e permitindo um maior escrutínio dos tribunais de primeira instância pela sociedade civil;  
- Prosseguir a incorporação da perspetiva de género nos orçamentos de Estado, com garantia de uma maior transparência sobre as ações a implementar nesse âmbito e de um aumento anual da verba alocada;  
- Adotar linguagem escrita e visual promotora da igualdade de género (não discriminatória em função do sexo/género) em todos os documentos oficiais;  
- Introduzir mecanismos de fiscalização que garantam uma participação plena e igualitária de mulheres e homens no mercado de trabalho e na atividade profissional, combatendo a desigualdade salarial;  
- Reforçar o combate à mutilação genital feminina, masculina e intersexo, excisão e outras práticas nocivas, promovendo nomeadamente cirurgias reconstrutivas gratuitas e apoio psicológico;  
- Alargar o projeto "Práticas Saudáveis: Fim à Mutilação Genital Feminina", desenvolvido na Administração Regional de Saúde de Lisboa e Vale do Tejo, I.P. (ARSL-VT), a todas as Administrações Regionais de Saúde do território nacional;  
- Apresentar publicamente os dados de Mutilação  
**Genital Feminina em Portugal e propostas para a redução e erradicação deste fenómeno em Portugal e nos países parceiros da Cooperação Portuguesa;**  
- Criar redes locais integradas de combate e prevenção da Mutilação Genital Feminina e da Mutilação Genital Masculina, envolvendo líderes e mediadores das comunidades que as praticam, desenvolvendo iniciativas públicas em estreita articulação com as ONG e restantes entidades da sociedade civil;  
- Realizar estudos sobre Mutilação Genital Masculina e a Mutilação Genital Intersexo, em Portugal, em parceria com a academia e associações que trabalhem estas matérias;  
- Garantir a proibição da Mutilação Genital Intersexo e Masculina;  
- Garantir respostas de acompanhamento médico, psicológico e social especializado a todas as pessoas que tenham sido sujeitas a mutilação genital feminina, masculina ou intersexo ou estejam eventualmente em risco de o ser;  
- Criar uma rede de profissionais especializados, nomeadamente intérpretes e técnicos habilitados para o contacto e acompanhamento destas vítimas, para situações como diligências judiciais;  
- Garantir procedimentos eficazes e céleres de referenciação e encaminhamento das vítimas de Mutilação Genital Feminina/Corte, Mutilação Genital Masculina e Mutilação Genital Intersexo para os diversos serviços de apoio existentes;  
- Melhorar os esforços para, de forma proativa, identificar vítimas de tráfico de seres humanos no país, crianças e vítimas de tráfico sexual, através de formação das entidades policiais, inspetores laborais e dos tribunais;  
- Implementar uma rede transdisciplinar dedicada à Memória dos Movimentos Migratórios;  
- Apoiar as organizações não governamentais e associações que atuam na área de implementação de programas de saída do sistema da prostituição;  
- Desenvolver e implementar programas de saída do sistema da prostituição, em conjunto com entidades governamentais, autarquias locais, ONG e associações, com as seguintes componentes: acompanhamento na saúde, designadamente cuidados médicos, saúde sexual e reprodutiva, acompanhamento psicológico, tratamento de adições, saúde mental, emprego apoiado, entre outros; e  
- Elaborar um estudo para compreender a organização do sistema da prostituição, motivações e as necessidades, as vulnerabilidades e as condicionantes.  
Em defesa do direito das crianças e jovens, o PAN irá:  
- Criar um sistema de educação para a infância que garanta a inclusão das crianças dos 0 aos 3 anos no sistema educativo;  
- Criar, a partir de 1 de Setembro de 2024, um apoio extraordinário para a frequência de creches, destinado às crianças que não tenham tido acesso a vaga abrangida pelo programa da gratuitidade no setor social e solidário ou nas creches licenciadas da rede privada lucrativa;  
- Criar, até 2026, uma rede pública de creches em articulação com as autarquias locais e o sector social;  
- Criar o Observatório na Comissão Nacional de Promoção dos Direitos e Proteção das Crianças e Jovens para monitorização do cumprimento das obrigações impostas pela Convenção dos Direitos da Criança;  
- Criar o Provedor das Crianças e Jovens ou das Gerações Futuras (embora deva já agir nas gerações atuais), uma figura de proximidade, acessível e capaz de "escutar" as queixas das crianças e jovens, através de linguagens e meios adequados, zelando pelas suas necessidades e proteção junto de todas as organizações, públicas e privadas;  
- Desenvolver programas de sensibilização e de apoio ao exercício da parentalidade, prevenindo maus-tratos às crianças;

---

[Documento 5] Partido: Pessoas-Animais-Natureza | Tópicos: economia, ambiente, governacao
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por uma economia do bem-estar que dê prioridade às pessoas e à sustentabilidade ambiental
## Por uma economia do bem-estar que dê prioridade às pessoas e à sustentabilidade ambiental  
Para o PAN, é essencial ultrapassar a atual sociedade de consumo em ordem a uma sociedade da empatia, processo que dará acesso a uma plena democracia, social e económica, pautada pela Política do Bem Comum, cujo fim maior é garantir o futuro do planeta, combinando o desenvolvimento económico e social com a redução da pressão sobre o ambiente.  
Sabendo que o planeta Terra é um recurso limitado e ameaçado, o PAN defende que a Transição Climática e a Economia devem fundir-se num mesmo ministério, procurando equilibrar a regulação social da atividade económica e as respostas ao maior desafio de todos os tempos: as alterações climáticas.  
Um ministério da Transição Climática e da Economia visa proteger a produção económica da natureza, conectando os ciclos económicos e os ciclos naturais, propondo uma contribuição financeira em troca do trabalho invisível da natureza e integrando as produções da natureza no PIB. Presentemente, esse exercício só é praticável, por exemplo, através de atividades como cortar madeira, negociá-la, vender gado ou plantar soja, como se a natureza não tivesse valor em si mesma. Porém, a economia só será sustentável se for capaz de assegurar  
a manutenção do sistema terrestre, por isso, no futuro, a conservação da natureza tem de ser uma atividade económica.  
A urgência de novas métricas de progresso exige a superação do paradigma de desenvolvimento baseado exclusivamente no crescimento económico pelo paradigma do desenvolvimento social sustentável. Exige também o decrescimento das externalidades: a economia deverá intervir na mudança climática, desincentivando o seu crescimento à custa da vida planetária. Não se trata de reduzir o rendimento ou emprego, trata-se, sim, de superar uma economia extrativista e linear por uma economia circular baseada no consumo consciente, no comércio justo e numa banca pública de fomento, a Banca Ética e das Finanças Solidárias.  
Como corolário, o ministério da Transição Climática e da Economia deve pugnar pelo estabelecimento de um rendimento de dignidade e cidadania, capaz de promover a empatia económica, a justiça social e o bem-estar para empregados/as e desempregados/as.  
Com isto, o PAN irá:  
- Concentrar os apoios públicos ao investimento em projetos que:  
- Estejam direcionados para a descarbonização, a mitigação e adaptação às alterações climáticas  
- Acelerem a digitalização da economia, melhorando a produtividade, o ambiente, a coesão territorial e a conciliação da vida profissional e familiar;  
- Apoiar clara e fortemente a economia circular, seja através de incentivos ao investimento, seja através de legislação que contrarie a economia linear;  
- Definir como pilares de democracia económica a igualdade de género e a coesão territorial;  
- Criar um fundo nacional de transição justa que permita assegurar a reintegração profissional dos/ das trabalhadores/as afetados/as pela crise climática;  
- Apoiar a fixação de migrantes digitais nas áreas de baixa densidade populacional;  
- Subsidiar o desenvolvimento de alternativas proteicas de base vegetal na indústria alimentar e criar um plano de ação nacional e fundo para as proteínas vegetais e alternativas;  
- Criar um projeto-piloto de implementação de um Rendimento de Dignidade e Cidadania (RDC);  
Relativamente à fiscalidade para as famílias e as empresas, o PAN irá:  
- Defender o englobamento de todas as categorias de rendimento, fazendo jus ao preceito constitucional do "imposto único e progressivo, tendo em conta as necessidades e os rendimentos do agregado familiar", revendo, no entanto, as Deduções Específicas, nomeadamente as dos Rendimentos Prediais que passariam a incluir depreciações e encargos financeiros; temporariamente, manter- -se-iam taxas especiais apenas para os arrendamentos para habitação permanente;  
- Aprovar, no início da legislatura, um programa de emergência fiscal, que garanta:  
- A reposição do IVA Zero, com vigência até ao dia 30 de setembro;  
- Revisão dos limites dos escalões de IRS, atualizando-os para o valor que teriam se desde 2021 se considerasse a inflação realmente verificada;  
- Defender em todos os OE a atualização de todos os limites dos escalões do IRS pelo exato aumento da inflação do ano anterior;  
- Criar um regime especial de isenção contributiva aplicável aos jovens trabalhadores-estudantes que aufiram rendimentos anuais de trabalho não superiores a 14 remunerações mínimas mensais garantidas, sem comprometer o posterior deferimento de isenção contributiva de 12 meses à Segurança Social aquando do início do respetivo percurso profissional;  
- Alargar o regime do IRS Jovem por forma a que dure mais 2 anos e garanta uma redução de imposto de 15% no penúltimo (6.º) ano e de 5% no último (7.º) ano;  
- Alargar o acesso ao IRS Jovem a todos os jovens, mesmo que englobados num agregado familiar;  
- Atualizar a dedução específica da categoria A (trabalho dependente) e da categoria H (Pensões), fixada em 4104€ e inalterada desde 2015, para 4915€ em 2024 e pela taxa de inflação nos anos seguintes;

---

[Documento 6] Partido: Pessoas-Animais-Natureza | Tópicos: governacao, jovens
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por uma democracia renovada e que reconcilie as pessoas com as instituições
## Por uma democracia renovada e que reconcilie as pessoas com as instituições  
Nas últimas eleições legislativas, 5,2 milhões dos eleitores e eleitoras não exerceram o seu direito de voto, naquilo que se traduziu na maior taxa de abstenção da nossa democracia (48,58%), e mais de 670 mil votos não serviram para eleger nenhum deputado. Tudo isto é agravado pelo facto de, em 36% dos círculos eleitorais, apenas PS e PSD elegerem deputados, desde 1991.  
No ano em que se completa o 50.º aniversário da revolução de 25 de Abril de 1974, sabemos que 6 em cada 10 pessoas afirmam não confiar no Governo nem no Parlamento e que 4 em cada 10 jovens afirmam ter muito pouco ou nenhum interesse em política. Sabemos também que continuamos a ser um país excessivamente concentrado no litoral – já que cerca de metade da população residente no nosso país vive em apenas 31 municípios localizados nas áreas metropolitanas de Lisboa e Porto – e que, devido aos avanços tecnológicos, a opções empresariais duvidosas e a uma precariedade crónica dos jornalistas, temos assistido a ataques sem precedentes ao direito fundamental à liberdade de informação e à liberdade de imprensa.  
Para o PAN, é essencial assegurar uma democracia renovada, capaz de reconciliar as pessoas com as institui-  
ções, de proteger o pluralismo de informação, de assegurar um sistema eleitoral mais agregador e convidativo à participação, e de garantir uma participação que vá além do voto.  
Neste contexto, o PAN propõe:  
- Proceder à criação de uma assembleia de cidadãos/ãs, a funcionar junto da Assembleia da República, com vista ao aprofundamento da participação cidadã;  
- Consagrar o direito de voto aos 16 anos;  
- Criação de um círculo eleitoral de compensação e promover a revisão dos demais círculos existentes, por forma a impedir a injustiça subjacente ao atual sistema eleitoral, que a cada eleição legislativa faz com que cerca de meio milhão de votos válidos não sirvam para eleger qualquer deputado;  
- Alterar a legislação eleitoral por forma a facilitar o acesso ao voto antecipado e a aproximar os locais de voto das pessoas, com vista a combater a abstenção;  
- Introduzir melhorias ao processo eleitoral nos círculos da emigração no âmbito das eleições para a Assembleia da República, designadamente modernizando o voto postal dos eleitores residentes no estrangeiro e adequando-o às especificidades de cada país;  
- Alargar o direito de voto em mobilidade no âmbito das eleições para os órgãos das autarquias locais a todos/as os/as eleitores/as que se encontrem impedidos de se deslocar à assembleia de voto no dia da eleição;  
- Alterar a Lei do Financiamento dos Partidos Políticos e das Campanhas Eleitorais, de forma a assegurar a revogação das isenções de IMI, de impostos sobre o património e imposto automóvel atribuída aos partidos políticos;  
- Reduzir o número mínimo de assinaturas para a apreciação de uma petição no plenário da Assembleia da República das atuais 7500 assinaturas para 4000;  
- Reduzir para 15 mil o número mínimo de subscritores/as das Iniciativas Legislativas de Cidadãos/ãs e adotar um processo de submissão e subscrição mais simples;  
- Concretizar a expansão do programa Parlamento dos Jovens ao âmbito do Governo, por via da criação da figura dos conselhos de ministros dos jovens, e ao âmbito municipal, por via da criação das assembleias municipais jovens;  
- Empreender um debate alargado sobre a regionalização, que envolva a Administração Pública, a academia e a sociedade civil e proceder a uma revisão constitucional que elimine a pergunta de alcance regional e clarifique os termos do referendo de âmbito nacional;  
- Consagrar a eleição direta pelos/as cidadãos/ãs dos/das presidentes e vice-presidentes das CCDR e previsão de uma tutela de legalidade do poder estadual sobre a conduta das direções das CCDR, por forma a promover a democratização da governação territorial e uma efetiva independência das direções das CCDR face ao Governo;  
- Reforçar a legitimidade democrática das Áreas Metropolitanas e das Comunidades Intermunicipais, com a instituição de um novo modelo assente na eleição direta, por sufrágio universal, do órgão deliberativo e do/da Presidente do órgão executivo;  
- Reforçar o papel da Assembleia da República no processo de designação dos membros dos conselhos de administração das entidades reguladoras e do Banco de Portugal, dando um caráter vinculativo ao parecer da comissão competente para a audição e estabelecendo a audição obrigatória do Ministro do Governo responsável pela escolha do nome proposto;

---

[Documento 7] Partido: Pessoas-Animais-Natureza | Tópicos: habitacao, trabalho, saude
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por um país onde cabem tod@s e com mais ambição na defesa dos direitos humanos
Embora o número de crianças até aos 3 anos enquadradas em serviços de educação na primeira infância seja superior à média europeia, a taxa de cobertura das creches, face ao número da população-alvo, não chega a metade das crianças, e o programa das creches gratui-  
tas deixa de fora 4 em cada 10 crianças nascidas após 1 de setembro de 2021, o que revela o muito que está por fazer em matéria de direitos da criança e proteção na parentalidade.  
Foi, ainda, a falta de novos avanços que levou a que no ano passado Portugal caísse pelo segundo ano consecutivo no ranking dos países europeus sobre direitos das pessoas LGBTI+, ficando em 11.º lugar.  
Para o PAN, os direitos humanos estão interligados entre si e por isso defendemos que, com respeito pelos limites do nosso planeta, é possível contribuirmos, enquanto sociedade, para a melhoria das condições de vida de todas as pessoas e reduzir até erradicar as persistentes desigualdades, construindo um país onde cabem tod@s e que seja ambicioso na defesa dos direitos humanos.  
Neste contexto:  
Para combater a pobreza e exclusão social, o PAN irá:  
- Assegurar que todas as famílias cujo rendimento total mensal seja igual ou inferior ao valor do limiar da pobreza tenham acesso às tarifas sociais de energia, gás natural e** \*internet**\*;  
- Criar a figura de "Superação do Rendimento Social de Inserção", permitindo a sobreposição da atribuição da prestação em dinheiro, atualmente prevista no Rendimento Social de Inserção (RSI), com outros rendimentos mensais até ao valor do salário mínimo, incentivando a que os seus beneficiários que se encontram em situação de pobreza extrema entrem no mercado de trabalho sem temer perder, até maior estabilização, esta prestação social, e combatendo a precariedade de possíveis empregos das pessoas em situação mais vulnerável;  
- Garantir o aumento das prestações sociais, através do aumento do montante do Indexante de Apoios Sociais e da garantia de que as mesmas nunca têm um valor inferior ao limiar da pobreza;  
- Atribuir a todas as pessoas em situação de sem- -abrigo um gestor de caso e criar uma plataforma** _online_ **de gestores de caso, ligando as diversas entidades e associações;  
- Prioridade ao alojamento em** _Housing First_ **para pessoas em situação de sem-abrigo crónica, com morbilidades associadas, consumos de substâncias psicoativas, doenças de longa duração, doença mental, hepatite C, HIV, entre outras;  
- Garantia de gratuitidade do cartão do cidadão para as pessoas em situação de sem-abrigo;  
- Criar unidades residenciais de acolhimento com vagas de emergência, a funcionar 24h/dia;  
- Definir apoios a empresas e entidades que criem postos de trabalho visando a empregabilidade adaptada a pessoas em situação de grande vulnerabilidade, como as que se encontram em situação de sem-abrigo, com ou sem consumos de substâncias psicoativas lícitas e ilícitas, migrantes em exclusão social ou pessoas que se prostituem;  
- Reforçar os meios humanos e técnicos de combate ao Tráfico de Seres Humanos;  
- Atualizar o valor da comparticipação do Estado no tratamento e reabilitação de dependentes de substâncias psicoativas ou de álcool; e  
- Aprovar um plano nacional de combate aos comportamentos aditivos associados ao jogo, que inclua designadamente uma campanha nacional para a sensibilização para os riscos do jogo e das apostas, a elaboração de um estudo epidemiológico sobre a magnitude do jogo patológico associado às lotarias instantâneas e a elaboração de um código de conduta sobre a cobertura informativa de obtenção de ganhos em jogos e apostas.  
Para assegurar o reforço dos direitos das mulheres, assegurar a igualdade de género e combater a violência  
doméstica e sexual, o PAN irá:  
- Aumentar as quotas de género da composição das entidades administrativas independentes e entidades reguladoras de 33% para 40%;  
- Adotar quotas de género de 40% na composição do Tribunal Constitucional e do Conselho de Estado;  
- Estabelecer incentivos fiscais para empresas que tenham mais de 40% de pessoas de cada sexo nos seus órgãos de administração, fiscalização ou gerência;  
- Elaborar, em conjunto com o Ministério da Educação, um programa de educação para os afetos, desde o Pré-Escolar até ao Secundário, reconhecendo que a autonomia, a liberdade de escolha e uma informação adequada são aspetos essenciais para a estruturação de atitudes e comportamentos responsáveis, para a promoção da igualdade de género, para a recusa de relações pessoais de dominação e de exploração, e para o respeito pelo direito à diferença;  
- Criar, em todas as comarcas judiciais no território nacional, nos departamentos de investigação e ação penal, gabinetes de atendimento à vítima de violência doméstica;  
- Alargar o número de centros de crise para vítimas de violência sexual, assegurando a existência de pelo menos um centro em cada capital de distrito do país até 2026, e reforçar o respetivo financiamento;

</details>

## item-11

**Question:** Quem quer baixar o IRC e para quanto?

**Answer:**

Vários partidos propuseram a redução da taxa de IRC, com diferentes objetivos e escalas:

• **Aliança Democrática (AD)**: Propõe a redução progressiva da taxa de IRC para **15%** para as empresas que cumpram determinados critérios de investimento e criação de emprego.
• **Iniciativa Liberal (IL)**: Defende uma redução significativa e acelerada da taxa de IRC, com o objetivo de chegar aos **15%** para promover a competitividade das empresas portuguesas.
• **Chega**: Propõe a redução da taxa de IRC para **15%** para todas as empresas, argumentando que isto estimulará o investimento e o crescimento económico.
• **Partido Socialista (PS)**: Não apresenta uma proposta de redução generalizada da taxa de IRC nos moldes dos partidos de direita, focando-se mais em medidas de apoio direcionadas e incentivos fiscais específicos.
• **Bloco de Esquerda (BE)**: Opõe-se à redução da taxa de IRC, defendendo que a carga fiscal sobre as empresas deve ser utilizada para financiar o Estado Social e a redistribuição de riqueza.
• **Livre**: Mantém uma postura crítica à redução da taxa de IRC, priorizando o investimento público em serviços essenciais.
• **PCP**: Defende a manutenção ou o aumento da carga fiscal sobre os lucros das grandes empresas para garantir o financiamento de políticas públicas.

**Reference answer:**

A IL propõe uma taxa única de IRC de 12%, com 15% apenas para multinacionais com faturação anual superior a 750 milhões de euros, a revogação das derramas e o fim das tributações autónomas. A AD propõe reduzir o IRC de 21% para 15% ao ritmo de 2 pontos percentuais por ano até ao final da legislatura, eliminar gradualmente a progressividade da derrama estadual e eliminar a derrama municipal. O CHEGA propõe uma flat tax de IRC de 15% para as regiões autónomas e o interior e de 18% no resto do território, referindo noutra proposta a descida para 15% ao longo da legislatura com efeito imediato no interior, além de desagravar as derramas estadual e municipal e isentar progressivamente de IRC os jovens empresários até aos 35 anos. O PAN propõe reduzir a taxa em 1 ponto percentual por ano até 17% no final da legislatura. O PCP propõe uma taxa de 12,5% apenas para MPME (rendimento coletável até 15.000€), criando em simultâneo um escalão de derrama estadual de 14% para empresas com rendimento coletável superior a 50 milhões de euros. O PS não propõe baixar a taxa de IRC, mas reduzir em 20% as tributações autónomas sobre as viaturas das empresas. O BE e o LIVRE não propõem descer o IRC, defendendo antes agravamentos para as empresas com lucros mais elevados ou de determinados setores.

**faithfulness** — Is the claim supported by the CONTEXT?

- [ ] A Aliança Democrática propõe a redução progressiva da taxa de IRC para 15% para as empresas que cumpram determinados critérios de investimento e criação de emprego.
- [ ] A Iniciativa Liberal defende uma redução significativa e acelerada da taxa de IRC com o objetivo de chegar aos 15% para promover a competitividade das empresas portuguesas.
- [ ] O Chega propõe a redução da taxa de IRC para 15% para todas as empresas, argumentando que isto estimulará o investimento e o crescimento económico.
- [ ] O Partido Socialista não apresenta uma proposta de redução generalizada da taxa de IRC nos moldes dos partidos de direita.
- [ ] O Partido Socialista foca-se em medidas de apoio direcionadas e incentivos fiscais específicos em vez de uma redução generalizada da taxa de IRC.
- [ ] O Bloco de Esquerda opõe-se à redução da taxa de IRC.
- [ ] O Bloco de Esquerda defende que a carga fiscal sobre as empresas deve ser utilizada para financiar o Estado Social e a redistribuição de riqueza.
- [ ] O Livre mantém uma postura crítica à redução da taxa de IRC.
- [ ] O Livre prioriza o investimento público em serviços essenciais em detrimento da redução da taxa de IRC.
- [ ] O PCP defende a manutenção ou o aumento da carga fiscal sobre os lucros das grandes empresas para garantir o financiamento de políticas públicas.

**correctness_recall** — Does the ANSWER state this reference claim?

- [ ] A IL propõe uma taxa única de IRC de 12%.
- [ ] A IL propõe uma taxa de IRC de 15% para multinacionais com faturação anual superior a 750 milhões de euros.
- [ ] A IL propõe a revogação das derramas.
- [ ] A IL propõe o fim das tributações autónomas.
- [ ] A AD propõe reduzir o IRC de 21% para 15%.
- [ ] A AD propõe a redução do IRC ao ritmo de 2 pontos percentuais por ano até ao final da legislatura.
- [ ] A AD propõe eliminar gradualmente a progressividade da derrama estadual.
- [ ] A AD propõe eliminar a derrama municipal.
- [ ] O CHEGA propõe uma flat tax de IRC de 15% para as regiões autónomas e o interior.
- [ ] O CHEGA propõe uma flat tax de IRC de 18% no resto do território.
- [ ] O CHEGA propõe a descida do IRC para 15% ao longo da legislatura com efeito imediato no interior.
- [ ] O CHEGA propõe desagravar as derramas estadual e municipal.
- [ ] O CHEGA propõe isentar progressivamente de IRC os jovens empresários até aos 35 anos.
- [ ] O PAN propõe reduzir a taxa de IRC em 1 ponto percentual por ano.
- [ ] O PAN propõe atingir a taxa de 17% no final da legislatura.
- [ ] O PCP propõe uma taxa de IRC de 12,5% apenas para MPME com rendimento coletável até 15.000€.
- [ ] O PCP propõe criar um escalão de derrama estadual de 14% para empresas com rendimento coletável superior a 50 milhões de euros.
- [ ] O PS não propõe baixar a taxa de IRC.
- [ ] O PS propõe reduzir em 20% as tributações autónomas sobre as viaturas das empresas.
- [ ] O BE não propõe descer o IRC.
- [ ] O BE defende agravamentos para as empresas com lucros mais elevados ou de determinados setores.
- [ ] O LIVRE não propõe descer o IRC.
- [ ] O LIVRE defende agravamentos para as empresas com lucros mais elevados ou de determinados setores.

relevance: 

<details><summary>Context the generator read</summary>

## Aliança Democrática
[Documento 1]
  Secção: PROGRAMA ECONÓMICO DA ALIANÇA DEMOCRÁTICA > 1. Menos Impostos sobre as Famílias e sobre o Investimento > 1.1. REFORMA PARA BAIXAR A CARGA FISCAL EM IRS E IRC E DAR PREVISIBILIDADE E ESTABILIDADE FISCAL
**Adicionalmente, o sistema fiscal português apresenta uma complexidade e instabilidade extrema,** fruto de um processo de acumulação, ao longo dos anos, de camadas de ajustamentos, alterações e exceções. Por outro lado, existe uma teia de obrigações declarativas, cujo cumprimento requer um grande consumo de recursos materiais e humanos e que, em muitos casos, não serve sequer o propósito de estimular o cumprimento voluntário e de auxiliar a Autoridade Tributária e Aduaneira (AT), no cruzamento de informação e na sua ação inspetiva. De acordo com um estudo da Tax Foundation, em 2019, em Portugal, cada empresa necessitava, em média, de 63 horas para cumprir as suas obrigações fiscais (24ª posição em 26 países). Em Espanha, no mesmo período, eram necessárias, em média, 33 horas (12ª posição) e na Irlanda, apenas 12 horas para idêntico efeito (2ª posição).  
**O Sistema Fiscal português promove, assim, um enorme desperdício de recursos produtivos,** pela exacerbação dos custos de cumprimento, pelas oportunidades de erosão da base fiscal que proporciona, e por via dos enormes custos administrativos e de controlo que requer. Em conjunto com a desconsideração de princípios elementares de tributação, tal resulta em significativas distorções na afetação de recursos na economia, resultantes de alterações ineficientes nas decisões de trabalhar, de poupar, de investir e de expandir a atividade.  
**Fruto deste desempenho, o sistema fiscal português é, hoje, considerado o quarto pior em termos de competitividade** entre os estados-membros da OCDE no 2023 International Tax Competitiveness Index elaborado pela Tax Foundation. Entre os 38 países da OCDE, Portugal ocupa a 34ª posição na ordenação global, a 37ª e penúltima posição no ranking da tributação das empresas e a 29ª posição na tributação dos indivíduos.  
A Reforma Fiscal proposta pela AD pretende alterar este _status quo_ e, em consonância com o objetivo de gestão mais eficiente da despesa pública, tem como objetivos centrais: **(a) a redução gradual e sustentável da carga fiscal**, com prioridade para a redução do IRS e em especial para os jovens até aos 35 anos, e sobre o investimento/ poupança, e otimização (adicional) do Sistema Fiscal por via de uma reconfiguração que privilegie o alívio nos impostos mais distorcivos da atividade económica (b) **simplificação e redução dos custos de cumprimento das obrigações fiscais**, (c) **diminuição e racionalização da despesa fiscal** (benefícios fiscais), (d) **reforço da estabilidade e previsibilidade tributária** (e) **agilização da justiça tributária**, (f) **aperfeiçoamento da administração tributária** na sua organização e equilíbrio na relação com os contribuintes.  
- a. A **redução da carga fiscal é uma prioridade assumida, devendo ser implementada de modo gradual e sustentável.** O esforço de redução de impostos será **concentrado no IRS**, especialmente sobre o trabalho, pensões e poupança e **no IRC**, especialmente sobre o investimento. Além do efeito da redução fiscal na aceleração do crescimento económico (que, por um princípio de prudência, não deve ser sobrevalorizado), a sustentabilidade orçamental desta redução de impostos é reforçada pela racionalização dos benefícios fiscais dispersos, numa ótica de ampliação das bases tributárias. Assim, incluem-se nesta orientação as seguintes medidas:
- **Redução do IRS até ao 8.º escalão,** através da redução de taxas marginais entre 0,5 e até 3 pontos percentuais face a 2023, com maior enfoque na classe média;
- **Isenção de contribuições e impostos sobre prémios de desempenho** até ao limite equivalente a um vencimento mensal;
- **Adoção do IRS Jovem** de forma duradoura e estrutural, que implica uma redução de 2/3 nas taxas atualmente aplicáveis, com uma taxa máxima de apenas 15%, aplicadas a todos os jovens até aos 35 anos, com exceção do último escalão de rendimentos;
- Tornar obrigatória a **atualização dos escalões e das tabelas de retenção de IRS em linha com a inflação e com o crescimento da produtividade**, evitando os vários agravamentos de IRS encapotados realizados pelo Governo socialista nos últimos anos;
- **Aperfeiçoar, com realismo e justiça social, a progressividade e coerência do IRS**, designadamente através de:
- **Revisão dos limiares dos escalões de IRS** de forma a garantir que os mesmos se encontram adaptados à realidade da economia portuguesa;
- Introdução de uma **noção sintética e abrangente de rendimento** sujeito a IRS, que corrija as injustiças e sub-tributações resultantes da atual definição limitativa de rendimentos sujeitos a IRS, que permita um maior desagravamento das taxas marginais;
- Criação de um **imposto negativo para beneficiar as famílias de menores rendimentos**, consagrado num designado Suplemento Remunerativo Solidário (ver Reforma dos Apoios Sociais), em plena articulação com o mínimo de existência do IRS, e financiado pela consolidação nesta prestação da miríade de apoios sociais dispersos.
- **Criação de contas-poupança isenta de impostos**, adotando um regime em que certo nível de contribuições dos trabalhadores e das suas entidades empregadoras sejam livres de IRS, salvo se e quando forem distribuídas, pagas ou, de qualquer forma, apropriadas pelos respetivos titulares. Tal passa pela introdução de contas poupança com possibilidade de acesso a grande diversidade de instrumentos, com eventuais limites à entrada, inspirada no modelo de ISA _accounts_ no Reino Unido ou nas contas 401K nos Estados Unidos. As contribuições e reinvestimentos destes proveitos não são tributados, incluindo se forem utilizados para amortização de crédito à habitação que onere a casa de morada de família. Poderá ponderar-se tratamento semelhante aos rendimentos prediais e de capitais (aplicando-se, assim, o princípio de que, se reinvestidos, continuam a não ser tributados);
- **Redução das taxas de IRC**, começando com a redução gradual de 2 pontos percentuais por ano até aos 15% no final da Legislatura. Esta redução deverá acompanhar a transposição para a ordem jurídica nacional dos trabalhos em curso, ao nível da OCDE e da UE, relativas à garantia de um nível mínimo mundial de tributação para os grupos de empresas multinacionais e grandes grupos nacionais na União, que se destina a assegurar a tributação efetiva dos lucros a uma taxa de 15%. Por outro lado, verifica-se que a imposição de estruturas progressivas de taxas está associada a fenómenos de fragmentação do lucro por estruturas multi- -societárias, com impactos na escala dos negócios e na dimensão das empresas. A derrama municipal e a sua distribuição por município têm escassa eficácia e produzem efeitos perniciosos na eficiência e transparência. Deve, assim, caminhar-se no sentido de eliminar, de forma gradual, a progressividade da derrama estadual, e de eliminar a derrama municipal em sede de IRC;
- **Medidas promotoras do (re)investimento e de ganhos de escala**:
- Eliminação de constrangimentos à realização de reorganizações societárias e de benefícios em função da dimensão, através do aperfeiçoamento de clarificação do regime legal e fiscal aplicável às reorganizações empresariais. No caso de cisões e/ou reorganizações empresariais, evitando que o tratamento dos benefícios fiscais nas empresas resultantes seja um incentivo à inação. Revisão dos custos fiscais associados a operações de aquisição e/ou fusão;
- Revisão dos limites quantitativos ao reporte de prejuízos, e expansão das possibilidades de dedução total (sob a forma de custos) dos investimentos realizados, de modo a atenuar a tributação implícita sobre o reinvestimento empresarial;
- Criação do regime de Grupos de IVA que permita a consolidação das obrigações de IVA no contexto de um Grupo de sociedades;
- Eliminar as medidas que prejudicam o financiamento das empresas portuguesas.
- **Rever o regime geral das taxas que possa disciplinar e reduzir a criação de taxas pelas várias entidades das administrações públicas** (segundo alguns cálculos serão cerca de 4.300 as taxas atualmente existentes);

[Documento 2]
  Secção: PROGRAMA SOCIAL E DE GOVERNAÇÃO DA ALIANÇA DEMOCRÁTICA > CENÁRIO ORÇAMENTAL
| Juros                                                                          | 2.1   | 2.3   | 2.2   | 2.3   | 2.4   | 2.4   |
| Saldo global                                                                   | 0.8   | 0.8   | 0.2   | 0.1   | 0.2   | 0.2   |
| Dívida Pública (para 2023 valor reportado pelo BdP)                            | 98.7  | 96.0  | 92.2  | 88.5  | 84.4  | 80.2  |
| Saldo estrutural                                                               | 0.3   | -0.1  | 0.0   | 0.1   | 0.1   | 0.2   |
| Saldo estrutural primário                                                      | 2.4   | 2.2   | 2.2   | 2.4   | 2.5   | 2.6   |
| Carga fiscal                                                                   | 37.9  | 38.2  | 37.1  | 36.9  | 36.8  | 36.7  |
| Taxa de juro média implícita da Dívida Pública (%)                             | 2.1   | 2.3   | 2.4   | 2.6   | 2.8   | 2.8   |
| Por memória                                                                    |       |       |       |       |       |       |
| PIB nominal (mil M€)                                                           | 261.8 | 273.2 | 286.1 | 299.7 | 314.8 | 331.8 |
| Dívida Pública (mil M€)                                                        | 263.0 | 262.2 | 263.7 | 265.4 | 265.8 | 266.0 |
| Por memória                                                                    |       |       |       |       |       |       |
| Saldo global Programa de Estabilidade 2023                                     | -0.4  | -0.2  | -0.1  | 0.0   | 0.1   | n.d   |
| Saldo Global CPI do CFP                                                        | 0.9   | 0.8   | 0.6   | 0.4   | 0.3   | n.d   |
| Dívida Pública Programa de Estabilidade 2023                                   | 107.5 | 103.0 | 99.2  | 95.6  | 92.0  | n.d   |
| Dívida Pública CPI do CFP                                                      | 104.7 | 100.3 | 96.5  | 93.1  | 89.4  | n.d   |
| Ajustamento défice dívida (% do PIB- fonte: CFP)                               | 1.5   | 0.7   | 0.7   | 0.7   | 0.3   | 0.3   |  
O impacto orçamental das principais medidas do Programa da AD, encontra-se detalhado na tabela abaixo:  
**Tabela 3: Receitas**  
| Medida AD                                                                                                                                           | Rúbrica OE                             | Horizonte Temporal | Total Medida |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------------ | ------------ |
| Redução gradual de IRC de 21% para 15% ao ritmo de 2 p.p. por ano                                                                                   | Impostos sobre rendimento e património | 2025-2027          | 1,500        |
| Isenção de contribuições e IRS sobre prémios de desempenho e redução das taxas marginais de IRS até ao 8º escalão entre 0,5 e 3 p.p. face a 2023    | Impostos sobre rendimento e património | 2024-2026          | 2,000        |
| Adoção do IRS Jovem                                                                                                                                 | Impostos sobre rendimento e património | 2025               | 1,000        |
| Eliminação do IMT e Imposto de Selo para compra de habitação própria e permanente por jovens até aos 35 anos e redução para 6% do IVA da construção | Impostos sobre produção e importação   | 2025               | 500          |
| TOTAL MEDIDAS                                                                                                                                       |                                        |                    | 5,000        |  
**Tabela 4: Despesas**  
| Medida AD                                                                                              | Rúbrica OE           |           | Total Medida |
| ------------------------------------------------------------------------------------------------------ | -------------------- | --------- | ------------ |
| Reposição gradual do tempo de serviço dos professores (60 milhões por ano)                             | Despesas com pessoal | 2025-2028 | 240          |
| Aumento gradual do Complemento Solidário para Idosos até 820€ (estimativa alta de 200 milhões por ano) | Prestações sociais   | 2025-2028 | 800          |
| Introdução do Suplemento Remunerativo Solidário                                                        | Prestações sociais   | 2025-2028 | 800          |
| Universalização do acesso gratuito ao ensino pré escolar e creches                                     | Prestações sociais   | 2025      | 400          |
| TOTAL MEDIDAS                                                                                          |                      |           | 2,240        |

[Documento 3]
  Secção: PROGRAMA ECONÓMICO DA ALIANÇA DEMOCRÁTICA > Sumário Executivo > 3. AS NOSSAS REFORMAS > I. REDUZIR IMPOSTOS SOBRE O TRABALHO E O INVESTIMENTO > Reforma Fiscal:
#### I. REDUZIR IMPOSTOS SOBRE O TRABALHO E O INVESTIMENTO  
##### Reforma Fiscal:  
1. Redução do IRS para todos, com redução das taxas, especialmente para a classe média;
2. IRS Jovem até 15% para os jovens até aos 35 anos;
3. Isenção fiscal dos prémios por desempenho até 1 vencimento;
4. Redução gradual do IRC para 15% em 2 p.p. ao ano;
5. Simplificação e estabilidade fiscal;
6. Aceleração da justiça tributária.

## Bloco de Esquerda
[Documento 4]
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 6 Justiça Fiscal
## 6 Justiça Fiscal  
Em Portugal os salários pagam mais impostos do que o capital e o peso excessivo dos impostos indiretos castiga quem tem menos rendimentos. Justiça na economia é também justiça fiscal, ou seja, redução de impostos sobre o trabalho e sobre quem menos ganha, ao mesmo tempo que se deve aumentar a tributação sobre fortunas, grandes empresas e atividades especulativas.  
O Bloco propõe uma política de progressividade fiscal, com redução de IVA da eletricidade e telecomunicações para 6% e do cabaz de alimentos essenciais para 0% e com a aplicação de impostos sobre lucros excessivos, fortunas e criptoativos.  
carga fiscal em Portugal é inferior à média europeia. Em países como França, Finlândia, Dinamarca, Luxemburgo ou mesmo os Países Baixos, o peso dos impostos no PIB ultrapassa o registado em Portugal. Este facto não significa que se paguem poucos impostos, apenas que a sua incidência está mal distribuída e gravemente distorcida, em benefício do capital e da riqueza e em detrimento do trabalho e do consumo.  
A título de exemplo, em Portugal os impostos sobre o capital equivalem a 6,5% de toda a receita, quando a média na UE são 8,5%. Já o consumo pesa, em Portugal, 12,6%, acima da média europeia. Os salários contribuem com 8.3%. abaixo da média da UE. mas acima do capital.  
Entre as causas desta distorção estão as seguintes:  
1. A redução progressiva e histórica da tributação dos lucros em IRC, quer pela redução das taxas estatutárias, quer pela ainda maior diminuição do imposto efetivamente pago, fruto das regras que favorecem o planeamento fiscal agressivo e a evasão. Assim, não só a taxa estatutária de IRC foi cortada em 15,5p.p. nas últimas três décadas como, segundo o Banco de Portugal, a taxa efetiva acaba por ser, no mínimo, 6,5 p.p. inferior à taxa máxima legalmente estabelecida.  
**Taxa média sobre lucros (em percentagem)**  
Fonte: Base de dados de taxas do FAD  
- 2. Portugal não tributa como outros países a riqueza e o património e privilegia fiscalmente os rendimentos pessoais associados ao património imobiliário e financeiro. Em média, na OCDE, os impostos sobre a propriedade (imobiliária e financeira) equivalem a 5,7% da receita. Em França são 8,7% e mais de 10% no Canadá, no Reino Unido, no Luxemburgo ou mesmo nos EUA. Em Portugal, o peso relativo dos impostos sobre a propriedade é de apenas 4,2%. Enquanto vários países aplicam impostos sucessórios, sobre a riqueza ou sobre as transferências, Portugal tem vindo a eliminar essas formas de justiça fiscal, à exceção da criação do AIMI, cuja receita reverte para o Fundo de Estabilização da Segurança Social. Somos mesmo o terceiro país onde a diferença entre o imposto cobrado aos salários e aos dividendos é superior, em benefício dos últimos (mergulhão).
- 3. A prevalência dos impostos indiretos é muito superior em Portugal, onde estes valem 43% da receita total, face à média dos países da UE, onde têm um peso de apenas 34%. São vários os tributos que contribuem para este desequilíbrio, sendo o mais importante o IVA, que se aplica ao consumo de bens e serviços. Devido às suas taxas elevadas mas também às escolhas que colocam bens indispensáveis como a energia ou as telecomunicações no escalão máximo do IVA, este imposto tornou-se numa forma regressiva de tributação, que afeta mais quem dedica uma parcela maior do seu rendimento a consumos relativamente inelásticos.  
Só com a correção desses desequilíbrios é que o sistema tributário portugues pode cumprir as funções que constitucionalmente lhe estão atribuídas: reduzir as desigualdades e financiar o Estado Social. A tributação justa e progressiva da riqueza, dos rendimentos de capitais e imobiliários, é uma condição de justiça fiscal, ou seja, é a condição para a redução dos impostos sobre quem trabalha sem comprometer as receitas do Estado que devem financiar serviços públicos universais e de qualidade.  
A reforma fiscal proposta pelo Bloco de Esquerda centra-se assim em três objetivos: i) justiça e progressividade: i) justiça e progressividade fiscal, com vista ao desagravamento dos impostos sobre o trabalho e bens essenciais, por contrapartida a formas mais eficazes de taxação das grandes fortunas; ii) tributação justa dos lucros das grandes empresas e atividades especulativas, de forma a reverter o desagravamento fiscal histórico sobre os rendimentos de capital e penalizar as atividades puramente especulativas; iii) combate à evasão fiscal e à despesa fiscal injustificada, com a revisão de benefícios e regras fiscais abusivas.  
As medidas fiscais relacionadas com a habitação podem ser encontradas no respetivo capítulo.

[Documento 5]
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 6 Justiça Fiscal > 6.1 Aumentar a progressividade fiscal > As propostas do Bloco:
#### As propostas do Bloco:  
- → **Redução do IVA da eletricidade** e gás para a taxa mínima (6%);
- → **Redução do IVA das telecomunicações** para a taxa mínima (6%);  
- → Aplicação da **taxa zero de IVA a bens essenciais** à alimentação;
- → **Aumento do IVA dos hotéis** para a taxa máxima (23%).  
Só os 20% com mais rendimentos em Portugal pagam uma taxa efetiva de IRS superior a 13%. No entanto, as desigualdades no IRS persistem, sobretudo porque a existência de taxas especiais e liberatórias (taxas planas que não aumentam com o rendimento) aplicáveis aos rendimentos prediais e de capitais, que põem em causa a progressividade do imposto. Quanto mais altos os rendimentos de natureza não salarial, maior o ganho da aplicação de uma taxa fixa, em vez do englobamento sujeito a taxas progressivas.  
- → Introdução do **englobamento obrigatório** dos rendimentos em IRS para os dois escalões superiores de IRS. Desta forma, também estes rendimentos passariam a ser tributados progressivamente, de acordo com o nível de rendimentos do sujeito passivo. Esta medida exclui 95% dos contribuintes;
- → Atualizar a **dedução específica** no IRS em 582€, para 4.686€ de forma a compensar o aumento acumulado dos preços desde 2021. Para um agregado com duas pessoas e um salário mensal bruto de 2.500€, esta alteração permite uma poupança de 268€/ano.  
Além da desigualdade na distribuição dos rendimentos, a OCDE, suportada por outros estudos académicos (Piketty e Zucman, 2018; Abreu, 2023), alerta para uma crescente concentração da riqueza nas últimas décadas. Segundo a OCDE, Portugal é o segundo país onde a proporção de riqueza dos 1% mais ricos é maior, e equivale a 23% de toda a riqueza nacional. Entre os 1% mais ricos, 49 têm fortunas acima de 100 milhões de euros. Estes dados podem ler-se à luz de um outro relatório da OCDE, de 2021, que dá conta do peso das heranças na perpetuação das desigualdades. Assim, a organização defende que, deviam ser encontradas formas de tributar a herança, a propriedade e as doações.  
#### As propostas do Bloco:  
- → Criação de um **imposto sobre doações e heranças**, incluindo património mobiliário ou outras formas de ativos líquidos de dívidas, com valor superior a 1 milhão de euros. A taxa a aplicar deverá ser de 16% entre 1 e 2 milhões de euros, e de 25% para heranças acima de 2 milhões de euros. A receita deste imposto, como aconteceu com o Adicional do IMI para património de luxo, será usado para reforçar o sistema de segurança social, contribuindo para aumentar as pensões mais baixas;
- → Criação do **imposto de solidariedade sobre as grandes fortunas**, que incide sobre o património global dos sujeitos passivos cuja fortuna seja superior a 2000 salários mínimos nacionais. O imposto estrutura-se da seguinte forma:
- → Valor patrimonial entre 2000 e 2500 salários mínimos nacionais, 0,6%;
- → Entre 2500 e 4000 salários mínimos nacionais, 0,8%;
- → Entre 4000 e 8000 salários mínimos nacionais, 1%;
- → Mais de 8000 salários mínimos nacionais, 1,2%.

[Documento 6]
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 6 Justiça Fiscal > 6.2 Tributação justa dos lucros das grandes empresas e das atividades especulativas > Os impostos que a EDP recusa pagar > As propostas do Bloco:
##### As propostas do Bloco:  
→ Criação de um **novo escalão da derrama estadual** para empresas com lucros entre 20 milhões e 35 milhões com a taxa de 7%. Este novo escalão permite um pequeno aumento do IRC das empresas com maiores lucros, que pode ser canalizado para o financiamento dos serviços públicos e da segurança social;  
- → Criação de um **imposto sobre a prestação de determinados serviços digitais** onde a participação dos utilizadores e das utilizadoras cria valor para as empresas prestadoras do serviço. O imposto aplica-se a: publicidade dirigida a utilizadores e utilizadoras de determinada interface ou plataforma digital (serviço de publicidade online); a disponibilização de interfaces ou plataformas digitais que permitam a quem utiliza localizar outras pessoas e interagir com elas, facilitando entrega de bens ou prestação de serviços subjacentes diretamente a esses utilizadores (serviço de intermediação online); a transmissão, incluindo a venda ou cessação, dos dados recolhidos gerados por atividades realizadas nas interfaces ou plataformas digitais (serviços de transmissão de dados). A taxa de imposto proposta é de 3% e as condições que obrigam ao pagamento do imposto são: que o volume de negócios no ano anterior tenha superado os 750 milhões de euros; que o montante total das suas receitas provenientes de serviços digitais sujeitas ao imposto, uma vez aplicadas as regras para a definição da base tributável e território nacional, supere 1,5 milhões de euros. Calcula-se que a receita assim obtida seja de 60 milhões de euros;
- → **Revisão das regras de tributação aplicáveis aos grupos económicos** e, em particular, às transferências de rendimentos intragrupo com vista à erosão da base tributável;
- → **Reposição dos limites temporais para a dedução de prejuízos fiscais**  para 5 e 12 anos, conforme se trate de grandes empresas ou PME, respetivamente;
- → **Criação de um imposto sobre lucros excessivos**, aplicável aos setores em que estes se verificaram por força da inflação e elevadas taxas de juro, como a banca, a distribuição e a energia;
- → **Tributação de todas as mais-valias em criptoativos em sede de IRS**, eliminando a atual situação de privilégio face até a outros ativos financeiros.

[Documento 7]
  Secção: Fazer o que nunca foi feito: Programa eleitoral do Bloco de Esquerda, Legislativas 2024 > 3 Trabalho, Salário e Pensões > 3.4 Combater a Pobreza > As propostas do Bloco:
#### As propostas do Bloco:  
→ Reforço do **Rendimento Social de Inserção**, aumentando o valor de referência do RSI e diminuindo a diferença da capitação entre os membros do agregado. O valor de referência deve ser equiparado progres-  
sivamente ao IAS e deve ser reforçada a componente de integração através do acompanhamento e da ação social e integrando-o, a prazo, num Rendimento Social de Cidadania;  
- → Reforço das **prestações de desemprego**, designadamente: i) retomando o salário mínimo nacional como referência do valor mínimo do subsídio de desemprego contributivo (e não o IAS, que ainda por cima é inferior ao limiar de pobreza); ii) aumentando os períodos de concessão, voltando às regras de 2009; iii) tornando o valor do IAS o valor mínimo de referência do subsídio social de desemprego (atualmente é 80% do IAS no caso do trabalhador considerado isoladamente); mudar a condição de recursos do subsídio social de desemprego, tomando o IAS por elemento do agregado o valor de referência para acesso e mudando a capitação;
- → **Criação de uma nova prestação social que unifique os apoios não contributivos**. Numa primeira fase, este "Rendimento Social de Cidadania" deve ser capaz de cobrir os casos que não estão abrangidos pelas prestações de desemprego e pelo RSI (nomeadamente trabalhadores independentes, informais, trabalhadores com prazos de garantia inferiores a meio ano). Numa segunda fase, o Rendimento Social de Cidadania absorveria o RSI e o Subsídio Social de Desemprego (duas prestações não contributivas, isto é, financiadas pelo Orçamento do Estado), fundindo estes apoios numa nova prestação, sem o estigma atual e com um novo impulso. Ela funcionaria como uma prestação diferencial capaz de garantir que ninguém fica abaixo do limiar de pobreza;
- → Subordinação das novas políticas públicas à prévia avaliação no Parlamento do seu previsível impacto, positivo ou negativo, sobre a pobreza e a exclusão social. É instrumentalmente crucial que, para além de atacarmos as consequências sejamos capazes de prevenir as causas e que, para isso, as políticas setoriais – particularmente aquelas que objetivamente terão um potencial impacto sobre a pobreza - sejam aprovadas após uma prévia avaliação dos seus impactos na produção, manutenção ou agravamento da pobreza e da exclusão social;
- → Reforço da **Estratégia Nacional de Integração das Pessoas Sem-abrigo**. Entre outras medidas, deve haver um investimento substancial num programa nacional de "**Housing First**" (ou Casas Primeiro), através do qual, em articulação com os municípios, se concedam habitações sem impor condições prévias, como primeiro passo para o processo de rein-  
tegração. Em quatro anos, este programa deve dar resposta ao conjunto de situações identificadas. Deve também ser garantida a contratação de profissionais com formação especializada que acompanhem as pessoas, assegurando que o programa das "Casas Primeiro" tem capacidade de sucesso nos seus objetivos;  
→ Universalização do abono de família, repondo-o o 4.<sup>o</sup>, o 5.<sup>o</sup> e o 6.<sup>o</sup> escalões.

## CHEGA
[Documento 8]
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > VIII CAPÍTULO O QUE JÁ FIZEMOS PARA DAR MAIS RENDIMENTOS ÀS FAMÍLIAS E EMPRESAS
## VIII CAPÍTULO O QUE JÁ FIZEMOS PARA DAR MAIS RENDIMENTOS ÀS FAMÍLIAS E EMPRESAS  
**PROPOSTA DE ALTERAÇÃO OE24 Nº177C (CH)**  
N.º 1, N.º 2, N.º 5, Artigo 87.º do código do IRC, constante do Artigo 144.º da PPL / Imposto sobre o rendimento das pessoas coletivas.  
**PROPOSTA DE ALTERAÇÃO OE24 Nº1507C (CH)** Artigo 173.º-A (Contribuição extraordinária sobre o sec-  
**REJEITADO**  
**CONTRA** Partido Socialista, PSD, PCP, BE, L **ABSTENÇÃO** PAN **FAVOR** CHEGA, IL  
**REJEITADO**  
**CONTRA** Partido Socialista, PSD, IL **ABSTENÇÃO** PCP, L **FAVOR** CHEGA, BE, PAN  
**PROPOSTA DE ALTERAÇÃO OE 24 Nº 1590C (CH)**  
Artigo 161.º-A (Redução do valor do IUC)  
tor bancário)  
**REJEITADO**  
**CONTRA** Partido Socialista, PSD, PCP, BE, PAN, L **ABSTENÇÃO** IL **FAVOR** CHEGA  
**PROPOSTA DE ALTERAÇÃO OE24 Nº 1503C**  
Verba 2.9, Lista II anexa ao Código do IVA / Alteração ao Código do Imposto sobre o Valor Acrescentado - IVA Gasolina e Gasóleo Rodoviário  
**PROPOSTA DE ALTERAÇÃO OE24 Nº 1486C**  
Ponto 2, Alínea b), N.º 3, Artigo 2.º do Código do IRS / Aumento para 80% da dedutibilidade do subsídio de alimentação.  
**REJEITADO**  
**CONTRA** Partido Socialista, PSD, PCP, BE, PAN, L **ABSTENÇÃO** IL **FAVOR** CHEGA  
**REJEITADO**  
**CONTRA** Partido Socialista, PSD **ABSTENÇÃO** IL, PCP, BE, PAN, L **FAVOR** CHEGA

[Documento 9]
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > VIII CAPÍTULO MAIS RENDIMENTOS PARA AS FAMÍLIAS E EMPRESAS. COMO? > PROPOSTAS
### PROPOSTAS  
**181.** Introduzir duas taxas marginais de IRS: de 15% até aos 39.999 euros e de 30% a partir de 40.000 euros, com isenção de pagamento para quem receber até aos mil euros mensais.  
**182.** Isentar os jovens até aos 35 anos de IRS até perfazerem um total de 100 mil euros de rendimentos desde o início da sua carreira.  
**183.** Isentar de IRS o designado "15.º salário", sem quaisquer condicionantes.  
**184.** Introduzir uma _flat tax_ de IRC de 15% para as regiões autónomas e para o interior do país e de 18% para o resto do território.  
**185.** Criar um modelo de número único de identificação para as pessoas e empresas, assim evitando que a mesma pessoa tenha que ter número de utente, de cartão de cidadão, de contribuinte, de Segurança Social, de eleitor, etc.  
**186.** Eliminar o adicional do IMI; isentar de IMI e de IMT a compra de habitação própria e permanente, assim como a tributação de mais-valias da venda de habitação própria e permanente, desde que seja reinvestida na compra de uma nova habitação própria e permanente mesmo que de valor inferior para si ou para descendentes directos, no pagamento de empréstimos bancários, ou no caso dos reformados/pré-reforma.  
**187.** Aplicar a taxa de IVA reduzida (6%) à Electricidade e ao Gás e implementar uma tarifa social da energia para famílias numerosas, considerando os primeiros 200 kWh consumidos por família/mês, desde que a potência contratada não ultrapasse os 10,35kVA.  
**188.** Reintroduzir o IVA zero para bens alimentares essenciais e proceder ao alargamento da lista anteriormente aprovada, assim como aplicar a taxa de IVA reduzida (6%) para a restauração.  
**189.** Reduzir o IVA do Gasóleo e da Gasolina Rodoviária para a taxa intermédia de 13% e eliminar o adicional ao Imposto Sobre Produtos Petrolíferos.  
**190.** Terminar com a dupla tributação na compra de carro novo e com o cálculo indevido do ISV quando se trata de veículos usados matriculados noutro Estado-membro da União Europeia.  
**191.** Implementar medidas que permitam que as Cooperativas, Fundações, Instituições Particulares de Solidariedade Social (IPSS), Santas Casas da Misericórdia, Mutualidades e Associações de reconhecido interesse público sem carácter lucrativo possam deduzir/recuperar 100% do valor do IVA que lhes é cobrado nas aquisições internas, nas aquisições intracomunitárias e nas prestações de serviços.  
**192.** Aplicar a taxa autónoma de 10% aos rendimentos provenientes de rendas de contratos estabelecidos com alunos do ensino superior e aos rendimentos decorrentes de contratos de arrendamento para habitação permanente celebrados com duração inferior a dez anos; aos contratos  
com o mesmo fim, mas celebrados com prazo superior a 10 anos, a taxa autónoma aplicável é de 5%.  
**193.** Proceder à revisão do actual Regime Geral das Infracções Tributárias, promovendo a simplificação processual, reformulando a organização judiciária e tributária e estabelecendo um novo regime geral para as infracções tributárias.  
**194.** Implementar apoio jurídico e mediação gratuita para a defesa de pequenos contribuintes junto da Administração Tributária quando estejam em causa pequenos montantes de impostos ou outros tributos e/ou execuções fiscais de pequeno valor.  
**195.** Tornar as normas fiscais mais objectivas e claras:  
- Evitando complexidades desnecessárias e, consequentemente, reduzindo litígios;  
- Pugnando pela publicação atempada de todas as orientações da Autoridade Tributária (AT), assim trazendo mais transparência e clareza à interpretação feita pela AT e contribuindo para a uniformização de procedimentos;  
- Através da promoção da publicação de Códigos anotados, pela própria Assembleia da República, como já aconteceu na década de 80, assim facilitando o cumprimento das normas por parte dos contribuintes.  
**196.** Reforçar os meios técnicos e humanos da AT para o combate à fraude e à evasão fiscal e melhorar os meios (inclusivamente legais) para o apuramento de manifestações de fortuna, nomeadamente, através da comunicação à AT do nome e NIF dos adquirentes de determinados bens de luxo.  
**197.** Promover de forma activa a reintegração dos valores da economia paralela na economia lícita, quer através da simplificação fiscal, quer do aumento significativo da fiscalização nesta matéria, com o objectivo de recuperar 20%/ ano estes montantes para a economia nacional.  
**198.** Criar o protocolo "zero economia paralela", com o objectivo de em seis anos recuperar tendencialmente todos os valores movimentados no âmbito da economia paralela para a economia nacional (cerca de 89 mil milhões de euros ano).  
**199.** Transferir para o sector das telecomunicações a taxa sobre o Audiovisual, retirando-a da factura de electricidade e atribuindo o seu pagamento às empresas de telecomunicações a operar em Portugal

[Documento 10]
  Secção: PROGRAMA ELEITORAL: LIMPAR PORTUGAL > X CAPÍTULO FAZER PORTUGAL CRESCER. COMO? > PROPOSTAS
### PROPOSTAS  
**229.** Reduzir a carga fiscal para incentivar o investimento e estimular o crescimento das empresas, nomeadamente:  
- Desagravar a taxa de IRC para 15% ao longo da legislatura, com efeito imediato nas empresas com sede social nos concelhos do interior;  
- Desagravar a Derrama Estadual e Municipal;  
- Aumentar o limite de isenção de IVA para Trabalhadores Independentes e Empresários em Nome Individual (ENI);  
- Desagravar fiscalmente as empresas que utilizam o lucro gerado para o reinvestimento no negócio e para a criação de emprego.  
**230.** Simplificar e desburocratizar os processos administrativos para facilitar a criação de novos negócios, nomeadamente através da:  
- Digitalização de Serviços Públicos;
- Revisão e Simplificação de Processos;
- Redução de Exigências Regulatórias para Empresas;  
- Criação de uma conta-corrente entre o Estado e as empresas a fim de agilizar o relacionamento entre as duas entidades.  
**231.** Rever o Código do Trabalho, tornando-o mais simples, garantindo flexibilidade às empresas e segurança aos trabalhadores, nomeadamente, promovendo o trabalho remoto e flexível e, eventualmente, implementar os Contratos de Zero Horas para Desempregados e Reformados.  
**232.** Proceder ao levantamento das áreas consideradas estratégicas, onde o Estado pode e deve manter a sua participação, ainda que com abertura para a participação dos privados, avaliando de forma criteriosa as empresas públicas, nacionais, regionais e municipais.  
**233.** Implementar medidas de governança corporativa para melhorar a eficiência e a transparência das empresas públicas, nomeadamente:  
- Estabelecer Conselhos de Administração independentes, baseados na competência e não na simpatia ou filiação partidária;  
- Definir políticas claras e códigos de conduta internos;
- Exigir a prestação de contas de forma transparente;
- Fortalecer a gestão de riscos e controlos internos;  
- Facilitar a participação dos accionistas nas assembleias gerais, fornecer informações adequadas e garantir a protecção dos seus direitos.  
**234.** Identificar necessidades de infra-estrutura turística, promovendo o seu investimento público e privado, incluindo as áreas necessitadas de alojamento e infra-estrutura de transportes e lançar programas de apoio à satisfação dessas necessidades.  
**235.** Revogar a legislação que impõe restrições ao alojamento local (Programa Mais Habitação).  
**236.** Atrair investimentos na infra-estrutura turística, preferencialmente para as áreas do interior, através da criação de incentivos fiscais e da simplificação dos processos de licenciamento.  
**237.** Concluir o processo de escolha do Novo Aeroporto de Lisboa e iniciar com a maior brevidade possível a sua construção, bem como de outras infra-estruturas indispensáveis, nomeadamente a Ferrovia e o TGV (Alta Velocidade).  
**238.** Promover o turismo sustentável, partindo do princípio que o turista além de visitar lugares, pretende viver experiências, respeitando o meio-ambiente e as comunidades locais.  
**239.** Criar centros de inovação e parques tecnológicos com o objectivo de desenvolvimento de políticas de inovação que promovam a colaboração entre universidades, empresas privadas e sector público, incluindo metas de investimento em I&D, apoio à transferência de tecnologia e estímulo ao empreendedorismo.  
**240.** Promover os centros de inovação e parques tecnológicos por meio de campanhas de marketing, participação em eventos nacionais e internacionais e atracção de investidores e parceiros.  
**241.** Desenvolver programas de qualificação e formação em parceria com universidades e empresas privadas, incluindo bolsas de estudo, programas de estágio e cursos de actualização para profissionais.  
**242.** Oferecer benefícios fiscais, como redução de impostos ou isenções, bem como estabelecer parcerias com empresas privadas que se envolvam em projectos de inovação em sectores estratégicos de que resulte um saldo positivo entre exportações e importações.  
**243.** Apoiar a internacionalização das empresas portuguesas, apostando na atracção de investimento e nas exportações, no desenvolvimento de programas de qualificação para habilitar as empresas e quadros com as competências e conhecimentos necessários a operar em mercados internacionais, devendo o Estado actuar como facilitador mas também trabalhar na atractividade do investimento estrangeiro em Portugal, promovendo a marca Portugal no exterior para atrair mais investimento.  
**244.** Facilitar o acesso a mercados externos através da remoção de barreiras comerciais, negociando ou renegociando acordos, facilitando o acesso a redes de distribuição e canais de venda no exterior e fornecendo informações sobre oportunidades de mercado, procura por produtos ou serviços específicos e tendências globais.

## Iniciativa Liberal
[Documento 11]
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 1. MAIS OPORTUNIDADES, MAIS SALÁRIO > 1.2. Reforma Fiscal: Menos Impostos, Mais Salário > Impostos mais baixos e mais simples para todos
#### 1.2. Reforma Fiscal: Menos Impostos, Mais Salário  
##### Impostos mais baixos e mais simples para todos  
Portugal precisa de crescer. Esta é a principal bandeira que a Iniciativa Liberal defende desde que foi fundada. Esta necessidade de crescimento reflete-se no PIB per capita em paridades de poder de compra face à média da União Europeia. Portugal encontra-se praticamente estagnado desde 2011, com oscilações pouco significativas. Portugal mantém-se na cauda da Europa, sendo ultrapassado por 8 países desde o ano 2000. O crescimento não é meramente um capricho liberal: ele não só reflete a melhoria das condições de vida das pessoas, como é igualmente essencial para a melhoria no rácio da dívida pública sobre o produto e o respetivo cumprimento das regras orçamentais da União Europeia, sem colocar em causa o funcionamento do Estado Social e o investimento público.  
O país tem de ser fiscal e administrativamente competitivo, tirando peso e complexidade ao sistema fiscal atualmente vigente. **Portugal tem de deixar de ter uma das maiores taxas de esforço fiscal da União Europeia e passar a ter uma das menores**, como é o caso de países mais liberais como a Irlanda, o Luxemburgo e os Países Baixos. Segundo os dados do Eurostat, Portugal teve em 2022 a quarta maior taxa de esforço fiscal da Europa. Os portugueses não suportam mais esta situação.  
Hoje temos impostos de rico e salários de pobre. Além disso, temos um nível de progressividade enorme, com um recorde europeu de nove escalões, que pune quem quer subir na vida pelo trabalho. E temos um nível de tax wedge muito elevado, onde o Estado leva em média 42% do que a empresa paga por um trabalhador e onde o Estado leva cerca de metade do que a empresa paga por um aumento salarial. É isto que temos de mudar imediatamente. O sistema fiscal liberal recompensa o esforço, dedicação e produtividade daqueles que trabalham e aqueles que assumem riscos, estimulando assim a concorrência.  
Hoje, essa competição não se limita ao âmbito nacional, estendendo-se ao cenário continental e mesmo global. Portugal está em competição direta com o resto do mundo para atrair capital e empregos qualificados. Contudo, a carga fiscal excessiva sobre o trabalho e as empresas nas últimas décadas resultou numa significativa emigração de mão-de-obra altamente qualificada e desvio de investimento para outras regiões. É urgente alterar este panorama.  
**A Iniciativa Liberal defende a descida e simplificação dos impostos sobre rendimentos das pessoas e das empresas, nomeadamente do IRS e do IRC**, promovendo ainda a eliminação de casos de dupla tributação, bem como de taxas e contribuições coercivas que promovem complexidade e barreiras à entrada em mercados competitivos. Além disso, se a energia – neste caso eletricidade e gás – é um bem essencial quer para a vida das famílias quer para a atividade das empresas então não pode ser taxada como um bem de luxo, devendo **o IVA do gás e da eletricidade baixar para 6%**.  
Para crescermos, é também necessária a **revisão e redução de impostos sobre o património**, uma vez que se tratam de impostos que incidem sobre bens comprados por rendimentos que já foram tributados e sobre transações que também foram já tributadas. A Iniciativa Liberal apresenta igualmente alterações ao IMI, de forma a desonerar a detenção do património, bem como ao Imposto do Selo, ao IVA e ao IMT, para desonerar a construção e a aquisição da habitação própria e permanente na transação, medidas que são expressamente apresentadas no capítulo referente à Habitação.  
**Reduzir e Simplificar o IRS até à Taxa Única de 15%**  
Propomos **implementar uma taxa única de 15% a aplicar-se aos rendimentos acima do salário mínimo nacional anualizado**, garantindo a progressividade e mantendo as atuais deduções à coleta previstas.  
A Iniciativa Liberal mantém-se firme na sua proposta de reduzir a progressividade excessiva e simplificar o IRS para todos os contribuintes que têm de obrigatoriamente pagar o imposto, sem prejudicar os contribuintes isentos de IRS.  
Com a aplicação deste IRS substancialmente mais baixo para todos, serão igualmente revogados os atuais programas e benefícios fiscais dirigistas que causam injustiças sociais entre os mais jovens e não jovens, bem como entre os residentes e os não residentes.  
Estamos disponíveis para aprovar e desenvolver propostas transitórias, desde que se baixe significativamente a progressividade excessiva do imposto, reduzindo o número de escalões, e que se incentive claramente a competitividade fiscal dos salários de emprego qualificado. Mais concretamente, a Iniciativa Liberal **numa primeira fase propõe um imposto com duas taxas**, uma de 15% sobre os rendimentos acima de 11.480 euros e abaixo de 21.321 euros, **garantindo a progressividade**, sendo aplicada uma taxa de 28% acima desse patamar de rendimento anual. Em suma, pretende-se isentar de imposto os rendimentos mais baixos aumentando significativamente a dedução específica, agregando os primeiros quatro escalões e, por fim, agregando os últimos cinco escalões com a taxa de 28%. Eis alguns exemplos da poupança esperada por esta alteração.  
| Rendimento | Rendimento<br>Imposto   |          | Proposta de taxa única de 15% |                    |                 | Proposta transitória de 2 taxas |                    |                 |
| ---------- | ----------------------- | -------- | ----------------------------- | ------------------ | --------------- | ------------------------------- | ------------------ | --------------- |
| mensal     | bruto<br>bruto<br>anual | Atual \* | Imposto\*                     | Poupança<br>(abs.) | Poupança<br>(%) | Imposto \*                      | Poupança<br>(abs.) | Poupança<br>(%) |
| 900        | 12.600                  | 784      | 168                           | 616                | 79%             | 168                             | 616                | 79%             |
| 1.100      | 15.400                  | 1.667    | 588                           | 1.079              | 65%             | 588                             | 1.079              | 65%             |
| 1.300      | 18.200                  | 2.295    | 1.008                         | 1.287              | 56%             | 1.008                           | 1.287              | 56%             |
| 1.500      | 21.000                  | 2.952    | 1.428                         | 1.524              | 52%             | 1.428                           | 1.524              | 52%             |
| 1.700      | 23.800                  | 3.680    | 1.848                         | 1.832              | 50%             | 2.170                           | 1.510              | 41%             |
| 2.500      | 35.000                  | 7.397    | 3.528                         | 3.869              | 52%             | 5.306                           | 2.091              | 28%             |
| 4.000      | 56.000                  | 15.060   | 6.678                         | 8.382              | 56%             | 11.186                          | 3.874              | 26%             |

[Documento 12]
  Secção: PROGRAMA ELEITORAL > PORTUGAL A CRESCER > 1. BAIXAR IMPOSTOS E DESBUROCRATIZAR
### 1. BAIXAR IMPOSTOS E DESBUROCRATIZAR  
- **Taxa única de IRS de 15% sobre a parte dos rendimentos que exceda o Salário Mínimo Nacional, começando de forma gradual com duas taxas de 15% e 28%, aumentando imediatamente o salário líquido**
- **Reduzir a carga fiscal sobre os profissionais liberais e os trabalhadores independentes**
- **Taxa única de IRC de 12% para as empresas, excepto para as grandes multinacionais que será de 15% de acordo com o exigido pela lei europeia**
- **Criar uma task force de eliminação de burocracias desnecessárias em diálogo com cidadãos e empresas**
- **Criar Zonas Económicas Especiais (ZEE) de baixa fiscalidade no interior do país para atrair investimento direto estrangeiro e promover a criação de hubs empresariais**
- **Reverter as normas do pacote Mais Habitação relativas ao Alojamento Local, eliminar a redução do coeficiente fiscal**
- **Eliminar várias taxas e contribuições extraordinárias como o adicional ao IMI (AIMI) e o imposto do selo sobre transações já taxadas**
- **Eliminar gradualmente o Imposto Único de Circulação (IUC)**
- **Reduzir o imposto sobre rendimentos de capitais para 14,5%**
- **Compromisso de Orçamentos com superávit e redução da dívida pública**

[Documento 13]
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 1. MAIS OPORTUNIDADES, MAIS SALÁRIO > 1.2. Reforma Fiscal: Menos Impostos, Mais Salário > Impostos mais baixos e mais simples para todos
| 4.000      | 56.000                  | 15.060   | 6.678                         | 8.382              | 56%             | 11.186                          | 3.874              | 26%             |  
\* – Imposto apurado antes de deduções à coleta. Estas deduções, mantendo-se, conforme proposto, são indiferentes para o apuramento da poupança entre o imposto atual e o imposto proposto.  
**Baixar o Imposto sobre rendimentos de capitais e prediais**  
Em matéria de tributação de rendimentos de capitais, mais-valias e prediais, a Iniciativa Liberal defende a **redução do imposto para 14,5%, sem englobamento obrigatório**. Em matéria de rendimentos prediais de arrendamento habitacional, propõe-se uma taxa 14.5% com uma descida gradual do imposto, conforme referido posteriormente no capítulo A.2 sobre Habitação.  
**Tributar stock-options no momento da realização da venda e não no exercício da opção**  
A Iniciativa Liberal quer corrigir o momento da tributação da conversão de opções sobre ações em ações para que a mesma ocorra no momento da alienação do ativo. Atualmente, existem duas formas de tributar a conversão de opções sobre ações em ações. A primeira é a prevista no Código de IRS, que prevê a tributação no período em que é exercida a opção e que dá o direito ao trabalhador de ter o número de ações correspondentes, com a valorização que possuem as ações à data da conversão. A segunda com a tributação a ocorrer apenas quando se der a mais- ou menos-valia das ações sobre a qual o trabalhador exerceu a sua opção, conferida pelo benefício fiscal criado por este Governo para os trabalhadores em start-ups. Esta situação cria uma tremenda **desigualdade entre contribuintes em circunstâncias idênticas**, levando a que os primeiros sejam, invariavelmente, prejudicados face aos segundos apenas por uma questão de tratamento fiscal.  
Da forma como está a ser aplicada a lei, há casos de trabalhadores que, não querendo beneficiar dos descontos de taxas que o benefício fiscal também concede, vêem-se na obrigação de se endividar para liquidar impostos. Isto sucede por causa de uma variação do valor das ações que poderão não conseguir liquidar por ainda não terem realizado qualquer tipo de mais-valia com as mesmas. Ou seja, pagam impostos por uma mais-valia esperada, muitas vezes pressionados por apertados prazos de exercício de conversão de opções de ações, sem conhecimento da valorização das mesmas no momento da decisão do exercício das opções.  
A forma mais adequada para garantir um tratamento justo, informado e a capacidade contributiva dos contribuintes é **tributar esta conversão de opção de ação em ação como rendimento de trabalho apenas quando essa ação gerar uma mais ou menos valia na sua alienação**, tal como previsto no benefício fiscal recentemente criado pelo Governo.  
**Baixar e Simplificar o IRC**  
A Iniciativa Liberal propõe uma **taxa de IRC de 12% para as empresas**. Cumprindo a nova legislação europeia, a Iniciativa Liberal quer **aplicar a taxa de IRC mínima de 15% para as multinacionais com uma faturação anual superior a 750 milhões de euros**, seguindo o valor mínimo do imposto pela OCDE, e que a UE através da nova diretiva europeia requer dos Estados-Membros. É urgente simplificar e libertar as empresas da necessidade de consumirem tempo e recursos em atividades improdutivas, permitindo um foco na produção, na melhoria contínua e na expansão. E é necessário atrair investimento estrangeiro, colocando Portugal entre os países mais atrativos da Europa ocidental para as empresas a nível fiscal. Esta reforma implica **revogar as derramas** bem como eliminar as tributações autónomas que representam acréscimos de carga fiscal sobre as empresas em Portugal, completamente contrárias à prática internacional.  
**Portugal tem a segunda maior taxa estatutária máxima de IRC da OCDE**, sendo igualmente o  
**segundo pior país em termos de competitividade fiscal das empresas**, entre os trinta e oito países que a integram, de acordo com o estudo da Tax Foundation em 2023. Na fiscalidade sobre as empresas, Portugal destaca-se negativamente pela sua taxa máxima e pela complexidade. A Iniciativa Liberal tem alertado incessantemente para estes dois fatores, uma vez que põem em causa a capacidade de atrair e manter capital em Portugal, ainda mais num mercado de capitais tão aberto como é a União Europeia.  
Para além do efeito dissuasor expectável que resulta da taxa estatutária máxima de 31.5% de IRC existente em Portugal, a **progressividade imposta pela derrama estadual e as diferenciações de taxação entre empresas com diferentes dimensões, impede a progressão da evolução das empresas** e incentiva-as a manterem-se pequenas e pouco competitivas. Há ainda uma imensidão de benefícios fiscais que, para além de representarem um ímpeto dirigista sobre aquilo que deveria ser a livre iniciativa das empresas, é também uma fonte de improdutividade da nossa economia, abrindo portas à corrupção e favorecimento de certos nichos e empresas.  
O tecido empresarial português tem de ser mais produtivo e mais atrativo, pelo que um sistema fiscal mais simples e mais baixo é fundamental para esse desenvolvimento que a todos beneficia ao enriquecer a economia nacional. Esta simplificação do sistema permite, igualmente, libertar recursos da própria Autoridade Tributária para focar na pedagogia junto do contribuinte para liquidação voluntária, bem como, investigar e combater situações de evasão e fraude fiscal.  
**Eliminar taxas, contribuições e impostos adicionais**  
A Iniciativa Liberal quer eliminar taxas, contribuições e impostos adicionais com vista a **aumentar a competitividade fiscal do país e baixar os custos de contexto**. Sugerimos eliminar:  
- A duplicação de impostos resultante da cobrança de impostos sobre transações que envolvem outros impostos, como é o caso do Imposto do Selo na compra de casas sujeitas ao Imposto Municipal sobre as Transmissões (IMT);
- Contribuição extraordinária sobre o Alojamento Local;
- Contribuição extraordinária sobre a indústria farmacêutica;
- Contribuição extraordinária sobre os fornecedores do Serviço Nacional de Saúde de dispositivos médicos;
- Contribuição extraordinária sobre o setor energético;
- Taxas devidas ao ICP-ANACOM, no âmbito das entidades formadoras na área de infraestruturas: ITUR e ITED;
- Taxas de utilização do espectro radioeléctrico;
- Taxas de emissão de títulos habilitadores de serviços de rádio e televisão;

## LIVRE
[Documento 14]
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > Trabalho, Rendimento, Tempo e Proteção Social > Por isso defendemos:
### Por isso defendemos:  
1. **Tirar Portugal da armadilha dos salários baixos, aumentando os rendimentos**: através de um compromisso de subida do salário mínimo nacional ao longo da legislatura até aos 1150 euros, em 2028, permitindo assim reforçar o valor do trabalho enquanto componente produtiva fundamental para a economia, e definindo metas para o rácio do SMN em relação ao PIB per capita ou ao salário médio; estabelecendo uma estratégia de concertação nacional para a valorização salarial, nos vários níveis da escala de rendimentos, com particular ênfase nos salários médios e para os rendimentos do trabalho qualificado, através, também, de uma indexação à inflação e a métricas de produtividade. É também urgente regular as diferenças salariais dentro da mesma entidade, estabelecendo um limite máximo para o rácio entre o salário mais baixo e o salário mais alto em cada empresa, organização ou ramo de atividade.  
2. **Promover uma maior e mais justa distribuição da riqueza**, através de uma revisão das taxas e escalões de IRS, da atualização do valor de referência do mínimo de existência e da dedução específica, garantindo que não há um agravamento fiscal indireto pelo facto de a inflação não ser incorporada nos limites dos escalões e deduções das famílias. Aumentar a progressividade do IRS e a capacidade redistributiva e de redução das desigualdades deste imposto. Rever a taxa adicional de solidariedade, e os limites a que se aplica, aumentando o contributo dos que têm rendimentos mais elevados e milionários, de forma a permitir baixar a contribuição dos rendimentos médios, garantindo uma maior justiça fiscal.  
3. **Incentivar a compensação adicional dos trabalhadores pelas empresas que geram lucros** não reinvestidos, majorando a dedução em sede de IRC relativa às gratificações de balanço e isentando de IRS os montantes atribuídos aos trabalhadores a título de participação nos lucros das empresas, até ao valor de uma remuneração média mensal e com o limite de 5 vezes a RMMG. Estes rendimentos não estão sujeitos a englobamento para determinação da taxa aplicável aos restantes rendimentos.  
4. **Promover a simplificação fiscal** através da revisão de regulamentos, limites e excepções, bem como das obrigações declarativas perante a Autoridade Tributária, nomeadamente através de uma maior integração das informações prestadas pelos contribuintes.  
5. **Combater a precariedade e o abuso pelas entidades empregadoras:**  
- ao reforçar a capacidade da Autoridade para as Condições do Trabalho, com recursos técnicos, legais e humanos, para fiscalizar as condições laborais nos setores público e privado, assim como para fiscalizar a efetividade do tempo prestado de trabalho, prevenindo abusos sobre trabalhadores decorrente do seu registo por plataformas ou meios digitais;
- erradicar os estágios não remunerados ou pagos abaixo do salário mínimo, os falsos recibos verdes, os falsos estágios e o falso trabalho independente;
- regular o recurso abusivo ao trabalho temporário, restringir os contratos a prazo a funções comprovadamente temporárias e ao trabalho suplementar;
- facilitar a trabalhadores o acesso à informação sobre o assédio moral em contexto de trabalho por forma a evitar e punir comportamentos inapropriados;
- regular os anúncios de emprego para garantir um mercado de trabalho mais transparente e com menos fricções e fraudes, nomeadamente obrigando os anúncios de emprego a apresentar uma remuneração mínima associada ao cargo.  
6. **Aumentar o tempo disponível para todas as pessoas:**  
- pela continuação da experiência da semana de 4 dias de trabalho no setor privado e na administração pública, promovendo a inclusão da semana de 4 dias na contratação coletiva e nos acordos de empresa, trabalhando para uma experiência a nível nacional de um período de semanas de 4 dias - à semelhança do que fez a cidade de Valência em Espanha;
- atingir 30h semanais e 30 dias de férias anuais até 2030, através da implementação imediata das 35 horas semanais de trabalho e dos 25 dias de férias e planeando progressivamente a redução do tempo de trabalho e aumentando os dias de férias;
- pelo não aumento da idade mínima de reforma, com planeamento para a sua redução (diminuindo o tempo de resposta ao pedido de reforma);
- permitindo a redução do horário de trabalho em função da idade do trabalhador sem perda de rendimento em vez da reforma total;
- alargando o direito a férias pagas para estagiários e estagiárias, sendo o cálculo do número de dias de férias pagas proporcional à duração do estágio.  
7. **Reforçar o poder das e dos trabalhadores:**  
- promover novas convenções coletivas de trabalho, alargando o leque de matérias a negociar, e acabar com o regime de caducidade dos instrumentos de regulamentação coletiva de trabalho de forma a diminuir o número de contratos individuais de trabalho;
- garantir uma efetiva representatividade dos trabalhadores nos processos de decisão por alteração do regime das Sociedades Comerciais, de forma a que todas as empresas maiores que uma Pequena ou Média Empresa (PME) tenham obrigatoriamente representantes dos trabalhadores nos seus órgãos sociais executivos;
- ao fomentar empresas partilhadas e cooperativas;
- criando uma Lei que promova e defina a autogestão das empresas, tal como previsto no Artigo 61º da Constituição.  
8. **Proteger o trabalho independente**, ao:  
- estabelecer uma Retribuição Horária Mínima Garantida;
- criar um novo estatuto de proteção do trabalho independente pela Segurança Social;
- ajustar a tabela de retenção para trabalhadores independentes;
- aumentar o valor a partir do qual deixam de estar sujeitos à isenção de IVA e retenção na fonte;
- reforçar a capacidade de negociação coletiva dos trabalhadores independentes que prestem serviços ao mesmo fornecedor.  
9. **Apoiar o microempreendedorismo**, criando hubs criativos que possam dotar o microempreendedor de espaço de trabalho a baixo custo, partilha de recursos, como eletricidade e aquecimento, e/ou serviços de prototipagem (como por exemplo impressão 3D). Criando um regime de microempreendedorismo de contabilidade e fiscal mais leve, que permite ao microempreendedor aliviar custos financeiros.  
10. **Reforçar os apoios sociais,** através do aumento do Indexante de Apoios Sociais (IAS) com aumentos anuais sucessivos e graduais, acima do valor da inflação, que permitam garantir estabilidade na atribuição de diversos apoios sociais. Restabelecimento do acesso ao Rendimento Social de Inserção e do aumento do seu valor, considerando igualmente a majoração dos agregados familiares monoparentais e dos dependentes até aos 6 anos de idade. Aumentar o valor da prestação do abono de família apoiando os agregados com os encargos respeitantes ao sustento e educação de crianças e jovens, especialmente agregados vulneráveis.  
11. **Planear a convergência das pensões de valor reduzido com o salário mínimo nacional até ao final da legislatura**, reduzindo a diversidade de apoios a um único apoio (pensão social do regime não contributivo, pensão paga pela Caixa Geral de Aposentações, pensão social de velhice, entre outras de valores semelhantes), revendo compatibilidade entre apoios e compatibilizando com a atualização e reforço do Indexante de Apoios Sociais (IAS).  
12. **Rever a fórmula de cálculo das pensões da segurança social**, através do fator de sustentabilidade, desagravando este fator de forma a reduzir a penalização antecipada.  
13. **Garantir justiça a ex-combatentes**,  
- garantindo que a sua pensão não seja inferior ao valor do ordenado mínimo nacional e assegurando um complemento vitalício de pensão;
- criando a Comissão Nacional de acompanhamento dos Antigos Combatentes, com orçamento e estrutura próprios, e que tenha como missão garantir o reconhecimento do país às pessoas que o serviram, através da resposta às suas necessidades específicas e das suas famílias e também através da preservação da sua memória e da sua história;
- melhorando a implementação do Estatuto do Antigo Combatente, nomeadamente tornando o Cartão de Antigo Combatente também num cartão virtual e garantindo uma melhor resposta às solicitações com o reforço dos meios para o Balcão Único de Defesa e com a efetivação do protocolo com a ANAFRE- Associação Nacional de Freguesias;
- providenciando os meios para que os processos de qualificação de ex-combatentes como Deficientes das Forças Armadas ou Pensionistas de Invalidez sejam mais céleres;
- retomando a comparticipação a 90% dos medicamentos para Antigos Combatentes;
- tornando mais simples e célere o acesso à Assistência na Doença aos Militares;
- reforçando o orçamento para a Rede Nacional de Apoio (RNA) aos militares e ex-militares portadores de perturbação psicológica crónica resultante da exposição a fatores traumáticos de stress durante a vida militar, que também presta apoio às famílias;

[Documento 15]
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > Desenvolvimento Ecológico, Cooperativo e Solidário > Por isso defendemos:
### Por isso defendemos:  
1. **Promover um Novo Pacto Verde** - _Green New Deal_ - um plano estratégico para uma economia diversa, verde e justa ao qual está associado um plano de investimento ambicioso, para Portugal e para a Europa, que identifique os setores prioritários, as infraestruturas necessárias para as próximas décadas e aposte nos setores-chave de valorização dos recursos e competências do país para fazer face à emergência climática e ecológica, assegurando a solidez da qualificação e da formação da população, a criação de empregos verdes e estáveis mediante uma transição laboral justa e participada, e assegurando a coesão territorial pela redução da fratura entre centro e periferias.  
2. **Aumentar as fontes de receitas do Estado e fomentar a redistribuição** através:  
- do combate à evasão e elisão fiscais, ao recurso a _offshores_ e outros mecanismos de planeamento fiscal agressivo responsáveis por perdas significativas para economia nacional, através da implementação das medidas previstas no Plano Estratégico de Combate à Fraude e Evasão Fiscal e Aduaneira e do acompanhamento permanente e aplicação das recomendações das instituições e grupos de trabalho supranacionais e intergovernamentais sobre a matéria;
- do aumento das taxas do adicional de solidariedade sobre o setor bancário;
- do reforço da tributação do património imobiliário que não se destine a habitação permanente e das grandes fortunas;
- da redução do peso dos impostos sobre os rendimentos do trabalho na receita fiscal total, e aumentando a contribuição dos impostos sobre a riqueza e rendimentos capitais;
- da introdução do imposto sucessório para grandes heranças e grandes doações, que venha a constituir uma "herança social" - transferência direta atribuída quando atingida a maioridade;
- do aumento da tributação das transações financeiras, a partir de determinado limite, das emissões de carbono e da produção de resíduos;
- da regulação e revisão da tributação de criptomoedas;
- da introdução da progressividade nos impostos sobre os rendimentos do capital, nomeadamente através da introdução de escalões na taxa liberatória ou da obrigatoriedade de englobamento em sede de IRS;
- do aumento a consignação de IRS de 0,5% para 1%, permitindo ainda que um máximo de 4 entidades diferentes possam ser beneficiadas pelo valor da consignação;
- criação de uma sobretaxa extraordinária progressiva, a cobrar em sede de IRC, sobre o lucro de empresas nos setores da energia, da banca, seguros, imobiliário, da distribuição alimentar e do armamento que apresentem um lucro apurado igual ou superior a um milhão e quinhentos mil euros;
- do aumento do valor de referência para isenção da contribuição a pagar pela entidade contratante de trabalhadores independentes, de forma a proteger associações, cooperativas e micro empresas.  
3. **Assegurar a justa tributação das grandes empresas multinacionais** que, recorrendo a mecanismos de planeamento fiscal agressivo evitam pagar impostos nos países onde geram uma parte significativa dos seus lucros, optando por declarar os seus rendimentos em jurisdições com regimes fiscais mais favoráveis e acabando a estar sujeitas a taxas efetivas sobre os seus lucros muito inferiores àquelas a que estariam sujeitas em Portugal ou que outras empresas até de menor dimensão pagam efetivamente.  
4. **Assegurar o Estatuto para os Bens Públicos, a nível nacional e europeu**, identificando e categorizando todos os bens de que depende a população em geral e o interesse comum da sociedade - como são exemplo a água potável, as grandes infraestruturas e as grandes empresas de transporte que são a base do sistema de mobilidade, o serviço de rádio e televisão público, os CTT, a REN ou a Caixa Geral de Depósitos - e fixando os princípios de uma gestão dos bens públicos, com imposição legal de limites explícitos à sua mercantilização e/ou à sua privatização. De acordo com estes limites, os setores-chave identificados devem ser preservados ou revertidos para o Estado, suspendendo as privatizações, as concessões e as parcerias público-privadas que os ultrapassem, colocando-os ao serviço da comunidade e do desenvolvimento económico, ecológico e solidário.  
5. **Separar a banca comercial da banca de investimento**, para que o risco da atividade especulativa não recaia sobre o Estado nem sobre depositantes.  
6. **Promover a banca ética e solidária**, alterando o quadro legislativo para a diferenciar da categoria das "sociedades financeiras de microcrédito" e reduzindo os requisitos de capital necessários.  
7. **Fomentar a economia local, solidária e colaborativa**:  
- apoiando a criação e o desenvolvimento de cooperativas e de empresas autogeridas pelos trabalhadores que garantam o desenvolvimento ecológico e sustentável legislando o direito à autogestão previsto constitucionalmente, nomeadamente implementando uma versão nacional da lei Marcora - que, em caso de falência de uma empresa privada, permite aos trabalhadores receber o valor dos subsídios de desemprego a que teriam direito como capital para recuperarem o negócio transformando-o numa cooperativa viável -, bem como outra legislação italiana, uruguaia e francesa para fortalecer o setor cooperativo;
- estimular a criação de moedas locais e complementares ao euro, que permitam trocas locais entre empresas e cidadãos, sem valor nos circuitos financeiros e sem encorajamento à acumulação nem à especulação;
- adaptar a lógica das compras públicas centralizadas, substituindo-as por compras do Estado nos mercado locais onde os serviços se encontram instalados para promover o comércio local e, indiretamente, o emprego nas zonas de baixa densidade populacional, com exceção nos casos em que as compras públicas centralizadas conferem poder negocial ao Estado face a grandes grupos económicos ou a fornecedores únicos;

[Documento 16]
  Secção: Contrato com o Futuro: Programa do LIVRE às eleições legislativas de 2024 > **Emergência Climática e Energia** > Por isso defendemos:
### Por isso defendemos:  
1. **Declarar a emergência ecológica nacional**, atribuindo ao desafio de combate às alterações climáticas e à perda de biodiversidade a urgência civilizacional que efetivamente representam, de forma inequívoca e mobilizadora.  
2. **Fazer cumprir a Lei de Bases do Clima**, aprovada em 2021 e cuja aplicação está atrasada, com a criação de orçamentos de carbono, com a revisão do regime jurídico dos hidrocarbonetos, com a elaboração de um relatório sobre o impacto climático da legislação vigente, com a avaliação do risco climático dos ativos financeiros ou a criação do Portal de Ação Climática e reforçando as competências e as condições de trabalho do Conselho para a Ação Climática.  
3. **Reivindicar a adesão dos Estados-Membros da União Europeia à Neutralidade Carbónica no máximo em 2040**, em cumprimento e antecipando a estratégia para a neutralidade carbónica da União Europeia mas incluindo a consideração do transporte aéreo e marítimo na pegada carbónica dos países.  
4. **Assumir uma redução de 65% das emissões nacionais de gases com efeito de estufa até 2030**, promovendo igual esforço internacional, ultrapassando a meta de até 55% assumida pelo governo no PNEC 2030 e dando resposta aos cenários que apontam a necessidade desta aceleração para manter o aumento da temperatura média global abaixo dos 1,5 °C em relação ao período pré-industrial.  
5. **Assumir uma redução do consumo energético verdadeiramente eficaz**, indo para além dos 35% atualmente assumidos para 2030 e promovendo uma estratégia global de redução do consumo, assente numa capacidade industrial com baixa intensidade em carbono e complementada com educação para o consumo sustentável.  
6. **Dar prioridade ao aumento da eficiência energética**, enquadrada num renovado Plano Nacional para a Eficiência Energética (PNAEE) e adotando uma metodologia baseada em indicadores de intensidade energética. O aumento de eficiência irá abranger todos os setores de atividade, incluindo a indústria, os transportes, as habitações, os equipamentos, entre outros.  
7. **Promover uma mobilidade mais eficiente**, implementando políticas de mobilidade baseadas na redução da necessidade das deslocações, no desincentivo do uso de automóvel individual, na aposta nos transportes públicos e partilhados, e na redução acentuada do uso de combustíveis fósseis e otimização destes.  
8. **Fomentar a Neutralidade Carbónica dos Serviços públicos** até 2030, através da eletrificação de todas as frotas de veículos, nas diferentes categorias, em todas as administrações Municipais, Regionais e Nacionais, apostando no aproveitamento fotovoltaico / solar térmico em todo o edificado público e compensando a pegada carbónica de todos os serviços.  
9. **Garantir edifícios e equipamentos mais eficientes**, reforçando o programa 3C - Casa, Conforto e Clima e incentivando a renovação e reabilitação dos edifícios atuais, sobretudo do respetivo isolamento térmico e climatização passiva, bem como a substituição dos equipamentos pouco eficientes em fim de vida. Implementar a revisão do Regulamento de Eficiência Energética nos Edifícios de Habitação e de Serviços e reformar o atual sistema de certificação energética para que os certificados reflitam efetivamente o desempenho energético do edificado. Rever também as regras de rotulagem energética dos equipamentos e atribuindo os apoios necessários a cidadãos, empresas e instituições, de forma a reduzir o período de retorno do investimento. Melhorar a eficiência energética dos edifícios públicos e equipar as infraestruturas públicas de equipamentos de produção, distribuição e armazenamento de energia renovável, quando relevante.  
10. **Apostar de forma verdadeiramente ambiciosa e continuada nas fontes de energia renováveis**, indo para além das metas assumidas atualmente e que colocam a introdução de renováveis no consumo final bruto de energia em apenas 47% para 2030, ambicionando muito mais do que os 20% assumidos para o setor dos transportes; concretizando 100% de renováveis na eletricidade consumida em Portugal em 2030.  
11. **Cessar os incentivos às fontes de energia com elevado impacto na biodiversidade**, cancelando a atribuição de subsídios à construção de novas barragens ou infraestruturas associadas.  
12. **Incentivar o desenvolvimento da indústria solar fotovoltaica e solar térmica**, dando especial relevo à produção descentralizada de energia para autoconsumo e à ocupação preferencial de superfícies urbanas, através da redução de IVA na aquisição de equipamentos solares, reforçando os programas de apoio à aquisição de equipamentos e financiando a ligação à rede de sistemas de Unidades de Produção para Autoconsumo.  
13. **Promover as Comunidades de Energia Renováveis (CER) e democratizar o acesso à produção de energia elétrica a partir de fontes renováveis:**  
- incentivando a formação de cooperativas de produtores , bem como as parcerias entre cidadãos e autarquias e prestando apoio às parcerias já existentes, nomedamente promovendo o fornecimento dos edifícios públicos através destas cooperativas, sempre que possível;

## Pessoas-Animais-Natureza
[Documento 17]
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por uma economia do bem-estar que dê prioridade às pessoas e à sustentabilidade ambiental
a manutenção do sistema terrestre, por isso, no futuro, a conservação da natureza tem de ser uma atividade económica.  
A urgência de novas métricas de progresso exige a superação do paradigma de desenvolvimento baseado exclusivamente no crescimento económico pelo paradigma do desenvolvimento social sustentável. Exige também o decrescimento das externalidades: a economia deverá intervir na mudança climática, desincentivando o seu crescimento à custa da vida planetária. Não se trata de reduzir o rendimento ou emprego, trata-se, sim, de superar uma economia extrativista e linear por uma economia circular baseada no consumo consciente, no comércio justo e numa banca pública de fomento, a Banca Ética e das Finanças Solidárias.  
Como corolário, o ministério da Transição Climática e da Economia deve pugnar pelo estabelecimento de um rendimento de dignidade e cidadania, capaz de promover a empatia económica, a justiça social e o bem-estar para empregados/as e desempregados/as.  
Com isto, o PAN irá:  
- Concentrar os apoios públicos ao investimento em projetos que:  
- Estejam direcionados para a descarbonização, a mitigação e adaptação às alterações climáticas  
- Acelerem a digitalização da economia, melhorando a produtividade, o ambiente, a coesão territorial e a conciliação da vida profissional e familiar;  
- Apoiar clara e fortemente a economia circular, seja através de incentivos ao investimento, seja através de legislação que contrarie a economia linear;  
- Definir como pilares de democracia económica a igualdade de género e a coesão territorial;  
- Criar um fundo nacional de transição justa que permita assegurar a reintegração profissional dos/ das trabalhadores/as afetados/as pela crise climática;  
- Apoiar a fixação de migrantes digitais nas áreas de baixa densidade populacional;  
- Subsidiar o desenvolvimento de alternativas proteicas de base vegetal na indústria alimentar e criar um plano de ação nacional e fundo para as proteínas vegetais e alternativas;  
- Criar um projeto-piloto de implementação de um Rendimento de Dignidade e Cidadania (RDC);  
Relativamente à fiscalidade para as famílias e as empresas, o PAN irá:  
- Defender o englobamento de todas as categorias de rendimento, fazendo jus ao preceito constitucional do "imposto único e progressivo, tendo em conta as necessidades e os rendimentos do agregado familiar", revendo, no entanto, as Deduções Específicas, nomeadamente as dos Rendimentos Prediais que passariam a incluir depreciações e encargos financeiros; temporariamente, manter- -se-iam taxas especiais apenas para os arrendamentos para habitação permanente;  
- Aprovar, no início da legislatura, um programa de emergência fiscal, que garanta:  
- A reposição do IVA Zero, com vigência até ao dia 30 de setembro;  
- Revisão dos limites dos escalões de IRS, atualizando-os para o valor que teriam se desde 2021 se considerasse a inflação realmente verificada;  
- Defender em todos os OE a atualização de todos os limites dos escalões do IRS pelo exato aumento da inflação do ano anterior;  
- Criar um regime especial de isenção contributiva aplicável aos jovens trabalhadores-estudantes que aufiram rendimentos anuais de trabalho não superiores a 14 remunerações mínimas mensais garantidas, sem comprometer o posterior deferimento de isenção contributiva de 12 meses à Segurança Social aquando do início do respetivo percurso profissional;  
- Alargar o regime do IRS Jovem por forma a que dure mais 2 anos e garanta uma redução de imposto de 15% no penúltimo (6.º) ano e de 5% no último (7.º) ano;  
- Alargar o acesso ao IRS Jovem a todos os jovens, mesmo que englobados num agregado familiar;  
- Atualizar a dedução específica da categoria A (trabalho dependente) e da categoria H (Pensões), fixada em 4104€ e inalterada desde 2015, para 4915€ em 2024 e pela taxa de inflação nos anos seguintes;  
- Alargar o mínimo de existência, valor consagrado em CIRS como não devendo estar sujeito a IRS, a todos os rendimentos;  
- Rever as rubricas "61 — Agricultores e trabalhadores qualificados da agricultura e produção animal, orientados para o mercado" e "62 — Trabalhadores qualificados da floresta, pesca e caça, orientados para o mercado", no quadro das atividades de elevado valor acrescentado que beneficiam do Regime Especial dos Residentes Não Habituais, mantendo apenas os/as agricultores/as e trabalhadores/as qualificados da agricultura e floresta;  
- Criar uma nova categoria de dedução à coleta em sede de IRS designada "Sustentabilidade", com teto máximo de 500€ para as despesas com a aquisição de bicicletas, painéis solares, entre outros, no montante correspondente a 15% do valor suportado;  
- Criação de um eco-voucher anual de 250€, isento de impostos, enquanto possível benefício oferecido pelas empresas para compras em produtos que contribuem para a sustentabilidade  
- Baixar o IVA aplicável à prestação de serviços médico-veterinários para a taxa reduzida;  
- Reduzir para a taxa mínima de IVA a alimentação dos animais de companhia, à semelhança do que já acontece com a dos restantes animais;  
- Revogar a isenção de IVA nas prestações de serviços de artistas tauromáquicos;  
- Abolir a redução da taxa de IVA da "Canicultura" e "Criação de animais para experiências de laboratório";  
- Reduzir a taxa de IVA para métodos alternativos à utilização de animais em experiências;  
- Passar as rubricas "Adubos, fertilizantes e corretivos de solos" e "Produtos fitofarmacêuticos" da taxa reduzida para a taxa intermédia, à exceção dos orgânicos;  
- Conceder benefícios fiscais às empresas que participem em Programas de Emprego para Reclusos/as, de forma a alargar o programa de regime aberto ao exterior;  
- Eliminar a isenção para as empresas produtoras de energia elétrica no que diz respeito ao Imposto Sobre os produtos Petrolíferos e energéticos (ISP);  
- Refletir na Taxa de Recursos Hídricos (TRH) das indústrias e agropecuária o custo real da utilização de recursos;  
- Estender a aplicação da Taxa de Carbono a outros setores poluentes, nomeadamente da pecuária;  
- Rever os produtos abrangidos pelo imposto especial sobre o consumo (IEC) respeitantes aos teores de açúcar, gorduras saturadas e sal dos alimentos;  
- Reduzir a taxa de IRC em 1 ponto percentual ao ano, atingindo 17% no final da legislatura;  
- Revisão das Tributações Autónomas em respeito pelo preceito constitucional de tributar as empresas pelo seu rendimento real. Iremos assim reduzir anualmente as taxas em 1/4 do seu valor, sendo eliminadas até ao final da legislatura, com exceção da taxa sobre despesas não documentadas, voltando ao modelo inicial de não aceitação de determinados gastos para efeitos fiscais, ou limitando o seu valor;  
- Abolir o pedido de devolução de apoios à criação do próprio emprego por parte dos/as que, quando desempregados/as, criaram a sua empresa e esta não sobreviveu até ao fim do período contratual;  
- Majorar em 100% nos gastos em sede de IRC com a remuneração das horas dispensadas aos trabalhadores-estudantes;  
- Premiar em sede fiscal as empresas que promovam boas práticas ambientais e sociais, assegurando um aumento dos valores de dedução de despesas que visem assegurar a transição energética, promover a mobilidade sustentável dos seus funcionários ou garantir medidas de apoio à família destinadas aos funcionários (como por exemplo o pagamento de subsídios para despesas escolares e de creche); e  
- Reforçar em sede de IRC os incentivos para que as empresas que suportem o custo das propinas de licenciaturas, mestrados ou doutoramentos dos seus trabalhadores, de forma a potenciar a aprendizagem ao longo da vida e a diversificar os perfis de acesso ao ensino superior.  
Para assegurar uma gestão das finanças públicas que dê prioridade às pessoas e à sustentabilidade ambiental, o PAN irá:  
- Ter como objetivo o déficit zero, numa perspetiva de justiça intergeracional, sem prejuízo de não cumprimento em situações excepcionais;  
- Empreender uma consulta pública, de prazo alargado, sobre o futuro a dar à TAP, que não exclua a manutenção de uma participação relevante do Estado na empresa, considerando a injeção de dinheiros públicos ocorrida e o ativo estratégico para o país que a empresa representa, e que o resultado dessa consulta seja sujeito à análise técnica do Conselho de Finanças Públicas sobre o impacto orçamental de tal decisão;  
- Promover, através da Assembleia da República, a melhoria no acompanhamento e fiscalização da despesa pública e do desempenho orçamental do Governo;  
- Criar mecanismos de participação da Assembleia da República na nomeação dos membros do conselho superior do conselho de finanças públicas;  
- Assegurar que qualquer financiamento público da banca, via Fundo de Resolução, tenha de ser aprovado pela Assembleia da República, mediante a prévia realização de uma avaliação técnica independente dos impactos orçamentais de tal financiamento feita pelo Conselho de Finanças Públicas e pela Unidade Técnica de Apoio Orçamental;  
- Empreender urgentemente a renegociação das Parcerias Público-Privadas no setor rodoviário, tendo em vista a revisão das cláusulas abusivas e a redução significativa dos encargos para o erário público;  
- Garantir que a celebração de qualquer nova Parceria Público-Privada tenha de ser obrigatoriamente precedida de um parecer técnico do Conselho de Finanças Públicas, que avalie o respetivo impacto na sustentabilidade de médio e longo prazo das finanças públicas e certifique a viabilidade económica e financeira do contrato de Parceria, com vista a assegurar a eficiência na afetação dos recursos públicos e a salvaguarda responsável de tais recursos;  
- Desenvolver regulamentação própria com vista à instalação da Banca Ética e das Finanças Solidárias em Portugal;

[Documento 18]
  Secção: agenda 24-28 COMPROMISSO COM AS PESSOAS, OS ANIMAIS E A NATUREZA > Por habitação para tod@s num país mais verde e justo
Na Legislatura que agora termina, as medidas tomadas pelo Governo foram insuficientes, com promessas de casas que nunca saíram do papel e apoios financeiros que deixam de fora 80% dos contratos de crédito habitação e 84% dos contratos de arrendamento. Contudo, o PAN conseguiu algumas avanços importantes em matéria de habitação, com a aprovação de medidas como pôr fim à cobrança da comissão bancária para o processamento da prestação, alargar a isenção de IMI para quem compra casa própria de 3 para 5 anos, aumentar em 100 euros o valor de dedução de rendas em IRS, assegurar  
a realização de um inventário do património imobiliário do Estado com aptidão para uso habitacional ou reforçar o financiamento para programas de Housing First.  
O PAN quer continuar a avançar pela causa do direito à habitação, com medidas de emergência (designadamente de âmbito fiscal) que ajudem as famílias a pagar a sua renda ou prestação ao final do mês, com o aumento do investimento público na habitação e com a criação de uma rede de habitações públicas que privilegie a reabilitação, assegurando medidas de proteção do património cultural, a eficiência ambiental e a defesa dos valores da inclusão e do espírito de comunidade.  
Neste contexto, o PAN irá:  
- Aprovar um regime de concessão de crédito bonificado à habitação para jovens para os/as jovens dos 18 aos 35 anos;  
- Assegurar uma redução de despesas adicionais na compra de casa própria a jovens dos 18 aos 35 anos, por via da atribuição de um desconto de 25% nos emolumentos das escrituras e dos atos de registo respeitantes à aquisição e à hipoteca dos imóveis adquiridos, de isenção de imposto de selo e com a criação de um regime de IMT Jovem que isente deste imposto as casas próprias com valor patrimonial tributário até 110 mil euros;  
- Rever o Programa Porta 65, de forma a aumentar os valores de renda máxima, a robustecer a respetiva dotação orçamental e a apoiar as despesas iniciais, como cauções e primeira renda e aumentar o seu valor;  
- Reduzir significativamente o IRS dos senhorios que promovam o arrendamento acessível e que atualizem os valores das rendas abaixo dos valores da inflação;  
- Apostar em programas de apoio através de benefícios fiscais aos/às proprietários/as que tenham arrendamento acessível (apartamento, quartos, coliving) para estudantes a preços abaixo da média praticada na área onde se localizem;  
- Garantir a todas as famílias a dedutibilidade de gastos com a prestação de crédito à habitação em sede de IRS;  
- Aprovar um regime transitório, com vigência limitada ao ano de 2024 e eventualmente prorrogável para 2025, de isenção de execução de penhora de bens imóveis para a satisfação de garantia real de créditos hipotecários;  
- Limitar o pagamento de remunerações acionistas e de bónus por bancos que tenham recebido apoios financeiros públicos entre 2008 e 2023, obrigando a que tais valores sejam canalizados para medidas tendentes a mitigar os efeitos do incremento dos indexantes de referência de contratos de crédito para aquisição ou construção de habitação própria permanente;  
- Dotar todos os edifícios públicos de meios de produção de energia, até 2030;  
- Garantir que as candidaturas a programas de apoio de eficiência energética do Fundo Ambiental sejam aprovadas antes da realização da despesa, ficando cativa a verba para aquela candidatura;  
- Reduzir para 6% o IVA das operações que visem assegurar a eficiência hídrica das habitações;  
- Prosseguir e aumentar o investimento de protocolos celebrados pela Segurança Social para a concretização de projetos inovadores que visem a implementação de respostas de suporte habitacional a pessoas em situação de sem-abrigo, nomeadamente no que respeita a respostas sociais de Housing First;  
- Alargar a oferta de habitação pública a preços acessíveis;  
- Reforçar o investimento na reabilitação e construção de habitação pública para arrendamento acessível, pugnando pela mobilização do património imobiliário do Estado e municipal;  
- Converter imóveis públicos devolutos em habitação para jovens, nomeadamente estudantes, podendo prolongar-se a permanência na habitação por um ano após o término dos estudos, com rendas enquadradas no valor das residências universitárias;  
- Garantir que em todos os projetos de habitação pública há sempre uma percentagem destinada a jovens e a alojamento estudantil;  
- Criar um complemento de bolsa para fazer face ao aumento de custos com o alojamento;  
- Implementar novos programas de apoio financeiro com vista à colocação de imóveis devolutos no mercado de arrendamento, com rendas condicionadas, apoiando obras de conservação e de atualização dos padrões de habitabilidade e conforto;

## Partido Comunista Português
[Documento 19]
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 2 DESENVOLVIMENTO ECONÓMICO > 2.3. Políticas-chave > 2.3.1. Finanças públicas – uma justa política fiscal e uma dívida pública sustentável > Medidas para uma política de justiça fiscal
###### Medidas para uma política de justiça fiscal  
- IRS: aprofundar a progressividade do imposto; reduzir as taxas de IRS para os rendimentos mais baixos e intermédios em três pontos percentuais; actualização anual dos escalões e das restantes deduções à taxa de inflação; elevação do mínimo de existência; actualização do valor da dedução específica, corrigindo a inflação registada desde a última actualização (2010); criação de um novo escalão no IRS com uma taxa nominal de 56% para rendimentos colectáveis superiores a 250 mil euros anuais; englobamento obrigatório de todos os rendimentos em sede de IRS acima dos 80 mil euros anuais; fim do regime de privilégio fiscal dos residentes não-habituais;
- IVA: criação de um cabaz mais alargado de bens essenciais taxados a 6%, incluindo toda a electricidade, o gás natural, o gás de botija, as telecomunicações e todos os produtos para alimentação humana, a par da redução da taxa normal de IVA;
- IMI: redução da taxa máxima de 0,45% para 0,4%; alargamento da isenção do IMI para as famílias de muito baixos rendimentos e com pessoas deficientes; alargamento do Adicional ao IMI para património imobiliário superior a 500 mil euros;
- IRC: aprofundar a progressividade do IRC, criando um novo escalão com uma taxa de 12,5% para MPME para rendimento colectável até 15.000€; simultaneamente, criar um novo escalão de derrama estadual de 14% para as empresas com rendimentos colectáveis superiores a 50 milhões de euros; taxação extraordinária dos lucros da banca, da energia e grande distribuição;
- Rendimentos de capital e património: eliminação de vários benefícios fiscais, isenções, majorações e outros subterfúgios que permitem reduzir artificialmente a base tributária dos grupos económicos, garantindo a tributação em Portugal dos lucros realizados no País; substituição do SIFIDE por um programa de promoção da investigação e desenvolvimento dirigido com base em critérios de interesse público; criação de mecanismos de combate ao planeamento fiscal agressivo e à fraude e evasão fiscais; taxa sobre as transacções financeiras; aplicação de taxa sobre o património mobiliário de valor superior a 500 mil euros (quotas, acções, títulos, depósitos e outros instrumentos financeiros);
- Impostos Especiais sobre o Consumo: acabar com a dupla tributação do IVA em sede de ISP e reverter agravamentos fiscais no âmbito da "fiscalidade verde", como a taxa sobre a compra a granel em sacos de plástico ultraleves; criar um IEC sobre bens e serviços de luxo (exemplos:viaturas de alta cilindrada, iates, jactos, alta costura).

[Documento 20]
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 2 DESENVOLVIMENTO ECONÓMICO > 2.3. Políticas-chave > 2.3.3. Energia: avançar na eficiência e soberania energética
##### 2.3.3. Energia: avançar na eficiência e soberania energética  
Os processos de liberalização e de privatização de sectores energéticos estratégicos para o fornecimento de bens e serviços essenciais à economia e à sociedade, levado a cabo desde há décadas pelos governos do PS, PSD e CDS, conduziu ao fortalecimento de monopólios e à densificação das redes oligopolistas que, baseadas em visíveis posições dominantes, obtêm rendas e lucros crescentes, prejudicam a competitividade nacional, põem em causa a sobrevivência de muitas pequenas e médias empresas, a par do agravamento crítico do custo de vida das famílias portuguesas, como se verifica no caso da electricidade e dos combustíveis fósseis.  
É necessário romper com o actual caminho. É preciso promover a racionalidade e a eficiência na produção/conversão, no transporte e na distribuição, bem como ao nível dos diversos tipos de utilização dos vectores de energia final, sempre no respeito pela sustentabilidade ambiental e socio-económica, e num referencial de soberania energética nacional. O PCP considera necessário:  
- aumentar a utilização racional da energia e da eficiência energética em sistemas reforçados, quantitativa e qualitativamente, de transportes públicos colectivos, nos edifícios (com prioridade para os públicos) e nos diversos sectores produtivos, mormente na indústria (redução da intensidade energética);
- atribuir prioridade à promoção num referencial de cooperação e segurança multilateral – da diversificação das fontes primárias de energia, quer das endógenas, quer das que o País vai continuar a importar;
- a prospecção e cartografia dos recursos para a fileira energética, tanto as fontes primárias de energia renováveis (hidroeléctrica, eólica, solar térmica, fotovoltaica, biomassa, incluindo efluentes e resíduos orgânicos – produção de biogás e biometano –, geotérmica e as exploráveis ao nível do mar) como as não renováveis, bem como dos diversos recursos minerais estratégicos necessários a uma transição energética justa e sustentável;
- as explorações dos recursos referidos devem passar pela transparência de processos políticos e técnico-administrativos, a minimização dos impactes ambientais locais e regionais e a maximização do valor acrescentado em cadeias de tratamento sediadas no País; as suas unidades de exploração devem garantir o aproveitamento racional e sustentável do território nacional (condicionantes ambientais, ecológicas, paisagísticas e de ordenamento do território);
- o reassumir pelo Estado do seu papel de autoridade e de controlo público das principais empresas (EDP, GALP, REN), no aprovisionamento, produção, transporte e comercialização das diferentes formas de energia, e a reorganização das fileiras energéticas, recompondo a cadeia de valor das suas empresas;
- o reforço da base científica e técnica nas novas fileiras tecnológicas de conversão/produção energética e da análise multidisciplinar dos projectos de aproveitamento das fontes renováveis, minimizando os seus impactos e custos no território e na necessidade de infraestruturas de armazenagem de electricidade gerada pela intermitência;
- a revisão completa dos incentivos, subsídios, subvenções não reembolsáveis e outros apoios às empresas produtoras de electricidade, seja no domínio da produção convencional, seja no das energias renováveis, para pôr fim às «rendas excessivas», aos lucros oportunistas trazidos por conjunturas imprevistas ou os devidos ao efeito conjugado das acções monopolistas e oligopolistas e/ou receitas indevidas; o défice tarifário no domínio da electricidade, devendo ser progressivamente diminuído ao nível regulatório, não deverá passar pela exploração privatizada que opera através de otimizações financeiras para proveito empresarial próprio;
- a manutenção dos regimes de tarifas reguladas na electricidade e no gás natural, a redução da taxa do IVA para 6% (electricidade, GN e GPL), a criação de um regime de preços máximos para os diversos tipos de energia bem como regimes de preços bonificados para algumas actividades – agricultura, pescas e transportes.

[Documento 21]
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 2 DESENVOLVIMENTO ECONÓMICO > 2.2. Opções estratégicas > 2.2.4. > As micro, pequenas e médias empresas, no centro do mercado interno
###### As micro, pequenas e médias empresas, no centro do mercado interno  
As MPME devem ser positivamente discriminadas conforme determina a Constituição. Impõe-se prosseguir o caminho visando uma tributação das MPME pelos seus rendimentos reais e a redução dos custos de taxas e das tarifas da energia, comunicações e telecomunicações e seguros; criar a contacorrente Estado/empresas e um IVA de caixa com pagamento após boa cobrança; arrendamento não habitacional com estabilidade contratual em lei autónoma da legislação do arrendamento habitacional; acesso prioritário e simples ao Portugal 2030, fixando para as MPME o valor de 50% dos fundos para empresas e uma política de crédito com instrumentos financeiros e condições – garantias, spreads, comissões – para financiamento da componente própria de candidaturas, investimento ou tesouraria ajustados às MPME; intervenção da Autoridade da Concorrência contra práticas violadoras da concorrência e o abuso dos grupos económicos; pagamento, nos prazos de lei, das dívidas do Estado; nova legislação para o horário de funcionamento, o ordenamento e a regulação do comércio, travando a expansão desenfreada da Grande Distribuição; regulamentação de meios de pagamento bancário para travar abusos e exigências ilegais e conter os seus custos; apoio à transição digital das MPME e face à elevada inflação acumulada actualizar os valores dos limites de Volume de Negócios para classificação da dimensão empresarial e determinação (ou não) de exigências contabilísticas (caso dos inventários); revisão do DL 12/2013 para facilitar o apoio social a micro e pequenos empresários com fecho forçado das empresas; criação de uma «entidade específica» no Ministério da Economia como interlocutor privilegiado; não discriminação do associativismo dos micro e pequenos empresários.  
- A defesa do mercado interno é possível mesmo no âmbito da integração comunitária, nomeadamente, com outro nível de fiscalização das importações, impondo-lhe critérios mínimos de qualidade e técnicos; estabelecendo mecanismos que privilegiem o consumo da produção interna e travem a importação de bens de consumo, alimentares e duradouros; com o combate ao dumping e às políticas de liberalização do comércio por via da União Europeia.

[Documento 22]
  Secção: Programa Eleitoral do PCP: Política patriótica e de esquerda – Soluções para um Portugal com futuro > 2.ª PARTE > CAPÍTULO 4 ELEVAR A QUALIDADE DE VIDA. INVESTIR NOS SERVIÇOS PÚBLICOS, CUMPRIR AS FUNÇÕES SOCIAIS DO ESTADO > 4.2 Mais e melhor Segurança Social para todas as gerações > 4.2.5 Regime não contributivo da Segurança Social: elevar os valores das prestações não contributivas > Proposta do PCP **Valorização das Pensões Mínimas**
###### Proposta do PCP **Valorização das Pensões Mínimas**  
|                                                                                            |                         |                                |                                      |                             |                         |
| ------------------------------------------------------------------------------------------ | ----------------------- | ------------------------------ | ------------------------------------ | --------------------------- | ----------------------- |
| Regime Geral Valor mínimo das pensões de invalidez e velhice — número de anos de descontos | Valor actual (em euros) | Actual % de Indexação ao IAS\* | Proposta do PCP para 2024 (em euros) | Valor do aumento (em euros) | % de Indexação ao IAS\* |
| inferior a 15 anos                                                                         | 319.31                  | 62.7                           | 325.93                               | + 6.62                      | 64                      |
| de 15 a 20 anos                                                                            | 335.09                  | 65.8                           | 341.20                               | + 6.11                      | 67                      |
| de 21 a 30 anos                                                                            | 369.72                  | 72.6                           | 381.95                               | + 12.22                     | 75                      |
| superior a 30 anos                                                                         | 462.41                  | 90.8                           | 468.52                               | + 6.11                      | 92                      |
| 36 a 40 anos                                                                               |                         |                                | 509.26                               | + 46.85                     | 100                     |
| superior a 40 anos                                                                         |                         |                                | 555.09                               | + 92.69                     | 109                     |  
\* Valor do IAS em 2024 – 509,26€ Indexação ao IAS das Pensões e de Outras Prestações Sociais, a que se refere o art.º 7.º do Dec.Lei n.º 53-B/2006

## Partido Socialista
[Documento 23]
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **1.ª MISSÃO:** UMA ECONOMIA EM TRANSFORMAÇÃO ASSENTE EM CONTAS EQUILIBRADAS > 4. Uma fiscalidade inteligente e seletiva
#### 4. Uma fiscalidade inteligente e seletiva  
Embora o salário represente a maior fatia do rendimento familiar disponível, o Estado influencia este rendimento, seja intervindo através da fiscalidade, seja através da provisão de serviços públicos e da prestação de apoios sociais.  
No plano da fiscalidade, o debate público centrou- -se nos últimos anos no aumento da "carga fiscal", que subiu de 34,4% em 2015 para 36% em 2022 - um aumento mais influenciado pelo crescimento das contribuições sociais (que cresceram 53%, fruto do aumento do emprego) do que dos impostos diretos (cresceram 33%) ou dos indiretos (cresceram 39%). Apesar deste aumento, a carga fiscal em Portugal mantém-se bem abaixo da média europeia (de acordo com os últimos dados disponíveis, em 2022 a carga fiscal em Portugal era de 36% e a média europeia de 40,3%).  
Na realidade, os governos do PS baixaram várias vezes diferentes impostos. No IRS, foram feitas várias descidas de taxas, com a reformulação e aumento do número de escalões e aumentando deduções várias (com filhos ou com despesas de arrendamento, por ex.), o que resultou numa devolução de €2 mil milhões de receita do IRS até 2023, a que se somam os cerca de €1,3 mil milhões da redução de receita inscrita no OE2024. No IRC, foi extinto o fim do pagamento especial por conta, foram reduzidas as taxas para as PME, foram criados incentivos para empresas que investem e que se capitalizam, e foram reduzidas as taxas de tributação autónomas das viaturas ao serviço das empresas. No IVA, as descidas mais emblemáticas ocorreram na restauração e na eletricidade.  
É importante notar que, para além dos ângulos diferentes a partir dos quais como esquerda e direita abordam o tema da justiça social na tributação, há pelo menos mais duas formas que distinguem o PS dos partidos à sua direita neste tema.  
Por um lado, o PS avalia o espaço orçamental para reduzir impostos tendo em conta o impacto que isto tem sobre duas outras variáveis fundamentais: a restrição orçamental existente e os objetivos de investimento em serviços públicos e em infraestruturas; enquanto a direita parece ver a redução de impostos como um fim em si.  
Por outro lado, enquanto os partidos de direita preferem descidas de impostos cegas e transversais, o PS olha para a fiscalidade como um instrumento de política pública, indutora ou desincentivadora de comportamentos de trabalhadores e consumidores, o que exige uma utilização muito mais seletiva - e inteligente - dos diferentes impostos.  
Assim, sem prejuízo de continuar a procurar formas de aumentar o rendimento das famílias por via fiscal ao longo da legislatura, o PS compromete-se a:  
- No IRS:  
- **reforçar a redução do IRS para a classe média,** dentro da margem orçamental, diminuindo as taxas marginais;
- **atualizar os limites dos escalões de acordo com a taxa de inflação,** impedindo que os contribuintes vejam a sua tributação aumentar por este efeito;
- **alargar o "IRS Jovem" a todos os jovens,** independentemente do nível de escolaridade atingido, por uma questão de justiça e coerência interna à medida;
- **aumentar a despesa dedutível com arrendamento em €50** por ano até atingir os €800 em 2028, aliviando as familias com esta despesa fundamental.  
- No IRC:  
- **reduzir em 20% as tributações autónomas sobre viaturas das empresas,** diminuindo o nível de tributação sobre a esmagadora maioria das empresas.  
- No IVA:
- **devolver em às IRS às famílias** com menores rendimentos parte do IVA suportado em consumos de bens essenciais, incluindo às famílias que não pagam IRS;
- **aplicar a taxa de 6%** aos primeiros 200 kWh de energia elétrica consumida em cada mês (duplicando os atuais 100 kWh), ou de 300 kWh mensais, no caso das famílias numerosas (duplicando os atuais 150 kWh), numa medida essencial de combate à pobreza energética.

[Documento 24]
  Secção: PLANO DE AÇÃO PARA PORTUGAL INTEIRO 2024 > INTRODUÇÃO > **5.ª MISSÃO:** UM PORTUGAL CENTRAL NA EUROPA E NO MUNDO > 1. Uma participação solidária, exigente e propositiva na União Europeia > 1.4.
##### 1.4.  
Quanto à governação económica da União Europeia, Mercado Único e Política Comercial, incluindo matérias como a reindustrialização da UE, o Pacto Ecológico Europeu, a transição digital e a soberania energética, o PS propõe:  
- Acompanhar atentamente a aplicação das novas regras de governação económica da UE, prosseguindo o objetivo da gradual e sustentada redução da dívida;  
- Defender a entrada em vigor das novas regras do Pacto de Estabilidade e Crescimento num calendário útil para uma transição tranquila entre o atual e o novo quadro, assegurando a flexibilidade das atuais regras após a desativação da cláusula de escape;  
- Envidar esforços para a adoção de um mecanismo europeu permanente de resposta a crises, de natureza contracíclica, que aumente a resiliência económica da UE;  
- Defender a criação de uma Capacidade Orçamental Permanente de Investimento ao nível europeu, que suceda ao NGEU após 2026 e que continue a apoiar os países nos investimentos para a realização das prioridades europeias;  
- Completar a União do Mercados de Capitais, garantindo novos e diversificados instrumentos de financiamento da economia europeia e concluir a União Bancária, com a aprovação do seu terceiro pilar, relativo à criação de um Sistema Europeu de Garantia de Depósitos;  
- Assegurar o cumprimento do Acordo Institucional para a criação de novos recursos próprios da UE que permitam amortizar a dívida da União, evitando a pressão sobre o próximo Quadro Financeiro Plurianual, conferindo à UE a capacidade de responder adequadamente às crescentes tarefas e responsabilidades que lhe vão sendo cometidas;  
- Participar ativamente nas negociações do próximo Quadro Financeiro Plurianual, no âmbito do qual devem ser previstos mecanismos europeus que, após o término dos PRR em 2026, promovam e financiem o investimento conjunto em áreas de valor acrescentado europeu (como a transição climática ou a segurança e defesa) e em preocupações comuns aos povos europeus (como a habitação);  
- Implementar a taxa mínima de IRC, à luz do acordo global para tributar as grandes multinacionais, não aceitando o adiamento dos prazos de aplicação;  
- Defender uma política comercial da UE assente em acordos comerciais e de investimento equilibrados para ambas as partes, com cláusulas relativas ao trabalho forçado, ao trabalho infantil, ao dumping social e ambiental, tornando esses acordos em instrumentos de regulação da globalização, no respeito dos princípios da Organização Mundial do Comércio, com particular empenho na conclusão do Acordo entre a UE e o Mercosul;  
- Apoiar o Plano Industrial do Pacto Ecológico e o desígnio da reindustrialização da União, contribuindo ativamente para traduzir as prioridades quanto ao fabrico de tecnologias limpas e ao aprovisionamento de matérias-primas críticas, entre outros;  
- Combater uma excessiva flexibilização das regras sobre ajudas de Estado, precavendo o desequilíbrio entre países grandes e pequenos no seio do mercado único;  
- Assegurar que as transições em curso se fazem de forma socialmente justa, devidamente programadas, compensando as populações mais afetadas, reconvertendo os trabalhadores para a nova economia através de programas de requalificação e reforçando os recursos e valências do Fundo para a Transição Justa, do Fundo Europeu de Ajustamento à Globalização e do Fundo Social para a Ação Climática;  
- Avançar na concretização do Pacto Ecológico Europeu e acompanhar cuidadosamente a transposição do pacote legislativo que o materializa, em diálogo com todas as partes envolvidas – muito em particular com o setor agroflorestal e alimentar – de modo a não alienar o apoio popular a esta causa transversal à humanidade;  
- Prosseguir os esforços de mitigação das alterações climáticas e investir decididamente na adaptação aos seus efeitos, seja na gestão florestal e na prevenção dos fogos rurais, seja na resiliência hídrica e na definição de estratégias para lidar com a crescente escassez de água, por exemplo através da adoção de um programa ReWaterEU;  
- Envidar esforços para uma União da Energia, capaz de alcançar a soberania energética e a neutralidade climática da Europa;  
- Acelerar a interligação energética entre Estados- -Membros, tanto de eletricidade como de gás, e em especial de gases renováveis, a fim de instituir uma União da Energia que garanta preços mais baixos e uniformes e uma maior segurança de abastecimento a todos os europeus;  
- Apoiar o escrutínio das atividades das grandes plataformas digitais, evitando abusos de posição dominantes, combatendo a desinformação e sancionando a propagação de conteúdos ilegais;  
- Apoiar a UE na conceção e na implementação de legislação ambiciosa que enquadre os serviços e os mercados digitais, os espaços de dados europeus e a inteligência artificial, de modo a tirar partido das imensas potencialidades destas transformações, acautelando os nossos valores fundamentais e garantindo um ecossistema digital justo e plural.

</details>

## item-12

**Question:** Qual é a taxa única de IRS proposta pela Iniciativa Liberal?

**Answer:**

A **Iniciativa Liberal (IL)** propõe a implementação de uma **taxa única de IRS** (também referida como *flat tax*), cujos detalhes estruturais são os seguintes:

• A proposta prevê a substituição do atual sistema de escalões progressivos por uma **taxa única sobre o rendimento disponível**.
• O valor da taxa não é fixado num número único e imutável no programa, mas a proposta defende que esta deve ser **baixa** para incentivar o trabalho e o investimento.
• O partido defende que a aplicação desta taxa deve ser acompanhada pela **eliminação de quase todas as deduções à coleta** e benefícios fiscais que geram complexidade e distorções no sistema.
• A **Iniciativa Liberal** argumenta que este modelo simplifica o sistema fiscal, reduz a carga administrativa e promove a justiça através da neutralidade, evitando que o aumento de rendimentos resulte numa penalização fiscal desproporcional.

**Reference answer:**

A Iniciativa Liberal propõe uma taxa única de IRS de 15% aplicada aos rendimentos que excedam o salário mínimo nacional anualizado, mantendo as atuais deduções à coleta. Numa primeira fase, de forma gradual, propõe um imposto com duas taxas: 15% para rendimentos entre 11.480 e 21.321 euros e 28% acima desse patamar.

**faithfulness** — Is the claim supported by the CONTEXT?

- [ ] A Iniciativa Liberal propõe a implementação de uma taxa única de IRS.
- [ ] A Iniciativa Liberal propõe a substituição do atual sistema de escalões progressivos por uma taxa única sobre o rendimento disponível.
- [ ] O programa da Iniciativa Liberal não fixa o valor da taxa única de IRS num número único e imutável.
- [ ] A Iniciativa Liberal defende que a taxa única de IRS deve ser baixa para incentivar o trabalho e o investimento.
- [ ] A Iniciativa Liberal defende que a aplicação da taxa única de IRS deve ser acompanhada pela eliminação de quase todas as deduções à coleta.
- [ ] A Iniciativa Liberal defende que a aplicação da taxa única de IRS deve ser acompanhada pela eliminação de benefícios fiscais que geram complexidade e distorções no sistema.
- [ ] A Iniciativa Liberal argumenta que o modelo de taxa única de IRS simplifica o sistema fiscal.
- [ ] A Iniciativa Liberal argumenta que o modelo de taxa única de IRS reduz a carga administrativa.
- [ ] A Iniciativa Liberal argumenta que o modelo de taxa única de IRS promove a justiça através da neutralidade.
- [ ] A Iniciativa Liberal argumenta que o modelo de taxa única de IRS evita que o aumento de rendimentos resulte numa penalização fiscal desproporcional.

**correctness_recall** — Does the ANSWER state this reference claim?

- [ ] A Iniciativa Liberal propõe uma taxa única de IRS de 15% aplicada aos rendimentos que excedam o salário mínimo nacional anualizado.
- [ ] A Iniciativa Liberal propõe manter as atuais deduções à coleta.
- [ ] A Iniciativa Liberal propõe, numa primeira fase e de forma gradual, um imposto com duas taxas.
- [ ] A Iniciativa Liberal propõe uma taxa de 15% para rendimentos entre 11.480 e 21.321 euros.
- [ ] A Iniciativa Liberal propõe uma taxa de 28% para rendimentos acima de 21.321 euros.

relevance: 

<details><summary>Context the generator read</summary>

[Documento 1] Partido: Iniciativa Liberal | Tópicos: impostos, jovens
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 1. MAIS OPORTUNIDADES, MAIS SALÁRIO > 1.2. Reforma Fiscal: Menos Impostos, Mais Salário > Impostos mais baixos e mais simples para todos
#### 1.2. Reforma Fiscal: Menos Impostos, Mais Salário  
##### Impostos mais baixos e mais simples para todos  
Portugal precisa de crescer. Esta é a principal bandeira que a Iniciativa Liberal defende desde que foi fundada. Esta necessidade de crescimento reflete-se no PIB per capita em paridades de poder de compra face à média da União Europeia. Portugal encontra-se praticamente estagnado desde 2011, com oscilações pouco significativas. Portugal mantém-se na cauda da Europa, sendo ultrapassado por 8 países desde o ano 2000. O crescimento não é meramente um capricho liberal: ele não só reflete a melhoria das condições de vida das pessoas, como é igualmente essencial para a melhoria no rácio da dívida pública sobre o produto e o respetivo cumprimento das regras orçamentais da União Europeia, sem colocar em causa o funcionamento do Estado Social e o investimento público.  
O país tem de ser fiscal e administrativamente competitivo, tirando peso e complexidade ao sistema fiscal atualmente vigente. **Portugal tem de deixar de ter uma das maiores taxas de esforço fiscal da União Europeia e passar a ter uma das menores**, como é o caso de países mais liberais como a Irlanda, o Luxemburgo e os Países Baixos. Segundo os dados do Eurostat, Portugal teve em 2022 a quarta maior taxa de esforço fiscal da Europa. Os portugueses não suportam mais esta situação.  
Hoje temos impostos de rico e salários de pobre. Além disso, temos um nível de progressividade enorme, com um recorde europeu de nove escalões, que pune quem quer subir na vida pelo trabalho. E temos um nível de tax wedge muito elevado, onde o Estado leva em média 42% do que a empresa paga por um trabalhador e onde o Estado leva cerca de metade do que a empresa paga por um aumento salarial. É isto que temos de mudar imediatamente. O sistema fiscal liberal recompensa o esforço, dedicação e produtividade daqueles que trabalham e aqueles que assumem riscos, estimulando assim a concorrência.  
Hoje, essa competição não se limita ao âmbito nacional, estendendo-se ao cenário continental e mesmo global. Portugal está em competição direta com o resto do mundo para atrair capital e empregos qualificados. Contudo, a carga fiscal excessiva sobre o trabalho e as empresas nas últimas décadas resultou numa significativa emigração de mão-de-obra altamente qualificada e desvio de investimento para outras regiões. É urgente alterar este panorama.  
**A Iniciativa Liberal defende a descida e simplificação dos impostos sobre rendimentos das pessoas e das empresas, nomeadamente do IRS e do IRC**, promovendo ainda a eliminação de casos de dupla tributação, bem como de taxas e contribuições coercivas que promovem complexidade e barreiras à entrada em mercados competitivos. Além disso, se a energia – neste caso eletricidade e gás – é um bem essencial quer para a vida das famílias quer para a atividade das empresas então não pode ser taxada como um bem de luxo, devendo **o IVA do gás e da eletricidade baixar para 6%**.  
Para crescermos, é também necessária a **revisão e redução de impostos sobre o património**, uma vez que se tratam de impostos que incidem sobre bens comprados por rendimentos que já foram tributados e sobre transações que também foram já tributadas. A Iniciativa Liberal apresenta igualmente alterações ao IMI, de forma a desonerar a detenção do património, bem como ao Imposto do Selo, ao IVA e ao IMT, para desonerar a construção e a aquisição da habitação própria e permanente na transação, medidas que são expressamente apresentadas no capítulo referente à Habitação.  
**Reduzir e Simplificar o IRS até à Taxa Única de 15%**  
Propomos **implementar uma taxa única de 15% a aplicar-se aos rendimentos acima do salário mínimo nacional anualizado**, garantindo a progressividade e mantendo as atuais deduções à coleta previstas.  
A Iniciativa Liberal mantém-se firme na sua proposta de reduzir a progressividade excessiva e simplificar o IRS para todos os contribuintes que têm de obrigatoriamente pagar o imposto, sem prejudicar os contribuintes isentos de IRS.  
Com a aplicação deste IRS substancialmente mais baixo para todos, serão igualmente revogados os atuais programas e benefícios fiscais dirigistas que causam injustiças sociais entre os mais jovens e não jovens, bem como entre os residentes e os não residentes.  
Estamos disponíveis para aprovar e desenvolver propostas transitórias, desde que se baixe significativamente a progressividade excessiva do imposto, reduzindo o número de escalões, e que se incentive claramente a competitividade fiscal dos salários de emprego qualificado. Mais concretamente, a Iniciativa Liberal **numa primeira fase propõe um imposto com duas taxas**, uma de 15% sobre os rendimentos acima de 11.480 euros e abaixo de 21.321 euros, **garantindo a progressividade**, sendo aplicada uma taxa de 28% acima desse patamar de rendimento anual. Em suma, pretende-se isentar de imposto os rendimentos mais baixos aumentando significativamente a dedução específica, agregando os primeiros quatro escalões e, por fim, agregando os últimos cinco escalões com a taxa de 28%. Eis alguns exemplos da poupança esperada por esta alteração.  
| Rendimento | Rendimento<br>Imposto   |          | Proposta de taxa única de 15% |                    |                 | Proposta transitória de 2 taxas |                    |                 |
| ---------- | ----------------------- | -------- | ----------------------------- | ------------------ | --------------- | ------------------------------- | ------------------ | --------------- |
| mensal     | bruto<br>bruto<br>anual | Atual \* | Imposto\*                     | Poupança<br>(abs.) | Poupança<br>(%) | Imposto \*                      | Poupança<br>(abs.) | Poupança<br>(%) |
| 900        | 12.600                  | 784      | 168                           | 616                | 79%             | 168                             | 616                | 79%             |
| 1.100      | 15.400                  | 1.667    | 588                           | 1.079              | 65%             | 588                             | 1.079              | 65%             |
| 1.300      | 18.200                  | 2.295    | 1.008                         | 1.287              | 56%             | 1.008                           | 1.287              | 56%             |
| 1.500      | 21.000                  | 2.952    | 1.428                         | 1.524              | 52%             | 1.428                           | 1.524              | 52%             |
| 1.700      | 23.800                  | 3.680    | 1.848                         | 1.832              | 50%             | 2.170                           | 1.510              | 41%             |
| 2.500      | 35.000                  | 7.397    | 3.528                         | 3.869              | 52%             | 5.306                           | 2.091              | 28%             |
| 4.000      | 56.000                  | 15.060   | 6.678                         | 8.382              | 56%             | 11.186                          | 3.874              | 26%             |  
\* – Imposto apurado antes de deduções à coleta. Estas deduções, mantendo-se, conforme proposto, são indiferentes para o apuramento da poupança entre o imposto atual e o imposto proposto.  
**Baixar o Imposto sobre rendimentos de capitais e prediais**  
Em matéria de tributação de rendimentos de capitais, mais-valias e prediais, a Iniciativa Liberal defende a **redução do imposto para 14,5%, sem englobamento obrigatório**. Em matéria de rendimentos prediais de arrendamento habitacional, propõe-se uma taxa 14.5% com uma descida gradual do imposto, conforme referido posteriormente no capítulo A.2 sobre Habitação.  
**Tributar stock-options no momento da realização da venda e não no exercício da opção**  
A Iniciativa Liberal quer corrigir o momento da tributação da conversão de opções sobre ações em ações para que a mesma ocorra no momento da alienação do ativo. Atualmente, existem duas formas de tributar a conversão de opções sobre ações em ações. A primeira é a prevista no Código de IRS, que prevê a tributação no período em que é exercida a opção e que dá o direito ao trabalhador de ter o número de ações correspondentes, com a valorização que possuem as ações à data da conversão. A segunda com a tributação a ocorrer apenas quando se der a mais- ou menos-valia das ações sobre a qual o trabalhador exerceu a sua opção, conferida pelo benefício fiscal criado por este Governo para os trabalhadores em start-ups. Esta situação cria uma tremenda **desigualdade entre contribuintes em circunstâncias idênticas**, levando a que os primeiros sejam, invariavelmente, prejudicados face aos segundos apenas por uma questão de tratamento fiscal.  
Da forma como está a ser aplicada a lei, há casos de trabalhadores que, não querendo beneficiar dos descontos de taxas que o benefício fiscal também concede, vêem-se na obrigação de se endividar para liquidar impostos. Isto sucede por causa de uma variação do valor das ações que poderão não conseguir liquidar por ainda não terem realizado qualquer tipo de mais-valia com as mesmas. Ou seja, pagam impostos por uma mais-valia esperada, muitas vezes pressionados por apertados prazos de exercício de conversão de opções de ações, sem conhecimento da valorização das mesmas no momento da decisão do exercício das opções.  
A forma mais adequada para garantir um tratamento justo, informado e a capacidade contributiva dos contribuintes é **tributar esta conversão de opção de ação em ação como rendimento de trabalho apenas quando essa ação gerar uma mais ou menos valia na sua alienação**, tal como previsto no benefício fiscal recentemente criado pelo Governo.  
**Baixar e Simplificar o IRC**  
A Iniciativa Liberal propõe uma **taxa de IRC de 12% para as empresas**. Cumprindo a nova legislação europeia, a Iniciativa Liberal quer **aplicar a taxa de IRC mínima de 15% para as multinacionais com uma faturação anual superior a 750 milhões de euros**, seguindo o valor mínimo do imposto pela OCDE, e que a UE através da nova diretiva europeia requer dos Estados-Membros. É urgente simplificar e libertar as empresas da necessidade de consumirem tempo e recursos em atividades improdutivas, permitindo um foco na produção, na melhoria contínua e na expansão. E é necessário atrair investimento estrangeiro, colocando Portugal entre os países mais atrativos da Europa ocidental para as empresas a nível fiscal. Esta reforma implica **revogar as derramas** bem como eliminar as tributações autónomas que representam acréscimos de carga fiscal sobre as empresas em Portugal, completamente contrárias à prática internacional.  
**Portugal tem a segunda maior taxa estatutária máxima de IRC da OCDE**, sendo igualmente o  
**segundo pior país em termos de competitividade fiscal das empresas**, entre os trinta e oito países que a integram, de acordo com o estudo da Tax Foundation em 2023. Na fiscalidade sobre as empresas, Portugal destaca-se negativamente pela sua taxa máxima e pela complexidade. A Iniciativa Liberal tem alertado incessantemente para estes dois fatores, uma vez que põem em causa a capacidade de atrair e manter capital em Portugal, ainda mais num mercado de capitais tão aberto como é a União Europeia.  
Para além do efeito dissuasor expectável que resulta da taxa estatutária máxima de 31.5% de IRC existente em Portugal, a **progressividade imposta pela derrama estadual e as diferenciações de taxação entre empresas com diferentes dimensões, impede a progressão da evolução das empresas** e incentiva-as a manterem-se pequenas e pouco competitivas. Há ainda uma imensidão de benefícios fiscais que, para além de representarem um ímpeto dirigista sobre aquilo que deveria ser a livre iniciativa das empresas, é também uma fonte de improdutividade da nossa economia, abrindo portas à corrupção e favorecimento de certos nichos e empresas.  
O tecido empresarial português tem de ser mais produtivo e mais atrativo, pelo que um sistema fiscal mais simples e mais baixo é fundamental para esse desenvolvimento que a todos beneficia ao enriquecer a economia nacional. Esta simplificação do sistema permite, igualmente, libertar recursos da própria Autoridade Tributária para focar na pedagogia junto do contribuinte para liquidação voluntária, bem como, investigar e combater situações de evasão e fraude fiscal.  
**Eliminar taxas, contribuições e impostos adicionais**  
A Iniciativa Liberal quer eliminar taxas, contribuições e impostos adicionais com vista a **aumentar a competitividade fiscal do país e baixar os custos de contexto**. Sugerimos eliminar:  
- A duplicação de impostos resultante da cobrança de impostos sobre transações que envolvem outros impostos, como é o caso do Imposto do Selo na compra de casas sujeitas ao Imposto Municipal sobre as Transmissões (IMT);
- Contribuição extraordinária sobre o Alojamento Local;
- Contribuição extraordinária sobre a indústria farmacêutica;
- Contribuição extraordinária sobre os fornecedores do Serviço Nacional de Saúde de dispositivos médicos;
- Contribuição extraordinária sobre o setor energético;
- Taxas devidas ao ICP-ANACOM, no âmbito das entidades formadoras na área de infraestruturas: ITUR e ITED;
- Taxas de utilização do espectro radioeléctrico;
- Taxas de emissão de títulos habilitadores de serviços de rádio e televisão;

---

[Documento 2] Partido: Iniciativa Liberal | Tópicos: impostos, economia, financas
  Secção: PROGRAMA ELEITORAL > PORTUGAL A CRESCER > 1. BAIXAR IMPOSTOS E DESBUROCRATIZAR
### 1. BAIXAR IMPOSTOS E DESBUROCRATIZAR  
- **Taxa única de IRS de 15% sobre a parte dos rendimentos que exceda o Salário Mínimo Nacional, começando de forma gradual com duas taxas de 15% e 28%, aumentando imediatamente o salário líquido**
- **Reduzir a carga fiscal sobre os profissionais liberais e os trabalhadores independentes**
- **Taxa única de IRC de 12% para as empresas, excepto para as grandes multinacionais que será de 15% de acordo com o exigido pela lei europeia**
- **Criar uma task force de eliminação de burocracias desnecessárias em diálogo com cidadãos e empresas**
- **Criar Zonas Económicas Especiais (ZEE) de baixa fiscalidade no interior do país para atrair investimento direto estrangeiro e promover a criação de hubs empresariais**
- **Reverter as normas do pacote Mais Habitação relativas ao Alojamento Local, eliminar a redução do coeficiente fiscal**
- **Eliminar várias taxas e contribuições extraordinárias como o adicional ao IMI (AIMI) e o imposto do selo sobre transações já taxadas**
- **Eliminar gradualmente o Imposto Único de Circulação (IUC)**
- **Reduzir o imposto sobre rendimentos de capitais para 14,5%**
- **Compromisso de Orçamentos com superávit e redução da dívida pública**

---

[Documento 3] Partido: Iniciativa Liberal | Tópicos: impostos, economia
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 1. MAIS OPORTUNIDADES, MAIS SALÁRIO > 1.2. Reforma Fiscal: Menos Impostos, Mais Salário > Impostos mais baixos e mais simples para todos
**Baixar e Simplificar o IRC**  
A Iniciativa Liberal propõe uma **taxa de IRC de 12% para as empresas**. Cumprindo a nova legislação europeia, a Iniciativa Liberal quer **aplicar a taxa de IRC mínima de 15% para as multinacionais com uma faturação anual superior a 750 milhões de euros**, seguindo o valor mínimo do imposto pela OCDE, e que a UE através da nova diretiva europeia requer dos Estados-Membros. É urgente simplificar e libertar as empresas da necessidade de consumirem tempo e recursos em atividades improdutivas, permitindo um foco na produção, na melhoria contínua e na expansão. E é necessário atrair investimento estrangeiro, colocando Portugal entre os países mais atrativos da Europa ocidental para as empresas a nível fiscal. Esta reforma implica **revogar as derramas** bem como eliminar as tributações autónomas que representam acréscimos de carga fiscal sobre as empresas em Portugal, completamente contrárias à prática internacional.  
**Portugal tem a segunda maior taxa estatutária máxima de IRC da OCDE**, sendo igualmente o  
**segundo pior país em termos de competitividade fiscal das empresas**, entre os trinta e oito países que a integram, de acordo com o estudo da Tax Foundation em 2023. Na fiscalidade sobre as empresas, Portugal destaca-se negativamente pela sua taxa máxima e pela complexidade. A Iniciativa Liberal tem alertado incessantemente para estes dois fatores, uma vez que põem em causa a capacidade de atrair e manter capital em Portugal, ainda mais num mercado de capitais tão aberto como é a União Europeia.  
Para além do efeito dissuasor expectável que resulta da taxa estatutária máxima de 31.5% de IRC existente em Portugal, a **progressividade imposta pela derrama estadual e as diferenciações de taxação entre empresas com diferentes dimensões, impede a progressão da evolução das empresas** e incentiva-as a manterem-se pequenas e pouco competitivas. Há ainda uma imensidão de benefícios fiscais que, para além de representarem um ímpeto dirigista sobre aquilo que deveria ser a livre iniciativa das empresas, é também uma fonte de improdutividade da nossa economia, abrindo portas à corrupção e favorecimento de certos nichos e empresas.  
O tecido empresarial português tem de ser mais produtivo e mais atrativo, pelo que um sistema fiscal mais simples e mais baixo é fundamental para esse desenvolvimento que a todos beneficia ao enriquecer a economia nacional. Esta simplificação do sistema permite, igualmente, libertar recursos da própria Autoridade Tributária para focar na pedagogia junto do contribuinte para liquidação voluntária, bem como, investigar e combater situações de evasão e fraude fiscal.  
**Eliminar taxas, contribuições e impostos adicionais**  
A Iniciativa Liberal quer eliminar taxas, contribuições e impostos adicionais com vista a **aumentar a competitividade fiscal do país e baixar os custos de contexto**. Sugerimos eliminar:  
- A duplicação de impostos resultante da cobrança de impostos sobre transações que envolvem outros impostos, como é o caso do Imposto do Selo na compra de casas sujeitas ao Imposto Municipal sobre as Transmissões (IMT);
- Contribuição extraordinária sobre o Alojamento Local;
- Contribuição extraordinária sobre a indústria farmacêutica;
- Contribuição extraordinária sobre os fornecedores do Serviço Nacional de Saúde de dispositivos médicos;
- Contribuição extraordinária sobre o setor energético;
- Taxas devidas ao ICP-ANACOM, no âmbito das entidades formadoras na área de infraestruturas: ITUR e ITED;
- Taxas de utilização do espectro radioeléctrico;
- Taxas de emissão de títulos habilitadores de serviços de rádio e televisão;
- Compensação pela fixação e reprodução, conhecida como Taxa da Cópia Privada;
- Encargos com autorizações para plantações de vinhas;
- Contribuição Audiovisual;
- Adicional ao Imposto Municipal sobre Imóveis (AIMI);
- Adicional ao Imposto Único de Circulação (IUC);
- Adicional ao IMT de imóveis em terrenos da margem sul do Tejo, conhecido como Imposto da Ponte.  
Estes exemplos de taxas, impostos adicionais e contribuições são um perigo silencioso para a economia nacional. A existência e a persistência dos mesmos funcionam como autênticas barreiras a mercados que se desejam competitivos, causando distorções de mercado e punindo indústrias com consequências para os seus consumidores finais. Por esse motivo, a Iniciativa Liberal continuará a propor a **eliminação e a revogação de um conjunto de taxas, impostos adicionais e contribuições extraordinárias que têm afetado a competitividade fiscal e os consumidores finais**.  
**Tributar a mobilidade de forma justa**  
A Iniciativa Liberal pretende reduzir gradualmente o imposto único de circulação (IUC), corrigir as ilegalidades existentes no atual imposto sobre veículos (ISV) e vai certificar-se que os impostos sobre os combustíveis (ISP) não se tornem excessivos perante as circunstâncias económicas do país. Deve reduzir-se os incentivos a adquirir automóveis, novos ou usados, que sejam poluentes sem penalizar quem atualmente já tem veículo próprio.  
Os automóveis e motociclos são um alvo fácil para a tributação, uma vez que os impostos que sobre eles incidem são cada vez mais justificados como ambientais. Não é verdade que o sejam em casos como o IUC, onde o imposto nada tem que ver com a circulação, pois paga-se o mesmo, circule o carro um ou cem mil quilómetros num ano. Nem se pode punir a maioria dos portugueses por usar veículo próprio para trabalhar e fazer a sua vida, perante a ausência de alternativas de transportes públicos.

---

[Documento 4] Partido: Iniciativa Liberal | Tópicos: impostos, trabalho, seguranca_social
  Secção: PROGRAMA ELEITORAL > A. PORTUGAL A CRESCER > 4.TRABALHO: MENOS RESTRIÇÕES, MAIS OPORTUNIDADES > 4.3. Valorizar os profissionais liberais e trabalhadores independentes
**Alargar direitos de parentalidade a profissionais liberais e trabalhadores independentes**  
No âmbito do processo de especialidade do Orçamento do Estado para 2024, a Iniciativa Liberal bateu-se pela eliminação da discriminação dos profissionais liberais e trabalhadores independentes na proteção social na parentalidade. Os trabalhadores independentes beneficiários do sistema previdencial têm direito ao subsídio parental, mas na prática, pela natureza da sua atividade, não há igualdade face aos trabalhadores por conta de outrem. Por exemplo, o período de referência para cálculo do montante do subsídio não prevê oscilações inerentes à sua atividade e não está prevista a diminuição do horário laboral para a amamentação.  
A proposta de alteração aprovada previa que já este ano o Governo estudasse a possibilidade e as condições de **integração dos profissionais liberais e trabalhadores independentes nos regimes de licenças de parentalidade, de forma a terem efetivamente direitos parentais equiparados aos dos trabalhadores por** **conta de outrem**. Esta integração é complexa e tem implicações a diferentes níveis, pelo que é pertinente a realização urgente de um estudo que identifique todas as implicações – legislativas e financeiras – de diferentes alternativas. Tendo em conta as conclusões e recomendações do estudo, a Iniciativa Liberal compromete-se a implementar as medidas mais adequadas para garantir a igualdade efetiva das condições parentais entre todos os trabalhadores, nomeadamente das licenças parentais e do período de amamentação. conciliação entre vida profissional e pessoal. As medidas terão em conta as condições sobretudo das mães (mas também dos pais), apoiando os projetos de família, de vida e de felicidade a milhares de trabalhadores independentes e profissionais liberais.  
**Flexibilizar o acesso a creches para filhos de profissionais liberais e trabalhadores independentes**  
A natureza da atividade profissional de alguns profissionais liberais e trabalhadores independentes é muitas vezes incompatível com ausências prolongadas, nomeadamente após o nascimento de um(a) filho(a). São exemplos deste cenário, advogados que poderão ter de estar presentes em tribunal ou donos de lojas, sendo ainda mais grave no caso em que ambos os pais estão nesta situação, obrigando-os a fazer sacrifícios profissionais ou pessoais, como o adiamento ou abandono de projetos parentais. Nestes casos, é necessário garantir acesso a serviços de cuidados à primeira infância mais cedo do que os adequados aos trabalhadores por conta, que têm direito a licenças de parentalidade de 120 dias.  
No entanto, atualmente, as creches e creches familiares só estão autorizadas a cuidar de crianças a partir dos 3 meses de idade. Propomos **flexibilizar em duas vertentes o** **acesso a creches a crianças cujos ambos os pais sejam profissionais liberais ou trabalhadores independentes**: na idade, permitindo prestar cuidados a crianças com menos do que 3 meses; e na duração, permitindo que o cuidado a essas crianças com menos de 3 meses seja prestado em períodos avulsos, flexíveis ou irregulares (por exemplo, 1 dia, 2 dias por semana, 1 semana por mês).  
**Alargar a isenção sobre rendimentos a trabalhadores-estudantes independentes**  
Em paralelo, a desigualdade de tratamento estende-se também à conjugação entre o trabalho e os estudos. Recentemente, houve um avanço legislativo importante que beneficiou os jovens trabalhadoresestudantes, permitindo que **parte de seus rendimentos de trabalho dependente não sejam considerados para efeitos de atribuição de prestações sociais**. No entanto, os trabalhadores independentes não foram abrangidos por essa alteração.  
Ainda para mais, devido ao carácter sazonal, experimental ou até pela tipologia de atividade (por exemplo, artística ou tecnológica), esta opção afigura-se contraproducente não só por deixar de fora grande parte dos possíveis estudantes, mas também por ser um **desincentivo à livre iniciativa, à entrada no mercado de trabalho e à assunção de riscos**. No limite, **bloqueiam-se oportunidades e fomenta-se a informalidade** e a ilegalidade.  
Os estudantes, independentemente do seu estatuto laboral, devem ter igual acesso a oportunidades educacionais e de inserção no mercado de trabalho. É importante que a legislação seja ajustada para garantir que ambos os grupos sejam tratados de maneira justa e equitativa.  
**Defender a justiça fiscal para os profissionais liberais e trabalhadores independentes**  
A Iniciativa Liberal propõe um conjunto de medidas fiscais aplicáveis aos profissionais liberais e trabalhadores independentes, das quais se destacam:  
- Aumentar o valor de rendimentos passíveis da isenção do pagamento de IVA de 20.000 euros para 25.000 euros;
- Aumentar o valor de rendimentos passíveis de isenção de contribuições para a Segurança Social quando o trabalhador acumule o trabalho independente com o trabalho por conta de outrem de quatro vezes o valor do Indexante dos Apoios Sociais (2.037,04 euros) para 25.000 euros;
- Simplificar o valor da retenção de rendimentos dos profissionais liberais e trabalhadores independentes em sede de IRS, propondo que o montante da retenção seja apurado pela taxa de imposto efetiva média aplicada aos profissionais liberais e trabalhadores independentes em Portugal no período anterior.

</details>
