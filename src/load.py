import os
import logging
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

def load_to_postgres(df, table_name="prices"):
    try:
        conn_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        engine = create_engine(conn_string)
        
        temp_table = f"{table_name}_temp"
        
        with engine.begin() as connection:
            df.to_sql(temp_table, connection, if_exists='replace', index=False)
            
            upsert_query = text(f"""
                INSERT INTO {table_name} (id, title, price, currency_id, permalink, extracted_at)
                SELECT id, title, price, currency_id, permalink, extracted_at
                FROM {temp_table}
                ON CONFLICT (id) DO UPDATE SET 
                    price = EXCLUDED.price,
                    extracted_at = EXCLUDED.extracted_at;
            """)
            connection.execute(upsert_query)
            
            connection.execute(text(f"DROP TABLE {temp_table}"))
            
            logger.info(f"Carga idempotente (UPSERT) concluída com sucesso para {len(df)} registros.")
            
    except Exception as e:
        logger.error(f"Erro crítico na carga de dados: {e}")
        raise e
