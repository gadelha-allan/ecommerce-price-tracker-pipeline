import os
import sys
import logging
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

def load_to_postgres(df, table_name="prices"):
    try:
        required_vars = ['DB_USER', 'DB_PASS', 'DB_HOST', 'DB_PORT', 'DB_NAME']
        for var in required_vars:
            if not os.getenv(var):
                raise EnvironmentError(f"Variável de ambiente {var} não configurada.")

        conn_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        engine = create_engine(conn_string)
        
        with engine.connect() as connection:
            df.to_sql(table_name, connection, if_exists='append', index=False)
            logger.info(f"Sucesso: {len(df)} registros inseridos na tabela {table_name}.")
            
    except Exception as e:
        logger.error(f"Erro crítico na carga de dados: {e}")
        raise e