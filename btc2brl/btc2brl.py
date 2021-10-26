# AUTHOR: Diego Neves
# Python3 Concept: API, JSON
# GITHUB: github.com/diegoaceneves

import requests
import json

URL="http://economia.awesomeapi.com.br/json/last/USD-BRL"
URL2="https://www.mercadobitcoin.net/api/BTC/ticker/"

response = requests.get(URL)
if (response.status_code == 200):
    response2 = requests.get(URL2)
    if (response2.status_code == 200):
        print("1 BTC equivale a R${:.2f}\n".format(
            float(response2.json()['ticker']['last'])*float(response.json()['USDBRL']['ask'])
            )
        )