import pandas as pd
import os

def transform_data():
    os.makedirs('data/transformed', exist_ok=True)
    df = pd.read_csv('data/clean/events.csv')
    
    # Extract date portion in YYYY-MM-DD format
    df['date'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d')
    
    df.to_csv('data/transformed/events.csv', index=False)

if __name__ == '__main__':
    transform_data()
