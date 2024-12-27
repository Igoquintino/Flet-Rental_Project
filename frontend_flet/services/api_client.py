import requests

BASE_URL = "http://127.0.0.1:8000/"  # URL base do backend

def api_request(method, endpoint, data=None, params=None):
    url = f"{BASE_URL}/{endpoint}"
    try:
        response = requests.request(method, url, json=data, params=params)
        response.raise_for_status()  # Levanta exceção para status 4xx e 5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer requisição para {url}: {e}")
        return None
