import os
from PIL import Image, ImageDraw, ImageFont
from apiHandling import getImageFromApi, getRuneImageFromApi


def createTempPath():
    if not os.path.exists('temp'):
        os.makedirs('temp')


def generateTemplateImage(path):
    if os.path.isfile(f'{path}'):
        return Image.open(f'{path}')
    image = Image.new('RGB', (370, 644), (80, 80, 80))
    image.save(f'{path}')
    return image


def createChampionLabel(champion, image):
    draw_image = ImageDraw.Draw(image)
    font = ImageFont.truetype("./assets/Roboto-Bold.ttf", 20)
    w, h = draw_image.textsize(f"{champion}", font=font)
    draw_image.text(((120 - w) / 2 + 20, 150), f"{champion}", (255, 255, 255), font=font)


def createSkillOrderLabel(skills, template_image):
    draw_image = ImageDraw.Draw(template_image)
    font = ImageFont.truetype("./assets/Roboto-Bold.ttf", 24)
    draw_image.text((240, 102), f"{skills[0]} > {skills[1]} > {skills[2]} ", (255, 255, 255), font=font)


def createItemLabel(label, template_image, x, y):
    draw_image = ImageDraw.Draw(template_image)
    font = ImageFont.truetype("./assets/Roboto-Regular.ttf", 16)
    draw_image.text((x, y), f'{label}', (255, 255, 255), font=font)


def generateImage(champion, boots_item, boots_en, boots_pl, mythic_item, mythic_item_en, mythic_item_pl,
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

    createTempPath()

    champion_image = getImageFromApi(champion, 'champion')
    boots_image = getImageFromApi(boots_item, 'item')
    mythic_item = getImageFromApi(mythic_item, 'item')
    for item in legendary_items:
        legendary_items_array.append(getImageFromApi(item, 'item'))
    summoner_spell_images = getImageFromApi('spell0', 'sprite')
    rune_image = getRuneImageFromApi(primary_rune.key, primary_rune.link, (64, 64), "BLACK")
    rune_tree_image = getRuneImageFromApi(rune_tree.key, rune_tree.link, (48, 48), (60, 60, 60))

    template_image = generateTemplateImage("./assets/template.png")

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

    createChampionLabel(champion, template_image)

    createSkillOrderLabel(skill_order, template_image)

    createItemLabel(boots_en, template_image, 94, 202)
    createItemLabel(boots_pl, template_image, 94, 202 + 24)
    # createItemLabel(boots_en, template_image, 94, 212)

    createItemLabel(mythic_item_en, template_image, 94, 202 + 74)
    createItemLabel(mythic_item_pl, template_image, 94, 202 + 74 + 24)
    # createItemLabel(mythic_item_en, template_image, 94, 212 + 74)

    for item in range(len(legendary_items_en)):
        createItemLabel(legendary_items_en[item], template_image, 94, 202 + 74 * (item + 2))
        createItemLabel(legendary_items_pl[item], template_image, 94, 202 + 24 + 74 * (item + 2))
        # createItemLabel(legendary_items_en[item], template_image, 94, 212 + 74 * (item + 2))

    template_image.save("./temp/output_file.png")
