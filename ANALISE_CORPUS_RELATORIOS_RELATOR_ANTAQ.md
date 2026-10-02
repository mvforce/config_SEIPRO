# Análise do corpus de Relatórios do Relator da ANTAQ

## 1. Escopo da amostra

Foram examinados 12 Relatórios do Relator constantes dos arquivos encaminhados, todos produzidos no âmbito da Assessoria da Diretoria D1. Embora os documentos estejam formalmente vinculados a relatores distintos, a elaboração material do texto é realizada pela assessoria, especialmente pela assessora Gabriella, em nome da Diretoria. Por essa razão, o corpus deve ser lido como expressão de um padrão redacional da D1, e não como soma de estilos pessoais dos Diretores.

A amostra abrange, entre outros, os seguintes tipos de matéria:

- processo administrativo sancionador;
- recurso hierárquico em processo sancionador;
- pedido de medida cautelar;
- procedimento licitatório com deliberação ad referendum;
- análise de projeto de investimento;
- alteração de cronograma e prorrogação do início da operação de TUP;
- outorga de autorização de instalação portuária.

A extensão do corpo narrativo varia bastante conforme a complexidade. Na amostra, os relatórios têm, aproximadamente, de 370 a 2.135 palavras no corpo útil, com mediana próxima de 1.060 palavras. Os parágrafos são relativamente longos, com média aproximada de 51 palavras, e as frases também tendem a ser extensas.

## 2. Conclusão central sobre a natureza do documento

O Relatório do Relator não funciona como uma nota técnica nem como um voto abreviado. Sua função predominante é reconstruir a marcha processual e colocar o processo em condições de julgamento.

A técnica redacional recorrente consiste em:

1. identificar imediatamente o objeto do processo;
2. expor o pedido, a imputação ou a controvérsia originária;
3. registrar os argumentos relevantes das partes;
4. reconstruir, em ordem lógica e predominantemente cronológica, as manifestações das unidades técnicas e das chefias;
5. indicar a posição conclusiva de cada unidade, atribuindo expressamente a conclusão a quem a formulou;
6. encerrar sem desenvolver juízo autônomo de mérito, com a fórmula "Era o que cumpria relatar.".

A separação entre relatório e voto é um traço essencial. O relatório pode reproduzir conclusões técnicas fortes, interpretações jurídicas e propostas decisórias, mas normalmente as apresenta como conteúdo de outra peça, e não como conclusão própria do relator.

## 3. Estrutura externa estável

### 3.1. Cabeçalho institucional

Os documentos seguem cabeçalho padronizado da ANTAQ, com identificação da Assessoria da Diretoria.

Em seguida aparecem os campos:

- **Processo:** número do processo substantivo ou originário tratado no relatório;
- **Tipo:** classificação processual;
- **Interessado:** interessado ou interessados principais;
- **Contextualização:** descrição muito curta da matéria;
- **Relator:** nome do diretor ou diretora relatora.

### 3.2. Atenção especial ao número do processo

Há uma característica importante no corpus: o número indicado no campo **Processo** do cabeçalho nem sempre coincide com o processo SEI que contém o próprio Relatório do Relator e aparece na referência final do documento.

Portanto, o agente não deve copiar automaticamente o número do processo corrente para o cabeçalho. Deve distinguir:

- processo de deliberação ou tramitação em que o relatório está sendo produzido;
- processo originário ou substantivo objeto do julgamento.

Essa distinção deve ser conferida documentalmente.

### 3.3. Corpo

O corpo começa diretamente com a narrativa. Não há, na amostra, uma seção autônoma intitulada "RELATÓRIO".

A abertura mais recorrente é uma destas:

- "Tratam os autos de...";
- "Trata-se de...";
- "Os presentes autos se prestam a...", especialmente em matéria de referendo.

### 3.4. Fecho

O fecho é extremamente estável:

> Era o que cumpria relatar.

Nos documentos do corpus, podem constar, após essa fórmula, o nome do relator e a respectiva função. Contudo, para fins de geração pelo agente, o comando deve ser diverso: após "Era o que cumpria relatar.", o documento deve ser encerrado, deixando em branco o espaço destinado à assinatura, ao nome e à função do Diretor.

## 4. Fluxo lógico do corpo

O padrão geral é mais processual do que temático. O relatório acompanha o caminho do processo.

### 4.1. Primeiro movimento: objeto

O primeiro parágrafo concentra grande densidade informacional. Em regra, contém:

- natureza do processo;
- nome da parte;
- CNPJ, quando relevante;
- ato, contrato, auto de infração, petição ou requerimento que originou a matéria;
- síntese da pretensão ou do fato controvertido;
- referência SEI dos documentos principais.

O parágrafo inicial deve permitir que o leitor compreenda o que está sendo decidido antes de conhecer o histórico.

### 4.2. Segundo movimento: contexto material mínimo

Quando necessário, vêm dados que explicam o objeto, tais como:

- área e localização;
- carga e capacidade operacional;
- investimentos;
- prazo contratual;
- cronograma;
- tipificação sancionadora;
- conteúdo da decisão recorrida;
- fundamento do pedido cautelar.

O relatório não procura esgotar tecnicamente esses elementos. Seleciona o que é necessário para compreender a tramitação e as posições técnicas posteriores.

### 4.3. Terceiro movimento: posição da parte

Nos casos contenciosos, aparecem de forma destacada:

- defesa;
- recurso;
- pedido cautelar;
- pedidos finais;
- fundamentos principais.

Há dois modos de apresentação no corpus:

1. síntese narrativa dos argumentos;
2. reprodução quase literal ou literal de itens da defesa, pedido ou documento técnico quando a formulação exata é relevante.

### 4.4. Quarto movimento: instrução técnica

A peça técnica principal é identificada pelo nome completo e número SEI. Em seguida o relatório registra:

- o que a unidade analisou;
- critérios utilizados;
- fatos relevantes considerados;
- conclusão técnica;
- proposta de encaminhamento.

A regra de redação mais importante é a atribuição da autoria. Exemplos de construção recorrente:

- "a área técnica concluiu que...";
- "a setorial técnica destacou que...";
- "o opinativo técnico consignou que...";
- "a Gerência se manifestou...";
- "a SFC entendeu...";
- "a SOG recomendou...".

### 4.5. Quinto movimento: manifestações hierárquicas

Depois da peça técnica, o relatório normalmente sobe a cadeia decisória:

- servidor ou equipe técnica;
- gerência;
- superintendência;
- eventualmente Diretoria, Poder Concedente ou órgão externo.

A transição costuma ser marcada por expressões como:

- "Ato seguinte,...";
- "Na mesma direção,...";
- "Por sua vez,...";
- "Em sua primeira análise sobre a matéria,...";
- "De posse dessas informações,...";
- "Por fim,...".

### 4.6. Último movimento: posição conclusiva que chegou ao relator

O relatório termina expondo a recomendação conclusiva da unidade técnica ou dirigente competente. Se houver proposta em itens, ela pode ser reproduzida.

O relator não deve, nessa etapa, converter a conclusão técnica em conclusão própria. A formulação deve preservar a autoria da recomendação.

## 5. Padrões por tipo de processo

### 5.1. Processo sancionador

Fluxo típico:

1. identificação do Auto de Infração;
2. descrição do fato infracional;
3. tipificação;
4. notificação e defesa;
5. síntese ou reprodução dos argumentos da autuada;
6. pedidos da defesa;
7. Parecer Técnico Instrutório;
8. posição da chefia regional ou gerência;
9. posição da SFC;
10. eventual divergência entre instâncias;
11. fecho.

Nos sancionadores, a reprodução documental é mais intensa do que nos demais tipos de processo.

### 5.2. Recurso hierárquico

Fluxo típico:

1. decisão recorrida e penalidade aplicada;
2. fundamentos recursais;
3. análise técnica do recurso;
4. fatos ou decisões supervenientes relevantes;
5. remessa à Diretoria;
6. fecho.

### 5.3. Pedido cautelar

Fluxo típico:

1. identificação do requerente e da medida pretendida;
2. fundamentos do requerente;
3. pedidos formulados;
4. análise preliminar de fiscalização ou outra unidade;
5. análise regulatória dos requisitos da cautelar;
6. manifestação gerencial;
7. manifestação da superintendência;
8. fecho.

O relatório descreve o exame de fumus boni iuris, periculum in mora e risco reverso quando essas categorias estiverem efetivamente presentes nas peças técnicas, mas não deve criar avaliação própria.

### 5.4. Outorga e alteração de cronograma

Fluxo típico:

1. pedido e identificação do empreendimento;
2. competência da ANTAQ e, quando necessário, do Poder Concedente;
3. contextualização do contrato e dos prazos;
4. justificativas da autorizatária;
5. critérios técnicos aplicados;
6. análise de exequibilidade;
7. situação de licenciamento e fiscalização;
8. manifestação da gerência;
9. manifestação da SOG;
10. proposta de encaminhamento;
11. fecho.

### 5.5. Investimentos e As Built

Fluxo típico:

1. objeto do investimento e base contratual;
2. histórico regulatório relevante;
3. fiscalização da execução física;
4. dimensão financeira;
5. comparação com EVTEA ou parâmetro regulatório;
6. documentação comprobatória;
7. análise patrimonial ou contábil, quando existente;
8. conclusão técnica;
9. manifestação da Superintendência;
10. urgência ou conexão com outros processos, se houver;
11. fecho.

## 6. Estilo redacional extraído do corpus

### 6.1. Registro

O registro é jurídico-administrativo, formal e descritivo. Há forte preferência por verbos que indicam atos processuais e posicionamentos institucionais.

Verbos recorrentes:

- requerer;
- consignar;
- concluir;
- destacar;
- ressaltar;
- reconhecer;
- manifestar-se;
- recomendar;
- acompanhar;
- atestar;
- registrar;
- afastar;
- encaminhar;
- restituir;
- anuir;
- deliberar.

### 6.2. Terminologia institucional recorrente

- autos;
- pleito;
- Requerente;
- Recorrente;
- Autuada;
- Arrendatária;
- Autorizatária;
- interessada;
- setorial técnica;
- área técnica;
- opinativo técnico;
- instrução processual;
- manifestação técnica;
- Despacho;
- Nota Técnica;
- Parecer Técnico;
- deliberação;
- Diretoria Colegiada;
- unidade técnica;
- autoridade julgadora;
- Poder Concedente.

A designação da parte varia conforme sua posição processual. O relatório procura evitar o uso repetitivo do nome empresarial quando uma qualificação processual é suficiente.

### 6.3. Conectores e fórmulas de progressão

Muito recorrentes:

- "De acordo com...";
- "Em síntese,...";
- "No que toca...";
- "Com relação a...";
- "Nesse contexto,...";
- "Consoante se extrai...";
- "Adicionalmente,...";
- "Ademais,...";
- "Ato seguinte,...";
- "Na mesma direção,...";
- "Por sua vez,...";
- "Diante da documentação apresentada,...";
- "Por fim,...".

Há preferência por conectores que marcam a posição de cada ato dentro da cadeia processual.

### 6.4. Referenciação documental

O padrão é identificar o documento e inserir a referência SEI imediatamente após sua menção, por exemplo:

- Nota Técnica nº X/AAAA/UNIDADE (SEI nº XXXXXXX);
- Despacho SOG (SEI nº XXXXXXX);
- Petição (SEI nº XXXXXXX);
- Acórdão nº XXX/AAAA-ANTAQ (SEI nº XXXXXXX).

A rastreabilidade documental é parte essencial do estilo.

### 6.5. Uso de números e grandezas

O corpus mantém muitos valores e medidas no corpo quando são materialmente relevantes para compreender a controvérsia. É comum apresentar:

- valor numérico;
- valor por extenso em seguida, especialmente para montantes financeiros;
- percentuais;
- datas-base;
- áreas;
- prazos;
- capacidades.

O agente deve preservar números exatamente como constam da fonte e cruzá-los quando o processo apresentar valores divergentes.

## 7. Variações internas do padrão redacional da D1

As diferenças observadas entre os relatórios não devem ser atribuídas, em princípio, a estilos pessoais dos Diretores formalmente indicados como relatores. Considerando que a elaboração material é realizada pela assessoria da D1, especialmente pela assessora Gabriella, o núcleo do estilo deve ser tratado como institucional e relativamente estável.

As variações encontradas no corpus parecem decorrer principalmente de três fatores:

- natureza do processo;
- complexidade da matéria;
- quantidade e densidade das peças instrutórias disponíveis.

### 7.1. Processos sancionadores e contenciosos

Nesses casos, o texto tende a:

- reproduzir com maior detalhe os fatos infracionais;
- registrar de forma mais extensa a defesa, o recurso e os pedidos;
- acompanhar mais rigidamente a sequência dos atos processuais;
- empregar com maior frequência fórmulas de transição como "Ato seguinte" e "Na mesma direção".

### 7.2. Outorgas, investimentos e matérias regulatórias

Nesses casos, o texto tende a:

- desenvolver mais a contextualização inicial;
- incorporar maior quantidade de informações técnicas, operacionais, financeiras e contratuais;
- explicitar com maior cuidado a sequência entre Gerência e Superintendência;
- sintetizar de forma mais explicativa as Notas Técnicas e demais opinativos.

### 7.3. Núcleo estável do padrão D1

Independentemente do tipo processual, permanecem recorrentes:

- abertura objetiva pelo objeto;
- narrativa predominantemente processual;
- elevada rastreabilidade SEI;
- atribuição clara das conclusões às respectivas unidades;
- ausência de conclusão própria de mérito no relatório;
- uso de conectores burocrático-administrativos recorrentes;
- fechamento com "Era o que cumpria relatar.";
- ausência, na versão gerada pelo agente, de assinatura, nome ou identificação do Diretor após o fecho.

## 8. Vícios de linguagem e falhas encontradas

As marcas abaixo integram a impressão digital do corpus. Para fins de geração pelo agente, deve-se distinguir entre vícios estilísticos intencionais, que podem e devem ser preservados de forma moderada para manter o tom humano do texto, e erros materiais, de digitação ou de conteúdo, que não devem ser reproduzidos. A imperfeição admitida é de forma, nunca de precisão factual.

### 8.1. Regência, crase e construções recorrentes a preservar

Foram encontrados exemplos como:

- "À título de contextualização";
- "corroborou com a análise";
- "procedeu as diligências";
- "Adentrando aos aspectos financeiros".

Essas construções, embora possam ser consideradas inadequadas sob uma revisão normativa estrita, devem ser tratadas pelo agente como marcas estilísticas possíveis do padrão D1. O comando não deve corrigi-las automaticamente. Seu emprego deve ser ocasional e natural, evitando concentração artificial de vícios em um mesmo parágrafo.

### 8.2. Concordância e revisão

Há ocorrências como:

- "o Superintendência";
- "que única pendência";
- construções com concordância verbal ou nominal fragilizada em períodos longos.

### 8.3. Erros materiais e digitação

Foram observados, entre outros:

- "exploraração";
- "outogas";
- "corrobou";
- "manifetou";
- "Grerente";
- "Licenciamente";
- "clausúla";
- "montanto".

Também há ao menos um risco de inconsistência geográfica, com menção a Caracaraí/PA em trecho que, no restante do documento, se refere a Caracaraí/RR.

### 8.4. Vícios sintáticos que compõem o tom do corpus

Podem ser preservados, de forma controlada:

- períodos extensos, com várias orações coordenadas e subordinadas;
- repetição de "por meio de", "nos termos de", "mediante" e "conforme";
- uso recorrente de "fora" como pretérito mais-que-perfeito simples;
- uso ocasional de "onde" para referência a documento ou ato;
- uso de "o mesmo" como pronome de retomada;
- nominalizações como "análise empreendida", "manifestação técnica empreendida" e "apreciação técnica da matéria";
- cadeias de gerúndios e construções burocráticas mais pesadas.

Esses elementos não devem ser eliminados por uma rotina de "melhoria estilística". Eles ajudam a afastar uma redação excessivamente polida, homogênea ou artificial. Ainda assim, o agente deve evitar que a soma desses traços prejudique a inteligibilidade. Duplicidades objetivamente erradas, como "prazo de 18 meses (dezoito) meses", continuam sendo falhas de revisão e não devem ser deliberadamente inseridas.

### 8.5. Inconsistências de padronização

Há variação entre:

- ANTAQ, Antaq e -ANTAQ;
- SEI nº e SEI n.;
- Arrendatária e arrendatária;
- Requerente e requerente;
- formas diferentes de citar artigos, resoluções e valores.

Essas variações podem ser preservadas quando já estiverem presentes nas fontes ou quando surgirem naturalmente no texto, desde que não gerem ambiguidade ou erro de identificação. O agente não deve fazer uma higienização estilística excessiva apenas para uniformizar o documento.

## 9. Riscos que o agente deve controlar

### 9.1. Transformar o relatório em voto

É o principal risco. Expressões como "entendo", "considero", "concluo" e "deve ser" somente devem ser usadas como posição própria quando o documento-fonte comprovar que se trata de ato anterior do próprio relator. Em regra, o relatório deve dizer quem entendeu, considerou ou concluiu.

### 9.2. Inventar conexão causal

O agente não pode preencher lacunas da cronologia com inferências. Se a relação entre dois documentos não estiver clara, deve descrevê-los separadamente ou sinalizar a ausência de informação.

### 9.3. Confundir processo corrente e processo originário

O número do processo do cabeçalho precisa ser conferido. A amostra comprova que ele pode ser diferente da referência SEI final.

### 9.4. Reproduzir erro da fonte como se fosse fato validado

Ao sintetizar documento de terceiro, o agente deve atribuir a informação: "a Requerente informou", "a área técnica registrou". Isso é particularmente importante quando os dados não foram verificados por outra peça.

### 9.5. Omitir divergência interna

Se parecer, gerência e superintendência não coincidirem, o relatório deve preservar a divergência. Não deve fundir as posições em uma falsa conclusão institucional única.

## 10. O que os processos originários acrescentariam

Os relatórios encaminhados são suficientes para extrair com boa segurança:

- estrutura externa;
- estilo;
- terminologia;
- encadeamento;
- fórmulas de abertura e fechamento;
- padrão de referência documental;
- diferenças por tipo processual;
- vícios recorrentes.

Contudo, os relatórios, isoladamente, não permitem reconstruir com a mesma segurança a **regra de seleção da informação**, isto é, por que determinado documento do processo foi mencionado e outro foi omitido, quanto de cada Nota Técnica foi condensado e em quais situações o relator preferiu transcrever literalmente.

Para calibrar essa segunda camada, seria útil comparar alguns destes relatórios com seus processos originários completos. Essa etapa não é necessária para a versão inicial do skill, mas é recomendável para transformá-lo em um skill de geração autônoma a partir de processos extensos.
