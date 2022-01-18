import requests
import random
from summonerSpellClass import SummonerSpell


def get_summoner_spells_from_api(lol_version) -> dict:
    summoner_spells = {}

    response_en = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/en_US/summoner.json")
    response_pl = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/pl_PL/summoner.json")

    resp_en = response_en.json()['data']
    resp_pl = response_pl.json()['data']

    for id in resp_en:
        if 'CLASSIC' in resp_en[id]['modes'] and resp_en[id]['name'] != 'Smite':
            summoner_spells[id] = SummonerSpell(id, resp_en[id]['name'], resp_pl[id]['name'], resp_en[id]['image']['x'],
                                                resp_en[id]['image']['y'], resp_en[id]['image']['w'],
                                                resp_en[id]['image']['h'])

    return summoner_spells


def randomize_summoner_spells(summoner_spells_dictionary) -> list:
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
