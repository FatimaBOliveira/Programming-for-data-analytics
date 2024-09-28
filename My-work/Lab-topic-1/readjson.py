# Program that reads a json file from a URL
# Author: Fatima Oliveira

import requests

url ="https://api.coindesk.com/v1/bpi/currentprice.json"

# 7. Write a program to print this JSON to the console

response = requests.get(url)
data = response.json()
print(data)

# Is this JSON or a Dict object that is outputted. -> dict object is printed.

# 8. Modify the program to only output the current price in Euros.

print(data['bpi']['EUR']['rate_float'])