"""import requests
import sys

try:
    try:
        if len(sys.argv) <= 1:
            sys.exit("Missing command-line argument")
        else:
            count = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey="
    r = requests.get(url)
    response = r.json()
    print(f"${float(response["data"]["priceUsd"]) * count:,.4f}")

except requests.RequestException:
    pass
"""

import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Get the current Bitcoin price in USD
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=")
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

    data = response.json()
    price = float(data["data"]["priceUsd"])
    total = bitcoins * price
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()
