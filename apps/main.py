from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI

from apps.routers import router
from bot import bot, dp
from config import MY_ID, WEBHOOK_PATH, WEBHOOK_URL
from db import Base, database, engine

app = FastAPI()

app.include_router(router)
Base.metadata.create_all(engine)


@app.on_event('startup')
async def on_startup():
    await database.connect()
    webhook_info = await bot.get_webhook_info()
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


@app.post(WEBHOOK_PATH, tags=['bot'])
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event('shutdown')
async def on_shutdown():
    await bot.get_session.close()
    await database.disconnect()
