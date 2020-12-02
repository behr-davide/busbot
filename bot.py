import os
import discord
import aiocron
import logging 
from random import choice
from arrr import translate, _PIRATE_PHRASES
from discord.ext import commands
from datetime import datetime
from dotenv import load_dotenv
from functools import lru_cache
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
MAIN_CHANNEL = 372152246156263425

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', intents=intents)
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


def get_members_by_role(members, role_name):
    role_members = []
    for member in members:
        for role in member.roles:
            if role.name.lower() == role_name.lower():
                role_members.append(member)
    return role_members


@bot.command()
async def members(ctx, role):
    members = get_members_by_role(ctx, role)
    await ctx.send(members)


@bot.command(name="randommember")
async def random_member(ctx):
    uroh_members = get_members_by_role(ctx.guild.members, "uroh")
    chosen_member = choice(uroh_members)
    await ctx.send(chosen_member.display_name)


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


@aiocron.crontab("0 11 * * *")
async def scheduled_member_of_the_day():
    channel = bot.get_channel(MAIN_CHANNEL)
    members = bot.get_all_members()
    uroh_members = get_members_by_role(members, "uroh")
    member = choice(uroh_members)
    embed = discord.Embed()
    embed.set_image(url=member.avatar_url)
    await channel.send(content=f"{member.mention} is the URoH member of the day!", embed=embed)


bot.run(TOKEN)
