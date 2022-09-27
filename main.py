from Dados import *
from Sap import Sap

dados_clientes = DadosClientes()
dados_clientes.carregar_dados_do_arquivo()
Sap(dados_clientes)
