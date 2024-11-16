import requests

citi_name = input()
print(citi_name)
print(f'Display Weather for city: {citi_name}')

url = f'https://wttr.in/{citi_name}'

result = requests.get(url)

print(result.text)