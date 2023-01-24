import discord
from discord.ext import commands
from random import randint
import asyncio
import selectors

PLAYERS : list[str] = []
selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)

print("[INFO] Launching bot...")
client = discord.Bot(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("[INFO] Bot is ready !")

@client.event
async def on_message(message):

    Team1 : list[str] = []
    Team2 : list[str] = []
    rand : int
    joueur : str

    # Le joueur qui écrit le message s'inscrit au pugs.
    if message.content.lower() == "!join pugs" or message.content.lower() == "!jpu":
        PLAYERS.append(str(message.author))
        print(PLAYERS)
        await message.channel.send(f"<@{message.author.id}> added")

    #inscrit le joueur mentionné au pugs
    if "!join players" in message.content.lower() or "!jpl" in message.content.lower():
        for user_mentioned in message.mentions:
            id : str = "<@" + str(user_mentioned.id) + ">"
            PLAYERS.append(id)
            await message.channel.send(id + " added")

    # Regarder la liste des joueurs inscrits.
    if message.content.lower() == "!check players" or message.content.lower() == "!chp":
        if len(PLAYERS) == 0:
            await message.channel.send("No one on list")
        else:
            await message.channel.send("Voici la liste des joueurs inscrits :")
            for player in PLAYERS:
                await message.channel.send("-" + player)


    # Supprimer les éléments de la liste des participants.
    if message.content.lower() == "!clear players" or message.content.lower() == "!clp":     
        PLAYERS.clear()
        await message.channel.send("list cleared")

    # Génère la liste des 2 équipes composées aléatoirement.
    if message.content.lower() == "!go pugs" or message.content.lower() == "!gpu":
        if len(PLAYERS) < 9:
            await message.channel.send("Pas assez de joueur pour PUGS")
        else:
            for i in range(len(PLAYERS) // 2):
                rand = randint(0, len(PLAYERS) -1)
                joueur = PLAYERS.pop(rand)
                Team1.append(joueur)
                rand = randint(0, len(PLAYERS) -1)
                joueur = PLAYERS.pop(rand)
                Team2.append(joueur)

            await message.channel.send("\n====== TEAM 1 ======")
            for player in Team1:
                await message.channel.send("- " + player)

            await message.channel.send("\n====== TEAM 2 ======")
            for player in Team2:
                await message.channel.send("- " + player)
            await message.channel.send("\n\nGL !")

client.run(open("token.txt", "r").readline())