import os
import discord
from bot import Pugsbot
import asyncio
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
# ■■■■■■■■■■■■■■■■■■■■■■■■■ Main ■■■■■■■■■■■■■■■■■■■■■■■■■■ #
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ #
class Main():
    @staticmethod
    async def run():
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        try:
            token = open(os.path.join(__location__, "../../token.txt"), "r").read().strip("\n")
        except FileNotFoundError:
            await quit("Please create a token.txt file and place your token in it!")
        if token is None:
            await quit("Please create a token.txt file and place your token in it!")
        else:
            intent = discord.Intents.all()
            intent.members = True
            intent.message_content = True
            bot = Pugsbot(intent)
            async with bot:
                await bot.start(open("./token.txt", "r").readline())

if __name__ == '__main__':
    asyncio.run(Main.run())