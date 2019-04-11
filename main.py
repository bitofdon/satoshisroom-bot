import requests
import json
from flask import Flask
#connect to API token from config.json and pass it
with open('config.json', 'r') as infile:
    config = dict(json.load(infile))
    token = config["token"]

app = Flask(__name__)

#https://pro-api.coinmarketcap.com
def get_cmc_data(crypto):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = {'symbol': crypto, 'convert': 'USD'}
    headers = {'X-CMC_PRO_API_KEY': token}

    r = requests.get(url, headers=headers, params=params).json()
    print(r)

def main():
    #print the call of get_cmc_data - BTC as an argument here as example
    get_cmc_data('BTC') #to get data

if __name__ == '__main__':
    main()
    #app.run(debug=True)
