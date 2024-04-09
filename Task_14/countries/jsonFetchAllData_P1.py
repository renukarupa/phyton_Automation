import requests

class CountryDataFetcher:

    # default constructor
    def __init__(self, url):
        self.url = url

    # a method for printing data members
    def  fetch_data(self):
        response = requests.get(self.url)
        response.raise_for_status()
        data = response.json()
        return data

# store the URL in url as
url = "https://restcountries.com/v3.1/all"

# creating object of the class
fetcher = CountryDataFetcher(url)
country_data = fetcher.fetch_data()
if country_data:
   print(country_data)




