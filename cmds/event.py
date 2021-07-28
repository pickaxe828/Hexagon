import os
import discord

from discord.ext import tasks
from discord.ext import commands
from discord.ext.commands.core import command

from .core import dev_guild, log_output, infos
from .core import Cog_Extension
from .core import functions
from .core import decorators
from .core import setups


class Event(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot
    


    #status_loop
    @tasks.loop(seconds=60)
    async def status_loop(self):

        status_loop_count = 0
        status_list = [f"📢{infos.prefix}help ",
                      f"📢I am working for {len(self.bot.guilds)} servers!!! ",
                      f"📢I am working for {len(self.bot.users)} people!!! ",
                      f"📢I am working since 22/5/2020!!! "]
        await self.bot.change_presence(activity=discord.Game(name=status_list[status_loop_count] + f"|💻Developer: Pickaxe828#4395 | ✅{infos.version}"))
        status_loop_count = status_loop_count + 1
        if status_loop_count == len(status_list):
            status_loop_count = 0


    #errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):

        #    description = f"`{infos.prefix}{ctx.command.name}` is missing one or more arguments!"
        #    Embed = discord.Embed(title="\U000026a0 Error",
        #                          description=description,
        #                          color=0xDD2E44)
        #    await ctx.send(embed=Embed)

            raise error

        elif isinstance(error, discord.ext.commands.errors.CommandNotFound):
            pass


        elif isinstance(error, decorators.Error.DevTeamError):
            
            description = f"`{infos.prefix}{ctx.command.name}` command is only for Dev Team!"
            Embed = discord.Embed(title="\U000026a0 No permission",
                                  description=description,
                                  color=0xFFCC4D)
            await ctx.send(embed=Embed)


        elif isinstance(error, decorators.Error.AlphaTestServerError):

            description = f"`{infos.prefix}{ctx.command.name}` command is only for Alpha Test servers!"
            Embed = discord.Embed(title="\U000026a0 No permission",
                                  description=description,
                                  color=0xFFCC4D)
            await ctx.send(embed=Embed)
            

        else:
            
            description = f"```py\n{error}```"
            Embed = discord.Embed(title="\U000026a0 Unknown error",
                                  description=description,
                                  color=0xFFCC4D)
            await ctx.send(embed=Embed)
        


    #on_ready
    @commands.Cog.listener()
    async def on_ready(self):

        log_output(mode=0, text=f"Bot online as {self.bot.user.name}")
        self.status_loop.start()
        functions.log_output(mode=0, text=f"Status loop started.")



    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        channel = self.bot.get_channel(dev_guild.bot_join)
        bot_entry = await guild.audit_logs(action=discord.AuditLogAction.bot_add).flatten()

        await channel.send(f"Bot has get invited to `{guild.name}` by `{bot_entry[0].user.name}`")
        await bot_entry[0].user.send("Hello! Thanks for inviting me!")


def setup(bot):
    bot.add_cog(Event(bot))
