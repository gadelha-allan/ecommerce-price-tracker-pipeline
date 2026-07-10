import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def load_to_postgres(df, table_name="prices"):
    try:
        DB_USER = os.getenv('DB_USER')
        DB_PASS = os.getenv('DB_PASS')
        DB_HOST = os.getenv('DB_HOST')
        DB_PORT = os.getenv('DB_PORT')
        DB_NAME = os.getenv('DB_NAME')
    
        conn_string = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        engine = create_engine(conn_string)
        
        with engine.connect() as connection:
            df.to_sql(table_name, connection, if_exists='append', index=False)
            print(f"Sucesso: {len(df)} registros inseridos na tabela {table_name}.")
            
    except Exception as e:
        print(f"Erro ao conectar ou inserir dados: {e}")