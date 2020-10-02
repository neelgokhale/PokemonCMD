"""
Created by Neel Gokhale at 2020-09-27
File setup.py from project PokemonCMD
Built using PyCharm

"""

from utils import *
from player import Player
from time import sleep


def setup(num, party_size):
    print("-----------------------------------------------------------------------------------------------------------\n")
    # setup player
    player = Player()
    if num == 1:
        message(f"Player {num}, what is your name?\n", "?")
    else:
        message(f"Ahh... A new challenger appears! Player {num}, introduce yourself.\n", "!")
    player.player_name = input("    > ENTER NAME: ")
    message(f"Welcome to the game, PKMN trainer {player.player_name}\n", "!")

    # select pokemon
    message("Setting up pokedex...\n", "!")
    sleep(2)
    message("When prompted, enter the name/pokedex number of you pokemon\n", "?")
    player.build_party(party_size)
    player.print_party(party_size)
    print("\n")

    return player
