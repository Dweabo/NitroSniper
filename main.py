from colorama import Fore, init, Style


from discord.ext import commands
import discord


client = commands.Bot(command_prefix='.', self_bot=True)
init(autoreset=True, convert=True)
client.remove_command('help')

token = 'mfa.kpTx9RILhvjZon7cikaohNRVrdbN63IE47g8My1UUGjYZr9oX7WTmlPyAXxw430uZpkiSxZ7vdImlW_Wfo_G'




@client.event
async def on_connect():
    print(Fore.GREEN+"=> Started FREESNIPER v2.0 by Dweeb")
    print(Fore.WHITE+"=> Listening for Nitro Gifts")


@client.event
async def on_message(message):
    if 'https://discord.gift/' in message.content:
        print(Fore.WHITE+"=> Found new Nitro Gift. Trying to claim it")
        code = message.content.split('https://discord.gift')[1].split(' ')[0]
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'Accept': 'application/json'}
        json = {
            'channel_id': None,
            'payment_source_id': None
        }
        r = requests.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+code+'/redeem', verify=False,headers=headers, json=json)
        if r.status_code == 200:
            print(Fore.GREEN + "=> Successfully claimed Nitro with Code: "+code)
        else:
            print(Fore.RED + "=> Code already claimed or not valid")

client.run(token, bot=False)
