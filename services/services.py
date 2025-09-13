from random import choice
from lexicon.lexicon import LEXICON_RU

def get_bot_choice() -> str:
    return choice(['paper', 'scissors', 'rock'])

def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key

def get_winner(bot_game_answer: str, user_game_answer: str) -> str:
    rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    user_choice = _normalize_user_answer(user_game_answer)
    if rules[user_choice] == bot_game_answer:
        return 'user_won'
    elif user_choice == bot_game_answer:
        return 'nobody_won'
    else:
        return 'bot_won'