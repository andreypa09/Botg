from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from lexicons.lexicon_ru import START_BTN_TEXT, COURSES_TEXT, COURSES_INFO
from keyboards.menu_kb import menu_kb, menu_join_kb
router = Router()

@router.message(F.text == START_BTN_TEXT[0])
async def courses_handler(message: Message):
    await message.answer(
        COURSES_TEXT,
        reply_markup=await menu_kb()
    )


@router.callback_query(F.data.startswith('course_'))
async def menu_handler(data: CallbackQuery):
    key = data.data
    info_text = COURSES_INFO[key]
    keyboard = await menu_join_kb()
    await data.message.edit_text(
        info_text,
        reply_markup=keyboard
    )
