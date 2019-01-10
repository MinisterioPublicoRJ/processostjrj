import os

from requests import Session

from zeep import Client
from zeep.transports import Transport


WSDL = os.environ['WSDL_MNI']


def cria_cliente():
    session = Session()
    session.verify = False
    transport = Transport(session=session)
    return Client(WSDL, transport=transport)
