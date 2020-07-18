import discord
import datetime
import requests
import asyncio

token = "mfa.1OrGB9TCJLY-wZKq0sCwI-alNU4ZzYvBOmssr_E60MccHBjOsHj1_qJlKVKQBsAp5qgPzwWJTog18OBiwEEu" #Replace with discord token
client = discord.Client()

@client.event
async def on_connect():
    x=1
    while True:
            await client.change_presence(activity=discord.Streaming(name="H", url='https://www.twitch.tv/'))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Streaming(name="He", url='https://www.twitch.tv/'))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Streaming(name="Hel", url='https://www.twitch.tv/'))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Streaming(name="Hell", url='https://www.twitch.tv/'))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Streaming(name="Hello", url='https://www.twitch.tv/'))
            x += 1
    print("ready")




@client.event
async def on_message(message):
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
