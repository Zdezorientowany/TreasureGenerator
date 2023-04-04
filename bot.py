import discord
import asyncio
from main import generate_treasures

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def my_background_task():
    print("Working")
    await client.wait_until_ready()
    counter = 0
    channel = client.get_channel(1092570289843490897) # replace with channel_id
    print(channel)
    while not client.is_closed():
        counter += 1
        await channel.send(counter)
        await asyncio.sleep(60) # task runs every 60 seconds

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    channel = client.get_channel(1092570289843490897)
    await channel.send(f"""{generate_treasures()}""")

async def main():
    await client.start('MTA5MjU2NTQ5NTQ2ODgwMjEzOQ.GqKIUK.dgPvt--rsqGpK-mPtuNmXZccVWdYXv2znI_h4A')
    await client.wait_until_ready()
    # client.loop.create_task(my_background_task())
    client.loop.run_forever()

asyncio.run(main())





#MTA5MjU2NTQ5NTQ2ODgwMjEzOQ.GqKIUK.dgPvt--rsqGpK-mPtuNmXZccVWdYXv2znI_h4A