import discord

from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import command

from .core import *
from .core import Cog_Extension
from .core import functions
from .core import decorators
from .core import setups

prefix = str(setups.prefix())

class Main(Cog_Extension):
    #ping
    @commands.command(aliases=["ping!"])
    async def ping(self, ctx):
        description = f"```prolog\nLatency: {round(self.bot.latency * 1000)} ms```"
        Embed = discord.Embed(title="Pong!",
                              description=description,
                              color=0x226699)
        await ctx.send(embed=Embed)


    @commands.command()
    async def settings(self, ctx, sub, arg):
        pass



    @commands.command()
    @decorators.is_dev_team()
    async def guildlist(self, ctx):
        text = ""
        for i in range(len(self.bot.guilds)):
            text = text + self.bot.guilds[i].name + "\n"

        await ctx.send(f"```{text}\n\nTotal: {len(self.bot.guilds)}```")


    @commands.command()
    @decorators.is_dev_team()
    async def announce(self, ctx, title, text):
        Embed = discord.Embed(title=title,
                              description=text,
                              color=0x5DADEC)
        for i in range(len(self.bot.guilds)):
            try:
                await self.bot.guilds[i].system_channel.send(embed=Embed)
                await ctx.send(f"Message sent to `{self.bot.guilds[i].name}` - `{self.bot.guilds[i].system_channel.name}`")
            except:
                pass


    @commands.command(aliases=["patchnote", "patch"])
    async def patchnotes(self, ctx, *test):
        channel = self.bot.get_channel(dev_guild.patch_notes)
        messages = channel.history(limit=3)
        messages = await messages.flatten()
        if test is not None and int(test[0])-1 > 0:
            await ctx.send(messages[int(test[0])-1].content)
        else: await ctx.send(messages[0].content)


    @commands.command()
    async def log(self, ctx, *, text):
        log_output(mode=1, text=text)


    #help
    @commands.command()
    async def help(self, ctx):

        info = str('```'
                   + str(prefix)+'help: That what you used.\n'
                   + str(prefix)+'ping: For Pong and latency!\n'
                   + str(prefix)+'info: For the bot\'s info\n\n'
                   + str(prefix)+'accinfo\n'
                   + str(prefix)+'kick\n'
                   + str(prefix)+'ban\n'
                   + str(prefix)+'unban\n\n'
                   + str(prefix)+'info: For how to invite me to your own server!\n'
                   + str(prefix)+'patchnotes: For our patch notes!\n'
                   + '```')
        #'@someone: Mention random ppl in your server! (have been removed)\n\n'\
        Embed = discord.Embed(title="Help", description=info, color=0x5555FF)
        await ctx.channel.send(embed=Embed)
    

    @commands.command()
    async def info(self, ctx):
        info = "\
Hello there! I am Hexagon and I am created by Pickaxe828#4395! I will be a security bot later and now, I am pretty useless. So here is my informations!\n\
Hosting service: Linode (5 USD / Month)\n\
Invite link: [HERE](https://discord.com/api/oauth2/authorize?client_id=713064870924255263&permissions=8&scope=bot)\n\
Patch notes: `.patchnotes`\n\
Offcial server: [HERE](https://discord.gg/WbrnZQm)"

        Embed = discord.Embed(title="Informations",
                              description=info, color=0x5555FF)
        await ctx.channel.send(embed=Embed)



def setup(bot):
    bot.add_cog(Main(bot))
