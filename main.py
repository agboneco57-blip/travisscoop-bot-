import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bienvenue sur TRAVISCOOP !\n\nCommandes :\n/bomba - Bombe du jour\n/safe - Safe du jour\n/vip - Infos VIP")

async def bomba(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💣 BOMBA DU JOUR TRAVISCOOP\n\nBientôt disponible. Reste branché !")

async def safe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ SAFE DU JOUR TRAVISCOOP\n\nBientôt disponible. Reste branché !")

async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👑 VIP TRAVISCOOP\n\nPour le VIP, contacte @Traviiscoop")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bomba", bomba))
    app.add_handler(CommandHandler("safe", safe))
    app.add_handler(CommandHandler("vip", vip))
    print("Bot lancé...")
    app.run_polling()
