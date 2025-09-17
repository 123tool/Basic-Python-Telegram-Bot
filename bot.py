from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Halo {update.effective_user.first_name}, saya adalah bot Telegram kamu!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Perintah yang tersedia: /start, /help")

app.add_handler(CommandHandler("help", help_command))
if __name__ == '__main__':
    app = ApplicationBuilder().token("YOUR_API_TOKEN_HERE").build()
    app.add_handler(CommandHandler("start", start))
    print("Bot sedang berjalan...")
    app.run_polling()
