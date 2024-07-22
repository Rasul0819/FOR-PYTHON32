from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton



car_menu = InlineKeyboardMarkup()
car_menu.add(InlineKeyboardButton(text='Sell Car',callback_data='sellcar'),
             InlineKeyboardButton(text='Buy Car',callback_data='buycar'))