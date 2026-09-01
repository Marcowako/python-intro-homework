import requests

response = requests.get("https://api.agify.io/?name=michael")
data = response.json()

print(f"Name: {data['name']}")
print(f"Predicted age: {data['age']}")
print(f"Birthday: {data.get('birthday', 'Not available')}")