import discord
from discord.ext import commands
from hype.logging import _log

async def on_shard_ready(shard_id):
    _log.info(f"Shard ID {shard_id} connected to discord gateway")