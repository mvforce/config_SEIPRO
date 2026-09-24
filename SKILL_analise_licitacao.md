---
name: analise-licitacao-portuaria
description: Analisa documentos preparatórios e EVTEA de licitação de arrendamento portuário, ordinária ou simplificada, com matriz de evidências e minuta de manifestação GPO/SOG.
---

# Análise de licitação portuária

## Quando ativar
Quando o pedido envolver preparatórios de licitação de área de porto organizado, EVTEA, aderência à Resolução ANTAQ nº 85/2022, exame de premissas regulatórias ou minuta de despacho/nota técnica da GPO/SOG. Não usar para autorização de contrato de transição nem para conferência de seu primeiro instrumento celebrado.

## Relação com o contexto fixo
Aplicar o contexto de Tavares já fornecido pela aplicação. Este arquivo acrescenta o procedimento específico do modelo `modelo_analise_licitação.pdf`; não reproduzir fatos de RDJ07 nem presumir que conclusões e normas do exemplo valham para outro processo. Prevalecem a solicitação concreta, os documentos atuais e as decisões vinculantes do caso.

## Sequência de trabalho
1. Identificar número do processo, área, porto, objeto, cargas, proponente, órgão que aprovou o estudo, decisão de aprovação, fase processual e demanda feita à ANTAQ. Citar documento e página/trecho quando disponíveis.
2. Consultar a árvore e ler o ato justificatório, despacho decisório, versões atuais do EVTEA, anexos, delimitação da área e peças de encaminhamento. Se houver PDF digitalizado ou leitura incompleta, procurar as páginas relevantes por outras ferramentas e declarar expressamente a limitação; ausência de trecho extraído não prova ausência no documento.
3. Determinar, pela decisão e normas aplicáveis, se a licitação é ordinária ou simplificada. A lista de seções e requisitos muda conforme a modalidade; não marcar as duas como simultaneamente aplicáveis.
4. Elaborar matriz documental: documento exigido, versão e identificador SEI, localização, situação (comprovado, não comprovado, inaplicável fundamentado, leitura pendente), observação. Para ordinária, examinar A apresentação, B mercado, C engenharia, D operacional, E financeiro, F ambiental e anexos pertinentes; para simplificada, identificar as seções efetivamente exigidas pela disciplina vigente, sem impor a estrutura ordinária.
5. Elaborar matriz de análise do estudo, item normativo, evidência localizada, confronto crítico e providência. No modelo, TV1 corresponde à disciplina da Resolução 85/2022 e TV2 a determinações/recomendações pertinentes do TCU. Verificar teor, destinatário e aplicabilidade de cada acórdão ao caso atual antes de cobrar atendimento. Nunca preencher automaticamente `SIM` por existir uma seção do EVTEA.
6. Conferir coerência entre demanda, capacidade, engenharia, investimentos, cronograma, operação, receitas, custos, pagamentos, MMC/MME e demais obrigações contratuais. Confrontar PDZ, planejamento setorial, concorrência, interferências portuárias e comunidades afetadas quando pertinentes e com suporte documental. Quantificar divergências e explicitar sua consequência para a modelagem.
7. Separar o que foi efetivamente verificado do que cabe ao Poder Concedente decidir. A aprovação prévia do EVTEA não impede apontar inconsistências relevantes à competência regulatória da ANTAQ; tampouco autoriza substituir a decisão do Poder Concedente. Propor diligência objetiva quando uma premissa essencial não estiver demonstrada.
8. Concluir de modo único: atendimento; atendimento parcial com ajustes identificados e avaliação expressa de eventual óbice; ou insuficiência que exige complementação antes do prosseguimento. Relacionar cada ressalva ao identificador da matriz, evidência e providência. Não copiar as três conclusões alternativas do exemplo.

## Saída
Se pedido um texto, redigir `INTRODUÇÃO`, `ANÁLISE` e `CONCLUSÃO/ENCAMINHAMENTO` no estilo do contexto fixo, com parágrafos numerados quando apropriado, tabela concisa e referências SEI. Se pedido um diagnóstico, apresentar matriz e pontos decisórios antes da minuta. Distinguir constatação, alegação da parte e inferência técnica. Não inventar número SEI, ato, percentuais ou fundamento legal. Quando o documento ou norma não estiver acessível, escrever `não verificado nos autos disponibilizados` e especificar a peça necessária.

## Fluxo interativo obrigatório com o usuário
1. Ao ser acionada, identificar o processo já aberto e examinar os documentos acessíveis com as funções de leitura e consulta do agente do SEI-Pro. Se não houver processo identificável, perguntar apenas qual processo deve ser analisado. Solicitar outras informações apenas quando indispensáveis, em perguntas curtas; não exigir que o usuário reapresente peças que o agente consegue ler.
2. Concluída a análise, apresentar na conversa uma prévia substantiva: fatos confirmados e documentos SEI, matriz de achados relevantes, limites de leitura, proposta de conclusão e minuta completa do despacho ou nota técnica de análise dos preparatórios da licitação. A minuta deve estar visível antes de qualquer proposta de criação no SEI.
3. Ao final dessa prévia, formular uma pergunta confirmatória explícita, destacando modalidade licitatória, itens atendidos ou pendentes, ressalvas à modelagem, conclusão sobre prosseguimento e encaminhamento. Exemplo: **"Você confirma o conteúdo e a conclusão da minuta ou deseja corrigir algum ponto?"** Aguardar resposta. Se houver correções, incorporá-las, mostrar a versão integral revisada e repetir a confirmação do conteúdo. Não interpretar silêncio como confirmação.
4. Somente depois da confirmação expressa da versão final, perguntar separadamente: **"Deseja que eu crie este documento no processo pelo SEI-Pro?"** Aguardar resposta. Uma confirmação do conteúdo, isoladamente, não autoriza a criação. Se o usuário negar ou apenas desejar o texto, encerrar com a versão aprovada na conversa.
5. Se houver resposta afirmativa à criação, utilizar as funções efetivamente disponíveis no agente SEI-Pro para criar documento no processo correto e inserir o texto final confirmado, selecionando o tipo documental adequado. Antes de chamar a função de escrita, conferir processo, tipo, título quando aplicável e texto. Não inventar nome de ferramenta nem afirmar criação quando houver apenas minuta. Respeitar o cartão de aprovação exibido pelo aplicativo; o usuário deve aprovar a operação ali. Não assinar, tramitar, dar ciência nem alterar outros dados sem pedido próprio.
6. Após a execução aprovada no aplicativo, confirmar o resultado pelas funções de leitura e informar número/identificador SEI se retornado. Se a função falhar, não declarar documento criado; explicar o erro e manter a minuta disponível.

## Controle final
Confirmar se a modalidade foi identificada; se cada conclusão tem suporte em peça e localização; se decisões atuais e alterações do estudo foram consideradas; se há exame regulatório além da mera presença formal quando o objeto assim exige; se citações normativas e determinações do TCU foram conferidas no texto aplicável; e se a proposta é compatível com a fase processual.

