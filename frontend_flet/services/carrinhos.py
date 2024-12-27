from services.api_client import api_request

def listar_carrinhos():
    return api_request("GET", "carts/")

def criar_carrinho(dados):
    return api_request("POST", "carts/", data=dados)

def atualizar_carrinho(carrinho_id, dados):
    return api_request("PATCH", f"carts/{carrinho_id}/", data=dados)
