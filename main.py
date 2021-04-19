import discord
import datetime
import requests
import asyncio

token = "mfa.whJDn1WLNXX1Cfxkl-FeHDKR8bslKSgcvlpiBjE2i8gCxS8iWKEwmTzWQ-3O2wiNaLaCAwuLLCBNtmREb3MN"

 #Replace with discord token

client = discord.Client()

#
#@client.event # Twitch streaming status
#async def on_connect():
#    print('Ready')
#    await client.change_presence(activity=discord.Streaming(name="...", url='https://www.twitch.tv/not_streaming_lmao_suck_it'))

@client.event # Main event
async def on_message(message):
    if "discord.gift/" in message.content:
        if len(message.content) == 29:
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
                print(f"[{datetime.datetime.now()}] Successfully redeemed Nitro")
            else:
                print(f"[{datetime.datetime.now()}] Failed To Redeem Nitro")

client.run(token, bot=False) # Runs the bot
