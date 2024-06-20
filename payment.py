from aiogram import Bot, types
from aiogram.types import LabeledPrice, PreCheckoutQuery
from config import PAY_TOKEN


async def order_1(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="It Takes Two",
                           description="Приключение,Adventure",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://cdn.akamai.steamstatic.com/steam/apps/1426210/capsule_616x353.jpg?t=1705372806",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=506_429_88),
                               LabeledPrice(label="Скидка", amount=100_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='It Takes Two',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """

    await message.answer(msg)


async def order_2(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Terraria",
                           description="Выживание,Приключение",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://cdn.akamai.steamstatic.com/steam/apps/105600/header.jpg",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=79_656_01),
                               LabeledPrice(label="Скидка", amount=-20_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Terraria',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_2(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_3(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Baldur's Gate 3",
                           description="RPG,Подземелье",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="https://cdn.akamai.steamstatic.com/steam/apps/1086940/capsule_616x353.jpg?t=1711532262",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=379_790_75),
                               LabeledPrice(label="Скидка", amount=-57_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Baldurs Gate 3',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_3(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_4(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_4(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_5(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='UZS',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_5(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_6(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_6(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_7(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_7(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_8(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_8(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_9(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_9(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_10(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_10(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_11(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_11(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_12(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_12(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_13(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_13(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_14(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_14(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_15(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_15(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_16(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_16(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_17(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_17(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_18(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_18(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_19(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_19(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_20(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_20(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_21(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_21(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_22(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_22(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_23(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_23(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_24(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_24(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_25(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_25(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_26(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_26(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_27(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_27(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_28(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_28(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_29(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_29(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_30(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_30(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_31(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_31(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_32(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_32(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_33(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_33(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_34(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_34(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_35(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_35(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_36(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_36(message: types.Message, bot: Bot):  # NOQA
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


async def order_37(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="",
                           description="",
                           provider_token=PAY_TOKEN,
                           currency='USD',
                           photo_url="",  # noqa
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Цена", amount=30_000_00),
                               LabeledPrice(label="Скидка", amount=-5_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='',
                           request_timeout=15
                           )

async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):  # NOQA
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment_37(message: types.Message, bot: Bot):
    msg = f"""
    Успешная Оплата ✅ 
    Название товара : {message.successful_payment.invoice_payload}
    Цена: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Успешно Купленно :  ✅ 
    """
    await message.answer(msg)


