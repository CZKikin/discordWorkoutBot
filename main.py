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
    minutes, seconds = await checkParamsAndSeparateTime(ctx, distance, time)
    if minutes == None or seconds == None:
        return
    
    tableData = { "workDone": distance,
            "workType": "run", 
            "minutes": minutes,
            "seconds": seconds
            }
    await saveToTable(ctx,tableData)

@client.command()
async def pushUps(ctx, workDone, time):
    minutes, seconds = await checkParamsAndSeparateTime(ctx, workDone, time)
    if minutes == None or seconds == None:
        return
    
    tableData = { "workDone": workDone,
            "workType": "pushUps", 
            "minutes": minutes,
            "seconds": seconds
            }
    await saveToTable(ctx,tableData)

async def checkParamsAndSeparateTime(ctx, work, time):
    try:
        work = float(work)
        minutes, seconds = time.split(":") 
        if not await isTime(ctx, minutes, seconds):
            return None, None

    except ValueError:
        await ctx.send("Zadal jsi špatně dráhu/počet cviků - zadej číslo v km/počet cviků")
        return None, None
    
    except Exception as exx:
        await ctx.send(f"Nastala chyba bota - kontaktuj admina a pošli mu tyto informace:\n\
                distance = {distance} time = {time}\n{exx}")
        return None, None

    return minutes, seconds


async def saveToTable(ctx, tableData):
    author = str(ctx.author)
    author = author.split('#') 
    tableData["author"] = author[0]

    if tableData["workType"] == "run":
        await ctx.send(f"Uběhl jsi {tableData['workDone']}km \
za {tableData['minutes']} minut a {tableData['seconds']} \
sekund, jen tak dál {tableData['author']}.")
    else:
        await ctx.send(f"Zvádl jsi {tableData['workDone']} cviků \
za {tableData['minutes']} minut a {tableData['seconds']} \
sekund, jen tak dál {tableData['author']}.")

    with open(tableData["workType"], "a+") as file:
        file.write(f'{tableData["author"]},{tableData["workDone"]},{tableData["minutes"]},{tableData["seconds"]}\n')

@client.command()
async def readTable(ctx, workType):
    readData = []
    try:
        with open(workType, "r") as file:
            lines = file.readlines()
            for i in lines:
                i = i.split(",")
                readData.append(i)
    except:
        await ctx.send("Tabulka neexistuje :), nebo nastalo velký špatný")
        return

    readData.sort(reverse=True, key=getScore) 
    await ctx.send(f"{workType} begin =============")
    for index, i in enumerate(readData):
        await ctx.send(f"{index+1} {i[0]}, disciplína {workType} {i[1]} za {i[2]}:{i[3]}")
    await ctx.send(f"{workType} end ===============")

def getScore(e):
    return float(e[1])/(int(e[2]) * 60 + int(e[3]))

@client.command()
async def hilfe(ctx):
    await ctx.send('''Tož co chceš...
ping - Vypíše ping bota.
run dráha čas - zapíše běh.
pushUps počet čas - zapíše kliky.
readTable disciplína - vypíše tabulku disciplíny
''')

client.run(klic.TOKEN) #I always forgot to remove token - added file which will be never pushed
