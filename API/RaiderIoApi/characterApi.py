import requests
import json

load_dotenv()

# "https://raider.io/api/v1/characters/profile?region=us&realm=Tichondrius&name=Chickensub&fields=gear%2C%20covenant" -H "accept: application/json"

baseString = "https://raider.io/api/v1/characters/profile"
region = "us"


def Character(realm, charName):
    query = {"region": region, "realm": realm, "name": charName}
    response = requests.get(baseString, params=query)
    return readCharJson(response.content)


def readCharJson(jsonContent):
    jsonResp = json.loads(jsonContent)
    finalCharString = "Name: {0} \nClass: {1} \nRealm: {2} \n {3}".format(
        jsonResp["name"], jsonResp["class"], jsonResp["realm"], jsonResp["thumbnail_url"])
    return finalCharString
