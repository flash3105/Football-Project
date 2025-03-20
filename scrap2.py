import requests

# Replace with your actual API URL and key
url = "https://api.example.com/players/squads"
params = {
    "team": "2691",  # Team ID (Kaizer Chiefs)
    "season": "2023"  # Season
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code == 200 and data['results'] > 0:
    players = data['response']
    for player in players:
        player_name = player['name']
        player_age = player['age']
        player_number = player['number']
        player_position = player['position']
        player_photo = player['photo']

        # Assuming you also want to extract stats like goals, assists, etc.
        player_stats = player.get('statistics', {})
        goals = player_stats.get('goals', 'N/A')
        assists = player_stats.get('assists', 'N/A')
        appearances = player_stats.get('appearances', 'N/A')

        print(f"Name: {player_name}, Age: {player_age}, Position: {player_position}")
        print(f"Goals: {goals}, Assists: {assists}, Appearances: {appearances}")
        print(f"Photo URL: {player_photo}")
        print("-" * 50)
else:
    print(f"Error: {data.get('errors', 'Unknown error')}")
