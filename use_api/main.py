import requests

url = 'https://dummyjson.com/products'
data = requests.get(url)
if data.status_code == 200:
   data = data.json()
   for e in data['products']:
       print(e['title'])
