import requests
import logging

logger = logging.getLogger(__name__)

def fetch_data(query="iphone", max_pages=5):
    all_results = []
    limit = 50
    
    try:
        for page in range(max_pages):
            offset = page * limit
            url = f"https://api.mercadolibre.com/sites/MLB/search?q={query}&offset={offset}&limit={limit}"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json().get('results', [])
            if not data:
                break
                
            all_results.extend(data)
            logger.info(f"Página {page + 1} extraída. {len(data)} itens coletados.")
            
        logger.info(f"Extração total concluída: {len(all_results)} itens.")
        return all_results
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Falha ao conectar na API na página {page + 1}: {e}")
        raise e
