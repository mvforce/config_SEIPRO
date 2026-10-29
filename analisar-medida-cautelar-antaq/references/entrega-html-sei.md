# HTML para colagem no SEI

## Uso e compatibilidade

O gerador formata texto técnico previamente elaborado e conferido. Não produz análise jurídica nem decide a cautelar. Requer Python 3.10+ e apenas biblioteca padrão. Para extrair ou converter imagem de PDF, o auxiliar requer PyMuPDF.

```text
python scripts/gerar_html_sei.py --dados caminho/dados.json --saida caminho/outputs
```

São gerados HTML completo, fragmento com corpo idêntico e cada figura PNG separada. Por padrão, o nome-base é `nota_tecnica_cautelar`. Abrir o arquivo completo em navegador, selecionar o conteúdo renderizado, copiar e colar no editor visual do SEI. Não colar o código literal nesse modo. Se o editor oferecer modo fonte, pode-se usar o fragmento.

Não há scripts, botões ou instruções de uso no corpo institucional. Os estilos essenciais estão inline; o HTML não depende de fonte remota, CSS externo ou rede. Numeração visível não depende de contador CSS. Tabelas têm bordas, cabeçalhos e células reais. Parágrafos e itens admitem números explícitos.

As imagens são incorporadas em base64 e também entregues separadamente. A colagem pode ser filtrada pelo editor. Se a imagem desaparecer, inserir o PNG pela ferramenta de imagem na posição da legenda. Não declarar compatibilidade com determinada versão do SEI sem teste real. A inspeção em navegador comprova somente a renderização local.

## Dados de entrada

Todos os textos são escapados. Não inserir HTML nos campos. Citações literais podem preservar pontuação original no bloco `citacao`, com fonte obrigatória; textos novos não admitem travessão longo. Não usar dados fictícios em análise real. O arquivo `assets/exemplo_sintetico.json` demonstra a estrutura sem representar processo existente.

Para conferir o formato sem autos, executar o comando acima com `--dados assets/exemplo_sintetico.json`, a partir da pasta da skill, ou ajustar os caminhos à pasta atual. O exemplo inclui duas tabelas e uma figura didática. Não usar seu texto como manifestação sobre caso concreto.

```json
{
  "titulo": "Nota Técnica - Minuta",
  "processo": "número comprovado nos autos",
  "assunto": "Objeto específico da análise",
  "arquivo_base": "nota_tecnica_cautelar",
  "blocos": [
    {"tipo":"secao","numero":"1","titulo":"DA INTRODUÇÃO E CONTEXTUALIZAÇÃO"},
    {"tipo":"paragrafo","numero":"1.1","texto":"Texto fundamentado nos documentos lidos."},
    {"tipo":"subsecao","numero":"2.1","titulo":"Quanto ao perigo na demora"},
    {"tipo":"tabela","titulo":"Quadro 1 - Pedidos","cabecalhos":["Pedido","Evidência","Conclusão"],"linhas":[["Objeto documental","Fonte e localização","Resultado fundamentado"]]},
    {"tipo":"figura","arquivo":"figura_documental.png","legenda":"Figura 1 - Identificação da infraestrutura.","fonte":"Fonte: documento, SEI, página e autoria."},
    {"tipo":"item","texto":"I - Providência específica, destinatário e limites."},
    {"tipo":"fecho","texto":"É o entendimento."}
  ]
}
```

Blocos disponíveis: `secao`, `subsecao`, `paragrafo`, `item`, `fecho`, `citacao`, `tabela` e `figura`. A citação exige `texto` e `fonte`. Tabela exige `titulo`, cabeçalhos e linhas de igual comprimento; `fonte` é opcional, mas a rastreabilidade documental deve estar na tabela ou no texto. Células devem ser strings não vazias, inclusive números e ausências explicadas. Quebra de linha textual vira `<br>`. O campo `numero` é opcional nos parágrafos e itens; a numeração de seções é explícita.

O caminho da figura é relativo ao JSON, salvo caminho absoluto. Aceita PNG; converter JPEG ou extrair recorte em PNG. Não incluir figura nem tabela sem função na análise: ambos os blocos são opcionais. O gerador mantém proporção da figura e evita ampliar imagens pequenas. Não usar imagem diminuta de página que fique ilegível na entrega; renderizar novamente em resolução adequada.

O nome-base admite letras ASCII, números, hífen e sublinhado. Saída existente não é sobrescrita sem `--sobrescrever`. Marcadores de preenchimento são rejeitados; isso não detecta toda lacuna factual, que depende de revisão humana/técnica. O gerador verifica estrutura PNG e CRCs; a abertura efetiva e a inspeção visual continuam necessárias.

## Imagem documental

Preferir extrair a figura original ou renderizar o recorte pertinente. Não recompor planta com geometria inventada, deslocar limites, omitir legenda relevante ou apresentar como fato confirmado interpretação da parte. Remover somente áreas exteriores ao conteúdo útil, sem alterar seu significado. Preservar escala e orientação quando relevantes.

```text
python scripts/extrair_figura_pdf.py --pdf documento.pdf --listar
python scripts/extrair_figura_pdf.py --pdf documento.pdf --pagina 2 --recorte 40 400 560 720 --dpi 180 --saida figura_documental.png
```

As coordenadas do exemplo são apenas sintaxe: escolher recorte após ver a página do caso. O script salva origem, página, hash, resolução e recorte em arquivo auxiliar `.origem.json`. Registrar SEI e autoria na legenda, pois o auxiliar não os adivinha. Se o documento não contiver imagem pertinente, entregar a análise sem figura. Um gráfico analítico novo deve identificar sua elaboração e os dados de origem.

Não reproduzir assinatura, QR Code, código de autenticação ou cabeçalho de documento anterior como se pertencessem à minuta nova. Em tabela extraída de PDF, conferir alinhamento de colunas, unidades, datas e notas; extração linear não garante correspondência correta.

## Verificação final

Executar o gerador e abrir o resultado em navegador ou renderizador. Examinar início, tabelas, todas as figuras e conclusão, sem cortes, texto sobreposto ou legenda ilegível. Testar largura de leitura e verificar acentos. Conferir dados e raciocínio separadamente. A geração bem-sucedida não comprova suficiência jurídica, assinatura ou inserção no SEI.

Se faltarem elementos essenciais, a minuta deve indicar o encaminhamento possível e o chat deve identificar a limitação. Não preencher lacunas com informações dos exemplos nem anunciar como pronta para uso uma minuta que ainda depende de prova determinante.
