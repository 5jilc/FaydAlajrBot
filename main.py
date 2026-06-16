import os
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

adhkar = [
"سبحان الله",
"الحمدلله",
"لا إله إلا الله",
"الله أكبر",
"أستغفر الله",
"سبحان الله وبحمده",
"سبحان الله العظيم"
]

def get_dhikr():
    return random.choice(adhkar)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📿 ذكر", callback_data="dhikr")],
        [InlineKeyboardButton("🤲 دعاء", callback_data="dua")]
    ]
    await update.message.reply_text(
        "أهلاً بك 🤍 اختر:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if q.data == "dhikr":
        await q.edit_message_text(get_dhikr())

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
