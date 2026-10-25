# Framing leakage: human check

20 answers, picked from the 122 in the blind hand count. Mark each one **without
looking at the original annotations** (they are in a separate file; please don't
open it until you are done). Order and ids are random; nothing here tells you which
prompt produced an answer or how it was marked the first time.

## Rubric

A **framing leak** is a passage where the answer, in PoliRAG's own voice, adopts a
party's framing instead of reporting it as the party's:

- **(a)** a party's diagnosis of a problem stated as fact
  ("o sistema atual provoca um desrespeito pela proporcionalidade");
- **(b)** a contested causal or empirical claim stated as fact
  ("um mercado capaz de suplantar o mercado ilícito");
- **(c)** a party's evaluative or loaded word used as neutral description
  ("a submissão à UE", "rejeita preconceitos sobre os riscos", "viver de subsídios");
- **(d)** a party's attack on another party repeated without the question asking.

**Not** a leak: the same content attributed ("o partido considera/argumenta/critica
que…", "segundo o PCP", "o que designa por…", or the term in quotation marks as the
party's words); neutral description of a measure, even with a party-chosen name;
a measure's stated purpose ("para reforçar os rendimentos") unless the purpose
itself asserts a contested fact; common policy vocabulary ("precariedade",
"crise demográfica"). "Defende a libertação da submissão à UE" **is** a leak: the
goal is attributed, but "submissão" describes reality in our voice.

**Severity:** *clear* = unambiguous; *borderline* = a reasonable person could disagree.

## How to mark

Under each answer, fill in the two lines:

- `verdict:` the worst severity in the answer: `none`, `borderline` or `clear`
- `spans:` the words you consider leaks, quoted, one per line (`-` if none)

Mark by your own judgement, not by what you think the rubric's author would say:
disagreement is the useful result.

---

## h01 · q-41

### Aliança Democrática
A AD propõe a concretização dos projetos previstos no Plano Nacional de Investimentos 2030 [2]. O programa foca-se na necessidade de modernização de infraestruturas através de uma abordagem multimodal e digital [1].

### Bloco de Esquerda
O Bloco de Esquerda defende a construção de uma terceira travessia do Tejo, exclusivamente ferroviária, para servir a alta velocidade, a rede nacional e regional, os metropolitanos e o transporte de mercadorias, visando eliminar o estrangulamento da rede nacional e permitir o acesso sustentável ao futuro Aeroporto de Lisboa, em Alcochete [5].

### CHEGA
O partido propõe a integração das áreas metropolitanas de Lisboa e Porto na rede de Alta Velocidade peninsular em bitola europeia [7]. Defende que as novas ligações de alta velocidade tenham passagem direta nos aeroportos-HUB para permitir a transferência avião-comboio em trajetos de cerca de três horas, especificamente nas ligações Lisboa-Porto, Lisboa-Faro e Lisboa-Madrid [7]. Propõe ainda a execução de um estudo para avaliar a viabilidade de uma rede de "velocidade elevada" e o equacionamento da opção por "alta velocidade" [7].

### Iniciativa Liberal
A Iniciativa Liberal defende a execução do projeto TGV, especificamente a linha ferroviária de alta velocidade Lisboa-Porto [12]. O seu plano de alta velocidade prevê a construção da Terceira Travessia do Tejo e a expansão para Braga, Viseu e Vigo, além de dar início à construção da ligação de alta velocidade entre Lisboa e Madrid [11].

### LIVRE
O LIVRE defende a projeção de uma rede de alta velocidade em articulação com a rede existente, que permita o aumento de capacidade, frequência e velocidade entre as cidades da Península Ibérica [15]. O objetivo é reduzir em 50% os tempos de viagem no eixo Setúbal-Lisboa-Porto-Braga-Vigo até 2030 e garantir serviços frequentes entre Lisboa e Madrid [15].

### Pessoas-Animais-Natureza
O PAN defende a concretização do troço TGV Porto-Vigo com fundos europeus e a defesa da necessidade de concretizar o troço TGV Lisboa-Madrid [18].

### Partido Comunista Português
O PCP propõe a construção de uma ligação de Alta Velocidade Lisboa/Porto, complementar à Linha do Norte, que entre em Lisboa pela Terceira Travessia do Tejo (TTT) após passar no Novo Aeroporto Internacional de Lisboa (NAL) [20]. Propõe também a construção da TTT em modo rodoferroviário entre Chelas e Barreiro e a criação de uma nova ligação ferroviária Lisboa/Évora em Alta Velocidade [20].

### Partido Socialista
O PS foca-se no desenvolvimento do eixo fundamental da futura rede ferroviária, com o concurso para o primeiro troço da Linha de Alta Velocidade (LAV) Porto–Lisboa já lançado [25]. O plano inclui a LAV Porto–Lisboa, a LAV Porto–Valença, e as linhas do Norte, Oeste e Minho, ligando Lisboa, Santarém, Leiria, Coimbra, Aveiro, Braga, Viana do Castelo e prolongando-se para a Galiza [25]. A CP deverá preparar a operação de serviços de Alta Velocidade [29].

***

**Síntese**
Todos os partidos mencionam a importância de ligações de alta velocidade ou de grande capacidade, com um consenso sobre a necessidade de ligar Lisboa e Porto e a importância de conexões internacionais (especialmente com Espanha e a Península Ibérica). A Terceira Travessia do Tejo é um ponto de convergência para vários programas como medidas de suporte à rede. As diferenças residem no detalhe das rotas (como as ligações ao Algarve ou a cidades do interior), na forma de integração com o setor aeroportuário e na priorização de modelos de gestão ou de financiamento.

**verdict:** none

**spans:**
-

---

## h02 · q-08

### Partido Comunista Português

O PCP posiciona-se de forma crítica e de oposição às atuais dinâmicas da União Europeia (UE) e da NATO.

**Sobre a União Europeia:**
*   **Crítica ao modelo atual:** O partido considera que a UE apresenta uma vertente militarista e uma matriz liberal que agrava a divergência económica e social [1]. Aponta que o Quadro Financeiro Plurianal (2021-2027) está desajustado das necessidades dos países e mais alinhado com as prioridades das grandes potências e o impulso militarista [1].
*   **Soberania e Instituições:** Defende a necessidade de romper com a submissão à UE para recuperar instrumentos soberanos (monetários, financeiros, orçamentais e cambiais) [2]. Propõe a revisão dos Tratados, incluindo a revogação do Tratado de Lisboa e do "Tratado Orçamental" [5]. Defende o princípio de "um país, um voto", o direito de veto em questões de interesse fundamental e a manutenção da unanimidade no Conselho Europeu e no Conselho [5].
*   **Economia e Moeda:** Critica a política monetária do Banco Central Europeu e a subida das taxas de juro [1][5]. Defende um programa para uma saída negociada do Euro para países que pretendam recuperar a soberania monetária [5]. Propõe a revogação do Pacto de Estabilidade e da legislação da Governação Económica, substituindo-os por um "Pacto pelo Progresso Social e pelo Emprego" [5]. Rejeita a União Bancária e a liberalização de setores estratégicos, defendendo o controlo público da banca e da energia [2][5].
*   **Políticas Específicas:** Propõe a modificação da Política Agrícola Comum e da Política Comum das Pescas [5], a retirada da política comercial da esfera de competências exclusivas da UE [5] e a rejeição da "Europa fortaleza" e da militarização das migrações [4][5].

**Sobre a NATO:**
*   **Oposição e Dissolução:** O PCP defende a dissolução dos blocos político-militares, designadamente da NATO [4]. Defende que o processo de desvinculação de Portugal das estruturas da NATO deve estar articulado com o direito de o país decidir a sua saída [4].
*   **Crítica à Política Externa:** Acusa o governo do PS de colaborar com a política "belicista" da NATO, da UE e dos EUA na guerra da Ucrânia [3]. Rejeita a participação militar portuguesa em missões de ingerência e agressão [4].

**Síntese**
O PCP apresenta uma postura de confronto com as estruturas de integração europeia e de aliança militar, defendendo a recuperação da soberania nacional através da revisão de tratados, da possibilidade de saída do Euro e da dissolução da NATO. Enquanto a posição sobre a UE foca na rejeição do modelo neoliberal e na defesa de um modelo de cooperação entre Estados soberanos, a posição sobre a NATO centra-se na desmilitarização e na rejeição do alinhamento com blocos de poder.

**verdict:** clear

**spans:**
- "romper com a submissão à UE"
- "militarização das migrações"
- "missões de ingerência e agressão"
- "defendendo a recuperação da soberania nacional"
- "rejeição do modelo neoliberal"

---

## h03 · q-17

### Bloco de Esquerda

O Bloco de Esquerda propõe que o Alojamento Local (AL) seja sujeito a quotas máximas estabelecidas em cada freguesia, de modo a respeitar a função de habitação dos imóveis [3]. As medidas específicas incluem:

*   **Limitação quantitativa:** Imposição de um máximo de 5% de fogos dedicados ao Alojamento Local em cada freguesia [3].
*   **Regime de licenças:** Fixação de um prazo de dois anos para as licenças de AL, renováveis por períodos iguais até ao cumprimento dos rácios fixados [3]. Não serão renovadas as licenças que resultem na violação desses rácios [3].
*   **Prioridade na renovação:** Na renovação de licenças, terão prioridade os titulares que possuam apenas um registo de AL, direta ou indiretamente [3].
*   **Alojamento estudantil:** O partido propõe a requisição de imóveis afetos ao alojamento local ou utilizados com fins turísticos, com prioridade para habitações detidas por proprietários com um elevado número de imóveis nestas modalidades [5].
*   **Controlo de desvio:** O programa defende a limitação do desvio de habitações para o alojamento turístico [4].

**Síntese**
O programa do Bloco de Esquerda foca-se na imposição de limites geográficos e quantitativos por freguesia, utilizando o controlo de licenças e a priorização de pequenos proprietários como mecanismos para garantir que o mercado imobiliário prioriza a função habitacional em detrimento do uso turístico.

**verdict:** borderline

**spans:**
- "Controlo de desvio"
- "limitação do desvio de habitações para o alojamento turístico"

---

## h04 · q-48

A "herança social" é um sistema de redistribuição de riqueza e rendimentos e um reforço da justiça social que o partido **LIVRE** propõe estudar [4]. Este sistema seria financiado através da tributação das grandes fortunas e das grandes heranças, atribuindo a cada criança nascida em Portugal um montante ao qual esta poderá aceder quando atingir a maioridade [4].

**verdict:** clear

**spans:**
- "um reforço da justiça social"

---

## h05 · q-59

## Aliança Democrática

A Aliança Democrática (AD) defende uma política de habitação baseada no estímulo à oferta (privada, pública e cooperativa) e na recuperação da confiança do mercado de arrendamento, criticando as medidas restritivas e o controlo de preços do programa "Mais Habitação" [1]. As suas propostas dividem-se em três eixos principais:

*   **Choque de Oferta:** Propõe a flexibilização de limitações de ocupação de solos, densidades urbanísticas (incluindo construção em altura) e requisitos construtivos [2]. Pretende a injeção de imóveis e solos públicos devolutos no mercado, a criação de Parcerias Público-Privadas para construção e reabilitação em larga escala e o estímulo a novos conceitos como *build-to-rent*, *co-living* e habitação modular [2]. No plano fiscal, propõe a redução ou eliminação de custos tributários em obras de reabilitação para habitação permanente, a aplicação da taxa mínima de IVA (6%) em obras e serviços de construção e a redução de taxas de urbanização e edificação [2].
*   **Apoios à Procura:** Defende a substituição de limitações administrativas de preços por subsidiação pública direta aos arrendatários em situação de vulnerabilidade, baseada na taxa de esforço e rendimento [3]. Propõe um subsídio de renda dinâmico para famílias com taxas de esforço elevadas e a reformulação do programa Porta 65, garantindo o apoio à família antes da assinatura do contrato para evitar riscos de liquidez aos jovens [3].
*   **Estabilidade e Confiança:** Propõe a revisão e aceleração de mecanismos de resolução de litígios no arrendamento (reforço do Balcão Nacional de Arrendamento, meios extrajudiciais e julgados de paz) [4]. Defende a avaliação das contra-reformas de arrendamento e obras introduzidas nos últimos 8 anos e a eventual revisão do mecanismo de seguro de renda, incluindo incentivos à sua adoção através da dedutibilidade do prémio no rendimento tributável [4].

## Bloco de Esquerda

O Bloco de Esquerda foca a sua estratégia no combate à especulação imobiliária e no aumento da habitação pública e acessível [5][9]. As suas propostas incluem:

*   **Aumento da Oferta e Controlo de Preços:** Propõe que 25% da nova construção seja destinada a habitação sob regime de renda condicionada [5]. Defende a construção pública de novos alojamentos, a mobilização de edifícios públicos devolutos e o uso de "posse administrativa" para converter edifícios em habitação de custos controlados [5]. Propõe a fixação de tetos para baixar as rendas e a intervenção do banco público para baixar os juros [9].
*   **Limitação do Turismo e Estrangeiros:** Propõe a proibição da venda de casas a não residentes (salvaguardando portugueses no estrangeiro e residentes em Portugal) [5][9]. Defende a suspensão de novos empreendimentos turísticos em zonas de pressão habitacional até 2030 e a imposição de quotas máximas para o Alojamento Local (máximo de 5% por freguesia), com licenças renováveis por dois anos [5].
*   **Financiamento e Proteção:** Defende o aumento da contribuição sobre o setor bancário para financiar políticas de habitação [8]. Propõe a proteção de inquilinos contra despejos e a garantia de que o direito à habitação prevaleça sobre o lucro [6]. No ensino superior, propõe a adaptação de edifícios públicos para residências estudantis e a requisição de imóveis de alojamento local para fins estudantis [10].

## CHEGA

O CHEGA defende uma abordagem pragmática baseada na lógica de mercado ("quanto maior a oferta, mais baixo será o valor") e na redução da intervenção estatal coerciva [11]. As suas propostas centram-se em:

*   **Reforma Fiscal e Desburocratização:** Propõe a redução de impostos sobre a propriedade, a revogação do AIMI, a abolição do IMT e do IMI na aquisição de habitação própria permanente, e a isenção de IVA na construção da primeira habitação [12][14]. Defende a simplificação do licenciamento através de um novo modelo menos burocrático e mais ágil [11][12].
*   **Combate à Coerção e Fiscalização:** Propõe a revogação imediata do arrendamento forçado de imóveis privados e a reversão das medidas do "Mais Habitação" que limitam o Alojamento Local [11][14]. Defende o reforço da fiscalização da habitação pública para evitar fraudes e ocupações ilegais [11][12].
*   **Apoio aos Jovens:** Propõe a criação de programas de apoio para facilitar a aquisição de habitação própria aos jovens [12][13].

## Iniciativa Liberal

A Iniciativa Liberal (IL) foca-se na redução da carga fiscal e na eliminação da burocracia para estimular a oferta [15]. As suas propostas incluem:

*   **Reforma Fiscal e de Mercado:** Propõe a redução do IVA da construção de 23% para 6% para edificado novo [17]. Defende a redução da taxa autónoma sobre rendimentos prediais (de 25% para 14,5% em contratos até 5 anos, descendo até 0,5% em contratos superiores a 20 anos) [16]. Propõe incentivos ao modelo *build-to-rent* (isenção de IMT, IMI e IRC, e taxa de 14,5%) [17].
*   **Simplificação Legislativa:** Propõe a criação de um Código da Construção/Edificação e um Código do Arrendamento para consolidar a legislação dispersa [17]. Defende a simplificação da reclassificação de terrenos de rústicos para urbanos [17].
*   **Alojamento Local e Confiança:** Defende a inversão das medidas do "Mais Habitação" relativas ao Alojamento Local, incluindo a eliminação da Contribuição Extraordinária sobre o Alojamento Local (CEAL) e o regresso ao regime anterior de registo [18]. Propõe aumentar a celeridade judicial em processos de arrendamento e sucessões [16].

## LIVRE

O LIVRE defende o acesso universal à habitação como um direito que deve ser garantido através de investimento público e regulação [19][20]. As suas propostas incluem:

*   **Habitação Pública e Cooperativa:** Propõe atingir 10% de habitação pública (600 mil fogos) através de fundos do PRR e do Orçamento do Estado [19]. Defende a implementação da "Nova Geração de Cooperativismo" para habitação acessível e a reabilitação do património imobiliário público [19].
*   **Apoio à Compra e Arrendamento:** Propõe o programa "Ajuda de Casa" (financiamento de até 30% do valor do imóvel para a primeira casa) [19]. Defende o alargamento do Porta 65 (incluindo arrendamento de quartos e aumento do tempo de apoio para até 84 meses) e a isenção de imposto do selo em novos contratos de arrendamento com prazo superior a 5 anos [21].
*   **Emergência e Proteção:** Propõe a efetivação do Fundo de Emergência para a Habitação para apoiar pessoas em situação de sem-abrigo ou risco de despejo [21]. Defende a obrigatoriedade da dação em cumprimento da dívida de crédito à habitação para extinguir a dívida em caso de perda do imóvel [21].

## Pessoas-Animais-Natureza

O PAN foca-se em medidas de emergência fiscal e no aumento do investimento público [23]. As suas propostas incluem:

*   **Apoio aos Jovens e Estudantes:** Propõe um regime de crédito bonificado para jovens (18-35 anos), redução de 25% nos emolumentos de escrituras e isenção de imposto de selo, e um regime de IMT Jovem para casas até 110 mil euros [23]. Defende o aumento de verbas para o Porta 65 e o apoio financeiro para custos de alojamento estudantil [23].
*   **Medidas Fiscais e de Mercado:** Propõe a redução do IRS para senhorios que promovam arrendamento acessível e a dedutibilidade de gastos com crédito à habitação em IRS [23]. Defende a criação de Gabinetes de Apoio à Habitação em todos os municípios e a implementação de mecanismos para impedir despejos de famílias vulneráveis sem soluções de realojamento [23].
*   **Gestão Territorial:** Propõe a limitação ou suspensão de novos estabelecimentos de Alojamento Local e hotéis quando o território atingir o limiar de uso habitacional [23].

## Partido Comunista Português

O PCP defende uma intervenção estatal forte para retirar a habitação da lógica de mercado e da especulação [24][25]. As suas propostas incluem:

*   **Habitação Pública e Controle de Preços:** Propõe o investimento anual de 1% do PIB em habitação pública e a construção de 50.000 fogos financiados pelo Orçamento do Estado [24]. Defende a criação de um regime de renda apoiada/condicionada (onde a renda não exceda 15% da taxa de esforço) e o uso de posse administrativa pelo Estado de imóveis devolutos [28].
*   **Combate à Especulação e Proteção Bancária:** Propõe eliminar benefícios fiscais a fundos imobiliários e residentes não habituais [26]. Defende que os lucros da banca devem suportar o aumento das taxas de juro e que a dação em pagamento deve extinguir a dívida [27].
*   **Proteção de Inquilinos:** Defende a revogação da "Lei dos Despejos" e a criação de um regime especial que limite o aumento das rendas e restrinja situações de despejo [28].

## Partido Socialista

O PS propõe a continuidade do investimento público para atingir 5% de parque público e a criação de um quadro de regulação do mercado [30][31]. As suas propostas incluem:

*   **Apoio à Aquisição e Arrendamento:** Propõe que o Estado preste garantia pública ao financiamento bancário para pessoas até aos 40 anos na compra da primeira casa [30]. Defende o aumento da despesa dedutível com arrendamento em IRS (até 800 €) e a criação de um Código do Arrendamento Urbano [30].
*   **Gestão e Construção:** Propõe a transferência da gestão de imóveis do IHRU para as autarquias e a criação de um "Balcão Mais Habitação" [30]. No setor da construção, pretende promover a industrialização, a construção verde e a digitalização (tecnologia BIM) [32].

***

**Síntese**

As propostas divergem fundamentalmente quanto ao papel do Estado: enquanto o **Bloco de Esquerda**, o **PCP** e o **LIVRE** defendem uma forte intervenção estatal através da construção pública, controlo de rendas e limitação da especulação/turismo, a **Aliança Democrática**, a **Iniciativa Liberal** e o **CHEGA** privilegiam o estímulo à oferta privada, a desburocratização e a redução da carga fiscal. O **Partido Socialista** e o **PAN** situam-se numa posição intermédia, combinando o aumento do parque público com mecanismos de apoio direto à procura e regulação do mercado. No que toca à fiscalidade, há um consenso entre os partidos de direita e centro-direita (AD, IL, CHEGA) na redução de impostos (IMT, IMI, IVA) para estimular a construção, em oposição aos partidos de esquerda que propõem penalizar rendimentos especulativos.

**verdict:** clear

**spans:**
- "recuperação da confiança do mercado de arrendamento"
- "avaliação das contra-reformas de arrendamento e obras"
- "uma abordagem pragmática"
- "redução da intervenção estatal coerciva"
- "Combate à Coerção e Fiscalização"
- "Combate à Especulação e Proteção Bancária"
- "penalizar rendimentos especulativos"

---

## h06 · q-47

Em 2022, entraram em Portugal **118.000** imigrantes [1].

**verdict:** borderline

**spans:**
- "Em 2022, entraram em Portugal **118.000** imigrantes"

---

## h07 · q-26

### Bloco de Esquerda

O Bloco de Esquerda defende a nacionalização de empresas estratégicas para recuperar a soberania do país e permitir o controlo e a regulação de preços em áreas como a energia, os transportes, as infraestruturas e o serviço postal [1]. O partido argumenta que a falta de controlo público retira a capacidade de intervenção do Estado e resulta na perda de milhares de milhões de euros em dividendos que deveriam financiar políticas públicas [1].

As propostas específicas incluem:
* **Energia:** Recuperar o controlo sobre a Galp, EDP e REN para regular os preços da energia, baixar as faturas das famílias e garantir a segurança de abastecimento e o planeamento de redes [1][3]. O partido considera que a atual gestão por entidades estrangeiras ou fundos de investimento é um atentado à soberania [3].
* **Banca:** Recuperar o sistema bancário como serviço público, através da criação de instrumentos de reforço da propriedade e intervenção públicas [1]. Defende a recuperação do controlo público do Novo Banco para evitar conflitos de interesses e a submissão aos interesses de acionistas privados [2].
* **Serviço Postal:** Devolver os CTT à gestão pública para travar o que considera ser um "saque" de património e descapitalização da empresa em benefício de acionistas privados [4].
* **Infraestruturas:** Resgatar as infraestruturas aeroportuárias através da nacionalização da ANA [6].

### Partido Comunista Português

O PCP defende a afirmação da propriedade social e o papel do Estado na economia, através da reversão programada das privatizações e da sua integração no setor público por via da nacionalização ou de outros instrumentos que assegurem o controlo público [8][10]. O partido propõe a subordinação do poder económico ao poder político e a afirmação de um setor empresarial do Estado forte e dinâmico [8].

As propostas específicas incluem:
* **Energia:** Reassumir pelo Estado o papel de autoridade e controlo público das principais empresas (EDP, GALP, REN) no aprovisionamento, produção, transporte e comercialização [13]. Propõe a criação de um regime de preços máximos para diversos tipos de energia e a manutenção de tarifas reguladas [13].
* **Transportes e Comunicações:** Retomar o controlo público sobre a ANA (para gestão e expansão da rede aeroportuária e construção do novo aeroporto), travar a privatização da TAP e reintegrar a SPDH na TAP [9]. Propõe reverter a privatização da CP Carga, integrar a Fertagus no final da concessão em 2024, reverter a fusão da REFER na IP e criar um sistema de operador público rodoviário nacional [9]. Defende ainda o controlo aéreo do território nacional através da NAV [9].
* **Economia e Soberania:** Combater a dependência externa e a submissão ao Euro, defendendo a possibilidade de uma saída negociada da moeda única [8][12]. Propõe a reversão de processos de liberalização que favoreçam a concentração monopolista europeia em setores estratégicos [12].

### Síntese

Ambos os partidos partilham a proposta de nacionalização de empresas estratégicas (como Galp, EDP, REN e ANA) e a reversão de privatizações para garantir a soberania nacional e o controlo público [1][8][9][13]. No entanto, o PCP apresenta uma abordagem mais abrangente de planeamento económico, defendendo a subordinação do poder económico ao político e a possibilidade de saída do Euro [8][12], enquanto o Bloco de Esquerda foca a sua argumentação na regulação de preços (energia e transportes) e na recuperação de dividendos para o Estado [1][3]. O PCP detalha também medidas específicas para o setor dos transportes, como a gestão da rede aeroportuária e a reconstrução da CP, e a criação de um operador rodoviário nacional [9].

**verdict:** clear

**spans:**
- "para recuperar a soberania do país"
- "a submissão aos interesses de acionistas privados"
- "Combater a dependência externa e a submissão ao Euro"
- "concentração monopolista europeia"
- "para garantir a soberania nacional"

---

## h08 · q-40

As propostas para os emigrantes e a diáspora variam significativamente entre os partidos:

**Aliança Democrática (AD)**
*   **Proximidade e Recursos:** Propõe o reforço dos recursos da rede consular e das câmaras de comércio [1], a adaptação e desburocratização dos processos notariais e de registos na rede consular [1], e o estudo da reorganização do agendamento de atos consulares, aproveitando o Consulado Virtual, a Chave Móvel Digital e as Permanências Consulares [5].
*   **Apoio e Integração:** Propõe a criação de um serviço de apoio ao emigrante (com presença online) [1], o desenvolvimento de Gabinetes de Apoio ao Emigrante 2.0 [5] e a criação de Conselhos da Diáspora junto dos municípios [5].
*   **Economia e Investimento:** Pretende realizar um Fórum Anual da Emigração para promover oportunidades de investimento, comércio e emprego [1], além de dar continuidade ao Gabinete de Apoio ao Investidor da Diáspora e ao Plano Nacional de Apoio ao Investidor da Diáspora [5].
*   **Educação e Regresso:** Propõe adaptar a rede de Ensino de Português no Estrangeiro e de Escolas Portuguesas à nova realidade sociológica [5] e dar continuidade ao Programa Regressar [5].

**CHEGA**
*   **Estrutura Política:** Propõe a criação de um **Ministério das Comunidades** para defender os interesses das comunidades e integrá-las no todo nacional [2][12].
*   **Atendimento e Serviços:** Propõe a criação de uma rede de balcões de atendimento com perfil de "Lojas do Cidadão" nos países da diáspora, em substituição dos balcões consulares [12], e a facilitação do acesso aos serviços da administração pública [10].
*   **Participação e Educação:** Defende assegurar a plena participação das comunidades nos processos eleitorais [10][12], garantir uma rede de ensino gratuito de português como língua materna e de História de Portugal [12], e valorizar o Conselho das Comunidades Portuguesas [12].
*   **Outras Medidas:** Propõe incentivos ao retorno [10], a criação de um gabinete de aconselhamento de investimentos [12], a revisão do "Programa Regressar" para incluir Açores e Madeira [12][19] e o apoio às Associações de Portugueses e Casas de Portugal [12].

**Partido Socialista (PS)**
*   **Planeamento e Apoio:** Propõe a elaboração de um **Plano Estratégico para a Diáspora** [3] e o reforço da captação de investimento de empresários da diáspora com acompanhamento personalizado [3].
*   **Serviços e Nacionalidade:** Propõe alocar recursos humanos à rede consular para reduzir tempos de espera [3] e garantir processos de atribuição de nacionalidade mais céleres [3].
*   **Educação e Cultura:** Propõe abolir a propina do ensino da Língua Portuguesa [3] e apoiar o património cultural e a atividade de artistas das comunidades [3].
*   **Social e Mobilidade:** Propõe agilizar o apoio social a emigrantes e idosos carenciados (ASEC e ASIC) [3], garantir ligações aéreas regulares da TAP para países com grandes comunidades [3] e encontrar uma fórmula tributária justa para reformados que mudem a residência fiscal para Portugal [3].
*   **Participação:** Defende dar novo impulso ao movimento associativo, com foco em jovens e mulheres [3].

**LIVRE**
*   **Instituições e Direitos:** Propõe reformar o Conselho das Comunidades Portuguesas, tornando a sua consulta vinculativa, afetando-o à Presidência do Conselho de Ministros e conferindo-lhe orçamento e estrutura [4].
*   **Voto e Democracia:** Defende a possibilidade de voto por correspondência em todos os atos eleitorais (incluindo presidenciais) e o investimento em voto eletrónico não presencial nos círculos da emigração [13].
*   **Serviços e Educação:** Propõe reforçar o serviço do Consulado Virtual e a rede consular [4], além de aprofundar o intercâmbio e reconhecimento entre universidades [4].
*   **CPLP:** Defende o fortalecimento da CPLP como espaço de livre circulação e a criação de uma Convenção sobre Igualdade de Direitos e Deveres entre os Estados-Membros [4].

**Partido Comunista Português (PCP)**
*   **Educação e Cultura:** Defende o reforço da rede de ensino de português no estrangeiro (EPE), a eliminação da propina e a gratuitidade dos manuais escolares [8], bem como a promoção da cultura portuguesa através do Plano Anual de Ação Cultural externa [8].
*   **Conselhos e Direitos:** Pugna pelo reconhecimento e valorização do Conselho das Comunidades como órgão representativo, com autonomia e financiamento adequado [8].
*   **Serviços e Segurança Social:** Propõe a reorganização e reforço da rede consular [8] e a revisão de acordos de Segurança Social para reforçar a proteção de trabalhadores e famílias, incluindo os programas ASEC e ASIC [8].

**Iniciativa Liberal (IL)**
*   **Ensino:** Defende a valorização do ensino do Português como **Língua Materna** para os filhos dos emigrantes [15].
*   **Consulados e Conselho:** Propõe uma reforma da rede consular para diminuir tempos de espera e remunerar funcionários de acordo com o custo de vida local [21], além de reforçar o papel do Conselho das Comunidades Portuguesas [21].

**Bloco de Esquerda (BE)**
*   **Consulados e Saúde:** Propõe o alargamento da rede consular e o reforço dos serviços online e móveis [9], além de revogar as alterações ao Registo Nacional de Utentes (RNU) para garantir que emigrantes tenham acesso a médico e equipa de saúde familiar [7][14].
*   **Educação:** Defende o fim das propinas no ensino do português e a gratuitidade dos manuais escolares [7][9].
*   **Voto e Segurança Social:** Propõe o aumento de assembleias eleitorais nos consulados para voto presencial, o reforço do voto postal [9] e o reforço dos meios da Segurança Social para o pagamento de reformas e pensões no estrangeiro [9].
*   **Cultura:** Propõe o aprofundamento das missões do Instituto Camões e da RTP Internacional [9].

**verdict:** none

**spans:**
-

---

## h09 · q-60

### Pessoas-Animais-Natureza

O PAN compromete-se a continuar empenhado em abolir a tourada e os espetáculos tauromáquicos em Portugal [1]. O partido propõe ainda a retirada de todas as atividades e espetáculos associados à tauromaquia da lista do Património Cultural Imaterial [2]. Adicionalmente, defende a eliminação de todos os apoios públicos, diretos ou indiretos, a tais espetáculos ou atividades tauromáquicas enquanto a abolição não for assegurada [2], bem como a garantia de um fundo para a reconversão de todas as praças de touros em espaços de lazer e/ou cultura que não envolvam atividades lesivas do bem-estar animal até ao final de 2025 [2].

### Partido Socialista

O programa do PS não refere a abolição ou o tratamento específico de espetáculos tauromáquicos.

**Síntese**
O PAN apresenta uma posição de oposição direta e estruturada à tauromaquia, propondo a sua abolição, o fim de apoios públicos e a reconversão das praças de touros, enquanto o programa do PS não aborda o tema.

**verdict:** borderline

**spans:**
- "atividades lesivas do bem-estar animal"

---

## h10 · q-15

### CHEGA

O CHEGA propõe uma série de medidas para assegurar uma imigração regulada e o controlo de fronteiras, baseando-se nas seguintes propostas:

*   **Controlo e Fiscalização:** Reverter a extinção do Serviço de Estrangeiros e Fronteiras (SEF), repondo a sua estrutura orgânica, atribuições e estatuto jurídico e operacional [2][4]. Propõe dotar o Estado de meios para fiscalizar o tráfico de seres humanos e o auxílio à imigração ilegal, aumentando as penas para estes crimes [2][3]. Pretende criar o crime de residência ilegal, impedindo a permanência de imigrantes ilegais e estabelecendo a proibição de regressar ou legalizar a situação em Portugal durante cinco anos [2].
*   **Gestão de Fluxos e Quotas:** Estabelecer quotas anuais de imigração baseadas nas qualificações, nas necessidades do mercado de trabalho e nas mais-valias trazidas para o país [2]. Propõe revogar o acordo de mobilidade com os países da CPLP, acabando com a autorização de residência automática [2].
*   **Nacionalidade e Integração:** Alterar a Lei da Nacionalidade para a atribuir apenas a quem conheça a língua e a cultura portuguesas [2][3]. Promover a integração através do ensino de português (língua não materna), História e Cultura de Portugal, e do acompanhamento das condições de sustentabilidade, habitabilidade e empregabilidade [2].
*   **Repatriamento e Apoios Sociais:** Rever as condições de repatriamento para quem incumprir a lei penal ou não demonstrar capacidade de auto-subsistência num período de 6 a 12 meses [2]. Criar o "Programa Bom Regresso" para apoiar o retorno de pessoas que não tenham meios para o fazer [2]. Propõe regulamentar o acesso a apoios sociais, exigindo um período mínimo de 5 anos de contribuição para o Estado Português [2].
*   **Segurança e Outras Medidas:** Retirar a nacionalidade a cidadãos binacionais que cometam crimes violentos (como terrorismo, homicídio, violação ou violência doméstica) [2]. Garantir a permanência de requerentes de asilo em Centros de Acolhimento Temporários enquanto aguardam decisão [2]. Impedir o avanço do fundamentalismo islâmico e garantir o respeito pela liberdade religiosa e direitos das mulheres e crianças [2]. Publicar relatórios anuais sobre a situação dos imigrantes (emprego, criminalidade, riqueza gerada, etc.) [2].

**Síntese**

O programa do CHEGA foca-se na reestruturação das autoridades de controlo (reposição do SEF), no estabelecimento de quotas baseadas em critérios de utilidade económica e na restrição de benefícios (como a residência automática da CPLP e o acesso a apoios sociais após 5 anos de contribuições). Diferencia-se pela proposta de criminalização da residência ilegal e pela possibilidade de perda de nacionalidade em casos de crimes violentos, contrastando com o modelo de "portas abertas" que o partido critica.

**verdict:** clear

**spans:**
- "permanência de imigrantes ilegais"
- "Impedir o avanço do fundamentalismo islâmico"

---

## h11 · q-32

### Aliança Democrática
O programa deste partido não menciona a energia nuclear.

### Bloco de Esquerda
O programa deste partido não menciona a energia nuclear.

### CHEGA
O partido defende a incorporação da energia nuclear na matriz energética nacional como uma forma de assegurar a soberania e a independência energética [7]. Propõe a modernização de reatores e a utilização de novos pequenos reatores modulares (SMRs), que considera serem mais eficientes, seguros, baratos e rápidos [7]. O partido também defende a promoção da investigação científica sobre a tecnologia nuclear com hidrogénio [9].

### Iniciativa Liberal
O partido defende a realização de uma discussão pública e informada sobre a viabilidade económica da energia nuclear em Portugal, rejeitando preconceitos sobre os seus riscos e impactos ambientais [11]. Propõe que se realizem os estudos necessários para avaliar essa viabilidade [11].

### LIVRE
O partido defende a gestão do risco nuclear em Portugal, especificamente o risco de poluição radioativa no rio Tejo, através da cooperação com Espanha para desenvolver um plano de níveis mínimos de risco na Península Ibérica [12]. Propõe acompanhar o desenvolvimento de novas tecnologias, como os *small modular reactors* (SMR) ou a fusão nuclear, que possam contribuir para a descarbonização [12].

### Pessoas-Animais-Natureza
O programa deste partido não menciona a energia nuclear.

### Partido Comunista Português
O programa deste partido não menciona a energia nuclear.

### Partido Socialista
O programa deste partido não menciona a energia nuclear.

***

**Síntese**
Os partidos que abordam a energia nuclear apresentam abordagens distintas: o CHEGA propõe a sua integração na matriz através de novos reatores modulares (SMRs) [7][9]; a Iniciativa Liberal foca-se na necessidade de debate e estudos de viabilidade económica [11]; e o LIVRE centra a sua posição na gestão de riscos de poluição e no acompanhamento de novas tecnologias como a fusão ou os SMRs [12].

**verdict:** clear

**spans:**
- "rejeitando preconceitos sobre os seus riscos e impactos ambientais"

---

## h12 · q-51

## Aliança Democrática
O programa da Aliança Democrática não aborda a questão da eutanásia.

## Bloco de Esquerda
O Bloco de Esquerda defende a despenalização da morte assistida, considerando-a uma vitória da democracia e da autonomia pessoal [5]. O partido assume o compromisso de exigir que o Governo regulamente com urgência a lei da despenalização da morte assistida, combatendo o que classifica como uma campanha revanchista da direita [5].

## CHEGA
O CHEGA defende a revogação da Lei n.º 22/2023, que regula a morte medicamente assistida, propondo que o tema envolva a sociedade e promova a consciencialização sobre o princípio do direito à vida [Documento 10].

## Iniciativa Liberal
O programa da Iniciativa Liberal não aborda a questão da eutanásia.

## LIVRE
O LIVRE defende a dignificação do fim de vida e a possibilidade de uma morte digna, acompanhando a implementação da legislação de despenalização da morte medicamente assistida [Documento 19]. O partido propõe assegurar apoio médico e psicológico especializado para garantir decisões informadas e conscientes, garantindo que, em situações de sofrimento extremo físico ou psíquico, sejam prestados todos os cuidados possíveis (biológicos, psicológicos e sociais), incluindo cuidados paliativos [Documento 19].

## Pessoas-Animais-Natureza
O programa do PAN não aborda a questão da eutanásia.

## Partido Comunista Português
O programa do Partido Comunista Português não aborda a questão da eutanásia.

## Partido Socialista
O programa do Partido Socialista não aborda a questão da eutanásia.

**Síntese**
Os partidos apresentam posições opostas: o Bloco de Esquerda e o LIVRE defendem a manutenção e regulamentação da morte assistida como um direito à morte digna e autonomia pessoal [5][19], enquanto o CHEGA propõe a revogação da lei que regula a morte medicamente assistida [Documento 10]. Os restantes partidos consultados não referem o tema nos seus programas.

**verdict:** none

**spans:**
-

---

## h13 · q-12

O Partido Socialista (PS) aborda a regionalização como um processo a implementar e aprofundar, visando criar níveis intermédios de decisão legitimados democraticamente para prosseguir os interesses das populações e dos territórios [1].

As principais propostas e visões do PS sobre a regionalização são:

* **Implementação e Roteiro:** O PS propõe estabelecer um roteiro para a regionalização de Portugal continental, promovendo uma análise de custo-benefício [1].
* **Objetivos e Eficiência:** O arranque do processo de regionalização visa assegurar maior proximidade dos cidadãos, maior responsabilidade dos eleitos e a eficiência dos serviços públicos [2].
* **Competências e Gestão:**
    * As futuras Regiões Administrativas deverão receber competências e meios para o planeamento e gestão do transporte público à escala regional [7].
    * O PS pretende aplicar o princípio da descentralização e da subsidiariedade, conferindo às CCDR e às entidades intermunicipais um papel-chave na gestão dos futuros Programas Regionais de gestão dos fundos europeus [1].
    * Pretende-se o empoderamento das Comissões de Coordenação e Desenvolvimento Regional (CCDR) para corrigir défices de coordenação entre financiamento, gestão e implementação de políticas de desenvolvimento territorial [1].
* **Autonomias Regionais (Açores e Madeira):**
    * O PS reafirma o compromisso com o aprofundamento das autonomias e a descentralização político-administrativa, garantindo meios para a boa governação dos territórios açoriano e madeirense [3].
    * Propõe desencadear um processo de revisão constitucional para a reforma e aprofundamento das autonomias insulares, que inclui a eventual extinção da figura do Representante da República e a melhoria da qualidade da democracia regional [3].
    * Prevê a revisão da Lei de Finanças das Regiões Autónomas e a revisão da Lei de Bases da Política de Ordenamento e Gestão do Espaço Marítimo Nacional, para permitir uma maior intervenção das regiões na gestão dos seus espaços marítimos [3].
* **Monitorização:** O partido prevê monitorizar e avaliar, em diálogo com os vários protagonistas, o procedimento de integração dos serviços desconcentrados do Estado nas novas CCDR, IP [1].

**verdict:** none

**spans:**
-

---

## h14 · q-52

### Partido Comunista Português

O programa do PCP não refere a legalização da canábis.

### Síntese

Não é possível estabelecer semelhanças ou diferenças, uma vez que apenas um partido foi consultado e o seu programa não aborda o tema em questão.

**verdict:** none

**spans:**
-

---

## h15 · q-34

As propostas para a redução das listas de espera variam significativamente entre os partidos, abrangendo desde o reforço da capacidade pública até à contratualização com o setor privado:

**Reforço da Capacidade e Recursos do SNS**
* **Aumento de profissionais e serviços públicos:** O **PCP** propõe um programa de emergência assente no aumento da capacidade dos serviços públicos [1]. O **Bloco de Esquerda** defende a contratação e fixação de profissionais para libertar tempo para consultas e cirurgias, além da abertura de concursos em unidades com excesso de horas extraordinárias [5]. O **PS** compromete-se a reforçar o SNS em Meios Complementares de Diagnóstico e Terapêutica (MDTC) e o respetivo pessoal técnico [8].
* **Gestão e Organização:** O **PCP** defende a garantia da gestão pública de todas as unidades [1]. O **LIVRE** propõe a monitorização da organização do SNS e a utilização de sistemas informáticos para agilizar o trabalho [17]. O **PS** propõe a criação de centros de excelência clínica para reduzir o tempo de resposta [9].
* **Cuidados de Proximidade:** O **PCP** propõe reforçar os cuidados primários e garantir uma rede de Urgências Básicas [1]. O **Bloco de Esquerda** defende a descentralização de cuidados como pediatria e ginecologia para mais perto das populações [5]. O **PAN** propõe reforçar as unidades de saúde próximas com meios de diagnóstico para evitar deslocações a hospitais [11].

**Contratualização e Setor Privado/Social**
* **Uso de vouchers e setor privado:** A **Aliança Democrática (AD)** propõe a emissão de um "Voucher Consulta de Especialidade" quando o Tempo Máximo de Resposta Garantido (TMRG) for ultrapassado [3]. A **Iniciativa Liberal (IL)** propõe a criação de um Programa Especial de Acesso a Cuidados de Saúde, com serviços contratualizados através de concurso público de abrangência internacional sempre que os TMRG não sejam cumpridos [4]. O **CHEGA** defende que, em caso de esgotamento dos TMRG, o Estado tem a obrigação de referenciar os utentes para os setores privado ou social [10].
* **Modelo de Sistema de Saúde:** A **IL** defende o modelo "SUA-Saúde", que integra os setores público, privado e social, focando na liberdade de escolha do utente e na concorrência entre prestadores [32]. O **CHEGA** propõe evoluir o SNS para um "Sistema Nacional de Saúde", integrando o setor público, privado e social através de parcerias público-privadas estratégicas [10].

**Medidas Específicas e Tecnológicas**
* **Inovação e Digitalização:** O **CHEGA** propõe a informatização de todo o sistema de saúde para melhorar a coordenação [10]. O **PS** propõe o "Registo de Saúde Eletrónico do Utente" para agilizar o acesso à informação [31]. O **LIVRE** defende a transição digital para diminuir a burocratização [17].
* **Cirurgias:** A **AD** propõe o desenvolvimento de Centros de Responsabilidade Integrados (CRIs) públicos de segunda geração e a criação de um sistema concorrencial para cirurgia de ambulatório [3].

**verdict:** none

**spans:**
-

---

## h16 · q-31

### Bloco de Esquerda

O Bloco de Esquerda defende o estabelecimento da semana de quatro dias através de um programa que combine a adesão voluntária das empresas com a via normativa [1]. Propõe que, para as empresas que optem por este modelo, sejam fixadas, a partir de 2028, as 32 horas semanais [1]. O partido defende que esta organização deve ser acompanhada por uma redução do horário de trabalho semanal sem perda de salário mensal [1]. Adicionalmente, propõe consagrar na lei a possibilidade de opção pela semana de quatro dias, também por iniciativa do trabalhador, estando esta vinculada à redução do horário de trabalho semanal e sem perda de rendimento [2].

### LIVRE

O LIVRE defende a continuação da experiência da semana de quatro dias tanto no setor privado como na administração pública [7]. O partido pretende promover a inclusão desta modalidade na contratação coletiva e nos acordos de empresa, trabalhando para que se realize uma experiência a nível nacional de um período de semanas de quatro dias [7]. O programa menciona que esta medida visa responder à necessidade de uma vida que não gire exclusivamente em torno do trabalho, permitindo a conciliação entre trabalho e família e o acesso ao lazer e descanso [8].

### Síntese

Ambos os partidos defendem a implementação da semana de quatro dias sem perda de rendimento e através da contratação coletiva [1][2][7]. Enquanto o Bloco de Esquerda propõe um cronograma normativo específico que fixa as 32 horas semanais para quem aderir ao modelo a partir de 2028 [1], o LIVRE foca-se na expansão de experiências já existentes para o setor público e privado, visando uma experiência de âmbito nacional [7].

**verdict:** none

**spans:**
-

---

## h17 · q-07

### Iniciativa Liberal

A Iniciativa Liberal pretende garantir um médico de família para todos até 2028 [4], estabelecendo como meta prioritária que as pessoas com mais de 65 anos, mulheres grávidas e crianças até aos 9 anos disponham de médico de família até ao final de 2025 [1][3][4]. Para alcançar este objetivo, o partido propõe as seguintes medidas:

*   **Modelo de prestação:** O sistema deve integrar os setores público, privado e social, permitindo que o médico de família possa ser público ou privado [3][4]. A estratégia inclui o reforço do SNS através de Unidades de Saúde Familiar de Modelo C (USF-C) direcionadas para as faixas etárias prioritárias e a contratualização com serviços de saúde do setor privado e social sempre que necessário [1][5].
*   **Gestão e estrutura:** Defende a expansão das USF-B e a implementação das USF-C [4]. Propõe um novo sistema de saúde que permita aos utentes escolher onde e por quem querem ser tratados, sem custos acrescidos além dos existentes [4].
*   **Foco e incentivos:** O foco deve ser o utente e não quem presta o serviço, apostando na medicina preventiva [2]. Propõe ainda a implementação de uma remuneração variável consoante o desempenho para todos os profissionais de saúde [4].

**Síntese**

A estratégia da Iniciativa Liberal assenta na integração de setores (público, privado e social) e na liberdade de escolha do utente para resolver a falta de médicos de família [2][4]. O plano estabelece um cronograma de execução com metas intermédias para grupos vulneráveis (idosos, grávidas e crianças) até 2025, visando a cobertura universal até 2028 [1][3][4].

**verdict:** borderline

**spans:**
- "O foco deve ser o utente e não quem presta o serviço"

---

## h18 · q-03

A Aliança Democrática (AD) propõe as seguintes medidas relativas ao **IRS Jovem**:

*   **Adoção duradoura e estrutural**: o partido pretende adotar o IRS Jovem de forma duradoura e estrutural [1].
*   **Redução de taxas**: a proposta implica uma redução de 2/3 nas taxas atualmente aplicáveis, estabelecendo uma **taxa máxima de apenas 15%** [1][2].
*   **Âmbito de aplicação**: a medida aplica-se a todos os **jovens até aos 35 anos**, com exceção do último escalão de rendimentos [1].
*   **Objetivo**: a medida procura reforçar os rendimentos dos jovens e reconhecer a perda gerada pela emigração massiva [4].
*   **Impacto orçamental**: a adoção do IRS Jovem tem um impacto orçamental previsto de **1.000 milhões de euros** para o ano de 2025 [3].

**verdict:** borderline

**spans:**
- "taxa máxima de apenas 15%"
- "reconhecer a perda gerada pela emigração massiva"

---

## h19 · q-35

As propostas para baixar as rendas e o preço da habitação variam significativamente entre os partidos:

**Medidas para baixar as rendas (Controlo e Subsídios):**

* **Controlo de preços e tetos máximos:**
    * O **Bloco de Esquerda** propõe a fixação de tetos máximos para rendas, inferiores aos valores da Portaria n.º 277-A/2010, considerando a área, qualidade, localização e tipologia [17], combinando esta medida com a limitação da atualização das rendas face ao poder de compra [17]. Defende também a limitação do aumento das rendas considerando a evolução do poder de compra [1].
    * O **LIVRE** propõe estabelecer limites máximos nas rendas por um período de pelo menos cinco anos para imóveis de proprietários que recebam financiamento estatal [9]. Propõe ainda que os novos contratos de arrendamento não excedam uma majoração de 30% dos limites gerais de preço de renda por tipologia previstos em portaria [9].
    * O **Partido Comunista Português (PCP)** defende a criação de um regime especial de proteção de inquilinos que limite o aumento das rendas e o seu valor em novos contratos [2].
    * A **Aliança Democrática (AD)** opõe-se ao controlo administrativo de preços e ao congelamento de rendas, argumentando que estas medidas prejudicam o investimento e a renovação de imóveis [4]. Propõe, em alternativa, a substituição de limitações de preços por subsidiação pública aos arrendatários em situações de vulnerabilidade [7].
    * A **Iniciativa Liberal (IL)** rejeita a fixação de rendas, afirmando que estas propostas levam a uma menor oferta a longo prazo [5].

* **Subsídios e apoios financeiros:**
    * O **Bloco de Esquerda** defende a aplicação de apoios ao pagamento de rendas [24].
    * O **LIVRE** propõe o reforço do apoio extraordinário à renda, reduzindo a taxa de esforço de referência para 30% e aumentando o valor máximo do apoio para 300 euros [29].
    * A **Aliança Democrática (AD)** propõe um subsídio de renda dinâmico que garanta comparticipação a famílias com taxas de esforço elevadas, verificando o universo de contratos frequentemente [7].
    * O **PAN** pretende rever o Programa Porta 65, aumentando os valores de renda máxima e a dotação orçamental [3].

**Medidas para baixar o preço da habitação (Oferta e Fiscalidade):**

* **Aumento da oferta e habitação pública:**
    * O **PCP** propõe um investimento público reforçado para a construção de 50.000 fogos de habitação pública [26].
    * O **LIVRE** defende atingir 10% de habitação pública (600 mil fogos) através de investimento contínuo e aplicação de fundos do PRR [35].
    * O **Partido Socialista (PS)** propõe atingir, no médio prazo, 5% de parque público de habitação através de investimento na requalificação e alargamento do parque existente [6].
    * O **Bloco de Esquerda** propõe que 25% da nova construção seja destinada a habitação acessível (regime de renda condicionada) [31].
    * A **Aliança Democrática (AD)** defende um "choque de oferta" através da flexibilização de limites de ocupação de solos, densidades urbanísticas e simplificação do licenciamento [21].
    * A **Iniciativa Liberal (IL)** propõe aumentar a oferta através da criação de um regime de incentivo à nova construção para arrendamento (*build-to-rent*) [15][27].
    * O **CHEGA** propõe a criação de parcerias público-privadas para disponibilizar terrenos para construção e estimular a construção de habitação acessível em terrenos públicos com concessão de 90 anos [22].

* **Medidas fiscais e de mercado:**
    * **Redução de impostos e custos:**
        * A **Iniciativa Liberal (IL)** propõe a eliminação do IMT na compra de habitação própria permanente [15][19], a isenção de imposto de selo em transações imobiliárias e arrendamentos [15][19], e a redução do IVA da nova construção de 23% para 6% [15]. Propõe ainda baixar a taxa autónoma sobre rendimentos prediais para 14,5% (em contratos até 5 anos) [14].
        * O **CHEGA** propõe abolir o IMT na aquisição de habitação própria permanente [22], revogar o AIMI [22] e isentar do IVA a construção da primeira habitação [22].
        * O **LIVRE** propõe aumentar o imposto sobre as mais-valias para controlar a especulação [9].
        * O **PS** propõe aumentar a despesa dedutível com arrendamento em IRS em 50 € por ano até atingir os 800 € [6][36].
    * **Restrições à especulação:**
        * O **Bloco de Esquerda** propõe a proibição da venda de casas a não residentes [31] e a limitação do Alojamento Local a um máximo de 5% por freguesia [31].
        * O **PCP** propõe limitar a aquisição de habitações por fundos imobiliários e limitar o Alojamento Local em áreas de carência habitacional [2][8].
        * O **LIVRE** propõe o fim dos Vistos *Gold* e dos benefícios fiscais para residentes não habituais e nómadas digitais [9].
        * O **CHEGA** defende a revogação do arrendamento forçado de imóveis devolutos e a revogação dos Vistos *Gold* [22].

**verdict:** borderline

**spans:**
- "Restrições à especulação"

---

## h20 · q-11

### Iniciativa Liberal

A Iniciativa Liberal defende a realização de uma discussão pública e informada sobre a viabilidade económica da energia nuclear em Portugal, rejeitando preconceitos sobre os seus riscos e impactos ambientais [1]. O partido manifesta uma visão positiva quanto ao renascimento do investimento em energia nuclear na União Europeia, incluindo o desenvolvimento de novas modalidades de produção em unidades mais pequenas (SMR) [1]. Propõe, por isso, que se proceda à realização e discussão dos estudos necessários para aferir a viabilidade económica desta fonte de energia no país [1].

### Síntese

O programa da Iniciativa Liberal não apresenta uma posição de apoio ou rejeição definitiva à energia nuclear, mas sim uma postura de abertura ao debate técnico e económico, propondo a realização de estudos de viabilidade para decidir o futuro da tecnologia em Portugal [1].

**verdict:** clear

**spans:**
- "rejeitando preconceitos sobre os seus riscos e impactos ambientais"
