from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "ТОКЕН_БОТА_ОТ_BOTFATHER"

# --- /start ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот-магазин.\nНапиши /shop, чтобы посмотреть товары.")

# --- /shop ---
async def shop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Товар A — 100₽", callback_data="item_a")],
        [InlineKeyboardButton("Товар B — 200₽", callback_data="item_b")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите товар:", reply_markup=reply_markup)

# --- обработка выбора ---
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "item_a":
        await query.edit_message_text("Вы выбрали Товар A. Спасибо за заказ!")
    elif query.data == "item_b":
        await query.edit_message_text("Вы выбрали Товар B. Спасибо за заказ!")

# --- запуск приложения ---
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shop", shop))
    app.add_handler(CallbackQueryHandler(button))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
