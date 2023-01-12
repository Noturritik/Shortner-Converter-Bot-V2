# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "17170430"))
API_HASH = os.environ.get("API_HASH", "f592f4ea158042de9f3e3cb4e09d325c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5940237917:AAFckqyS-snA4EayLl8Pq4qQI8uUClvAACk")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5911991454")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Db Name")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Ritik:ritik//!!?@cluster0.6qzamdp.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5911991454")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001893128378")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "MoViEs_xD1") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
