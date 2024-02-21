import os
import dotenv
import bot

__author__ = "Blake Nall"

dotenv.load_dotenv()
token = os.environ['DISCORD_ACCESS_TOKEN']

def start_app(dev: bool):
    if dev:
        bot.start(token=token)
    return True
