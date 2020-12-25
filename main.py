import os
import discord
import messages
import random
import API.RaiderIoApi.affixesApi as affixAPI
import API.RaiderIoApi.characterApi as charAPI

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
    msg = message.content
    if message.author == client.user:
        return
    if message.content.startswith("character"):
        realm = msg.split()[1]
        charName = msg.split()[2]
        if realm == None or charName == None:
            await channel.send(messages.charHelp)
        else:
            await channel.send(charAPI.Character(realm, charName))
    elif msg.startswith("affixes"):
        await channel.send(affixAPI.Affixes())
    elif msg == "raiderio help":
        await channel.send(messages.helpString)


client.run(os.getenv('TOKEN'))
