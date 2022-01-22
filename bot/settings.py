from os import environ
from pathlib import Path

STATIC_DIR = Path.cwd() / "bot" / "static"

COMMAND_PREFIX = "."

DEBUG = True if environ.get("DEBUG") in ["true", "True", "TRUE"] else False

BOT_TOKEN = environ.get("BOT_TOKEN")

API_BASE_URL = "https://api.sleepykittyguild.com"

TEST_GUILD_IDS = [438583304783134731]
