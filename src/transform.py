import pandas as pd
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def transform_data(raw_data):
    try:
        df = pd.DataFrame(raw_data)
        df['extracted_at'] = datetime.now()
        logger.info("Conversão para DataFrame concluída.")
        return df
    except Exception as e:
        logger.error(f"Erro ao converter dados: {e}")
        raise e
