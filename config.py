from environs import Env

env = Env()
env.read_env()

NAME = env.str('NAME')
TOKEN = env.str('TOKEN')
MY_ID = env.str('MY_ID')
NGROK = env.str('NGROK')
URL = env.str('URL')

WEBHOOK_PATH = f'/bot/{TOKEN}'
WEBHOOK_URL = f'{NGROK}{WEBHOOK_PATH}'
