# 🍔 EVOS Telegram Bot

> **EVOS®** — O‘zbekistonning mashhur tez xizmat ko‘rsatish restoranlari tarmog‘i uchun yaratilgan rasmiy Telegram bot.  
> Bot foydalanuvchilarga kompaniya haqida ma’lumot olish, filiallarni xaritada ko‘rish, menyu bilan tanishish va bo‘sh ish o‘rinlariga murojaat qilish imkonini beradi.

---

## ✨ Asosiy imkoniyatlar

✅ Uch tilda ishlaydi: 🇺🇿 O‘zbekcha | 🇷🇺 Русский | 🇬🇧 English  
🏢 Kompaniya haqida to‘liq ma’lumot (rasm bilan)  
🍔 Menyu rasmi + ijtimoiy tarmoqlar havolalari  
📍 Filiallar joylashuvi (xarita bilan birga)  
💼 Bo‘sh ish o‘rinlari shaharlar bo‘yicha  
📞 Kontaktlar va manzil ma’lumotlari  

💾 Foydalanuvchi tili `user_data.json` faylida saqlanadi  
🧠 Har bir foydalanuvchi /start bosganda terminalda `print()` orqali chiqadi  

---

## 🧩 Ishlash prinsipi

1. **/start** — foydalanuvchi botni ishga tushiradi.  
   - Bot foydalanuvchining tilini aniqlaydi yoki tanlash menyusini ko‘rsatadi.  
   - EVOS logosi bilan kutib olish xabari yuboriladi.

2. **Asosiy menyu** ochiladi:  

🍔 Menyu
🏢 Kompaniya haqida
💼 Bo‘sh ish o‘rinlari
📍 Filiallar
📰 Yangiliklar
📞 Kontaktlar/Manzil
🇺🇿/🇷🇺/🇬🇧 Til


3. **Har bir bo‘limda:**
- “🍔 Menyu” bosilganda — EVOS menyu rasmi yuboriladi, ijtimoiy tarmoqlar havolalari bilan.  
- “📍 Filiallar” bosilganda — filial joylashuvi va xarita yuboriladi.  
- “💼 Bo‘sh ish o‘rinlari” bosilganda — shaharlar ro‘yxati chiqadi va ish pozitsiyalari ko‘rsatiladi.  
- “📞 Kontaktlar” — telefon, sayt va xaritadagi manzil yuboriladi.  
- “🇺🇿/🇷🇺/🇬🇧 Til” — foydalanuvchi yangi tilni tanlaydi, va bu tanlov `user_data.json` faylida saqlanadi.

4. **Foydalanuvchi ma’lumotlari**  
- Har bir yangi /start bosgan foydalanuvchi terminalga chiqadi:  
  ```
  👤 Yangi foydalanuvchi: username (ID: 123456789) botni ishga tushirdi.
  ```
- Ularning tili va statusi `user_data.json` faylida saqlanadi.

---

## ⚙️ O‘rnatish

```bash
git clone https://github.com/username/evos-bot.git
cd evos-bot
pip install -r requirements.txt

🔑 Sozlash

config.py faylini oching va tokenni joylashtiring:

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"


Rasm uchun image.png faylni Evos menyu rasmi sifatida joylashtiring.

Keyin botni ishga tushiring:

python bot.py


🌐 Bog‘lanishlar

🌍 evos.uz

📸 Instagram

💬 Telegram

📘 Facebook

🧠 Texnik qisqacha ma’lumot

Platforma: Python 3.x

Kutubxona: python-telegram-bot (v13+)

Ma’lumot saqlash: JSON fayl (user_data.json)

Interfeys: Oddiy ReplyKeyboardMarkup asosida

🏁 Ishga tushganda terminalda
🤖 Bot ishga tushdi...
👤 Yangi foydalanuvchi: @username (ID: 12345678) botni ishga tushirdi.


