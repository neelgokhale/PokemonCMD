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

def do_battle(party_size, player1, player2):
    while len(player1.party) > 0 and len(player2.party) > 0:
        sleep(2)
        print("-----------------------------------------------------------------------------------------------------------\n")
        message(f"PKMN Trainer {player1.player_name}, choose your pokemon for battle\n", "!")
        player1.print_party(party_size)
        player1_pick = -1
        while player1_pick not in [i + 1 for i in range(len(player1.party))]:
            player1_pick = int(input("    > ENTER PKMN NUMBER: "))
        message(f"PKMN Trainer {player2.player_name}, choose your pokemon for battle\n", "!")
        player2.print_party(party_size)
        player2_pick = -1
        while player2_pick not in [i + 1 for i in range(len(player2.party))]:
            player2_pick = int(input("    > ENTER PKMN NUMBER: "))

        player1.party[player1_pick - 1].fight_pokemon(player2.party[player2_pick - 1])
        player1.remove_fainted_pkmn()
        player2.remove_fainted_pkmn()

    if len(player1.party) > len(player2.party):
        print("-----------------------------------------------------------------------------------------------------------\n")
        message(f"The battle is over! PKMN trainer {player1.player_name} has won!", "!")
    elif len(player2.party) > len(player1.party):
        print("-----------------------------------------------------------------------------------------------------------\n")
        message(f"The battle is over! PKMN trainer {player2.player_name} has won!", "!")
    else:
        print("-----------------------------------------------------------------------------------------------------------\n")
        message(f"The battle is over! This is a tie!", "!")
