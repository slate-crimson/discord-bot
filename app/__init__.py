import os
import dotenv
from .bot import *

__author__ = "Blake Nall"

dotenv.load_dotenv()
token = os.environ['DISCORD_ACCESS_TOKEN']

def start_app(dev: bool):
    if dev:
        start(token=token)
    return True
