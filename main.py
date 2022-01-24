from champions import get_champions_from_api
from items import get_items_from_api
from summoner_spells import get_summoner_spells_from_api
from config import league_of_legends_version
from runes import get_runes_from_api
from ssl_handling import verify_ssl_certificate
from discord_bot import runDiscordBot

verify_ssl_certificate()

[mythic_items, legendary_items, boots_items] = get_items_from_api(league_of_legends_version)
champions = get_champions_from_api(league_of_legends_version)
summoner_spells = get_summoner_spells_from_api(league_of_legends_version)
primary_runes, rune_trees = get_runes_from_api(league_of_legends_version)

runDiscordBot(mythic_items, legendary_items, boots_items, champions, summoner_spells, primary_runes, rune_trees)
