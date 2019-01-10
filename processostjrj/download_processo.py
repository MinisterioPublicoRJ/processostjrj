import requests
import json
from bs4 import BeautifulSoup
from .utils import formata_numero_processo, cria_hash_do_processo
from .parser import (
    parse_metadados,
    area_dos_metadados,
    parse_itens,
    prepara_soup,
    cria_url_movimentos
)
from logging import Logger

URL_PROCESSO_TJRJ = (
    'http://www4.tjrj.jus.br/numeracaoUnica/faces/index.jsp?'
    'numProcesso={doc_number}'
)
_LOGGER = Logger('processostjrj.processo')


def processo(processo, headers=None, timeout=10):
    """Efetua o download e parsing de um processo TJRJ a partir
    do seu número. """

    _LOGGER.info(processo)
    dados_processo = {}
    numero_processo = formata_numero_processo(processo)
    try:
        resp = requests.post(
            URL_PROCESSO_TJRJ.format(doc_number=numero_processo),
            headers=headers,
            timeout=10,
            allow_redirects=True
        )
        soup = prepara_soup(BeautifulSoup(resp.content, 'lxml'))
        link_movimentos = cria_url_movimentos(soup, resp.url)
        resp = requests.get(link_movimentos)
        soup = prepara_soup(BeautifulSoup(resp.content, 'lxml'))
        linhas = soup.find_all('tr')
        inicio, fim = area_dos_metadados(linhas)
        dados_processo.update(
            parse_metadados(
                linhas,
                numero_processo,
                inicio,
                fim))
        dados_processo['hash'] = cria_hash_do_processo(
            json.dumps(dados_processo))
        dados_processo.update(parse_itens(soup, processo, inicio + 1))
    except Exception as erro:
        _LOGGER.error(
            "Erro de parsing do processo - {0}, com mensagem: {1}".format(
                numero_processo,
                erro))
        raise erro
    return dados_processo
