import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.enums import ParseMode, ChatAction

from keyboards import choose_keyboard, action_keyboard
from utils.messages import get_message
from utils.generator import generate_password

router = Router()

password_configuration = {}


@router.callback_query(F.data.startswith("length_"))
async def choose_password_length(callback: CallbackQuery):
    length = callback.data.split("_")[1]
    password_configuration["length"] = length

    text = get_message("digits")

    await callback.answer(f"Password length is {length}.")
    await callback.message.edit_text(
        text=text,
        reply_markup=choose_keyboard.digits,
        parse_mode=ParseMode.HTML
    )


@router.callback_query(F.data.startswith("digits_"))
async def choose_digits_adding(callback: CallbackQuery):
    digits = callback.data.split("_")[1]
    password_configuration["digits"] = digits

    text = get_message("symbols")

    await callback.answer("Digits are added." if digits != "no" else "Digits are not added.")
    await callback.message.edit_text(
        text=text,
        reply_markup=choose_keyboard.symbols,
        parse_mode=ParseMode.HTML
    )


@router.callback_query(F.data.startswith("symbols_"))
async def choose_symbols_adding(callback: CallbackQuery):
    symbols = callback.data.split("_")[1]
    password_configuration["symbols"] = symbols

    text = get_message("generate")

    await callback.answer("Symbols are added." if symbols != "no" else "Symbols are not added.")
    await callback.message.edit_text(
        text=text,
        parse_mode=ParseMode.HTML,
        reply_markup=action_keyboard.generate
    )


@router.callback_query(F.data.startswith("generate_"))
async def manipulate_password_generation(callback: CallbackQuery):
    if (callback.data.split("_")[1] == "start"):
        password = generate_password(password_configuration)
        text = get_message("result", password=password)
        await callback.message.edit_text(
            text=text,
            parse_mode=ParseMode.HTML
        )
    else:
        text = get_message("/generate")
        await callback.message.edit_text(
            text=text,
            parse_mode=ParseMode.HTML,
            reply_markup=choose_keyboard.length
        )
