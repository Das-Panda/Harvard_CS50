pip install requests

import sys
import requests

def main():
    # Check if the command-line argument is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: python Bitcoin.py <number_of_bitcoins>")

    try:
        # Convert the command-line argument to a float
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: The argument must be a valid number.")

    try:
        # Query the CoinDesk API for the current Bitcoin price
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()

        # Extract the current price of Bitcoin in USD
        price_per_bitcoin = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error: Could not fetch the Bitcoin price.")

    # Calculate the total cost
    total_cost = bitcoins * price_per_bitcoin

    # Output the total cost formatted to four decimal places with thousands separator
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()