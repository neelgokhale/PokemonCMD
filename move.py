"""
Created by Neel Gokhale at 2020-10-02
File move.py from project PokemonCMD
Built using PyCharm

"""

import pokebase as pb
import requests
import random


class Move(object):

    def __init__(self, pkmn_move):
        self.name = pkmn_move.name
        self.acc = pkmn_move.accuracy
        self.pwr = 0 if pkmn_move.power is None else pkmn_move.power
        self.pp = pkmn_move.pp
        self.flv_txt_dump = pkmn_move.flavor_text_entries[0].flavor_text
        self.flv_txt = ""
        for i in self.flv_txt_dump:
            if i == "\n":
                i = " "
                self.flv_txt += i
            else:
                self.flv_txt += i

    def move_made(self):
        self.pp -= 1
