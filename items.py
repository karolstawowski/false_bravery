import random
import requests


def getItemsFromApi(lol_version):
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

    # print(mythic_items)
    # print(legendary_items)
    # print(boots_items)

    return [mythic_items, legendary_items, boots_items]


def randomizeBoots(boots):
    boots_id = random.choice(list(boots.keys()))
    boots_name_en = boots[boots_id][0]
    boots_name_pl = boots[boots_id][1]

    return [boots_id, boots_name_en, boots_name_pl]
