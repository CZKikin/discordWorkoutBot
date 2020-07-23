'''
Author: CZKikin
'''
try:
    import discord 
    from discord.ext import commands
    import klic 

except Exception as e:
    print(e)

client = commands.Bot(command_prefix = '.')

class Enter:

    def __init__(self, name, wpm):
        self.name = name
        self.wpm = wpm
    
    def __str__(self):
        return f"{self.name};{self.wpm}"


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
    
    enter = Enter(name, wpm) 
    print(str(enter))
    await add_to_table(enter, work_type)

async def add_to_table(enter, work_type):
    with open("{}.records".format(work_type),"a+") as file:
        file.write("{}\n".format(str(enter)))
    print("added to file {}.records".format(work_type))
    #await sort_the_table()


@client.command()
async def hilfe(ctx):
    await ctx.send('''Tož co chceš...
Ping - Vypíše ping bota.
Beh dráha čas - zapíše běh.
Na dalších commandech se pracuje. :)
    ''')

client.run(klic.TOKEN) #I always forgot to remove token - added file which will be never pushed


