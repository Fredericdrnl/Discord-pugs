import discord
from discord.ext import commands

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■ Helps ■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class HelpsCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot : commands.Bot = bot

    @commands.command()
    async def helps(self, ctx):
        """Commande permettant d'afficher toutes les commandes du bot avec une explication de celles-ci.
        """
        embedFR = discord.Embed(
            title="Help 🇫🇷",
            description="Toute la description des commandes du BOT.",
            colour=discord.Colour.from_rgb(240, 128, 128))
        
        embedFR.set_thumbnail(url="https://i.goopics.net/ykuh2d.jpg")

        embedFR.add_field(
            name="`+rdmpugs [@un membre dans le vocal]`",
            value="Créer et affiche les teams pour le pugs (teams randoms).",
            inline=False)
        
        embedFR.add_field(name="`+leaders [@un membre dans le vocal]`",
                            value="Donne 2 capitaines parmis le vocal.",
                            inline=False)
        
        embedFR.add_field(name="`+map`",
                            value="Donne une map aléatoire.",
                            inline=False)

        embedFR.add_field(name="`+setpugs`",
                            value="Donne 2 capitaines parmis le vocal et une map aléatoire.",
                            inline=False)
        
        embedFR.set_footer(text="By WarFlay#8465",
                            icon_url="https://i.goopics.net/encbhm.png")

        embedEN = discord.Embed(title="Help 🇬🇧",
                                description="All description of BOT's commands.",
                                colour=discord.Colour.from_rgb(240, 128, 128))
        
        embedEN.set_thumbnail(url="https://i.goopics.net/ykuh2d.jpg")

        embedEN.add_field(name="`+rdmpugs [@member in vocal channel]`",
                            value="Create and show teams for pugs (randoms teams).",
                            inline=False)
        
        embedEN.add_field(name="`+leaders [@member in vocal channel]`",
                            value="Give 2 leaders among the members on vocal.",
                            inline=False)
        
        embedEN.add_field(name="`+map`", value="Give random map.", inline=False)

        embedEN.add_field(name="`+setpugs`",
                            value="Give 2 leaders among the members on vocal and a random map.",
                            inline=False)

        embedEN.set_footer(text="By WarFlay#8465",
                            icon_url="https://i.goopics.net/encbhm.png")
        
        await ctx.send(embed=embedFR)
        await ctx.send(embed=embedEN)

def setup(bot):
    bot.add_cog(HelpsCommand(bot))
