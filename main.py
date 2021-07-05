#!/usr/bin/python3
'''
Author: CZKikin
'''
try:
    import discord 
    from discord.ext import commands
    import klic 

except Exception as e:
    print(f"Failed to import!\ne")

#Client has to be defined before using decorators
client = commands.Bot(command_prefix = 'w ')

@client.event
async def on_ready():
    print("Bot is ready.")

async def isTime(ctx, minutes, seconds):
    try:
        minutes = int(minutes)
        seconds = int(seconds)
        if seconds > 59 or seconds < 0 or minutes < 0:
            await ctx.send("Špatně zadaný čas X:XX")
            return False
    except ValueError:
        await ctx.send("Zadal jsi špatně čas!")
        return False
    return True


@client.command()
async def ping(ctx):
    await ctx.send(f"Tvá odezva je: {client.latency * 1000}ms.")

@client.command()
async def run(ctx, distance, time):
    try:
        distance = float(distance)
        minutes, seconds = time.split(":") 
        if not await isTime(ctx, minutes, seconds):
            return

    except ValueError:
        await ctx.send("Zadal jsi špatně dráhu - zadej číslo v km")
        return
    
    except Exception as exx:
        await ctx.send(f"Nastala chyba bota - kontaktuj admina a pošli mu tyto informace:\n\
                distance = {distance} time = {time}\n{exx}")
        return

    author = str(ctx.author)
    author = author.split('#') 
    await ctx.send(f"Uběhl jsi {distance}km za {minutes} minut a {seconds} sekund, jen tak dál {author[0]}.")

    tableData = { "author": author[0],
            "distance": distance,
            "workType": "run",
            "minutes": minutes,
            "seconds": seconds
            }
    await saveToTable(tableData)

async def saveToTable(tableData):
    with open(tableData["workType"], "a+") as file:
        file.write(f'{tableData["author"]},{tableData["distance"]},{tableData["minutes"]},{tableData["seconds"]}')

@client.command()
async def readTable(ctx, workType):
    readData = []
    with open(workType, "r") as file:
        lines = file.readlines()
        for i in lines:
            i = i.split(",")
            readData.append(i)

    readData.sort(reverse=True, key=getScore) 
    for i in readData:
        await ctx.send(f"{i[0]}, disciplína {workType} {i[1]} za {i[2]}:{i[3]}")

def getScore(e):
    print(f"{float(e[1])/(int(e[2]) * 60 + int(e[3]))}")
    return float(e[1])/(int(e[2]) * 60 + int(e[3]))

@client.command()
async def hilfe(ctx):
    await ctx.send('''Tož co chceš...
ping - Vypíše ping bota.
run dráha čas - zapíše běh.
readTable disciplína - vypíše tabulku disciplíny
''')

client.run(klic.TOKEN) #I always forgot to remove token - added file which will be never pushed
