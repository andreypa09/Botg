from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicons.lexicon_ru import LIST_COURSES


async def menu_kb():
    list_btns = []
    for keys, values in LIST_COURSES.items():
        btn = InlineKeyboardButton(
            text = keys,
            callback_data = values
        )
        list_btns.append([btn])
    keyboards = InlineKeyboardMarkup(
        inline_keyboard=list_btns
    )
    return keyboards