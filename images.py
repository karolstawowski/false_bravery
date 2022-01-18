import os
from PIL import Image, ImageDraw, ImageFont
from apiImageHandling import get_image_from_api, get_rune_image_from_api
from primaryRuneClass import PrimaryRune
from runeTreeClass import RuneTree
from summonerSpellClass import SummonerSpell


def create_temp_directory():
    if not os.path.exists('temp'):
        os.makedirs('temp')


def generate_template_image(path: str) -> Image:
    if os.path.isfile(f'{path}'):
        return Image.open(f'{path}')
    image = Image.new('RGB', (370, 644), (80, 80, 80))
    image.save(f'{path}')
    return image


def create_champion_label(champion_name: str, image: Image):
    draw_image = ImageDraw.Draw(image)
    font = ImageFont.truetype("./assets/Roboto-Bold.ttf", 20)
    w, h = draw_image.textsize(f"{champion_name}", font=font)
    draw_image.text(((120 - w) / 2 + 20, 150), f"{champion_name}", (255, 255, 255), font=font)


def create_skill_order_label(skills: list, template_image: Image):
    draw_image = ImageDraw.Draw(template_image)
    font = ImageFont.truetype("./assets/Roboto-Bold.ttf", 24)
    draw_image.text((240, 102), f"{skills[0]} > {skills[1]} > {skills[2]} ", (255, 255, 255), font=font)


def create_item_label(item_label: str, template_image: Image, x_axis: int, y_axis: int):
    draw_image = ImageDraw.Draw(template_image)
    font = ImageFont.truetype("./assets/Roboto-Regular.ttf", 16)
    draw_image.text((x_axis, y_axis), f'{item_label}', (255, 255, 255), font=font)


def generate_image(champion: str, boots_item: str, boots_en: str, boots_pl: str, mythic_item: str, mythic_item_en: str,
                   mythic_item_pl: str,
                   legendary_items: list, legendary_items_en: list, legendary_items_pl: list,
                   summoner_spell_1: SummonerSpell, summoner_spell_2: SummonerSpell,
                   skill_order: list, primary_rune: PrimaryRune, rune_tree: RuneTree):
    legendary_items_array = []
    item_image_size = 64
    champion_image_size = 120
    line_height = 20
    outer_padding = 20
    inside_padding = 10

    create_temp_directory()

    # get images

    champion_image = get_image_from_api(champion, 'champion')
    boots_image = get_image_from_api(boots_item, 'item')
    mythic_item_image = get_image_from_api(mythic_item, 'item')
    for item in legendary_items:
        legendary_items_array.append(get_image_from_api(item, 'item'))
    summoner_spell_images = get_image_from_api('spell0', 'sprite')
    rune_image = get_rune_image_from_api(primary_rune.key, primary_rune.image_link, (64, 64), (0, 0, 0))
    rune_tree_image = get_rune_image_from_api(rune_tree.key, rune_tree.image_link, (48, 48), (60, 60, 60))

    # prepare template image

    template_image = generate_template_image("./assets/template.png")

    # insert images

    template_image.paste(champion_image, (outer_padding, outer_padding))

    template_image.paste(boots_image,
                         (outer_padding, champion_image_size + 2 * outer_padding + inside_padding + line_height))

    template_image.paste(mythic_item_image, (
        outer_padding, champion_image_size + 2 * outer_padding + 2 * inside_padding + item_image_size + line_height))

    template_image.paste(summoner_spell_images.crop((summoner_spell_1.image_x_axis, summoner_spell_1.image_y_axis,
                                                     summoner_spell_1.image_x_axis + summoner_spell_1.image_width,
                                                     summoner_spell_1.image_y_axis + summoner_spell_1.image_height)),
                         (160, 26))

    template_image.paste(summoner_spell_images.crop((summoner_spell_2.image_x_axis, summoner_spell_2.image_y_axis,
                                                     summoner_spell_2.image_x_axis + summoner_spell_2.image_width,
                                                     summoner_spell_2.image_y_axis + summoner_spell_2.image_height)),
                         (160, 84))

    legendary_item_i = 0
    while legendary_item_i < 4:
        template_image.paste(legendary_items_array[legendary_item_i], (
            outer_padding,
            champion_image_size + 2 * outer_padding + inside_padding + item_image_size * (
                    legendary_item_i + 2) + line_height + inside_padding * (
                    legendary_item_i + 2)))
        legendary_item_i += 1

    template_image.paste(rune_image, (230, 26))

    template_image.paste(rune_tree_image, (304, 34))

    # insert labels

    create_champion_label(champion, template_image)

    create_skill_order_label(skill_order, template_image)

    create_item_label(boots_en, template_image, 94, 202)
    create_item_label(boots_pl, template_image, 94, 202 + 24)

    create_item_label(mythic_item_en, template_image, 94, 202 + 74)
    create_item_label(mythic_item_pl, template_image, 94, 202 + 74 + 24)

    for item in range(len(legendary_items_en)):
        create_item_label(legendary_items_en[item], template_image, 94, 202 + 74 * (item + 2))
        create_item_label(legendary_items_pl[item], template_image, 94, 202 + 24 + 74 * (item + 2))

    template_image.save("./temp/output_file.png")
