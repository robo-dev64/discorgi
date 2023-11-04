import discord
import os
from discord.ext import commands
import asyncio



intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '-', intents = intents)

bot.remove_command("help")

@bot.event
async def on_ready():
    print("Corgi is up!")
    print("-"*20)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("Ping!")


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)


token = os.getenv("TOKEN")

asyncio.run(main())
