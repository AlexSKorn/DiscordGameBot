import os
import discord
import constants
import random
import API.RaiderIoApi.affixesApi as affixAPI
import API.RaiderIoApi.characterApi as charAPI
import API.LeagueApi.summonerApi as summonerAPI

from dotenv import load_dotenv



client = discord.Client()
load_dotenv()

# py -3 main.py


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    channel = message.channel
    msg = message.content.lower()
    if message.author == client.user:
        return
    if msg.startswith("character"):
        realm = msg.split()[1]
        charName = msg.split()[2]
        if realm == None or charName == None:
            await channel.send(message.charHelp)
        else:
            await channel.send(charAPI.getCharacter(realm, charName))
    elif msg.startswith("affixes"):
        await channel.send(affixAPI.getAffixes())
    elif msg.startswith("summoner"):
        await channel.send(summonerAPI.GetSummonerDetails())
    elif msg == "raiderio help":
        await channel.send(message.helpString)


client.run(os.getenv('TOKEN'))
