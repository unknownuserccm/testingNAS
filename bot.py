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
bot.run('MTM2NjcxMDk5ODk0OTY5MTQ1Mg.GJHd2n.0cUNcSO5DBlv3oppUWiqYw-hC6rU0iPml33A2o')  # Replace 'YOUR_BOT_TOKEN' with your actual bot token
