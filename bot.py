import discord
import asyncio
from main import generate_treasures

intents = discord.Intents(messages=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

async def start_bot():
    try:
        await client.start('MTA5MjU2NTQ5NTQ2ODgwMjEzOQ.GwbmqM.1OvJtA_p8wPntVjVbaKW6iMLMX7cpxgLASfVZU')
    except Exception as e:
        print("Failed to start bot: ", e)

@client.event
async def send_treasures():
    await client.wait_until_ready()
    channel = client.get_channel(int(1092570289843490897))
    while not client.is_closed():
        if client.is_ready():
            await channel.send(generate_treasures())
        await asyncio.sleep(60)  # send message every 60 seconds

if __name__ == "__main__":
    asyncio.get_event_loop().create_task(start_bot())
    asyncio.get_event_loop().create_task(send_treasures())
    asyncio.get_event_loop().run_forever()