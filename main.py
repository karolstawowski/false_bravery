import discord

from champions import getChampionsFromApi, randomizeChampion
from items import getItemsFromApi, randomizeBoots, randomizeMythicItem, randomizeLegendaryItems
from summonerSpells import getSummonerSpellsFromApi, randomizeSummonerSpells
from images import generateImage
from leagueOfLegendsVersion import getLeagueOfLegendsVersion
from skills import randomizeSkillOrder

client = discord.Client()

lol_version = getLeagueOfLegendsVersion()

[mythic_items, legendary_items, boots_items] = getItemsFromApi(lol_version)
champions = getChampionsFromApi(lol_version)
summoner_spells = getSummonerSpellsFromApi(lol_version)

password = open('bot_password.txt', 'r').read()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!aramki'):
        random_legendary_items = randomizeLegendaryItems(legendary_items)
        random_summoner_spells = randomizeSummonerSpells(summoner_spells)
        random_boots = randomizeBoots(boots_items)
        random_mythic_item = randomizeMythicItem(mythic_items)
        random_skill_order = randomizeSkillOrder()
        random_champion = randomizeChampion(champions)

        generateImage(random_champion, random_boots, boots_items[random_boots][0],
                      boots_items[random_boots][1],
                      random_mythic_item, mythic_items[random_mythic_item][0], mythic_items[random_mythic_item][1],
                      random_legendary_items, [legendary_items[i][0] for i in random_legendary_items],
                      [legendary_items[i][1] for i in random_legendary_items],
                      summoner_spells[random_summoner_spells[0]],
                      summoner_spells[random_summoner_spells[1]], random_skill_order)

        await message.reply(file=discord.File("./temp/output_file.png"))

client.run(password)
