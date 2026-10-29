"""Renderiza texto técnico já elaborado em HTML completo e fragmento para o SEI."""
from __future__ import annotations
import argparse
import base64
import html
import json
from pathlib import Path
import re
import shutil
from html.parser import HTMLParser

FONT = 'font-family:Calibri,Arial,sans-serif;font-size:12pt;color:#000;'
PAR = FONT + 'text-align:justify;line-height:1.35;margin:0 0 10pt 0;'
CELL = FONT + 'font-size:10.5pt;border:1px solid #777;padding:7px;vertical-align:top;text-align:left;overflow-wrap:anywhere;'

def esc(value):
    return html.escape(str(value), quote=True)

def text_value(record, key):
    value = record.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'Campo textual obrigatório: {key}')
    return value.strip()

class Validator(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tables = self.images = 0
        self.texts = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('script','iframe','object','embed','link','svg','canvas'):
            raise ValueError(f'Recurso incompatível: {tag}')
        if any(k.lower().startswith('on') for k in attrs):
            raise ValueError('Atributo de execução de código')
        if tag == 'img':
            self.images += 1
            src = attrs.get('src','')
            if not src.startswith('data:image/png;base64,'):
                raise ValueError('Imagem deve estar incorporada como PNG')
            data = base64.b64decode(src.split(',',1)[1], validate=True)
            if not data.startswith(b'\x89PNG\r\n\x1a\n'):
                raise ValueError('Imagem PNG inválida')
        if tag == 'table': self.tables += 1
        if tag in ('table','thead','tbody','tr','th','td','p','div','strong','em'):
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in ('table','thead','tbody','tr','th','td','p','div','strong','em'):
            if not self.stack or self.stack.pop() != tag:
                raise ValueError(f'Estrutura HTML incorreta no fechamento: {tag}')

    def handle_data(self, data): self.texts.append(data)

    def finish(self):
        if self.stack: raise ValueError('Tags não fechadas')
        if self.tables < 1 or self.images < 1:
            raise ValueError('Entrega exige tabela e figura')
        text = '\n'.join(self.texts)
        if '\u2014' in text: raise ValueError('Travessão longo na redação')
        if re.search(r'\{\{[^}]+\}\}|\[TODO[^\]]*\]|\[PREENCHER[^\]]*\]', text, re.I):
            raise ValueError('Marcador de preenchimento não resolvido')

def generate(data_path: Path, output: Path, overwrite=False):
    data_path = data_path.resolve()
    data = json.loads(data_path.read_text(encoding='utf-8-sig'))
    title = text_value(data,'titulo')
    process = text_value(data,'processo')
    subject = text_value(data,'assunto')
    stem = data.get('arquivo_base','nota_tecnica')
    if not re.fullmatch(r'[A-Za-z0-9_-]+',stem):
        raise ValueError('Nome-base de arquivo inválido')
    blocks = data.get('blocos')
    if not isinstance(blocks,list) or not blocks:
        raise ValueError('Lista de blocos ausente')
    body = [
        f'<div style="{FONT}">',
        f'<p style="{FONT}text-align:center;margin:0 0 6pt 0;"><strong>Agência Nacional de Transportes Aquaviários</strong></p>',
        f'<p style="{FONT}text-align:center;margin:0 0 18pt 0;"><strong>{esc(title)}</strong></p>',
        f'<p style="{PAR}"><strong>Processo nº:</strong> {esc(process)}</p>',
        f'<p style="{PAR}"><strong>Assunto:</strong> {esc(subject)}</p>',
    ]
    image_outputs = []
    for b in blocks:
        kind = b.get('tipo')
        if kind in ('secao','subsecao'):
            number, heading = text_value(b,'numero'), text_value(b,'titulo')
            if not re.fullmatch(r'\d+(?:\.\d+)*',number):
                raise ValueError('Numeração de seção inválida')
            content = f'{esc(number)}. {esc(heading)}'
            if kind == 'subsecao': content = '<em>'+content+'</em>'
            body.append(f'<p style="{FONT}text-align:left;margin:18pt 0 10pt 0;page-break-after:avoid;"><strong>{content}</strong></p>')
        elif kind in ('paragrafo','item','fecho'):
            value = esc(text_value(b,'texto'))
            style = PAR
            if kind == 'item': style += 'margin-left:24pt;'
            if kind == 'fecho': style = FONT+'text-align:center;margin:20pt 0;'
            body.append(f'<p style="{style}">{value}</p>')
        elif kind == 'tabela':
            headers,rows = b.get('cabecalhos'),b.get('linhas')
            if not headers or not isinstance(headers,list) or not isinstance(rows,list) or not rows:
                raise ValueError('Tabela sem cabeçalhos ou linhas')
            if any(not isinstance(row,list) or len(row)!=len(headers) for row in rows):
                raise ValueError('Número de células inconsistente')
            if b.get('titulo'):
                body.append(f'<p style="{FONT}text-align:center;font-size:11pt;margin:14pt 0 6pt 0;"><strong>{esc(b["titulo"])}</strong></p>')
            body.append('<table border="1" cellspacing="0" cellpadding="7" width="100%" style="width:100%;border-collapse:collapse;table-layout:fixed;margin:0 0 14pt 0;">')
            body.append('<thead><tr>'+''.join(f'<th scope="col" style="{CELL}background-color:#e8e8e8;font-weight:bold;">{esc(x)}</th>' for x in headers)+'</tr></thead><tbody>')
            for row in rows:
                body.append('<tr>'+''.join(f'<td style="{CELL}">{esc(x)}</td>' for x in row)+'</tr>')
            body.append('</tbody></table>')
        elif kind == 'figura':
            source = (data_path.parent/text_value(b,'arquivo')).resolve()
            image_bytes = source.read_bytes()
            if not image_bytes.startswith(b'\x89PNG\r\n\x1a\n'):
                raise ValueError('Figura deve ser PNG válido')
            image_name = f'figura_{len(image_outputs)+1}.png'
            image_outputs.append((source,image_name))
            encoded = base64.b64encode(image_bytes).decode('ascii')
            caption = text_value(b,'legenda')
            body.append(f'<p style="{FONT}text-align:center;margin:14pt 0 5pt 0;"><img alt="{esc(caption)}" src="data:image/png;base64,{encoded}" width="850" style="max-width:100%;width:100%;height:auto;border:0;"></p>')
            body.append(f'<p style="{FONT}font-size:10pt;text-align:center;margin:0 0 4pt 0;">{esc(caption)}</p>')
            body.append(f'<p style="{FONT}font-size:10pt;text-align:center;margin:0 0 14pt 0;">{esc(text_value(b,"fonte"))}</p>')
        else:
            raise ValueError(f'Tipo de bloco desconhecido: {kind}')
    body.append('</div>')
    fragment = '\n'.join(body)+'\n'
    validator = Validator()
    validator.feed(fragment)
    validator.finish()
    template = (Path(__file__).resolve().parents[1]/'assets'/'nota_tecnica_base.html').read_text(encoding='utf-8')
    rendered = template.replace('{{TITULO}}',esc(title)).replace('{{CORPO}}',fragment)
    if '{{' in rendered: raise ValueError('Token não resolvido no template')
    output = output.resolve()
    targets = [output/f'{stem}.html',output/f'{stem}_fragmento_sei.html']
    image_targets = [output/name for _,name in image_outputs]
    if not overwrite and any(p.exists() for p in targets+image_targets):
        raise FileExistsError('Saída já existe; para regenerar sua entrega, use --sobrescrever')
    output.mkdir(parents=True,exist_ok=True)
    for source,name in image_outputs:
        dest=output/name
        if source!=dest: shutil.copyfile(source,dest)
    targets[0].write_text(rendered,encoding='utf-8')
    targets[1].write_text(fragment,encoding='utf-8')
    return {'html':str(targets[0]),'fragmento':str(targets[1]),'figuras':[str(x) for x in image_targets],'tabelas':validator.tables,'blocos':len(blocks)}

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--dados',type=Path,required=True)
    p.add_argument('--saida',type=Path,required=True)
    p.add_argument('--sobrescrever',action='store_true')
    a=p.parse_args()
    print(json.dumps(generate(a.dados,a.saida,a.sobrescrever),ensure_ascii=False,indent=2))
