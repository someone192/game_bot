from random import choice

list_1 = ['ножницы', 'бумага', 'камень']

bot_win = ['Каменьбумага','Ножницыкамень', 'Бумаганожницы']

def who_wins(user_answer: str | None = None) -> str:
    bot_answ = choice(list_1)
    try:
        if user_answer + bot_answ in bot_win:
            return f'Мой выбор - {bot_answ}, Я выиграл, сыграем ещё?'
        elif user_answer.lower() == bot_answ :
            return f'Мой выбор - {bot_answ}, Ничья, сыграем ещё?'
        return f'Мой выбор - {bot_answ}, Вы выиграли, сыграем ещё?'
    except Exception:
        return 'что то странное'