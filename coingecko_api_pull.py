#This script uses the tokens list(predetermined) and grabs the designated values from the coingecko API(name, current price, total volume, and last updated)  
#and writes them to a csv file with today's date.  

import requests
import json
import csv
import pandas as pd
from datetime import datetime


json_list = []

#Predetermined list of tokens.  Use token ID from https://docs.google.com/spreadsheets/d/1wTTuxXt8n9q7C4NDXqQpI3wpKu1_5bGVmP9Xz0XGSyU/edit#gid=0
tokens = ["bitcoin", "ethereum", "ripple", "solana", "cardano", "terra-luna", "avalanche-2", "polkadot", "dogecoin", "shiba-inu", "ravencoin", "matic-network", "near", "litecoin", "cosmos", "uniswap", "tron", "ethereum-classic", "algorand", "monero", "decentraland"]

#For each token, grab the name, current price, total volume, and last updated values from the API.  Append to the json_list from earlier.
for token in tokens:
   url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=" + token
   response = requests.get(url)
   json_data = response.json()
   for json_dic in json_data:
      json_name = json_dic.get('name')
      json_current_price = json_dic.get('current_price')
      json_total_volume = json_dic.get('total_volume')
      json_last_updated = json_dic.get('last_updated')
      json_list.append([json_name, json_current_price, json_total_volume, json_last_updated])

#Create a pandas dataframe from the json_list, then write to a file with today's date.
df = pd.DataFrame(json_list)
date = datetime.now().strftime("%Y_%m_%d")
write_file="/opt/crypto/reports/crypto_data_" + date + ".csv"
df.to_csv(write_file, mode='a', index=False, header=False)

#[{'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin', 'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579', 'current_price': 42373, 
#'market_cap': 805383061765, 'market_cap_rank': 1, 'fully_diluted_valuation': 889828881986, 'total_volume': 18750211486, 'high_24h': 43747, 'low_24h': 42212, 
#'price_change_24h': -1373.739536610316, 'price_change_percentage_24h': -3.14022, 'market_cap_change_24h': -25487620908.508423, 'market_cap_change_percentage_24h': -3.06758, 
#'circulating_supply': 19007075.0, 'total_supply': 21000000.0, 'max_supply': 21000000.0, 'ath': 69045, 'ath_change_percentage': -38.60921, 'ath_date': '2021-11-10T14:24:11.849Z', 
#'atl': 67.81, 'atl_change_percentage': 62409.59118, 'atl_date': '2013-07-06T00:00:00.000Z', 'roi': None, 'last_updated': '2022-04-09T15:48:40.232Z'}]