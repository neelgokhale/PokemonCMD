"""
Created by Neel Gokhale at 2020-09-30
File dummy.py from project PokemonCMD
Built using PyCharm

"""
import requests

data = requests.get("https://pokeapi.co/api/v2/type/ground")
data = data.json()

dmg_relations = data['damage_relations']


#double dmg from
for dmg_typ in dmg_relations['double_damage_from']:
    print(dmg_typ['name'])