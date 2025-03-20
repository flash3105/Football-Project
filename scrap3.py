import requests
import json

API_KEY = "ccb787fbc7f9ae85ed84af417347d024"
team_id = 2691  # Kaizer Chiefs team ID
league_id = 288  # Assuming league ID 1 for example; replace with actual league ID if needed

# URL to fetch player statistics (you might need to adjust the endpoint based on your API documentation)
players_url = f"https://v3.football.api-sports.io/players/statistics?team={team_id}&league={league_id}"

headers = {
    "x-apisports-key": API_KEY
}

response = requests.get(players_url, headers=headers)

print(f"Status Code: {response.status_code}")  # Check the status code
if response.status_code == 200:
    data = response.json()
    print("Response Data:", json.dumps(data, indent=4))  # Print the full response data to check

    if 'response' in data and data['response']:
        players_stats = []

        # Extract player data and their stats
        for player in data['response']:
            # Check if statistics are available
            statistics = player.get('statistics', [])
            if statistics:
                stats = statistics[0]  # Assuming we only need the first entry

                player_info = {
                    'player_name': player.get('player', {}).get('name', 'N/A'),
                    'player_id': player.get('player', {}).get('id', 'N/A'),
                    'position': player.get('statistics', [{}])[0].get('games', {}).get('position', 'N/A'),
                    'goals': stats.get('goals', {}).get('total', 0),
                    'assists': stats.get('assists', {}).get('total', 0),
                    'yellow_cards': stats.get('cards', {}).get('yellow', 0),
                    'red_cards': stats.get('cards', {}).get('red', 0),
                    'minutes_played': stats.get('games', {}).get('minutes', 0),
                    'photo': player.get('player', {}).get('photo', 'N/A')
                }
            else:
                # If no statistics are found, return default values
                player_info = {
                    'player_name': player.get('player', {}).get('name', 'N/A'),
                    'player_id': player.get('player', {}).get('id', 'N/A'),
                    'position': 'N/A',
                    'goals': 0,
                    'assists': 0,
                    'yellow_cards': 0,
                    'red_cards': 0,
                    'minutes_played': 0,
                    'photo': 'N/A'
                }

            players_stats.append(player_info)
            # Optionally, print player stats to verify
            print(player_info)

        # Save player stats data to a local JSON file
        with open('kaizer_chiefs_player_stats.json', 'w') as f:
            json.dump(players_stats, f, indent=4)

        print("Player stats saved to kaizer_chiefs_player_stats.json.")
    else:
        print("No player statistics found.")
else:
    print(f"Error: {response.status_code}, {response.text}")
