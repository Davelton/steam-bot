from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn = [
    [KeyboardButton(text="Категория⌨️"), KeyboardButton(text="Профиль💼")],
    [KeyboardButton(text="Поддержка📞"), KeyboardButton(text="Информацияℹ️")]
]
menu = ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)

btnCat = [
    [KeyboardButton(text="Игры🎮")],
    [KeyboardButton(text="Список игр📋"), KeyboardButton(text="Бесплатные игры🆓")],
    [KeyboardButton(text="🔙Назад")]
]

btn_Cat = ReplyKeyboardMarkup(keyboard=btnCat, resize_keyboard=True)


steam_btn = [
    [KeyboardButton(text="Приключение🏖"), KeyboardButton(text="Хоррор🪓")],
    [KeyboardButton(text="Сюжет⏳"), KeyboardButton(text="Гонки🚘")],
    [KeyboardButton(text="Головоломка🧩"), KeyboardButton(text="Экшен🔫")],
    [KeyboardButton(text="🔙Back")]
]

menu_steam = ReplyKeyboardMarkup(keyboard=steam_btn, resize_keyboard=True)

#Приключение
steam_btn1 = [
    [KeyboardButton(text="It Takes Two"), KeyboardButton(text="Terraria")],
    [KeyboardButton(text="Baldur's Gate 3"), KeyboardButton(text="Rust")],
    [KeyboardButton(text="Stray"), KeyboardButton(text="Starfield")],
    [KeyboardButton(text="🔙BACK")]
]

menu_steam1 = ReplyKeyboardMarkup(keyboard=steam_btn1, resize_keyboard=True)

#Хоррор
steam_btn2 = [
    [KeyboardButton(text="Alone in the Dark"), KeyboardButton(text="Resident Evil 7 Biohazard")],
    [KeyboardButton(text="Dead by Daylight"), KeyboardButton(text="Sons Of The Forest")],
    [KeyboardButton(text="Buckshot Roulette"), KeyboardButton(text="Little Nightmares II")],
    [KeyboardButton(text="🔙BACK")]
]

menu_steam2 = ReplyKeyboardMarkup(keyboard=steam_btn2, resize_keyboard=True)

#Сюжет
steam_btn3 = [
    [KeyboardButton(text="The Last of Us™: Part I"), KeyboardButton(text="Red Dead Redemption 2")],
    [KeyboardButton(text="Ведьмак 3:Дикая Охота"), KeyboardButton(text="Mafia:Definitive Edition")],
    [KeyboardButton(text="Cyberpunk 2077"), KeyboardButton(text="God of War")],
    [KeyboardButton(text="🔙BACK")]
]

menu_steam3 = ReplyKeyboardMarkup(keyboard=steam_btn3, resize_keyboard=True)

#Гонки
steam_btn4 = [
    [KeyboardButton(text="BeamNG.drive"), KeyboardButton(text="Wreckfest")],
    [KeyboardButton(text="Forza Horizon 4"), KeyboardButton(text="Need for Speed™ Heat")],
    [KeyboardButton(text="Forza Horizon 5"), KeyboardButton(text="Need for Speed™ Hot Pursuit Remastered")],
    [KeyboardButton(text="🔙BACK")]
]

menu_steam4 = ReplyKeyboardMarkup(keyboard=steam_btn4, resize_keyboard=True)

#Головоломка
steam_btn5 = [
    [KeyboardButton(text="Machinarium"), KeyboardButton(text="Creaks")],
    [KeyboardButton(text="LIMBO"), KeyboardButton(text="Portal 2")],
    [KeyboardButton(text="Teardown"), KeyboardButton(text="The Talos Principle 2")],
    [KeyboardButton(text="🔙BACK")]
]

menu_steam5 = ReplyKeyboardMarkup(keyboard=steam_btn5, resize_keyboard=True)

#Экшен
steam_btn6 = [
    [KeyboardButton(text="Call of Duty:MW III"), KeyboardButton(text="Far Cry 6")],
    [KeyboardButton(text="Assassin's Creed Origins"), KeyboardButton(text="HELLDIVERS™ 2")],
    [KeyboardButton(text="Grand Theft Auto V"), KeyboardButton(text="Warface")],
    [KeyboardButton(text="🔙BACK")]
]

menu_steam6 = ReplyKeyboardMarkup(keyboard=steam_btn6, resize_keyboard=True)


catMenu1 = ReplyKeyboardMarkup(keyboard=btnCat, resize_keyboard=True)

inlineBtn1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить",callback_data="pay_1")]
])


catMenu2 = ReplyKeyboardMarkup(keyboard=btnCat, resize_keyboard=True)

inlineBtn2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить",callback_data="pay_2")]
])


catMenu3 = ReplyKeyboardMarkup(keyboard=btnCat, resize_keyboard=True)

inlineBtn3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить",callback_data="pay_3")]
])

catMenu4 = ReplyKeyboardMarkup(keyboard=btnCat, resize_keyboard=True)

inlineBtn4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить",callback_data="pay_4")]
])

catMenu5 = ReplyKeyboardMarkup(keyboard=btnCat, resize_keyboard=True)

inlineBtn5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить",callback_data="pay_5")]
])

catMenu6 = ReplyKeyboardMarkup(keyboard=btnCat, resize_keyboard=True)

inlineBtn6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить",callback_data="pay_6")]
])




