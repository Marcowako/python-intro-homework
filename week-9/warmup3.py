import requests

response = requests.get("https://restcountries.com/v3.1/region/europe?fields=name,population")
countries = response.json()

print(response.status_code)
print(countries)

for country in countries[:10]:
    print(country["name"]["common"])