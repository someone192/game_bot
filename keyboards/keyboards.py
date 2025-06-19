from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keyboards.buttons.buttons import scissors_btn, stone_btn, paper_btn, yes_btn, no_btn, help_btn

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
        [InlineKeyboardButton(text="Кнопка 1", callback_data="button1")],
        [InlineKeyboardButton(text="Кнопка 2", callback_data="button2")]
    ]
) 

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