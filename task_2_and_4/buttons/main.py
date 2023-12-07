from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_buutons():
    btn1 = KeyboardButton(text="Filial 📍")
    btn2 = KeyboardButton(text="Start ✅")
    btn3 = KeyboardButton(text="Admin 👨🏻‍💻")
    btn4 = KeyboardButton(text='news 📂')
    design = [
        [btn1, btn2],
        [btn3, btn4]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
