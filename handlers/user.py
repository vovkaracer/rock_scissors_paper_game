from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import game_kb, yes_no_kb

user_router = Router()

@user_router.message(Command(commands=LEXICON_RU['yes_button']))
async def process_positive_answer(message: Message):
    await message.answer(
        text=LEXICON_RU['positive_answer'],
        reply_markup=game_kb
    )

@user_router.message(Command(commands=LEXICON_RU['no_button']))
async def process_negative_answer(message: Message):
    await message.answer(
        text=LEXICON_RU['negative_answer'],
        reply_markup=yes_no_kb
    )

@user_router.message(Command(commands=[LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']]))
async def process_game_answer(message: Message):
    await message.answer(

    )

@user_router.message(Command(commands=LEXICON_RU['other_answer']))
async def process_other_answer(message: Message):
    await message.answer(
        text=LEXICON_RU['other_answer']
    )