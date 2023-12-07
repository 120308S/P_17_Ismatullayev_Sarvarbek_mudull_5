from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def start_butons():
    btn1 = KeyboardButton(text="Men")
    btn2 = KeyboardButton(text="Woman")
    btn3 = KeyboardButton(text="🔙 back")
    design = [
        [btn1, btn2],
           [btn3]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)

def month_buttons():
    btn1 = KeyboardButton(text="1-oy")
    btn2 = KeyboardButton(text="2-oy")
    btn3 = KeyboardButton(text="3-oy")
    btn4 = KeyboardButton(text="4-oy")
    btn5 = KeyboardButton(text="🔙 back")
    design = [
        [btn1, btn2],
        [btn3, btn4],
           [btn5]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
def days_buttons():
    btn1 = KeyboardButton(text="Dushanba")
    btn2 = KeyboardButton(text="Seshanba")
    btn3 = KeyboardButton(text="Chorshanba")
    btn4 = KeyboardButton(text="Payshanba")
    btn5 = KeyboardButton(text="Juma")
    btn6 = KeyboardButton(text="Shanba")
    btn7 = KeyboardButton(text="🔙 back")
    design = [
        [btn1, btn2],
        [btn3, btn4],
        [btn5, btn6],
        [btn7]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)