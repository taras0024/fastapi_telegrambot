import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

NAME = os.getenv('NAME')
TOKEN = os.getenv('TOKEN')
MY_ID = os.getenv('MY_ID')
NGROK = os.getenv('NGROK')
URL = os.getenv('URL')

WEBHOOK_PATH = f'/bot/{TOKEN}'
WEBHOOK_URL = f'{NGROK}{WEBHOOK_PATH}'
