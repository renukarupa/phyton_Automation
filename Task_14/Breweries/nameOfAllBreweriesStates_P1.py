import requests


def get_breweries_in_states(states):
    try:
        url = "https://api.openbrewerydb.org/breweries"
        response = requests.get(url)
        data = response.json()

        breweries = []
        for brewery in data:
            if brewery['state'] in states:
                breweries.append(brewery['name'])

        return breweries

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []


if __name__ == "__main__":
    states = ['Alaska', 'Maine', 'New York']
    breweries = get_breweries_in_states(states)
    print("Breweries in the states of Alaska, Maine, and New York:")
    for brewery in breweries:
        print("-", brewery)