import requests

def getSummonerSpellsFromApi(lol_version):
    summoner_spells = {}

    response_en = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/en_US/summoner.json")
    response_pl = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/pl_PL/summoner.json")

    resp_en = response_en.json()['data']
    resp_pl = response_pl.json()['data']

    for id in resp_en:
        summoner_spells[id] = [resp_en[id]['name']]
        summoner_spells[id].append(resp_pl[id]['name'])

    print(summoner_spells)

    return summoner_spells