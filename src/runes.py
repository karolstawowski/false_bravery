import random

from api_handling import get_json_from_api
from data_type_class import Data_type
from locale_class import Locale
from primary_rune_class import PrimaryRune
from rune_tree_class import RuneTree


def get_runes_from_api(lol_version: str) -> list:
    primary_runes = []
    rune_trees = []

    resp_en = get_json_from_api(lol_version, Data_type.rune, Locale.en_US)

    for tree in resp_en:
        rune_trees.append(RuneTree(tree["name"], tree["icon"]))
        for rune in tree["slots"][0]["runes"]:
            primary_runes.append(PrimaryRune(rune["key"], rune["icon"], tree["name"]))
    return [primary_runes, rune_trees]


def randomize_primary_rune(runes_list: list) -> PrimaryRune:
    return random.choice(runes_list)


def randomize_rune_tree(
    random_primary_rune: PrimaryRune, rune_trees_list: list
) -> RuneTree:
    random_rune_tree = random.choice(rune_trees_list)
    while random_primary_rune.rune_tree == random_rune_tree.key:
        random_rune_tree = random.choice(rune_trees_list)
    return random_rune_tree
