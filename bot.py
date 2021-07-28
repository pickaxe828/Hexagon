import os
import sys
import discord

from discord.ext.commands.converter import PartialEmojiConverter

import cmds.core
from cmds.core import Cog_Extension
from cmds.core import functions
from cmds.core import decorators
from cmds.core import setups

from discord.ext import commands, tasks
from discord.ext.commands.cooldowns import BucketType


functions.log_output(mode=0, text=f"Library import finished.")

prefix = str(setups.prefix())
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)
debug_token = setups.token.debug_TOKEN
token = setups.token.TOKEN

statusLoopCount = 0

bot.remove_command('help')

functions.log_output(mode=0, text=f"Initialize finished.")

@bot.command()
@decorators.is_dev_team()
async def load(ctx, ext_name: str):    
    try:
        bot.unload_extension(f"cmds.{ext_name}")
        info = f"Extension {ext_name} has loaded sucessfully!"
        Embed = discord.Embed(title="\U00002705 Success",
                              description=info,
                              color=0x77B255)
        await ctx.channel.send(embed=Embed)


    except:
        info = f"Can't load extension: {ext_name}"
        Embed = discord.Embed(title="\U000026a0 Unknown extension",
                              description=info,
                              color=0xFFCC4D)
        await ctx.channel.send(embed=Embed)



@bot.command()
@decorators.is_dev_team()
async def unload(ctx, ext_name: str):
    try:
        bot.unload_extension(f"cmds.{ext_name}")
        info = f"Extension {ext_name} has unloaded sucessfully!"
        Embed = discord.Embed(title="\U00002705 Success",
                              description=info,
                              color=0x77B255)
        await ctx.channel.send(embed=Embed)

        functions.log_output(mode=0, text=f"Extension {ext_name} was unloaded")

    except:
        info = f"Can't unload extension: {ext_name}"
        Embed = discord.Embed(title="\U000026a0 Unknown extension",
                              description=info,
                              color=0xFFCC4D)
        await ctx.channel.send(embed=Embed)


@bot.command()
@decorators.is_dev_team()
async def reload(ctx, ext_name: str):
    try:
        bot.reload_extension(f"cmds.{ext_name}")
        info = f"Extension {ext_name} has reloaded sucessfully!"
        Embed = discord.Embed(title="\U00002705 Success",
                              description=info,
                              color=0x77B255)
        await ctx.channel.send(embed=Embed)

        functions.log_output(mode=0, text=f"Extension {ext_name} was reloaded")

    except:
        info = f"Can't reload extension: {ext_name}"
        Embed = discord.Embed(title="\U000026a0 Unknown extension",
                              description=info,
                              color=0xFFCC4D)
        await ctx.channel.send(embed=Embed)



@bot.command()
@decorators.is_dev_team()
async def logout(ctx):
    await ctx.send("Bot stopping...")
    bot.logout()


#extension loader
dir_filter = ["music.py"]
for Filename in os.listdir("./cmds"):
    if Filename.endswith(".py") and not Filename in dir_filter:
        bot.load_extension(f"cmds.{Filename[:-3]}")



if __name__ == "__main__":
    if '--debug' in sys.argv:
        functions.log_output(mode=0, text="Debug mode ENABLED.")
        bot.run(debug_token)

    else:
        
        bot.run(token)



