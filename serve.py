import json
from game import Game


# lemos o JSON em disco
json_string = open('teams.json').read()

parsed_json = json.loads(json_string)


print(parsed_json[0]['name'])

Game(
    parsed_json[0]['name'],
    parsed_json[1]['name'],
    1,
    "Campeonato Brasileiro"
)
