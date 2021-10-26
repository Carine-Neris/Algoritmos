# AUTHOR: Diego Neves
# Python3 Concept: API, JSON
# GITHUB: github.com/diegoaceneves

import requests
import json

URL="http://economia.awesomeapi.com.br/json/last/BRL-EUR"

response = requests.get(URL)
if (response.status_code == 200):
    print("€1.00 is equal R${:.2f}\n".format(float(response.json()['BRLEUR']['ask'])))
