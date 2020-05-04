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
async def vojta(ctx):
    await ctx.send("Vojta je prostě machr :lidl:")

client.run("NzA2OTI5NTkwNDA4NDQ1OTU1.XrBZnQ.m2fAg8qHdJ0DFXjI1e_V7WblyNU")



