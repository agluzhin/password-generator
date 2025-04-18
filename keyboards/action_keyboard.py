from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

generate = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Start", callback_data="generate_start")],
    [InlineKeyboardButton(text="Cancel", callback_data="generate_cancel")]
])
