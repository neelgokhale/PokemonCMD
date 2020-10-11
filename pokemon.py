"""
Created by Neel Gokhale at 2020-09-27
File pokemon.py from project PokemonCMD
Built using PyCharm

"""

import pokebase as pb
import requests
import random
from move import Move
from utils import message, simulate_accuracy
from time import sleep

class Pokemon(object):

    def __init__(self, pkmn):
        self.pkmn = pkmn
        self.name = pkmn.name
        self.health = pkmn.stats[0].base_stat
        self.moveset = []
        self.damage_to = None
        self.damage_from = None
        self.fainted = False

    def populate_moveset(self):
        move_list = generate_moveset(self.pkmn)
        picked_move_list = pick_moves(move_list, self.pkmn)
        for m in picked_move_list:
            self.moveset.append(Move(m))

    def factor_type_advantages(self, pkmn2):
        damage_dict = damage_multiplier(self.pkmn, pkmn2.pkmn)
        self.damage_to = damage_dict[self.name]['to']
        self.damage_from = damage_dict[self.name]['from']
        damage_dict = damage_multiplier(pkmn2.pkmn, self.pkmn)
        pkmn2.damage_to = damage_dict[pkmn2.name]['to']
        pkmn2.damage_to = damage_dict[pkmn2.name]['from']

    def has_fainted(self):
        self.fainted = True

    def fight_pokemon(self, pkmn2):
        message("Battle Stage!!!\n", "*")
        message(f"PKMN {self.name} V.S. PKMN {pkmn2.name}\n", "*")
        print(f"    > {self.name}: {self.health} HP")
        print(f"    > {pkmn2.name}: {pkmn2.health} HP")

        while (self.health > 0) and (pkmn2.health > 0):

            #PKMN 1 turn
            self.factor_type_advantages(pkmn2)
            message(f"PKMN {self.name}, make your move\n", "?")
            print_moves(self.moveset)
            pkmn1_choice = -1
            while pkmn1_choice not in [1, 2, 3, 4]:
                pkmn1_choice = int(input("    > ENTER MOVE NUMBER: "))
                if self.moveset[pkmn1_choice - 1].pp > 0:
                    pkmn1_choice = pkmn1_choice
                else:
                    pkmn1_choice = -1
            message(f"PKMN {self.name} used {self.moveset[pkmn1_choice - 1].name}. " + f"{self.moveset[pkmn1_choice - 1].flv_txt}.\n", "*")

            if simulate_accuracy(self.moveset[pkmn1_choice - 1].acc):
                pkmn2.health -= self.moveset[pkmn1_choice - 1].pwr * self.damage_to
            else:
                message(f"PKMN {self.name} missed!\n", "*")
            self.moveset[pkmn1_choice - 1].move_made()
            pkmn1_choice = -1
            sleep(1)

            print(f"    > {self.name}: {self.health} HP")
            print(f"    > {pkmn2.name}: {pkmn2.health} HP")

            if pkmn2.health <= 0:
                pkmn2.has_fainted()
                message(f"PKMN {pkmn2.name} has fainted...\n", "*")
                break

            #PKMN 2 turn
            message(f"PKMN {pkmn2.name}, make your move\n", "?")
            print_moves(pkmn2.moveset)
            pkmn2_choice = -1
            while pkmn2_choice not in [1, 2, 3, 4]:
                pkmn2_choice = int(input("    > ENTER MOVE NUMBER: "))
                if pkmn2.moveset[pkmn2_choice - 1].pp > 0:
                    pkmn2_choice = pkmn2_choice
                else:
                    pkmn2_choice = -1
            message(f"PKMN {pkmn2.name} used {pkmn2.moveset[pkmn2_choice - 1].name}. " + f"{pkmn2.moveset[pkmn2_choice - 1].flv_txt}.\n", "*")

            if simulate_accuracy(pkmn2.moveset[pkmn2_choice - 1].acc):
                self.health -= pkmn2.moveset[pkmn2_choice - 1].pwr * pkmn2.damage_to
            else:
                message(f"PKMN {pkmn2.name} missed!\n", "*")
            pkmn2.moveset[pkmn2_choice - 1].move_made()
            pkmn2_choice = -1
            sleep(1)

            print(f"    > {self.name}: {self.health} HP")
            print(f"    > {pkmn2.name}: {pkmn2.health} HP")

            if self.health <= 0:
                self.has_fainted()
                message(f"PKMN {self.name} has fainted...\n", "*")
                break


def create_pokemon(name_or_id):
    if name_or_id.isnumeric():
        name_or_id = int(name_or_id)
    elif type(name_or_id) is str and len(name_or_id) > 0:
        name_or_id = name_or_id.lower()
    else:
        return -1
    pokemon = pb.pokemon(name_or_id)
    try:
        test = pokemon.base_experience
    except:
        return -1
    return pokemon


def generate_moveset(party_pkmn):
    all_moves = party_pkmn.moves
    pkmn_moveset = []
    for m in all_moves:
        lvl_learned_at = m.version_group_details[0].level_learned_at
        if 0 < lvl_learned_at:
            pkmn_moveset.append(m.move.name)
    return pkmn_moveset


def pick_moves(moveset, party_pkmn):
    final_moveset = []
    base_exp = party_pkmn.base_experience
    if len(moveset) < 4:
        for m in moveset:
            final_moveset.append(pb.move(m))
        return final_moveset
    else:
        exclusion_list = []
        if base_exp < 100:
            for i in range(4):
                final_moveset.append(pb.move(moveset[i]))
            return final_moveset
        elif 200 > base_exp >= 100:
            for i in range(4):
                rand_choice = random.choice(moveset)
                exclusion_list.append(rand_choice)
                final_moveset.append(pb.move(rand_choice))
                moveset = [i for i in moveset if i not in exclusion_list]
            return final_moveset
        elif base_exp >= 200:
            for i in reversed(range(1, 5)):
                final_moveset.append(pb.move(moveset[-i]))
            return final_moveset


def print_moves(moveset):
    for i, m in enumerate(moveset):
        acc = m.acc
        pwr = "--" if m.pwr == 0 else m.pwr
        pp = m.pp
        print(f"    <move {i+1}> {m.name} [ acc: {acc} / pwr: {pwr} / pp: {pp} ]")


def damage_multiplier(pkmn1, pkmn2):
    dmg_dict = {}
    pkmn1_types = [t.type.name for t in pkmn1.types]
    pkmn2_types = [t.type.name for t in pkmn2.types]
    pkmn1_dmg_to = []
    pkmn1_dmg_from = []
    pkmn2_dmg_to = []
    pkmn2_dmg_from = []

    # dmg multiplier for pkmn1
    for t in pkmn1_types:

        data = requests.get("https://pokeapi.co/api/v2/type/" + t)
        data = data.json()
        dmg_relations = data['damage_relations']

        for dmg_typ in dmg_relations['no_damage_to']:
            if dmg_typ['name'] in pkmn2_types:
                pkmn1_dmg_to.append(0)
        for dmg_typ in dmg_relations['half_damage_to']:
            if dmg_typ['name'] in pkmn2_types:
                pkmn1_dmg_to.append(0.5)
        for dmg_typ in dmg_relations['double_damage_to']:
            if dmg_typ['name'] in pkmn2_types:
                pkmn1_dmg_to.append(2)
        for dmg_typ in dmg_relations['no_damage_from']:
            if dmg_typ['name'] in pkmn2_types:
                pkmn1_dmg_from.append(0)
        for dmg_typ in dmg_relations['half_damage_from']:
            if dmg_typ['name'] in pkmn2_types:
                pkmn1_dmg_from.append(0.5)
        for dmg_typ in dmg_relations['double_damage_from']:
            if dmg_typ['name'] in pkmn2_types:
                pkmn1_dmg_from.append(2)

    # dmg multiplier for pkmn2
    for t in pkmn2_types:

        data = requests.get("https://pokeapi.co/api/v2/type/" + t)
        data = data.json()
        dmg_relations = data['damage_relations']

        for dmg_typ in dmg_relations['no_damage_to']:
            if dmg_typ['name'] in pkmn1_types:
                pkmn2_dmg_to.append(0)
        for dmg_typ in dmg_relations['half_damage_to']:
            if dmg_typ['name'] in pkmn1_types:
                pkmn2_dmg_to.append(0.5)
        for dmg_typ in dmg_relations['double_damage_to']:
            if dmg_typ['name'] in pkmn1_types:
                pkmn2_dmg_to.append(2)
        for dmg_typ in dmg_relations['no_damage_from']:
            if dmg_typ['name'] in pkmn1_types:
                pkmn2_dmg_from.append(0)
        for dmg_typ in dmg_relations['half_damage_from']:
            if dmg_typ['name'] in pkmn1_types:
                pkmn2_dmg_from.append(0.5)
        for dmg_typ in dmg_relations['double_damage_from']:
            if dmg_typ['name'] in pkmn1_types:
                pkmn2_dmg_from.append(2)

    if not pkmn1_dmg_to:
        pkmn1_dmg_to = 1
    else:
        pkmn1_dmg_to = sum(pkmn1_dmg_to) / len(pkmn1_dmg_to)
    if not pkmn1_dmg_from:
        pkmn1_dmg_from = 1
    else:
        pkmn1_dmg_from = sum(pkmn1_dmg_from) / len(pkmn1_dmg_from)

    if not pkmn2_dmg_to:
        pkmn2_dmg_to = 1
    else:
        pkmn2_dmg_to = sum(pkmn2_dmg_to) / len(pkmn2_dmg_to)
    if not pkmn2_dmg_from:
        pkmn2_dmg_from = 1
    else:
        pkmn2_dmg_from = sum(pkmn2_dmg_from) / len(pkmn2_dmg_from)

    dmg_dict[pkmn1.name] = {"to": pkmn1_dmg_to, "from": pkmn1_dmg_from}
    dmg_dict[pkmn2.name] = {"to": pkmn2_dmg_to, "from": pkmn2_dmg_from}

    return dmg_dict


if __name__ == '__main__':
    pokemon1 = pb.pokemon("rayquaza")
    pokemon2 = pb.pokemon("charizard")
    rayquaza = Pokemon(pokemon1)
    print(rayquaza.name)
    print(rayquaza.health)
    rayquaza.populate_moveset()
    print_moves(rayquaza.moveset)