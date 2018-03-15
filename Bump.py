import discord
import time
from discord.ext import commands

class Bump:
    """Bump servers!"""

def __init__(self, bot):
    self.bot = bot

    @commands.command()
    async def bump(self):
        """Bumps servers!"""

#Your code will go here
    await self.bot.say("=bump")
    await self.bot.say("dlm!bump")

def setup(bot):
    bot.add_cog(Bump(bot))
