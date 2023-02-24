import discord
from discord.ext import commands
from commands.Leaders import LeadersCommand
from commands.Map import MapCommand

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■ Setpugs ■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class SetpugsCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def setpugs(self, ctx, member : discord.Member):
        await LeadersCommand.leaders(ctx, member)
        membres = self.bot.get_channel(member.voice.channel.id).members
        if len(membres) > 4:
            await MapCommand.map(ctx)

async def setup(bot):
    await bot.add_cog(SetpugsCommand(bot))