import requests
import json
from flask import Flask
#connect to API token from config.json and pass it
with open('config.json', 'r') as infile:
    config = dict(json.load(infile))
    token = config["token"]

app = Flask(__name__)

#prettify json - dump & write the call into a file called response.json
def write_json(data, filename='response.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

#https://pro-api.coinmarketcap.com
def get_cmc_data(crypto):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = {'symbol': crypto, 'convert': 'USD'}
    headers = {'X-CMC_PRO_API_KEY': token}

    #get the price of any 'crypto', we pass in our data dictionary
    #BTC dictionary has keys: 'quote', 'USD', 'price'
    r = requests.get(url, headers=headers, params=params).json()
    price = r['data'][crypto]['quote']["USD"]['price']
    return price

def main():
    #print the call of get_cmc_data - BTC as an argument here as example
    print(get_cmc_data('BTC'))

if __name__ == '__main__':
    main()
