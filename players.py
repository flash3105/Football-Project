import http.client
import json
import time

# Create a connection to the API host
conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "ccb787fbc7f9ae85ed84af417347d024"  # Replace with your valid API key
}

# Sample player registration numbers
reg_numbers = {
    296274, 98933
}

# Store all responses in a list
players_data = []

# Example of querying multiple endpoints
endpoints = {
    #"players_profiles": "/players/profiles",
    "players_teams": "/players/teams",
    "fixtures": "/fixtures",
    "fixtures_rounds": "/fixtures/rounds",
    "fixtures_statistics": "/fixtures/statistics",
    "injuries": "/injuries",
    "sidelined": "/sidelined",
    "trophies": "/trophies",
    "odds_live": "/odds/live",
    "teams": "/teams",
    "teams_statistics": "/teams/statistics",
    "fixtures_headtohead": "/fixtures/headtohead",
    "players_squads": "/players/squads",
    "players_topassists": "/players/topassists",
    "players_topyellowcards": "/players/topyellowcards",
    "players_topredcards": "/players/topredcards"
}

# Define a function to fetch data from each endpoint
def fetch_data(endpoint, params=None):
    # Build URL with params if provided
    url = endpoint
    if params:
        url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])
    
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    
    # Parse the response data
    response_data = json.loads(data.decode("utf-8"))
    return response_data

# Fetch data for each endpoint
for player_id in reg_numbers:
    # Example: Fetch player profiles
   # profiles_params = {"player": player_id}
    #profiles_data = fetch_data(endpoints["players_profiles"], profiles_params)
    
    # Example: Fetch player teams and career details
   # teams_params = {"player": player_id}
    #teams_data = fetch_data(endpoints["players_teams"], teams_params)
    
    # Example: Fetch fixtures data
    #ixtures_params = {"team": 2691 , "season": 2023}
   #fixtures_data = fetch_data(endpoints["fixtures"], fixtures_params)
    
    # Example: Fetch player statistics in fixtures
    statistics_params = { "fixture": 1119767}
    statistics_data = fetch_data(endpoints["fixtures_statistics"], statistics_params)

    # Append all fetched data for the current player
    players_data.append({
       #"player_id": player_id,
       # "profiles": profiles_data,
       # "teams": teams_data,
       #"fixtures": fixtures_data,
        "statistics": statistics_data
    })

    # Sleep to avoid hitting the rate limit
    time.sleep(6)

# Close the connection
conn.close()

# Save all responses to a JSON file
with open("stats_data.json", "w", encoding="utf-8") as file:
    json.dump(players_data, file, indent=4)

print("Player data saved to players_data.json")
