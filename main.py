
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from config import TOKEN
from buttons import *
from payment import pre_checkout_query, successful_payment, order_1, order_2, order_3, order_4, order_5, order_6, \
        order_7, order_8, order_9, order_10, order_11, order_12, order_13, order_14, order_15, order_16, order_17, \
        order_18, order_19, order_20, order_21, order_22, order_23, order_24, order_25, order_26, order_27, order_28, \
        order_29, order_30, order_31, order_32, order_33, order_34, order_35, order_36, order_37


dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Добро Пожаловать, {message.from_user.first_name}!", reply_markup=menu)


@dp.message(F.text == "Категория⌨️")
async def category(message: Message):
    await message.answer("Выберите кнопку", reply_markup=catMenu1)


@dp.message(F.text == "Профиль💼")
async def profile(message: Message):
    await message.answer("💼На вашем счету:$100 mlrd\n"
                         "💸Все Эти деньги Виртуальные\n", reply_markup=menu)


@dp.message(F.text == "Поддержка📞")
async def support(message: Message):
    await message.answer("По всем вопросам обращаться к @buzstard\n", reply_markup=menu)


@dp.message(F.text == "Информацияℹ️")
async def support(message: Message):
    await message.answer("Бот создан для того чтобы пользователь\n"
                              "мог приобретать разные игры с помощью нашего бота\n", reply_markup=menu)


@dp.message(F.text == "Игры🎮")
async def support(message: Message):
    await message.answer("Выберите кнопку\n", reply_markup=menu_steam)


@dp.message(F.text == "Приключение🏖")
async def support(message: Message):
    await message.answer("Выберите кнопку\n", reply_markup=menu_steam1)


@dp.message(F.text == "Хоррор🪓")
async def support(message: Message):
    await message.answer("Выберите кнопку\n", reply_markup=menu_steam2)


@dp.message(F.text == "Сюжет⏳")
async def support(message: Message):
    await message.answer("Выберите кнопку\n", reply_markup=menu_steam3)


@dp.message(F.text == "Гонки🚘")
async def support(message: Message):
    await message.answer("Выберите кнопку\n", reply_markup=menu_steam4)


@dp.message(F.text == "Головоломка🧩")
async def support(message: Message):
    await message.answer("Выберите кнопку\n", reply_markup=menu_steam5)


@dp.message(F.text == "Экшен🔫")
async def support(message: Message):
    await message.answer("Выберите кнопку\n", reply_markup=menu_steam6)


@dp.message(F.text == "🔙Назад")
async def support(message: Message):
    await message.answer("Выберите кнопку",reply_markup=menu)


@dp.message(F.text == "🔙Back")
async def support(message: Message):
    await message.answer("Выберите кнопку",reply_markup=catMenu1)


@dp.message(F.text == "🔙BACK")
async def support(message: Message):
    await message.answer("Выберите кнопку",reply_markup=menu_steam)


@dp.message(F.text == "Бесплатные игры🆓")
async def free_games(message: Message):
    await message.answer_photo(
            photo="https://i.redd.it/qkrjp3c9a2a81.jpg",
            caption="Dota 2🧙\n"
                    "CS:GO 2🔫\n"
                    "Destiny 2🎮\n"
                    "The Finals🔨\n"
                    "War Thunder🛩\n"
                    "Apex Legens⚔️\n"
                    "Valorant👾\n"
                    "Warframe🔱\n"
                    "Fallout Shelter⚠️\n", reply_markup=btn_Cat)


@dp.message(F.text == "Список игр📋")
async def games_list(message: Message):
    await message.answer_photo(
            photo="https://www.nyfa.edu/wp-content/uploads/2022/11/Steam-Library.png",
            caption="[Приключение🏖⬇️]\n"
                    "It Takes Two\n"
                    "Terraria\n"
                    "Baldur's Gate 3\n"
                    "Rust\n"
                    "Stray\n"
                    "Starfield\n"
                    "[Хоррор🪓⬇️]\n"
                    "Alone in the Dark\n"
                    "Resident Evil 7 Biohazard\n"
                    "Dead by Daylight\n"
                    "Sons Of The Forest\n"
                    "Buckshot Roulette\n"
                    "Little Nightmares II\n"
                    "[Сюжет⏳ ⬇️]\n"
                    "The Last of Us™: Part I\n"
                    "Red Dead Redemption 2\n"
                    "Ведьмак 3:Дикая Охота\n"
                    "Mafia:Definitive Edition\n"
                    "Cyberpunk 2077\n"
                    "God of War\n"
                    "[Гонки🚘⬇️]\n"
                    "BeamNG.drive\n"
                    "Wreckfest\n"
                    "Forza Horizon 4\n"
                    "Need for Speed™ Heat\n"
                    "Forza Horizon 5\n"
                    "Need for Speed™ Hot Pursuit Remastered\n"
                    "[Головоломка🧩⬇️]\n"
                    "Machinarium\n"
                    "Creaks\n"
                    "LIMBO\n"
                    "Portal 2\n"
                    "Teardown\n"
                    "The Talos Principle 2\n"
                    "[Экшен🔫⬇️]\n"
                    "Call of Duty:MW III\n"
                    "Far Cry 6\n"
                    "Assassin's Creed Origins\n"
                    "HELLDIVERS™ 2\n"
                    "Grand Theft Auto V\n"
                    "Warface\n", reply_markup=btn_Cat)


@dp.message(F.text == "It Takes Two")
async def product_1(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/1426210/capsule_616x353.jpg?t=1705372806",
            caption="It Takes Two\n"
                    "ЦЕНА:$39.99\n"
                    "ДАТА ВЫХОДА:26 мар. 2021 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная системаОС:Windows 8.1 64-bit or Windows 10 64-bit\n"
                    "Процессор: Intel Core i3-2100T or AMD FX 6100\n"
                    "Оперативная память: 8 GB ОЗУ\n"
                    "Видеокарта: Nvidia GeForce GTX 660 or AMD R7 260xDirectX\n"
                    "Место на диске: 50 GB\n", reply_markup=inlineBtn1)


@dp.message(F.text == "Terraria")
async def product_2(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/105600/header.jpg",
            caption="Terraria\n"
                    "ЦЕНА:$6.29\n"
                    "ДАТА ВЫХОДА:16 мая. 2011 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "ОС: Windows XP, Vista, 7\n"
                    "Процессор: с тактовой частотой 1,6 ГГц\n"
                    "Оперативная память: 512 МБ\n"
                    "Видеокарта: со 128 МБ видеопамяти и поддержкой шейдеров 1.1\n",reply_markup=inlineBtn1)


@dp.message(F.text == "Baldur's Gate 3")
async def product_3(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/1086940/capsule_616x353.jpg?t=1711532262",
            caption="Baldur's Gate 3\n"
                    "ЦЕНА:$29.99\n"
                    "ДАТА ВЫХОДА:3 авг. 2023 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10 64-bit\n"
                    "Процессор: Intel I5 4690 / AMD FX 8350\n"
                    "Место на диске: 150 GB\n"
                    "Оперативная память: 8 GB ОЗУ\n", reply_markup=inlineBtn1)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Rust")
async def product_4(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/252490/header.jpg?t=1701938429",
            caption="Rust\n"
                    "ЦЕНА:$19.99\n"
                    "ДАТА ВЫХОДА:8 фев. 2018 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10\n"
                    "Процессор: Intel Core i5-2300 | AMD FX-6350\n"
                    "Оперативная память: 8 GB ОЗУ\n"
                    "Видеокарта: GTX 670 2GB / AMD R9 280 DirectX: версии 11\n",reply_markup=inlineBtn1)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Stray")
async def product_5(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/1332010/capsule_616x353.jpg?t=1709318461",
            caption="Stray\n"
                    "ЦЕНА:$15.99\n"
                    "ДАТА ВЫХОДА:19 июл. 2022 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10 \n"
                    "Intel Core i5-2300 | AMD FX-6350\n"
                    "Место на диске: 10 GB\n"
                    "Оперативная память: 8 GB ОЗУ\n"
                    "Видеокарта: NVIDIA GeForce GTX 650 Ti, 2 GB | AMD Radeon R7 360, 2 GB\n",reply_markup=inlineBtn1) # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Starfield")
async def product_6(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/1716740/capsule_616x353.jpg?t=1704299959",
            caption="Starfield\n"
                    "ЦЕНА:$42.99\n"
                    "ДАТА ВЫХОДА:6 сен. 2023 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10\n"
                    "Процессор: AMD Ryzen 5 2600X, Intel Core i7-6800K\n"
                    "Место на диске: 125 GB\n"
                    "Видеокарта: AMD Radeon RX 5700,NVIDIA GeForce 1070 Ti\n"
                    "Оперативная память: 16 GB ОЗУ\n", reply_markup=inlineBtn1)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Alone in the Dark")
async def product_7(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/1310410/capsule_616x353.jpg?t=1711546287",
            caption="Alone in The Dark\n"
                    "ЦЕНА:$26.99\n"
                    "ДАТА ВЫХОДА:20 мар. 2024 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10\n"
                    "Процессор: Ryzen 3 3100 / Core i3-8300\n"
                    "Место на диске: 50 GB\n"
                    "Видеокарта: GeForce GTX 1050 Ti / Radeon RX 570\n"
                    "Оперативная память: 8 GB ОЗУ\n", reply_markup=inlineBtn2)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Resident Evil 7 Biohazard")
async def product_8(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/418370/header.jpg?t=1701827839",
            caption="Resident Evil 7 Biohazard\n"
                    "ЦЕНА:$15.99\n"
                    "ДАТА ВЫХОДА:24 янв. 2017 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10\n"
                    "Процессор: Intel® Core™ i5-4460, 2.70GHz or AMD FX™-6300 or better / Core i3-8300\n"
                    "Место на диске: 24 GB\n"
                    "Видеокарта: NVIDIA® GeForce® GTX 960 or AMD Radeon™ RX 460\n"
                    "Оперативная память: 8 GB ОЗУ\n", reply_markup=inlineBtn2)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Dead by Daylight")
async def product_9(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/381210/capsule_616x353.jpg?t=1712084583",
            caption="Dead by Daylight\n"
                    "ЦЕНА:$12.59\n"
                    "ДАТА ВЫХОДА:14 июн. 2016 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10\n"
                    "Процессор: Intel Core i3-4170 или AMD FX-8120\n"
                    "Место на диске: 50 GB\n"
                    "Видеокарта: поддержка DX11, совместимая видеокарта GeForce GTX 460 1 ГБ или AMD с HD 6850 1 ГБ\n"
                    "Оперативная память: 8 GB ОЗУ\n", reply_markup=inlineBtn2)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Sons Of The Forest")
async def product_10(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/1326470/capsule_616x353.jpg?t=1708624856",
            caption="Dead by Daylight\n"
                    "ЦЕНА:$12.59\n"
                    "ДАТА ВЫХОДА:22 фев. 2024 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10\n"
                    "Процессор: INTEL CORE I5-8400 or AMD RYZEN 3 3300X\n"
                    "Место на диске: 50 GB\n"
                    "Видеокарта: поддержка DX11, совместимая видеокарта GeForce GTX 460 1 ГБ или AMD с HD 6850 1 ГБ\n"
                    "Оперативная память: 8 GB ОЗУ\n", reply_markup=inlineBtn2)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Buckshot Roulette")
async def product_12(message: Message):
    await message.answer_photo(
            photo="https://i.ytimg.com/vi/96rymZ6RhCg/maxresdefault.jpg",
            caption="Buckshot Roulette\n"
                    "ЦЕНА:$1.34\n"
                    "ДАТА ВЫХОДА:4 апр. 2024 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10\n"
                    "Процессор: Intel Core i3\n"
                    "Оперативная память: 2 GB ОЗУ\n"
                    "Видеокарта:Относительно современная дискретная видеокарта (требуется поддержка Vulkan)\n"
                    "Место на диске:500 МБ\n", reply_markup=inlineBtn2)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Little Nightmares II")
async def product_13(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/860510/capsule_616x353.jpg?t=1711727324",
            caption="Little Nightmares II\n"
                    "ЦЕНА:$19.99\n"
                    "ДАТА ВЫХОДА:11 фев. 2021 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10\n"
                    "Процессор: Intel Core i5-2300 | AMD FX-4350\n"
                    "Оперативная память: 4 GB ОЗУ\n"
                    "Видеокарта: Nvidia GeForce GTX 570, 1 GB | AMD Radeon HD 7850, 2 GB\n", reply_markup=inlineBtn2)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "The Last of Us™: Part I")
async def product_14(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/1888930/capsule_616x353.jpg?t=1705640438",
            caption="The Last of Us™: Part I\n"
                    "ЦЕНА:$49.99\n"
                    "ДАТА ВЫХОДА:28 Mar 2023\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10\n"
                    "Процессор: AMD Ryzen 5 1500X, Intel Core i7-4770K\n"
                    "Оперативная память: 16 GB ОЗУ\n"
                    "Видеокарта: AMD Radeon RX 470 (4 GB), AMD Radeon RX 6500 XT (4 GB), NVIDIA GeForce GTX 1050 Ti \n"
                    "Место на диске:100 GB\n", reply_markup=inlineBtn3)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Red Dead Redemption 2")
async def product_15(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/1174180/capsule_616x353.jpg?t=1695140956",
            caption="Red Dead Redemption 2\n"
                    "ЦЕНА:$34.99\n"
                    "ДАТА ВЫХОДА:5 дек. 2019 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10\n"
                    "Процессор: Intel® Core™ i7-4770K / AMD Ryzen 5 1500X\n"
                    "Оперативная память: 12 GB ОЗУ\n"
                    "Место на диске: 150 GB\n"
                    "Видеокарта: Nvidia GeForce GTX 1060 6GB / AMD Radeon RX 480 4GB\n", reply_markup=inlineBtn3)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Ведьмак 3:Дикая Охота")
async def product_16(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/292030/capsule_616x353_russian.jpg?t=1710411171",
            caption="Ведьмак 3:Дикая Охота\n"
                    "ЦЕНА:$19.99\n"
                    "ДАТА ВЫХОДА:18 мая. 2015 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: 64-bit Windows 7, 64-bit Windows 8 (8.1)\n"
                    "Процессор: Intel CPU Core i5-2500K 3.3GHz / AMD A10-5800K APU (3.8GHz)\n"
                    "Оперативная память: 6 GB ОЗУ\n"
                    "Место на диске: 50 GB\n"
                    "Видеокарта: Nvidia GPU GeForce GTX 660 / AMD GPU Radeon HD 7870\n", reply_markup=inlineBtn3)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Mafia:Definitive Edition")
async def product_17(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/1030840/capsule_616x353.jpg?t=1632420251",
            caption="Mafia:Definitive Edition\n"
                    "ЦЕНА:$19.99\n"
                    "ДАТА ВЫХОДА:25 сен. 2020 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС:Windows 10 64-bit\n"
                    "Процессор: Intel Core-i5 2550K 3.4GHz / AMD FX 8120 3.1 GHz\n"
                    "Оперативная память: 6 GB ОЗУ\n"
                    "Место на диске: 50 GB\n"
                    "Видеокарта: NVIDIA GeForce GTX 660 / AMD Radeon HD 7870\n", reply_markup=inlineBtn3)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Cyberpunk 2077")
async def product_18(message: Message):
    await message.answer_photo(
            photo="https://shop.buka.ru/data/img_files/13473/additional750x580/FgF2C0SWi5_719x0.jpg",
            caption="Cyberpunk 2077\n"
                    "ЦЕНА:$29.99\n"
                    "ДАТА ВЫХОДА:10 дек. 2020 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС:Windows 10 64-bit\n"
                    "Процессор: Core i7-6700 or Ryzen 5 1600\n"
                    "Оперативная память: 12 GB ОЗУ\n"
                    "Место на диске: 70 GB\n"
                    "Видеокарта: GeForce GTX 1060 6GB or Radeon RX 580 8GB or Arc A380\n", reply_markup=inlineBtn3)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "God of War")
async def product_19(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/1593500/capsule_616x353.jpg?t=1695758729",
            caption="God of War\n"
                    "ЦЕНА:$39.99\n"
                    "ДАТА ВЫХОДА:14 янв. 2022 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС:Windows 10 64-bit\n"
                    "Процессор: Intel i5-2500k (4 core 3.3 GHz) or AMD Ryzen 3 1200 (4 core 3.1 GHz)\n"
                    "Оперативная память: 8 GB ОЗУ\n"
                    "Место на диске: 70 GB\n"
                    "Видеокарта: NVIDIA GTX 960 (4 GB) or AMD R9 290X (4 GB)\n", reply_markup=inlineBtn3)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "BeamNG.drive")
async def product_20(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/284160/capsule_616x353.jpg?t=1709017559",
            caption="BeamNG.drive\n"
                    "ЦЕНА:$12.49 \n"
                    "ДАТА ВЫХОДА:29 мая. 2015 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС *: Windows 7 Service Pack 1 64-bit\n"
                    "Процессор: AMD FX 6300 3.5Ghz / Intel Core i3-6300 3.8Ghz \n"
                    "Оперативная память: 16 GB ОЗУ\n"
                    "Место на диске: 45 GB\n"
                    "Видеокарта: Radeon HD 7750 / Nvidia GeForce GTX 550 Ti\n", reply_markup=inlineBtn4)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Wreckfest")
async def product_21(message: Message):
    await message.answer_photo(
            photo="https://gaming-cdn.com/images/products/582/orig/wreckfest-pc-game-steam-cover.jpg?v=1692960253",
            caption="Wreckfest\n"
                    "ЦЕНА:$14.99\n"
                    "ДАТА ВЫХОДА:14 июн. 2018 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС : Windows 10\n"
                    "Процессор: Intel® Core™ i3 with 2.8 GHz or AMD equivalent\n"
                    "Оперативная память: 8 GB ОЗУ\n"
                    "Место на диске: 32 GB\n"
                    "Видеокарта: NVIDIA Geforce® GTX™ 560 or AMD Radeon™ HD 7770\n", reply_markup=inlineBtn4)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Forza Horizon 4")
async def product_22(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/1293830/capsule_616x353.jpg?t=1702576030",
            caption="Forza Horizon 4\n"
                    "ЦЕНА:$27.99\n"
                    "ДАТА ВЫХОДА:9 мар. 2021 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10 version 15063.0 or higher\n"
                    "Процессор: Intel i3-4170 @ 3.7Ghz OR Intel i5 750 @ 2.67Ghz\n"
                    "Оперативная память: 8 GB ОЗУ\n"
                    "Место на диске: 80 GB\n"
                    "Видеокарта: NVidia 650TI OR AMD R7 250x\n", reply_markup=inlineBtn4)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Need for Speed™ Heat")
async def product_23(message: Message):
    await message.answer_photo(
            photo="https://i.ytimg.com/vi/9ewiJJe_nYI/maxresdefault.jpg",
            caption="Need for Speed™ Heat\n"
                    "ЦЕНА:$69.99\n"
                    "ДАТА ВЫХОДА:8 ноя. 2019 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10\n"
                    "Процессор: FX-6350 or Equivalent; Core i5-3570 or Equivalent\n"
                    "Оперативная память: 8 GB ОЗУ\n"
                    "Место на диске: 50 GB\n"
                    "Видеокарта: AMD: Radeon 7970/Radeon R9 280x or Equivalent; NVIDIA: GeForce GTX 760 or Equivalent\n", reply_markup=inlineBtn4)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Forza Horizon 5")
async def product_24(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/1551360/header.jpg?t=1711724056",
            caption="Forza Horizon 5\n"
                    "ЦЕНА:$34.78\n"
                    "ДАТА ВЫХОДА:9 ноя. 2021 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10 \n"
                    "Процессор: Intel i5-4460 or AMD Ryzen 3 1200\n"
                    "Оперативная память: 8 GB ОЗУ\n"
                    "Место на диске: 110 GB\n"
                    "Видеокарта: NVidia GTX 970 OR AMD RX 470\n", reply_markup=inlineBtn4)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Need for Speed™ Hot Pursuit Remastered")
async def product_25(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/1328660/capsule_616x353.jpg?t=1667318486",
            caption="Need for Speed™ Hot Pursuit Remastered\n"
                    "ЦЕНА:$29.99\n"
                    "ДАТА ВЫХОДА:6 ноя. 2020 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10, 64 bit \n"
                    "Процессор: (AMD) Phenom II X4 965 or equivalent (Intel) Corei3-2120 or equivalent\n"
                    "Оперативная память: 8 GB ОЗУ\n"
                    "Место на диске: 45 GB\n"
                    "Видеокарта: (AMD) Radeon HD 5870 or equivalent (Nvidia) GeForce GT 640 or equivalent\n", reply_markup=inlineBtn4)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Machinarium")
async def product_26(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/40700/capsule_616x353.jpg?t=1683630220",
            caption="Machinarium\n"
                    "ЦЕНА:$3.49\n"
                    "ДАТА ВЫХОДА:16 окт. 2009 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "ОС: Microsoft® Windows® XP/Vista/7/8/10\n"
                    "Процессор: 1.8 ГГц\n"
                    "Жесткий диск: 380 МБ свободного места\n"
                    "Память: 1 ГБ\n",reply_markup=inlineBtn5)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Creaks")
async def product_27(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/956030/capsule_616x353.jpg?t=1682627734",
            caption="Creaks\n"
                    "ЦЕНА:$6.49\n"
                    "ДАТА ВЫХОДА:22 июл. 2020 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 7 (64-bit) or better \n"
                    "Процессор: 2 GHz Intel i5 or better\n"
                    "Оперативная память: 4 GB ОЗУ\n"
                    "Место на диске: 5 GB\n"
                    "Видеокарта: DirectX 11 compatible GPU\n", reply_markup=inlineBtn5)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "LIMBO")
async def product_28(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/48000/header.jpg?t=1673342440",
            caption="LIMBO\n"
                    "ЦЕНА:$6.29\n"
                    "ДАТА ВЫХОДА:2 авг. 2011 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows XP, Vista, 7\n"
                    "Процессор: с частотой 2 ГГц\n"
                    "Оперативная память:512 МБ\n"
                    "Жесткий диск: 150 МБ свободного места\n"
                    "Видеокарта:не старше 5 лет. Интегрированные видеокарты и очень дешевые экземпляры могут не работать\n",reply_markup=inlineBtn5)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Portal 2")
async def product_29(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/620/header.jpg",
            caption="Portal 2\n"
                    "ЦЕНА:$6.29\n"
                    "ДАТА ВЫХОДА:19 апр. 2011 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС : Windows 7/Vista/XP\n"
                    "Процессор: Pentium 4 с тактовой частотой 3 ГГц, Dual Core 2.0 (или выше) или AMD64X2 (или выше)\n"
                    "Оперативная память: 2 GB ОЗУ\n"
                    "Место на диске: 8 GB\n"
                    "Видеокарта:(ATI Radeon X800 или выше/ NVIDIA GeForce 7600 или выше/ Intel HD Graphics 2000 или выше).\n", reply_markup=inlineBtn5) # noqa


@dp.message(F.text == "Teardown")
async def product_30(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/1167630/capsule_616x353.jpg?t=1700055440",
            caption="Teardown\n"
                    "ЦЕНА:$16.49\n"
                    "ДАТА ВЫХОДА:21 апр. 2022 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10, 64 bit \n"
                    "Процессор:  Intel Core i7 or better\n"
                    "Оперативная память: 4 GB ОЗУ\n"
                    "Место на диске: 4 GB\n"
                    "Видеокарта: NVIDIA GeForce GTX 1080 or similar. 8 Gb VRAM.\n", reply_markup=inlineBtn5)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "The Talos Principle 2")
async def product_31(message: Message):
    await message.answer_photo(
            photo="https://upload.wikimedia.org/wikipedia/ru/1/1c/The_Talos_Principle_2.jpg",
            caption="The Talos Principle 2\n"
                    "ЦЕНА:$14.49\n"
                    "ДАТА ВЫХОДА:2 ноя. 2023 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС:64-bit Windows 10 \n"
                    "Процессор: 4 core CPU @ 2.5 GHz (AMD Ryzen 5, Intel core i3/i5)\n"
                    "Оперативная память: 8 GB ОЗУ\n"
                    "Место на диске:  75 GB\n"
                    "Видеокарта: 4 GB VRAM; Radeon RX 470, GeForce GTX 970\n", reply_markup=inlineBtn5)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Call of Duty:MW III")
async def product_32(message: Message):
    await message.answer_photo(
            photo="https://upload.wikimedia.org/wikipedia/ru/0/0b/Call_Of_Duty_MW3_2023.jpg",
            caption="Call of Duty: Modern Warfare III\n"
                    "ЦЕНА:$69.99\n"
                    "ДАТА ВЫХОДА:28 окт. 2022 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС:64-разрядная Windows® 10 (последнее обновление)\n"
                    "Процессор:Intel Core i7-6700К или AMD Ryzen 5 1600X.\n"
                    "Оперативная память: 16 GB ОЗУ\n"
                    "Место на диске: 149 Гб свободного места на SSD.\n"
                    "Видеокарта GeForce GTX 1080 Ti/RTX 3060 или Radeon RX 6600XT.\n", reply_markup=inlineBtn6)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Far Cry 6")
async def product_33(message: Message):
    await message.answer_photo(
            photo="https://cdn2.unrealengine.com/tetra-preorder-standard-edition-epic-store-landscape-2560x1440-2560x1440-430970417.jpg", # noqa
            caption="Far Cry 6\n"
                    "ЦЕНА:$32.99\n"
                    "ДАТА ВЫХОДА:11 мая. 2023 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10 (20H1 version or newer, 64-bit versions)\n"
                    "Процессор: AMD Ryzen 5 3600X @ 3.8 GHz or Intel Core i7-7700 @ 3.6 GHz \n"
                    "Оперативная память: 16 GB ОЗУ\n"
                    "Место на диске:   170 GB\n"
                    "Видеокарта: AMD RX Vega 64 (8 GB) or NVIDIA GeForce GTX 1080 (8 GB)\n", reply_markup=inlineBtn6)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Assassin's Creed Origins")
async def product_34(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/582160/capsule_616x353.jpg?t=1703026224",
            caption="Assassin's Creed Origin\n"
                    "ЦЕНА:$32.99\n"
                    "ДАТА ВЫХОДА:27 окт. 2017 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС: Windows 10 (64-bit versions only) \n"
                    "Процессор:Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz or equivalent \n"
                    "Оперативная память: 8 GB ОЗУ\n"
                    "Место на диске:  42  GB\n"
                    "Видеокарта: NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0 or better) \n", reply_markup=inlineBtn6)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "HELLDIVERS™ 2")
async def product_35(message: Message):
    await message.answer_photo(
            photo="https://cdn.akamai.steamstatic.com/steam/apps/553850/capsule_616x353.jpg?t=1709666906",
            caption="HELLDIVERS™ 2\n"
                    "ЦЕНА:$39.99\n"
                    "ДАТА ВЫХОДА:8 фев. 2024 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС:Windows 10 \n"
                    "Процессор: Intel Core i7-9700K or AMD Ryzen 7 3700X \n"
                    "Оперативная память: 16 GB ОЗУ\n"
                    "Место на диске: 100 GB\n"
                    "Видеокарта: NVIDIA GeForce RTX 2060 or AMD Radeon RX 6600XT\n", reply_markup=inlineBtn6)  # CHANGE THIS BUTTONS NAME


@dp.message(F.text == "Grand Theft Auto V")
async def product_36(message: Message):
    await message.answer_photo(
            photo="https://assetsio.gnwcdn.com/eurogamer-zjp1vx.jpg?width=1200&height=1200&fit=bounds&quality=70&format=jpg&auto=webp",  # noqa
            caption="Grand Theft Auto V\n"
                    "ЦЕНА:$33.98\n"
                    "ДАТА ВЫХОДА:14 апр. 2015 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС:Windows 10 64 Bit \n"
                    "Процессор:Intel Core i5 3470  3.2 Ггц (четырехъядерный) / AMD X8 FX-8350  4 Ггц (восьмиядерный) \n"  # noqa
                    "Оперативная память: 8 GB ОЗУ\n"
                    "Место на диске:  110  GB\n"
                    "Видеокарта:NVIDIA GTX 660 с 2 Гб видеопамяти / AMD HD7870 с 2 Гб видеопамяти \n", reply_markup=inlineBtn6)


@dp.message(F.text == "Warface")
async def product_37(message: Message):
    await message.answer_photo(
            photo="https://cdn2.unrealengine.com/featured-image-1920x1080-428c2a37bd6e.png",
            caption="Warface\n"
                    "ЦЕНА:\n"
                    "ДАТА ВЫХОДА:21 окт 2013 г.\n"
                    "СИСТЕМНЫЕ ТРЕБОВАНИЯ:\n"
                    "64-разрядные процессор и операционная система\n"
                    "ОС:Windows 7 / 8 / 10 \n"
                    "Процессор:Core i3-3210 / AMD Phenom II X4 910e \n"
                    "Оперативная память: 4 GB ОЗУ\n"
                    "Место на диске: 35 GB\n"
                    "Видеокарта: GeForce 650 Ti / Radeon HD 5970\n", reply_markup=inlineBtn6)


dp.callback_query.register(order_1, F.data == "pay_1")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_2, F.data == "pay_2")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_3, F.data == "pay_3")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_4, F.data == "pay_4")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_5, F.data == "pay_5")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_6, F.data == "pay_6")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_7, F.data == "pay_7")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_8, F.data == "pay_8")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_9, F.data == "pay_9")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_10, F.data == "pay_10")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_11, F.data == "pay_11")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_12, F.data == "pay_12")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_13, F.data == "pay_13")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_14, F.data == "pay_14")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_15, F.data == "pay_15")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_16, F.data == "pay_16")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_17, F.data == "pay_17")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_18, F.data == "pay_18")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_19, F.data == "pay_19")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_20, F.data == "pay_20")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_21, F.data == "pay_21")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_22, F.data == "pay_22")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_23, F.data == "pay_23")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_24, F.data == "pay_24")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_25, F.data == "pay_25")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_26, F.data == "pay_26")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_27, F.data == "pay_27")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_28, F.data == "pay_28")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_29, F.data == "pay_29")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_30, F.data == "pay_30")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_31, F.data == "pay_31")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_32, F.data == "pay_32")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_33, F.data == "pay_33")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_34, F.data == "pay_34")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_35, F.data == "pay_35")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_36, F.data == "pay_36")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


dp.callback_query.register(order_37, F.data == "pay_37")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
