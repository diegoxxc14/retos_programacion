import requests

api_url = 'https://jsonplaceholder.typicode.com/todos/1'
#api_url = 'https://feriados-cl-api.herokuapp.com/feriados'
res = requests.get(api_url)  # Send a GET request

sts_code = res.status_code
hds = res.headers["Content-Type"]

print('Code:', sts_code)
print('Content Type:', hds)
print(res.json())  # View the data that came back from the API
