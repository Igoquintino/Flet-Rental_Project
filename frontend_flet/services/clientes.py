from services.api_client import api_request

def listar_clientes():
    return api_request("GET", "clientes/")

def criar_cliente(dados):
    return api_request("POST", "clientes/", data=dados)
