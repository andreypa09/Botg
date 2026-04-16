from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from lexicons.lexicon_ru import START_BTN_TEXT, COURSES_TEXT, COURSES_INFO
from keyboards.menu_kb import menu_kb, menu_join_kb
from aiogram.fsm.state import State, StatesGroup

class Registration(StatesGroup):
    waiting_class = State()
    waiting_name = State()
    waiting_contact = State()


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
    await data.message.answer("Введите ваш класс и школу:")
    await state.set_state(Registration.waiting_class)

@router.message(Registration.waiting_class)
async def process_class(message: Message, state: FSMContext):
    await message.answer("Введите ваше ФИО:")
    await state.update_data(klass = message.text)
    await state.set_state(Registration.waiting_name)



@router.message(Registration.waiting_name)
async def process_name(message: Message, state: FSMContext):
    await message.answer("Отправьте ваш контакт")
    await state.update_data(name = message.text)
    await state.set_state(Registration.waiting_contact)


@router.message(Registration.waiting_contact)
async def process_contact(message: Message, state: FSMContext):
    await state.update_data(contact = message.contact)
    state_data = await state.get_data()
    klass = state_data.get("klass", "undefined")
    name = state_data.get("name", "undefined")
    contact = state_data.get("contact", "undefined")
    await message.answer(
        f"Ваш класс и школа: {klass}\nВаше имя: {name}\nВаш контакт: {contact}"
    )
    await state.set_state(None) # Заканчивает состояние
    # await state.clear() # Отчищает все данные и состояния