import discord
from discord.ext import commands
from random import randint
import asyncio
import selectors

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■          ■■■■               ■■■■               ■■■■             ■■■■■■ #
# ■■■■■■  ■■■■■   ■■■■   ■■      ■■  ■■■■    ■■■■■■■■   ■■■■    ■■■■■■   ■■■■■■ #     
# ■■■■■■  ■■   ■  ■■■■   ■■      ■■  ■■■■   ■■■         ■■■■   ■■        ■■■■■■ # 
# ■■■■■■  ■■■■■   ■■■■   ■■      ■■  ■■■■   ■■    ■■■■  ■■■■     ■■■     ■■■■■■ #       
# ■■■■■■  ■■      ■■■■   ■■■    ■■■  ■■■■   ■■     ■■   ■■■■      ■■■    ■■■■■■ #      
# ■■■■■■  ■■      ■■■■    ■■■■■■■    ■■■■    ■■■■■■■■   ■■■■   ■■■■■     ■■■■■■ #    
# ■■■■■■          ■■■■               ■■■■               ■■■■             ■■■■■■ #                
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# Author : WarFlay#8465 on discord

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ INIT BOT ■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #

selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)

print("[INFO] Launching bot...")
PLAYERS : list[str] = []

intent = discord.Intents.default()
intent.members = True
intent.message_content = True
bot = commands.Bot(command_prefix="+", intents=intent)

@bot.event
async def on_ready():
    print("[INFO] Bot is ready !")


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■ COMMAND ■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong ! ({round(bot.latency * 1000)}ms)')

# Le joueur qui écrit le message s'inscrit au pugs.
@bot.command()
async def jpu(ctx):
    id : str = "<@" + str(ctx.author.id) + ">"
    PLAYERS.append(id)
    print(PLAYERS)
    await ctx.send(f"<@{ctx.author.id}> added")

#inscrit le joueur mentionné au pugs
@bot.command()
async def jpl(ctx):
    for user_mentioned in ctx.message.mentions:
        id : str = "<@" + str(user_mentioned.id) + ">"
        PLAYERS.append(id)
        await ctx.send(id + " added")

# Regarder la liste des joueurs inscrits.
@bot.command()
async def chp(ctx):
    if len(PLAYERS) == 0:
        await ctx.send("No one on list")
    else:
        await ctx.send("Voici la liste des joueurs inscrits :")
        for player in PLAYERS:
            print(player)
            await ctx.send("- " + player)

#supprimer un joueur de la liste (le supprime une seule fois).
@bot.command()
async def rp(ctx):
    for user_mentioned in ctx.message.mentions:
        user : str = "<@" + str(user_mentioned.id) + ">"
        print(user)
        if user in PLAYERS:
            PLAYERS.pop(PLAYERS.index(user))
            await ctx.send("Le joueur " + str(user) + " à été supprimé de la liste.")
        else:
            await ctx.send("Le joueur " + str(user) + " n'est pas dans la liste.")   

# Supprimer les éléments de la liste des participants. 
@bot.command()
async def clp(ctx):
    PLAYERS.clear()
    await ctx.send("list cleared")

# Génère la liste des 2 équipes composées aléatoirement.
@bot.command()
async def gpu(ctx):

    Team1 : list[str] = []
    Team2 : list[str] = []
    rand : int
    joueur : str

    if len(PLAYERS) < 9:
        await ctx.send("Pas assez de joueur pour PUGS")
    else:
        for i in range(len(PLAYERS) // 2):
            rand = randint(0, len(PLAYERS) -1)
            joueur = PLAYERS.pop(rand)
            Team1.append(joueur)
            rand = randint(0, len(PLAYERS) -1)
            joueur = PLAYERS.pop(rand)
            Team2.append(joueur)

        await ctx.send("\n====== TEAM 1 ======")
        for player in Team1:
            await ctx.send("- " + player)

        await ctx.send("\n====== TEAM 2 ======")
        for player in Team2:
            await ctx.send("- " + player)
        await ctx.send("\n\nGL !")

#génère les teams avec les numéros de 1 à 10 qui représente le placement dans un vocal discord.
@bot.command()
async def td(ctx):

    Team1 : list[str] = []
    Team2 : list[str] = []
    rand : int
    joueur : str

    on_discord : list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(on_discord) // 2):
        rand = randint(0, len(on_discord) -1)
        joueur = on_discord.pop(rand)
        Team1.append(joueur)
        rand = randint(0, len(on_discord) - 1)
        joueur = on_discord.pop(rand)
        Team2.append(joueur)

    await ctx.send("\n====== TEAM 1 ======")
    for player in Team1:
        await ctx.send("- " + str(player))

    await ctx.send("\n====== TEAM 2 ======")
    for player in Team2:
        await ctx.send("- " + str(player))
    await ctx.send("\n\nGL !")



# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■ RUN ■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #

bot.run(open("token.txt", "r").readline())