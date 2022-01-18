import random
import requests


def get_champions_from_api(lol_version):
    champions = []

    response_en = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/en_US/champion.json")

    resp_en = response_en.json()['data']

    for id in resp_en:
        champions.append(id)

    return champions


def randomize_champion(champions_list):
    return random.choice(champions_list)
