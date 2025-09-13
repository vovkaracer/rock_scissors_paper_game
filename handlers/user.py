from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import game_kb, yes_no_kb
from services.services import get_bot_choice, get_winner

user_router = Router()

@user_router.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=yes_no_kb
    )

@user_router.message(Command(commands='help'))
async def process_command_help(message: Message):
    await message.answer(
        text=LEXICON_RU['/help'],
        reply_markup=yes_no_kb
    )

@user_router.message(F.text == LEXICON_RU['yes_button'])
async def process_positive_answer(message: Message):
    await message.answer(
        text=LEXICON_RU['positive_answer'],
        reply_markup=game_kb
    )

@user_router.message(F.text == LEXICON_RU['no_button'])
async def process_negative_answer(message: Message):
    await message.answer(
        text=LEXICON_RU['negative_answer']
    )

@user_router.message(F.text.in_([LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']]))
async def process_game_answer(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(
        text=f'{LEXICON_RU["bot_choice"]}{LEXICON_RU[bot_choice]}'
    )
    winner = get_winner(bot_choice, message.text)

    if winner == 'user_won':
        message_effect_id = '5046509860389126442'
    else:
        message_effect_id = None

    await message.answer(
        text=LEXICON_RU[winner],
        message_effect_id=message_effect_id,
        reply_markup=yes_no_kb
    )