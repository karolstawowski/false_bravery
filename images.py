import os
from PIL import Image, ImageDraw, ImageFont
from apiImageHandling import get_image_from_api, get_rune_image_from_api


def create_temp_directory():
    if not os.path.exists('temp'):
        os.makedirs('temp')


def generate_template_image(path) -> Image:
    if os.path.isfile(f'{path}'):
        return Image.open(f'{path}')
    image = Image.new('RGB', (370, 644), (80, 80, 80))
    image.save(f'{path}')
    return image


def create_champion_label(champion, image):
    draw_image = ImageDraw.Draw(image)
    font = ImageFont.truetype("./assets/Roboto-Bold.ttf", 20)
    w, h = draw_image.textsize(f"{champion}", font=font)
    draw_image.text(((120 - w) / 2 + 20, 150), f"{champion}", (255, 255, 255), font=font)


def create_skill_order_label(skills, template_image):
    draw_image = ImageDraw.Draw(template_image)
    font = ImageFont.truetype("./assets/Roboto-Bold.ttf", 24)
    draw_image.text((240, 102), f"{skills[0]} > {skills[1]} > {skills[2]} ", (255, 255, 255), font=font)


def create_item_label(label, template_image, x, y):
    draw_image = ImageDraw.Draw(template_image)
    font = ImageFont.truetype("./assets/Roboto-Regular.ttf", 16)
    draw_image.text((x, y), f'{label}', (255, 255, 255), font=font)


def generate_image(champion, boots_item, boots_en, boots_pl, mythic_item, mythic_item_en, mythic_item_pl,
                  legendary_items, legendary_items_en, legendary_items_pl, summoner_spell_1, summoner_spell_2,
                  skill_order, primary_rune, rune_tree):
    legendary_items_array = []
    item_image_size = 64
    champion_image_size = 120
    line_height = 20
    outer_padding = 20
    inside_padding = 10
    # summoner_spell_image_size = 48
    # rune_image_size = 64

    create_temp_directory()

    champion_image = get_image_from_api(champion, 'champion')
    boots_image = get_image_from_api(boots_item, 'item')
    mythic_item = get_image_from_api(mythic_item, 'item')
    for item in legendary_items:
        legendary_items_array.append(get_image_from_api(item, 'item'))
    summoner_spell_images = get_image_from_api('spell0', 'sprite')
    rune_image = get_rune_image_from_api(primary_rune.key, primary_rune.link, (64, 64), "BLACK")
    rune_tree_image = get_rune_image_from_api(rune_tree.key, rune_tree.link, (48, 48), (60, 60, 60))

    template_image = generate_template_image("./assets/template.png")

    template_image.paste(champion_image, (outer_padding, outer_padding))

    template_image.paste(boots_image,
                         (outer_padding, champion_image_size + 2 * outer_padding + inside_padding + line_height))

    template_image.paste(mythic_item, (
        outer_padding, champion_image_size + 2 * outer_padding + 2 * inside_padding + item_image_size + line_height))

    template_image.paste(summoner_spell_images.crop((summoner_spell_1.x, summoner_spell_1.y,
                                                     summoner_spell_1.x + summoner_spell_1.w,
                                                     summoner_spell_1.y + summoner_spell_1.h)), (160, 26))

    template_image.paste(summoner_spell_images.crop((summoner_spell_2.x, summoner_spell_2.y,
                                                     summoner_spell_2.x + summoner_spell_2.w,
                                                     summoner_spell_2.y + summoner_spell_2.h)), (160, 84))

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

    create_champion_label(champion, template_image)

    create_skill_order_label(skill_order, template_image)

    create_item_label(boots_en, template_image, 94, 202)
    create_item_label(boots_pl, template_image, 94, 202 + 24)
    # create_item_label(boots_en, template_image, 94, 212)

    create_item_label(mythic_item_en, template_image, 94, 202 + 74)
    create_item_label(mythic_item_pl, template_image, 94, 202 + 74 + 24)
    # createItemLabel(mythic_item_en, template_image, 94, 212 + 74)

    for item in range(len(legendary_items_en)):
        create_item_label(legendary_items_en[item], template_image, 94, 202 + 74 * (item + 2))
        create_item_label(legendary_items_pl[item], template_image, 94, 202 + 24 + 74 * (item + 2))
        # createItemLabel(legendary_items_en[item], template_image, 94, 212 + 74 * (item + 2))

    template_image.save("./temp/output_file.png")
