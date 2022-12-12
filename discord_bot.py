import discord

from champions import randomize_champion
from config import LEAGUE_OF_LEGENDS_VERSION
from images import generate_image
from items import (randomize_boots, randomize_legendary_items,
                   randomize_mythic_item)
from runes import randomize_primary_rune, randomize_rune_tree
from skills import randomize_skill_order
from summoner_spells import randomize_summoner_spells


def get_bot_password():
    return open('bot_password.txt', 'r').read()


def runDiscordBot(mythic_items, legendary_items, boots_items, champions, summoner_spells, primary_runes, rune_trees):
    client = discord.Client()

    password = get_bot_password()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.mention_everyone:
            return

        if message.content.startswith('!aramki'):
            random_legendary_items = randomize_legendary_items(legendary_items)
            random_summoner_spells = randomize_summoner_spells(summoner_spells)
            random_boots = randomize_boots(boots_items)
            random_mythic_item = randomize_mythic_item(mythic_items)
            random_skill_order = randomize_skill_order()
            random_champion = randomize_champion(champions)
            random_primary_rune = randomize_primary_rune(primary_runes)
            random_rune_tree = randomize_rune_tree(
                random_primary_rune, rune_trees)

            generate_image(random_champion, random_boots,
                           random_mythic_item,
                           random_legendary_items,
                           summoner_spells[random_summoner_spells[0]],
                           summoner_spells[random_summoner_spells[1]
                                           ], random_skill_order, random_primary_rune,
                           random_rune_tree, LEAGUE_OF_LEGENDS_VERSION)

            await message.reply(file=discord.File("./temp/output_file.png"))

        if client.user.mentioned_in(message):
            embed = discord.Embed(title="Oxygen's Bot Help")
            embed.add_field(name="Available commands:",
                            value="!aramki - generate random stuff")
            embed.set_footer(
                text="https://github.com/karolstawowski/false_bravery")
            await message.channel.send(embed=embed)

    client.run(password)
