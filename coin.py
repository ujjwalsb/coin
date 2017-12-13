import requests
import csv
from datetime import date

r = requests.get('https://api.coinmarketcap.com/v1/ticker/?convert=INR&limit=2')
res = (r.json())

print type(res)
print res

# today = date.today()
# with open("BTC","w+") as f:
# 	a = csv.DictWriter (f, res.keys())
# 	a.writeheader
# 	a.writerow(res)