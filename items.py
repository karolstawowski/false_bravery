import requests
# Itemki pod mapy
def getItemsFromApi(lol_version):
    mythicItems = {}
    legendaryItems = {}
    bootsItems = {}

    response_en = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/en_US/item.json")
    response_pl = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/pl_PL/item.json")

    resp_en = response_en.json()['data']
    resp_pl = response_pl.json()['data']

    for id in resp_en:
        if 'into' not in resp_en[id] and 'from' in resp_en[id] and "Consumable" not in resp_en[id]['tags'] and resp_en[id]['gold'][
            'purchasable'] and 'Boots' not in resp_en[id]['tags']:
            if '<rarityMythic>Mythic Passive:</rarityMythic>' in resp_en[id]['description']:
                mythicItems[id] = [resp_en[id]['name']]
                mythicItems[id].append(resp_pl[id]['name'])
            else:
                legendaryItems[id] = [resp_en[id]['name']]
                legendaryItems[id].append(resp_pl[id]['name'])

        if 'Boots' in resp_en[id]['tags'] and resp_en[id]['gold']['purchasable'] and 'into' not in resp_en[id]:
            bootsItems[id] = [resp_en[id]['name']]
            bootsItems[id].append(resp_pl[id]['name'])

    print(mythicItems)
    print(legendaryItems)
    print(bootsItems)

    return [mythicItems, legendaryItems, bootsItems]