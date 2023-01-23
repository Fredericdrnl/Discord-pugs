from discord.ext import commands
import asyncio
import selectors
from random import randint

selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)

class PugsBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".")
        self.players : list[str] = []
        self.team1 : list[str] = []
        self.team2 : list[str] = []
        self.rand : int
        self.joueur : str

        @self.command(name='addMe')
        async def addMe(self, ctx):
            self.players.append(str(ctx.author))
            print(self.players)
            await ctx.channel.send(f"{ctx.author.mention} added")

    @commands.command(name="addPlayer")
    async def addPlayer(self, ctx):
        self.players.append(str(ctx.author.name))
        await ctx.channel.send(f"{ctx.author.name} added")

    @commands.command(name="removePlayer")
    async def removePlayer(self, ctx, player):
        self.players.pop(player.display_name.index())
        await ctx.channel.send(f"{player.display_name} removed")

    @commands.command(name="checkList")
    async def checkList(self, ctx):
        if len(self.players) == 0:
            await ctx.channel.send("No one on list")
        for player in self.players:
            await ctx.channel.send(player)

    @commands.command(name="clearList")
    async def clearList(self, ctx):
        self.players.clear()
        await ctx.channel.send("list cleared")

    @commands.command(name="pugs")
    async def pugs(self, ctx):
        if len(self.players) < 9:
            await ctx.channel.send("Pas assez de joueur pour PUGS")
        else:
            for i in range(len(self.players) // 2):
                rand = randint(0, len(self.players) -1)
                joueur = self.players.pop(rand)
                self.team1.append(joueur)
                rand = randint(0, len(self.players) -1)
                joueur = self.players.pop(rand)
                self.team2.append(joueur)

            await ctx.channel.send("\n====== TEAM 1 ======")
            for player in self.team1:
                await ctx.channel.send("-" + player)

            await ctx.channel.send("\n====== TEAM 2 ======")
            for player in self.team2:
                await ctx.channel.send("-" + player)
            await ctx.channel.send("\n\nGL !")

bot = PugsBot()
bot.run(open("token.txt", "r").readline())