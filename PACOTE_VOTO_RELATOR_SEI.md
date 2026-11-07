---
name: elaboracao-voto-relator-sei
description: Redige a parte textual de Voto do Relator da ANTAQ, a partir dos elementos fornecidos, preservando a estrutura SEI, a voz decisória, o ritmo argumentativo e a correspondência entre fundamentos e dispositivo. Não substitui a análise técnica nem executa atos no SEI.
---

# Elaboração de Voto do Relator: redação e estrutura SEI

## 1. Finalidade e limites

Elaborar **o documento Voto do Relator**, e não um despacho da GPO, uma Nota Técnica, um relatório de tramitação ou um acórdão. A tarefa é converter os elementos efetivamente disponíveis em fundamentação decisória e proposta de deliberação, com linguagem, ritmo e organização compatíveis com os votos de referência.

Esta skill cuida da **estrutura, parte textual, apresentação e dispositivo**. Não estabelece fluxo de auditoria integral do processo, confirmação item a item, seleção de documentos por cartões, criação no SEI, assinatura ou tramitação. A consulta a documentos serve à fidelidade da redação, sem ampliar automaticamente o trabalho para reanálise econômica, jurídica ou regulatória de toda a instrução.

O voto deve indicar **o que se decide, por quais razões e com quais efeitos**. A concordância com a área técnica não elimina a necessidade de tornar compreensível a razão decisiva. A divergência não autoriza inventar tese, fato, cálculo ou posição do relator.

**Regra central:** sintetizar a instrução, delimitar a questão decisória, explicitar o juízo do relator e formular comandos correspondentes. Não reproduzir o processo em ordem cronológica nem transportar conclusões de outros casos.

## 2. Base de referência e alcance do padrão

A referência empírica desta versão são os oito PDFs fornecidos pelo usuário. Os localizadores abaixo permitem recuperar os exemplos sem depender da memória da conversa.

| Arquivo | Voto SEI | Exemplo de construção textual | Trechos de referência |
|---|---|---|---|
| VT01.pdf | 2534586 | Marimex: dependência entre projetos, elemento superveniente, solução temporal e separação de competências | §§ 2-14; dispositivo I-V |
| VT02.pdf | 2570215 | TPAR: comando anterior, tratamento dos pontos determinados e alteração de item específico de acórdão | §§ 2-10; dispositivo I-III |
| VT03.pdf | 2573357 | TES: explicação de mecanismo financeiro e ratificação de decisão anterior | §§ 2-7; dispositivo I-V |
| VT04.pdf | 2636852 | Coamo: integração de manifestações de diferentes unidades e escolha pontual entre GPO e SOG | §§ 3-13; dispositivo I-X |
| VT05.pdf | 2689522 | TEMAPE: contextualização espacial, divergência metodológica identificada e escolha do relator | §§ 2-16, sobretudo 9-14; dispositivo I-VII |
| VT06.pdf | 2736186 | VPorts: delimitação de alternativas e resposta a consulta organizada em alíneas | §§ 2-18; dispositivo I, alíneas a-c, e II |
| VT07.pdf | 2771220 | Coamo: questionamento posterior, distinção de datas-base e proposta de retificação | §§ 2-6; dispositivo I-VII |
| VT08.pdf | 2900685 | PAR05: competência, acolhimento por remissão e aprovação condicionada a ajustes identificados | §§ 3-4 e 9-14; dispositivo I-II |

VT01 a VT07 são subscritos por Flávia Morais Lopes Takafashi; VT08 é subscrito por Cristina Castro Lucas de Souza. Adotar a estrutura comum e o ritmo predominante, sem atribuir a todas as relatorias as particularidades de uma delas. Se houver modelo do gabinete destinatário, ele prevalece nos aspectos formais e nas fórmulas de redação.

Os exemplos são **referências de redação**, não precedentes automaticamente aplicáveis. Não incorporar seus valores, áreas, prazos, normas, conclusões concorrenciais, comandos de sigilo ou destinatários a um novo voto.

A amostra não contém modelos específicos de voto em recurso, medida cautelar, processo sancionador ou voto-vista. Não anunciar que essas espécies estão calibradas pelos oito documentos; aproveitar apenas a estrutura geral até haver referência específica.

## 3. Entradas e tratamento de lacunas

Reunir, dos documentos e das instruções já fornecidos:

- processo de mérito; eventual processo de deliberação; interessado; objeto; instrumento contratual, quando pertinente; identificação do relator, se confirmada;
- questão submetida à decisão e resultado pretendido, quando já definido;
- manifestações técnicas, jurídicas e gerenciais relevantes, suas referências SEI e eventuais posições diferentes;
- fatos, parâmetros, condições e atos anteriores necessários para sustentar a proposta;
- relatório do relator e HTML nativo do voto, se disponíveis.

Não pedir novamente informações já fornecidas. Não exigir o processo integral apenas para reproduzir linguagem e estrutura. Para redigir voto concreto, solicitar somente a peça cuja ausência comprometa uma afirmação ou comando material, explicando sua finalidade.

Na falta de elemento essencial, produzir o que estiver sustentado e identificar a lacuna fora do corpo do documento. Em **modelo ou minuta de trabalho**, admitir campos claros entre colchetes. Em **versão final**, não deixar campos não resolvidos nem preencher lacunas por presunção. Não classificar como pronto para assinatura um texto que depende de confirmação material.

Não interpretar uma instrução de estilo ou um pedido para redigir como concordância do relator com determinada conclusão. Quando a orientação não estiver definida, apresentar a posição proposta com base nas fontes, sem atribuir-lhe aprovação já ocorrida.

## 4. Arquitetura do documento

A ordem de referência é a seguinte. Os nomes dos blocos são instruções de elaboração, **não títulos a inserir automaticamente no voto**.

### 4.1. Identificação inicial, sem numeração

Preservar, nesta ordem, os campos observados na amostra:

```text
Processo: [processo de mérito confirmado]
Tipo: [tipo processual confirmado]
Interessado: [denominação confirmada]
Contextualização: [objeto concreto em uma ou duas frases]
Relator: [nome confirmado]
```

O campo `Tipo` descreve a classificação do processo. Não o preencher com `Voto do Relator`, que é a espécie documental. Não substituir `Contextualização` por uma ementa longa ou por histórico do processo.

Não confundir o processo indicado nesse cabeçalho com o processo eventualmente apresentado na referência automática do rodapé. A amostra contém numerações diferentes nesses dois lugares; a relação entre elas depende da árvore e da instrução, não da aparência do PDF.

Preservar os elementos institucionais do modelo nativo, quando fornecido. Não copiar o logotipo, o nome da relatoria ou os metadados de um voto anterior como dados do caso novo.

### 4.2. Certificação inicial

Os oito votos abrem o corpo numerado com certificação de regularidade e aptidão para deliberação. A fórmula predominante é:

> Certifico que o processo está devidamente instruído, regular e apto a ser submetido à deliberação da Diretoria Colegiada; bem como atesto a observância do disposto no art. 11, inciso I, da Resolução ANTAQ nº 66/2022.

**Essa declaração não é enfeite de formulário.** Inserir a redação institucional somente quando a situação processual e a referência normativa estiverem verificadas para o caso, e submetê-la à validação do gabinete. O fato de constar dos modelos não comprova a regularidade de outro processo nem a aplicabilidade temporal do dispositivo.

Se isso não puder ser confirmado, manter a posição do bloco no modelo de trabalho com indicação de pendência, comunicada fora da minuta final. Não afirmar que a própria IA certificou a instrução. Também não alterar silenciosamente a declaração para ocultar a falta de suporte.

### 4.3. Objeto da deliberação

Após a certificação, abrir com formulação direta:

> Encontra-se para deliberação [pedido, consulta, reanálise, atendimento de determinação ou questionamento], referente a [objeto e instrumento], formulado por [parte, quando pertinente].

A variante `Em deliberação, ...` também aparece na amostra. Escolher uma abertura, sem repeti-la nos parágrafos seguintes.

Distinguir o processo de fundo da questão efetivamente submetida à sessão. Um processo de reequilíbrio pode chegar à Diretoria apenas para esclarecer um valor, ratificar determinado resultado ou retificar um item. Não reabrir todo o mérito pela forma de apresentar o objeto.

### 4.4. Contexto suficiente

Selecionar apenas os antecedentes que explicam a decisão atual: ato anterior, condição contratual, pedido, fato superveniente, divergência ou dependência entre intervenções.

Se existir relatório separado, não duplicar sua cronologia. Usar `Conforme adiantado no Relatório...` somente se o relatório tiver sido fornecido ou consultado e contiver efetivamente a informação retomada. Não criar referência a relatório inexistente.

### 4.5. Fundamentação e juízo do relator

Desenvolver as questões na ordem em que sustentam a decisão, e não na ordem em que os documentos foram juntados. Identificar a manifestação técnica pertinente, o fundamento decisivo, a avaliação do relator e o efeito correspondente.

### 4.6. Síntese decisória e dispositivo

Encerrar a fundamentação com a consequência que resulta do exame, sem acrescentar nova questão. Introduzir o dispositivo, normalmente em parágrafo numerado, com:

> Diante do exposto e dos demais elementos contidos nos autos, VOTO por:

Admitir as variantes breves presentes nos modelos, como `Diante do exposto, VOTO por:`. Não acumular expressões conclusivas para aumentar artificialmente a solenidade.

### 4.7. Fecho

A fórmula `É como voto.` aparece em VT01 a VT07, fora da sequência dos incisos; VT08 encerra sem essa fórmula. Utilizá-la como padrão da amostra predominante, ressalvado modelo diverso do gabinete.

Nome do relator e função, quando integrarem a área editável do modelo, aparecem centralizados. Preencher apenas com dados confirmados e não duplicar campos automáticos. Não reproduzir assinatura eletrônica, autenticação, QR code, código CRC, data de assinatura ou número SEI de outro documento.

## 5. Linguagem e ritmo

Escrever na voz do relator: `verifico`, `entendo`, `acolho`, `me alinho`, `manifesto minha concordância`, `concluo` e `VOTO`. Não usar `No entendimento desta setorial técnica`, `esta Gerência recomenda à SOG` ou `submeto à consideração superior` como voz do voto.

A linguagem é institucional e argumentativa, mas direta. Cada parágrafo deve cumprir função identificável: apresentar um fato relevante, explicar a controvérsia, avaliar uma manifestação ou extrair uma consequência. Não impor limite rígido de linhas ou frases; encurtar o que não acrescenta fundamento.

Conectivos observados e suas funções:

| Função | Repertório de referência |
|---|---|
| Delimitar o objeto ou a premissa | `Encontra-se para deliberação`, `De plano`, `No que se refere` |
| Identificar suporte | `Conforme informado`, `De acordo com`, `Compulsando os autos` |
| Explicar o raciocínio | `Com efeito`, `Ou seja`, `Por essa razão` |
| Introduzir contraste | `Contudo`, `No entanto`, `Em que pese` |
| Mudar o ponto de análise | `No tocante`, `Com relação`, `Ainda em relação` |
| Extrair consequência | `Desse modo`, `Nesse contexto`, `Sendo assim`, `Dito isso` |
| Encerrar a proposta | `Diante do exposto`, `É como voto` |

Escolher o conectivo pela relação lógica real. Não iniciar todos os parágrafos com a mesma expressão, nem inserir `Compulsando os autos` quando só se recebeu um resumo. `Pois bem.` e `Digo isto, pois` não são fórmulas obrigatórias desta amostra.

Evitar elogios genéricos à área técnica, adjetivação, juízos enfáticos sem demonstração e frases intercambiáveis entre processos. Quando houver concordância, explicar o motivo determinante em vez de apenas qualificar a análise como robusta, criteriosa ou acertada.

Preservar a força da afirmação original: alegação continua sendo alegação; possibilidade não vira certeza; inexistência de óbice em determinado âmbito não vira autorização geral. Não adotar como fórmula de redação inferências categóricas de um exemplo sem suporte no novo caso.

Não utilizar travessão como recurso redacional. O hífen separador de inciso, como em `I - aprovar`, é admitido.

## 6. Construção dos argumentos

Para cada questão relevante, organizar o raciocínio conforme sua necessidade:

**questão a decidir → elementos pertinentes → posição técnica identificada → fundamento determinante → juízo do relator → consequência.**

Essa sequência é um guia, não obrigação de produzir seis parágrafos. Em questão simples, dois parágrafos podem cumprir as funções; uma controvérsia exige desenvolvimento suficiente para explicar a escolha.

### 6.1. Concordância

Indicar qual conclusão se acolhe e por que ela resolve a questão. A remissão à fundamentação técnica pode evitar transcrição, mas deve ter objeto e alcance identificáveis.

Modelo de construção, a preencher somente com dados do caso:

> A [unidade], por meio da [manifestação e SEI], concluiu que [conclusão relevante]. Essa conclusão se apoia em [premissa determinante].
>
> Nesse ponto, acompanho o entendimento apresentado, uma vez que [razão decisória]. Desse modo, [efeito para o pedido].

No padrão de VT08, a incorporação por remissão convive com o destaque expresso das ressalvas e condições. Não declarar acolhimento integral e, em seguida, alterar conclusão material sem delimitar a diferença. Eventual fundamento legal da motivação por remissão deve ser verificado, e não copiado automaticamente do modelo.

### 6.2. Divergência ou posições distintas na instrução

Distinguir analista, Gerência, Superintendência e demais unidades. Não resumir posições opostas como `a área técnica concluiu`.

O exemplo central é VT05: identifica a divergência entre a NT e o despacho da SOG, expõe o ponto metodológico e adota uma posição. Em VT04, a escolha relativa à MMC segue a manifestação da SOG. Portanto, não presumir preferência fixa pela GPO, pela SOG ou pelo documento mais recente.

Estrutura adaptável:

> A [primeira manifestação] propõe [solução] com fundamento em [razão]. A [segunda manifestação], por sua vez, entende [posição diversa], em razão de [fundamento].
>
> Sobre esse ponto, [acolho/não acompanho] [posição precisamente delimitada], pois [fundamento disponível]. Assim, [efeito].

Não transformar a narrativa da divergência em desqualificação pessoal. Não encobrir divergência substantiva com fórmulas vagas de concordância parcial.

### 6.3. Cumprimento de determinação ou esclarecimento posterior

Identificar o comando anterior pelo ato, item e objeto. Explicar a providência adotada, o resultado relevante e o que ainda demanda decisão.

Distinguir `ratificar`, `retificar` e `alterar`. Não escolher o verbo apenas porque apareceu no voto de referência: explicitar qual aspecto permanece e qual se modifica, conforme o conteúdo efetivamente demonstrado.

Em questão financeira, explicar o mecanismo decisivo em linguagem compreensível, como faz VT03 ao tratar dos sinais do fluxo. Não importar aquele mecanismo para outros modelos financeiros.

### 6.4. Consulta

Delimitar os quesitos e as alternativas. Separar eventual admissibilidade do mérito quando necessário e sustentado. Responder a cada questão na ordem que permita correspondência direta com o dispositivo.

Não converter resposta sobre ausência de óbice no âmbito da ANTAQ em aprovação de providência sujeita a outro órgão. Identificar os limites e as competências considerados nos próprios documentos de suporte.

### 6.5. Condicionantes, providências futuras e fatos supervenientes

Explicar por que a condição é necessária, a qual decisão se vincula e quem deverá cumpri-la. Distinguir condição anterior à implementação de providência de acompanhamento posterior.

Atuação pessoal do relator, reunião, visita ou negociação somente pode ser narrada se houver informação confirmada. O relato de tratativas em VT01 não autoriza criar participação pessoal em novos casos.

Quando houver nova manifestação ou documento posterior à análise técnica, esclarecer o que ele acrescenta. Não atribuir à NT conclusão fundada em fato que ela não examinou.

## 7. Parte dispositiva

O dispositivo deve poder ser compreendido sem reconstruir toda a fundamentação. Formular um comando principal por inciso, agregando apenas qualificações indispensáveis ao mesmo objeto.

Utilizar algarismos romanos e verbos no infinitivo. Empregar alíneas `a)`, `b)`, `c)` quando houver respostas ou desdobramentos dentro do mesmo comando, como em VT06. Não usar listas Markdown como versão final para o SEI.

A ordem preferencial, ajustável ao caso, é: **decisão principal; parâmetros e condições; providências de execução ou acompanhamento; encaminhamentos e ciência**. Admissibilidade antecede o mérito quando houver necessidade. Não criar incisos apenas para preencher essa ordem.

| Verbo ou operação | Precisão exigida na redação |
|---|---|
| conhecer | Identificar o pedido, consulta ou recurso e o suporte para o exame de admissibilidade, se aplicável |
| aprovar, autorizar, deferir ou indeferir | Delimitar objeto, interessado, instrumento e alcance da decisão, sem confundir as operações |
| declarar ou reconhecer | Descrever exatamente a situação que os fundamentos permitem afirmar |
| considerar ou fixar parâmetro | Identificar valor ou parâmetro, finalidade, unidade e referências temporais necessárias |
| ratificar | Identificar o ato e a parcela mantida |
| retificar ou alterar | Identificar ato, item alcançado, conteúdo anterior pertinente e conteúdo que passa a valer; usar redação substitutiva quando necessária à clareza |
| sobrestar | Identificar a instrução atingida, a duração e a condição de retomada que tenham suporte no caso |
| determinar | Identificar responsável, providência, objeto, prazo e marco inicial, quando cabíveis e definidos |
| recomendar | Identificar destinatário e providência, preservando a distinção entre recomendação e determinação |
| encaminhar | Identificar destinatário e finalidade; não usar remessa como substituto de decisão de mérito |
| cientificar | Identificar quem receberá ciência e de quê |

Não transformar essa tabela em sequência obrigatória. Não reproduzir o número de incisos de um modelo nem inserir sempre comandos de concorrência, adimplência, regularidade contratual, sigilo ou encaminhamento ao Ministério.

**Competência deve aparecer no verbo e no destinatário.** VT01 distingue o sobrestamento da instrução, a recomendação ao MPOR sobre prazos contratuais e as determinações de acompanhamento às unidades internas. Aproveitar essa distinção de construção, não seus prazos ou seu resultado.

Condições, ressalvas e limites que alterem o alcance da decisão devem constar do comando pertinente ou de remissão precisa que os torne identificáveis. Evitar `observadas as ressalvas acima` quando houver vários pontos diferentes ou dúvidas sobre o que condiciona a decisão.

Não introduzir no dispositivo obrigação, sanção, prazo, fundamento ou restrição que não tenha sido tratado e sustentado. Inversamente, não omitir do dispositivo a providência decisiva afirmada na fundamentação.

Pontuação: incisos separados por ponto e vírgula; conjunção antes do último, quando adequada; ponto final no encerramento. Conferir a sequência após qualquer exclusão de inciso. Não reproduzir falhas de pontuação dos documentos de referência.

## 8. Dados, referências e intensidade das conclusões

Preservar denominações, números SEI, contratos, itens de acórdãos, unidades, valores e datas conforme a documentação pertinente. Havendo versões diferentes, identificar a adotada e não combinar trechos incompatíveis.

Em VPL, investimento e demais valores: distinguir montante, sinal, data-base, data focal, atualização e finalidade. Conferir consistência entre fundamentos e dispositivo. Os valores de VT04 e VT07 pertencem a momentos distintos da mesma discussão e não podem ser fundidos em um resultado único.

Usar valores por extenso nos pontos decisivos, conforme a prática predominante dos modelos, conferindo sua correspondência com os algarismos. Não repetir a expressão completa em cada menção sem necessidade. Não confundir m², m³, toneladas, capacidade e movimentação, nem substituir MMC por MME sem apoio na fonte.

Os comandos de restrição de acesso presentes em alguns votos são específicos daqueles casos. Não inserir `manter o sigilo` nem reproduzir sua base legal por rotina. Tratar abrangência, fundamento e necessidade somente quando sustentados pelos elementos do novo processo.

A redação não substitui a conferência técnica: se a documentação contiver contradição de valor, área ou premissa capaz de afetar a proposta, sinalizar o problema e não solucioná-lo apenas pela escolha da frase mais conveniente.

Citações no documento: usar `Nota Técnica nº [número]/[ano]/[unidade] (SEI nº [identificador])`, com referência suficiente para localização. Não incluir marcadores internos de ferramentas ou citações da interface de chat no HTML do voto.

## 9. Transcrições, tabelas e imagens

Transcrever apenas a passagem cujo teor literal seja necessário: determinação a cumprir, cláusula controvertida, redação proposta ou ajuste de minuta. Nos demais casos, sintetizar e atribuir a fonte.

Conferir a transcrição com o documento disponível, preservar omissões identificadas por `[...]` e separar citação de comentário do relator. Não corrigir silenciosamente o conteúdo de uma citação. Campos em aberto de uma minuta citada devem ser identificáveis como parte da citação, não como campos esquecidos do voto.

Citações longas têm recuo e fonte menor nos modelos. Não transportá-las como parágrafos numerados autônomos do voto nem repetir no dispositivo toda a transcrição quando uma referência precisa resolver.

Tabelas não são elemento obrigatório da amostra. Utilizá-las somente quando melhorarem a compreensão de comparação essencial e os dados estiverem disponíveis.

Imagem ou planta é facultativa. VT05 usa figura para situar a área, com referência à NT de origem. Quando necessária, extrair ou recortar a figura efetivamente fornecida, preservar sua proporção e elementos relevantes e inserir legenda/fonte. Não desenhar planta substitutiva, inventar delimitação nem tratar inspeção visual como validação de área. Não usar imagens decorativas.

## 10. Formatação SEI e HTML

### 10.1. Modelo nativo tem prioridade

Se houver HTML original do **Voto do Relator** ou modelo exportado do editor do SEI, preservar sua organização, classes, estilos de parágrafo, recuos, mecanismos de numeração e campos automáticos. Substituir conteúdo, não reconstruir o documento por aproximação.

Identificar previamente quais partes são editáveis e quais são geradas pelo sistema. Preservar as diferenças entre: cabeçalho; parágrafo numerado; citação; inciso; alínea; fecho; identificação do signatário.

Não presumir nomes de classes CSS a partir de um PDF. Não transplantar sem validação o HTML de Nota Técnica ou de Despacho para Voto do Relator. Não somar números digitados à numeração automática. A sequência decimal do corpo e a sequência romana do dispositivo são diferentes e devem permanecer independentes.

### 10.2. O que a amostra em PDF permite reproduzir

O padrão visual observado compreende:

- campos iniciais alinhados à esquerda, com rótulos em negrito;
- texto principal em Calibri, aproximadamente 12 pt na exportação examinada, justificado;
- parágrafos numerados sequencialmente em algarismos arábicos, com recuo de primeira linha;
- dispositivo recuado, com incisos romanos e alíneas quando necessárias;
- citações extensas em corpo menor, com recuo próprio, frequentemente em itálico;
- fecho separado e identificação do relator centralizada.

Essas observações não comprovam os nomes das classes, as medidas originais do editor ou o funcionamento de sua numeração. Não prometer fidelidade nativa com base somente nos PDFs.

### 10.3. Ausência de HTML nativo

É possível entregar HTML de referência, mas identificá-lo como **base portátil de redação, pendente de validação no editor do SEI**. Empregar estrutura simples, codificação UTF-8, estilos locais e um único mecanismo de numeração por nível. O arquivo `MODELO_VOTO_RELATOR_REFERENCIA.html` que acompanha esta skill é apenas essa alternativa.

Não alegar que a cópia e colagem manterá automaticamente a numeração nativa. Na adaptação posterior, substituir a numeração portátil pelos estilos reais e testar a sequência no editor. Não fazer as duas formas coexistirem.

Não reproduzir cabeçalho de impressão do navegador, URL do controlador, horário de exportação, número de página, assinatura eletrônica, autenticação ou rodapé automático. Não introduzir scripts, recursos externos ou dependências para apresentar o voto.

A ausência de HTML nativo não impede a elaboração do texto e da skill; impede apenas certificar a reprodução exata do mecanismo de formatação do SEI.

## 11. Esqueleto textual de composição

O esquema abaixo é **modelo de trabalho**, não texto pronto para assinatura. Os rótulos explicativos devem desaparecer da versão final. Os parágrafos efetivos serão numerados pelo mecanismo escolhido, sem números literais duplicados.

```text
Processo: [PROCESSO]
Tipo: [TIPO PROCESSUAL]
Interessado: [INTERESSADO]
Contextualização: [QUESTÃO CONCRETA]
Relator: [RELATOR CONFIRMADO]

[CERTIFICAÇÃO INSTITUCIONAL, SOMENTE APÓS VALIDAÇÃO]

Encontra-se para deliberação [questão específica], referente a [objeto].

[Antecedente necessário: ato, pedido, condição contratual ou fato que explica a controvérsia.]

Conforme [manifestação identificada], [conclusão e premissa relevante].

[Se houver divergência, expor as posições e seus fundamentos sem atribuir consenso inexistente.]

Nesse ponto, [juízo do relator], uma vez que [fundamento decisivo disponível].

Desse modo, [consequência para o pedido, com condições e limites pertinentes].

Diante do exposto e dos demais elementos contidos nos autos, VOTO por:

I - [comando principal, com objeto e alcance definidos];
II - [parâmetro, condição ou providência adicional, somente se necessário]; e
III - [encaminhamento ou ciência, somente quando pertinente].

É como voto.

[NOME CONFIRMADO, SE O CAMPO FOR EDITÁVEL]
[FUNÇÃO CONFIRMADA, SE O CAMPO FOR EDITÁVEL]
```

Eliminar módulos inaplicáveis, acrescentar desenvolvimento apenas onde necessário e renumerar. Não conservar três incisos apenas porque o esquema tem três. Não acrescentar títulos `RELATÓRIO`, `FUNDAMENTAÇÃO` e `CONCLUSÃO` por hábito: os votos examinados usam texto corrido numerado, sem essa divisão. Modelo específico do gabinete ou solicitação expressa pode determinar organização diferente.

## 12. Controle final de redação

Antes da entrega, conferir silenciosamente:

1. O texto está na voz do relator, sem linguagem de despacho gerencial ou de decisão colegiada já proferida?
2. A questão atual está delimitada, sem reabertura desnecessária do processo de fundo?
3. As manifestações foram atribuídas às unidades corretas, inclusive quando divergem?
4. A motivação explica a passagem dos elementos disponíveis para a conclusão?
5. Cada comando tem fundamento e cada conclusão com efeito decisório está refletida no dispositivo?
6. Valores, sinais, áreas, datas-base, datas focais, prazos e identificadores coincidem entre os blocos?
7. Competência, destinatários, condições e limites estão expressos sem ampliar os documentos de suporte?
8. A certificação processual tem suporte; não há reunião, relatório, parecer ou atuação pessoal inventados?
9. O formato distingue parágrafos, incisos e alíneas e não duplica numeração ou campos automáticos?
10. A versão final está sem campos pendentes, instruções internas, metadados de outro processo ou assinatura simulada?

Entregar o voto e, separadamente, apenas as pendências relevantes. Não anexar relatório de auditoria, matriz ou explicação metodológica ao corpo do voto por padrão. Quando a solicitação for somente um modelo, preservar os campos de preenchimento e identificar essa condição.

## 13. Materiais adicionais úteis para aperfeiçoar esta skill

**Para a estrutura e a linguagem, os oito votos já são suficientes.** Os complementos abaixo têm finalidades distintas e não são pré-requisitos cumulativos:

- **Um Voto do Relator em HTML nativo do SEI:** permite reproduzir classes, campos editáveis, recuos e numeração sem aproximação. É o complemento prioritário para a formatação.
- **Um conjunto Relatório + NT + despachos GPO/SOG + Voto + Acórdão:** permite observar o que o gabinete sintetiza, incorpora, afasta e converte em comando. Um caso representativo é suficiente para começar.
- **Processo do TEMAPE, indicado no cabeçalho de VT05 como 50300.013489/2024-59:** a NT nº 165/2024/GPO/SOG (SEI 2355772) e o Despacho SOG (SEI 2564886) ajudam a estudar a passagem de posições divergentes para a escolha do relator.
- **Processo da Coamo, indicado nos cabeçalhos de VT04 e VT07 como 50300.001303/2022-57:** as manifestações e planilhas que antecedem a decisão e a retificação permitem separar resultado original, atualização, esclarecimento e comando substitutivo.
- **Processo da Marimex, indicado no cabeçalho de VT01 como 50300.019064/2022-91:** as manifestações finais, o relatório e o Termo de Compromisso nº 001/2025 (SEI 2592361) ajudam a identificar a incorporação de fatos supervenientes e a repartição dos comandos.

O conjunto PAR05 também pode complementar a calibração da motivação por remissão e das condicionantes: NT nº 40/2026/GPO/SOG (SEI 2852804), Despacho SOG (SEI 2863035), NT nº 11/2026/SELC/DG (SEI 2864360) e Despacho SELC (SEI 2868447), relacionados em VT08.

Os processos acima são os **indicados nos cabeçalhos dos votos**. Não presumir que coincidam com os processos de deliberação constantes dos rodapés. Confirmar a vinculação antes de solicitar ou consultar autos específicos.

**Resultado esperado:** voto com a estrutura documental dos modelos, raciocínio próprio do relator, seleção dos elementos determinantes e dispositivo preciso, sem confundir reprodução de estilo com validação automática do mérito.

## 14. Uso deste pacote por link único

Este arquivo reúne a skill completa, o complemento de síntese processual abaixo e o modelo HTML integral no Anexo A. Não é necessário abrir outro link para obter as instruções e a base HTML. Os dois arquivos originais são preservados separadamente para edição.

**Comando de uso:** Leia integralmente este pacote e elabore o Voto do Relator com base nos documentos do caso. Aplique a estrutura, a linguagem, o ritmo argumentativo e as regras do dispositivo. Entregue em HTML. Não invente fatos, referências, certificações ou comandos. Informe as pendências relevantes fora do documento.

O pacote não cria, assina, publica ou tramita documentos no SEI. Os PDFs de referência e os processos administrativos não integram a publicação. A elaboração de um voto concreto continua dependendo dos documentos do respectivo caso.

O HTML é uma base portátil, não uma exportação nativa do Voto do Relator. Não sobrepor sua numeração à numeração automática do SEI. A presença de HTML de notas técnicas, despachos ou acórdãos em um processo não equivale ao fornecimento do HTML nativo de um voto.

## 15. Complemento: da instrução à razão de decidir

Estas regras complementam a versão-base após a leitura das peças centrais do processo de origem do exemplo TEMAPE. Não representam auditoria integral do processo, validação dos cálculos ou adesão às teses jurídicas e econômicas daquele caso. Não publicar os documentos de origem junto com o pacote.

1. **Relatório e voto desempenham funções diferentes.** O relatório identifica o pedido e apresenta a evolução das manifestações. O voto seleciona o que importa para decidir e explicita a posição do relator. Relatar uma conclusão não equivale a acolhê-la.
2. **Não usar a manifestação mais recente como posição única da instrução.** Identificar as alternativas sustentadas pelas unidades, o ponto exato de divergência e a razão da escolha. Documento complementar pode conter fundamento decisivo ausente da primeira NT.
3. **Atribuir cada fundamento à sua fonte efetiva.** Quando um voto de referência citar uma NT, mas o trecho literal estiver em documento complementar, conferir e ajustar a atribuição no caso novo. Não perpetuar inexatidão de referência porque aparece no exemplo.
4. **Manter coerência entre premissa escolhida, resultado e comando.** Não adotar a fundamentação de uma linha de análise e o valor ou resultado de outra sem justificativa expressa. A tarefa de redação não autoriza resolver essa incompatibilidade por conta própria.
5. **Preservar o alcance do pedido e da decisão.** Distinguir resposta a consulta, dispensa de análise, aprovação de estudo, aprovação de reequilíbrio e autorização contratual. Não converter uma dessas providências em outra por mera adaptação do verbo. Havendo mudança de objeto ao longo do processo, identificar seu suporte.
6. **Não confundir original e reprodução juntada.** Registrar separadamente o identificador do documento original e o da cópia incorporada aos autos. Citar aquele que permita localizar com segurança o conteúdo utilizado e esclarecer a relação quando necessário.
7. **Separar proposta e deliberação.** Em estudo de caso concluído, comparar voto e acórdão para identificar o que foi efetivamente decidido. Em processo novo, o voto propõe; não escrever como se o Colegiado já tivesse deliberado.
8. **Não reproduzir falhas da amostra.** Divergências de área, unidade, extenso, referência ou objeto devem ser apontadas, e não corrigidas silenciosamente nem tratadas como padrão de estilo. A síntese textual não dispensa a identificação da pendência material.

## Anexo A. Modelo HTML incorporado

Conteúdo integral de `MODELO_VOTO_RELATOR_REFERENCIA.html`. Resolver ou remover os campos entre colchetes antes da entrega de uma versão final. O quadro de orientação está fora do corpo do voto.

```html
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Modelo textual de Voto do Relator</title>
<style>
  /* Base portátil, não exportação nativa do SEI. Não usar estas classes
     como se fossem nomes de estilos internos do editor institucional. */
  html { background: #f1f1f1; }
  body { margin: 0; color: #111; font-family: Calibri, Arial, sans-serif; font-size: 12pt; }
  .orientacao { max-width: 18cm; margin: 1cm auto .5cm; padding: .5cm; background: #fff; border: 1px solid #aaa; font-size: 10pt; line-height: 1.35; }
  .orientacao p { margin: 0 0 .25cm; }
  .orientacao p:last-child { margin-bottom: 0; }
  .documento { box-sizing: border-box; width: 21cm; min-height: 27cm; margin: 0 auto 1cm; padding: 1.8cm 1.7cm; background: #fff; }
  .identificacao { margin-bottom: 1cm; }
  .identificacao p { margin: 0 0 .22cm; line-height: 1.25; text-align: left; }
  .paragrafos { margin: 0; padding-left: .65cm; list-style-type: decimal; }
  .paragrafos > li { margin: 0 0 .3cm; padding-left: .1cm; text-align: justify; line-height: 1.25; }
  .paragrafos > li > p { margin: 0; text-indent: 1.7cm; }
  .incisos { margin: .35cm 0 0 1.2cm; padding-left: .9cm; list-style-type: upper-roman; }
  .incisos > li { margin: 0 0 .25cm; text-align: justify; padding-left: .15cm; }
  .incisos > li::marker { content: counter(list-item, upper-roman) " - "; }
  .alineas { margin: .25cm 0; padding-left: .7cm; list-style-type: lower-alpha; }
  .alineas > li::marker { content: counter(list-item, lower-alpha) ") "; }
  .fecho { margin: .7cm 0 .8cm 1.7cm; }
  .signatario { text-align: center; margin: 0; }
  .funcao { text-align: center; margin: .25cm 0 0; }
  .campo { color: #111; }
  @media (max-width: 850px) { .documento { width: calc(100% - 1cm); padding: 1cm; } .orientacao { margin: .5cm; } }
  @media print { html { background: #fff; } .orientacao { display: none; } .documento { margin: 0; width: auto; padding: 0; min-height: auto; } @page { size: A4; margin: 2cm; } }
</style>
</head>
<body>
<aside class="orientacao" aria-label="Instruções de uso, fora do voto">
  <p><strong>Modelo de trabalho. Não é um voto pronto para assinatura.</strong></p>
  <p>Esta é uma base HTML portátil de redação. Os PDFs permitem reproduzir a estrutura visual, mas não identificar as classes ou a numeração nativa do SEI. Antes do uso no sistema, adaptar a um HTML original de Voto do Relator e conferir a numeração no editor.</p>
  <p>Preencher os campos com fontes do caso, excluir parágrafos e incisos inaplicáveis e desenvolver somente os fundamentos necessários. A lista decimal e a lista romana usam numeração própria desta página; não as sobrepor à numeração automática do SEI.</p>
  <p>Este quadro não integra o documento. Não foram reproduzidos logotipo, assinatura eletrônica, autenticação, rodapé ou identificadores de votos anteriores.</p>
</aside>
<main class="documento" id="corpo-voto">
  <header class="identificacao">
    <p><strong>Processo:</strong> <span class="campo">[PROCESSO DE MÉRITO CONFIRMADO]</span></p>
    <p><strong>Tipo:</strong> <span class="campo">[TIPO PROCESSUAL CONFIRMADO]</span></p>
    <p><strong>Interessado:</strong> <span class="campo">[DENOMINAÇÃO CONFIRMADA]</span></p>
    <p><strong>Contextualização:</strong> <span class="campo">[QUESTÃO CONCRETA SUBMETIDA À DELIBERAÇÃO]</span></p>
    <p><strong>Relator:</strong> <span class="campo">[NOME CONFIRMADO]</span></p>
  </header>
  <ol class="paragrafos">
    <li><p>[INSERIR A CERTIFICAÇÃO INSTITUCIONAL SOMENTE APÓS VERIFICAÇÃO DA SITUAÇÃO PROCESSUAL, DA REFERÊNCIA NORMATIVA E VALIDAÇÃO PELO GABINETE.]</p></li>
    <li><p>Encontra-se para deliberação [PEDIDO, CONSULTA, REANÁLISE OU QUESTÃO ESPECÍFICA], referente a [OBJETO E INSTRUMENTO], [FORMULADO POR OU DECORRENTE DE ATO CONFIRMADO, QUANDO PERTINENTE].</p></li>
    <li><p>[APRESENTAR SOMENTE O ANTECEDENTE NECESSÁRIO PARA COMPREENDER A DECISÃO ATUAL, SEM REPETIR O RELATÓRIO.]</p></li>
    <li><p>Conforme [MANIFESTAÇÃO IDENTIFICADA E SEI], [CONCLUSÃO RELEVANTE E SUA PREMISSA].</p></li>
    <li><p>[SE HOUVER POSIÇÕES DISTINTAS, IDENTIFICAR CADA UNIDADE E O FUNDAMENTO DA DIVERGÊNCIA. EXCLUIR ESTE PARÁGRAFO SE INAPLICÁVEL.]</p></li>
    <li><p>Nesse ponto, [JUÍZO DO RELATOR SOBRE A QUESTÃO], uma vez que [FUNDAMENTO DECISIVO DISPONÍVEL NOS DOCUMENTOS].</p></li>
    <li><p>Desse modo, [CONSEQUÊNCIA PARA O PEDIDO, COM AS CONDIÇÕES E OS LIMITES PERTINENTES].</p></li>
    <li>
      <p>Diante do exposto e dos demais elementos contidos nos autos, <strong>VOTO</strong> por:</p>
      <ol class="incisos" type="I">
        <li>[VERBO NO INFINITIVO, OBJETO E ALCANCE DO COMANDO PRINCIPAL];</li>
        <li>[PARÂMETRO, CONDIÇÃO OU PROVIDÊNCIA ADICIONAL FUNDAMENTADA, SOMENTE SE NECESSÁRIA]; e</li>
        <li>[ENCAMINHAMENTO OU CIÊNCIA COM DESTINATÁRIO E FINALIDADE, SOMENTE SE PERTINENTE].</li>
      </ol>
    </li>
  </ol>
  <p class="fecho">É como voto.</p>
  <p class="signatario">[NOME CONFIRMADO, APENAS SE O CAMPO FOR EDITÁVEL]</p>
  <p class="funcao">[FUNÇÃO CONFIRMADA, APENAS SE O CAMPO FOR EDITÁVEL]</p>
</main>
</body>
</html>
```
