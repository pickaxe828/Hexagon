import discord
from datetime import datetime

from discord.ext import commands

async def embed(ctx, color:int, title:str, *, text:str):
    Embed = discord.Embed(title=title, description=text, color=color)
    await ctx.channel.send(embed=Embed)

#log
mode_str = ["LOG", "ERROR"]
def log_output(**kwargs):
    if isinstance(kwargs['mode'], int):
        print(
            f"[{datetime.now().time()} {mode_str[kwargs['mode']]}]: " + str(kwargs["text"]))
            
    elif isinstance(kwargs['mode'], str):
        print(
            f"[{datetime.now().time()} {kwargs['mode']}]: " + str(kwargs["text"]))
