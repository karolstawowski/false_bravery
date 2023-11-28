import requests


def get_league_of_legends_version() -> str:
    try:
        return requests.get(
            "https://ddragon.leagueoflegends.com/api/versions.json"
        ).json()[0]
    except requests.exceptions.RequestException:
        return "13.23.1"
