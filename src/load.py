import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def load_to_postgres(df, table_name="prices"):

    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    
    conn_string = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(conn_string)
    
  
    df.to_sql(table_name, engine, if_exists='append', index=False)
    print(f"Dados inseridos com sucesso na tabela {table_name}!")