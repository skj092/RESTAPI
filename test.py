# this script is use to test the REST API

import requests

# get the localhost:7000 url

url = "http://localhost:7000/"

# get the response of the API
r = requests.get(url)
print('Response Code: ', r.status_code)
print('Response: ', r.json())

# testing post method
url = "http://localhost:7000/items"
new_item = {'id': 4, 'name': 'item4'}
r = requests.post(url, json=new_item)
print('Response Code: ', r.status_code)
print('Response: ', r.json())

# testing put method
url = "http://localhost:7000/items/4"
r = requests.put(url, json={'name': 'Updated item'})
print('Response Code: ', r.status_code)
print('Response: ', r.json())

# testing patch method
url = "http://localhost:7000/items/4"
r = requests.patch(url, json={'name': 'Updated item'})
print('Response Code: ', r.status_code)
print('Response: ', r.json())

# testing delete method
url = "http://localhost:7000/items/4"
r = requests.delete(url)
print('Response Code: ', r.status_code)
print('Response: ', r.json())

