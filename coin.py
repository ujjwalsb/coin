import requests
import unicodecsv as csv
from datetime import date

r = requests.get('https://api.coinmarketcap.com/v1/ticker/?convert=INR&limit=5')
res = (r.json())

# n = res[0].values()
keys = res[0].keys()
today = date.today()
for item in res:
	with open(str(item['id'])+"_"+str(today)+".csv","w+") as f:
		a = csv.DictWriter (f, keys)
		a.writeheader()
		a.writerows(res)