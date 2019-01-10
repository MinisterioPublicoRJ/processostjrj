from unittest import TestCase
from unittest.mock import patch

from bs4 import BeautifulSoup

from processostjrj.parser import (parse_metadados,
                                  area_dos_metadados,
                                  extrai_dados_colunas,
                                  parse_itens,
                                  parse_processo_apensado,
                                  prepara_soup,
                                  extrai_link_movimentos,
                                  extrai_url_base,
                                  cria_url_movimentos,
                                  extrai_links_instancias)
from .fixtures.paginas import desambiguacao
from .fixtures.processos import (processo_judicial_1,
                                 processo_judicial_2,
                                 processo_judicial_3,
                                 processo_judicial_4,
                                 processo_judicial_5,
                                 processo_judicial_6,
                                 processo_judicial_7,
                                 trecho_processo_judicial_1,
                                 process_com_mandado_pagamento,
                                 processo_sem_movimentos)


def _prepara_html(html, tag='tr'):
    soup_obj = BeautifulSoup(html, 'lxml')
    return soup_obj.find_all(tag)


class ParserMetadados(TestCase):
    def test_parse_processos_no_tribunal(self):
        esperado = {
            'processo-s-no-tribunal-de-justica': [
                '0021913-53.2011.8.19.0000',
                '0000159-51.2010.8.19.0045'
            ]
        }

        item = {}
        parse_processo_apensado(
            _prepara_html(trecho_processo_judicial_1, 'td'),
            item,
            'processo-s-no-tribunal-de-justica')
        assert item == esperado

    def test_parse_metadados_processo_judicial(self):
        metadados = parse_metadados(
            _prepara_html(processo_judicial_1),
            '0004999-58.2015.8.19.0036',
            inicio_metadados=6,
            fim_metadados=26
        )

        esperado = {
            'numero-processo': '0004999-58.2015.8.19.0036',
            'status': 'PROCESSO COM BAIXA',
            'comarca': [
                'Comarca de Nilópolis',
                '2ª Vara de Família e da Infância e da Juventude e do Idoso',
                'Cartório da 2ª Vara de Família, Inf. e da Juv. e do Idoso'],
            'endereco': ['Getúlio Vargas 571 - 6º andar'],
            'bairro': ['Olinda'],
            'aviso-ao-advogado': [''],
            'cidade': ['Nilópolis'],
            'acao': [('Medidas Pertinentes Aos Pais Ou '
                     'Responsável / Seção Cível')],
            'assunto': [('Medidas Pertinentes Aos Pais Ou Responsável'
                         ' / Seção Cível')],
            'classe': [('Perda ou Suspensão ou Restabelecimento do Poder '
                        'Familiar')],
            'autor': ['MINISTÉRIO PÚBLICO DO ESTADO DO RIO DE JANEIRO'],
            'requerido': ['DANIELLE MARIA GOMES BARBOSA'],
            'requerente': [''],
            'advogado-s': ['TJ000002 - DEFENSOR PÚBLICO']}

        for chave, valor in esperado.items():
            with self.subTest():
                self.assertEqual(metadados[chave], valor)

    def test_parse_metadados_de_outro_processo_com_outras_informacoes(self):
        metadados = parse_metadados(
            _prepara_html(processo_judicial_2),
            '0025375-16.2012.8.19.0054',
            inicio_metadados=6,
            fim_metadados=27
        )

        esperado = {
            'numero-processo': '0025375-16.2012.8.19.0054',
            'status': 'ARQUIVADO EM DEFINITIVO - MAÇO Nº 722, em 20/05/2013',
            'comarca': [
                'Comarca de São João de Meriti',
                'Juizado da Infância e Juventude e do Idoso',
                'Cartório do Juizado da Infância e Juventude e do Idoso'],
            'endereco': ['Av. Presidente Lincoln 857'],
            'bairro': ['Vilar dos Teles'],
            'cidade': ['São João de Meriti'],
            'acao': ['Entrada e Permanência de Menores / Seção Cível'],
            'assunto': ['Entrada e Permanência de Menores / Seção Cível'],
            'classe': ['Autorização judicial - ECA'],
            'aviso-ao-advogado': ['tem peça na pasta.'],
            'autor': [''],
            'livro': [''],
            'folha': [''],
            'numero-do-tombo': [''],
            'requerido': [''],
            'requerente': ['IGREJA EVANGÉLICA NOVA ASSEMBLÉIA DE DEUS'],
            'advogado-s': ['RJ081634 - IRANY SPERANDIO DE MEDEIROS']}

        for chave, valor in esperado.items():
            with self.subTest():
                self.assertEqual(metadados[chave], valor)

    def test_parsea_processo_com_informacoes_de_comarca_diferentes(self):
        metadados = parse_metadados(
            _prepara_html(processo_judicial_3),
            '0001762-56.2009.8.19.0026',
            inicio_metadados=7,
            fim_metadados=23
        )

        esperado = {
            'numero-processo': '0001762-56.2009.8.19.0026',
            'status': 'ARQUIVADO EM DEFINITIVO - MAÇO Nº 1903, em 22/11/2012',
            'comarca': [
                'Comarca de Itaperuna',
                'Vara de Família e da Infância e da Juventude e do Idoso',
                'Cartório da Vara de Família, Inf. e da Juv. e do Idoso'],
            'endereco': ['Rodovia Br-356 Km 01'],
            'bairro': [''],
            'cidade': ['Itaperuna'],
            'acao': ['Adoção de Criança / Seção Cível'],
            'assunto': ['Adoção de Criança / Seção Cível'],
            'classe': ['Adoção c/c Destituição do Poder Familiar - ECA'],
            'aviso-ao-advogado': [''],
            'autor': [''],
            'requerido': [''],
            'requerente': [''],
            'advogado-s': ['RJ146889 - VIRGINIA MARIA RAMOS DA FONSECA']}

        for chave, valor in esperado.items():
            with self.subTest():
                self.assertEqual(metadados[chave], valor)

    def test_parsea_processo_com_link_nos_metadados(self):
        metadados = parse_metadados(
            _prepara_html(processo_judicial_4),
            '0441870-74.2008.8.19.0001',
            inicio_metadados=7,
            fim_metadados=27
        )

        esperado = {
            'numero-processo': '0441870-74.2008.8.19.0001',
            'status': 'ARQUIVADO EM DEFINITIVO - MAÇO Nº 9819, em 24/02/2013',
            'comarca': [
                'Comarca da Capital',
                '1ª Vara da Infância da Juventude e do Idoso',
                'Cartório da 1ª Vara da Infância, da Juventude e do Idoso'],
            'endereco': ['Praça Onze de Junho 403 Praça Onze'],
            'bairro': ['Centro'],
            'cidade': ['Rio de Janeiro'],
            'acao': [''],
            'assunto': ['Adoção Nacional / Seção Cível'],
            'classe': ['Adoção c/c Destituição do Poder Familiar - ECA'],
            'aviso-ao-advogado': [''],
            'autor': [''],
            'requerido': ['MARIA GISLEUDA RODRIGUES DA SILVA'],
            'requerente': ['FRANCISCO CAMILO RIBEIRO e outro(s)...'],
            'advogado-s': ['TJ000002 - DEFENSOR PÚBLICO']}

        for chave, valor in esperado.items():
            with self.subTest():
                self.assertEqual(metadados[chave], valor)

    def test_parsea_processo_com_link_antes_dos_metadados(self):
        metadados = parse_metadados(
            _prepara_html(processo_judicial_5),
            '0001394-96.2011.8.19.0084',
            inicio_metadados=0,
            fim_metadados=23
        )

        esperado = {
            'numero-processo': '0001394-96.2011.8.19.0084',
            'status': '',
            'comarca': [
                'Comarca de Carapebus / Quissamã',
                'Vara Única',
                'Cartório da Vara Única'],
            'endereco': ['Estrada do Correio Imperial 1003'],
            'bairro': ['Piteiras'],
            'cidade': ['Quissamã'],
            'acao': ['Medidas Pertinentes Aos Pais Ou Responsável /'
                     ' Seção Cível'],
            'assunto': ['Medidas Pertinentes Aos Pais Ou Responsável /'
                        ' Seção Cível'],
            'classe': ['Apuração de Infração Administrativa às Normas de'
                       ' Proteção'],
            'aviso-ao-advogado': [''],
            'autor': [''],
            'requerido': [''],
            'requerente': [''],
            'advogado-s': ['RJ125011 - ALBECIR RIBEIRO RJ143662 -'
                           ' PAULO ROMERO AQUINO BARBOSA']}

        for chave, valor in esperado.items():
            with self.subTest():
                self.assertEqual(metadados[chave], valor)

    def test_parsea_processo_com_nome_regional_ao_inves_de_comarca(self):
        metadados = parse_metadados(
            _prepara_html(processo_judicial_6),
            '0021491-54.2011.8.19.0202',
            inicio_metadados=6,
            fim_metadados=21
        )

        esperado = {
            'numero-processo': '0021491-54.2011.8.19.0202',
            'status': 'ARQUIVADO EM DEFINITIVO - MAÇO Nº 442, em 27/02/2012',
            'comarca': [
                'Regional de Madureira',
                '3ª Vara da Infância, da Juventude e do Idoso',
                'Cartório da 3ª Vara da Infância, da Juventude e do Idoso'],
            'endereco': ['Avenida Ernani Cardoso 152 2º andar'],
            'bairro': ['Cascadura'],
            'cidade': ['Rio de Janeiro'],
            'acao': ['Acolhimento Institucional de Crianças e'
                     ' Adolescentes/seção Cível'],
            'assunto': ['Acolhimento Institucional de Crianças e'
                        ' Adolescentes/seção Cível'],
            'classe': ['Providência - ECA'],
            'aviso-ao-advogado': [''],
            'autor': [''],
            'requerido': [''],
            'requerente': [''],
            'advogado-s': ['']}

        for chave, valor in esperado.items():
            with self.subTest():
                self.assertEqual(metadados[chave], valor)

    def test_delimita_linhas_dos_metadados_processo_judicial_1(self):
        inicio, fim = area_dos_metadados(
            _prepara_html(processo_judicial_1)
        )

        inicio_esperado = 6
        fim_esperado = 26

        self.assertEqual(inicio, inicio_esperado)
        self.assertEqual(fim, fim_esperado)

    def test_delimita_linhas_dos_metadados_processo_judicial_3(self):
        """
            O Processo judicial numero 3, diferente dos outros 2 presentes
            nas fixtures, inicia os metadados em uma linha diferente.
        """
        inicio, fim = area_dos_metadados(
            _prepara_html(processo_judicial_3)
        )

        inicio_esperado = 7
        fim_esperado = 23

        self.assertEqual(inicio, inicio_esperado)
        self.assertEqual(fim, fim_esperado)

    def test_extrai_dados_das_colunas(self):
        html = """
                <tr>
                 <td class="negrito" nowrap="" valign="top">Tipo:</td>
                 <td align="justify" class="normal" valign="top">Conclusão</td>
                 </tr>
                """
        soup = _prepara_html(html)[0].find_all('td')
        dados_das_colunas = extrai_dados_colunas(soup)
        esperado = ['Tipo:', 'Conclusão']

        self.assertEqual(dados_das_colunas, esperado)

    def test_extrai_metadados_processos_sem_movimentos(self):
        linhas = _prepara_html(processo_sem_movimentos)
        inicio, fim = area_dos_metadados(linhas)

        self.assertEqual(inicio, 6)
        self.assertEqual(fim, 35)

    def test_prepara_soup(self):
        soup = BeautifulSoup(processo_sem_movimentos, 'lxml')
        soup_limpo = prepara_soup(soup)

        elementos_indesejados = soup_limpo.find(
            'div', {'id': 'wndHistoricoMandados'}
        )

        self.assertIsNone(elementos_indesejados)

    def test_prepara_soup_sem_elementos_indesejados(self):
        soup = BeautifulSoup(processo_judicial_1, 'lxml')
        soup_limpo = prepara_soup(soup)

        elementos_indesejados = soup_limpo.find(
            'div', {'id': 'wndHistoricoMandados'}
        )

        self.assertIsNone(elementos_indesejados)

    def test_encontra_link_para_movimentos(self):
        html = '''<a href="javascript:location.href='consultaMov.do?v=2&'''\
               '''numProcesso=2013.029.112186-8&acessoIP='''\
               '''intranet&tipoUsuario='"> <img height="17" width="26"'''\
               '''class="margin-icos" src="http://www.tjrj.jus.br/imagens/'''\
               '''ico-nova-busca.gif" title="Listar Todos Movimentos"'''\
               '''alt="Listar Todos Movimentos"/> </a>'''
        soup = BeautifulSoup(html, 'lxml')
        link_mov = extrai_link_movimentos(soup)
        self.assertEqual(
            link_mov,
            'consultaMov.do?v=2&numProcesso=2013.029.112186-8&acessoIP='
            'intranet&tipoUsuario='
        )

    def test_extrai_base_url(self):
        url = 'http://www4.tjrj.jus.br/consultaProcessoWebV2/'\
              'consultaProc.do?v=2&FLAGNOME=&back=1&tipoConsulta='\
              'publica&numProcesso=2013.029.112186-8'
        url_base = extrai_url_base(url)

        self.assertEqual(
            url_base,
            'http://www4.tjrj.jus.br/consultaProcessoWebV2'
        )

    def test_cria_url_para_movimentos(self):
        html = '''<a href="javascript:location.href='consultaMov.do?v=2&'''\
               '''numProcesso=2013.029.112186-8&acessoIP='''\
               '''intranet&tipoUsuario='"> <img height="17" width="26"'''\
               '''class="margin-icos" src="http://www.tjrj.jus.br/imagens/'''\
               '''ico-nova-busca.gif" title="Listar Todos Movimentos"'''\
               '''alt="Listar Todos Movimentos"/> </a>'''
        url = 'http://www4.tjrj.jus.br/consultaProcessoWebV2/'\
              'consultaProc.do?v=2&FLAGNOME=&back=1&tipoConsulta='\
              'publica&numProcesso=2013.029.112186-8'
        soup = BeautifulSoup(html, 'lxml')
        url_movimentos = cria_url_movimentos(soup, url)

        self.assertEqual(
            url_movimentos,
            'http://www4.tjrj.jus.br/consultaProcessoWebV2/consultaMov.do?'
            'v=2&numProcesso=2013.029.112186-8&acessoIP=intranet&tipoUsuario='
        )

    def test_descobre_link_para_instancias(self):
        soup = BeautifulSoup(desambiguacao, 'lxml')
        links = extrai_links_instancias(soup)
        esperado = [
            'http://www4.tjrj.jus.br/consultaProcessoWebV2/consultaProc.do?'
            'v=2&FLAGNOME=&back=1&tipoConsulta=publica&numProcesso='
            '2015.900.018832-7',
            'http://www4.tjrj.jus.br/ejud/ConsultaProcesso.aspx?N=201805100327'
        ]

        self.assertEqual(links, esperado)


class ComparaItensProcessoMixin:
    def assert_items_equal(self, first, second):
        self.assertEqual(first['numero-processo'], second['numero-processo'])
        items_first = first['itens']
        items_second = second['itens']

        self.assertEqual(len(items_first), len(items_second))

        for item_first, item_second in zip(items_first, items_second):
            for key, value in item_second.items():
                with self.subTest():
                    self.assertEqual(item_first[key], value)


class ParserItems(ComparaItensProcessoMixin, TestCase):
    @patch('processostjrj.parser.cria_hash_do_movimento',
           return_value='1234')
    def test_extrai_itens_do_processo_judicial_1(self, _chdm):
        soup = BeautifulSoup(processo_judicial_1, 'lxml')
        itens = parse_itens(
            soup,
            '0004999-58.2015.8.19.0036',
            inicio_itens=26
        )
        esperado = {
            'numero-processo': '0004999-58.2015.8.19.0036',
            'itens': [{
                'tipo-do-movimento': 'Declínio de Competência',
                'hash': '1234',
                'data': ['11/01/2016'],
                'descricao':
                ['VIJI DA COMARCA DE SÃO MATHEUS - ESPIRITO SANTOS']
            }, {
                'tipo-do-movimento': 'Recebimento',
                'data-de-recebimento': ['19/11/2015']
            }, {
                'tipo-do-movimento': 'Decisão - Declínio de Competência',
                'hash': '1234',
                'data-decisao':
                ['21/10/2015'],
                'descricao': ['Ante o teor de fls. 104, DECLINO DE MINHA'
                              ' COMPETÊNCIA para o Juízo da Infância e'
                              ' Juventude da Comarca de São Mateus, no'
                              ' Espírito Santo. Dê-se baixa e encaminhem-se'
                              ' imediatamente, com as nossas homenagens.']
            }, {
                'tipo-do-movimento': 'Conclusão ao Juiz',
                'hash': '1234',
                'data-da-conclusao': ['21/10/2015'],
                'juiz': ['VIVIANE TOVAR DE MATTOS ABRAHAO']
            }, {
                'tipo-do-movimento': 'Decurso de Prazo',
                'hash': '1234',
                'data-do-movimento': ['20/10/2015']
            }, {
                'tipo-do-movimento': 'Recebidos os autos',
                'hash': '1234',
                'data-do-recebimento': ['20/10/2015']
            }, {
                'tipo-do-movimento': 'Remessa',
                'hash': '1234',
                'destinatario': ['Ministério Público'],
                'data-da-remessa': ['06/08/2015'],
                'prazo': ['15 dia(s)']
            }, {
                'tipo-do-movimento': 'Recebimento',
                'hash': '1234',
                'data-de-recebimento': ['30/07/2015']
            }, {
                'tipo-do-movimento':
                'Despacho - Proferido despacho de mero expediente',
                'hash': '1234',
                'data-despacho':
                ['28/07/2015'],
                'descricao':
                ['Dê-se vista ao Ministério Público.']
            }, {
                'tipo-do-movimento': 'Conclusão ao Juiz',
                'hash': '1234',
                'data-da-conclusao': ['28/07/2015'],
                'juiz': ['VIVIANE TOVAR DE MATTOS ABRAHAO']
            }, {
                'tipo-do-movimento': 'Decurso de Prazo',
                'hash': '1234',
                'data-do-movimento': ['27/07/2015']
            }, {
                'tipo-do-movimento': 'Recebidos os autos',
                'hash': '1234',
                'data-do-recebimento': ['21/07/2015']
            }, {
                'tipo-do-movimento': 'Remessa',
                'hash': '1234',
                'destinatario': ['Psicologia'],
                'data-da-remessa': ['17/07/2015'],
                'prazo': ['15 dia(s)']
            }, {
                'tipo-do-movimento': 'Recebidos os autos',
                'hash': '1234',
                'data-do-recebimento': ['17/07/2015']
            }, {
                'tipo-do-movimento': 'Remessa',
                'hash': '1234',
                'destinatario': ['Assistente Social'],
                'data-da-remessa': ['15/06/2015'],
                'prazo': ['15 dia(s)']
            }, {
                'tipo-do-movimento': 'Recebimento',
                'hash': '1234',
                'data-de-recebimento': ['22/05/2015']
            }, {
                'tipo-do-movimento':
                'Despacho - Proferido despacho de mero expediente',
                'hash': '1234',
                'data-despacho':
                ['11/05/2015'],
                'descricao': ['Atenda-se ao Ministério Público. Promovam-se os'
                              ' estudos social e psicológico com a demandada'
                              ' e os adolescentes.'],
                'inteiro-teor': ('Atenda-se ao Ministério Público. Promovam-se'
                                 '  os estudos social e psicológico com a'
                                 ' demandada e os adolescentes.'),
            }, {
                'tipo-do-movimento': 'Conclusão ao Juiz',
                'hash': '1234',
                'data-da-conclusao': ['11/05/2015'],
                'juiz': ['VIVIANE TOVAR DE MATTOS ABRAHAO']
            }, {
                'tipo-do-movimento': 'Recebidos os autos',
                'hash': '1234',
                'data-do-recebimento': ['30/04/2015']
            }, {
                'tipo-do-movimento': 'Remessa',
                'hash': '1234',
                'destinatario': ['Ministério Público'],
                'data-da-remessa': ['08/04/2015'],
                'prazo': ['15 dia(s)']
            }, {
                'tipo-do-movimento': 'Recebimento',
                'hash': '1234',
                'data-de-recebimento': ['27/03/2015']
            }, {
                'tipo-do-movimento':
                'Despacho - Proferido despacho de mero expediente',
                'hash': '1234',
                'data-despacho': ['19/03/2015'],
                'descricao': ['Dê-se vista ao Ministério Público.'],
                'inteiro-teor': 'Dê-se vista ao Ministério Público.'
            }, {
                'tipo-do-movimento': 'Conclusão ao Juiz',
                'hash': '1234',
                'data-da-conclusao': ['19/03/2015'],
                'juiz': ['VIVIANE TOVAR DE MATTOS ABRAHAO']
            }, {
                'tipo-do-movimento': 'Distribuição Dirigida',
                'hash': '1234',
                'data-da-distribuicao': ['19/03/2015'],
                'serventia': ['Cartório da 2ª Vara de Família, Inf. e da'
                              ' Juv. e do Idoso - 2ª Vara de Família e da'
                              ' Infância e da Juventude e do Idoso'],
                'localizacao-na-serventia': ['Saída de Acervo']
            }]
        }

        self.assert_items_equal(itens, esperado)

    @patch('processostjrj.parser.cria_hash_do_movimento',
           return_value='1234')
    def test_extrai_itens_de_processo_com_links_sem_atributo_onclick(self,
                                                                     _chdm):
        soup = BeautifulSoup(processo_judicial_7, 'lxml')
        itens = parse_itens(
            soup,
            '0002346-95.2011.8.19.0045',
            inicio_itens=26
        )
        esperado = {
            'numero-processo':
            '0004999-58.2015.8.19.0036',
            'itens': [{
                'tipo-do-movimento': 'Distribuição Dirigida',
                'hash': '1234',
                'data-da-distribuicao':
                ['14/03/2011'],
                'serventia':
                ['Cartório da 2ª Vara de Família, da Inf., da Juv. '
                 'e do Idoso -'
                 ' 2ª Vara de Família Infância e Juventude e do Idoso'],
                'processo-s-apensado-s': ['0000159-51.2010.8.19.0045'],
                'processo-s-no-tribunal-de-justica':
                ['0002346-95.2011.8.19.0045'],
                'protocolo-s-no-tribunal-de-justica':
                ['201500617620 - Data: 26/10/2015'],
                'localizacao-na-serventia':
                ['Aguardando Arquivamento']
            }]
        }

        for chave, valor in esperado['itens'][-1].items():
            with self.subTest():
                self.assertEqual(itens['itens'][-1][chave], valor)

    @patch('processostjrj.parser.cria_hash_do_movimento',
           return_value='1234')
    def test_parse_process_com_mandado_pagamento(self, _chdm):
        soup = BeautifulSoup(process_com_mandado_pagamento, 'lxml')
        itens = parse_itens(
            soup,
            '0166627-93.2017.8.19.0001',
            inicio_itens=29
        )
        esperado = {
            'numero-processo':
            '0166627-93.2017.8.19.0001',
            'itens': [{
                'data-da-distribuicao': ['04/07/2017'],
                'hash':
                '1234',
                'localizacao-na-serventia': ['Arquivado na Serventia'],
                'processo-s-no-conselho-recursal': ['Não há.'],
                'serventia': [
                    'Cartório do 6º Juizado Especial Cível - '
                    'Lagoa - 6º Juizado Especial Cível - Lagoa'
                ],
                'tipo-do-movimento':
                'Distribuição Sorteio'
            }, {
                'hash': '1234',
                'no-mandado': ['742474'],
                'situacao-mandado': ['Pago'],
                'tipo-do-movimento': 'Mandado de Pagamento:'
            }, {
                'data-pagamento': ['18/10/2017'],
                'hash': '1234',
                'no-guia': ['081010000041111402'],
                'situacao-da-guia': ['Disponível'],
                'tipo-do-movimento': 'Guia de Depósito:',
                'valor-pago': ['R$ 2.585,33']
            }],
        }

        for chave, valor in esperado['itens'][-1].items():
            with self.subTest():
                self.assertEqual(itens['itens'][-1][chave], valor)
