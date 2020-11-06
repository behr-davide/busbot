import os
import discord
import aiocron
import logging 
from random import choice
from arrr import translate, _PIRATE_PHRASES
from discord.ext import commands
from datetime import datetime
from dotenv import load_dotenv


TOKEN = os.getenv("DISCORD_TOKEN")
MAIN_CHANNEL = 372152246156263425


bot = commands.Bot(command_prefix='?')
logging.basicConfig(filename='busbot.log', level=logging.INFO)


def get_weekday():
    return datetime.today().strftime("%A")


def build_greeting():
    english_greeting = f"Hello sailors, today it is {get_weekday()}"
    return f":pirate_flag: :bus: {choice(_PIRATE_PHRASES)} {translate(english_greeting)}!"


def choose_cat_pic():
    catters_path = "assets"
    cat_pics = os.listdir(catters_path)
    return f"{catters_path}/{choice(cat_pics)}"


@bot.event
async def on_ready():
    logging.info("-" * 10)
    logging.info("Logged in to server as...")
    logging.info(bot.user.name)
    logging.info(bot.user.id)
    logging.info("-" * 10)


@bot.command()
async def day(ctx):
    greeting = build_greeting()
    await ctx.send(greeting)


@bot.command()
async def pirate(ctx, message):
    await ctx.send(translate(message))


@bot.command()
async def catters(ctx):
    await ctx.send(file=discord.File(choose_cat_pic()))


@aiocron.crontab("0 10 * * *")
async def scheduled_greeting():
    channel = bot.get_channel(MAIN_CHANNEL)
    greeting = build_greeting()
    await channel.send(greeting)


bot.run(TOKEN)