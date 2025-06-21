from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keyboards.buttons import (scissors_btn, stone_btn, paper_btn, yes_btn, no_btn, help_btn,
                                url_button_1, url_button_2, big_button_1, big_button_2)
from keyboards.inline_kb_creator import create_inline_kb
from lexicon.lexicon import BUTTONS

kb_builder = ReplyKeyboardBuilder()
yes_no_kb_builder = ReplyKeyboardBuilder()

# Основная клавиатура
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меню 1"), KeyboardButton(text="Меню 2")],
        [KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True
)

# Инлайн клавиатура (пример)
inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [big_button_1],
        [big_button_2]
    ]
)

inline_kb_2 = create_inline_kb(4, 'but_1', 'but_3', 'but_7')

kb_builder.row(scissors_btn, stone_btn, paper_btn, width=3)

game_kb: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

yes_no_kb_builder.row(yes_btn, no_btn, help_btn, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)