from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.states.user.registration import RegistrationState

from main import bot

router = Router()


@router.callback_query(F.data == 'user_registration')
async def click_register(callback_query: CallbackQuery, state: FSMContext) -> None:
    await bot.send_message(chat_id=callback_query.message.chat.id, text='Введите имя')
    await callback_query.answer(text='Введите имя')
    await state.set_state(RegistrationState.name) 
    
@router.callback_query()
async def all(callback_query: CallbackQuery, state: FSMContext) -> None:
    print('all', callback_query.data)


async def set_name(msg: Message, state: FSMContext) -> None:
    await msg.reply(text='Введите возраст')
    await state.update_data({'name': msg.text})
    await state.set_state(await RegistrationState.next())
    
async def set_age(msg: Message, state: FSMContext) -> None:
    try:
        age = int(msg.text)
        if age < 0:
            await msg.reply(text='Нужно ввести положительное число')
            return
        await state.update_data({'age': age})
        await state.set_state(await RegistrationState.next())
    except ValueError:
        await msg.reply(text='Нужно ввести целое число')