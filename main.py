import os

import discord
from discord import app_commands
from dotenv import load_dotenv
from random import randrange

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "roll", description = "Roll away")
@app_commands.describe(
    number='The first value you want to add something to',
)
async def first_command(interaction, number: int):
    response = randrange(int(number))+1
    if response == 69:
        response = '<:noice:788500634424573973>'
    if response == 1:
        response = '<:YouDied:976458484398833705>'
    await interaction.response.send_message(f"Rolled {response} from {number}")

@client.event
async def on_ready():
    await tree.sync()
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
            response = '<:YouDied:976458484398833705>'
        await message.channel.send(response)

client.run(TOKEN)