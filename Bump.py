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

commands = ['bump', 'dlm!bump']

for command in commands:
    self.bot.say(command)

def setup(bot):
    bot.add_cog(Bump(bot))
