import random

from api_handling import get_json_from_api
from data_type_class import Data_type
from locale_class import Locale
from summoner_spell_class import SummonerSpell


def get_summoner_spells_from_api(lol_version: str) -> dict:
    summoner_spells = {}

    resp_en = get_json_from_api(lol_version, Data_type.summoner_spell, Locale.en_US)
    resp_pl = get_json_from_api(lol_version, Data_type.summoner_spell, Locale.pl_PL)

    for id in resp_en:
        if "CLASSIC" in resp_en[id]["modes"] and resp_en[id]["name"] != "Smite":
            summoner_spells[id] = SummonerSpell(
                id,
                resp_en[id]["name"],
                resp_pl[id]["name"],
                resp_en[id]["image"]["x"],
                resp_en[id]["image"]["y"],
                resp_en[id]["image"]["w"],
                resp_en[id]["image"]["h"],
            )

    return summoner_spells


def randomize_summoner_spells(summoner_spells_dictionary: dict) -> list:
    random_summoner_spells = []
    i = 0
    while i < 2:
        random_summoner_spell = random.choice(list(summoner_spells_dictionary.keys()))
        if random_summoner_spell not in random_summoner_spells:
            random_summoner_spells.append(random_summoner_spell)
        else:
            continue
        i += 1
    return random_summoner_spells
