import discord
from discord.ext import commands
import os

# Configurações do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Carrega cogs
@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} está online e conectado ao Discord!")
    bot.load_extension("cogs.comandos")

# Token do bot
bot.run('SEU_TOKEN_AQUI')
