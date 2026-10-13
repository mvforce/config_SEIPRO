# Cadastrar contrato no Sistema de Arrendamento a partir de um processo do SEI

Use quando o usuário pedir para cadastrar, no Sistema de Arrendamento da ANTAQ, o contrato que chegou num processo do SEI (cessão de uso, arrendamento, passagem, transição, uso temporário). O cadastro é feito pelo conector MCP "Arrendamento" (ferramentas `arrendamento_*`, via mcp_buscar_tools e mcp_chamar). Em mcp_chamar, o servidor é "Arrendamento".

As ferramentas abaixo EXISTEM no conector; chame-as direto com mcp_chamar, sem procurar antes:

| tool | argumentos |
|---|---|
| arrendamento_sessao | (nenhum) |
| arrendamento_buscar_contratos | numero_contrato, porto |
| arrendamento_listar_opcoes | tipo (portos, tipos-outorga...) |
| arrendamento_consultar_campos | recurso ("contrato" ou o nome de uma aba) |
| arrendamento_criar_contrato | dados (objeto), confirmar (false = prévia, true = grava) |
| arrendamento_incluir_registro | recurso, id_contrato, dados (objeto), confirmar |
| arrendamento_consultar_contrato | id_contrato |
| arrendamento_enviar_arquivo | id_contrato, caminho_arquivo (o caminho devolvido por documento_baixar), confirmar |

Se precisar do esquema de uma delas, use mcp_buscar_tools com UMA palavra só, o trecho do nome (ex.: busca "criar_contrato"). Não busque com várias palavras nem com "arrendamento": a busca devolve só as 10 primeiras que casam com qualquer palavra, e as de cadastro ficam de fora.

## 1. Ler o processo

1. Liste os documentos do processo (documentos_listar) e leia o ofício de encaminhamento, o contrato (com o log de assinaturas no fim) e o despacho de análise, se houver (documento_ler).
2. Leia o contrato ATÉ O FIM. Cada leitura devolve um trecho (12.000 caracteres por padrão): peça `tamanho` 60000 ou continue com `inicio` até o texto acabar. O log de assinaturas fica nas últimas páginas e é dele que sai a data de assinatura.
3. Se o contrato for imagem sem texto, diga que não conseguiu ler e pare. Não preencha de memória.

## 2. Extrair os dados

Monte o objeto `dados` do contrato com estes campos. Valor que não está no processo fica de fora e é perguntado ao usuário; nunca invente.

| Campo | De onde vem |
|---|---|
| cdContrato | número do contrato como está no título, sem a sigla da autoridade (ex.: 002/2026/00) |
| noNomeInstrumento | padrão da GPO: "CONTRATO DE C.U.O. <número> - <autoridade>" para cessão de uso onerosa; para os demais, o nome do instrumento e o número |
| noTipoOutorga | Arrendamento · Contrato de Passagem · Contrato de Transição · Contrato de Uso Temporário · Cessão de Uso Onerosa · Cessão de Uso Não Onerosa (outros: arrendamento_listar_opcoes tipo=tipos-outorga) |
| tpContrato | 1 operacional · 2 não operacional (área não afeta à operação portuária, como restaurante, escritório, canteiro de obras) |
| stLicitacaoPrevia | 1 houve licitação · 2 não houve · 3 em apuração. Contrato que não cita edital nem licitação, ou que é transitório até uma licitação futura, é 2. Use 3 só quando o processo deixar dúvida real |
| cdTrigrama | trigrama do porto (arrendamento_listar_opcoes tipo=portos; Itaqui = IQI, Santos = SSZ) |
| nrCnpj, noFantasiaEmpresa | CNPJ e razão social da contratada (cessionária ou arrendatária), não da autoridade portuária |
| nrcnpjInstalacao, noInstalacao | os mesmos da contratada, salvo se o contrato indicar outra instalação portuária |
| dtAssinatura | data de celebração. Se o contrato disser que vale a última assinatura eletrônica das partes, use a última assinatura de uma PARTE no log (testemunha e validador não são partes) |
| dtOperacao | início da vigência (em geral a mesma da assinatura, salvo cláusula diferente) |
| dtFimContrato | início da vigência + prazo |
| nrPrazoContrato, nrPrazoContratoMeses, nrPrazoContratoDias | prazo em anos, meses e dias, como escrito (180 dias = 0, 0, 180) |
| noRenovacao | "Possui" ou "Nao possui" cláusula de prorrogação, conforme a cláusula de prazo do CONTRATO |
| dsExercida | "Sim" ou "Não" (prorrogação já exercida; contrato novo = "Não") |
| stContrato | A publicar · B concessão portuária ou de acesso · C não publicar (processo público = A) |
| mmObjeto | o texto da cláusula do objeto, copiado |

Nomes de pessoas chegam a você mascarados ([PESSOA_1], [CPF_2]) e vão mascarados também ao conector. Se um marcador desses cair num campo que será gravado (razão social de firma individual, texto do objeto), avise o usuário e pergunte o valor a gravar antes de enviar; não grave o marcador.

Quando o despacho ou o ofício divergir do contrato assinado (prazo, prorrogação, data), vale o contrato. Não pare para perguntar: siga com o contrato e aponte a divergência na prévia, para o usuário decidir ali.

Não pergunte a versão do contrato: contrato novo é versão 1 e o conector já preenche. O relato da situação usa o valor que o sistema devolve (Vigente, Encerrado...), não "cadastrado".

Datas no formato AAAA-MM-DD. Em dúvida sobre nomes ou obrigatórios: arrendamento_consultar_campos recurso=contrato.

## 3. Conferir e gravar

1. Chame arrendamento_sessao e diga ao usuário em qual ambiente está (produção ou homologação).
2. Chame arrendamento_buscar_contratos com numero_contrato e porto. Se já existir, mostre e pare.
3. Chame arrendamento_criar_contrato com `dados` e SEM confirmar. Mostre ao usuário, em tabela, o que será gravado e destaque cada valor que foi interpretação sua (data de assinatura, término calculado, tipo de contrato).
4. Só depois do "pode gravar" do usuário, repita com confirmar=true.
5. Busque de novo pelo número para obter o idContratoArrendamento.

## 4. Abas (sempre prévia, depois confirmar=true)

Com arrendamento_incluir_registro, id_contrato do passo anterior:

- recurso=aspectos-fisicos: {"vlAreaTotal": área em m²}.
- recurso=contratos-processos: {"nrProcesso": número do processo SEI (11111.111111/1111-11), "dsAtoAntaq": "Acórdão" ou "Resolução", "nrAto": "SEI nº <número SEI do contrato>", "dtAto": data do ato}. Sem acórdão nem resolução, a GPO usa "Acórdão" e, em dtAto, a data em que o contrato foi protocolado no SEI (está no Recibo Eletrônico de Protocolo ou na data do documento na árvore). Nunca a data de hoje. Confirme com o usuário.
- recurso=observacoes: {"noResponsavel": unidade do usuário, "dtObservacao": hoje, "dsObservacao": resumo em 2 a 4 frases com finalidade, valor mensal, valor global e valor da garantia (os três, quando o contrato trouxer), condições de prazo e o resultado do despacho de análise}.
- Só se o contrato trouxer: investimentos-previstos, bens, coordenadas, perfis-carga-passageiros, tipos-servicos-contrato (campos em arrendamento_consultar_campos).

## 5. Anexar o contrato

Depois das abas, anexe o PDF do contrato assinado:

1. Baixe o documento do contrato com documento_baixar (ferramenta do SEI, não do conector), passando o nº SEI dele. O usuário aprova no cartão. A ferramenta devolve o caminho do arquivo em Downloads/SEI Pro/<processo>/.
2. Chame arrendamento_enviar_arquivo com id_contrato e `caminho_arquivo` igual ao caminho devolvido, copiado sem mudar nada, SEM confirmar. Mostre nome e tamanho ao usuário.
3. Com o "pode anexar", repita com confirmar=true.

Anexe só o contrato (documento externo). documento_baixar não baixa documento criado no editor do SEI (despacho, ofício interno) nem sigiloso: se recusar, diga qual documento ficou sem anexo e siga. O mesmo nome de arquivo não pode ser anexado duas vezes ao mesmo contrato.

## 6. Fechar

Consulte arrendamento_consultar_contrato e relate: id, situação, abas gravadas, anexo e o que ficou pendente.

## Erros

- "[sessao] ... janela de login": peça ao usuário para concluir o login da Microsoft na janela do Chrome que abriu e repita a mesma chamada.
- "[validacao]": o dado foi recusado antes de enviar; corrija conforme a mensagem.
- "[validacao] ... fora das pastas permitidas" ou "extensão não aceita" ao anexar: o arquivo não veio de documento_baixar ou não é documento; baixe de novo com documento_baixar e use o caminho devolvido.
- "[acesso]" ou "[permissao]": o usuário não tem acesso ou perfil no sistema; informe e pare.
- "não está rodando neste computador": o servidor do conector Arrendamento está desligado; peça ao usuário para iniciá-lo e repita a chamada.
- "não tem autorização para acessar o endereço": peça ao usuário para abrir a configuração do agente, em Conectores, e clicar em "Testar conexão" no conector Arrendamento.
