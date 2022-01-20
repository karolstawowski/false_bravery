import random
from apiHandling import get_json_from_api
from dataTypeClass import Data_type
from localeClass import Locale


def get_champions_from_api(lol_version: str) -> list:
    resp_en = get_json_from_api(lol_version, Data_type.champion, Locale.en_US)

    return [id for id in resp_en]


def randomize_champion(champions_list: list) -> str:
    return random.choice(champions_list)
