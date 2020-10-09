import os
import logging 
from arrr import translate
from discord import commands
from datetime import datetime
from dotenv import load_dotenv


TOKEN = os.getenv("DISCORD_TOKEN")
MAIN_CHANNEL = 372152246156263425


bot = commands.Bot(command_prefix='!')
logging.basicConfig(filename='busbot.log', encoding='utf-8', level=logging.DEBUG)


def get_weekday():
    return datetime.today().strftime("%A")


def build_greeting():
    english_greeting = f"Hello sailors, today it is {get_weekday()}"
    return f":pirate_flag: :bus: {translate(english_greeting)}"


@bot.event
async def on_ready():
    logging.info("Logged in to server as...")
    logging.info(bot.user.name)
    logging.info(bot.user.id)
    logging.info("-" * 10)


@bot.command()
async def day(ctx):
    greeting = build_greeting()
    await ctx.send(greeting)


@aiocron.crontab("0 10 * * *")
async def scheduled_greeting():
    channel = bot.get_channel(MAIN_CHANNEL)
    greeting = build_greeting()
    await channel.send(greeting)


bot.run(TOKEN)