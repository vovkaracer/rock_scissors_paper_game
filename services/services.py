from random import choice
from lexicon.lexicon import LEXICON_RU

def get_bot_choice() -> str:
    answers = [LEXICON_RU['paper'], LEXICON_RU['scissors'], LEXICON_RU['rock']]
    return choice(answers)

def get_winner(bot_game_answer: str, user_game_answer: str) -> bool:
