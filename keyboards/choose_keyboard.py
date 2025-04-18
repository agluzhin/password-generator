from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

length = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="10", callback_data="length_10")],
    [InlineKeyboardButton(text="15", callback_data="length_15")],
    [InlineKeyboardButton(text="20", callback_data="length_20")],
    [InlineKeyboardButton(text="25", callback_data="length_25")],
    [InlineKeyboardButton(text="30", callback_data="length_30")]
])

digits = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Yes", callback_data="digits_yes")],
    [InlineKeyboardButton(text="No", callback_data="digits_no")]
])

symbols = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Yes", callback_data="symbols_yes")],
    [InlineKeyboardButton(text="No", callback_data="symbols_no")]
])
