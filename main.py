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

    # 27.
    # button_1 = KeyboardButton(text = 'Команда 1')
    # keyboard = ReplyKeyboardMarkup(keyboard=[[button_1]])
    #
    # @dp.message(Command(commands=['start']))
    # async def start_handler(message: Message):
    #     await message.answer(
    #         text = 'Вот тебе клава',
    #         reply_markup = keyboard
    #     )
    #
    # @dp.message(F.text == 'Команда 1')
    # async def command_handler1(message: Message):
    #     await message.answer(
    #         text = 'Ты выбрал первую команду'
    #     )
    #
    # knopka_1 = KeyboardButton(text='Отправить номер телефона', request_contact=True)
    # knopka_2 = KeyboardButton(text='Отправить геолокацию', request_location=True)
    # keyboard = ReplyKeyboardMarkup(
    #     keyboard=[[knopka_1, knopka_2]],  # Передаем туда кнопки, формируем клавиатуру
    #     resize_keyboard=True,  # сжалась кнопка до высоты текста и ширины экрана телефона
    #     input_field_placeholder="Клавиатура ...",
    #     one_time_keyboard=True
    # )
    #
    # @dp.message(Command(commands=['reg']))
    # async def start(message: Message):
    #     await message.answer(
    #         text="Выбери кнопку",
    #         reply_markup=keyboard
    #     )
    #
    # @dp.message(F.text == 'Отправить номер телефона')
    # async def com1_handler(message: Message):
    #     await message.answer(
    #         text="Вот команда 1",
    #         reply_markup=ReplyKeyboardRemove()
    #     )
    #
    # @dp.message(F.contact)
    # async def get_contact(message: Message):
    #     data = message.contact.phone_number
    #     with open("data.txt", "a") as f:
    #         f.write(f'{message.from_user.username}-{data}\n')
    #
    # @dp.message(F.location)
    # async def get_location(message: Message):
    #     loc1 = message.location.latitude
    #     loc2 = message.location.longitude
    #     with open("data.txt", "a") as f:
    #         f.write(f'{message.from_user.username}-{loc1};{loc2}\n')


    # 28.
    # InlineKeyboardMarkup клавиатура
    # InlineKeyboardButton кнопки

    # btn_1 = InlineKeyboardButton(text="Пицца", callback_data="пицца")
    # btn_2 = InlineKeyboardButton(text="Американские бургеры", callback_data="бургеры")
    # keyboard = InlineKeyboardMarkup(inline_keyboard=[[btn_1], [btn_2]])
    #
    # @dp.message(F.text == "заказ")
    # async def start(message: Message):
    #     await message.answer(text="Выберите блюдо", reply_markup=keyboard)
    #
    # @dp.callback_query(F.data)
    # async def callback_handler(callback: CallbackQuery):
    #     data = callback.data
    #     await callback.message.edit_text(f"Вы выбрали: {data}")
    #     await asyncio.sleep(1)
    #     await callback.answer("Оформляем заказ...")
    #     await asyncio.sleep(1)
    #     await callback.message.edit_text("Ожидание курьера...")
    #     await asyncio.sleep(1)
    #     await callback.message.edit_text(f"{data} - заказ готов")

    # Проект «Опросник»
    # Сценарий: Сбор данных о пользователе (анкета из 3-х вопросов).
    # Твоя задача:
    # Пользователь жмет «Начать тест». Бот присылает первый вопрос.
    # Под вопросом кнопки с вариантами ответа
    # После нажатия на кнопку идет переход на следующий вопрос
    # После третьего вопроса отправляется весь тест с ответами в формате:
    # 1 вопрос:
    # Какой результат деления на 10
    # ответ: {ответ человека}
    # 2 вопрос:
    # Какой результат деления на 10
    # ответ: {ответ человека}
    # 3 вопрос:
    # Какой результат деления на 10
    # ответ: {ответ человека}


    questions = [
        {"В каком году родился Алексей II?":
             {"1892",
              }
         },
        {"Сколько лет было мне когда я пошел в садик?": "4"},
        {"Кто проживает на дне океана?": "Патрик"}

    ]
    start_test_button = KeyboardButton(
        text = "Начать тест"
    )

    menu_buttons = ReplyKeyboardMarkup(
        keyboard=[[start_test_button]]
    )
    @dp.message(Command(commands = ["start"]))
    async def start_handler(message: Message):
        await message.answer(
            "Начинаем тест, нажмите начать тест",
            reply_markup=menu_buttons
        )

    counter = 0
    @dp.message(F.text == "Начать тест")
    async def start_test_handler(message: Message):

        quest = list(questions[counter].keys())
        answ = list(questions[counter].values())
        answ_1_btn = InlineKeyboardButton(
            text = answ[0],
            callback_data = "questions_1"
        )
        answ_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[answ_1_btn]]
        )

        await message.answer(
            text = quest[0],
            reply_markup=answ_keyboard
        )
    @dp.callback_query(F.data.startswith('question'))
    async def answ_handler(callback: CallbackQuery):
        nonlocal counter
        counter += 1

        quest = list(questions[counter].keys())
        answ = list(questions[counter].values())

        answ_1_btn = InlineKeyboardButton(
            text=answ[0],
            callback_data="questions_2"
        )
        answ_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[answ_1_btn]]
        )

        await callback.message.answer(
            text = quest[0],
            reply_markup=answ_keyboard
        )
    await dp.start_polling(bot)
print(f'[LOG] Бот запущен.')
if __name__ == '__main__':
    run(main()) # запускает цикла событий(dispatcher)