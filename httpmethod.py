# Learning different ways to test APIs
import requests

# Method 1: Using requests.get()
# Test 1: Get the status code of the API
url = "https://jsonplaceholder.typicode.com/todos/1"
r = requests.get(url)
print('Status code: ', r.status_code)

# Test 2: Get the response of the API
url = "https://jsonplaceholder.typicode.com/todos/1"
r = requests.get(url)
print('Response: ', r.json())

# Test 3: Get the response of the API in JSON format
url = "https://jsonplaceholder.typicode.com/todos/1"
r = requests.get(url)
response_dict = r.json()
print('Response in JSON format: ', response_dict)

# Method 2: Using requests.post()
# Test 4: Post a new todo
url = "https://jsonplaceholder.typicode.com/todos"
new_todo = {'userId': 1, 'title': 'Test todo', 'completed': False}
r = requests.post(url, json=new_todo)
print('Status code: ', r.status_code)
print('Response: ', r.json())

# Method 3: Using requests.put()
# Test 5: Update a todo
url = "https://jsonplaceholder.typicode.com/todos/1"
r = requests.put(url, json={'title': 'Updated todo'})
print('Status code: ', r.status_code)
print('Response: ', r.json())cl

# Method 4: Using requests.patch()
# Test 6: Update a todo
url = "https://jsonplaceholder.typicode.com/todos/2"
r = requests.patch(url, json={'title': 'Updated todo'})
print('Status code: ', r.status_code)
print('Response: ', r.json())

# Method 5: Using requests.delete()
# Test 7: Delete a todo
url = "https://jsonplaceholder.typicode.com/todos/1"
r = requests.delete(url)
print('Status code: ', r.status_code)
print('Response: ', r.json())