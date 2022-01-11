import requests
from summonerSpellClass import SummonerSpell


def getSummonerSpellsFromApi(lol_version):
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

    print(summoner_spells)

    return summoner_spells
