import requests
import json
from bs4 import BeautifulSoup
from .utils import formata_numero_processo, cria_hash_do_processo
from .parser import (
    parse_metadados,
    area_dos_metadados,
    parse_itens,
    prepara_soup,
    cria_url_movimentos,
    extrai_personagens,
    extrai_historico_personagens
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
        form = soup.find('form', {'id': 'form'})
        if form:
            table = soup.find('table')
            links = table.find_all('a')
            new_url = links[0]['href'].strip()
            new_resp = requests.post(
                new_url,
                headers=headers,
                timeout=10,
                allow_redirects=True
            )
            soup = prepara_soup(BeautifulSoup(new_resp.content, 'lxml'))
            link_movimentos = cria_url_movimentos(soup, new_resp.url)
        else:
            link_movimentos = cria_url_movimentos(soup, resp.url)

        resp = requests.get(link_movimentos, headers=headers)
        soup = prepara_soup(BeautifulSoup(resp.content, 'lxml'))

        soup_personagens = soup.find('div', {'id': 'listaPersonagens'})
        soup_historico = soup.find(
            'div',
            {'id': 'listaHistoricoPersonagens'}
        )

        if soup_personagens is not None:
            soup.find('a', {'href': 'javascript:exibeListaPersonagens();'}).decompose()
            dados_processo['lista-personagens'] = extrai_personagens(
                soup_personagens
            )

        if soup_historico is not None:
            soup.find('a', {'href': 'javascript:exibeListaHistoricoPersonagens();'}).decompose()
            extrai_historico_personagens(soup_historico)

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
