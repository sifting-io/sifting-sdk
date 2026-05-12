/**
 * Sifting API — JavaScript REST example
 * Get real-time price for any symbol across crypto, FX, and US equities.
 *
 * Docs: https://sifting.io/docs
 * Get API key: https://sifting.io
 */

const API_KEY = "your_bearer_token_here";
const BASE_URL = "https://api.sifting.io/v1";

async function getPrice(symbol, venue = "crypto") {
  /**
   * Get latest price for a symbol.
   *
   * @param {string} symbol - e.g. "BTC/USD", "EUR/USD", "AAPL"
   * @param {string} venue  - "crypto" | "fx" | "equities" | "onchain"
   */
  const url = `${BASE_URL}/price?symbol=${symbol}&venue=${venue}`;

  const response = await fetch(url, {
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    },
  });

  if (!response.ok) {
    throw new Error(`API error: ${response.status}`);
  }

  return response.json();
}

// Examples
async function main() {
  // Crypto
  const btc = await getPrice("BTC/USD", "crypto");
  console.log("BTC/USD:", btc);

  // Forex
  const eur = await getPrice("EUR/USD", "fx");
  console.log("EUR/USD:", eur);

  // US Equities
  const aapl = await getPrice("AAPL", "equities");
  console.log("AAPL:   ", aapl);
}

main().catch(console.error);
