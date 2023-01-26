from types import NoneType
import discord
from discord.ext import commands
from random import randint
import asyncio
import selectors

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■          ■■■■              ■■■■              ■■■■           ■■■■■■ #
# ■■■■■■  ■■■■■   ■■■■  ■■      ■■  ■■■■   ■■■■■■■■   ■■■■   ■■■■■■  ■■■■■■ #     
# ■■■■■■  ■■   ■  ■■■■  ■■      ■■  ■■■■  ■■■         ■■■■  ■■       ■■■■■■ # 
# ■■■■■■  ■■■■■   ■■■■  ■■      ■■  ■■■■  ■■    ■■■■  ■■■■    ■■■    ■■■■■■ #       
# ■■■■■■  ■■      ■■■■  ■■■    ■■■  ■■■■  ■■     ■■   ■■■■     ■■■   ■■■■■■ #      
# ■■■■■■  ■■      ■■■■   ■■■■■■■    ■■■■   ■■■■■■■■   ■■■■  ■■■■■    ■■■■■■ #    
# ■■■■■■          ■■■■              ■■■■              ■■■■           ■■■■■■ #                
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# Author : WarFlay#8465 on discord

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ INIT BOT ■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #

# For async/await
selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)

print("[INFO] Launching bot...")
# Init for commands
PLAYERS : list[str] = []

# Init for Bot
intent = discord.Intents.default()
intent.members = True
intent.message_content = True
bot = commands.Bot(command_prefix="+", intents=intent)

# Message when bot is ready
@bot.event
async def on_ready():
    print("[INFO] Bot is ready !")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■ COMMANDS ■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #

# Know ping of the bot.
@bot.command()
async def ping(ctx):
    embedPing = discord.Embed(title=f'{round(bot.latency * 1000)}ms', description="Ping of PUGS bot.",colour=discord.Colour.from_rgb(240,128,128))
    embedPing.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")
    await ctx.send(embed=embedPing)

# Create and show teams with numbers that represent the place of the person in the voice lounge on Discord.
@bot.command()
async def od(ctx):

    Team1 : list[str] = []
    Team2 : list[str] = []
    rand : int
    player : str

    on_discord : list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(on_discord) // 2):
        rand = randint(0, len(on_discord) -1)
        player = on_discord.pop(rand)
        Team1.append(player)
        rand = randint(0, len(on_discord) - 1)
        player = on_discord.pop(rand)
        Team2.append(player)

    embedTeam1 = discord.Embed(title="Team 1", colour=discord.Colour.from_rgb(1, 156, 166))
    embedTeam1.set_thumbnail(url="https://i.goopics.net/crdhux.jpg")
    for player in Team1:
        embedTeam1.add_field(name= "- " + str(player), value="", inline=False)
    embedTeam1.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")

    embedTeam2 = discord.Embed(title="Team 2", colour=discord.Colour.from_rgb(172, 11, 1))
    embedTeam2.set_thumbnail(url="https://i.goopics.net/ag3mej.jpg")
    for player in Team2:
        embedTeam2.add_field(name= "- " + str(player), value="", inline=False)
    embedTeam2.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")
    
    await ctx.send(embed=embedTeam1)
    await ctx.send(embed=embedTeam2)

# Create and show teams with the members of the voice channel where the member passed in parameter is located.
@bot.command()  
async def ov(ctx, member : discord.Member):
    try:
        channel1 = member.voice.channel.id
    except AttributeError:
        embedNeedVocal = discord.Embed(title= str(member.name) + " n'est pas dans un salon vocal.",colour=discord.Colour.from_rgb(240,128,128))
        return await ctx.send(embed=embedNeedVocal)

    channel = bot.get_channel(channel1)
    #finds members connected to the channel
    members = channel.members 

    players = [] 
    for member in members:
        players.append("<@" + str(member.id) + ">")

    print(players)

    Team1 : list[str] = []
    Team2 : list[str] = []
    rand : int
    player : str

    if len(players) < 4:
        embedNeedPlayer = discord.Embed(title="Pas assez de player pour PUGS (nb < 3)",colour=discord.Colour.from_rgb(240,128,128))
        embedNeedPlayer.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")
        await ctx.send(embed=embedNeedPlayer)
    else:
        nbPlayer : int = len(players)
        if len(players) > 10:
            nbPlayer = 10
        for i in range(nbPlayer // 2):
            rand = randint(0, len(players) -1)
            player = players.pop(rand)
            Team1.append(player)
            rand = randint(0, len(players) -1)
            player = players.pop(rand)
            Team2.append(player)

        embedTeam1 = discord.Embed(title="Team 1",colour=discord.Colour.from_rgb(1, 156, 166))
        embedTeam1.set_thumbnail(url="https://i.goopics.net/crdhux.jpg")
        for player in Team1:
            name = str(bot.get_user(int(player[2:-1])))
            embedTeam1.add_field(name= "- " + name, value="", inline=False)
        embedTeam1.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")

        embedTeam2 = discord.Embed(title="Team 2", colour=discord.Colour.from_rgb(172, 11, 1))
        embedTeam2.set_thumbnail(url="https://i.goopics.net/ag3mej.jpg")
        for player in Team2:
            name = str(bot.get_user(int(player[2:-1])))
            embedTeam2.add_field(name= "- " + name, value="", inline=False)
        embedTeam2.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")
        
        await ctx.send(embed=embedTeam1)
        await ctx.send(embed=embedTeam2)

# Shows the details of the bot commands
@bot.command()
async def helps(ctx):
    embed = discord.Embed(title="Help", description="All description of BOT's commands", colour=discord.Colour.from_rgb(240,128,128))
    embed.set_thumbnail(url="https://i.goopics.net/ykuh2d.jpg")
    embed.add_field(name="- od (On discord)", value="Create and show teams with numbers that represent the place of the person in the voice lounge.", inline=False)
    embed.add_field(name="- ov (To voice channel)", value="Create and show teams with person on the voice channel where is the person.", inline=False)
    embed.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")
    await ctx.send(embed=embed)


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■ RUN ■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #

bot.run(open("token.txt", "r").readline())