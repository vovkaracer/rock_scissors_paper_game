from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import yes_no_kb

other_router = Router()

@other_router.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=yes_no_kb
    )

@other_router.message(Command(commands='/help'))
async def process_command_help(message: Message):
    await message.answer(
        text=LEXICON_RU['/help'],
        reply_markup=yes_no_kb
    )