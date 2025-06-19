import random

from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon import LEXICON
from services.services import who_wins

router = Router()

list_1 = ['ножницы', 'бумага', 'камень']

bot_win = ['Каменьбумага','Ножницыкамень', 'Бумаганожницы']

positions = {
    1: 'ножницы',
    2: 'бумага', 
    3: 'камень'
}

# Хендлер на команду /start
@router.message(Command("start"))
async def process_start_command(message: Message):
    await message.answer(
        LEXICON['start'],
        reply_markup=yes_no_kb
        )

# Хендлер на команду /help
@router.message(Command("help"))
async def process_help_command(message: Message):
    await message.answer(
        LEXICON['help'],
        reply_markup=yes_no_kb
    )

# Хендлер на текстовые сообщения
#@router.message(F.text == "Меню 1")
#async def process_menu1(message: Message):
#    await message.answer(LEXICON['menu1'], reply_markup=inline_kb)

#@router.message(F.text == "Меню 2")
#async def process_menu2(message: Message):
#    await message.answer(LEXICON['menu2'])

## Хендлер на callback_query
#@router.callback_query(F.data == "button1")
#async def process_button1(callback: CallbackQuery):
#    await callback.answer("Вы нажали кнопку 1!")

#@router.callback_query(F.data == "button2")
#async def process_button2(callback: CallbackQuery):
#    await callback.answer("Вы нажали кнопку 2!") 

@router.message(F.text.lower() == 'да')
async def process_positive_answer(message: Message):
    await message.answer(
        text='Хорошо, выберите камень, ножницы или бумагу',
        reply_markup=game_kb
    )

@router.message(F.text.lower() == 'нет')
async def process_negative_answer(message: Message):
    await message.answer(
        text='Жаль, если захотите поиграть - пишите',
        reply_markup=yes_no_kb
    )

#@router.message(F.text.lower() == 'камень')
#async def process_stone_answer(message: Message):
#    answ = random.randint(1, 3)
#    if answ == 2:
#        await message.answer(
#        text='Я выиграл, сыграем ещё?',
#        reply_markup=yes_no_kb
#    )  
#    elif message.text == positions[answ]:
#        await message.answer(
#        text='Ничья, сыграем ещё?',
#        reply_markup=yes_no_kb
#    )  
#    else:
#        await message.answer(
#        text='Вы выиграли, сыграем ещё?',
#        reply_markup=yes_no_kb
#    ) 

@router.message(F.text.lower().in_(list_1))
async def process_answer(message: Message):
    await message.answer(
        text=who_wins(message.text),
        reply_markup=yes_no_kb
    ) 

@router.message(Command('delmenu'))
async def delete_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "Menu" удалена')

@router.message()
async def process_other_answer(message: Message):
    await message.answer(
        text='Я простой бот, давайте просто сыграем?',
        reply_markup=yes_no_kb
    )