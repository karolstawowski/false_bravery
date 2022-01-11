from PIL import Image, ImageDraw, ImageFont
import urllib.request


def createChampionLabel(champion, image):
    draw_image = ImageDraw.Draw(image)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("./assets/Roboto-Regular.ttf", 20)
    # draw.text((x, y),"Sample Text",(r,g,b))
    w, h = draw_image.textsize(f"{champion}", font=font)
    draw_image.text(((120 - w) / 2 + 20, 150), f"{champion}", (255, 255, 255), font=font)


def getImageFromApi(source, source_type):
    urllib.request.urlretrieve(f'http://ddragon.leagueoflegends.com/cdn/12.1.1/img/{source_type}/{source}.png',
                               f'./assets/{source}.png')
    return Image.open(f'./assets/{source}.png')


def generateTemplateImage(path):
    image = Image.new('RGB', (320, 644), (80, 80, 80))  # 296
    image.save(f'{path}')
    return image


def createSkillOrderLabel(template_image):
    draw_image = ImageDraw.Draw(template_image)
    font = ImageFont.truetype("./assets/Roboto-Regular.ttf", 20)
    draw_image.text((170, 84), "Skill order", (255, 255, 255), font=font)
    draw_image.text((170, 114), "R > Q > W > E ", (255, 255, 255), font=font)


def createItemLabel(label, template_image, x, y):
    draw_image = ImageDraw.Draw(template_image)
    font = ImageFont.truetype("./assets/Roboto-Regular.ttf", 16)
    draw_image.text((x, y), f'{label}', (255, 255, 255), font=font)


def generateImage(champion, boots_item, boots_en, boots_pl, mythic_item, mythic_item_en, mythic_item_pl,
                  legendary_items, legendary_items_en, legendary_items_pl, summoner_spell_1, summoner_spell_2):
    legendary_items_array = []
    item_image_width = 64
    item_image_padding = 10
    champion_image_width = 120
    champion_image_padding = 20
    # champion_image_width_combined = champion_image_padding + champion_image_width + 10

    champion_image = getImageFromApi(champion, 'champion')
    boots_image = getImageFromApi(boots_item, 'item')
    mythic_item = getImageFromApi(mythic_item, 'item')
    for item in legendary_items:
        legendary_items_array.append(getImageFromApi(item, 'item'))
    summoner_spell_images = getImageFromApi('spell0', 'sprite')

    template_image = generateTemplateImage("./temp/img.png")

    template_image.paste(champion_image, (20, champion_image_padding))

    template_image.paste(boots_image, (20, champion_image_width + champion_image_padding + 10 + 40))

    template_image.paste(mythic_item, (
    20, champion_image_width + champion_image_padding + 10 + item_image_width + item_image_padding + 40))

    template_image.paste(summoner_spell_images.crop((summoner_spell_1.x, summoner_spell_1.y,
                                                     summoner_spell_1.x + summoner_spell_1.w,
                                                     summoner_spell_1.y + summoner_spell_1.h)), (170, 26))

    template_image.paste(summoner_spell_images.crop((summoner_spell_2.x, summoner_spell_2.y,
                                                     summoner_spell_2.x + summoner_spell_2.w,
                                                     summoner_spell_2.y + summoner_spell_2.h)), (242, 26))

    item = 0
    while item < 4:
        template_image.paste(legendary_items_array[item], (
            20,
            champion_image_width + champion_image_padding + 10 + item_image_width * (item + 2) + item_image_padding * (
                        item + 2) + 40))
        item += 1

    createChampionLabel(champion, template_image)

    createSkillOrderLabel(template_image)

    createItemLabel(boots_en, template_image, 94, 190 + 12)
    createItemLabel(boots_pl, template_image, 94, 190 + 12 + 24)

    createItemLabel(mythic_item_en, template_image, 94, 190 + 12 + 64 + 10)
    createItemLabel(mythic_item_pl, template_image, 94, 190 + 12 + 64 + 10 + 24)

    for item in range(len(legendary_items_en)):
        createItemLabel(legendary_items_en[item], template_image, 94, 190 + 12 + 74 * (item + 2))

    for item in range(len(legendary_items_pl)):
        createItemLabel(legendary_items_pl[item], template_image, 94, 190 + 12 + 24 + 74 * (item + 2))

    template_image.save("./assets/ready.png")
