from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# ===============================================================

get_code = InlineKeyboardButton(text="get_code", callback_data="In_First_button")
track = InlineKeyboardButton(text="track", callback_data="In_Second_button")
keyboard_inline = InlineKeyboardMarkup().add(get_code, track)


# ===============================================================

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)

start_buttons = KeyboardButton('/start')
get_code_buttons = KeyboardButton('/get_code')
track_buttons = KeyboardButton('/track')



start.add(start_buttons, get_code_buttons, track_buttons)


# ===============================================================

start_test = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
    ).add(
    KeyboardButton('/start'),
    KeyboardButton('/get_code'),
    KeyboardButton('/track'),
)

# ===============================================================

start_test_1 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
    )

start_test_1.add(
    KeyboardButton('/start'),
    KeyboardButton('/get_code'),
    KeyboardButton('/track'),
)

# ===============================================================

cancel_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton('Отмена')
)

submit_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton('Да'),
    KeyboardButton('Нет')
)

get_code_buttons = KeyboardButton('/get_code')
track_buttons = KeyboardButton('/track')