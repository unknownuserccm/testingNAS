import discord
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

TOKEN = os.getenv("DISCORD_TOKEN")  # Get the bot token from environment variables

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run(TOKEN)
