from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from asyncio import run
from config import BOT_TOKEN
import os
import asyncio


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    @dp.message(F.photo | F.video | F.voice)
    async def get_photo_video(message: Message, bot: Bot):
        print(f"[LOG] Пользователь {message.from_user.id} вызвал функцию get_photo_video")
        os.makedirs("downloads", exist_ok=True)
        if message.photo:
            file = await bot.get_file(message.photo[-1].file_id)
            print(f'[LOG] Файл {file.file_unique_id} получен')
            PATH = os.path.join("downloads", f"{file.file_unique_id}.jpg")
        elif message.voice:
            file = await bot.get_file(message.voice.file_id)
            PATH = os.path.join("downloads", f"{file.file_unique_id}.ogg")
        else:
            file = await bot.get_file(message.video.file_id)
            print(f'[LOG] Файл {file.file_unique_id} получен')
            PATH = os.path.join("downloads", f"{file.file_unique_id}.mp4")

        print(f'[LOG] Файл {file} сохраняется в {PATH}')
        await bot.download_file(file.file_path, destination=PATH)
        print(f'[LOG] Файл {file} сохранен в {PATH}')

        await message.answer("крутое фото или видео")

    @dp.message(F.sticker)
    async def sticker_handler(message: Message):
        print(f"[LOG] Пользователь {message.from_user.id} вызвал функцию sticker_handler")
        with open("stickers.txt", "a+") as f:
            f.write(message.sticker.file_id + '\n')
            print(f"[LOG] ID стикера {message.sticker.file_id} сохранен в stickers.txt")


    @dp.message(F.text == 'Отправь фото')
    async def send_video(message: Message):
        print(f'[LOG] Пользователь {message.from_user.id} вызвал функцию send_video')
        # await message.answer_photo(
        #     photo = "https://pin.it/IcbS7Pdyk",
        #     caption = "Это кот"
        # )
        PATH = os.path.join("files", "20260123_152149.mp4")
        print("[LOG] Начало бинаризации")
        video = FSInputFile(PATH)
        print("[LOG] Конец бинаризации")
        await message.answer_video(
            video = video,
            caption = 'не за что'
        )
        print(f"Видео {PATH} отправлено с локального сервера")
        
    @dp.message(Command(commands = ['show']))
    async def show(message: Message):
        if os.path.exists("show.txt"):
            pass
        else:
            os.makedirs("show.txt", exist_ok = True)
            with open("show.txt", "w") as f:
                f.write("curs, temperature\n 60:20\n 55:12\n 67:13")
        with open("show.txt", "r") as f:
            next(f)
            list_data = f.readlines()
            print(list_data)
            if list_data == []:
                await message.answer("Данных нет")
            else:
                for index, item in enumerate(list_data):
                    elements = item.split(":")
                    if index == 0:
                        await message.answer(f'Текущая температура на улице: {elements[1]}')
                        await asyncio.sleep(10)
                    else:
                        await message.edit_text(f'Текущая температура на улице: {elements[1]}')
                        await asyncio.sleep(10)

                await message.delete()


    await dp.start_polling(bot)
print(f'[LOG] Бот запущен.')
if __name__ == '__main__':
    run(main()) # запускает цикла событий(dispatcher)