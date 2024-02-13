import pandas as pd
import requests

url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/latest"
headers = {
    "X-RapidAPI-Key": "f6bf0cad81mshc53de1314a052eep1bc4ccjsn277040b05312",
    "X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com",
}


response = requests.get(url, headers=headers)

if response.status_code == 200:
    # print(response.json())

    jsonData = response.json()
    data = pd.json_normalize(jsonData)
    print(data)
    data.to_csv("currency.csv")
    print(data.rates.EUR, data.rates.USD)
else:
    print("Error:", response.status_code)

# import requests

# url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/latest"

# querystring = {"from": "USD", "to": "EUR,GBP"}

# headers = {
#     "X-RapidAPI-Key": "f6bf0cad81mshc53de1314a052eep1bc4ccjsn277040b05312",
#     "X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com",
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())
