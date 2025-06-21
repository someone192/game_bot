from aiogram.types import KeyboardButton, InlineKeyboardButton

big_button_1 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='big_button_1_pressed'
)

big_button_2 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data='big_button_2_pressed'
)

url_button_1 = InlineKeyboardButton(
    text='Курс "Телеграм-боты на Python и AIOgram"',
    url='https://stepik.org/120924'
)

url_button_2 = InlineKeyboardButton(
    text='Документация Telegram Bot API',
    url='https://core.telegram.org/bots/api'
)

stone_btn = KeyboardButton(
    text='Камень'
)

scissors_btn = KeyboardButton(
    text='Ножницы'
)

paper_btn = KeyboardButton(
    text='Бумага'
)

yes_btn = KeyboardButton(
    text='Да'
)

no_btn = KeyboardButton(
    text='Нет'
)

help_btn = KeyboardButton(
    text='/help'
)