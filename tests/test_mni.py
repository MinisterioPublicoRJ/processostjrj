import os

from unittest import TestCase, mock, main

from processostjrj.mni import cria_cliente

WSDL = os.environ['WSDL_MNI']


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
            WSDL,
            transport='transport_obj'
        )
        self.assertFalse(session_mock.verify)
        self.assertEqual(cliente_obj, 'cliente_obj')


if __name__ == '__main__':
    main()
