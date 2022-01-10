import discord

# client = discord.Client()


import requests
import json

response = requests.get("http://ddragon.leagueoflegends.com/cdn/12.1.1/data/en_US/item.json")

def toprettyjson(obj):
    return json.dumps(obj, sort_keys=True, indent=4)

resp = response.json()['data']

items = []
mythics = {}
legendaries = []
boots = []

for id in resp:
    if 'into' not in resp[id] and 'from' in resp[id] and "Consumable" not in resp[id]['tags'] and resp[id]['gold']['purchasable'] and 'Boots' not in resp[id]['tags']:
        items.append(resp[id]['name'])
        if '<rarityMythic>Mythic Passive:</rarityMythic>' in resp[id]['description']:
            mythics[id] = [resp[id]['name']]
        else:
            legendaries.append(resp[id]['name'])

for i in mythics:
    mythics[i].append('asd')

print(mythics)
print("Items: " + str(len(items)))
print("Mythics: " + str(len(mythics)))
print("Legendaries: " + str(len(legendaries)))

# #
# from PIL import Image
# import urllib.request
#
# urllib.request.urlretrieve(
#   'https://media.geeksforgeeks.org/wp-content/uploads/20210318103632/gfg-300x300.png')
# imgurl = Image.open("gfg.png")
#
# filename = "C:/Pliki/Sandbox/PYTHON/Python Discord Bot/assets/f1.jpg"
# imglocal =  Image.open(filename)
#
# imglocal.paste(imgurl, (50, 50))
# imglocal.save("C:/Pliki/Sandbox/PYTHON/Python Discord Bot/assets/f12.jpg")
# #


# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
#
#
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('$hello'):
#         # for i in range(len(mythicsids)):
#         #     imageURL = f"http://ddragon.leagueoflegends.com/cdn/12.1.1/img/item/{mythicsids[i]}.png"
#         #     embed = discord.Embed(title=mythics[i])
#         #     embed.set_image(url=imageURL)
#         #     await message.channel.send(embed=embed)
#         await message.channel.send(file=discord.File('http://ddragon.leagueoflegends.com/cdn/12.1.1/img/item/101.png'))
#
# client.run("OTI1ODIwNTU1OTc2OTI1MjE0.YcyrlQ.lhxjfnRF-NnKLaeC1PjlMJT6QwU")