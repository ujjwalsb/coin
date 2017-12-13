import requests
import csv
from datetime import date

r = requests.get('https://api.coinmarketcap.com/v1/ticker/?convert=INR&limit=2')
print(r.json())

today = date.today()
btc = open("BTC","w+")
eth = open("ETH","w+")
