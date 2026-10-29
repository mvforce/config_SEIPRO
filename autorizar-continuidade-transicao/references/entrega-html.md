# HTML para o SEI e relatório final

## Arquivos de entrega

Produzir `nota_tecnica.html`, `nota_tecnica_fragmento_sei.html` e `figura_1.png`. O HTML completo é aberto no navegador para copiar o conteúdo renderizado; o fragmento contém apenas o corpo, útil quando houver acesso ao modo fonte do editor. Não colar código literal no modo visual.

Usar UTF-8, fonte Calibri/Arial 12 pt, texto justificado, espaçamento moderado, títulos institucionais e tabelas simples com bordas. Parágrafos, tabelas, células e figura têm estilos essenciais inline. Não depender de CSS externo, JavaScript, fontes remotas, flex/grid ou contadores CSS para informação indispensável. Numeração de seções explícita.

A figura deve ser extraída do documento correto. Preferir PNG com resolução legível, sem alterar limites ou criar delimitação inventada. Identificar figura, SEI, anexo e página. Não reproduzir assinaturas, CRC ou QR Code no corpo da nova Nota.

O gerador incorpora PNG em base64 para o arquivo ser autocontido e entrega PNG separado. O SEI pode remover a imagem em colagem; nesse caso inserir o PNG pela ferramenta de imagem na posição da legenda. Não afirmar compatibilidade testada no SEI se houve apenas inspeção local do navegador.

## Gerador

Requer Python 3.10+ e apenas biblioteca padrão. Recebe JSON com cabeçalho e blocos já redigidos. Não faz análise jurídica nem inventa texto:

```text
python scripts/gerar_html_sei.py --dados caminho/dados.json --saida caminho/outputs
```

Estrutura dos dados:

```json
{
  "titulo": "Nota Técnica - Minuta",
  "processo": "número documental",
  "assunto": "objeto completo",
  "arquivo_base": "nota_tecnica",
  "blocos": [
    {"tipo":"secao","numero":"1","titulo":"DA INTRODUÇÃO"},
    {"tipo":"paragrafo","texto":"Texto já redigido e fundamentado."},
    {"tipo":"subsecao","numero":"3.1","titulo":"Quanto ao enquadramento do pleito"},
    {"tipo":"tabela","titulo":"Quadro 1 - Evolução contratual","cabecalhos":["Instrumento","Data","Conteúdo"],"linhas":[["instrumento comprovado","data comprovada","fato comprovado"]]},
    {"tipo":"figura","arquivo":"figura.png","legenda":"Figura 1 - identificação","fonte":"Fonte documental, SEI, página"},
    {"tipo":"fecho","texto":"É o entendimento."}
  ]
}
```

Caminho de figura relativo ao JSON. O script escapa o texto, valida linhas das tabelas e exige pelo menos tabela e figura PNG. Não suporta HTML arbitrário nos campos. Redigir os dados a partir do processo; não preencher ausências com fatos do exemplo. O arquivo `assets/exemplo_sintetico.json` demonstra a estrutura com fatos, área e valores inteiramente fictícios e não é modelo de mérito universal.

O arquivo-base só admite letras ASCII, números, hífen e sublinhado. O script não sobrescreve arquivo existente por padrão; usar `--sobrescrever` somente para regenerar a própria entrega. O validador incorporado verifica estrutura, referências locais de imagem, tokens pendentes, travessão longo e recursos ativos/externos.

## Conferência e inspeção

Executar o gerador e conferir se o fragmento é idêntico ao corpo completo. Abrir ou renderizar o HTML localmente; examinar início, tabelas, figura, conclusão, bordas e ausência de cortes. Conferir texto e cálculos separadamente. Renderização local não comprova assinatura nem inserção no SEI.

Se o caso tiver impedimento material, entregar minuta com diligência e encaminhamento corretos, sem declarar aprovação integral. Campos essenciais realmente ausentes devem ser identificados no chat; não chamar minuta com marcadores não resolvidos de pronta para uso.

## Relatório no próprio chat

Após os links, apresentar uma tabela com:

| Documento/localização | Problema relevante ou limitação | Repercussão | Providência e momento |
| --- | --- | --- | --- |
| Referência concreta | Fato específico, sem presumir descumprimento | Impeditivo, condição de assinatura, acompanhamento ou limitação de conferência | Ação delimitada, responsável e quando necessária |

Não transferir toda a fundamentação para a tabela. Não tratar ponto superado como impedimento. Se houver questão material omitida do documento, corrigir a Nota antes de entregar. Quando não houver pendência relevante, registrar em linha única que não foi identificada e apontar apenas o encaminhamento cabível.

Quando houver comunicação autorizativa anterior, delimitar seu alcance, verificar condições de formalização e não exigir nova decisão genérica sobre matéria já apreciada. Registrar limites dos documentos efetivamente disponibilizados.
