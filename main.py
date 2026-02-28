import requests
import asyncio

from aiogram.filters import CommandStart
from aiohttp.hdrs import CONTENT_TYPE

from config import Config, load_config
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from pathlib import Path

config: Config = load_config()
bot_token = config.bot.token

bot = Bot(token=bot_token)

dp = Dispatcher()
# домашняя папка пользователя
HOME_DIR = Path.home()
# рабочий стол
DESKTOP_DIR = HOME_DIR / "Desktop"
# папка downloads
DOWNLOAD_DIR = DESKTOP_DIR / "Downloads"

# @dp.message(F.photo)
# async def download_photo(message: Message, bot: Bot):
#     photo = message.photo[-1]
#     file = await bot.get_file(photo.file_id)
#     await bot.download_file(file.file_path, DOWNLOAD_DIR)
#     print(file)
#
@dp.message(F.text.lower() == 'дай фото')
async def send_photo_url(message: Message):
    #  нельзя отправить текст > 4096
    #  нельзя отправить caption > 1024
    #  photo = 'https://ru.freepik.com/free-photo/british-shorthair-cat-look-camera_17420038.htm#fromView=keyword&page=1&position=0&uuid=89393b9f-4c4c-4dbe-9ba9-5a512e6ef43f&query=%D0%9A%D0%BE%D1%82%D1%8B'
    # await message.answer_photo(
    #     photo,
    #     caption = 'Фото кота'
    # )
    photo = FSInputFile("files/test1.jpg")
    await message.answer_photo(
        photo = photo,
        caption = "Вот сохраненное фото"
    )
@dp.message(F.photo)
async def reply_photo(message: Message):
    photo = message.photo[-1]
    await message.answer_photo(
        photo = photo.file_id,
        caption = 'не присылай больше'
    )
@dp.message(CommandStart)
async def start(message: Message):
    await message.answer('Привет, отправь свой любимый стикер!')
@dp.message(F.sticker)
async def is_sticker(message: Message):
    sticker = message.sticker.file_id[-1]
    await message.answer_sticker(
        sticker,
        caption = 'А вот мой'
    )
@dp.message(~F.sticker)
async def is_not_sticker(message: Message):
    await message.answer('Это не похоже на стикер. Отправь стикер!')
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())