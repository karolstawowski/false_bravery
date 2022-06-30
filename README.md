# False Bravery

![Language](https://img.shields.io/badge/language-Python-3993fa)
![License](https://img.shields.io/github/license/karolstawowski/false_bravery?color=3993fa)
![Number of lines](https://img.shields.io/tokei/lines/github/karolstawowski/false_bravery?color=3993fa)
![Version](https://img.shields.io/badge/version-1.0.0.0-3993fa) <br>

## Description

False Bravery is a Discord Bot for League of Legends players which creates an image with random champion, summoner spells, items and skill order and sends it to the Discord channel.

## Installation

To run False Bravery, you need to have <a href="https://www.python.org/downloads/">Python</a> and <a href="https://pip.pypa.io/en/stable/cli/pip_install/">pip</a> installed.

```bash
git clone https://github.com/karolstawowski/false_bravery.git
```

## Usage

1. Create virtual enviroment

```
py -m venv env
```

2. Activate virtual enviroment

```
.\env\Scripts\activate
```

3. Install required packages using pip

```
py -m pip install -r requirements.txt
```

4. Create bot_password.txt file and paste your bot's token into it

5. Run program

```
python main.py
```

6. Bot is ready to use! Type `!aramki` in Discord text chat to get your random build!

## App structure

```bash
📦false_bravery
 ┣ 📂assets
 ┃ ┣ 📜Roboto-Bold.ttf
 ┃ ┣ 📜Roboto-Regular.ttf
 ┃ ┗ 📜template.png
 ┣ 📜.gitignore
 ┣ 📜api_handling.py
 ┣ 📜bot_password.txt
 ┣ 📜champions.py
 ┣ 📜config.py
 ┣ 📜data_type_class.py
 ┣ 📜discord_bot.py
 ┣ 📜images.py
 ┣ 📜items.py
 ┣ 📜item_class.py
 ┣ 📜league_of_legends_version.py
 ┣ 📜LICENSE
 ┣ 📜locale_class.py
 ┣ 📜main.py
 ┣ 📜primary_rune_class.py
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┣ 📜runes.py
 ┣ 📜rune_tree_class.py
 ┣ 📜skills.py
 ┣ 📜ssl_handling.py
 ┣ 📜summoner_spells.py
 ┗ 📜summoner_spell_class.py
```

## Resources

<a href="https://developer.riotgames.com/docs/lol">Riot Games API</a>, <a href="https://pillow.readthedocs.io/en/stable/">Python Imaging Library</a>

## Tools and technologies used

Python, pip, Python Imaging Library (PIL)
