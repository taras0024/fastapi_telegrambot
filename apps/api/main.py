from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI

from .routers import router
from ..bot import bot, dp
from ..settings import MY_ID, TOKEN, Base, database, engine
from ..utils import set_env_ngrok_url

app = FastAPI()

app.include_router(router)
Base.metadata.create_all(engine)


@app.on_event('startup')
async def on_startup():
    NGROK_URL = set_env_ngrok_url()
    WEBHOOK_URL = f'{NGROK_URL}/bot/{TOKEN}'

    await database.connect()
    webhook_info = await bot.get_webhook_info()
    print(f'{webhook_info.url} === {WEBHOOK_URL}')
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Start bot'),
            types.BotCommand('help', 'Help'),
        ]
    )

    try:
        await dp.bot.send_message(MY_ID, 'Bot started')
    except Exception as e:
        print(f'Something went wrong', e)

    webhook_info = await bot.get_webhook_info()
    print(f'{webhook_info.url} === {WEBHOOK_URL}')


@app.post('/bot/{token:str}', tags=['bot'])
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event('shutdown')
async def on_shutdown():
    await bot.get_session.close()
    await database.disconnect()
