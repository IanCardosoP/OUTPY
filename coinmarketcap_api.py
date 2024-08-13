import requests
import json

API_KEY = "YOUR FREE COINMARKETCAP API KEY"
# Remember to edit assets.json with your correct criptos symbol and quantity that you have

def fetch_cryptocurrency_data(asset):
    # URL del endpoint
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    # Parámetros de la solicitud
    parameters = {
        'symbol': asset,  
        'convert': 'USD'
    }

    # Encabezados de la solicitud
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY  
    }

    # Realiza la solicitud
    response = requests.get(url, headers=headers, params=parameters)
    data = json.loads(response.text)


    price = data['data'][asset]['quote']['USD']['price']
    rounded_price = round(price, 3)

    return rounded_price



