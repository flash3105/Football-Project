import mysql.connector
import json

# MySQL database connection
def connect_to_mysql():
    return mysql.connector.connect(
        host="127.0.0.1",  
        user="root",    
        password="Manqoba2008#",  
        database="player_profiles"
    )

# Load JSON Data
with open("stats_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)


#print(type(data))  # Check if it's a list or dictionary
#print(data[:2])  
# Connect to MySQL
conn = connect_to_mysql()
cursor = conn.cursor()

# SQL Insert Query with INSERT IGNORE
sql = """
INSERT IGNORE INTO season_fixtures (
    fixture_id, league_id, league_name, country, league_logo, country_flag, 
    season_year, round, standings, referee, timezone, match_date, timestamp, 
    venue_id, venue_name, city, status_long, status_short, elapsed, 
    home_team_id, home_team_name, home_team_logo, 
    away_team_id, away_team_name, away_team_logo, 
    winner_team_id, home_goals, away_goals, 
    halftime_home, halftime_away, fulltime_home, fulltime_away, 
    extratime_home, extratime_away, penalty_home, penalty_away
) VALUES (
    %(fixture_id)s, %(league_id)s, %(league_name)s, %(country)s, %(league_logo)s, %(country_flag)s, 
    %(season_year)s, %(round)s, %(standings)s, %(referee)s, %(timezone)s, %(match_date)s, %(timestamp)s, 
    %(venue_id)s, %(venue_name)s, %(city)s, %(status_long)s, %(status_short)s, %(elapsed)s, 
    %(home_team_id)s, %(home_team_name)s, %(home_team_logo)s, 
    %(away_team_id)s, %(away_team_name)s, %(away_team_logo)s, 
    %(winner_team_id)s, %(home_goals)s, %(away_goals)s, 
    %(halftime_home)s, %(halftime_away)s, %(fulltime_home)s, %(fulltime_away)s, 
    %(extratime_home)s, %(extratime_away)s, %(penalty_home)s, %(penalty_away)s
);
"""

# Insert Data into MySQL
# Iterate over the list
for item in data:
    fixtures = item["fixtures"]["response"]  # Access "response" inside "fixtures"
    for fixture in fixtures:
        fixture_data = {
            "fixture_id": fixture["fixture"]["id"],
            "league_id": fixture["league"]["id"],
            "league_name": fixture["league"]["name"],
            "country": fixture["league"]["country"],
            "league_logo": fixture["league"]["logo"],
            "country_flag": fixture["league"]["flag"],
            "season_year": fixture["league"]["season"],
            "round": fixture["league"]["round"],
            "standings": fixture["league"]["standings"],

            "referee": fixture["fixture"].get("referee"),
            "timezone": fixture["fixture"]["timezone"],
            "match_date": fixture["fixture"]["date"],
            "timestamp": fixture["fixture"]["timestamp"],
            
            "venue_id": fixture["fixture"]["venue"].get("id"),
            "venue_name": fixture["fixture"]["venue"].get("name"),
            "city": fixture["fixture"]["venue"].get("city"),

            "status_long": fixture["fixture"]["status"]["long"],
            "status_short": fixture["fixture"]["status"]["short"],
            "elapsed": fixture["fixture"]["status"]["elapsed"],

            "home_team_id": fixture["teams"]["home"]["id"],
            "home_team_name": fixture["teams"]["home"]["name"],
            "home_team_logo": fixture["teams"]["home"]["logo"],

            "away_team_id": fixture["teams"]["away"]["id"],
            "away_team_name": fixture["teams"]["away"]["name"],
            "away_team_logo": fixture["teams"]["away"]["logo"],

            "winner_team_id": fixture["teams"]["home"]["id"] if fixture["teams"]["home"]["winner"] else
                            fixture["teams"]["away"]["id"] if fixture["teams"]["away"]["winner"] else None,

            "home_goals": fixture["goals"]["home"],
            "away_goals": fixture["goals"]["away"],

            "halftime_home": fixture["score"]["halftime"]["home"],
            "halftime_away": fixture["score"]["halftime"]["away"],
            "fulltime_home": fixture["score"]["fulltime"]["home"],
            "fulltime_away": fixture["score"]["fulltime"]["away"],

            "extratime_home": fixture["score"]["extratime"]["home"],
            "extratime_away": fixture["score"]["extratime"]["away"],
            "penalty_home": fixture["score"]["penalty"]["home"],
            "penalty_away": fixture["score"]["penalty"]["away"]
        }
        
        try:
            cursor.execute(sql, fixture_data)
        except mysql.connector.Error as err:
            print(f"Error inserting fixture {fixture_data['fixture_id']}: {err}")

# Commit and Close
conn.commit()
cursor.close()
conn.close()

print("✅ Data inserted successfully!")
