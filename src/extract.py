import requests
import json
import logging

logger = logging.getLogger(__name__)

def fetch_data(query="iphone"):
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={query}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()['results']

        with open('data/raw_data.json', 'w') as f:
            json.dump(data, f)
            
        logger.info(f"Extração concluída. {len(data)} itens encontrados.")
        return data
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Falha ao conectar na API: {e}")
        raise e