import discord
import datetime
import requests

token = "mfa.1OrGB9TCJLY-wZKq0sCwI-alNU4ZzYvBOmssr_E60MccHBjOsHj1_qJlKVKQBsAp5qgPzwWJTog18OBiwEEu" #Replace with discord token
client = discord.Client()

@client.event
async def on_connect():
    print("ready")
    await client.change_presence(activity=discord.Streaming(name=":3", url='https://www.twitch.tv/'))



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
