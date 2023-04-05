import discord
import asyncio
from main import generate_treasures_for_discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(1092570289843490897)
    await channel.send("```"+ generate_treasures_for_discord() + "```")
    await client.close()

async def main():
    await client.start('MTA5MjU2NTQ5NTQ2ODgwMjEzOQ.GqKIUK.dgPvt--rsqGpK-mPtuNmXZccVWdYXv2znI_h4A')
    print("Finished")

print("\033[93m=======Sending the output to DISCORD=======\033[0m")
asyncio.run(main())





#MTA5MjU2NTQ5NTQ2ODgwMjEzOQ.GqKIUK.dgPvt--rsqGpK-mPtuNmXZccVWdYXv2znI_h4A