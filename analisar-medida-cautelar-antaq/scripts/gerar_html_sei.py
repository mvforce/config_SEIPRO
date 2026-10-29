"""Gera Nota Técnica HTML autocontida e fragmento idêntico para colagem no SEI.

Python 3.10+, biblioteca padrão. Não redige nem decide a matéria.
"""
from __future__ import annotations

import argparse
import base64
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import struct
import zlib

FONT = 'font-family:Calibri,Arial,sans-serif;font-size:12pt;color:#000;'
PAR = FONT + 'text-align:justify;line-height:1.35;margin:0 0 10pt 0;'
CELL = FONT + 'font-size:10.5pt;border:1px solid #777;padding:7px;vertical-align:top;text-align:left;overflow-wrap:anywhere;'
PNG = b'\x89PNG\r\n\x1a\n'
PENDING = re.compile(r'\{\{.*?\}\}|\[(?:TODO|PREENCHER|INSERIR|A CONFIRMAR)\b[^\]]*\]', re.I)


def value(record, key, original=False):
    result = record.get(key)
    if not isinstance(result, str) or not result.strip():
        raise ValueError(f'Campo textual obrigatório: {key}')
    result = result.strip()
    if PENDING.search(result):
        raise ValueError(f'Marcador pendente em {key}')
    if '\u2014' in result and not original:
        raise ValueError(f'Travessão longo em texto novo: {key}')
    return result


def esc(text):
    return html.escape(text, quote=True).replace('\n', '<br>')


def number(text):
    if not re.fullmatch(r'\d+(?:\.\d+)*', text):
        raise ValueError(f'Numeração inválida: {text}')
    return text


def png_dimensions(data):
    """Verifica estrutura e CRCs de PNG e obtém suas dimensões."""
    if not data.startswith(PNG):
        raise ValueError('Figura deve ser PNG; converter JPEG ao extrair/renderizar')
    offset, dimensions, has_pixels = 8, None, False
    while offset + 12 <= len(data):
        length = struct.unpack('>I', data[offset:offset+4])[0]
        end = offset + 12 + length
        if end > len(data):
            raise ValueError('PNG truncado')
        kind = data[offset+4:offset+8]
        payload = data[offset+8:offset+8+length]
        crc = struct.unpack('>I', data[end-4:end])[0]
        if zlib.crc32(kind + payload) & 0xffffffff != crc:
            raise ValueError('CRC inválido na figura PNG')
        if offset == 8:
            if kind != b'IHDR' or length != 13:
                raise ValueError('Cabeçalho PNG inválido')
            dimensions = struct.unpack('>II', payload[:8])
            if not all(dimensions):
                raise ValueError('Dimensões PNG inválidas')
        if kind == b'IDAT':
            has_pixels = True
        if kind == b'IEND':
            if length or end != len(data) or not has_pixels:
                raise ValueError('Final de PNG inválido')
            return dimensions
        offset = end
    raise ValueError('Figura PNG sem encerramento')


class Validator(HTMLParser):
    """Valida a estrutura produzida, sem executar ou aceitar HTML do usuário."""
    allowed = {'div', 'p', 'strong', 'em', 'br', 'table', 'thead', 'tbody', 'tr', 'th', 'td', 'img'}
    void = {'br', 'img'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.tables = self.images = 0

    def handle_starttag(self, tag, attrs):
        if tag not in self.allowed:
            raise ValueError(f'Tag não permitida: {tag}')
        attrs = dict(attrs)
        if any(k.startswith('on') for k in attrs):
            raise ValueError('Atributo ativo no HTML')
        if tag == 'img':
            src = attrs.get('src', '')
            if not src.startswith('data:image/png;base64,'):
                raise ValueError('Figura não incorporada')
            png_dimensions(base64.b64decode(src.split(',', 1)[1], validate=True))
            self.images += 1
        if tag == 'table':
            self.tables += 1
        if tag not in self.void:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag not in self.allowed or tag in self.void or not self.stack or self.stack.pop() != tag:
            raise ValueError(f'Fechamento HTML inválido: {tag}')

    def finish(self):
        self.close()
        if self.stack:
            raise ValueError('HTML com tags abertas')


def generate(data_path: Path, output: Path, overwrite=False):
    data_path, output = Path(data_path).resolve(), Path(output).resolve()
    data = json.loads(data_path.read_text(encoding='utf-8-sig'))
    if not isinstance(data, dict):
        raise ValueError('Os dados devem ser um objeto JSON')
    title, subject = value(data, 'titulo'), value(data, 'assunto')
    process = value(data, 'processo')
    stem = data.get('arquivo_base', 'nota_tecnica_cautelar')
    if not isinstance(stem, str) or not re.fullmatch(r'[A-Za-z0-9_-]+', stem):
        raise ValueError('Nome-base inválido')
    blocks = data.get('blocos')
    if not isinstance(blocks, list) or not blocks:
        raise ValueError('Lista de blocos obrigatória')
    body = [f'<div style="{FONT}">',
            f'<p style="{FONT}text-align:center;margin:0 0 6pt 0;"><strong>Agência Nacional de Transportes Aquaviários</strong></p>',
            f'<p style="{FONT}text-align:center;margin:0 0 18pt 0;"><strong>{esc(title)}</strong></p>',
            f'<p style="{PAR}"><strong>Processo:</strong> {esc(process)}</p>',
            f'<p style="{PAR}"><strong>Assunto:</strong> {esc(subject)}</p>']
    figures = []
    for block in blocks:
        if not isinstance(block, dict):
            raise ValueError('Bloco inválido')
        kind = block.get('tipo')
        if kind in ('secao', 'subsecao'):
            heading = esc(number(value(block, 'numero')) + '. ' + value(block, 'titulo'))
            if kind == 'subsecao':
                heading = '<em>' + heading + '</em>'
            body.append(f'<p style="{FONT}text-align:left;margin:18pt 0 10pt 0;page-break-after:avoid;"><strong>{heading}</strong></p>')
        elif kind in ('paragrafo', 'item', 'fecho'):
            text = value(block, 'texto')
            if block.get('numero') is not None:
                text = number(value(block, 'numero')) + '. ' + text
            style = PAR
            if kind == 'item':
                style += 'margin-left:24pt;'
            elif kind == 'fecho':
                style = FONT + 'text-align:center;margin:20pt 0;'
            body.append(f'<p style="{style}">{esc(text)}</p>')
        elif kind == 'citacao':
            text = value(block, 'texto', original=True)
            source = value(block, 'fonte')
            body.append(f'<p style="{PAR}font-size:11pt;margin-left:36pt;">{esc(text)}</p>')
            body.append(f'<p style="{FONT}font-size:10pt;text-align:right;">{esc(source)}</p>')
        elif kind == 'tabela':
            headers, rows = block.get('cabecalhos'), block.get('linhas')
            if not isinstance(headers, list) or not headers or not isinstance(rows, list) or not rows:
                raise ValueError('Tabela sem cabeçalhos ou linhas')
            if any(not isinstance(row, list) or len(row) != len(headers) for row in rows):
                raise ValueError('Tabela com número de células inconsistente')
            all_cells = headers + [cell for row in rows for cell in row]
            for cell in all_cells:
                value({'celula': cell}, 'celula')
            caption = value(block, 'titulo')
            body.append(f'<p style="{FONT}font-size:11pt;text-align:center;margin:14pt 0 6pt 0;"><strong>{esc(caption)}</strong></p>')
            body.append('<table border="1" cellspacing="0" cellpadding="7" width="100%" style="width:100%;border-collapse:collapse;table-layout:fixed;margin:0 0 14pt 0;">')
            body.append('<thead><tr>' + ''.join(f'<th scope="col" style="{CELL}background-color:#ededed;font-weight:bold;">{esc(x)}</th>' for x in headers) + '</tr></thead><tbody>')
            for row in rows:
                body.append('<tr>' + ''.join(f'<td style="{CELL}">{esc(x)}</td>' for x in row) + '</tr>')
            body.append('</tbody></table>')
            if block.get('fonte') is not None:
                body.append(f'<p style="{FONT}font-size:10pt;text-align:left;">{esc(value(block, "fonte"))}</p>')
        elif kind == 'figura':
            path = (data_path.parent / value(block, 'arquivo')).resolve()
            picture = path.read_bytes()
            width, height = png_dimensions(picture)
            caption, source = value(block, 'legenda'), value(block, 'fonte')
            name = f'{stem}_figura_{len(figures)+1}.png'
            figures.append((name, picture))
            encoded = base64.b64encode(picture).decode('ascii')
            display_width = min(width, 850)
            display_height = round(height * display_width / width)
            body.append(f'<p style="{FONT}text-align:center;margin:14pt 0 5pt 0;"><img alt="{esc(caption)}" src="data:image/png;base64,{encoded}" width="{display_width}" height="{display_height}" style="max-width:100%;height:auto;border:0;"></p>')
            body.append(f'<p style="{FONT}font-size:10pt;text-align:center;margin:0 0 4pt 0;">{esc(caption)}</p>')
            body.append(f'<p style="{FONT}font-size:10pt;text-align:center;margin:0 0 14pt 0;">{esc(source)}</p>')
        else:
            raise ValueError(f'Tipo de bloco desconhecido: {kind}')
    body.append('</div>')
    fragment = '\n'.join(body) + '\n'
    checker = Validator()
    checker.feed(fragment)
    checker.finish()
    template_path = Path(__file__).resolve().parents[1] / 'assets/nota_tecnica_base.html'
    template = template_path.read_text(encoding='utf-8')
    if template.count('{{CORPO}}') != 1 or template.count('{{TITULO}}') != 1:
        raise ValueError('Template inválido')
    rendered = template.replace('{{TITULO}}', html.escape(title, quote=True)).replace('{{CORPO}}', fragment)
    if rendered.split('<body>\n', 1)[1].split('</body>', 1)[0] != fragment:
        raise ValueError('Corpo completo e fragmento divergentes')
    targets = {output / f'{stem}.html': rendered.encode('utf-8'),
               output / f'{stem}_fragmento_sei.html': fragment.encode('utf-8')}
    targets.update({output / name: picture for name, picture in figures})
    if not overwrite and any(path.exists() for path in targets):
        raise FileExistsError('Saída existente; usar --sobrescrever apenas para regenerar a própria entrega')
    if any(path.exists() and not path.is_file() for path in targets):
        raise ValueError('Destino de saída não é arquivo')
    output.mkdir(parents=True, exist_ok=True)
    for path, content in targets.items():
        path.write_bytes(content)
    return {'html': str(output / f'{stem}.html'),
            'fragmento': str(output / f'{stem}_fragmento_sei.html'),
            'figuras': [str(output / name) for name, _ in figures],
            'tabelas': checker.tables, 'blocos': len(blocks), 'corpos_identicos': True}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dados', type=Path, required=True)
    parser.add_argument('--saida', type=Path, required=True)
    parser.add_argument('--sobrescrever', action='store_true')
    args = parser.parse_args()
    print(json.dumps(generate(args.dados, args.saida, args.sobrescrever), ensure_ascii=False, indent=2))
