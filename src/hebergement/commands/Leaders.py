import discord
from discord.ext import commands
from random import randint

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■ Leaders ■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class LeadersCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot : commands.Bot = bot

    @commands.command()
    async def leaders(self, ctx, member: discord.Member):
        try:
            channel1 = member.voice.channel.id
        except AttributeError:

            embedNeedVocal = discord.Embed(
            title=str(member.name) + " n'est pas dans un salon vocal.",
            colour=discord.Colour.from_rgb(240, 128, 128))
            
            return await ctx.send(embed=embedNeedVocal)

        channel = self.bot.get_channel(channel1)
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
        leader1 = str(self.bot.get_user(int(leader1[2:-1])))

        embedleader1 = discord.Embed(title=leader1,
                                    colour=discord.Colour.from_rgb(1, 156, 166))
        
        embedleader1.set_footer(text="By WarFlay#8465",
                                icon_url="https://i.goopics.net/encbhm.png")

        rand = randint(0, len(players) - 1)
        leader2 = players.pop(rand)
        leader2 = str(self.bot.get_user(int(leader2[2:-1])))

        embedleader2 = discord.Embed(title=leader2,
                                    colour=discord.Colour.from_rgb(172, 11, 1))
        
        embedleader2.set_footer(text="By WarFlay#8465",
                                icon_url="https://i.goopics.net/encbhm.png")

        await ctx.send(embed=embedleader1)
        await ctx.send(embed=embedleader2)

async def setup(bot):
    await bot.add_cog(LeadersCommand(bot))