from unittest import TestCase

from bs4 import BeautifulSoup

from processostjrj.parser import estripa
from processostjrj.utils import (
    formata_numero_processo,
    limpa_conteudo,
    remove_data_consulta,
    cria_hash_do_movimento,
    cria_hash_do_processo,
)
from .fixtures.processos import processo_judicial_1


class Utils(TestCase):
    def test_format_document_numner(self):
        numero_processo = "09878976543451238976"

        numero_processo_formatado = formata_numero_processo(numero_processo)
        expected = "0987897-65.4345.1.23.8976"

        self.assertEqual(numero_processo_formatado, expected)

    def test_limpa_conteudo(self):
        conteudo_sujo = ('\r\n                        Av. Presidente Lincol'
                         'n\r\n                        \xa0\r\n            '
                         '            857\r\n                        \xa0\r'
                         '\n                        \r\n                   '
                         '\xa0\r\n                      ')

        conteudo_limpo = limpa_conteudo(conteudo_sujo)
        esperado = 'Av. Presidente Lincoln 857'

        self.assertEqual(conteudo_limpo, esperado)

    def test_estripa_texto_com_tags_erradas(self):
        html = """
            <td valign=top align=justify class='normal'><N>EDITAL DE CITAÇÃO
                                     (Com o prazo de 15 dias)<\\N>

             O MM. Juiz de Direito, Dr.(a) Rodrigo Leal Manhaes de Sa -
             Juiz Titular do Cartório da Vara Criminal da Comarca de Araru...
             <br><br>
             <a href='javascript:void("17");' onClick=window.open(
             'popdespacho.jsp?tipoato=Descri%E7%E3o&numMov=17&descMov=
             Publica%E7%E3o+de+Edital','','width=500,height=250,left=300,
             top=300,location=no,menubar=no,resizable=no,scrollbars=yes,
             status=no,toolbar=no');> Ver íntegra do(a) Publicação de Edital
                                                         </a>
                                                         </td>
            """
        soup = BeautifulSoup(html, 'lxml')
        saida = estripa(soup)

        self.assertIn("O MM. Juiz de Direito", saida)


class Hash(TestCase):
    def test_cria_hash_do_conteudo_html_do_processo(self):
        hash_documento = cria_hash_do_processo(processo_judicial_1)
        esperado = '30a5e6dc4717981102f2dfc2598eac27'

        self.assertEqual(hash_documento, esperado)

    def test_remove_data_de_consulta_do_html(self):
        trecho_processo = '<tr valign="top"><td colspan="2" class="info">'\
            'TJ/RJ -\r\n                      23/03/2018 12:48:23</td>'\
            '</tr>'.encode()

        processo_sem_data = remove_data_consulta(trecho_processo)
        esperado = '<tr valign="top"><td colspan="2" class="info"></td>'\
            '</tr>'.encode()

        self.assertEqual(processo_sem_data, esperado)

    def test_cria_hash_para_um_movimento(self):
        item = {
            'tipo-do-movimento': 'Conclusão ao Juiz',
            'data-da-conclusao': ['21/10/2015'],
            'juiz': ['VIVIANE TOVAR DE MATTOS ABRAHAO']
        }

        movimento_hash = cria_hash_do_movimento(item)
        esperado = '03b979f3d68a8b526746c94370039ddb'

        self.assertEqual(movimento_hash, esperado)
