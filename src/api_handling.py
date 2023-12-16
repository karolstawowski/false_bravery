import os
import urllib.request

import requests
from PIL import Image
from PIL.Image import Image as PILImage
from data_type_class import Data_type
from locale_class import Locale


def get_image_from_api(source: str, source_type: str, lol_version: str) -> PILImage:
    if os.path.isfile(f"../temp/{source_type}/{source}.png"):
        return Image.open(f"../temp/{source_type}/{source}.png")
    if not os.path.isdir(f"../temp/{source_type}"):
        os.mkdir(f"../temp/{source_type}")
    urllib.request.urlretrieve(
        f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/img/{source_type}/{source}.png",
        f"../temp/{source_type}/{source}.png",
    )
    return Image.open(f"../temp/{source_type}/{source}.png")


def get_rune_image_from_api(
    name: str,
    source: str,
    size: tuple[int, int],
    background_color: tuple[int, int, int],
) -> PILImage:
    if os.path.isfile(f"../temp/runes/{name}.jpg"):
        return Image.open(f"../temp/runes/{name}.jpg")
    if not os.path.isdir(f"../temp/runes"):
        os.mkdir(f"../temp/runes")
    urllib.request.urlretrieve(
        f"https://ddragon.canisback.com/img/{source}", f"../temp/runes/{name}.png"
    )
    rune_image = Image.open(f"../temp/runes/{name}.png")
    rune_image = rune_image.resize(size)
    return convert_png_to_jpg(name, rune_image, size, background_color)


def convert_png_to_jpg(
    image_name: str,
    png_image: PILImage,
    size: tuple[int, int],
    background_color: tuple[int, int, int],
) -> PILImage:
    new_image = Image.new("RGBA", size, background_color)
    new_image.paste(png_image, (0, 0), png_image)
    new_image.convert("RGB").save(f"../temp/runes/{image_name}.jpg")
    return new_image


def get_json_from_api(lol_version: str, data_type: Data_type, locale: Locale):
    try:
        response = requests.get(
            f"http://ddragon.leagueoflegends.com/cdn/{lol_version}/data/{locale.value}/{data_type.value}.json"
        )
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        raise
    except requests.exceptions.RequestException:
        raise

    return response.json() if data_type == Data_type.rune else response.json()["data"]
