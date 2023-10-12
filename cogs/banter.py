import discord
from discord.ext import commands

from bot import MyClient

class Banter(commands.Cog, name="banter"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(message):
        # if message.author == self.bot.user:
        #     return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

    def setup(bot): # this is called by Pycord to setup the cog
        bot.add_cog(Banter(bot)) # add the cog to the bot