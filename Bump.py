import discord
from discord.ext import commands

class Bump:
    """Bump servers!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def b(self):
        """Bumps servers!"""

        #Your code will go here
        await self.bot.say("dlm!bump")
        await self.bot.say("=bump")

def setup(bot):
    bot.add_cog(Bump(bot))
