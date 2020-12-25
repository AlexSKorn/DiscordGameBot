import requests
import json
from models import summoner
from dotenv import load_dotenv

load_dotenv()

regionRouting = "americas.api.riotgames.com"
platformRouting = "https://na1.api.riotgames.com/"
summonerByNameUrl = "lol/summoner/v4/summoners/by-name/"
langCode = "en_US"

# Need to execute this request first to get puuid
# https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/monitorman33/NA1

# https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/MonitorMan33
# /lol/summoner/v4/summoners/by-name/{summonerName}
# this key expires every 24 hours

# League V4 to get ranked data
# https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/monitorman33


def SummonerLevel(summonerId):
        response = requests.get(
        platformRouting + summonerByNameUrl, params=summonerId)
    summoner = Summoner()
    return summoner
