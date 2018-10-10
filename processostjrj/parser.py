import re
import collections
from slugify import slugify
from .utils import limpa_conteudo, cria_hash_do_movimento


PADRAO_MOV = re.compile(r'numMov=(\d+)')


def parse_metadados(linhas_de_dados, numero_processo, inicio_metadados,
                    fim_metadados):
    metadados = {
        'status': [''],
        'comarca': [''],
        'endereco': [''],
        'bairro': [''],
        'cidade': [''],
        'acao': [''],
        'assunto': [''],
        'classe': [''],
        'livro': [''],
        'folha': [''],
        'numero-do-tombo': [''],
        'aviso-ao-advogado': [''],
        'autor': [''],
        'requerido': [''],
        'requerente': [''],
        'advogado-s': ['']
    }

    # Delimita o processo na regiao dos metadados
    linhas_com_metadados = linhas_de_dados[inicio_metadados:fim_metadados]

    metadados['numero-processo'] = numero_processo
    metadados['status'] = limpa_conteudo(
        linhas_com_metadados[0].find_all('td')[0].get_text()
    )

    # Apaga linhas utilizadas
    del linhas_com_metadados[:2]

    comarcas = []
    comecou_comarca = False
    for tr in list(linhas_com_metadados):
        linhas_com_metadados.pop(0)
        colunas = tr.find_all('td')
        dados = ''.join([c.get_text() for c in colunas])
        if 'Comarca' in dados or \
           'Regional' in dados:
            comecou_comarca = True

        if comecou_comarca:
            comarcas += extrai_dados_colunas(colunas)

        if len(colunas) == 1 and comecou_comarca:
            break

    metadados['comarca'] = comarcas

    for tr in list(linhas_com_metadados):
        linhas_com_metadados.pop(0)
        linha = []
        colunas = tr.find_all('td')
        linha = extrai_dados_colunas(colunas)
        if linha:
            metadados[slugify(linha[0])] = linha[1:]

    return metadados


def estripa(texto):
    return ' '.join(limpa_conteudo(texto).split("\n")).strip()


def atribui(chave, item, valor):
    valor = estripa(valor)
    if valor:
        item[chave].append(valor)


def parse_processo_apensado(cols, item, campo):
    dados = cols[1].find_all('a')
    if dados:
        item[campo] = [estripa(link.get_text()) for link in dados]


def parse_descricao(cols, item, campo):
    for link in cols[1].find_all('a'):
        if 'onclick' in link.attrs:
            conteudo_escondido = link.attrs['onclick']
            inteiro_teor = PADRAO_MOV.findall(
                conteudo_escondido)
            if inteiro_teor:
                item['inteiro-teor'] = inteiro_teor

    atribui(campo, item, next(cols[1].descendants))


METODOS_PARSING = {
    'processo-s-apensado-s': parse_processo_apensado,
    'processo-s-no-tribunal-de-justica': parse_processo_apensado,
    'descricao': parse_descricao,
}


def parse_itens(soup, numero_processo, inicio_itens):
    # Recorta area com os itens
    itens = {}
    itens['numero-processo'] = numero_processo
    lista_de_itens = []
    linhas_de_dados = soup.find_all(attrs={'name': 'formResultado'})[0]\
        .find_all('tr')
    linhas_com_itens = linhas_de_dados[inicio_itens:]

    for indice, linha in enumerate(list(linhas_com_itens)):
        if linha.attrs == {'class': ['tipoMovimento']}:
            item = collections.defaultdict(list)
            colunas = linha.find_all('td')
            # Podem existir cabeçalhos de itens sem texto, como o
            # Mandado de Pagamento
            # Nesses caso registraremos como tipo de movimento o
            # título do bloco
            if len(colunas) == 1:
                texto = colunas[0].get_text().strip()
                chave = 'tipo-do-movimento'
            else:
                texto = limpa_conteudo(
                    colunas[1].get_text()
                )
                chave = slugify(colunas[0].get_text())

            item[chave] = texto

            info = linhas_com_itens[indice + 1:]
            cont = 0
            while cont < len(info) and\
                    info[cont].attrs != {'class': ['tipoMovimento']}:

                cols = info[cont].find_all('td')
                if len(cols) > 1:
                    campo = slugify(cols[0].get_text())
                    if campo == 'tipo-do-movimento':
                        campo = 'sub-tipo-do-movimento'
                    if campo in METODOS_PARSING:
                        METODOS_PARSING[campo](cols, item, campo)
                    else:
                        atribui(campo, item, cols[1].get_text())
                else:
                    cont += 1
                    continue

                cont += 1

            lista_de_itens.append(item)

    for item in lista_de_itens:
        if 'inteiro-teor' in item:
            item['inteiro-teor'] = soup.find(
                'input', {
                    'type': 'HIDDEN',
                    'name': 'descMov{0}'.format(item['inteiro-teor'][0])
                }).attrs['value']

    for item in lista_de_itens:
        item['hash'] = cria_hash_do_movimento(item)

    itens['itens'] = lista_de_itens
    return itens


def area_dos_metadados(linhas_de_dados):
    # Aparentemente esse valor e fixo
    inicio = 0
    atributos_inicio_metadados = {'align': 'center',
                                  'class': ['negrito'],
                                  'colspan': '2'}
    for indice, linha in enumerate(linhas_de_dados):
        coluna = linha.find('td')
        if not inicio and coluna.attrs == atributos_inicio_metadados:
            inicio = indice

        if 'Tipo do Movimento:' in linha.get_text():
            fim = indice - 1
            break

    return inicio, fim


def extrai_dados_colunas(colunas):
    linha = []
    for td in colunas:
        linha += list(
            filter(None, [limpa_conteudo(td.get_text()) if td else ''])
        )

    return linha
