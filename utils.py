"""
Created by Neel Gokhale at 2020-09-26
File utils.py from project PokemonCMD
Built using PyCharm

"""

from time import sleep
from random import shuffle, choice

def message(msg: str, typ: str):
    print(f"({typ}) > ", end="")
    for s in msg:
        print(s, end='', flush=True)
        sleep(0.02)


def print_game_title():
    print("""
# 
# 
#  /$$$$$$$           /$$                                                         /$$                  /$$$$$$  /$$      /$$ /$$$$$$$ 
# | $$__  $$         | $$                                                        |__/                 /$$__  $$| $$$    /$$$| $$__  $$
# | $$  \ $$ /$$$$$$ | $$   /$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$        /$$ /$$$$$$$       | $$  \__/| $$$$  /$$$$| $$  \ $$
# | $$$$$$$//$$__  $$| $$  /$$/ /$$__  $$| $$_  $$_  $$ /$$__  $$| $$__  $$      | $$| $$__  $$      | $$      | $$ $$/$$ $$| $$  | $$
# | $$____/| $$  \ $$| $$$$$$/ | $$$$$$$$| $$ \ $$ \ $$| $$  \ $$| $$  \ $$      | $$| $$  \ $$      | $$      | $$  $$$| $$| $$  | $$
# | $$     | $$  | $$| $$_  $$ | $$_____/| $$ | $$ | $$| $$  | $$| $$  | $$      | $$| $$  | $$      | $$    $$| $$\  $ | $$| $$  | $$
# | $$     |  $$$$$$/| $$ \  $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$/| $$  | $$      | $$| $$  | $$      |  $$$$$$/| $$ \/  | $$| $$$$$$$/
# |__/      \______/ |__/  \__/ \_______/|__/ |__/ |__/ \______/ |__/  |__/      |__/|__/  |__/       \______/ |__/     |__/|_______/ 
# 
# 
# 
# 
# 
#                                                      By Neel Gokhale                                                                                                                                                                                                             
    \n""")


def simulate_accuracy(acc_percent):
    if acc_percent is None:
        acc_percent = 0
    acc_list = []
    for i in range(acc_percent):
        acc_list.append(True)
    for i in range(100 - acc_percent):
        acc_list.append(False)
    shuffle(acc_list)
    return choice(acc_list)
