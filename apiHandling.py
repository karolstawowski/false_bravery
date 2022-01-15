import os
import urllib.request
from PIL import Image
from images import convertPngToJpg


def getImageFromApi(source, source_type):
    if os.path.isfile(f'./temp/{source}.png'):
        return Image.open(f'./temp/{source}.png')
    urllib.request.urlretrieve(f'http://ddragon.leagueoflegends.com/cdn/12.1.1/img/{source_type}/{source}.png',
                               f'./temp/{source}.png')
    return Image.open(f'./temp/{source}.png')


def getRuneImageFromApi(name, source, size):
    if os.path.isfile(f'./temp/runes/{name}.jpg'):
        return Image.open(f'./temp/runes/{name}.jpg')
    urllib.request.urlretrieve(f'https://ddragon.canisback.com/img/{source}', f'./temp/runes/{name}.png')
    rune_image = Image.open(f'./temp/runes/{name}.png')
    rune_image = rune_image.resize(size)
    return convertPngToJpg(name, rune_image, size)
