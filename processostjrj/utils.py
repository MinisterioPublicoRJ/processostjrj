import hashlib
import json
import re

from hashlib import md5


def formata_numero_processo(numero_processo):
    mascara = "{0}-{1}.{2}.{3}.{4}.{5}"

    primeira_parte = slice(0, 7)
    segunda_parte = slice(7, 9)
    terceira_parte = slice(9, 13)
    quarta_parte = slice(13, 14)
    quinta_parte = slice(14, 16)
    sexta_parte = slice(16, 20)

    return mascara.format(
        numero_processo[primeira_parte],
        numero_processo[segunda_parte],
        numero_processo[terceira_parte],
        numero_processo[quarta_parte],
        numero_processo[quinta_parte],
        numero_processo[sexta_parte]
    )


def limpa_conteudo(conteudo_sujo):
    return re.sub(r'\s+', ' ', conteudo_sujo).strip()


def remove_data_consulta(html):
    html = html.decode('latin-1')
    return re.sub(
        r'TJ/RJ -\r\n                      '
        r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}',
        '',
        html).encode()


def cria_hash_do_processo(html):
    return md5(html.encode()).hexdigest()


def cria_hash_do_movimento(item):
    chaves = sorted(item.keys())
    valores = [item[chave] for chave in chaves]
    itens_ordenados = list(zip(chaves, valores))
    item_json = json.dumps(itens_ordenados)
    return hashlib.md5(item_json.encode()).hexdigest()
