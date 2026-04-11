from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from lexicons.lexicon_ru import START_TEXT
from keyboards.start_kb import start_kb

router = Router()

@router.message(Command(commands = ["start"]))
async def cmd_start(message: Message):
    await message.answer(
        START_TEXT,
        reply_markup = await start_kb()
    )
