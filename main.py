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

# Add yourself on pugs list.
@bot.command()
async def jpu(ctx):
    id : str = "<@" + str(ctx.author.id) + ">"
    PLAYERS.append(id)
    embedjpu = discord.Embed(title=f"{ctx.author.name} added", colour=discord.Colour.from_rgb(240,128,128))
    embedjpu.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")
    await ctx.send(embed=embedjpu)

# Add the mentioned players on pugs list.
@bot.command()
async def jpl(ctx):
    for user_mentioned in ctx.message.mentions:
        id : str = "<@" + str(user_mentioned.id) + ">"
        name = str(user_mentioned.name)
        PLAYERS.append(id)
        embedjpl = discord.Embed(title=name + " added",colour=discord.Colour.from_rgb(240,128,128))
        embedjpl.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")
        await ctx.send(embed=embedjpl)

# Remove mentioned players from the pugs list.
@bot.command()
async def rp(ctx):
    embedrp = discord.Embed(title="Remove players", description="Remove players from pugs's list",colour=discord.Colour.from_rgb(240,128,128))
    for user_mentioned in ctx.message.mentions:
        user : str = "<@" + str(user_mentioned.id) + ">"
        name = str(user_mentioned.name)
        if user in PLAYERS:
            PLAYERS.pop(PLAYERS.index(user))
            embedrp = discord.Embed(title=name + " à été supprimé de la liste.",colour=discord.Colour.from_rgb(240,128,128))
        else:
            embedrp = discord.Embed(title=name + " n'est pas dans la liste.",colour=discord.Colour.from_rgb(240,128,128))
    embedrp.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")
    await ctx.send(embed=embedrp) 

# Clear pugs list. 
@bot.command()
async def clp(ctx):
    PLAYERS.clear()
    embedclp = discord.Embed(title="List cleared",colour=discord.Colour.from_rgb(240,128,128))
    embedclp.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")
    await ctx.send(embed=embedclp)

# Show the pugs list.
@bot.command()
async def chp(ctx):
    if len(PLAYERS) == 0:
        embedchp = discord.Embed(title="No one on list",colour=discord.Colour.from_rgb(240,128,128))
    else:
        embedchp = discord.Embed(title="Voici la liste des players inscrits :" , colour=discord.Colour.from_rgb(240,128,128))
        for player in PLAYERS:
            name = str(bot.get_user(int(player[2:-1])))
            embedchp.add_field(name= "- " + name, value="", inline=False)
    embedchp.add_field(name = "(" + str(len(PLAYERS)) + " Players)", value="", inline=False)
    embedchp.set_footer(text ="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")
    await ctx.send(embed=embedchp)

# Create and show teams for pugs.
@bot.command()
async def gpu(ctx):

    Team1 : list[str] = []
    Team2 : list[str] = []
    playersCopy : list[str] = PLAYERS.copy()
    rand : int
    player : str

    if len(playersCopy) < 4:
        embedNeedPlayer = discord.Embed(title="Pas assez de player pour PUGS (4 > nb)",colour=discord.Colour.from_rgb(240,128,128))
        embedNeedPlayer.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")
        await ctx.send(embed=embedNeedPlayer)
    else:
        nbPlayer : int = len(playersCopy)
        if len(playersCopy) > 10:
            nbPlayer = 10
        for i in range(nbPlayer // 2):
            rand = randint(0, len(playersCopy) -1)
            player = playersCopy.pop(rand)
            Team1.append(player)
            rand = randint(0, len(playersCopy) -1)
            player = playersCopy.pop(rand)
            Team2.append(player)

        embedTeam1 = discord.Embed(title="Team 1", description="Composition of Team 1",colour=discord.Colour.from_rgb(1, 156, 166))
        embedTeam1.set_thumbnail(url="https://i.goopics.net/crdhux.jpg")
        for player in Team1:
            name = str(bot.get_user(int(player[2:-1])))
            embedTeam1.add_field(name= "- " + name, value="", inline=False)
        embedTeam1.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")

        embedTeam2 = discord.Embed(title="Team 2", description="Composition of Team 2", colour=discord.Colour.from_rgb(172, 11, 1))
        embedTeam2.set_thumbnail(url="https://i.goopics.net/ag3mej.jpg")
        for player in Team2:
            name = str(bot.get_user(int(player[2:-1])))
            embedTeam2.add_field(name= "- " + name, value="", inline=False)
        embedTeam2.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")
        
        await ctx.send(embed=embedTeam1)
        await ctx.send(embed=embedTeam2)

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

    embedTeam1 = discord.Embed(title="Team 1", description="Composition of Team 1",colour=discord.Colour.from_rgb(1, 156, 166))
    embedTeam1.set_thumbnail(url="https://i.goopics.net/crdhux.jpg")
    for player in Team1:
        embedTeam1.add_field(name= "- " + str(player), value="", inline=False)
    embedTeam1.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")

    embedTeam2 = discord.Embed(title="Team 2", description="Composition of Team 2", colour=discord.Colour.from_rgb(172, 11, 1))
    embedTeam2.set_thumbnail(url="https://i.goopics.net/ag3mej.jpg")
    for player in Team2:
        embedTeam2.add_field(name= "- " + str(player), value="", inline=False)
    embedTeam2.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")
    
    await ctx.send(embed=embedTeam1)
    await ctx.send(embed=embedTeam2)

# Shows the details of the bot commands
@bot.command()
async def helps(ctx):
    embed = discord.Embed(title="Help", description="All description of BOT's commands", colour=discord.Colour.from_rgb(240,128,128))
    embed.set_thumbnail(url="https://i.goopics.net/ykuh2d.jpg")
    embed.add_field(name="- jpu (Join pugs)", value="You join the pugs list.", inline=False)
    embed.add_field(name="- jpl [players's mentions] (Join players)", value="The players mentioned join the pugs list.", inline=False)
    embed.add_field(name="- clp (Clear players)", value="Clear the list of pugs.", inline=False)
    embed.add_field(name="- rp [players's mentions] (Remove players)", value="Remove the mentioned players from the list.", inline=False)
    embed.add_field(name="- chp (Check players)", value="Show the list of pugs.", inline=False)
    embed.add_field(name="- gpu (Go pugs)", value="Create and show the teams for pugs.", inline=False)
    embed.add_field(name="- od (To discord)", value="Create and show teams with numbers that represent the place of the person in the voice lounge.", inline=False)
    embed.set_footer(text="By WarFlay#8465", icon_url="https://i.goopics.net/encbhm.png")
    await ctx.send(embed=embed)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■ RUN ■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #

bot.run(open("token.txt", "r").readline())