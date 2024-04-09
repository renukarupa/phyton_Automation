import requests


def display_country_currency(url):
    try:
        response = requests.get(url)
        data = response.json()

        for country_data in data:
            name = country_data.get('name', {}).get('common', 'N/A')
            currencies = country_data.get('currencies', {})

            print(f"Country: {name}")
            print("Currencies:")
            for currency, details in currencies.items():
                #code = details.get('code', 'N/A')
                symbol = details.get('symbol', 'N/A')
                print(f"\tCurrency: {currency}")
                #print(f"\t\tCode: {code}")
                print(f"\t\tSymbol: {symbol}")
            print("-----------------------------------")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    display_country_currency(url)










