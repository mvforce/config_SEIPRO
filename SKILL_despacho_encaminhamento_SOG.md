---
name: despacho-encaminhamento-sog
description: Examina a conclusão de Nota Técnica da GPO, consulta o processo e redige despacho da Gerência à SOG, com confirmação item a item, anuência ou divergência fundamentada e proposta de encaminhamento.
---

# Despacho da GPO à SOG após Nota Técnica

## Finalidade e limites
Use esta skill quando houver Nota Técnica ou manifestação conclusiva de servidor da GPO a ser apreciada pela chefia imediata e encaminhada à Superintendência de Outorgas. A Nota Técnica é a manifestação técnica do analista; o despacho é a posição própria da Gerência. Não presumir concordância do gerente, nem transformar o despacho de encaminhamento em voto da Diretoria. Aplicar o contexto fixo de Tavares já enviado à API para estilo e método, sem repetir o perfil pessoal no documento.

## Regra de execução: mostrar botões antes de avançar
Esta skill deve ser carregada com `skill_ler` quando o usuário pedir despacho da GPO à SOG. **A primeira interação após localizar a NT é uma chamada de ferramenta `perguntar` com `opcoes`, antes de qualquer resposta final ou minuta.** Escrever “Deseja encaminhar?” na mensagem não cria botão. Exemplo executável:

```json
{"pergunta":"Encaminhar a Nota Técnica nº [N]/[ANO]/GPO/SOG (SEI nº [ID]) à SOG?","opcoes":["Sim, esta NT","Ver resumo","Escolher outra NT"]}
```

Depois de cada justificativa técnica, chamar novamente `perguntar` com opções de posição; depois da minuta integral, chamar `perguntar` para confirmar o texto. Nunca encerrar um turno com a pergunta escrita em prosa quando se espera uma escolha. Se `perguntar` não estiver disponível, informar explicitamente que o aplicativo não disponibilizou cartões interativos nesta conversa; não afirmar que apresentou botões. O cartão de escolha da próxima etapa não substitui a aprovação nativa da gravação do documento.

## Interface de escolhas do SEI-Pro
Sempre que uma resposta do usuário determinar qual NT usar, como avaliar uma conclusão ou qual versão da minuta manter, **chamar a ferramenta nativa `perguntar` com `pergunta` e `opcoes`**, para exibir um cartão com botões. Não apresentar as opções apenas como texto corrido ou lista Markdown. O SEI-Pro aceita até seis rótulos em `opcoes` e já mostra o campo `Outra resposta...`; deixar rótulos curtos, claros e orientados à ação. O cabeçalho do cartão traz contexto suficiente, como número da NT e item da conclusão. Não criar HTML de botões na mensagem: o aplicativo renderiza os botões a partir da chamada à ferramenta.

Exemplo de chamada para escolher a NT (adapte aos dados efetivamente lidos):

```json
{"pergunta":"Nota Técnica nº 132/2026/GPO/SOG (SEI nº 2996813) · Análise da área SSZ34. Qual documento deseja encaminhar à SOG?","opcoes":["Encaminhar esta NT","Escolher outra NT","Ver resumo antes"]}
```

Exemplo para cada conclusão, **após mostrar a evidência e a justificativa sugerida no texto da conversa**:

```json
{"pergunta":"NT nº [número] · Item [identificador]. Como a Gerência deve se posicionar?","opcoes":["Acompanhar proposta","Divergir parcialmente","Divergir integralmente","Pedir diligência","Ver fundamento"]}
```

Ao escolher `Ver resumo antes` ou `Ver fundamento`, apresentar os dados solicitados e abrir **novo cartão** com opções de decisão. Quando houver divergência, o campo livre ou um novo cartão com `Informar minha tese` deve permitir ao usuário indicar raciocínio e novas peças; não escolher uma tese por ele. Quando a resposta escrita for indispensável, pedir em uma única instrução: linha de raciocínio, tese desejada e documentos novos. Nunca interpretar um clique em `Ver fundamento` como anuência.

O cartão `perguntar` resolve **escolhas de conteúdo e de fluxo**. Não o usar como substituto da aprovação da escrita: `documento_criar`/ferramenta equivalente abre seu próprio cartão de autorização no aplicativo. Após a confirmação do texto, abrir cartão de **escolha de próxima etapa** com `perguntar` e botões `Criar despacho no SEI`, `Manter apenas a minuta` e `Solicitar ajustes`. Essa escolha não aprova a escrita; a autorização efetiva ocorre no cartão da função de criação. Não invocar ferramenta de escrita se o usuário escolher apenas a minuta.

## Primeiro: identificar e confirmar a Nota Técnica
1. No processo aberto no SEI-Pro, listar as Notas Técnicas elaboradas pela GPO/SOG, com número, identificador SEI, data, assunto e situação disponível. Identificar a **última NT da GPO no processo**, preferencialmente pelo ato mais recente exibido na árvore e sua data, conferindo se trata da matéria em curso. Não selecionar automaticamente uma NT da Infra S.A., do Ministério, de outra unidade ou uma NT antiga da GPO só por ter número semelhante. Se houver minuta e versão final, destacar ambas e propor a versão final, se efetivamente existente.
2. **Antes de analisar as conclusões ou redigir o despacho**, exibir o cartão `perguntar` com o número, SEI, data e assunto da NT encontrada e os botões `Encaminhar esta NT`, `Escolher outra NT` e `Ver resumo antes`. Aguardar escolha explícita. Caso o usuário diga não, mostrar as demais NTs GPO encontradas ou pedir o número SEI correto e só então prosseguir. Se não houver NT GPO no processo, informar isso e perguntar qual peça deseja encaminhar. Não tomar silêncio como confirmação.
3. Confirmada a NT, ler seu inteiro teor, anexos e referências, eventuais retificações e manifestações posteriores. Extrair todas as conclusões, inclusive incisos, ressalvas, condicionantes e proposta de encaminhamento. Conferir se há ato posterior que a substitua ou altere. Caso haja, avisar o usuário e confirmar qual versão deve ser apreciada antes de continuar.
4. Consultar os documentos que a própria NT cita para sustentar cada conclusão, com identificador SEI e localização. Reconstruir apenas o contexto processual necessário à redação do despacho: objeto, provocação original, peças principais, tramitação e comando eventualmente dirigido à GPO. **Não presumir a origem da provocação, tema ou posição fixa na árvore**; esses elementos só entram quando forem pertinentes ao caso concreto. Se houver peça ilegível, declarar o limite e buscar leitura alternativa antes de concluir.

## Estrutura, ritmo e ordem lógica do despacho
Tomar como referência de **forma e ritmo**, quando pertinente, o Despacho GPO SEI nº 3005027, que aprecia a NT nº 132/2026/GPO/SOG (SEI nº 2996813), no Processo nº 50300.015718/2026-31. O exemplo está ligado ao caso SSZ34; não reproduzir automaticamente sua tese, os itens TV1/TV2 nem a conclusão sobre PDZ em outros processos. O despacho contém uma posição da chefia, e não uma reedição integral da Nota Técnica.

A sequência efetivamente observada é:

1. **Abertura curta:** destinatário `À Superintendência de Outorgas`, assunto preciso, referência ao ato de encaminhamento **se existente e relevante**, retorno dos autos, identificação da NT e posição global já anunciada: aprovação integral ou parcial, ou divergência. No exemplo: primeiro retorna os autos; em seguida diz que aprova parcialmente o teor da NT e que indicará divergências.
2. **Transição e questão preliminar:** `Pois bem.` e `De início, cumpre delimitar...` introduzem a premissa que controla a análise. Quando houver precedente da Diretoria ou controvérsia de competência, expor a decisão vigente, sua força vinculante para as unidades e a possibilidade de propor revisão ao próprio Colegiado. Separar a **regra aplicada no processo atual** da **proposta de revisão para o futuro**; não anunciar como revogado entendimento ainda vigente. Se não houver questão preliminar relevante, passar diretamente à análise, sem fabricar discussão institucional.
3. **Construção argumentativa:** enunciar a regra e o fato, depois a avaliação e consequência em parágrafos curtos, com conectivos como `Digo isto, pois,`, `Veja.`, `Desse modo,` e `No entendimento desta Gerência,` apenas quando naturais. No SEI nº 3005027, a tese de controle regulatório de elementos essenciais aparece após a explicação do entendimento colegiado, sem propor segunda aprovação do EVTEA. Não usar passagem retórica extensa se a matéria for simples.
4. **Achados agrupados pela consequência**, sempre com referência aos itens da NT: primeiro pontos aproveitáveis ou sanáveis sem impedir avanço; depois pontos de que a Gerência diverge, com fundamento e efeito preciso; por fim, ponto decisivo que muda o encaminhamento, analisado em parágrafos próprios. Essa organização não exige um parágrafo repetitivo para cada item quando vários comportarem a mesma consequência. A matriz de conferência continua item a item nos bastidores e com o usuário.
5. **Fecho direto:** afirmar a consequência processual concreta e encaminhar à SOG. No exemplo, o PDZ é tratado após os demais itens, recebe fundamento próprio e leva à recomendação de interromper a instrução até a compatibilização do estudo. Usar a forma de incisos `reconhecer/declarar/aprovar/responder` apenas se houver proposta colegiada com tais comandos. Não acrescentar proposição à Diretoria em todo despacho.

No caso do exemplo, a NT nº 132 concluiu pela pendência de TV1.I, IV, V, VI e XIV, TV2.II e TV2.III e recomendou saneamento antes da consulta e audiência. O despacho da Gerência não repete essa conclusão em bloco: (a) mantém TV2.II e TV2.III e trata TV1.VI e IV como melhorias sem óbice; (b) afasta TV1.I e V por entender que extrapolam o escopo então definido pela Resolução nº 5.945-ANTAQ; e (c) considera TV1.XIV, compatibilidade com o PDZ, impeditivo ao prosseguimento. Essa relação entre NT e despacho demonstra **como agrupar, hierarquizar e justificar** pontos, não qual resultado adotar em novo processo.

### Como construir a introdução e a contextualização
Depois de confirmar a NT, obter da árvore o objeto, o pedido original, o despacho que remeteu à GPO se houver, a versão dos estudos e as decisões relevantes. Selecionar apenas os antecedentes necessários para compreender a posição da Gerência. Abrir com `Faço referência ao [ato] (SEI nº [...]), para retornar os autos` quando houver encaminhamento identificado. Em seguida: `A matéria foi analisada no âmbito da Nota Técnica nº [número]/[ano]/GPO/SOG (SEI nº [...]), cujo teor [acompanho na íntegra / aprovo parcialmente, pelas razões a seguir / não acompanho, pelas razões a seguir].` Não atribuir à Gerência trabalho feito apenas pelo servidor. Evitar inventário longo se o leitor puder encontrá-lo na NT.

## Conferência item a item com o usuário
Antes de redigir a versão final, extrair **todas as conclusões autônomas da NT**, incluindo subitens capazes de mudar a decisão, sem fundir pontos de natureza distinta. Exibir um quadro de trabalho com as colunas `item da NT | conclusão da área técnica | suporte (SEI/localização) | justificativa sugerida pela Gerência | consequência proposta | posição do usuário`. Redigir uma justificativa **original e específica para cada item** a partir dos autos: fato verificado, norma/decisão aplicável, avaliação crítica e consequência. Quando a área técnica não tiver fundamento suficiente, apontar a lacuna, sem completar o raciocínio com suposições.

Para cada item, apresentar primeiro o contexto e a justificativa, depois abrir o cartão nativo `perguntar` com botões de posição. Esperar resposta e manter a numeração da NT:

> **Item [n] da Nota Técnica:** [transcrição curta ou paráfrase fiel da conclusão]. **Fundamento encontrado:** [SEI, página/seção e norma ou decisão aplicável]. **Proposta da Gerência:** [acompanhar / divergir parcialmente / divergir integralmente / pedir complementação]. **Justificativa proposta:** [duas a quatro frases com fato, fundamento e consequência]. Em seguida, use `perguntar` com `opcoes` como `Acompanhar proposta`, `Divergir parcialmente`, `Divergir integralmente`, `Pedir diligência` e `Ver fundamento`.

Se o usuário escolher **Acompanhar proposta**, incorporar a justificativa confirmada ao despacho. Se escolher uma divergência ou responder pelo campo livre que deseja ajuste, pedir objetivamente que informe **(i)** a linha de raciocínio, **(ii)** a tese ou conclusão pretendida e **(iii)** os novos elementos ou peças a considerar. Usar as informações fornecidas para verificar novamente os autos, elaborar nova justificativa e submetê-la à confirmação. Não aceitar a divergência como fundamento em si; fundamentar a posição em evidência verificável. Prosseguir para o item seguinte apenas depois de registrar uma posição expressa para o item atual. Se forem muitos itens, mostrar o quadro completo e perguntar por grupos numerados, mas registrar resposta para **cada item** e retomar os que ficaram sem posição. Não interpretar silêncio como concordância.

Ao final, mostrar a matriz consolidada de decisões: item, posição da área técnica, posição confirmada da Gerência, motivo e efeito sobre o encaminhamento. Abrir cartão `perguntar` para confirmar a síntese antes de apresentar o despacho integral, com opções `Confirmar síntese`, `Rever item` e `Ver evidências`. Esse passo não substitui a confirmação da versão final do documento.

## Regra para anuência e divergência
- **Todos os itens acompanhados sem ressalva:** usar exatamente o fecho solicitado, ajustando apenas a identificação já criada pelo SEI: **"A matéria foi analisada no âmbito da Nota Técnica nº [XXX]/[ANO]/GPO/SOG (SEI nº [XXX]), cujo teor acompanho na íntegra."** Não acrescentar "acompanho na íntegra" se existir qualquer ressalva substantiva da Gerência.
- **Divergência parcial:** declarar "Divirjo parcialmente da Nota Técnica nº [XXX] quanto ao item [n]" e expor, separadamente, quais itens acompanha, qual conclusão modifica, por quê e qual encaminhamento resulta. Se a divergência atingir parte de um item, delimitar a parcela e preservar expressamente o restante.
- **Divergência integral:** declarar "Divirjo integralmente da conclusão da Nota Técnica nº [XXX]" somente quando rejeitar o conjunto de suas conclusões decisórias, apontando fundamentos para cada ponto determinante e proposta substitutiva. A mera discordância quanto ao resultado final pode exigir explicação dos itens que permanecem aceitos.
- **Insuficiência de instrução:** quando não houver base para anuência ou divergência conclusiva, propor diligência objetiva, indicando documento, pergunta e finalidade. Não classificar automaticamente essa situação como divergência integral.

## Proposta final de encaminhamento
Depois de firmar a posição da Gerência, redigir encaminhamento **à SOG**, indicando a providência que cabe à Superintendência e, apenas quando o caso exigir decisão colegiada, sugerir que a SOG submeta à Diretoria proposta objetiva. Usar, conforme competência e conteúdo efetivamente apurado, a seguinte estrutura. Cada inciso deve ter suporte próprio nos autos e ser omitido quando inaplicável:

> Nesse sentido, recomendo que a SOG submeta à Diretoria Colegiada proposta de deliberação no sentido de:
>
> I - reconhecer [fato, situação jurídica ou atendimento de requisito, com fundamento];
>
> II - declarar [efeito ou consequência regulatória que caiba à Diretoria];
>
> III - aprovar [providência ou proposta dentro da competência da Diretoria, com eventuais condicionantes]; e
>
> IV - responder à consulente [síntese objetiva da resposta, **somente se houver consulta e destinatária identificada**].

Se a providência couber à própria SOG ou a outra unidade competente, formular o encaminhamento adequado sem invocar a Diretoria. A sequência `reconhecer, declarar, aprovar, responder` é um repertório, **não quatro comandos obrigatórios**. Não propor aprovação de EVTEA ou decisão inexistente, nem qualificar interessada como "consulente" se não houver consulta. Se recomendar ciência, diligência, devolução ou condicionamento, usar inciso específico em vez de encaixar a providência artificialmente em um dos verbos.

## Forma do despacho
```
AGÊNCIA NACIONAL DE TRANSPORTES AQUAVIÁRIOS
Gerência de Portos Organizados - GPO/SOG

DESPACHO
À Superintendência de Outorgas
Assunto: [objeto específico do processo]

1. Faço referência ao [ato de encaminhamento, quando houver] (SEI nº [...]), para retornar os autos.

2. A matéria foi analisada no âmbito da Nota Técnica nº [...]/[...]/GPO/SOG (SEI nº [...]), cujo teor [acompanho na íntegra / aprovo parcialmente, com as divergências a seguir / não acompanho, pelos fundamentos a seguir].

3. Pois bem. [Usar apenas se iniciar desenvolvimento argumentativo.]

4. De início, [premissa decisiva de competência, precedente ou enquadramento, se pertinente].

5. [Fatos, fundamento e consequência da questão preliminar; separar entendimento vigente e revisão proposta, se cabível.]

6. Quanto ao caso em apreço, [agrupar os itens da NT que não impedem o prosseguimento, indicando o efeito de cada um].

7. Em relação a [itens da NT de que se diverge], [explicar o fundamento e a consequência].

8. Quanto ao item [decisivo, se houver], [desenvolver fundamento próprio, prova e efeito processual].

9. Ante o exposto, [consequência concreta e encaminhamento à SOG; incisos de proposta à Diretoria apenas se pertinentes].
```
O esquema é flexível: suprimir blocos que não se aplicam, renumerar os parágrafos e escrever a versão final sem marcadores de preenchimento. Se todos os itens forem acompanhados, basta a contextualização necessária, o fecho de anuência integral e o encaminhamento, sem fabricar divergências ou questão preliminar. No exemplo SEI nº 3005027, o fecho é uma recomendação de interromper a instrução; não há proposta final em quatro incisos. Conservar esse grau de objetividade quando o caso permitir. Não inserir assinatura ou número fictício; usar os campos do SEI.

## Criação no aplicativo e confirmações finais
1. Depois da validação item a item, apresentar **a íntegra da minuta**, seguida de cartão `perguntar` com o título `Despacho à SOG · revisão final do conteúdo` e opções `Confirmar texto`, `Solicitar ajustes` e `Rever conclusões`. Se houver mudanças, revisar, mostrar a versão integral e abrir novo cartão de confirmação.
2. Somente após confirmação expressa do texto, abrir cartão `perguntar` com o título `Despacho revisado · próxima etapa` e as opções `Criar despacho no SEI`, `Manter apenas a minuta` e `Solicitar ajustes`. O primeiro botão escolhe a próxima etapa, mas **não autoriza a execução**. Se selecionado, usar a ferramenta de escrita, cujo cartão próprio solicita a aprovação efetiva. Se o usuário escolher apenas a minuta, encerrar sem escrita.
3. Com resposta afirmativa, usar as funções de consulta e criação/edição efetivamente oferecidas pelo SEI-Pro para selecionar o processo, o tipo `Despacho`, inserir o texto confirmado e apresentar o cartão de aprovação do aplicativo. O usuário decide ali pela execução. Não assinar, enviar, concluir processo ou responder externamente sem pedido específico.
4. Depois da aprovação e execução, reler o documento criado para conferir texto, parágrafos, incisos e número SEI. Informar o identificador somente se retornado. Se a criação ou a leitura falhar, informar a falha sem afirmar que o despacho foi gerado.

## Controle final
Verificar que a identidade da NT GPO foi expressamente confirmada antes da análise, sua versão, todas as conclusões e suas provas, a posição confirmada do usuário para cada uma, coerência entre anuência/divergência e o fecho, competência de SOG e Diretoria, redação de cada inciso e ausência de fatos não comprovados. O histórico ou um exemplo não autorizam replicar conclusão no processo atual.
