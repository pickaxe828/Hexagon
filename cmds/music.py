import os
import discord
import youtube_dl
import json
import requests


from discord.ext import commands
from googleapiclient.discovery import build

from .core import *
from .core import Cog_Extension
from .core import functions
from .core import decorators
from .core import setups


ydl_opts = {
    'format': 'bestaudio', #best
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

class Music(Cog_Extension):
    @commands.command(aliases=["join", "connect"])
    async def play(self, ctx, *, search_str: str):

        #check if the song is still here
        if os.path.isfile("song.mp3"):
            try:
                os.remove("song.mp3")
            except PermissionError:
                await ctx.send("等這首歌播放完或者用b?stop 指令")
                return
        

        channel = ctx.message.author.voice.channel

        voice = ctx.guild.voice_client
        
        if voice and voice.is_connected():
            await ctx.guild.change_voice_state(channel=channel)
            member = ctx.guild.me
            await member.edit(deafen=True)
        else:
            voice = await channel.connect()

        #searching
        yt_token = setups.token.youtube_TOKEN

        youtube = build("youtube", "v3", developerKey=yt_token)

        req = youtube.search().list(q=search_str + " (Official Audio)", part="snippet", type="video", videoCategoryId=10)

        res = req.execute()

        video_ids = []
        titles = []
        descriptions = []
        video_links = []

        for i in range(len(res["items"])):
            video_ids.append(res["items"][i]["id"]["videoId"])
            titles.append(res["items"][i]["snippet"]["title"])
            descriptions.append(res["items"][i]["snippet"]["description"])
            video_links.append("https://www.youtube.com/watch?v=" + video_ids[i])

        with open("queue.json", mode="a") as jfile:
            data = json.load(jfile)
            data["data"] = {str(ctx.guild.id): {str(channel.id): []}}
            data["data"][str(ctx.guild.id)][str(channel.id)].append()

        Embed = discord.Embed(
            title=titles[0], 
            description=descriptions[0],
            color=0x55FF55)

        await ctx.channel.send(embed=Embed)
        await ctx.send(f"```json\n{res['items'][0]}\n```")
            
        #download
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_links[0]])
        

        #finding .mp3 files
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                #rename file
                os.rename(file, "song.mp3")

        #play audio
        voice.play(discord.FFmpegPCMAudio("song.mp3"),
        after=lambda e: print(f"{titles[0]} has finished playing"))


        voice.sorce = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.02

        #os.remove("song.mp3")

        print(ctx.guild.name)
        


    @commands.command()
    async def leave(self, ctx):
        voice = voice = ctx.guild.voice_client
        if voice.is_connected():
            await voice.disconnect()
            voice.cleanup()



    @commands.command()
    async def pause(self, ctx):
        voice = voice = ctx.guild.voice_client
        if voice.is_playing():
            voice.pause()



    @commands.command()
    async def resume(self, ctx):
        voice = voice = ctx.guild.voice_client
        if voice.is_paused():
            voice.resume()



    @commands.command()
    async def skip(self, ctx):
        voice = voice = ctx.guild.voice_client
        voice.stop()


def setup(bot):
    bot.add_cog(Music(bot))
