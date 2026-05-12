# Sifting SDK — Real-Time Market Data API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Sifting](https://sifting.io) provides enterprise-grade real-time market data across **crypto, foreign exchange, US equities, and on-chain venues** — delivered over REST and WebSocket behind a single bearer token.

- Unified JSON schema across all venues
- Multi-venue aggregation into one canonical view
- Sub-100ms streams worldwide
- Single bearer token for all endpoints

## Quick Start

### REST — Get latest price

```python
import requests

API_KEY = "your_bearer_token"

headers = {"Authorization": f"Bearer {API_KEY}"}

# Get BTC/USD price
response = requests.get(
    "https://api.sifting.io/v1/price",
    headers=headers,
    params={"symbol": "BTC/USD", "venue": "crypto"}
)

print(response.json())
```

### WebSocket — Live price stream

```python
import asyncio
import websockets
import json

API_KEY = "your_bearer_token"

async def stream_prices():
    uri = f"wss://stream.sifting.io/v1/prices"
    
    async with websockets.connect(
        uri,
        extra_headers={"Authorization": f"Bearer {API_KEY}"}
    ) as ws:
        # Subscribe to BTC and EUR/USD
        await ws.send(json.dumps({
            "action": "subscribe",
            "symbols": ["BTC/USD", "EUR/USD", "AAPL"]
        }))
        
        async for message in ws:
            data = json.loads(message)
            print(f"{data['symbol']}: {data['price']} ({data['venue']})")

asyncio.run(stream_prices())
```

### JavaScript — REST example

```javascript
const API_KEY = "your_bearer_token";

const response = await fetch("https://api.sifting.io/v1/price?symbol=BTC/USD", {
  headers: {
    "Authorization": `Bearer ${API_KEY}`
  }
});

const data = await response.json();
console.log(data);
```

## Supported Asset Classes

| Asset class | Example symbols |
|---|---|
| Crypto | BTC/USD, ETH/USD, SOL/USD |
| Foreign Exchange | EUR/USD, GBP/USD, USD/JPY |
| US Equities | AAPL, MSFT, TSLA |
| On-chain | On-chain venue data |

## Documentation

Full API reference: [https://sifting.io/docs](https://sifting.io/docs)

Get your API key: [https://sifting.io](https://sifting.io)

## License

MIT
