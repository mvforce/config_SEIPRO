"""Conferência aritmética; não valida IPCA, fundamentação jurídica ou proporcionalidade."""
import argparse
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
import json
from pathlib import Path

def dec(v):
    if isinstance(v,float): raise ValueError('Usar moeda em texto decimal, não ponto flutuante')
    return Decimal(str(v))

def cash(v): return str(v.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

def check(data):
    result={'natureza':'Conferência aritmética, sem validação jurídica ou do índice de reajuste'}
    if 'protocolo' in data and 'termino' in data:
        days=(date.fromisoformat(data['termino'])-date.fromisoformat(data['protocolo'])).days
        result['antecedencia_dias']=days
        result['antecedencia_minima_60_dias']=days>=60
    if 'mensal' in data:
        monthly=dec(data['mensal'])
        if monthly<0: raise ValueError('Remuneração mensal negativa')
        if 'mensalidades' in data:
            n=dec(data['mensalidades'])
            if n<=0: raise ValueError('Mensalidades devem ser positivas')
            total=(monthly*n).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
            result['global_calculado']=cash(total)
            if 'global_informado' in data:
                result['global_confere']=total==dec(data['global_informado'])
        if 'multiplicador_garantia' in data:
            factor=dec(data['multiplicador_garantia'])
            if factor<0: raise ValueError('Multiplicador de garantia negativo')
            guarantee=(monthly*factor).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
            result['garantia_calculada']=cash(guarantee)
            if 'garantia_informada' in data:
                result['garantia_confere']=guarantee==dec(data['garantia_informada'])
        if 'mensal_anterior' in data:
            previous=dec(data['mensal_anterior'])
            if previous<=0: raise ValueError('Base mensal anterior deve ser positiva')
            result['variacao_mensal_implicita_percentual']=str(((monthly/previous-1)*100).quantize(Decimal('.0001')))
    if 'mme' in data:
        result['razoes_mme']={}
        for load,pair in data['mme'].items():
            before,after=map(dec,pair)
            if before<=0 or after<0: raise ValueError('MME anterior deve ser positiva; nova não pode ser negativa')
            result['razoes_mme'][load]=str(after/before)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--dados',type=Path,required=True)
    a=p.parse_args()
    print(json.dumps(check(json.loads(a.dados.read_text(encoding='utf-8-sig'))),ensure_ascii=False,indent=2))
