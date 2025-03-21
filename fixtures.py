import http.client
import json
import time

# Create a connection to the API host
conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "ccb787fbc7f9ae85ed84af417347d024"  # Replace with your valid API key
}

# Define the endpoint for fixture statistics
endpoint_fixtures_statistics = "/fixtures"

# Define the fixture ID to fetch statistics for
fixture_id = 1104071 #e with your desired fixture ID

# Function to fetch fixture statistics
def fetch_fixture_statistics(fixture_id):
    url = f"{endpoint_fixtures_statistics}?fixture={fixture_id}"
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    # Parse response data
    response_data = json.loads(data.decode("utf-8"))
    return response_data

# Fetch fixture statistics
fixture_statistics = fetch_fixture_statistics(fixture_id)

# Close the connection
conn.close()

# Save response to a JSON file
with open("fixture_statistics.json", "w", encoding="utf-8") as file:
    json.dump(fixture_statistics, file, indent=4)

print("Fixture statistics saved to fixture_statistics.json")
