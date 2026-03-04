from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from requests import get
from asyncio import run
from config import BOT_TOKEN


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    @dp.message(Command(commands=['start']))
    async def start_handler(message: Message):
        print(f"[LOG] пользователь {message.from_user.id, message.from_user.first_name} нажал на кнопку старт")

        await message.answer(f'Привет {message.from_user.full_name}')

    # https://catfact.ninja/fact
    @dp.message(Command(commands=['catfact']))
    async def get_cat_fact(message: Message):
        print(f'[LOG] Пользователь {message.from_user.id} вывел факт о кошках')
        print('[LOG] Запрашиваю информацию с сервера')
        response = get('https://catfact.ninja/fact')
        print(f'[LOG] Получен результат со статусом {response.status_code}')
        print(response.json()["length"])
        await message.answer(response.json()["fact"])

    @dp.message(Command(commands=['breeds']))
    async def get_cat_breeds(message: Message):
        print(f'[LOG] Пользователь {message.from_user.id} запрашивает породу кошки')
        print('[LOG] Запрашиваю информацию с сервера')
        response = get('https://catfact.ninja/breeds')
        print(f'[LOG] Получен результат со статусом {response.status_code}')
        response_json = response.json()
        print(response_json['data'][0]['country'])
        await message.answer(response_json["data"][0]['breed'])
        print(f'[LOG] Пользователь {message.from_user.id} вывел породу кошки')

    @dp.message()
    async def text_handler(message: Message):
        print(f"[LOG] Пользователь {message.from_user.id} ввел сообщение")
        await message.answer('Не знаю такой команды')



    await dp.start_polling(bot)


print(f'[LOG] Бот запущен.')
if __name__ == '__main__':
    run(main()) # запускает цикла событий(dispatcher)