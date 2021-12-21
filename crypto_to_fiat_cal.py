
import sys, os
from os.path import dirname, join, abspath
import requests, json

def get_price_from_third_party(from_currency):
    try: 
        if(from_currency):
            uri = 'https://api.coingecko.com/api/v3/coins/'
            url = uri+from_currency
            response = requests.get(url)
            if response.status_code == 200:
                response_data = response.content.decode('UTF-8')
                data = json.loads(response_data)
                market_data = data.get('market_data')
                currencies_price = market_data.get('current_price')
                return currencies_price

    except Exception as e:
        return False



def convert_crypto_to_fiat(from_currency, to_currency, value):
    try:
        print("****************************************************")
        price_data = get_price_from_third_party(from_currency)
        if(price_data):
            from_currency_current_price = price_data.get(to_currency)
            to_amount = str(format(float(value)*float(from_currency_current_price), '.8f'))
            print(f"Converting From :{value} eth to {to_currency}")
            print(f"Calculating: {value} * {from_currency_current_price} = {to_amount}")

            result_data =  {
            'fromAmount' : value,
            'toAmount' : to_amount,
            'fromCurrency' : from_currency,
            'toCurrency' : to_currency,
            'price' :from_currency_current_price
        }

        print(result_data)
    except Exception as e:
        return False


convert_crypto_to_fiat(from_currency='ethereum', to_currency='usd', value=0.11)