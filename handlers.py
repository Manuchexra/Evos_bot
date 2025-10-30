import json, os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from keyboards import main_menu, filiallar_menu, ish_orinlari_menu

EVOS_LOGO_URL = "https://marketing.uz/uploads/articles/2323/article-original.jpg"
USER_DATA_FILE = "user_data.json"

# ---------- JSON funksiyalar ----------
def load_user_data():
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "w") as f:
            json.dump({}, f)
    with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_user_data(data):
    with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_lang(user_id):
    data = load_user_data()
    return data.get(str(user_id), "uz")

def set_lang(user_id, lang):
    data = load_user_data()
    data[str(user_id)] = lang
    save_user_data(data)

# ---------- Matnlar ----------
texts = {
    "welcome": {
        "uz": "Assalomu alaykum! 👋\nEVOS rasmiy botiga xush kelibsiz!",
        "ru": "Здравствуйте! 👋 Добро пожаловать в официальный бот EVOS!",
        "en": "Hello! 👋 Welcome to the official EVOS bot!"
    },
    "company": {
        "uz": (
            "EVOS ® tez xizmat ko‘rsatish restoranlari tarmog‘i bir joyda turmaydi — "
            "siz uchun va siz bilan doimo o‘sib boradi! 🌱\n\n"
            "📍 50 dan ortiq filiallar O‘zbekistonda!\n👩‍🍳 Ishonchli brend, barqaror daromad va martaba imkoniyatlari!"
        ),
        "ru": (
            "EVOS ® — сеть ресторанов быстрого обслуживания, которая растёт вместе с вами! 🌱\n\n"
            "📍 Более 50 филиалов по всему Узбекистану.\n👩‍🍳 Надёжный бренд и карьерные перспективы!"
        ),
        "en": (
            "EVOS ® — a fast-service restaurant chain growing with you! 🌱\n\n"
            "📍 Over 50 branches across Uzbekistan.\n👩‍🍳 Trusted brand, stable income and career growth!"
        )
    }
}

# /start
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user = update.effective_user
    lang = get_lang(chat_id)

    username = user.username or user.first_name
    print(f"👤 Foydalanuvchi: {username} ({chat_id}) /start bosdi")

    context.bot.send_photo(
        chat_id=chat_id,
        photo=EVOS_LOGO_URL,
        caption=texts["welcome the telegram bot"][lang],
        reply_markup=main_menu(lang)
    )

# ---------- Asosiy handler ----------
def main_menu_handler(update: Update, context: CallbackContext):
    text = update.message.text
    chat_id = update.effective_chat.id
    lang = get_lang(chat_id)

    # --- Til tanlash menyusi ---
    if text in ["🇺🇿/🇷🇺/🇬🇧 Til", "🇺🇿/🇷🇺/🇬🇧 Язык", "🇺🇿/🇷🇺/🇬🇧 Language"]:
        keyboard = ReplyKeyboardMarkup(
            [["🇺🇿 O‘zbekcha", "🇷🇺 Русский", "🇬🇧 English"]],
            resize_keyboard=True
        )
        update.message.reply_text(
            "Tilni tanlang / Выберите язык / Choose language:",
            reply_markup=keyboard
        )
        return

    # --- Til o‘zgartirish ---
    if text in ["🇺🇿 O‘zbekcha", "🇷🇺 Русский", "🇬🇧 English"]:
        new_lang = "uz" if "🇺🇿" in text else "ru" if "🇷🇺" in text else "en"
        set_lang(chat_id, new_lang)
        msg = {
            "uz": "✅ Til o‘zgartirildi!",
            "ru": "✅ Язык изменён!",
            "en": "✅ Language changed!"
        }[new_lang]
        update.message.reply_text(msg, reply_markup=main_menu(new_lang))
        return

    # --- Kompaniya haqida ---
    if text in ["🏢 Kompaniya haqida", "🏢 О компании", "🏢 About Company"]:
        context.bot.send_photo(chat_id=chat_id, photo=EVOS_LOGO_URL, caption=texts["company"][lang], reply_markup=main_menu(lang))
        return

    # --- Filiallar ---
    if text in ["📍 Filiallar", "📍 Филиалы", "📍 Branches"]:
        update.message.reply_text(
            {"uz": "📍 Filialni tanlang:", "ru": "📍 Выберите филиал:", "en": "📍 Choose a branch:"}[lang],
            reply_markup=filiallar_menu(lang)
        )
        return

    # --- Filiallar joylashuvi ---
    filiallar = {
        "📍 Toshkent (Amir Temur)": (41.311081, 69.240562, "Amir Temur ko'chasi, 10"),
        "📍 Samarqand (Registon)": (39.6542, 66.9750, "Registon maydoni yaqinida"),
        "📍 Farg‘ona (Markaz)": (40.3842, 71.7843, "Markaziy ko‘cha, 5")
    }

    if text in filiallar:
        lat, lon, address = filiallar[text]
        msg = {
            "uz": f"📍 Manzil: {address}\n⏰ Ish vaqti: 08:00 - 23:00",
            "ru": f"📍 Адрес: {address}\n⏰ Время работы: 08:00 - 23:00",
            "en": f"📍 Address: {address}\n⏰ Working hours: 08:00 - 23:00"
        }[lang]
        update.message.reply_text(msg, reply_markup=filiallar_menu(lang))
        context.bot.send_location(chat_id=chat_id, latitude=lat, longitude=lon)
        return

    # --- Bo‘sh ish o‘rinlari ---
    if text in ["💼 Bo'sh ish o'rinlari", "💼 Вакансии", "💼 Vacancies"]:
        update.message.reply_text(
            {"uz": "💼 EVOS jamoasiga qo‘shiling!\n📍 Shaharni tanlang:",
             "ru": "💼 Присоединяйтесь к команде EVOS!\n📍 Выберите город:",
             "en": "💼 Join EVOS team!\n📍 Choose a city:"}[lang],
            reply_markup=ish_orinlari_menu(lang)
        )
        return

    # --- Shaharlar uchun ish joylari ---
    cities = ["Toshkent", "Samarqand", "Farg‘ona", "Shahrisabz", "Xorazm viloyati", "Navoiy", "Urganch"]
    if text in cities:
        msg = {
            "uz": f"✅ {text} shahridagi bo‘sh ish o‘rinlari:\n- Kassir\n- Oshpaz\n- Administrator\n\n📩 Ariza: hr@evos.uz",
            "ru": f"✅ Вакансии в городе {text}:\n- Кассир\n- Повар\n- Администратор\n\n📩 Резюме: hr@evos.uz",
            "en": f"✅ Vacancies in {text}:\n- Cashier\n- Cook\n- Administrator\n\n📩 Apply: hr@evos.uz"
        }[lang]
        update.message.reply_text(msg, reply_markup=ish_orinlari_menu(lang))
        return

     # --- 🍔 Menyu ---
    if text in ["🍔 Menyu", "🍔 Меню", "🍔 Menu"]:
        photo_path = "image.png"
        if lang == "uz":
            caption = (
                "🌐 Evos saytiga o'tish 👉 https://evos.uz/\n\n"
                "📱 Bizni kuzating:\n"
                "Instagram — https://www.instagram.com/evosuzbekistan/\n"
                "Telegram — https://t.me/evosdeliverybot\n"
                "Facebook — https://www.facebook.com/evosuzbekistan/"
            )
        elif lang == "ru":
            caption = (
                "🌐 Перейдите на сайт EVOS 👉 https://evos.uz/\n\n"
                "📱 Мы в соцсетях:\n"
                "Instagram — https://www.instagram.com/evosuzbekistan/\n"
                "Telegram — https://t.me/evosdeliverybot\n"
                "Facebook — https://www.facebook.com/evosuzbekistan/"
            )
        else:
            caption = (
                "🌐 Visit EVOS website 👉 https://evos.uz/\n\n"
                "📱 Follow us:\n"
                "Instagram — https://www.instagram.com/evosuzbekistan/\n"
                "Telegram — https://t.me/evosdeliverybot\n"
                "Facebook — https://www.facebook.com/evosuzbekistan/"
            )

        with open(photo_path, "rb") as photo:
            context.bot.send_photo(chat_id=chat_id, photo=photo, caption=caption, reply_markup=main_menu(lang))
        return


    # --- Yangiliklar ---
    if text in ["📰 Yangiliklar", "📰 Новости", "📰 News"]:
        msg = {
            "uz": "📰 Yangi filiallar va aksiyalar!",
            "ru": "📰 Новые филиалы и акции!",
            "en": "📰 New branches and promotions!"
        }[lang]
        update.message.reply_text(msg, reply_markup=main_menu(lang))
        return

        # --- Kontaktlar ---
    if text in ["📞 Kontaktlar/Manzil", "📞 Контакты/Адрес", "📞 Contacts/Address"]:
        contact_text = {
            "uz": (
                "📍 *EVOS markaziy ofisi*\n"
                "Manzil: Toshkent shahri, Amir Temur shoh ko'chasi, 10\n\n"
                "☎️ Telefon: +998 71 123 45 67\n"
                "📩 Email: info@evos.uz\n"
                "🌐 Sayt: https://evos.uz/\n\n"
                "📱 Ijtimoiy tarmoqlar:\n"
            ),
            "ru": (
                "📍 *Главный офис EVOS*\n"
                "Адрес: г. Ташкент, проспект Амира Темура, 10\n\n"
                "☎️ Телефон: +998 71 123 45 67\n"
                "📩 Email: info@evos.uz\n"
                "🌐 Сайт: https://evos.uz/\n\n"
                "📱 Мы в соцсетях:\n"
            ),
            "en": (
                "📍 *EVOS Headquarters*\n"
                "Address: Amir Temur Avenue, 10, Tashkent, Uzbekistan\n\n"
                "☎️ Phone: +998 71 123 45 67\n"
                "📩 Email: info@evos.uz\n"
                "🌐 Website: https://evos.uz/\n\n"
                "📱 Follow us:\n"
            )
        }[lang]

        update.message.reply_text(contact_text, parse_mode="Markdown", reply_markup=main_menu(lang))

        # 🗺️ Lokatsiya (Toshkentdagi EVOS ofis)
        context.bot.send_location(chat_id=chat_id, latitude=41.311081, longitude=69.240562)
        return


    # --- Orqaga yoki Bekor qilish ---
    if text in ["⬅️ Orqaga", "⬅️ Назад", "⬅️ Back", "❌ Bekor qilish ❌", "❌ Отмена ❌", "❌ Cancel ❌"]:
        update.message.reply_text("🏠", reply_markup=main_menu(lang))
        return

    # --- Noma'lum xabarlar ---
    update.message.reply_text(
        {"uz": "Iltimos, menyudan tanlang.", "ru": "Пожалуйста, выберите из меню.", "en": "Please choose from the menu."}[lang],
        reply_markup=main_menu(lang)
    )
