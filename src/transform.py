import pandas as pd
from datetime import datetime

def transform_data(raw_data):
    df = pd.DataFrame(raw_data)
    
    columns_to_keep = ['id', 'title', 'price', 'currency_id', 'permalink']
    df = df[columns_to_keep]
    
    df['search_date'] = datetime.now()
    
    df['price'] = df['price'].astype(float)
    
    return df