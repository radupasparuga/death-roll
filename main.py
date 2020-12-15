import os

import discord
from dotenv import load_dotenv
from random import randrange

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
    	  return

    if message.content.startswith('!roll'):
        content = message.content.split()
        response = randrange(int(content[1]))+1
        if response == 69:
            response = '<:noice:788500634424573973>'
        if response == 1:
            response = '<:YouDied:788477968976052224>'
        await message.channel.send(response)

client.run(TOKEN)