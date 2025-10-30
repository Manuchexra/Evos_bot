from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import start, main_menu_handler
from config import TOKEN

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, main_menu_handler))

    print("🤖 Bot ishga tushdi — 3 tilda (🇺🇿 / 🇷🇺 / 🇬🇧)")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
