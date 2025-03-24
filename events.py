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
endpoint_fixtures_statistics = "/fixtures/events"

# List of fixture IDs
fixture_ids = [
    1100220, 1104071, 1104076, 1104088, 1104093, 1104102, 1104110, 1104119, 1104125, 
    1104131, 1104141, 1104151, 1104155, 1104167, 1104171, 1104183, 1104193, 1104195, 
    1104208, 1104214, 1104220, 1104226, 1104234, 1104243, 1104251, 1104259, 1104269, 
    1104275, 1104285, 1104292, 1104299, 1119766, 1119767, 1138924, 1172434
]

# Function to fetch fixture statistics
def fetch_fixture_statistics(fixture_id):
    url = f"{endpoint_fixtures_statistics}?fixture={fixture_id}"
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    # Parse response data
    response_data = json.loads(data.decode("utf-8"))
    return response_data

# Dictionary to store all fixture statistics
all_fixtures_statistics = {}

# Loop through all fixture IDs and fetch data
for fixture_id in fixture_ids:
    print(f"Fetching data for fixture ID: {fixture_id}")
    try:
        fixture_statistics = fetch_fixture_statistics(fixture_id)
        all_fixtures_statistics[fixture_id] = fixture_statistics
        time.sleep(1)  # Sleep to avoid rate limiting
    except Exception as e:
        print(f"Error fetching data for fixture {fixture_id}: {e}")

# Close the connection
conn.close()

# Save response to a JSON file
with open("fixtures_statistics.json", "w", encoding="utf-8") as file:
    json.dump(all_fixtures_statistics, file, indent=4)

print("All fixture statistics saved to fixtures_statistics.json")
