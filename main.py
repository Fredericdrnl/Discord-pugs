from discord.ext import commands
import asyncio
import selectors
from random import randint

PLAYERS : list[str] = []
selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)

print("[INFO] Launching bot...")
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("[INFO] Bot is ready !")

@bot.command(name='addMe')
async def addMe(message):
    PLAYERS.append(str(message.author))
    print(PLAYERS)
    await message.channel.send(f"{message.author.mention} added")

@bot.command(name="addPlayer")
async def addPlayer(ctx, player):
    PLAYERS.append(str(player.display_name))
    await ctx.channel.send(f"{player.display_name} added")

@bot.command(name="removePlayer")
async def removePlayer(ctx, player):
    PLAYERS.pop(player.display_name.index())
    await ctx.channel.send(f"{player.display_name} removed")

@bot.command(name="checkList")
async def checkList(ctx):
    if len(PLAYERS) == 0:
        await ctx.channel.send("No one on list")
    for player in PLAYERS:
        await ctx.channel.send(player)

@bot.command(name="clearList")
async def clearList(ctx):
    PLAYERS.clear()
    await ctx.channel.send("list cleared")

@bot.command(name="pugs")
async def pugs(ctx):

    Team1 : list[str] = []
    Team2 : list[str] = []
    rand : int
    joueur : str

    if len(PLAYERS) < 9:
        await ctx.channel.send("Pas assez de joueur pour PUGS")
    else:
        for i in range(len(PLAYERS) // 2):
            rand = randint(0, len(PLAYERS) -1)
            joueur = PLAYERS.pop(rand)
            Team1.append(joueur)
            rand = randint(0, len(PLAYERS) -1)
            joueur = PLAYERS.pop(rand)
            Team2.append(joueur)

        await ctx.channel.send("\n====== TEAM 1 ======")
        for player in Team1:
            await ctx.channel.send("-" + player)

        await ctx.channel.send("\n====== TEAM 2 ======")
        for player in Team2:
            await ctx.channel.send("-" + player)
        await ctx.channel.send("\n\nGL !")


bot.run(open("token.txt", "r").readline())