import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('Bot is Ready')

@client.event
async def on_memeber_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_memeber_removed(member):
    print(f'{member} has been removed from a server.')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')



@client.command()
async def hurt_me(ctx):
    insult = [ 'Can you legs breathe in those jeans?',
               'You are smelly.',
               'What died in here?',
               'Oh well looks who decides to speak',
               'Too much effort',
               'Baka!']
    await ctx.send(f'{random.choice(insult)}')


@client.command()
aysnc def help(ctx):
    await ctx.send()

client.run('NzEzMjQ2MDUyOTcwMzk3Nzk0.XsdUXA.6-Q2rtKfj_QnkwQr-vPhC1SCnhM')