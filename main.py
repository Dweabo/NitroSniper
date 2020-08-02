import discord
import datetime
import requests
import asyncio

token = "mfa.6XrQjdpoBJIAKw3oPL05jddkMot70MuBIgcjx_1GMy-CrzUWze4gr7AEoF5JCoz_gaRc5WMO1uSx1csravMu" #Replace with discord token
client = discord.Client()

@client.event
async def on_connect():
    x=1
    while True: #Change status
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="3.1"))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="3.14"))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="3.141"))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="3.1415"))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="3.14159"))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="3.141592"))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="3.1415926"))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="3.14159265"))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="3.141592653"))
            x += 1
    print("Ready")


@client.event
async def on_message(message): # Sniper itself
    if "discord.gift/" in message.content:
        print("Found Nitro Gift")

        indexNum = message.content.find("discord.gift/")
        indexNum += 13
        giftCode = message.content[indexNum:indexNum+16]

        print("Gift Code:",giftCode)

        URL = "https://discordapp.com/api/v6/entitlements/gift-codes/" + giftCode + "/redeem"

        headers = {
            "authorization": "{}".format(token),
        }

        requestResponse = requests.post(url=URL, data="", headers=headers)

        print(f"[{datetime.datetime.now()}] Attempting to Redeem")

        if requestResponse.status_code == 200:
            print(f"[{datetime.datetime.now()}] Successfully Attempted To Redeem Nitro")
        else:
            print(f"[{datetime.datetime.now()}] Failed To Redeem Nitro")

client.run(token, bot=False)
