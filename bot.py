from dotenv import load_dotenv
import os
import discord

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!doug'):
        await message.add_reaction('👀')
        await message.channel.send('give me your kidneys')

client.run(TOKEN)
