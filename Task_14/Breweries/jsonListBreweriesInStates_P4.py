import requests

def count_breweries_with_websites(states):
    for state in states:
        # Fetch data from Open Brewery DB API for the state
        url = "https://api.openbrewerydb.org/breweries?by_state={state}"
        response = requests.get(url)
        breweries = response.json()

        # Count the number of breweries with websites
        breweries_with_websites = sum(1 for brewery in breweries if brewery['website_url'])

        # Print the result
        print("In {state}, there are {breweries_with_websites} breweries with websites.")

# States of interest
states_of_interest = ["Alaska", "Maine", "New York"]
count_breweries_with_websites(states_of_interest)