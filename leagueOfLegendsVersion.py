import requests


def getLeagueOfLegendsVersion():
    try:
        return requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0]
    except requests.exceptions.RequestException:
        return '12.1.1'
