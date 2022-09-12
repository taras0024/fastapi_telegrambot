from typing import Union

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from . import messages as ms
from .managers import AsyncContextManager
from ..utils import paginate

pagination_cd = CallbackData('pagination', 'previous_page', 'next_page')
file_cd = CallbackData('file', 'name')


async def files_keyboard(_previous=0, _next=0):
    async with AsyncContextManager() as session:
        files, _page = paginate(await session.get_files(), _previous, _next)

    if not files:
        return

    markup = InlineKeyboardMarkup(row_width=2)
    for file in files:
        markup.insert(
            InlineKeyboardButton(text=file['name'], callback_data=file_cd.new(name=file['name']))
        )

    markup.row(
        InlineKeyboardButton(text='<<<', callback_data=pagination_cd.new(previous_page=_page - 1, next_page='0')),
        InlineKeyboardButton(text='>>>', callback_data=pagination_cd.new(previous_page='0', next_page=_page + 1))
    )
    return markup


async def list_files(message: Union[types.Message | types.CallbackQuery], _previous=0, _next=0):
    markup = await files_keyboard(_previous, _next)
    if markup is None:
        await message.answer(ms.NO_FILES)
        return

    if isinstance(message, types.Message):
        await message.answer(ms.GET_FILES, reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)
