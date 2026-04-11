from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicons.lexicon_ru import START_BTN_TEXT

async def start_kb():
    list_btns = []
    for text in START_BTN_TEXT:
        button1 = KeyboardButton(text = text)
        list_btns.append([button1])
    keyboards = ReplyKeyboardMarkup(
        keyboard = list_btns
    )
    return keyboards