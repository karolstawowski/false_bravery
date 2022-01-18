import random
import requests


def get_champions_from_api(lol_version: str) -> list:
    response_en = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/en_US/champion.json")

    resp_en = response_en.json()['data']

    champions = [id for id in resp_en]

    return champions


def randomize_champion(champions_list: list) -> str:
    return random.choice(champions_list)
