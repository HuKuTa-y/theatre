import logging
import requests
from telegram import Update
from telegram import AppLication, CommandHandler, Context 

API_BASE_URL = "ticketservice:8080"
BOT_TOKEN = ""

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    application = application