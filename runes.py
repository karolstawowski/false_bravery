import requests
import random


def getRunesFromApi(lol_version):
    runes = {}

    response_en = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/en_US/runesReforged.json')

    resp_en = response_en.json()

    for tree in resp_en:
        for rune in tree['slots'][0]['runes']:
            runes[rune['key']] = rune['icon']

    # print(runes)

    return runes


def randomizeRune(runes_list):
    random_rune_name = random.choice(list(runes_list.keys()))
    return [random_rune_name, runes_list[random_rune_name]]
