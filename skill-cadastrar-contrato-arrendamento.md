# Cadastrar contrato no Sistema de Arrendamento a partir de um processo do SEI

Use quando o usuário pedir para cadastrar, no Sistema de Arrendamento da ANTAQ, o contrato que chegou num processo do SEI (cessão de uso, arrendamento, passagem, transição, uso temporário), ou para registrar os efeitos de termo de apostilamento em instrumento já cadastrado. Após a confirmação e verificação do cadastro, prepare o despacho de registro e, crie-o diretamente no processo SEI por meio do agente SEI-Pro, sem exibir uma minuta antecipada; respeite apenas o cartão de autorização de escrita exigido pelo SEI-Pro. Para apostilamentos, siga a rotina específica abaixo: não crie outro contrato. O cadastro é feito pelo conector MCP "Arrendamento" (ferramentas `arrendamento_*`, via mcp_buscar_tools e mcp_chamar). Em mcp_chamar, o servidor é "Arrendamento".

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

## 7. Rotina específica — incluir Termo de Apostilamento em contrato existente

**Condição de acionamento.** Use esta rotina quando o pedido envolver apostilamento. Ela não substitui o fluxo de criação para contratos novos. Um apostilamento pode retificar dados, registrar informações ou produzir outros efeitos definidos no próprio instrumento; não assuma que todo apostilamento altera CNPJ ou que produz efeitos sobre todos os instrumentos relacionados.

### 7.1 Identificar o instrumento efetivamente alcançado

1. Consulte a sessão com `arrendamento_sessao` e informe ao usuário o ambiente (produção ou homologação).
2. No SEI, liste e leia integralmente o termo de apostilamento, o contrato original e os aditivos ou outros documentos necessários para interpretar seu objeto, suas referências e a cadeia de alterações. Confira assinaturas, datas e identificação dos signatários quando relevantes. Documento sem texto legível: não presuma seu conteúdo; interrompa a etapa dependente dele.
3. No Sistema de Arrendamento, busque o contrato por número, porto e demais identificadores disponíveis. Consulte o registro-base e os aditivos cadastrados, inclusive seus vínculos e IDs. Não use apenas a coincidência de processo, a ordem cronológica ou o documento mais recente para decidir o destino.
4. Determine e justifique, citando o trecho/documento SEI pertinente, se a correção incide no contrato-base, em aditivo específico ou em mais de um instrumento. Em caso de ambiguidade material, **não grave nem anexe** até que a identificação seja resolvida pelo processo ou confirmada pelo usuário com suporte documental.
5. Verifique previamente se o apostilamento ou a correção já estão cadastrados, evitando duplicação. **Não crie um contrato novo.**

### 7.2 Planejar as correções com escopo estrito

1. Elabore um quadro de consistência: **instrumento/ID afetado | campo | valor atual | valor proposto | fundamento (cláusula e SEI) | efeito sobre outros registros | situação da validação**.
2. Altere somente os campos expressamente corrigidos ou inequivocamente alcançados pelo apostilamento, por exemplo, `nrCnpj` da contratada e, **somente se comprovada a correspondência**, `nrcnpjInstalacao`. Confira identidade da pessoa jurídica e da instalação; não pressuponha que seus CNPJs sejam sempre iguais.
3. Preserve os demais campos e os dados históricos dos aditivos tal como assinados, salvo retificação expressamente aplicável a cada um. Não replique automaticamente correções do contrato-base.
4. Não infira datas, identificadores ou campos obrigatórios ausentes. Diferencie assinatura, início dos efeitos, protocolo no SEI e registro no sistema. Em divergência entre instrumentos ou insuficiência documental relevante, destaque a pendência e não a resolva por suposição.
5. Antes de chamar ferramenta de **edição**, consulte o esquema efetivamente disponível no MCP (busca pelo trecho singular do nome, se necessário) e confirme se aceita alterar o registro existente e quais identificadores/campos exige. **`arrendamento_criar_contrato` não serve para atualizar; `arrendamento_incluir_registro` não deve ser usado como edição sem comprovação de que esse recurso permite atualização.** Se não houver ferramenta de atualização suportada, pare a etapa e relate a limitação, sem simular gravação.
6. Apresente prévia detalhada, incluindo ambiente, IDs, quadro de diferenças e potenciais impactos. Use `confirmar=false` se a ferramenta de atualização o suportar. **Só execute a alteração com autorização expressa do usuário**, utilizando `confirmar=true` quando essa for a convenção da ferramenta; caso o conector use outro mecanismo, siga o esquema real e nunca interprete a ausência do parâmetro como autorização tácita.
7. Reconsulte o registro e compare valores efetivamente persistidos com o plano. Se houver divergência, suspenda as etapas dependentes e informe o problema.

### 7.3 Registrar processo e ato, quando cabível

1. Verifique se já há vínculo correspondente na aba `contratos-processos`. Não duplique processos ou atos cadastrados.
2. Quando couber, vincule ao **registro do instrumento alcançado** o número do processo SEI e, em `nrAto`, a referência `SEI nº <número do apostilamento>`, após conferir os campos permitidos em `arrendamento_consultar_campos` para `contratos-processos`.
3. Para `dsAtoAntaq`, use a categoria que o sistema efetivamente admite. Se não houver Acórdão ou Resolução, a convenção operacional da GPO mencionada nesta skill é selecionar **"Acórdão"**; entretanto, **isso é somente uma classificação imposta pelo cadastro, não transforma o apostilamento em Acórdão**. Mostre explicitamente a incongruência na prévia e peça confirmação do usuário antes de utilizá-la. Se houver opção própria para apostilamento, prefira a categoria correta.
4. Para `dtAto`, use a data de protocolo do apostilamento comprovada no SEI, quando aplicada a convenção da unidade; **não utilize a data de assinatura, de hoje ou a do contrato original em substituição automática**. Se não constar protocolo confiável, solicite o dado antes de gravar.
5. Execute prévia, obtenha autorização expressa e então grave; reconsulte o vínculo e verifique processo, número SEI, tipo e data.

### 7.4 Baixar, nomear e anexar o documento ao registro correto

1. Baixe pelo SEI o PDF do termo assinado por meio de `documento_baixar`, respeitando eventuais limitações de documentos internos ou sigilosos. Identifique o ID do contrato-base ou aditivo **que o termo efetivamente corrige**.
2. Apresente ao usuário um nome descritivo, por exemplo: `Termo de Apostilamento - Correção do CNPJ da SRRF02 (SEI nº 2894521).pdf`. Este é um **exemplo de nomenclatura, não um dado do processo analisado**.
3. O conector descrito nesta skill **não disponibiliza ferramenta de renomeação de anexos**. Somente se houver recurso local efetivamente acessível e permitido, renomeie ou copie o PDF para um nome claro **dentro das pastas aceitas para envio**, preservando conteúdo, extensão e vínculo com o documento original; não presuma que seja possível renomear. Use o caminho absoluto exato resultante. Se o conector aceitar apenas o caminho original devolvido por `documento_baixar`, mantenha-o e explique a limitação de nomenclatura.
4. Confirme o destino, nome, tamanho e, se possível, identidade do arquivo, antes de anexar. Use `arrendamento_enviar_arquivo` sem confirmação para a prévia, obtenha autorização expressa ("pode anexar") e só então envie com `confirmar=true`. **Não associe ao aditivo apenas porque está no mesmo processo.**
5. Após o envio, consulte a listagem de anexos ou detalhe do registro e confirme que o novo PDF aparece com o nome e vínculo corretos. **Não presuma sucesso pela chamada de envio isolada.**
6. Se houver anexo incorreto anterior, **não o exclua até comprovar o envio e o vínculo do correto**. A exclusão exige ferramenta disponível e suporte explícito, avaliação do impacto sobre a trilha de auditoria, identificação inequívoca do anexo e autorização separada do usuário. Se o envio novo falhar, preserve integralmente o existente. Se não houver exclusão permitida, mantenha-o e relate pendência de saneamento, sem alegar remoção.

### 7.5 Verificação final e relato

1. Consulte novamente o contrato-base e todos os aditivos potencialmente afetados. Verifique tanto os **campos alterados** quanto a **preservação dos não abrangidos**.
2. Confirme separadamente: ID e situação do registro corrigido; valores antes/depois; identificação SEI e data do processo/ato; PDF, nome e vínculo efetivos; eventuais duplicidades ou anexos incorretos.
3. Informe, de modo explícito, o que foi **apenas analisado**, o que teve **prévia**, o que foi **gravado e verificado**, e as etapas **não executadas ou pendentes**, inclusive insuficiência de permissão ou inexistência de ferramenta de edição, renomeação ou exclusão.
4. Nenhuma autorização para atualizar um campo ou anexar um PDF abrange automaticamente modificar outro registro, excluir arquivo ou executar nova operação de gravação.

## 8. Despacho de registro após o cadastro — criação no SEI-Pro

**Aplica-se a contratos novos, termos aditivos, retificações, apostilamentos e outros instrumentos efetivamente registrados ou atualizados.** Esta etapa integra o fluxo: após a verificação do cadastro no sistema Arrendamento, não encerre a atividade sem criar diretamente o despacho no SEI pela ferramenta de criação de documento interno do SEI-Pro, respeitada a aprovação operacional do próprio agente. A mera prévia de gravação não autoriza afirmar que o cadastro ocorreu.

### 8.1 Pré-condição e conferência

1. Reconsulte o Sistema de Arrendamento e confirme a efetiva persistência do contrato ou alteração: ambiente, ID, número, instrumento alcançado, informações principais, abas pertinentes e, se houver, anexos e seus vínculos. Registre no relato as pendências.
2. Confira qual processo SEI deve receber o despacho: normalmente o processo que encaminhou o instrumento para registro, salvo determinação/documentação em sentido diverso. Não crie o despacho em processo apenas relacionado sem comprovar o vínculo.
3. Antes de redigir, leia os documentos SEI relevantes: petição/ofício de encaminhamento, instrumento assinado e seus anexos, análise técnica ou deliberação prévia, se houver; para aditivos e apostilamentos, examine o instrumento original e os antecedentes necessários. Não afirme regularidade, aprovação, anuência, eficácia ou fundamento normativo se não estiverem documentalmente demonstrados.
4. Quando apenas parte da rotina tiver sido concluída, descreva a **providência efetivamente executada**, sem usar "cadastrado" para etapas ainda não gravadas. Diante de falha material ou divergência no registro, proponha texto de pendência, mas não finalize um despacho que ateste conclusão inexistente.

### 8.2 Padrão de redação GPO extraído dos 11 despachos-modelo

Produza o **conteúdo de um despacho da GPO**, normalmente de 2 a 5 parágrafos numerados, com:
- **Assunto:** "Cadastro do [tipo e número do instrumento] - [contratada] - Porto de [nome]"; para apostilamento, identificar "Termo de Apostilamento ao [contrato]" e a retificação tratada.
- **Parágrafo inicial:** "Trata-se de..." ou "Refiro-me a...", identificando órgão/autoridade portuária remetente, documento de encaminhamento e número SEI, instrumento assinado e número SEI, contratante/contratada e vínculo com o porto.
- **Parágrafo de objeto:** síntese fiel da cláusula pertinente, incluindo área, finalidade, prazo, datas e alterações **somente quando relevantes e comprovados**, sem transcrever cláusulas inteiras desnecessariamente.
- **Parágrafo de antecedentes, se necessário:** decisão, Nota Técnica, ofício anterior, contrato substituído ou aditivo relacionado, com números SEI corretos. Diferencie registro cadastral de análise regulatória. Só mencione adequação/regularidade quando houver suporte técnico efetivo.
- **Fecho:** quando todo registro relevante estiver confirmado: "Registra-se, por fim, que o instrumento foi cadastrado no Sistema de Gestão de Arrendamento Portuário." Em apostilamento que apenas corrigiu dados: "Registra-se, por fim, que as alterações constantes do Termo de Apostilamento foram lançadas no registro do instrumento correspondente, no Sistema de Gestão de Arrendamento Portuário." Adapte o fecho se houve cadastro parcial, e explicite a pendência sem afirmar conclusão integral.
- **Conclusão do processo:** "Diante do exposto, concluem-se os autos nesta unidade." **Somente se** o processo estiver apto a ser concluído, sem providência substancial pendente e se esse for o encaminhamento documentalmente adequado. Este texto não autoriza executar a ação de concluir processo.
- **Assinatura:** não invente nome, cargo, data de assinatura, código verificador ou CRC. Utilize a estrutura/cabeçalho institucional do próprio tipo documental Despacho GPO no SEI; deixe a assinatura para o responsável no sistema, sem assinatura automática e sem reproduzir rodapés de PDFs anteriores.

**Estilo:** jurídico-administrativo, objetivo, conectivos naturais e frases curtas; sem travessão. Evite fórmulas de deferimento ou atestado de legalidade em um despacho cujo único objeto é registrar providência cadastral. Se houver ressalva relevante na análise ou falha de anexação, relate-a expressamente. O nível de detalhe pode ser maior quando houver alterações substantivas, tal como os exemplos de aditivos de exploração portuária; não expanda artificialmente despachos simples.

**Regra obrigatória de identificação do documento na árvore do SEI: o resultado deve aparecer como "Despacho GPO", jamais "Despacho Despacho".** Diferencie os campos usados pelo SEI-Pro:
- **Tipo documental:** consulte o catálogo real de tipos internos. Se o tipo for **"Despacho"**, selecione-o como tipo, sem duplicar essa palavra em outro campo. Caso haja um tipo específico **"Despacho GPO"**, use-o apenas quando confirmado que esse é o tipo documental correto da unidade.
- **Descrição/nome na árvore:** não preencha com "Despacho" nem "Despacho GPO" se o SEI já prefixar automaticamente o tipo. Prefira **deixar a descrição em branco**, quando permitido. Se houver campo obrigatório de descrição complementar, preencha apenas **"GPO"** caso a ferramenta use esse campo para formar "Despacho GPO", ou um assunto substantivo, nunca o nome do próprio tipo repetido.
- **Assunto no corpo:** é o assunto do contrato cadastrado, não um segundo título "Despacho".
- **Verificação antes da escrita:** confira a pré-composição de tipo + descrição fornecida pela ferramenta. Se resultar em "Despacho Despacho", corrija o campo duplicado **antes de criar**, sem trocar arbitrariamente o tipo.
- **Verificação posterior:** consulte a árvore e confira o nome exibido. Se não ficar "Despacho GPO", relate a divergência e só tente corrigi-la se houver ferramenta de edição do nome/descrição e aprovação operacional para isso. Não crie um segundo documento para tentar corrigir o primeiro.

Não use "Despacho GPO" como valor de um campo livre só porque esse é o nome esperado na árvore; determine primeiro como o SEI compõe a identificação final. Se o catálogo ou as regras de nomenclatura não puderem ser consultados, preserve o tipo correto da unidade e evite qualquer descrição redundante.

### 8.3 Integração operativa com o agente SEI-Pro

1. Após concluir e verificar a etapa cadastral, **não apresente minuta de despacho no chat e não crie uma etapa de revisão textual ou confirmação conversacional específica para o despacho**. Elabore o conteúdo internamente e inicie diretamente o fluxo de criação de documento interno no SEI, sujeito ao cartão de aprovação de escrita do próprio SEI-Pro. Não invente interface ou ferramenta específica.
2. Identifique, nas ferramentas efetivamente disponibilizadas pelo **agente SEI-Pro**, a operação de **criar documento interno** e a de **escrever/editar seu conteúdo**. Consulte suas descrições e parâmetros reais; não confunda ferramentas do conector externo Arrendamento com as ferramentas internas do SEI. Se não estiverem disponíveis, apresente a minuta para inserção manual e relate a limitação.
3. No **processo correto**, acione a ferramenta de criação de documento interno usando o **tipo documental correto para Despacho da GPO**, conforme as regras de composição do nome na árvore acima, preferencialmente com o modelo institucional da unidade, e insira o texto elaborado no editor do SEI. **Não solicite uma aprovação de minuta no chat**. A execução da escrita dependerá exclusivamente da autorização no cartão próprio do SEI-Pro, quando exigida. Nunca crie documento externo PDF no lugar de documento interno editável, salvo instrução expressa.
4. A criação e o preenchimento, quando dependerem de operações distintas, devem respeitar cada aprovação operacional exigida pelo SEI-Pro. Não acrescente uma aprovação conversacional redundante nem interprete a autorização de uma operação como autorização irrestrita para outras. Não duplique despacho já existente: consulte antes a árvore do processo, inclusive eventuais minutas do mesmo assunto.
5. Reabra/consulte o documento criado e verifique número SEI gerado, assunto, conteúdo integral, referências, parágrafos e situação (minuta/não assinado). Se a criação funcionar mas a inserção do texto falhar, relate o documento criado e a pendência, em vez de declarar finalização.
6. **Não assine, não envie o processo, não conclua os autos e não exclua documentos automaticamente.** Essas ações exigem pedido e autorização específicos, separados da autorização para criar a minuta. Se o usuário solicitar assinatura, o fluxo de senha/cargo deve ocorrer exclusivamente no cartão próprio do SEI-Pro, jamais na conversa.
7. Na resposta final, informe: processo, documento SEI criado (quando houver), situação da assinatura, ID do cadastro no Arrendamento, instrumento registrado e pendências. Se houver impedimento, forneça a minuta completa e diga precisamente qual operação não foi possível executar.

### 8.4 Consistência obrigatória entre cadastro e despacho

Antes da gravação no SEI, confronte: número do processo; números SEI de encaminhamento e instrumento; nome e número do contrato ou apostilamento; contratada; porto; área e prazo; natureza e extensão da alteração; situação real no Arrendamento; ausência ou existência de anexos. A informação documental é a fonte para descrever o instrumento; a consulta posterior ao Arrendamento é a fonte para declarar **o que efetivamente foi cadastrado**. Discrepâncias materiais devem ser saneadas antes da criação do despacho; se impedirem afirmação segura do cadastro, informe o bloqueio e não crie documento inexato. Não é necessária prévia textual do despacho no chat.

## Erros

- "[sessao] ... janela de login": peça ao usuário para concluir o login da Microsoft na janela do Chrome que abriu e repita a mesma chamada.
- "[validacao]": o dado foi recusado antes de enviar; corrija conforme a mensagem.
- "[validacao] ... fora das pastas permitidas" ou "extensão não aceita" ao anexar: o arquivo não veio de documento_baixar ou não é documento; baixe de novo com documento_baixar e use o caminho devolvido.
- "[acesso]" ou "[permissao]": o usuário não tem acesso ou perfil no sistema; informe e pare.
- "não está rodando neste computador": o servidor do conector Arrendamento está desligado; peça ao usuário para iniciá-lo e repita a chamada.
- "não tem autorização para acessar o endereço": peça ao usuário para abrir a configuração do agente, em Conectores, e clicar em "Testar conexão" no conector Arrendamento.
