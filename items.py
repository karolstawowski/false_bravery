import random
from apiHandling import get_json_from_api
from dataTypeClass import Data_type
from itemClass import Item
from localeClass import Locale


def get_items_from_api(lol_version: str) -> list:
    mythic_items = []
    legendary_items = []
    boots_items = []

    resp_en = get_json_from_api(lol_version, Data_type.item, Locale.en_US)
    resp_pl = get_json_from_api(lol_version, Data_type.item, Locale.pl_PL)

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
