import requests
response = requests.get("http://127.0.0.1:5000/api/nombre")
requests.post("http://127.0.0.1:5000/api/nombre", {"nombre": "Maria", "nota": "5"})
print(response.json())

response = requests.get("http://127.0.0.1:5000/api/nota")
print(response.json())

response = requests.get("http://127.0.0.1:5000/api/titulacion")
print(response.json())