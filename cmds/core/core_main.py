import discord
from discord.ext import commands

#setup for the cog system
class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot