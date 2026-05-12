"""
Sifting API — REST example
Get real-time price for any symbol across crypto, FX, and US equities.

Docs: https://sifting.io/docs
Get API key: https://sifting.io
"""

import requests

API_KEY = "your_bearer_token_here"
BASE_URL = "https://api.sifting.io/v1"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_price(symbol: str, venue: str = "crypto"):
    """
    Get latest price for a symbol.
    
    Args:
        symbol: e.g. "BTC/USD", "EUR/USD", "AAPL"
        venue:  "crypto" | "fx" | "equities" | "onchain"
    """
    response = requests.get(
        f"{BASE_URL}/price",
        headers=headers,
        params={"symbol": symbol, "venue": venue}
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # Crypto
    btc = get_price("BTC/USD", venue="crypto")
    print(f"BTC/USD: {btc}")

    # Forex
    eur = get_price("EUR/USD", venue="fx")
    print(f"EUR/USD: {eur}")

    # US Equities
    aapl = get_price("AAPL", venue="equities")
    print(f"AAPL:    {aapl}")
