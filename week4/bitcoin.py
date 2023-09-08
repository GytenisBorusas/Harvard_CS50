
import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Missing or too many command-line arguments")
        sys.exit(1)

    try:
        user_bitcoin_amount = int(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Raises an exception if the request was unsuccessful

        data = response.json()
        bitcoin_price_usd_str = data["bpi"]["USD"]["rate"]
        
        # Convert price string to float (remove commas)
        bitcoin_price_usd = float(bitcoin_price_usd_str.replace(',', ''))
        
        # Calculate and print the amount
        amount = bitcoin_price_usd * user_bitcoin_amount
        # print(f"Bitcoin price in USD: {bitcoin_price_usd:,.2f}")
        print(f"Total in USD for {user_bitcoin_amount} Bitcoins: ${amount:,.2f}")
    except requests.RequestException:
        print("Failed to fetch data!")
        sys.exit(1)



if __name__ == "__main__":
    main()

