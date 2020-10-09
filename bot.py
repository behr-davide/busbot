import emoji
from arrr import translate
from datetime import datetime


def get_weekday():
    return datetime.today().strftime("%A")

def build_greeting():
    greeting = f":pirate_flag: :bus:> Hello sailors, today it is {get_weekday()}"
    return emoji.emojize(greeting)


print(translate(build_greeting()))