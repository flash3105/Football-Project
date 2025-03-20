import requests
import json

API_KEY = "ccb787fbc7f9ae85ed84af417347d024"
league_id = 288  # Premier Soccer League ID
season = 2023 # You can use the relevant season here

# Correct endpoint to fetch teams in a league for a specific season
url = f"https://v3.football.api-sports.io/teams?league={league_id}&season={season}"

headers = {
    "x-apisports-key": API_KEY
}

response = requests.get(url, headers=headers)

print(f"Status Code: {response.status_code}")  # Check the status code
if response.status_code == 200:
    data = response.json()
    print("Response Data:", json.dumps(data, indent=4))  # Print the full response data to check
    
    if data['response']:
        teams = []
        
        # Extract team names and IDs
        for team in data['response']:
            team_info = {
                'team_name': team['team']['name'],
                'team_id': team['team']['id']
            }
            teams.append(team_info)
        
        # Save teams data to a local JSON file
        with open('psl_teams.json', 'w') as f:
            json.dump(teams, f, indent=4)
        
        print("Team IDs saved to psl_teams.json.")
    else:
        print("No teams found for the Premier Soccer League.")
else:
    print(f"Error: {response.status_code}, {response.text}")
