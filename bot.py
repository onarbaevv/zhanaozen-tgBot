import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# 1. Логтарды баптау (Боттың жұмысын бақылау үшін)
logging.basicConfig(level=logging.INFO)

# 2. Сіздің Телеграм бот токеніңіз
BOT_TOKEN = "8357496348:AAG4b6HFTxzbBnZUz4pIyZ5OO0rakLOu420"

# Бот пен Диспеччерді іске қосу
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 3. Басты мәзір батырмалары (Reply-клавиатура)
def get_main_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="ℹ️ Біз туралы"))
    builder.add(types.KeyboardButton(text="🎨 Бағыттар мен Клубтар"))
    builder.add(types.KeyboardButton(text="📞 Байланыс деректері"))
    # Батырмаларды реттеп орналастыру (2 батырма жоғарыда, 1 батырма төменде)
    builder.adjust(2, 1)
    return builder.as_markup(resize_keyboard=True)

# 4. /start командасы басылғанда шығатын сәлемдесу мәтіні
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    welcome_text = (
        f"👋 **Сәлем, {message.from_user.first_name}!**\n\n"
        "Жаңаөзен қалалық жастар ресурстық орталығының ресми ботына қош келдің! "
        "Бұл жерде сен өзіңе пайдалы ақпарат тауып, қаламыздың белсенді жастарының қатарына қосыла аласың. 🚀\n\n"
        "Қажетті ақпаратты алу үшін төмендегі батырмаларды қолдан:"
    )
    await message.answer(welcome_text, parse_mode="Markdown", reply_markup=get_main_keyboard())

# 5. "ℹ️ Біз туралы" батырмасы басылғанда
@dp.message(F.text == "ℹ️ Біз туралы")
async def about_us(message: types.Message):
    text = (
        "🏢 **Жаңаөзен қалалық жастар ресурстық орталығы (ЖРО)**\n\n"
        "**Біздің мақсатымыз:** Жастардың бастамаларына қолдау көрсету, олардың "
        "әлеуетін дамыту, бос уақытын тиімді ұйымдастыру және мемлекеттік жастар саясатын жүзеге асыру.\n\n"
        "✨ Біз белсенді, талантты және жасампаз жастарды біріктіретін үлкен отбасымыз!"
    )
    await message.answer(text, parse_mode="Markdown")

# 6. "🎨 Бағыттар мен Клубтар" батырмасы басылғанда
@dp.message(F.text == "🎨 Бағыттар мен Клубтар")
async def directions(message: types.Message):
    text = (
        "🚀 **Орталықтың негізгі жұмыс бағыттары мен клубтары:**\n\n"
        "🙋‍♂️ **Волонтерлік қозғалыс:** Қалалық әлеуметтік және қайырымдылық іс-шаралар.\n"
        "🗣 **Пікірсайыс (Дебат клубы):** Тұлғалық даму, шешендік өнер мен сыни ойлау.\n"
        "💼 **Жастарды жұмыспен қамту:** «Жасыл ел» еңбек жасақтары және Жастар практикасы бойынша кеңес беру.\n"
        "🧠 **Психологиялық көмек:** Жастарға арналған тегін және құпия консультациялар.\n"
        "🇬🇧 **Үйірмелер:** Тіл үйрену курстары, шығармашылық пен спорттық жобалар."
    )
    await message.answer(text, parse_mode="Markdown")

# 7. "📞 Байланыс деректері" батырмасы басылғанда
@dp.message(F.text == "📞 Байланыс деректері")
async def contacts(message: types.Message):
    text = (
        "📞 **Байланыс және Мекенжай:**\n\n"
        "📍 **Мекенжай:** Жаңаөзен қаласы, Жастар орталығының ғимараты.\n"
        "⏰ **Жұмыс уақыты:** Дүйсенбі - Жұма, 09:00 - 18:30 (Үзіліс: 13:00 - 14:30).\n"
        "📧 **E-mail:** zhanaozen_jro@mail.ru\n"
        "🌐 **Instagram:** @zhanaozen_jro\n\n"
        "✍️ Сұрақтарың немесе ұсыныстарың болса, бізге хабарласудан тартынба!"
    )
    await message.answer(text, parse_mode="Markdown")

# 8. Ботты іске қосу функциясы
async def main():
    # Ескі хабарламаларды өшіріп, жаңаларын ғана қабылдау
    await bot.delete_webhook(drop_pending_updates=True)
    print("Бот сәтті іске қосылды...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())