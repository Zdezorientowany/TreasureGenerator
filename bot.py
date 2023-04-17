import discord
import asyncio
import sys
import configparser
from utils import colors, format_text

result = sys.argv[1]

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config.get('CONFIG', 'API_KEY')
channel_id = config.get('CONFIG', 'CHANNEL_ID')

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    # print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(int(channel_id))
    await channel.send("```"+ result + "```")
    await client.close()

async def main():
    await client.start(str(api_key))
    print(format_text("Sent!","light"))

print(format_text("Sending the output to DISCORD","light"))
asyncio.run(main())