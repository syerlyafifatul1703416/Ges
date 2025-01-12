from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Saya bot Telegram Anda.")

app = ApplicationBuilder().token("TOKEN_API_ANDA").build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run_polling()
