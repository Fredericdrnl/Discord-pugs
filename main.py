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
PLAYERS: list[str] = []
MAPS_IMG: list[str] = [
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/7/72/Loading_Isle.png/revision/latest/scale-to-width-down/300?cb=20200216202446',  #FROG ISLE
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/1/13/Loading_Jaguar_Falls.png/revision/latest/scale-to-width-down/300?cb=20220703100404',  #JAGUAR FALLS
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/7/7e/Loading_BeachV2.png/revision/latest/scale-to-width-down/300?cb=20161121123855',  #SERPENT BEACH
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/e/e5/Loading_NRIgloo.png/revision/latest/scale-to-width-down/300?cb=20201006103647',  #FROZEN GUARD
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/b/b2/Loading_NRMines.png/revision/latest/scale-to-width-down/300?cb=20190817013544',  #ICE MINES
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/b/b8/Loading_Village.png/revision/latest/scale-to-width-down/300?cb=20161012050227',  #FISH MARKET
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/7/7b/Loading_SpiralV2.png/revision/latest/scale-to-width-down/300?cb=20210205011206',  #TIMBER MILL
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/6/6a/Loading_Castle.png/revision/latest/scale-to-width-down/300?cb=20210831172847',  #STONE KEEP
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/d/db/Loading_Atrium.png/revision/latest/scale-to-width-down/300?cb=20170504114439',  #BRIGHTMARSH
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/4/44/Loading_Quarry.png/revision/latest/scale-to-width-down/300?cb=20170722155850',  #SPLISTONE QUARRY
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/3/38/Loading_AscensionPeak.png/revision/latest/scale-to-width-down/300?cb=20180210174622',  #ASCENSION PEAK
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/2/2b/Loading_DragonSiege.png/revision/latest/scale-to-width-down/300?cb=20220225193429',  #WARDER'S GATE 
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/3/39/Loading_ShatteredDesert.png/revision/latest/scale-to-width-down/300?cb=20190507191952',  #SHATTERED DESERT
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/e/ea/Loading_Bazaar.png/revision/latest/scale-to-width-down/300?cb=20190507192056',  #BAZAAR
  'https://static.wikia.nocookie.net/paladins_gamepedia/images/3/36/Loading_Dawnforge.png/revision/latest/scale-to-width-down/300?cb=20221029120554'  #DAWNFORGE
]

MAPS_NOM = [
  "Frog isle", "Jaguar falls", "Serpent beach", "Frozen Guard", "Ice mines",
  "Fish market", "Timber mill", "Stone keep", "Brightmarsh",
  "Splitstone quarry", "Ascension peak", "Warder's gate", "Shattered desert",
  "Bazaar", "Dawnforge"
]

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
  embedPing = discord.Embed(title=f'{round(bot.latency * 1000)}ms',
                            description="Ping of PUGS bot.",
                            colour=discord.Colour.from_rgb(240, 128, 128))
  
  embedPing.set_footer(text="By WarFlay#8465",
                       icon_url="https://i.goopics.net/encbhm.png")
  

  await ctx.send(embed=embedPing)


# Create and show teams with numbers that represent the place of the person in the voice lounge on Discord.
@bot.command()
async def od(ctx):

  Team1: list[str] = []
  Team2: list[str] = []
  rand: int
  player: str

  on_discord: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  for i in range(len(on_discord) // 2):
    rand = randint(0, len(on_discord) - 1)
    player = on_discord.pop(rand)
    Team1.append(player)
    rand = randint(0, len(on_discord) - 1)
    player = on_discord.pop(rand)
    Team2.append(player)

  embedTeam1 = discord.Embed(title="Team 1",
                             colour=discord.Colour.from_rgb(1, 156, 166))
  
  embedTeam1.set_thumbnail(url="https://i.goopics.net/crdhux.jpg")
  for player in Team1:
    embedTeam1.add_field(name="- " + str(player), value="", inline=False)
  embedTeam1.set_footer(text="By WarFlay#8465",
                        icon_url="https://i.goopics.net/encbhm.png")

  embedTeam2 = discord.Embed(title="Team 2",
                             colour=discord.Colour.from_rgb(172, 11, 1))
  
  embedTeam2.set_thumbnail(url="https://i.goopics.net/ag3mej.jpg")
  for player in Team2:
    embedTeam2.add_field(name="- " + str(player), value="", inline=False)
  embedTeam2.set_footer(text="By WarFlay#8465",
                        icon_url="https://i.goopics.net/encbhm.png")

  await ctx.send(embed=embedTeam1)
  await ctx.send(embed=embedTeam2)


# Create and show teams with the members of the voice channel where the member passed in parameter is located.
@bot.command()
async def rdmpugs(ctx, member: discord.Member):
  try:
    channel1 = member.voice.channel.id
  except AttributeError:
    embedNeedVocal = discord.Embed(
      title=str(member.name) + " n'est pas dans un salon vocal.",
      colour=discord.Colour.from_rgb(240, 128, 128))
    
    return await ctx.send(embed=embedNeedVocal)

  channel = bot.get_channel(channel1)
  #finds members connected to the channel
  members = channel.members

  players = []
  for member in members:
    players.append("<@" + str(member.id) + ">")

  Team1: list[str] = []
  Team2: list[str] = []
  rand: int
  player: str

  if len(players) < 4:
    embedNeedPlayer = discord.Embed(
      title="Pas assez de player pour PUGS (nb < 3)",
      colour=discord.Colour.from_rgb(240, 128, 128))
    
    embedNeedPlayer.set_footer(text="By WarFlay#8465",
                               icon_url="https://i.goopics.net/encbhm.png")
    
    return await ctx.send(embed=embedNeedPlayer)
  else:
    nbPlayer: int = len(players)
    if len(players) > 10:
      nbPlayer = 10
    for i in range(nbPlayer // 2):
      rand = randint(0, len(players) - 1)
      player = players.pop(rand)
      Team1.append(player)
      rand = randint(0, len(players) - 1)
      player = players.pop(rand)
      Team2.append(player)

    embedTeam1 = discord.Embed(title="Team 1",
                               colour=discord.Colour.from_rgb(1, 156, 166))
    
    embedTeam1.set_thumbnail(url="https://i.goopics.net/crdhux.jpg")
    for player in Team1:
      name = str(bot.get_user(int(player[2:-1])))
      embedTeam1.add_field(name="- " + name, value="", inline=False)

    embedTeam1.set_footer(text="By WarFlay#8465",
                          icon_url="https://i.goopics.net/encbhm.png")

    embedTeam2 = discord.Embed(title="Team 2",
                               colour=discord.Colour.from_rgb(172, 11, 1))
    embedTeam2.set_thumbnail(url="https://i.goopics.net/ag3mej.jpg")
    for player in Team2:
      name = str(bot.get_user(int(player[2:-1])))
      embedTeam2.add_field(name="- " + name, value="", inline=False)

    embedTeam2.set_footer(text="By WarFlay#8465",
                          icon_url="https://i.goopics.net/encbhm.png")

    await ctx.send(embed=embedTeam1)
    await ctx.send(embed=embedTeam2)


@bot.command()
async def map(ctx):
  nb: int = randint(0, len(MAPS_NOM) - 1)

  embed = discord.Embed(title=MAPS_NOM[nb],
                        colour=discord.Colour.from_rgb(240, 128, 128))
  
  embed.set_image(url=MAPS_IMG[nb])
  embed.set_footer(text="By WarFlay#8465",
                   icon_url="https://i.goopics.net/encbhm.png")
  await ctx.send(embed=embed)


@bot.command()
async def leaders(ctx, member: discord.Member):
  try:
    channel1 = member.voice.channel.id
  except AttributeError:

    embedNeedVocal = discord.Embed(
      title=str(member.name) + " n'est pas dans un salon vocal.",
      colour=discord.Colour.from_rgb(240, 128, 128))
    
    return await ctx.send(embed=embedNeedVocal)

  channel = bot.get_channel(channel1)
  #finds members connected to the channel
  members = channel.members

  leader1: str
  leader2: str
  players: list[str] = []
  for member in members:
    players.append("<@" + str(member.id) + ">")

  if len(players) < 4:

    embedNeedPlayer = discord.Embed(
      title="Pas assez de player pour PUGS (nb < 3)",
      colour=discord.Colour.from_rgb(240, 128, 128))
    
    embedNeedPlayer.set_footer(text="By WarFlay#8465",
                               icon_url="https://i.goopics.net/encbhm.png")
    
    return await ctx.send(embed=embedNeedPlayer)

  rand = randint(0, len(players) - 1)
  leader1 = players.pop(rand)
  leader1 = str(bot.get_user(int(leader1[2:-1])))

  embedleader1 = discord.Embed(title=leader1,
                               colour=discord.Colour.from_rgb(1, 156, 166))
  
  embedleader1.set_footer(text="By WarFlay#8465",
                          icon_url="https://i.goopics.net/encbhm.png")

  rand = randint(0, len(players) - 1)
  leader2 = players.pop(rand)
  leader2 = str(bot.get_user(int(leader2[2:-1])))

  embedleader2 = discord.Embed(title=leader2,
                               colour=discord.Colour.from_rgb(172, 11, 1))
  
  embedleader2.set_footer(text="By WarFlay#8465",
                          icon_url="https://i.goopics.net/encbhm.png")

  await ctx.send(embed=embedleader1)
  await ctx.send(embed=embedleader2)


# Shows the details of the bot commands
@bot.command()
async def helps(ctx):
  
  embedEN = discord.Embed(
    title="Help 🇫🇷",
    description="Toute la description des commandes du BOT.",
    colour=discord.Colour.from_rgb(240, 128, 128))
  
  embedEN.set_thumbnail(url="https://i.goopics.net/ykuh2d.jpg")

  embedEN.add_field(
    name="+rdmpugs [@un membre dans le vocal]",
    value="Créer et affiche les teams pour le pugs (teams randoms).",
    inline=False)
  
  embedEN.add_field(name="+leaders [@un membre dans le vocal]",
                    value="Donne 2 capitaines parmis le vocal.",
                    inline=False)
  
  embedEN.add_field(name="+map",
                    value="Donne une map aléatoire.",
                    inline=False)
  
  embedEN.set_footer(text="By WarFlay#8465",
                     icon_url="https://i.goopics.net/encbhm.png")

  embedFR = discord.Embed(title="Help 🇬🇧",
                          description="All description of BOT's commands.",
                          colour=discord.Colour.from_rgb(240, 128, 128))
  
  embedFR.set_thumbnail(url="https://i.goopics.net/ykuh2d.jpg")

  embedFR.add_field(name="+rdmpugs [@member in vocal channel]",
                    value="Create and show teams for pugs (randoms teams).",
                    inline=False)
  
  embedFR.add_field(name="+leaders [@member in vocal channel]",
                    value="Give 2 leaders among the members on vocal.",
                    inline=False)
  
  embedFR.add_field(name="+map", value="Give random map.", inline=False)

  embedFR.set_footer(text="By WarFlay#8465",
                     icon_url="https://i.goopics.net/encbhm.png")
  
  await ctx.send(embed=embedFR)
  await ctx.send(embed=embedEN)


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■ RUN ■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #

bot.run(open("token.txt", "r").readline())
