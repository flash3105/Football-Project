import json
import mysql.connector

# Load the JSON data
with open("fixtures_statistics.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Establish a connection to MySQL
def connect_to_mysql():
    return mysql.connector.connect(
        host="127.0.0.1",  
        user="root",    
        password="Manqoba2008#",  
        database="player_profiles"
    )
conn = connect_to_mysql()
cursor = conn.cursor()

# SQL query to insert data
sql = """
INSERT INTO fixture_events (
    fixture_id, elapsed_time, extra_time, team_id, team_name, team_logo,
    player_id, player_name, assist_id, assist_name, event_type, event_detail, comments
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Loop through fixtures in JSON
for fixture_id, fixture_data in data.items():
    for event in fixture_data["response"]:
        values = (
            fixture_id,
            event["time"]["elapsed"],
            event["time"]["extra"],
            event["team"]["id"],
            event["team"]["name"],
            event["team"]["logo"],
            event["player"]["id"] if event["player"] else None,
            event["player"]["name"] if event["player"] else None,
            event["assist"]["id"] if event["assist"] else None,
            event["assist"]["name"] if event["assist"] else None,
            event["type"],
            event["detail"],
            event["comments"]
        )
        
        cursor.execute(sql, values)

# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully!")
