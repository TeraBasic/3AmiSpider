import requests
import json

url = "https://www.bellevue.ch/en/asset-management/products-performance/"
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0'}

r = requests.get(url, headers=headers)

print("r.text: ", r.text)













