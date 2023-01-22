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

    if message.content.lower() == "join pugs":
        PLAYERS.append(str(message.author))
        print(PLAYERS)
        await message.channel.send(f"{message.author.mention} added")

    if message.content.lower() == "check players":
        if len(PLAYERS) == 0:
            await message.channel.send("No one on list")
        for player in PLAYERS:
            await message.channel.send(player)

    if message.content.lower() == "clear players":     
        PLAYERS.clear()
        await message.channel.send("list cleared")

    if message.content.lower() == "go pugs":
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
                await message.channel.send("-" + player)

            await message.channel.send("\n====== TEAM 2 ======")
            for player in Team2:
                await message.channel.send("-" + player)

            await message.channel.send("\n\nGL !")
        PLAYERS.clear()   



client.run(open("token.txt", "r").readline())
