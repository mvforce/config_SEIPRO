"""Lista imagens ou renderiza recorte documental de página PDF em PNG.

Requer PyMuPDF: python -m pip install pymupdf. Coordenadas em pontos PDF.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def extract(pdf, page_number, output, crop=None, dpi=180, overwrite=False):
    import pymupdf
    pdf, output = Path(pdf).resolve(), Path(output).resolve()
    if output.suffix.lower() != '.png':
        raise ValueError('A saída deve ter extensão .png')
    if not 72 <= dpi <= 600:
        raise ValueError('Usar resolução entre 72 e 600 dpi')
    metadata_path = output.with_suffix('.origem.json')
    if not overwrite and (output.exists() or metadata_path.exists()):
        raise FileExistsError('Saída existente; conferir destino ou usar --sobrescrever')
    with pymupdf.open(pdf) as doc:
        if not 1 <= page_number <= len(doc):
            raise ValueError('Página fora dos limites do PDF')
        page = doc[page_number-1]
        rect = page.rect
        clip = pymupdf.Rect(crop) if crop is not None else rect
        if clip.is_empty or clip.is_infinite or not rect.contains(clip):
            raise ValueError('Recorte inválido ou fora da página')
        pix = page.get_pixmap(dpi=dpi, clip=clip, alpha=False)
        picture = pix.tobytes('png')
        metadata = {'arquivo_fonte': pdf.name, 'sha256_pdf': hashlib.sha256(pdf.read_bytes()).hexdigest(),
                    'pagina_pdf': page_number, 'paginas_pdf': len(doc),
                    'recorte_pontos_pdf': list(clip), 'dpi': dpi,
                    'largura_px': pix.width, 'altura_px': pix.height,
                    'observacao': 'Reprodução documental; conferir legenda, autoria e contexto na fonte.'}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(picture)
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return {'figura': str(output), 'origem': str(metadata_path), **metadata}


def inventory(pdf):
    import pymupdf
    with pymupdf.open(pdf) as doc:
        result = []
        for i, page in enumerate(doc):
            images = []
            for img in page.get_images(full=True):
                images.append({'xref': img[0], 'largura_px': img[2], 'altura_px': img[3],
                               'retangulos': [list(rect) for rect in page.get_image_rects(img[0])]})
            result.append({'pagina': i+1, 'limites_pontos_pdf': list(page.rect), 'imagens': images})
        return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdf', type=Path, required=True)
    parser.add_argument('--listar', action='store_true')
    parser.add_argument('--pagina', type=int)
    parser.add_argument('--recorte', nargs=4, type=float, metavar=('X0', 'Y0', 'X1', 'Y1'))
    parser.add_argument('--dpi', type=int, default=180)
    parser.add_argument('--saida', type=Path)
    parser.add_argument('--sobrescrever', action='store_true')
    args = parser.parse_args()
    if args.listar:
        result = inventory(args.pdf)
    else:
        if args.pagina is None or args.saida is None:
            parser.error('Informar --pagina e --saida, ou usar --listar')
        result = extract(args.pdf, args.pagina, args.saida, args.recorte, args.dpi, args.sobrescrever)
    print(json.dumps(result, ensure_ascii=False, indent=2))
