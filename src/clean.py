import pandas as pd
import os

# Define what constitutes a valid event type for your dataset
VALID_EVENT_TYPES = ['click', 'view', 'purchase', 'login', 'logout'] # Update this list based on your data

def clean_data():
    os.makedirs('data/clean', exist_ok=True)
    df = pd.read_csv('data/raw/events.csv')

    # Drop missing fields
    df = df.dropna()

    # Drop invalid event_types
    df = df[df['event_type'].isin(VALID_EVENT_TYPES)]

    # Drop non-positive duration
    df = df[df['duration_seconds'] > 0]

    df['duration_seconds'] = df['duration_seconds'].astype(int)

    # Normalize timestamp to ISO 8601 (YYYY-MM-DDTHH:MM:SS)
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed').dt.strftime('%Y-%m-%dT%H:%M:%S')

    df.to_csv('data/clean/events.csv', index=False)

if __name__ == '__main__':
    clean_data()
