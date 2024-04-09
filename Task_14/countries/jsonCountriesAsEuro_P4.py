import requests


class CountryInfo:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            self.data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            self.data = None

    def display_euro_countries(self):
        if not hasattr(self, 'data'):
            print("Data not fetched. Call fetch_data method first.")
            return

        euro_countries = []
        for country_data in self.data:
            currencies = country_data.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                if currency_code == 'EUR':
                    euro_countries.append(country_data.get('name', {}).get('common', 'N/A'))
                    break

        if euro_countries:
            print("Countries using Euro as currency:")
            for country in euro_countries:
                print(f"- {country}")
        else:
            print("No countries found using Euro as currency.")


if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    country_info = CountryInfo(url)
    country_info.fetch_data()
    country_info.display_euro_countries()