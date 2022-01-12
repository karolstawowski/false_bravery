from PIL import Image, ImageDraw, ImageFont
import urllib.request
import random
import os


def createChampionLabel(champion, image):
    draw_image = ImageDraw.Draw(image)
    font = ImageFont.truetype("./assets/Roboto-Regular.ttf", 20)
    w, h = draw_image.textsize(f"{champion}", font=font)
    draw_image.text(((120 - w) / 2 + 20, 150), f"{champion}", (255, 255, 255), font=font)


def getImageFromApi(source, source_type):
    if os.path.isfile(f'./temp/{source}.png'):
        return Image.open(f'./temp/{source}.png')
    urllib.request.urlretrieve(f'http://ddragon.leagueoflegends.com/cdn/12.1.1/img/{source_type}/{source}.png',
                               f'./temp/{source}.png')
    return Image.open(f'./temp/{source}.png')


def generateTemplateImage(path):
    if os.path.isfile(f'{path}'):
        return Image.open(f'{path}')
    image = Image.new('RGB', (360, 644), (80, 80, 80))
    image.save(f'{path}')
    return image


def createSkillOrderLabel(template_image):
    skills = ['Q', 'W', 'E']
    random.shuffle(skills)
    random.shuffle(skills)
    draw_image = ImageDraw.Draw(template_image)
    font = ImageFont.truetype("./assets/Roboto-Regular.ttf", 20)
    draw_image.text((190, 84), "Skill order", (255, 255, 255), font=font)
    draw_image.text((190, 114), f"R > {skills[0]} > {skills[1]} > {skills[2]} ", (255, 255, 255), font=font)


def createItemLabel(label, template_image, x, y):
    draw_image = ImageDraw.Draw(template_image)
    font = ImageFont.truetype("./assets/Roboto-Regular.ttf", 16)
    draw_image.text((x, y), f'{label}', (255, 255, 255), font=font)


def generateImage(champion, boots_item, boots_en, boots_pl, mythic_item, mythic_item_en, mythic_item_pl,
                  legendary_items, legendary_items_en, legendary_items_pl, summoner_spell_1, summoner_spell_2):
    legendary_items_array = []
    item_image_size = 64
    champion_image_size = 120
    summoner_spell_image_size = 48
    line_height = 20
    outter_padding = 20
    inside_padding = 10

    champion_image = getImageFromApi(champion, 'champion')
    boots_image = getImageFromApi(boots_item, 'item')
    mythic_item = getImageFromApi(mythic_item, 'item')
    for item in legendary_items:
        legendary_items_array.append(getImageFromApi(item, 'item'))
    summoner_spell_images = getImageFromApi('spell0', 'sprite')

    template_image = generateTemplateImage("./assets/template.png")

    template_image.paste(champion_image, (outter_padding, outter_padding))

    template_image.paste(boots_image,
                         (outter_padding, champion_image_size + 2 * outter_padding + inside_padding + line_height))

    template_image.paste(mythic_item, (
        outter_padding, champion_image_size + 2 * outter_padding + 2 * inside_padding + item_image_size + line_height))

    template_image.paste(summoner_spell_images.crop((summoner_spell_1.x, summoner_spell_1.y,
                                                     summoner_spell_1.x + summoner_spell_1.w,
                                                     summoner_spell_1.y + summoner_spell_1.h)), (190, 26))

    template_image.paste(summoner_spell_images.crop((summoner_spell_2.x, summoner_spell_2.y,
                                                     summoner_spell_2.x + summoner_spell_2.w,
                                                     summoner_spell_2.y + summoner_spell_2.h)), (262, 26))

    item = 0
    while item < 4:
        template_image.paste(legendary_items_array[item], (
            outter_padding,
            champion_image_size + 2 * outter_padding + inside_padding + item_image_size * (
                        item + 2) + line_height + inside_padding * (
                    item + 2)))
        item += 1

    createChampionLabel(champion, template_image)

    createSkillOrderLabel(template_image)

    createItemLabel(boots_en, template_image, 94, 202)
    createItemLabel(boots_pl, template_image, 94, 202 + 24)

    createItemLabel(mythic_item_en, template_image, 94, 202 + 74)
    createItemLabel(mythic_item_pl, template_image, 94, 202 + 74 + 24)

    for item in range(len(legendary_items_en)):
        createItemLabel(legendary_items_en[item], template_image, 94, 202 + 74 * (item + 2))

    for item in range(len(legendary_items_pl)):
        createItemLabel(legendary_items_pl[item], template_image, 94, 202 + 24 + 74 * (item + 2))

    template_image.save("./temp/output_file.png")
