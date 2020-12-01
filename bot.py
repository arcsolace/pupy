import os
import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
from youtubesearchpython import SearchVideos
import json
import wavelink

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await message.channel.send(
        f'Hey {member.name}, welcome to the server!'
    )

bot = commands.Bot(command_prefix='^')

class AlreadyConnectedToChannel(commands.CommandError):
    pass


class NoVoiceChannel(commands.CommandError):
    pass


class QueueIsEmpty(commands.CommandError):
    pass


class NoTracksFound(commands.CommandError):
    pass


class PlayerIsAlreadyPaused(commands.CommandError):
    pass


class NoMoreTracks(commands.CommandError):
    pass


class NoPreviousTracks(commands.CommandError):
    pass


class InvalidRepeatMode(commands.CommandError):
    pass

@bot.command(name = 'find')
async def find_vid(ctx, *, arg):
    search = SearchVideos(arg, offset = 1, mode = "json", max_results = 1)
    result_dict = json.loads(search.result())
    result = result_dict['search_result']
    res = result[0]
    link = res['link']
    title = res['title']
    response = f'Found: {title} | {link} | Was it what you were looking for?'.format(title, link)
    await ctx.send(response)

@bot.command(name = 'join')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(name = 'leave')
async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run(TOKEN)
