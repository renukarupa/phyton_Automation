import requests

def count_brewery_types_by_city(state):
    # Fetch data from Open Brewery DB API
    url = f"https://api.openbrewerydb.org/breweries"  # Limiting to 50 breweries per page
    response = requests.get(url)
    breweries = response.json()

    # Create a dictionary to store counts of brewery types for each city
    city_brewery_types = {}

    # Iterate over each brewery
    for brewery in breweries:
        city = brewery['city']
        brewery_type = brewery['brewery_type']

        # Check if the city already exists in the dictionary
        if city in city_brewery_types:
            # Increment count for the brewery type if city exists
            if brewery_type in city_brewery_types[city]:
                city_brewery_types[city][brewery_type] += 1
            else:
                city_brewery_types[city][brewery_type] = 1
        else:
            # Add city to the dictionary if not already present
            city_brewery_types[city] = {brewery_type: 1}

    # Print the results
    for city, brewery_types in city_brewery_types.items():
        print(f"City: {city}")
        for brewery_type, count in brewery_types.items():
            print(f"- {brewery_type}: {count}")
        print()

# Example usage
state = "California"
count_brewery_types_by_city(state)