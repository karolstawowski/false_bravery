import random
import requests


def get_items_from_api(lol_version) -> list:
    mythic_items = {}
    legendary_items = {}
    boots_items = {}

    response_en = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/en_US/item.json")
    response_pl = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/pl_PL/item.json")

    resp_en = response_en.json()['data']
    resp_pl = response_pl.json()['data']

    for id in resp_en:
        if 'into' not in resp_en[id] and 'from' in resp_en[id] and "Consumable" not in resp_en[id]['tags'] and \
                resp_en[id]['gold'][
                    'purchasable'] and 'Boots' not in resp_en[id]['tags'] and resp_en[id][
            'name'] != 'Mejai\'s Soulstealer':
            if '<rarityMythic>Mythic Passive:</rarityMythic>' in resp_en[id]['description']:
                mythic_items[id] = [resp_en[id]['name'], resp_pl[id]['name']]
            else:
                legendary_items[id] = [resp_en[id]['name'], resp_pl[id]['name']]

        if 'Boots' in resp_en[id]['tags'] and resp_en[id]['gold']['purchasable'] and 'into' not in resp_en[id]:
            boots_items[id] = [resp_en[id]['name'], resp_pl[id]['name']]

    return [mythic_items, legendary_items, boots_items]


def randomize_boots(boots_dictionary) -> list:
    return random.choice(list(boots_dictionary.keys()))


def randomize_mythic_item(mythic_items_dictionary) -> list:
    return random.choice(list(mythic_items_dictionary.keys()))


def randomize_legendary_items(legendary_items_dictionary) -> list:
    random_legendary_items = []
    i = 0
    while i < 4:
        random_legendary_item = random.choice(list(legendary_items_dictionary.keys()))
        if random_legendary_item not in random_legendary_items:
            random_legendary_items.append(random_legendary_item)
        else:
            continue
        i += 1
    return random_legendary_items
