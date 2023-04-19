import os
import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Aquí puedes definir las funciones y eventos de tu bot
# que se ejecutarán cuando el bot esté en línea.
# ...

client.run('TOKEN')

client = discord.Client()
client.run(os.environ['DISCORD_TOKEN'])