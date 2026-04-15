from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from lexicons.lexicon_ru import START_BTN_TEXT, COURSES_TEXT, COURSES_INFO
from keyboards.menu_kb import menu_kb, menu_join_kb
from aiogram.fsm.state import State, StatesGroup

class Registration(StatesGroup):
    waiting_name = State()
    waiting_username = State()


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


@router.callback_query(F.data == "join_sign_up")
async def sign_up_handler(data: CallbackQuery, state: FSMContext):
    await data.message.answer("Введите ваше имя:")
    await state.set_state(Registration.waiting_name)

@router.message(Registration.waiting_name)
async def process_handler(message: Message, state: FSMContext):
    await message.answer("Введите юзернейм")
    await state.update_data(name = message.text)
    await state.set_state(Registration.waiting_username)


@router.message(Registration.waiting_username)
async def process_username(message: Message, state: FSMContext):
    state_data = await state.get_data()
    name = state_data.get("name", "undefined")
    await message.answer(
        f"Ваше имя: {name}\nВаш юзернейм: {message.text}"
    )
    await state.set_state(None) # Заканчивает состояние
    await state.clear() # Отчищает все данные и состояния