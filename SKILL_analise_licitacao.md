---
name: analise-licitacao-portuaria
description: Analisa documentos preparatórios e EVTEA de licitação de arrendamento portuário, ordinária ou simplificada, com matriz de evidências e minuta de manifestação GPO/SOG.
---

# Análise de licitação portuária

## Quando ativar
Quando o pedido envolver preparatórios de licitação de área de porto organizado, EVTEA, aderência à Resolução ANTAQ nº 85/2022, exame de premissas regulatórias ou minuta de despacho/nota técnica da GPO/SOG. Não usar para autorização de contrato de transição nem para conferência de seu primeiro instrumento celebrado.

## Relação com o contexto fixo
Aplicar o contexto de Tavares já fornecido pela aplicação. Este arquivo acrescenta o procedimento específico do modelo `modelo_analise_licitação.pdf`; não reproduzir fatos de RDJ07 nem presumir que conclusões e normas do exemplo valham para outro processo. Prevalecem a solicitação concreta, os documentos atuais e as decisões vinculantes do caso.

## Cartões com botões no SEI-Pro
Quando for necessária uma escolha do usuário que altere o rumo da análise, chamar a ferramenta nativa `perguntar` com os campos `pergunta` e `opcoes`. Isso produz um cartão de opções clicáveis e um campo `Outra resposta...`. Não simular botões com Markdown ou HTML na mensagem. O aplicativo aceita até seis opções; usar rótulos curtos e específicos, com contexto suficiente no título do cartão.

Exemplos de chamadas, com dados reais substituindo os marcadores:

```json
{"pergunta":"Licitação [ÁREA] · confirme o processo a analisar","opcoes":["Analisar este processo","Escolher outro processo","Ver árvore primeiro"]}
```

```json
{"pergunta":"Achado TV1.[ITEM] · qual consequência adotar?","opcoes":["Sem óbice","Ajuste antes de avançar","Pedir diligência","Rever fundamento"]}
```

```json
{"pergunta":"Nota Técnica [ÁREA] · conclusão e encaminhamento","opcoes":["Confirmar conclusão","Rever ressalvas","Alterar encaminhamento","Ver evidências"]}
```

Antes do cartão de cada achado, apresentar em texto conciso a evidência (SEI e localização), o requisito, a justificativa e a consequência sugerida. O botão registra a decisão do usuário; `Ver evidências` ou `Rever fundamento` apenas abre explicação e depois novo cartão de decisão. Se o usuário trouxer tese diversa no campo livre, verificar a prova e propor nova redação; não tratar seleção de "rever" como aprovação tácita.

Após exibir a **minuta integral da Nota Técnica e as três tabelas renderizadas**, abrir cartão `perguntar` com título `Revisão final · Nota Técnica [ÁREA]` e botões `Confirmar texto`, `Solicitar ajustes` e `Rever conclusões`. Após confirmação, abrir cartão de **próxima etapa** com `Criar Nota Técnica no SEI`, `Manter apenas minuta` e `Solicitar ajustes`. Esse cartão escolhe o caminho, mas não autoriza gravar. A criação usa ferramenta de escrita do aplicativo e seu próprio cartão de aprovação. Não usar `perguntar` como aprovação da escrita.

## Leitura da árvore e identificação do comando
Antes de estudar o EVTEA, identificar a **ordem concreta dirigida à unidade**. Na árvore processual, localizar o despacho de encaminhamento mais recente e pertinente à área, verificar seu emissor, destinatário, objeto e finalidade, e ler o inteiro teor. Distinguir: (a) ofício externo que remete os estudos; (b) despacho da SELC ou de outra unidade que demanda análise à SOG/GPO; (c) despachos antigos já atendidos; (d) manifestações técnicas anteriores. O ofício não substitui automaticamente a ordem interna. Não tomar um documento anterior ou um ato de aprovação do Poder Concedente como comando atual à GPO. Se houver vários comandos, rastrear a cadeia de encaminhamento até a unidade, sua data e eventuais delimitações de escopo.

No exemplo RDJ10 do Processo 50300.019865/2024-19, o usuário aponta o **Despacho SEI nº 3001939** como comando atual e informa que as peças pertinentes ficam, na árvore, **imediatamente acima desse despacho SELC e abaixo do ofício da Secretaria Nacional de Portos**. Procurar esse despacho no processo em tempo real, ler seu texto e identificar o que exige da unidade. O arquivo de referência disponibilizado contém o Ofício SNP SEI nº 3001879, a decisão SEI nº 3001880, o Despacho nº 3001881, o ato justificatório SEI nº 3001882, a Nota Técnica da Infra S.A. SEI nº 3001884 e as Seções A a F SEI nº 3001890 a 3001895; **não contém o SEI nº 3001939**. Portanto, estes números só ajudam a reconhecer o exemplo; não presumir o teor do comando ausente nem sua posição exata com base na ordem dos arquivos do ZIP.

Usar a **posição na árvore efetivamente exibida pelo aplicativo**, e não a ordem numérica dos SEI, a data de exportação ou a sequência de arquivos em um ZIP, para delimitar o bloco documental. Registrar seus dois marcos: ofício da SNP e despacho SELC de encaminhamento. Percorrer **todas as peças entre os marcos** no sentido visual da árvore e relacionar seus números SEI. Ler anexos ou peças referenciadas fora do intervalo se forem necessários à análise; identificá-los como complementares, com justificativa. Se o despacho indicado não for localizável, não inferir seu conteúdo: informar a ausência, examinar a cadeia disponível e solicitar acesso ao despacho antes de fixar escopo ou redigir conclusão definitiva.

| Papel no processo | Exemplo de 2026 | Verificação necessária |
| --- | --- | --- |
| Marco de remessa externa | Ofício SNP 3001879 | Peças encaminhadas, objeto e caráter restrito |
| Decisão do Poder Concedente | 3001880 | O que foi aprovado e determinado; não é o comando da GPO |
| Subsídios e estudo | 3001881, 3001882, 3001884, 3001890 a 3001895 | Versão pertinente, conteúdo e anexos no bloco da árvore |
| Comando interno atual indicado | Despacho SELC 3001939 | Ler inteiro teor no SEI; identificar destinatário e escopo |
| Histórico anterior | Despacho SELC 2358227, NT 170/2024/GPO/SOG 2365952 | Não confundir análise de 2024 com novo estudo de 2026 |

## Sequência de trabalho
1. Confirmar o despacho que efetivamente pede a manifestação e transcrever em uma linha o comando operacional: quem encaminha, a quem, para qual análise, de quais peças e com que finalidade. Se houver limite expresso, prazo, condicionante ou pedido de minuta, registrar. Só então definir o produto esperado; a análise técnica pode ser Nota Técnica, acompanhada de despacho de encaminhamento, conforme a ordem e o fluxo real.
2. Montar inventário da faixa pertinente da árvore: título, SEI, emissor, data/versão, relação com o comando e legibilidade. Verificar se o ofício externo e sua decisão aprovam a mesma versão do estudo incluída no processo. Ler os anexos e as peças relevantes por inteiro; se um PDF digitalizado for parcialmente extraído, tentar outras funções de leitura e explicitar a limitação.
3. Identificar processo, área, porto, cargas, órgão aprovador, fase e tipo de licitação a partir das peças atuais. No exemplo RDJ10, o material de 2024 foi analisado como licitação simplificada, enquanto os documentos de 2026 se apresentam em seções A a F no formato ordinário. Não transportar enquadramento nem conclusão de uma rodada para outra.
4. Fazer matriz documental: documento exigido, versão e SEI, localização, estado (comprovado, não comprovado, inaplicável justificado, leitura pendente) e observação. Para a modalidade ordinária, verificar A apresentação, B mercado, C engenharia, D operacional, E financeiro, F ambiental e anexos; para a simplificada, identificar a estrutura aplicável à versão efetivamente analisada.
5. Fazer matriz analítica: requisito e base normativa conferida, peça/trecho, confrontação, lacuna, consequência e providência. No modelo de referência, TV1 contempla Resolução ANTAQ nº 85/2022 e TV2 determinações e recomendações do TCU. Conferir teor, destinatário e aplicabilidade dos acórdãos. Presença de uma seção não equivale a atendimento do requisito.
6. Conferir coerência entre demanda, capacidade, engenharia, investimentos, cronograma, operação, receitas, custos, pagamentos, MMC/MME e obrigações futuras. Confrontar com PDZ, planejamento setorial, concorrência e interferências portuárias relevantes, se houver suporte documental. Quantificar diferenças verificáveis e explicitar o efeito na modelagem.
7. Distinguir aprovação pelo Poder Concedente, exame técnico solicitado à unidade e providências da SELC/CPLA. A aprovação do EVTEA não impede apontar inconsistências regulatórias relevantes; não pressupor competência para uma segunda aprovação do estudo. Propor diligência quando faltar premissa essencial.
8. Concluir de modo único e fundamentado: atendimento, atendimento parcial com ajustes e avaliação expressa de eventual óbice, ou insuficiência que exija complementação. Referenciar cada ressalva à matriz e ao comando interno. Não copiar conclusões alternativas de modelos ou manifestações de fases anteriores.

## Estrutura HTML obrigatória da Nota Técnica de referência
Quando o produto for uma Nota Técnica, usar como **matriz de estrutura e formatação** o documento `[13]-2365952_Nota_Tecnica_170.html` (SEI nº 2365952), que contém HTML nativo exportado do SEI. Consultar, se disponível no processo, o próprio documento para conferir a aparência e o tipo documental antes de criar a nova peça. Reproduzir a estrutura editorial e os estilos que o editor do SEI aceitar; **substituir integralmente o conteúdo factual, jurídico e as conclusões** pela análise atual. O exemplo é de 2024, modalidade simplificada; os estudos RDJ10 de 2026 têm formato ordinário. Não copiar o enquadramento antigo, os indicadores de atendimento, as citações de atos não aplicáveis, o nome do assinante, assinatura ou numeração de documento.

A estrutura observada no HTML exportado é: título da Nota Técnica; parágrafo `Assunto`; `INTRODUÇÃO` com parágrafos numerados, identificação da modalidade e tabela de conformidade documental; `ANÁLISE` com delimitação de competência/escopo, tabela TV1 de requisitos do EVTEA e tabela TV2 de acórdãos TCU aplicáveis; `CONCLUSÕES` com **uma única conclusão** fundamentada e encaminhamento `À consideração superior.`. O arquivo tem seis elementos `<table>`: as três primeiras tabelas são de conteúdo (inventário documental, TV1 e TV2), e as três últimas pertencem à apresentação/rodapé do SEI. Não copiar estas últimas como tabelas analíticas. Seus títulos usam `p.Item_Nivel1`, parágrafos principais `p.Item_Nivel2`, incisos `p.Item_Inciso_Romano`, alínea conclusiva `p.Item_Alinea_Letra`, células com `p.Tabela_*`. A numeração visual decorre de regras CSS `counter` do SEI. Confirmar no documento criado se o editor preservou classes, numeração, tabelas, largura das colunas, acentuação e alinhamento; se não preservou, inserir numeração textual explícita e formatação compatível pelo editor antes de propor aprovação.

Modelo de corpo HTML sem dados do caso, a adaptar após a análise e confirmação do usuário:

```html
<p class="Texto_Alinhado_Esquerda_Maiusc_Negrito">NOTA TÉCNICA Nº [GERADO PELO SEI]/GPO/SOG</p>
<p class="Texto_Justificado"><strong>Assunto:</strong> Análise dos documentos preparatórios para a licitação da área [ÁREA], no Porto Organizado de [PORTO].</p>
<p class="Item_Nivel1">INTRODUÇÃO</p>
<p class="Item_Nivel2">[Objeto, área, ofício e documentos encaminhados; referências SEI atuais.]</p>
<p class="Item_Nivel2">[Ato decisório do Poder Concedente, versão do EVTEA e finalidade do encaminhamento.]</p>
<p class="Item_Nivel2">[Comando à unidade, despacho lido, destinatário e escopo.]</p>
<p class="Item_Nivel2">Tipo de processo:</p>
<p class="Item_Inciso_Romano">[Modalidade efetivamente comprovada e motivo.]</p>
<p class="Texto_Centralizado"><strong>VERIFICAÇÃO DE CONFORMIDADE DOCUMENTAL</strong></p>
<table border="1" style="border-collapse:collapse;width:100%;"><thead><tr><th>Documento</th><th>SEI / versão</th><th>Situação</th><th>Observações</th></tr></thead><tbody><tr><td>[Peça]</td><td>[Número]</td><td>[Situação comprovada]</td><td>[Evidência ou lacuna]</td></tr></tbody></table>
<p class="Item_Nivel1">ANÁLISE</p>
<p class="Item_Nivel2">[Competência, limites do pedido e exame crítico das peças atuais.]</p>
<p class="Item_Nivel2">[Critérios jurídicos e regulatórios conferidos no caso.]</p>
<p class="Texto_Centralizado"><strong>TABELA DE VERIFICAÇÃO Nº 01 (TV1) - [MODALIDADE]</strong></p>
<table border="1" style="border-collapse:collapse;width:100%;"><thead><tr><th>Item</th><th>Fundamento</th><th>Origem / SEI</th><th>Exigência</th><th>Situação</th><th>Observação fundamentada</th></tr></thead><tbody><tr><td>TV1.I</td><td>[Norma]</td><td>[Peça]</td><td>[Exigência]</td><td>[Resultado]</td><td>[Fundamentação]</td></tr></tbody></table>
<p class="Texto_Centralizado"><strong>TABELA DE VERIFICAÇÃO Nº 02 (TV2) - TCU</strong></p>
<table border="1" style="border-collapse:collapse;width:100%;"><thead><tr><th>Item</th><th>Determinação ou recomendação aplicável</th><th>Origem / SEI</th><th>Critério</th><th>Situação</th><th>Observação fundamentada</th></tr></thead><tbody><tr><td>TV2.I</td><td>[Acórdão, item e destinatário]</td><td>[Peça]</td><td>[Critério]</td><td>[Resultado]</td><td>[Fundamentação]</td></tr></tbody></table>
<p class="Item_Nivel1">CONCLUSÕES</p>
<p class="Item_Nivel2">[Síntese única, ressalvas vinculadas às tabelas, impacto no prosseguimento e encaminhamento.]</p>
<p class="Texto_Justificado_Recuo_Primeira_Linha">À consideração superior.</p>
```

O título, referência, assinatura, cabeçalho e rodapé podem ser campos gerados pelo próprio SEI: aproveitar esses campos do tipo `Nota Técnica` em vez de inserir número fictício ou assinar como outra pessoa. Se o aplicativo só aceitar texto puro, criar o tipo documental correto e usar a função de escrita/edição que preserve HTML quando disponível; não enviar etiquetas HTML literais ao usuário final como se fossem o documento renderizado. Se não houver função capaz de preservar tabelas e formatação, informar a limitação e pedir ao usuário que aprove apenas uma versão cuja aparência tenha sido verificada. A confirmação do conteúdo textual e a aprovação da operação no SEI permanecem etapas distintas.

## Saída
Se pedido um texto, redigir a Nota Técnica com `INTRODUÇÃO`, `ANÁLISE` e `CONCLUSÕES` segundo a estrutura HTML acima no estilo do contexto fixo, com parágrafos numerados quando apropriado, tabela concisa e referências SEI. Se pedido um diagnóstico, apresentar matriz e pontos decisórios antes da minuta. Distinguir constatação, alegação da parte e inferência técnica. Não inventar número SEI, ato, percentuais ou fundamento legal. Quando o documento ou norma não estiver acessível, escrever `não verificado nos autos disponibilizados` e especificar a peça necessária.

## Fluxo interativo obrigatório com o usuário
1. Ao ser acionada, identificar o processo já aberto, localizar o despacho que determina a análise e examinar os documentos acessíveis com as funções de leitura e consulta do agente do SEI-Pro. Se não houver processo identificável, usar `perguntar` com opções `Informar processo`, `Usar processo aberto` (se houver tela ativa) e `Cancelar análise`; aceitar também o campo livre. Solicitar outras informações apenas quando indispensáveis, em perguntas curtas; não exigir que o usuário reapresente peças que o agente consegue ler.
2. Concluída a análise, apresentar na conversa uma prévia substantiva: fatos confirmados e documentos SEI, matriz de achados relevantes, limites de leitura, proposta de conclusão e minuta completa da Nota Técnica de análise dos preparatórios da licitação, com prévia renderizada das três tabelas. A minuta deve estar visível antes de qualquer proposta de criação no SEI.
3. Ao final dessa prévia, abrir cartão `perguntar` para confirmar o conteúdo e a conclusão da minuta, destacando modalidade, pendências, óbices e encaminhamento. Usar os botões `Confirmar texto`, `Solicitar ajustes` e `Rever conclusões`. Se houver correções, incorporá-las, mostrar a versão integral revisada e repetir o cartão de confirmação. Não interpretar silêncio como confirmação.
4. Somente depois da confirmação expressa da versão final, abrir cartão `perguntar` de próxima etapa com `Criar Nota Técnica no SEI`, `Manter apenas minuta` e `Solicitar ajustes`. A escolha da primeira opção não é aprovação da operação: esta dependerá do cartão próprio da ferramenta de escrita. Se o usuário desejar apenas o texto, encerrar com a versão aprovada na conversa.
5. Se houver resposta afirmativa à criação, utilizar as funções efetivamente disponíveis no agente SEI-Pro para criar documento no processo correto e inserir o texto final confirmado, selecionando o tipo documental `Nota Técnica` e preservando a estrutura HTML da referência. Não reduzir tabelas a listas de texto. Antes de chamar a função de escrita, conferir processo, tipo, título quando aplicável e texto. Não inventar nome de ferramenta nem afirmar criação quando houver apenas minuta. Respeitar o cartão de aprovação exibido pelo aplicativo; o usuário deve aprovar a operação ali. Não assinar, tramitar, dar ciência nem alterar outros dados sem pedido próprio.
6. Após a execução aprovada no aplicativo, confirmar o resultado pelas funções de leitura e informar número/identificador SEI se retornado. Se a função falhar, não declarar documento criado; explicar o erro e manter a minuta disponível.

## Controle final
Confirmar se o comando à unidade foi lido, se o bloco entre ofício e despacho foi inventariado na ordem real da árvore, se documentos de 2024 foram separados dos de 2026, se a modalidade foi identificada; se cada conclusão tem suporte em peça e localização; se decisões atuais e alterações do estudo foram consideradas; se há exame regulatório além da mera presença formal quando o objeto assim exige; se citações normativas e determinações do TCU foram conferidas no texto aplicável; e se a proposta é compatível com a fase processual.
