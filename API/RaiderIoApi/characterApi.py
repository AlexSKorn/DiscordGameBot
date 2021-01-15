import requests

baseString = "https://raider.io/api/v1/characters/profile"
region = "us"


def getCharacter(realm, charName):
    query = {"region": region, "realm": realm,
             "name": charName, "fields": bestRunString}
    response = requests.get(baseString, params=query)
    if response.status_code == 200:
        return readCharJson(response.json())
    else:
        return response.status_code + " " + response.content


def readCharJson(charJson):
    finalCharString = readBasicCharData(charJson)
    return finalCharString


def readBasicCharData(charJson):
    basicCharString = "Name: {0} \nClass: {1} \nRealm: {2} \n{3}".format(
        charJson["name"], charJson["class"], charJson["realm"], charJson["profile_url"])
    return basicCharString


def readMPlusData(charJson):
    mPlusString = ("Normal: {0} \nHeroic: {1}".format(charJson))
    return mPlusString


def readRaidData(charJson):
    raidProgress = jsonResp["raid_progression"]
    raidString = ("Normal: {0} \nHeroic: {1}".format(
        raidProgress["normal_bosses_killed"], raidProgress["heroic_bosses_killed"]))
    return raidString
