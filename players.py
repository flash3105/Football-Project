import http.client
import json

# Create a connection to the API host
conn = http.client.HTTPSConnection("v3.football.api-sports.io")


headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "" 
}


conn.request("GET", "/players/profiles?player=296274", headers=headers)


res = conn.getresponse()
data = res.read()

response_data = json.loads(data.decode("utf-8"))
print(json.dumps(response_data, indent=4))  # Pretty-print the response data
