"""
Created by Neel Gokhale at 2020-09-26
File utils.py from project PokemonCMD
Built using PyCharm

"""

from time import sleep


def message(msg: str, typ: str):
    print(f"({typ}) > ", end="")
    for s in msg:
        print(s, end='', flush=True)
        sleep(0.05)


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

