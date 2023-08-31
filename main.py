import requests
import json

def scrape_charging_stations():
    url = 'https://dataspace.mobi/api/3/action/datastore_search?resource_id=f39bb18a-bf5b-4e93-a22e-91f13b2ad9a7&limit=5'  # Replace this with the actual charging station JSON API URL
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for successful response
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

    try:
        charging_stations = json.loads(response.text)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return None

    return charging_stations

if __name__ == "__main__":
    charging_stations_data = scrape_charging_stations()
    if charging_stations_data:
        for station in charging_stations_data:
            print(station)
    else:
        print("No charging station data available.")
