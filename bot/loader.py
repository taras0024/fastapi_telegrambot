import asyncio

from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.types import ChatActions, KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.message import ParseMode
from aiogram.utils.markdown import bold, text

import bot.messages as ms
from config import TOKEN, MY_ID
from utils import AsyncContextManager, create_file, get_file, get_files

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(ms.START)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text(bold(ms.HELP))
    await message.answer(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def file_handler(message: types.Message):
    username = message.from_user.username
    file_id = message.document.file_id
    file_name = str(message.document.file_name.split('.')[0])

    f = await get_file(params={'name': file_name})
    if not f:
        await create_file(data={'name': str(file_name), 'file_id': str(file_id)})
        await message.reply(f'File saved')
    else:
        await message.reply(f'File `{file_name}`, already exist')

    # file_obj = await bot.get_file(file_id)
    # file_path = file_obj.file_path
    # file_io = await bot.download_file_by_id(file_id)


@dp.message_handler(commands=['files'])
async def process_file_command(message: types.Message):
    mark_up = ReplyKeyboardMarkup(resize_keyboard=True)

    # 1 ---
    # async with AsyncContextManager as s:
    #     files = await s._get_files()

    # 2 ---
    files = await get_files()

    for file in files:
        mark_up.add(KeyboardButton(file['name']))
    await bot.send_message(message.from_user.id, 'Your files: ...', reply_markup=mark_up)


@dp.message_handler()
async def echo_message(message: types.Message):
    user_id = message.from_user.id
    files = [file['name'] for file in await get_files()]

    if message.text in files:
        file = await get_file(params={'name': message.text})
        if file:
            file_id = file['file_id']
            await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
            await asyncio.sleep(1)
            await bot.send_document(user_id, file_id, caption='Your file')
    else:
        await bot.send_message(message.from_user.id, f"{message.text}")
