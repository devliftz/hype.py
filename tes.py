import discord
from discord.ext import commands
import hype

bot = commands.Bot(command_prefix=".", intents=discord.Intents().all())
hype.init(debug=False, mobile=True)

bot.run("MTA5NjQ4NDg1OTQ3Nzc1NDAwOA.GRF13B.ESsGT2MeAtTXsKdMHegpYeDtCJE6KXL-V3oC_0")