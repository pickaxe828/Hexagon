import discord
from discord.ext import commands


devTeamList = [465026906450821121, 381631464409792523, 147680291824074752]  #465026906450821121
alphaTesterServerList = [725299874907815978,
                         762857969732812851, 712891443970048001]
#errors
class Error():

    class DevTeamError(commands.CheckFailure):
        #Thrown when the command user is not in the Dev Team List.
        pass

    class AlphaTesterError(commands.CheckFailure):
        #Thrown when the command user is not alpha testers.
        pass

    class AlphaTestServerError(commands.CheckFailure):
        #Thrown when the command user is not alpha testers.
        pass

    class NoVoiceChannel(commands.CheckFailure):
        #Thrown when the command user is not alpha testers.
        pass


#decorators
def is_dev_team():
    async def predicate(ctx):
        if ctx.author.id in devTeamList:
            return True

        else:
            raise Error.DevTeamError
        
    
    return commands.check(predicate)


def is_alpha_test_server():
    async def predicate(ctx):
        if ctx.guild.id in alphaTesterServerList or ctx.author.id in devTeamList:
            return True

        else:
            raise Error.AlphaTestServerError
            

    return commands.check(predicate)


def testing():
    async def predicate(ctx):
        await ctx.send("This command is currently under open testing. If there is any bug/error occurs while using, please go to our support server to report it.")

    return commands.check(predicate)


def under_dev():
    async def predicate(ctx):
        '''
        info = "This command is undergoing development!"
        Embed = discord.Embed(title="\U000026a0 Error",
                              description=info,
                              color=0xFF5555)
        await ctx.channel.send(embed=Embed)
        '''
        return False

    return commands.check(predicate)
