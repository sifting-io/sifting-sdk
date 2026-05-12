"""
Sifting API — WebSocket example
Subscribe to real-time price stream across crypto, FX, and US equities.

Docs: https://sifting.io/docs
Get API key: https://sifting.io
"""

import asyncio
import websockets
import json

API_KEY = "your_bearer_token_here"
WS_URL = "wss://stream.sifting.io/v1/prices"


async def stream_prices(symbols: list):
    """
    Stream real-time prices for a list of symbols.

    Args:
        symbols: e.g. ["BTC/USD", "EUR/USD", "AAPL"]
    """
    async with websockets.connect(
        WS_URL,
        extra_headers={"Authorization": f"Bearer {API_KEY}"}
    ) as ws:

        # Subscribe
        await ws.send(json.dumps({
            "action": "subscribe",
            "symbols": symbols
        }))
        print(f"Subscribed to: {symbols}")
        print("-" * 40)

        # Listen
        async for message in ws:
            data = json.loads(message)
            print(f"{data['symbol']:12} {data['price']:>12} ({data['venue']})")


if __name__ == "__main__":
    symbols = [
        "BTC/USD",   # crypto
        "ETH/USD",   # crypto
        "EUR/USD",   # forex
        "AAPL",      # equities
    ]
    asyncio.run(stream_prices(symbols))
