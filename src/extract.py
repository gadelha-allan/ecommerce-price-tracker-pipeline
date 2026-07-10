import requests
import json

def fetch_data(query="iphone"):
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['results']
        with open('data/raw_data.json', 'w') as f:
            json.dump(data, f)
        return data
    else:
        raise Exception(f"Erro na API: {response.status_code}")

if __name__ == "__main__":
    fetch_data()