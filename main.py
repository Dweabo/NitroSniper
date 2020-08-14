import discord
import datetime
import requests
import asyncio
import json
import random
from discord.ext import commands





client = commands.Bot(command_prefix=(";"), self_bot=True)


token = "mfa.U3IyS-PTjeGJE2DzyG60fGJrKQ7ZFlhh44rIv_IBK8XqwZ2UcBK0TPKQK4Isrwih2lSpgdUGRT7ZkCaAG9cy" #Replace with discord token



text="\\"

@client.event
async def on_connect():
    x=1
    while True: #Infinite loop
        channel = client.get_channel(730734099240714240)
        msg = ["זה בוט xp" , "This is an xp bot"]
        randomsg = random.choice(msg)
        await channel.send(randomsg)
        await asyncio.sleep(10)
        x += 1
    while True: #Change status
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="/"))
            await asyncio.sleep(1)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="-"))
            await asyncio.sleep(1)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="|"))
            await asyncio.sleep(1)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="-"))
            await asyncio.sleep(1)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text))
            await asyncio.sleep(1)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="|"))
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
