import requests
import sys
def bitcoin_price():
    try:
        x=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        # x.raise_for_status()
        y = x.json()
        return y['bpi']['USD']['rate_float']
    except:
        sys.exit(1)

def main():
    if len(sys.argv) ==1:
        sys.exit("Missing command-line argument  ")

    try:
        num =float(sys.argv[1])
    except:
        print("Command-line argument is not a number ")
        sys.exit(1)

    price = bitcoin_price()
    cost = num * price

    print(f"${cost:,.4f}")
if __name__ == "__main__":
    main()