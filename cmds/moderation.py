import discord
import asyncio

from discord.ext import commands

from .core import *
from .core import Cog_Extension
from .core import functions
from .core import decorators
from .core import setups

from datetime import datetime as dt

class Moderation(Cog_Extension):

    #clear
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount):
        try:
            amount = int(amount)
        except:
            print('test')
            amount = 0

        await ctx.channel.purge(limit=amount+1)
        message = await ctx.send(f'***{str(amount)} messages are deleted***')
        await message.delete(delay=2.5)


    #kick
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(ctx, member: discord.Member, *, reason):
        await member.kick(reason=reason)
        await ctx.send(f'{str(member)} was **kicked** by admin, reason: {reason}')


    #ban
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(ctx, member: discord.Member, *, reason):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} was **banned** by admin, reason: {reason}')


    #unban
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            global user
            user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user} have been **unbanned** sucessfully")
            return

    #accinfo


    @commands.cooldown(1, 5)
    @commands.command(aliases=["accountinfo", "getinfo"])
    async def accinfo(self, ctx, *, user: discord.Member):

        now = dt.now()
        create_time = user.created_at  # 2020-09-15 09:14:18.055000
        current_time = dt.now()

        mobile_status = ""
        web_status = ""
        desktop_status = ""

        if user.mobile_status == discord.Status.online:
            mobile_status = f"\U0001f7e2"
        else:
            mobile_status = f"\U0001f534"

        if user.web_status == discord.Status.online:
            web_status = f"\U0001f7e2"
        else:
            web_status = f"\U0001f534"

        if user.desktop_status == discord.Status.online:
            desktop_status = f"\U0001f7e2"
        else:
            desktop_status = f"\U0001f534"

        info = "```prolog\n\
This account is created since: {create_time}\n\
This account have created for: {created_time}\n\n\
On Mobiles: {mobile_status}\n\
On Website: {web_status}\n\
On Desktop: {desktop_status}\
    ```".format(
            create_time=create_time,
            created_time=current_time - create_time,
            mobile_status=mobile_status,
            web_status=web_status,
            desktop_status=desktop_status
        )

        Embed = discord.Embed(title="Account Info",
                              description=info, color=0x5555FF)
        Embed.set_footer(
            text="\U0001f7e2 is online \n\U0001f534 is offline \nDon't ask me what does it mean again")

        await ctx.channel.send(embed=Embed)

    
def setup(bot):
    bot.add_cog(Moderation(bot))