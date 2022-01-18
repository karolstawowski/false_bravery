import os
import urllib.request
from PIL import Image


def get_image_from_api(source: str, source_type: str) -> Image:
    if os.path.isfile(f'./temp/{source_type}/{source}.png'):
        return Image.open(f'./temp/{source_type}/{source}.png')
    if not os.path.isdir(f'./temp/{source_type}'):
        os.mkdir(f'./temp/{source_type}')
    urllib.request.urlretrieve(f'http://ddragon.leagueoflegends.com/cdn/12.1.1/img/{source_type}/{source}.png',
                               f'./temp/{source_type}/{source}.png')
    return Image.open(f'./temp/{source_type}/{source}.png')


def get_rune_image_from_api(name: str, source: str, size: tuple, background_color: tuple) -> Image:
    if os.path.isfile(f'./temp/runes/{name}.jpg'):
        return Image.open(f'./temp/runes/{name}.jpg')
    if not os.path.isdir(f'./temp/runes'):
        os.mkdir(f'./temp/runes')
    urllib.request.urlretrieve(f'https://ddragon.canisback.com/img/{source}', f'./temp/runes/{name}.png')
    rune_image = Image.open(f'./temp/runes/{name}.png')
    rune_image = rune_image.resize(size)
    return convert_png_to_jpg(name, rune_image, size, background_color)


def convert_png_to_jpg(image_name: str, png_image: Image, size: tuple, background_color: tuple) -> Image:
    new_image = Image.new("RGBA", size, background_color)
    new_image.paste(png_image, (0, 0), png_image)
    new_image.convert('RGB').save(f'./temp/runes/{image_name}.jpg')
    return new_image
