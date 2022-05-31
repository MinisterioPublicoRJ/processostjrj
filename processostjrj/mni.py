import os

from requests import Session

from zeep import Client
from zeep.transports import Transport
from decouple import config

# WSDL = os.environ.get('WSDL_MNI', '')
# ID = os.environ.get('ID_MNI', '')
# SENHA = os.environ.get('SENHA_MNI', '')

WSDL = config('WSDL_MNI', '')
ID = config('ID_MNI', '')
SENHA = config('SENHA_MNI', '')


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
