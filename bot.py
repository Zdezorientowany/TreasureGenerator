import discord
import asyncio
from main import generate_treasures
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config.get('CONFIG', 'API_KEY')
channel_id = config.get('CONFIG', 'CHANNEL_ID')

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(channel_id)
    await channel.send("```"+ generate_treasures(colors=False) + "```")
    await client.close()

async def main():
    await client.start(api_key)
    print("Finished")

print("\033[93m=======Sending the output to DISCORD=======\033[0m")
asyncio.run(main())