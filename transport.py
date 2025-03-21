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

# Function to insert data into MySQL
def insert_player_data(player):
    try:
        connection = connect_to_mysql()
        cursor = connection.cursor()

        query = """
        INSERT INTO players (id, name, firstname, lastname, age, birth_date, 
                             birth_country, nationality, height, weight, number, position, photo_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        data = (
            player['id'],
            player['name'],
            player['firstname'],
            player['lastname'],
            player['age'],
            player['birth'].get('date'),  # Handle missing values
            player['birth'].get('country'),
            player['nationality'],
            player.get('height'),
            player.get('weight'),
            player.get('number'),
            player.get('position'),
            player.get('photo')
        )

        cursor.execute(query, data)
        connection.commit()
        print(f"Player {player['name']} inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Function to read JSON and upload data
def upload_json_to_mysql(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

            # Iterate through the list
            for entry in data:
                if "response" in entry and isinstance(entry["response"], list):
                    for player_data in entry["response"]:
                        if "player" in player_data:
                            insert_player_data(player_data["player"])
                        else:
                            print("Unexpected structure:", player_data)
                else:
                    print("Unexpected JSON structure:", entry)

    except Exception as e:
        print(f"Error reading the JSON file: {e}")

if __name__ == "__main__":
    json_file = 'players_data.json'
    upload_json_to_mysql(json_file)
