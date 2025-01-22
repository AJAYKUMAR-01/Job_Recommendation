import requests

BASE_URL = "http://127.0.0.1:8000"

def api_post(endpoint, payload):
    try:
        response = requests.post(f"{BASE_URL}{endpoint}", json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def api_get(endpoint):
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
