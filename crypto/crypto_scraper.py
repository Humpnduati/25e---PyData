import requests
import pandas as pd
import os
import time
from datetime import datetime

CSV_FILE = os.path.expanduser('/home/humpnduati/DATA_SCIENCE/25e---PyData/crypto/crypto_data.csv')
CURRENCY = 'usd'

def fetch_all_crypto_data():
    all_data = []
    page = 1

    while True:
        print(f"Fetching page {page}...")
        url = 'https://api.coingecko.com/api/v3/coins/markets'
        params = {
            'vs_currency': CURRENCY,
            'order': 'market_cap_desc',
            'per_page': 250,
            'page': page,
            'sparkline': False
        }

        response = requests.get(url, params=params)

        if response.status_code == 429:
            print("⚠️ Rate limit hit. Waiting 60 seconds before retrying...")
            time.sleep(60)
            continue

        response.raise_for_status()
        data = response.json()

        if not data:
            break

        all_data.extend(data)
        page += 1
        time.sleep(1.2)

    return all_data

def process_data(data, previous_df=None):
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    rows = []

    for coin in data:
        name = coin['name']
        price = coin['current_price']
        market_cap = coin['market_cap']
        volume_24h = coin['total_volume']
        circulating_supply = coin['circulating_supply']
        change_6hrs = None

        if previous_df is not None:
            prev_row = previous_df[previous_df['name'] == name]
            if not prev_row.empty:
                prev_price = prev_row.iloc[-1]['price']
                if prev_price:
                    change_6hrs = round(((price - prev_price) / prev_price) * 100, 2)

        rows.append({
            'timestamp': now,
            'name': name,
            'price': price,
            'market_cap': market_cap,
            'volume_24h': volume_24h,
            'circulating_supply': circulating_supply,
            'change_6hrs': change_6hrs
        })

    return pd.DataFrame(rows)

def save_to_csv(new_df):
    if os.path.exists(CSV_FILE):
        existing_df = pd.read_csv(CSV_FILE)
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        combined_df.to_csv(CSV_FILE, index=False)
    else:
        new_df.to_csv(CSV_FILE, index=False)

def run_scraper():
    if os.path.exists(CSV_FILE):
        full_df = pd.read_csv(CSV_FILE)
        latest_time = full_df['timestamp'].max()
        latest_df = full_df[full_df['timestamp'] == latest_time]
    else:
        latest_df = None

    try:
        all_data = fetch_all_crypto_data()
        new_df = process_data(all_data, latest_df)
        save_to_csv(new_df)
        print(f"[{datetime.now()}] ✅ Scraped {len(new_df)} coins and appended to CSV.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    run_scraper()
