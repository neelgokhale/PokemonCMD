"""
Created by Neel Gokhale at 2020-09-18
File main.py from project PokemonCMD
Built using PyCharm

"""
from utils import *
from time import sleep
from setup import setup, do_battle


def main():
    # welcome message
    print_game_title()
    sleep(1)
    message("Welcome to the Pokemon Game!\n", "!")

    # setup party size
    message("What is the preferred party size (max is 6 pokemons)?\n", "?")
    run_party_size = True
    while run_party_size:
        party_size = int(input("    > PARTY SIZE: "))
        if type(party_size) is int and party_size < 7:
            run_party_size = False
        else:
            run_party_size = True

    # setup players
    player_1 = setup(1, party_size)
    player_2 = setup(2, party_size)

    do_battle(party_size, player_1, player_2)


if __name__ == '__main__':
    main()
