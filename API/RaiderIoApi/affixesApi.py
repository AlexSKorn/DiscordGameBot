import requests

baseString = "https://raider.io/api/v1/mythic-plus/affixes"
query = {"region": "us", "locale": "en"}


def getAffixes():
    response = requests.get(
        baseString, params=query)
    return readAffixJson(response.content)


def readAffixJson(jsonContent):
    affixes = json.loads(jsonContent)["affix_details"]
    finalAffixString = ""
    for affix in affixes:
        finalAffixString += oneAffixString(affix) + "\n"
    return finalAffixString


def oneAffixString(affix):
    affixDetail = "Affix Name: {0},\n Description: {1}".format(
        affix["name"], affix["description"])
    return affixDetail
