from aiogram import F, Router
from aiogram.types import Message
from lexicons.lexicon_ru import START_BTN_TEXT, COURSES_TEXT
from keyboards.menu_kb import menu_kb
router = Router()

@router.message(F.text == START_BTN_TEXT[0])
async def courses_handler(message: Message):
    await message.answer(
        COURSES_TEXT,
        reply_markup=await menu_kb()
    )