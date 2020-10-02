"""
Created by Neel Gokhale at 2020-09-26
File player.py from project PokemonCMD
Built using PyCharm

"""

from utils import *
from pokemon import create_pokemon, generate_moveset, pick_moves, print_moves, Pokemon


class Player(object):

    def __init__(self):
        self.player_name = None
        self.party = []

    def build_party(self, party_size=6):
        for i in range(party_size):
            pkmn = -1
            while pkmn == -1:
                name = input("    > ENTER NAME/NUM: ")
                pkmn = create_pokemon(name)
            message(f"PKMN {pkmn.name} has been added to your party\n", "+")
            pkmn_added = Pokemon(pkmn)
            pkmn_added.populate_moveset()
            print_moves(pkmn_added.moveset)
            self.party.append(pkmn_added)

    def print_party(self, party_size=6):
        if len(self.party):
            message(f"{self.player_name}'s party:\n", "!")
            for i, p in enumerate(self.party):
                print(f"    > ({i + 1}/{party_size}) PKMN {p.name}")

