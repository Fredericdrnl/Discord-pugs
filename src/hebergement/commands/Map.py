import discord
from discord.ext import commands
from random import randint

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■ Map ■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class MapCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot : commands.Bot = bot
        self.mapNAME : list[str] = [
        "Frog isle", "Jaguar falls", "Serpent beach", "Frozen Guard", "Ice mines",
        "Fish market", "Timber mill", "Stone keep", "Brightmarsh",
        "Splitstone quarry", "Ascension peak", "Warder's gate", "Shattered desert",
        "Bazaar", "Dawnforge"
        ]
        self.mapIMG : list[str] = [
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

    @commands.command()
    async def map(self, ctx):
        nb: int = randint(0, len(self.mapNAME) - 1)

        embed = discord.Embed(title= self.mapNAME[nb],
                                colour=discord.Colour.from_rgb(240, 128, 128))
        
        embed.set_image(url= self.mapIMG[nb])
        embed.set_footer(text="By WarFlay#8465",
                        icon_url="https://i.goopics.net/encbhm.png")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(MapCommand(bot))


