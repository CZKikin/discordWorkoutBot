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
        if not await is_time(ctx, minutes, seconds):
            return

    except ValueError:
        await ctx.send("Zadal jsi špatně dráhu - zadej číslo v km")
        return
    
    except Exception as exx:
        await ctx.send("Nastala chyba bota - kontaktuj admina :)")
        print(f"ERROR WITH ARGUMENTS distance = {distance} time = {time}\n{exx}")
        return

    author = str(ctx.author)
    author = author.split('#') 
    await ctx.send(f"Uběhl jsi {distance}km za {minutes} minut a {seconds} sekund, jen tak dál {author[0]}.")
    await format_data_for_table(ctx, author[0], distance, "run", minutes, seconds)
    
async def is_time(ctx, minutes, seconds):
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

async def format_data_for_table(ctx, name, work, work_type, minutes, seconds):
    wpm = 60 * (float(work) / (float(minutes) * 60 + float(seconds)))
    if work_type == "run":
        await ctx.send(f"Zvládl jsi {wpm:.2f}km/min") 
    else: 
        await ctx.send(f"Zvládl jsi {wpm:.2f}cviku(ů)/min")
    
    enter = f"{name};{wpm};{work_type}" 


async def save_table():
    pass

@client.command()
async def hilfe(ctx):
    await ctx.send('''Tož co chceš...
Ping - Vypíše ping bota.
Beh dráha čas - zapíše běh.
Na dalších commandech se pracuje. :)
    ''')
client.run("NzA2OTI5NTkwNDA4NDQ1OTU1.Xrvozg.PuMbteDygiKU3KYQrmM9Daba1Ac")

