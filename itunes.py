import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
#print(response.json())
#print(json.dumps(response.json(), indent = 5))

ob = response.json()

for result in ob["results"]:
    print(result["trackName"])
