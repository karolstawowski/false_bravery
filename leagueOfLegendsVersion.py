import requests


def getLeagueOfLegendsVersion():
    return requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0]
