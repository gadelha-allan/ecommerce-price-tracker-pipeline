import logging
from src.extract import fetch_data, upload_to_s3
from src.transform import transform_data
from src.load import load_to_postgres

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    try:
        logging.info("--- Extração e Data Lake ---")
        raw_data = fetch_data("iphone", max_pages=3)
        upload_to_s3(raw_data)
        
        logging.info("--- Transformação ---")
        df_cleaned = transform_data(raw_data)
        
        logging.info("--- Carga Idempotente ---")
        load_to_postgres(df_cleaned)
        
        logging.info("Pipeline finalizado com sucesso!")
        
    except Exception as e:
        logging.error(f"Falha crítica na execução do pipeline: {e}")
        raise e 

if __name__ == "__main__":
    run_pipeline()
