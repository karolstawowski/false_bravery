import discord
import random

from champions import getChampionsFromApi
from items import getItemsFromApi
from summonerSpells import getSummonerSpellsFromApi
from images import generateImage

client = discord.Client()

lol_version = "12.1.1"

[mythic_items, legendary_items, boots_items] = getItemsFromApi(lol_version)
champions = getChampionsFromApi(lol_version)
summoner_spells = getSummonerSpellsFromApi(lol_version)

random_legendary_items = []
random_summoner_spells = []

i = 0
while i < 4:
    random_legendary_item = random.choice(list(legendary_items.keys()))
    if random_legendary_item not in random_legendary_items:
        random_legendary_items.append(random_legendary_item)
    else:
        continue
    i += 1

i = 0
while i < 2:
    random_summoner_spell = random.choice(list(summoner_spells.keys()))
    if random_summoner_spell not in random_summoner_spells:
        random_summoner_spells.append(random_summoner_spell)
    else:
        continue
    i += 1

random_boots = random.choice(list(boots_items.keys()))
random_mythic_item = random.choice(list(mythic_items.keys()))

generateImage(random.choice(champions), random_boots, boots_items[random_boots][0], boots_items[random_boots][1],
              random_mythic_item, mythic_items[random_mythic_item][0], mythic_items[random_mythic_item][1],
              random_legendary_items, [legendary_items[i][0] for i in random_legendary_items],
              [legendary_items[i][1] for i in random_legendary_items],
              summoner_spells[random_summoner_spells[0]],
              summoner_spells[random_summoner_spells[1]])

password = open('bot_password.txt', 'r').read()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        # random_champion = randomizeChampion(champions)
        # random_boots = randomizeBoots(boots_items)
        # description = f'Champion: {random_champion} \n Items: \n{random_boots[1]} - {random_boots[2]}'
        # imageURL = f"http://ddragon.leagueoflegends.com/cdn/12.1.1/img/champion/{random_champion}.png"
        # embed = discord.Embed(title=random_champion, description=description)
        # embed.set_image(url=imageURL)
        await message.channel.send(file=discord.File("./assets/ready.png"))

client.run(password)
