import os
import ssl
import discord
from champions import getChampionsFromApi, randomizeChampion
from items import getItemsFromApi, randomizeBoots, randomizeMythicItem, randomizeLegendaryItems
from summonerSpells import getSummonerSpellsFromApi, randomizeSummonerSpells
from images import generateImage
from leagueOfLegendsVersion import getLeagueOfLegendsVersion
from skills import randomizeSkillOrder
from runes import getRunesFromApi, randomizeRune

if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
    ssl._create_default_https_context = ssl._create_unverified_context

client = discord.Client()

lol_version = getLeagueOfLegendsVersion()

[mythic_items, legendary_items, boots_items] = getItemsFromApi(lol_version)
champions = getChampionsFromApi(lol_version)
summoner_spells = getSummonerSpellsFromApi(lol_version)
runes = getRunesFromApi(lol_version)

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
        random_rune = randomizeRune(runes)

        generateImage(random_champion, random_boots, boots_items[random_boots][0],
                      boots_items[random_boots][1],
                      random_mythic_item, mythic_items[random_mythic_item][0], mythic_items[random_mythic_item][1],
                      random_legendary_items, [legendary_items[i][0] for i in random_legendary_items],
                      [legendary_items[i][1] for i in random_legendary_items],
                      summoner_spells[random_summoner_spells[0]],
                      summoner_spells[random_summoner_spells[1]], random_skill_order, random_rune)

        await message.reply(file=discord.File("./temp/output_file.png"))

    if client.user.mentioned_in(message):
        embed = discord.Embed(title="Oxygen's Bot Help")
        embed.add_field(name="Available commands:", value="!aramki - generate random stuff")
        embed.add_field(name="Github repository", value="https://github.com/karolstawowski/false_bravery")
        await message.channel.send(embed=embed)


client.run(password)
