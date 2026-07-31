import requests
import logging
import json
import boto3
import os
from datetime import datetime


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

def upload_to_s3(data, bucket_name="bronze", file_prefix="mercadolivre_"):
    s3_client = boto3.client(
        's3',
        endpoint_url='http://localhost:9000', 
        aws_access_key_id=os.getenv('MINIO_USER', 'admin'),
        aws_secret_access_key=os.getenv('MINIO_PASS', 'admin123')
    )
    
    try:
        s3_client.create_bucket(Bucket=bucket_name)
    except s3_client.exceptions.BucketAlreadyOwnedByYou:
        pass

    file_name = f"{file_prefix}{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=json.dumps(data)
        )
        logger.info(f"Dados brutos salvos com sucesso no Data Lake: {bucket_name}/{file_name}")
    except Exception as e:
        logger.error(f"Erro ao salvar no Data Lake: {e}")
        raise e
