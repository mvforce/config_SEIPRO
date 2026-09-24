---
name: autorizacao-contrato-transicao
description: Analisa pedido de autorização para celebrar contrato de transição em porto organizado e produz matriz de requisitos, ressalvas e proposta de manifestação GPO/SOG.
---

# Autorização de contrato de transição

## Quando ativar
Quando a autoridade portuária solicita à ANTAQ autorização para celebrar contrato de transição ou apresenta minuta antes da celebração. Para contrato já celebrado após autorização, usar a skill de primeiro contrato de transição.

## Relação com o contexto fixo
Aplicar estilo e contexto de Tavares recebidos no prompt da API. Este procedimento decorre de `analise_autorização_transição.pdf`, que contém campos em branco, alternativas mutuamente excludentes e exemplo do Porto do Recife. Não tratar esses trechos como fatos ou texto aprovado para qualquer outro processo. Conferir redação vigente da Resolução ANTAQ nº 127/2025, eventuais regras transitórias e o momento dos atos; o modelo contém referências que podem refletir versões anteriores.

## Instrução
1. Delimitar área, metragem, localização, atividade e cargas, empresa pretendida, situação atual de ocupação, histórico contratual, PDZ vigente, urgência alegada, processo licitatório planejado e decisões já proferidas. Fazer inventário dos documentos e respectivos números SEI, inclusive solicitação, justificativa, declarações, seleção/chamamento, planta georreferenciada, minuta e plano de licitação.
2. Verificar a compatibilidade concreta com o PDZ e com a destinação da área. Confirmar se a atividade proposta é operacional e se existem condicionantes do planejamento e interferências concorrenciais; não presumir regularidade pela simples menção ao PDZ.
3. Identificar e conferir o regime normativo aplicável à data do pleito. A matriz do exemplo usa arts. 37, §1º, 38 e 39 da Resolução 127/2025; confirmar dispositivo, texto atual e hipóteses de incidência antes de atribuir exigência. A referência do modelo à emergência e à dispensa de licitação deve ser confrontada com os pareceres e legislação pertinentes, distinguindo posição jurídica documentada de conclusão própria.
4. Verificar motivação da transitoriedade: continuidade após extinção de vínculo anterior ou seleção simplificada, quando exigível; adimplência; capacidade técnica; relevante interesse público; danos concretos da ociosidade ou interrupção; plano e estágio da licitação definitiva. Relacionar alegações a dados objetivos e localizar lacunas.
5. Montar matriz com `requisito | base normativa conferida | documento/SEI e trecho | situação | efeito/providência`. Usar `comprovado`, `não comprovado`, `inaplicável justificado` ou `leitura pendente`. Conferir anúncio e critérios da seleção, se cabíveis, e análise concorrencial quando relevante.
6. Conferir minuta e anexos: identificação das partes, objeto, área, planta, bens e arrolamento, cargas, termo inicial e final, relação com a licitação, desocupação, preço e reajuste, metas quando previstas, investimentos e eventual indenização, obrigações operacionais, segurança, fiscalização, seguros, extinção e devolução. Os 40 itens do modelo são roteiro de triagem, não cláusulas automaticamente obrigatórias; validar cada um no texto normativo e no caso. Ressalvar contradições entre minuta, anexos e autorização pretendida.
7. Diferenciar falha sanável antes de assinar, falta essencial à autorização e matéria que exige diligência. Se a prova de interesse público ou fundamento da transição faltar, evitar conclusão positiva condicionada a correções genéricas.

## Saída
Redigir introdução/contextualização, justificativa normativa, análise de requisitos, observações e conclusão com proposta precisa à instância competente. Em cada ressalva, indicar peça, cláusula ou item, correção e momento em que deve ser cumprida. Concluir por autorização fundamentada, diligência ou não atendimento, segundo a prova. Usar o estilo do contexto fixo; não copiar empresa, área, valores, itens marcados ou alternativas do exemplo. Sem acesso integral ao documento, indicar `não verificado nos autos disponibilizados`, sem afirmar inexistência.

## Fluxo interativo obrigatório com o usuário
1. Ao ser acionada, identificar o processo já aberto e examinar os documentos acessíveis com as funções de leitura e consulta do agente do SEI-Pro. Se não houver processo identificável, perguntar apenas qual processo deve ser analisado. Solicitar outras informações apenas quando indispensáveis, em perguntas curtas; não exigir que o usuário reapresente peças que o agente consegue ler.
2. Concluída a análise, apresentar na conversa uma prévia substantiva: fatos confirmados e documentos SEI, matriz de achados relevantes, limites de leitura, proposta de conclusão e minuta completa do despacho ou nota técnica sobre o pedido de autorização do contrato de transição. A minuta deve estar visível antes de qualquer proposta de criação no SEI.
3. Ao final dessa prévia, formular uma pergunta confirmatória explícita, destacando fundamento e necessidade da transição, requisitos demonstrados, pendências da minuta, conclusão quanto à autorização e condições ou diligências. Exemplo: **"Você confirma o conteúdo e a conclusão da minuta ou deseja corrigir algum ponto?"** Aguardar resposta. Se houver correções, incorporá-las, mostrar a versão integral revisada e repetir a confirmação do conteúdo. Não interpretar silêncio como confirmação.
4. Somente depois da confirmação expressa da versão final, perguntar separadamente: **"Deseja que eu crie este documento no processo pelo SEI-Pro?"** Aguardar resposta. Uma confirmação do conteúdo, isoladamente, não autoriza a criação. Se o usuário negar ou apenas desejar o texto, encerrar com a versão aprovada na conversa.
5. Se houver resposta afirmativa à criação, utilizar as funções efetivamente disponíveis no agente SEI-Pro para criar documento no processo correto e inserir o texto final confirmado, selecionando o tipo documental adequado. Antes de chamar a função de escrita, conferir processo, tipo, título quando aplicável e texto. Não inventar nome de ferramenta nem afirmar criação quando houver apenas minuta. Respeitar o cartão de aprovação exibido pelo aplicativo; o usuário deve aprovar a operação ali. Não assinar, tramitar, dar ciência nem alterar outros dados sem pedido próprio.
6. Após a execução aprovada no aplicativo, confirmar o resultado pelas funções de leitura e informar número/identificador SEI se retornado. Se a função falhar, não declarar documento criado; explicar o erro e manter a minuta disponível.

## Controle final
Checar compatibilidade PDZ, motivo concreto da transição, seleção quando aplicável, situação licitatória definitiva, minuta e anexos, adequação concorrencial e competência decisória. Não apresentar a minuta como contrato assinado nem registrar ato administrativo como praticado por mera recomendação da skill.

