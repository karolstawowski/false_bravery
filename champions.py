import random
import requests


def getChampionsFromApi(lol_version):
    champions = []

    response_en = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/en_US/champion.json")

    resp_en = response_en.json()['data']

    for id in resp_en:
        champions.append(id)

    # print(champions)

    return champions


def randomizeChampion(champions_list):
    return random.choice(champions_list)
