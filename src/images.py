import os
from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Image as PILImage
from PIL.ImageDraw import ImageDraw as PILImageDraw
from api_handling import get_image_from_api, get_rune_image_from_api
from item_class import Item
from primary_rune_class import PrimaryRune
from rune_tree_class import RuneTree
from summoner_spell_class import SummonerSpell

DEFAULT_FONT_SIZE = 16
HEADING_FONT_SIZE = 20


def create_temp_directory():
    if not os.path.exists("../temp"):
        os.makedirs("../temp")


def generate_template_image(template_image_path: str) -> PILImage:
    if os.path.isfile(f"{template_image_path}"):
        return Image.open(f"{template_image_path}")
    image = Image.new("RGB", (370, 644), (80, 80, 80))
    image.save(f"{template_image_path}")
    return image


def create_champion_label(champion_name: str, template_image: PILImage):
    draw_image = ImageDraw.Draw(template_image)
    font = ImageFont.truetype("../assets/Roboto-Bold.ttf", HEADING_FONT_SIZE)
    draw_image.text(
        ((120 - DEFAULT_FONT_SIZE) / 2 + HEADING_FONT_SIZE, 150),
        f"{champion_name}",
        (255, 255, 255),
        font=font,
    )


def create_skill_order_label(skills_list: list, template_image: PILImage):
    draw_image = ImageDraw.Draw(template_image)
    font = ImageFont.truetype("../assets/Roboto-Bold.ttf", 24)
    draw_image.text(
        (240, 102),
        f"{skills_list[0]} > {skills_list[1]} > {skills_list[2]} ",
        (255, 255, 255),
        font=font,
    )


def create_item_label(
    item_label: str, template_image: PILImage, x_axis: int, y_axis: int
):
    draw_image = ImageDraw.Draw(template_image)
    font = ImageFont.truetype("../assets/Roboto-Regular.ttf", DEFAULT_FONT_SIZE)
    draw_image.text((x_axis, y_axis), f"{item_label}", (255, 255, 255), font=font)


def generate_image(
    champion: str,
    boots_item: Item,
    legendary_items: list,
    summoner_spell_1: SummonerSpell,
    summoner_spell_2: SummonerSpell,
    skill_order: list,
    primary_rune: PrimaryRune,
    rune_tree: RuneTree,
    lol_version: str,
):
    item_image_size = 64
    champion_image_size = 120
    line_height = 20
    outer_padding = 20
    inside_padding = 10

    create_temp_directory()

    # Get images

    champion_image = get_image_from_api(champion, "champion", lol_version)
    boots_image = get_image_from_api(boots_item.id, "item", lol_version)
    legendary_items_images = [
        get_image_from_api(item.id, "item", lol_version) for item in legendary_items
    ]
    summoner_spell_images = get_image_from_api("spell0", "sprite", lol_version)
    rune_image = get_rune_image_from_api(
        primary_rune.key,
        primary_rune.image_link,
        (item_image_size, item_image_size),
        (0, 0, 0),
    )
    rune_tree_image = get_rune_image_from_api(
        rune_tree.key, rune_tree.image_link, (48, 48), (60, 60, 60)
    )

    # Prepare template image

    template_image = generate_template_image("../assets/template.png")

    # Insert images

    template_image.paste(champion_image, (outer_padding, outer_padding))

    template_image.paste(
        boots_image,
        (
            outer_padding,
            champion_image_size + 2 * outer_padding + inside_padding + line_height,
        ),
    )

    template_image.paste(
        summoner_spell_images.crop(
            (
                summoner_spell_1.image_x_axis,
                summoner_spell_1.image_y_axis,
                summoner_spell_1.image_x_axis + summoner_spell_1.image_width,
                summoner_spell_1.image_y_axis + summoner_spell_1.image_height,
            )
        ),
        (160, 26),
    )

    template_image.paste(
        summoner_spell_images.crop(
            (
                summoner_spell_2.image_x_axis,
                summoner_spell_2.image_y_axis,
                summoner_spell_2.image_x_axis + summoner_spell_2.image_width,
                summoner_spell_2.image_y_axis + summoner_spell_2.image_height,
            )
        ),
        (160, 84),
    )

    for idx, legendary_item in enumerate(legendary_items_images):
        template_image.paste(
            legendary_item,
            (
                outer_padding,
                champion_image_size
                + 2 * outer_padding
                + item_image_size * (idx + 1)
                + line_height
                + inside_padding * (idx + 2),
            ),
        )

    template_image.paste(rune_image, (230, 26))

    template_image.paste(rune_tree_image, (304, 34))

    # Insert labels

    create_champion_label(champion, template_image)

    create_skill_order_label(skill_order, template_image)

    create_item_label(boots_item.en_name, template_image, 94, 202)
    create_item_label(boots_item.pl_name, template_image, 94, 202 + 24)

    for item in range(len(legendary_items)):
        create_item_label(
            legendary_items[item].en_name, template_image, 94, 202 + 74 * (item + 1)
        )
        create_item_label(
            legendary_items[item].pl_name,
            template_image,
            94,
            202 + 24 + 74 * (item + 1),
        )

    template_image.save("../temp/output_file.png")
