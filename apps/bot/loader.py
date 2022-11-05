import asyncio

from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ChatActions, KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.message import ParseMode
from aiogram.utils.markdown import bold, text

from . import messages as ms
from .keyboards import list_files, file_cd, pagination_cd
from .managers import AsyncContextManager
from ..settings import TOKEN
from ..utils import exception_handler

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
@exception_handler()
async def process_start_command(message: types.Message):
    await message.reply(ms.START)


@dp.message_handler(commands=['help'])
@exception_handler()
async def process_help_command(message: types.Message):
    msg = text(bold(ms.HELP))
    await message.answer(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
@exception_handler()
async def file_handler(message: types.Message):
    file_id = message.document.file_id
    file_name = str(message.document.file_name.split('.')[0])

    async with AsyncContextManager() as session:
        file = await session.get_file({'name': file_name})

    if file:
        return await message.reply(ms.FILE_ALREADY_EXISTS % {'file_name': file_name})

    async with AsyncContextManager() as session:
        await session.create_file({'name': str(file_name), 'file_id': str(file_id)})

    await message.reply(ms.FILE_SAVE_SUCCESS)


@dp.message_handler(commands=['files'])
@exception_handler()
async def process_file_command(message: types.Message):
    mark_up = ReplyKeyboardMarkup(resize_keyboard=True)

    async with AsyncContextManager() as session:
        files = await session.get_files()

    if not files:
        await bot.send_message(message.from_user.id, ms.NO_FILES, reply_markup=mark_up)
        return

    for file in files:
        mark_up.add(KeyboardButton(file['name']))
    await bot.send_message(message.from_user.id, ms.GET_FILES, reply_markup=mark_up)


# ----------------------------------------------------------------------------------------------------------------------
#                                               Files Menu
# ----------------------------------------------------------------------------------------------------------------------
@dp.message_handler(Command('files_menu'))
@exception_handler()
async def files_menu(message: types.Message):
    await list_files(message)


@dp.callback_query_handler(file_cd.filter())
@exception_handler()
async def process_callback_file(callback: types.CallbackQuery):
    async with AsyncContextManager() as session:
        file = await session.get_file({'name': callback['data'].split(':')[1]})

    if file:
        await bot.send_chat_action(callback.from_user.id, ChatActions.UPLOAD_DOCUMENT)
        await asyncio.sleep(1)
        await bot.send_document(callback.from_user.id, file['file_id'], caption=ms.GET_FILE)


@dp.callback_query_handler(pagination_cd.filter())
@exception_handler()
async def process_callback_pagination(callback: types.CallbackQuery):
    previous_page = callback['data'].split(':')[2]
    next_page = callback['data'].split(':')[1]
    await list_files(callback, _previous=int(previous_page), _next=int(next_page))
    return


# ----------------------------------------------------------------------------------------------------------------------
#                                           Echo + Files handler
# ----------------------------------------------------------------------------------------------------------------------
@dp.message_handler()
@exception_handler()
async def echo_message(message: types.Message):
    async with AsyncContextManager() as session:
        files = await session.get_files()

    files_name = [file['name'] for file in files]
    if message.text not in files_name:
        return await bot.send_message(message.from_user.id, f'{message.text}')

    async with AsyncContextManager() as session:
        file = await session.get_file({'name': message.text})

    if not file:
        return

    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_DOCUMENT)
    await asyncio.sleep(1)
    await bot.send_document(message.from_user.id, file['file_id'], caption=ms.GET_FILE)
