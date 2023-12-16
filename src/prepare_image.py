import discord
from champions import randomize_champion
from images import generate_image
from items import randomize_boots, randomize_legendary_items
from runes import randomize_primary_rune, randomize_rune_tree
from skills import randomize_skill_order
from summoner_spells import randomize_summoner_spells


async def prepare_image(
    lol_version,
    legendary_items,
    boots_items,
    champions,
    summoner_spells,
    primary_runes,
    rune_trees,
):
    random_legendary_items = randomize_legendary_items(legendary_items)
    random_summoner_spells = randomize_summoner_spells(summoner_spells)
    random_boots = randomize_boots(boots_items)
    random_skill_order = randomize_skill_order()
    random_champion = randomize_champion(champions)
    random_primary_rune = randomize_primary_rune(primary_runes)
    random_rune_tree = randomize_rune_tree(random_primary_rune, rune_trees)

    generate_image(
        random_champion,
        random_boots,
        random_legendary_items,
        summoner_spells[random_summoner_spells[0]],
        summoner_spells[random_summoner_spells[1]],
        random_skill_order,
        random_primary_rune,
        random_rune_tree,
        lol_version,
    )
