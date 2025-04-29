import discord
from discord.ext import commands

# Create a bot instance
intents = discord.Intents.default()  # You can enable specific intents here if needed
bot = commands.Bot(command_prefix="!", intents=intents)

# Event when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Command that responds to !hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.display_name}!')

# Run the bot with your bot token
bot.run('MTM0OTY4MjYwOTM0NDYxNDQ0Mg.GL8IGg.nT5Jd4qbFsvy5ST4G_v87hm9nNyt9DVGjuOvI0')  # Replace 'YOUR_BOT_TOKEN' with your actual bot token
