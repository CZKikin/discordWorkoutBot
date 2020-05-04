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
    except ValueError:
        await ctx.send("Zadal jsi špatně dráhu - zadej číslo v km")
        return
    
    await ctx.send(f'Uběhl jsi {distance} za {time}')
    
@client.command()
async def hilfe(ctx):
    await ctx.send('''Tož co chceš...
Ping - Vypíše ping.
Beh dráha čas - zapíše běh.
Na dalších commandech se pracuje. :)
    ''')
client.run("TOKEN_HERE")




