import requests

response = requests.get("http://api.open-notify.org/astros.json")

print("Antal astronauter i rymden:", response.json()['number'], "St")
print("De astronauter som är i rymden är:")

iterations = response.json()['number']

for a in range(iterations):
    print(response.json()['people'][a]['name'])
