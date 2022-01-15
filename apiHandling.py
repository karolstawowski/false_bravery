import os
import urllib.request
from PIL import Image


def getImageFromApi(source, source_type):
    if os.path.isfile(f'./temp/{source_type}/{source}.png'):
        return Image.open(f'./temp/{source_type}/{source}.png')
    if not os.path.isdir(f'./temp/{source_type}'):
        os.mkdir(f'./temp/{source_type}')
    urllib.request.urlretrieve(f'http://ddragon.leagueoflegends.com/cdn/12.1.1/img/{source_type}/{source}.png',
                               f'./temp/{source_type}/{source}.png')
    return Image.open(f'./temp/{source_type}/{source}.png')


def getRuneImageFromApi(name, source, size):
    if os.path.isfile(f'./temp/runes/{name}.jpg'):
        return Image.open(f'./temp/runes/{name}.jpg')
    if not os.path.isdir(f'./temp/runes'):
        os.mkdir(f'./temp/runes')
    urllib.request.urlretrieve(f'https://ddragon.canisback.com/img/{source}', f'./temp/runes/{name}.png')
    rune_image = Image.open(f'./temp/runes/{name}.png')
    rune_image = rune_image.resize(size)
    return convertPngToJpg(name, rune_image, size)


def convertPngToJpg(image_name, png_image, size):
    new_image = Image.new("RGBA", size)
    new_image.paste(png_image, (0, 0), png_image)
    new_image.convert('RGB').save(f'./temp/runes/{image_name}.jpg')
    return new_image
