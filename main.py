import discord
from champions import get_champions_from_api, randomize_champion
from items import get_items_from_api, randomize_boots, randomize_mythic_item, randomize_legendary_items
from summonerSpells import get_summoner_spells_from_api, randomize_summoner_spells
from images import generate_image
from leagueOfLegendsVersion import get_league_of_legends_version
from skills import randomize_skill_order
from runes import get_runes_from_api, randomize_primary_rune, randomize_rune_tree

client = discord.Client()

lol_version = get_league_of_legends_version()

[mythic_items, legendary_items, boots_items] = get_items_from_api(lol_version)
champions = get_champions_from_api(lol_version)
summoner_spells = get_summoner_spells_from_api(lol_version)
primary_runes, rune_trees = get_runes_from_api(lol_version)

password = open('bot_password.txt', 'r').read()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!aramki'):
        random_legendary_items = randomize_legendary_items(legendary_items)
        random_summoner_spells = randomize_summoner_spells(summoner_spells)
        random_boots = randomize_boots(boots_items)
        random_mythic_item = randomize_mythic_item(mythic_items)
        random_skill_order = randomize_skill_order()
        random_champion = randomize_champion(champions)
        random_primary_rune = randomize_primary_rune(primary_runes)
        random_rune_tree = randomize_rune_tree(random_primary_rune, rune_trees)

        generate_image(random_champion, random_boots, boots_items[random_boots][0],
                       boots_items[random_boots][1],
                       random_mythic_item, mythic_items[random_mythic_item][0], mythic_items[random_mythic_item][1],
                       random_legendary_items, [legendary_items[i][0] for i in random_legendary_items],
                       [legendary_items[i][1] for i in random_legendary_items],
                       summoner_spells[random_summoner_spells[0]],
                       summoner_spells[random_summoner_spells[1]], random_skill_order, random_primary_rune,
                       random_rune_tree)

        await message.reply(file=discord.File("./temp/output_file.png"))

    if client.user.mentioned_in(message):
        embed = discord.Embed(title="Oxygen's Bot Help")
        embed.add_field(name="Available commands:", value="!aramki - generate random stuff")
        embed.set_footer(text="https://github.com/karolstawowski/false_bravery")
        await message.channel.send(embed=embed)


client.run(password)
