import os
from unittest import TestCase, mock, main
from processostjrj.mni import cria_cliente, consulta_processo
import requests


class TestMni(TestCase):
    @mock.patch('processostjrj.mni.Session')
    @mock.patch('processostjrj.mni.Transport', return_value='transport_obj')
    @mock.patch('processostjrj.mni.Client')
    def test_cria_cliente_mni(self, _client, _transport, _session):
        session_mock = mock.MagicMock()
        _session.return_value = session_mock
        _client.return_value = 'cliente_obj'

        cliente_obj = cria_cliente()

        _transport.assert_called_once_with(session=session_mock)
        _client.assert_called_once_with(
            "",
            transport='transport_obj'
        )
        self.assertFalse(session_mock.verify)
        self.assertEqual(cliente_obj, 'cliente_obj')

    def test_consulta_processo(self):
        ID_MNI = ''
        SENHA_MNI = ''
        numero_processo = '1234'
        cliente = mock.MagicMock()
        cliente.service.consultarProcesso.return_value = 'resposta'
        resposta = consulta_processo(
            cliente,
            numero_processo,
            _value_1=[{'incluirCabecalho': True}]
        )

        cliente.service.consultarProcesso.assert_called_once_with(
            idConsultante=ID_MNI,
            senhaConsultante=SENHA_MNI,
            numeroProcesso=numero_processo,
            _value_1=[{'incluirCabecalho': True}]
        )
        self.assertEqual(resposta, 'resposta')


if __name__ == '__main__':
    main()
