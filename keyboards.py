from telegram import ReplyKeyboardMarkup

def main_menu(lang):
    menus = {
        "uz": [
            ["🏢 Kompaniya haqida", "📍 Filiallar"],
            ["💼 Bo'sh ish o'rinlari", "🍔 Menyu"],
            ["📰 Yangiliklar", "📞 Kontaktlar/Manzil"],
            ["🇺🇿/🇷🇺/🇬🇧 Til"]
        ],
        "ru": [
            ["🏢 О компании", "📍 Филиалы"],
            ["💼 Вакансии", "🍔 Меню"],
            ["📰 Новости", "📞 Контакты/Адрес"],
            ["🇺🇿/🇷🇺/🇬🇧 Язык"]
        ],
        "en": [
            ["🏢 About Company", "📍 Branches"],
            ["💼 Vacancies", "🍔 Menu"],
            ["📰 News", "📞 Contacts/Address"],
            ["🇺🇿/🇷🇺/🇬🇧 Language"]
        ]
    }
    return ReplyKeyboardMarkup(menus[lang], resize_keyboard=True)

def filiallar_menu(lang):
    back = {"uz": "⬅️ Orqaga", "ru": "⬅️ Назад", "en": "⬅️ Back"}[lang]
    return ReplyKeyboardMarkup([
        ["📍 Toshkent (Amir Temur)", "📍 Samarqand (Registon)"],
        ["📍 Farg‘ona (Markaz)"],
        [back]
    ], resize_keyboard=True)

def ish_orinlari_menu(lang):
    back = {"uz": "⬅️ Orqaga", "ru": "⬅️ Назад", "en": "⬅️ Back"}[lang]
    cancel = {"uz": "❌ Bekor qilish ❌", "ru": "❌ Отмена ❌", "en": "❌ Cancel ❌"}[lang]
    return ReplyKeyboardMarkup([
        ["Toshkent", "Samarqand"],
        ["Farg‘ona", "Shahrisabz"],
        ["Xorazm viloyati", "Navoiy"],
        ["Urganch"],
        [cancel, back]
    ], resize_keyboard=True)
