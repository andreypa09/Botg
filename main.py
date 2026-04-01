from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from asyncio import run
from config import BOT_TOKEN
import os
import asyncio


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    button_1 = KeyboardButton(text = 'Команда 1')
    keyboard = ReplyKeyboardMarkup(keyboard=[[button_1]])

    @dp.message(Command(commands=['start']))
    async def start_handler(message: Message):
        await message.answer(
            text = 'Вот тебе клава',
            reply_markup = keyboard
        )

    @dp.message(F.text == 'Команда 1')
    async def command_handler1(message: Message):
        await message.answer(
            text = 'Ты выбрал первую команду'
        )

    knopka_1 = KeyboardButton(text='Отправить номер телефона', request_contact=True)
    knopka_2 = KeyboardButton(text='Отправить геолокацию', request_location=True)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[knopka_1, knopka_2]],  # Передаем туда кнопки, формируем клавиатуру
        resize_keyboard=True,  # сжалась кнопка до высоты текста и ширины экрана телефона
        input_field_placeholder="Клавиатура ...",
        one_time_keyboard=True
    )

    @dp.message(Command(commands=['reg']))
    async def start(message: Message):
        await message.answer(
            text="Выбери кнопку",
            reply_markup=keyboard
        )

    @dp.message(F.text == 'Отправить номер телефона')
    async def com1_handler(message: Message):
        await message.answer(
            text="Вот команда 1",
            reply_markup=ReplyKeyboardRemove()
        )

    @dp.message(F.contact)
    async def get_contact(message: Message):
        data = message.contact.phone_number
        with open("data.txt", "a") as f:
            f.write(f'{message.from_user.username}-{data}\n')

    @dp.message(F.location)
    async def get_location(message: Message):
        loc1 = message.location.latitude
        loc2 = message.location.longitude
        with open("data.txt", "a") as f:
            f.write(f'{message.from_user.username}-{loc1};{loc2}\n')


    await dp.start_polling(bot)
print(f'[LOG] Бот запущен.')
if __name__ == '__main__':
    run(main()) # запускает цикла событий(dispatcher)