from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon import LEXICON_RU

#клавиатура с билдером
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(*[button_yes, button_no], width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(resize_keyboard=True)

#клавиатура без билдера
rock_button = KeyboardButton(text=LEXICON_RU['rock'])
scissors_button = KeyboardButton(text=LEXICON_RU['scissors'])
paper_button = KeyboardButton(text=LEXICON_RU['paper'])

game_kb = ReplyKeyboardMarkup(
    keyboard=[[rock_button], [scissors_button], [paper_button]],
    resize_keyboard=True
)