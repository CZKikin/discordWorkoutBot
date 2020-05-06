'''
Author: CZKikin
'''
try:
    import discord 
    from discord.ext import commands

except Exception as e:
    print(e)

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("RoBot je připraven.")

@client.command()
async def ping(ctx):
    await ctx.send(f"Tvá odezva je: {client.latency * 1000}ms, Tvůj workoutbot_beta :)")

@client.command()
async def beh(ctx, distance, time):
    try:
        distance = float(distance)
        minutes, seconds = time.split(":")    

    except ValueError:
        await ctx.send("Zadal jsi špatně dráhu - zadej číslo v km")
        return
    
    except Exception as exx:
        await ctx.send("Nastala chyba bota - kontaktuj admina :)")
        print(f"ERROR WITH ARGUMENTS distance = {distance} time = {time}\n{exx}")
        return

    try:
        minutes = int(minutes)
        seconds = int(seconds)
        if seconds > 59 or seconds < 0 or minutes < 0:
            await ctx.send("Špatně zadaný čas X:XX")
            return
    except ValueError:
        await ctx.send("Zadal jsi špatně čas!")
        return

    print(minutes, seconds)
    author = str(ctx.author)
    author = author.split('#') 
    await ctx.send(f"Uběhl jsi {distance}km za {minutes} minut a {seconds} sekund, jen tak dál {author[0]}.")
    
async def save_table():
    pass

@client.command()
async def hilfe(ctx):
    await ctx.send('''Tož co chceš...
Ping - Vypíše ping bota.
Beh dráha čas - zapíše běh.
Na dalších commandech se pracuje. :)
    ''')
client.run("FUCKING_DO_NOT_PUT_HERE_TOKEN")

