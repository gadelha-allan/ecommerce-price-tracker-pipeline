import pandas as pd
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def transform_data(raw_data):
    try:
        df = pd.DataFrame(raw_data)
        
        columns_to_keep = ['id', 'title', 'price', 'currency_id', 'permalink']
        
        if not all(col in df.columns for col in columns_to_keep):
            missing = [c for c in columns_to_keep if c not in df.columns]
            raise ValueError(f"Colunas ausentes no JSON da API: {missing}")
        
        df = df[columns_to_keep].copy()
        df['search_date'] = datetime.now()
        
        df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)
        
        logger.info("Transformação concluída com sucesso.")
        return df
        
    except Exception as e:
        logger.error(f"Erro na transformação de dados: {e}")
        raise e