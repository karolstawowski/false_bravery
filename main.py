import os
from champions import get_champions_from_api
from items import get_items_from_api
from summonerSpells import get_summoner_spells_from_api
from leagueOfLegendsVersion import get_league_of_legends_version
from runes import get_runes_from_api
from sslHandling import verify_ssl_certificate
from discordBot import runDiscordBot

verify_ssl_certificate()

os.environ["LOL_VERSION"] = get_league_of_legends_version()

[mythic_items, legendary_items, boots_items] = get_items_from_api(os.environ["LOL_VERSION"])
champions = get_champions_from_api(os.environ["LOL_VERSION"])
summoner_spells = get_summoner_spells_from_api(os.environ["LOL_VERSION"])
primary_runes, rune_trees = get_runes_from_api(os.environ["LOL_VERSION"])

runDiscordBot(mythic_items, legendary_items, boots_items, champions, summoner_spells, primary_runes, rune_trees)
