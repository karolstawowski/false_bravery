import discord

from config import LEAGUE_OF_LEGENDS_VERSION
from send_image import send_image


def get_bot_password():
    return open("bot_password.txt", "r").read()


RUN_COMMAND_KEYWORD = "!aramki"


def run_discord_bot(
    legendary_items, boots_items, champions, summoner_spells, primary_runes, rune_trees
):
    client = discord.Client()
    password = get_bot_password()

    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.mention_everyone:
            return

        if message.content.startswith(RUN_COMMAND_KEYWORD):
            return await send_image(
                message,
                LEAGUE_OF_LEGENDS_VERSION,
                legendary_items,
                boots_items,
                champions,
                summoner_spells,
                primary_runes,
                rune_trees,
            )

        if client.user.mentioned_in(message):
            embed = discord.Embed(title="Oxygen's Bot Help")
            embed.add_field(
                name="Available commands:",
                value=f"{RUN_COMMAND_KEYWORD} - generate random stuff",
            )
            embed.set_footer(text="https://github.com/karolstawowski/false_bravery")
            await message.channel.send(embed=embed)

    client.run(password)
