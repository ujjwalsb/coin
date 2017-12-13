import requests
import unicodecsv as csv
from datetime import date

r = requests.get('https://api.coinmarketcap.com/v1/ticker/?convert=INR&limit=3')
res = (r.json())

# print res

dict_keys = res[0].values()
keys = res[0].keys()
today = date.today()

# print type(dict_keys)

for dict_keys[7] in enumerate(dict_keys[8]): 

	with open(str(dict_keys[7])+"_"+str(today)+".csv","w+") as f:
		a = csv.DictWriter (f, keys)
		a.writeheader()
		a.writerows(res)

		print a.writeheader