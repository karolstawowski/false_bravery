# False Bravery

![Language](https://img.shields.io/badge/language-Python-3993fa)
![License](https://img.shields.io/github/license/karolstawowski/false_bravery?color=3993fa)

## Description

False Bravery is a Discord Bot for League of Legends players which creates an image with random champion, summoner spells, items and skill order and sends it to the Discord channel.

## Installation and usage

To run False Bravery, you need to have <a href="https://www.python.org/downloads/">Python</a> and <a href="https://pip.pypa.io/en/stable/cli/pip_install/">pip</a> installed.

1. Clone github repository

```
git clone https://github.com/karolstawowski/false_bravery.git
```

2. Create virtual enviroment

```
py -m venv .venv
```

3. Activate virtual enviroment

```
.\env\Scripts\activate
```

4. Install required packages using pip

```
py -m pip install -r requirements.txt
```

5. Create bot_password.txt file and paste your bot's token into it

6. Run program

```
python main.py
```

7. Bot is ready to use! Type `!aramki` in Discord text chat to get your random build!

## Docker

You can also run False Bravery using Docker. To do so, you need to have <a href="https://docs.docker.com/get-docker/">Docker</a> installed.

1. Create docker image

```
docker build -t false_bravery .
```

2. Create docker container

```
docker run -d --name false_bravery false_bravery
```

## Resources

<a href="https://developer.riotgames.com/docs/lol">Riot Games API</a>, <a href="https://pillow.readthedocs.io/en/stable/">Python Imaging Library</a>

## Tools and technologies used

Python, pip, Python Imaging Library (PIL)
