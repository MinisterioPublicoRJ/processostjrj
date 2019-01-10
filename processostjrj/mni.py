import os

from requests import Session

from zeep import Client
from zeep.transports import Transport


WSDL = os.environ['WSDL_MNI']
ID = os.environ['ID_MNI']
SENHA = os.environ['SENHA_MNI']


def cria_cliente():
    session = Session()
    session.verify = False
    transport = Transport(session=session)
    return Client(WSDL, transport=transport)


def consulta_processo(cliente, numero_processo, *args, **kwargs):
    return cliente.service.consultarProcesso(
        idConsultante=ID,
        senhaConsultante=SENHA,
        numeroProcesso=numero_processo,
        *args,
        **kwargs
    )
