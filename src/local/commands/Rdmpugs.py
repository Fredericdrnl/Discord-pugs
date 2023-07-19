import discord
from discord.ext import commands
from random import randint


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■ Rdmpugs ■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class RdmpugsCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def rdmpugs(self, ctx, member: discord.Member):
        """Commande permettant 2 équipes aléatoires à partir du salon vocal du joueur mentionné.
        """
        try:
            channel1 = member.voice.channel.id
        except AttributeError:
            embedNeedVocal = discord.Embed(
            title=str(member.name) + " n'est pas dans un salon vocal.",
            colour=discord.Colour.from_rgb(240, 128, 128))
            
            return await ctx.send(embed=embedNeedVocal)

        channel = self.bot.get_channel(channel1)

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
                name = str(self.bot.get_user(int(player[2:-1])))
                embedTeam1.add_field(name="- " + name, value="", inline=False)

            embedTeam1.set_footer(text="By WarFlay#8465",
                                icon_url="https://i.goopics.net/encbhm.png")

            embedTeam2 = discord.Embed(title="Team 2",
                                    colour=discord.Colour.from_rgb(172, 11, 1))
            embedTeam2.set_thumbnail(url="https://i.goopics.net/ag3mej.jpg")
            for player in Team2:
                name = str(self.bot.get_user(int(player[2:-1])))
                embedTeam2.add_field(name="- " + name, value="", inline=False)

            embedTeam2.set_footer(text="By WarFlay#8465",
                                icon_url="https://i.goopics.net/encbhm.png")

            await ctx.send(embed=embedTeam1)
            await ctx.send(embed=embedTeam2)

def setup(bot):
    bot.add_cog(RdmpugsCommand(bot))