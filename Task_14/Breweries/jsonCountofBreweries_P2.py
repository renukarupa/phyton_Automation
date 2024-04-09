import requests

def get_brewery_count_by_state(states):
    try:
        url = "https://api.openbrewerydb.org/breweries"
        response = requests.get(url)
        data = response.json()

        state_counts = {}
        for brewery in data:
            if brewery['state'] in states:
                state = brewery['state']
                if state in state_counts:
                    state_counts[state] += 1
                else:
                    state_counts[state] = 1

        return state_counts

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return {}


if __name__ == "__main__":
    states = ['Alaska', 'Maine', 'New York']
    brewery_counts = get_brewery_count_by_state(states)
    print("Brewery counts in the states of Alaska, Maine, and New York:")
    for state, count in brewery_counts.items():
        print(f"{state}: {count}")