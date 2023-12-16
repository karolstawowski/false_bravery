import discord
from discord.ext import commands

from config import LEAGUE_OF_LEGENDS_VERSION
from prepare_image import prepare_image


def get_bot_token():
    return open("../bot_password.txt", "r").read()


RUN_COMMAND_KEYWORD = "!aramki"


def run_discord_bot(
    legendary_items, boots_items, champions, summoner_spells, primary_runes, rune_trees
):
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix="!", intents=intents)
    BOT_TOKEN = get_bot_token()

    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))
        await client.tree.sync()

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.mention_everyone:
            return

        if message.content == RUN_COMMAND_KEYWORD:
            await prepare_image(
                LEAGUE_OF_LEGENDS_VERSION,
                legendary_items,
                boots_items,
                champions,
                summoner_spells,
                primary_runes,
                rune_trees,
            )

            return await message.reply(file=discord.File("../temp/output_file.png"))

        if client.user.mentioned_in(message):
            embed = discord.Embed(title="Oxygen's Bot Help")
            embed.add_field(
                name="Available commands:",
                value=f"{RUN_COMMAND_KEYWORD} - generate random stuff",
            )
            embed.set_footer(text="https://github.com/karolstawowski/false_bravery")
            await message.channel.send(embed=embed)

    @client.tree.command(
        name="aramki",
        description="Generate a random set of items, runes, summoner spells and skill order.",
    )
    async def _space(ctx: discord.interactions.Interaction):
        await prepare_image(
            LEAGUE_OF_LEGENDS_VERSION,
            legendary_items,
            boots_items,
            champions,
            summoner_spells,
            primary_runes,
            rune_trees,
        )
        await ctx.response.send_message(file=discord.File("../temp/output_file.png"))

    client.run(BOT_TOKEN)
