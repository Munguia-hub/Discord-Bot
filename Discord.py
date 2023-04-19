import discord

client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
DISCORD_TOKEN=MTA5ODM1OTI3NTg1MzcyOTgxMw.GV8m-s.A50GBEoF-JFd_IUsPrPz4Pjp3ttkho9anWUmzI
