import requests
import random
from primaryRuneClass import PrimaryRune
from runeTreeClass import RuneTree


def getRunesFromApi(lol_version):
    primary_runes = []
    rune_trees = []

    response_en = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/en_US/runesReforged.json')

    resp_en = response_en.json()

    for tree in resp_en:
        # print(tree)
        rune_trees.append(RuneTree(tree['name'], tree['icon']))
        # print(tree['name'], tree['icon'])
        for rune in tree['slots'][0]['runes']:
            primary_runes.append(PrimaryRune(rune['key'], rune['icon'], tree['name']))
            # print(rune['key'], rune['icon'], tree['name'])
    # print(primary_runes)
    return [primary_runes, rune_trees]


def randomizePrimaryRune(runes_list):
    return random.choice(runes_list)


def randomizeRuneTree(random_primary_rune, rune_trees_list):
    random_rune_tree = random.choice(rune_trees_list)
    while random_primary_rune.tree == random_rune_tree.key:
        random_rune_tree = random.choice(rune_trees_list)
    return random_rune_tree
