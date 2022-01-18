import random
import requests
from itemClass import Item


def get_items_from_api(lol_version: str) -> list:
    mythic_items = []
    legendary_items = []
    boots_items = []

    response_en = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/en_US/item.json")
    response_pl = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/pl_PL/item.json")

    resp_en = response_en.json()['data']
    resp_pl = response_pl.json()['data']

    for id in resp_en:
        if 'into' not in resp_en[id] and 'from' in resp_en[id] and "Consumable" not in resp_en[id]['tags'] and \
                resp_en[id]['gold'][
                    'purchasable'] and 'Boots' not in resp_en[id]['tags'] and resp_en[id]['name'] != \
                'Mejai\'s Soulstealer':
            if '<rarityMythic>Mythic Passive:</rarityMythic>' in resp_en[id]['description']:
                mythic_items.append(Item(id, resp_en[id]['name'], resp_pl[id]['name']))
            else:
                legendary_items.append(Item(id, resp_en[id]['name'], resp_pl[id]['name']))

        if 'Boots' in resp_en[id]['tags'] and resp_en[id]['gold']['purchasable'] and 'into' not in resp_en[id]:
            boots_items.append(Item(id, resp_en[id]['name'], resp_pl[id]['name']))

    return [mythic_items, legendary_items, boots_items]


def randomize_boots(boots_list) -> Item:
    return random.choice(boots_list)


def randomize_mythic_item(mythic_items_list) -> Item:
    return random.choice(mythic_items_list)


def randomize_legendary_items(legendary_items_list) -> list:
    random_legendary_items = []
    i = 0
    while i < 4:
        random_legendary_item = random.choice(legendary_items_list)
        if random_legendary_item not in random_legendary_items:
            random_legendary_items.append(random_legendary_item)
        else:
            continue
        i += 1
    return random_legendary_items
