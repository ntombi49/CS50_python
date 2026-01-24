import sys
import requests

# 1. Validate command-line argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# 2. Query CoinCap API
api_key = "YOUR_API_KEY_HERE"
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Error fetching Bitcoin price")

# 3. Calculate cost
total_cost = bitcoins * price

# 4. Output formatted result
print(f"${total_cost:,.4f}")
