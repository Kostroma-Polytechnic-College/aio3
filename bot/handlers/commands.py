from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.keyboards.commands import get_kb_by_start

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        text="Привет! ",
        reply_markup=get_kb_by_start()
    )


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")