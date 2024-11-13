#Import module
import sys
import requests

def main():
    #Get bitcoin number from command line argument
    try:
        bitcoin = float(sys.argv[1])
    except IndexError:
        sys.exit('Missing command-line arguments')
    except ValueError:
        sys.exit('Command-line argument is not a number')

    #Request the current bitcoin price in USD
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        text = r.json()
    except requests.RequestException:
        print('Invalid URL')

    #Output current bitcoin price
    amount = text['bpi']['USD']['rate']
    amount = float(amount.replace(',', ''))
    amount *= bitcoin
    print(f"${amount:,.4f}")

if __name__ == '__main__':
    main()