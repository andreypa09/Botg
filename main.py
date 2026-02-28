from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from asyncio import run
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def start_handler(message: Message):

    print(f"[LOG] пользователь {message.from_user.id, message.from_user.first_name} нажал на кнопку старт")

    await message.answer(f'Привет {message.from_user.full_name}')
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    run(main()) # запускает цикла событий(dispatcher)
