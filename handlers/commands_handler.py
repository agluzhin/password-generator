import asyncio
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode, ChatAction

from utils.messages import get_message
from keyboards import choose_keyboard

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    user_name = message.from_user.full_name
    chat_id = message.from_user.id

    text = get_message("/start", user_name=user_name)

    await message.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    await asyncio.sleep(2)

    await message.answer(
        text=text,
        parse_mode=ParseMode.HTML
    )


@router.message(Command("generate"))
async def cmd_generate(message: Message):
    chat_id = message.from_user.id

    text = get_message("/generate")

    await message.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    await asyncio.sleep(2)

    await message.answer(
        text=text,
        parse_mode=ParseMode.HTML,
        reply_markup=choose_keyboard.length
    )
