import discord
from discord.ext import commands
import hype

bot = commands.Bot(command_prefix=".", intents=discord.Intents().all())
hype.init(debug=False, mobile=True)

bot.run("token")
