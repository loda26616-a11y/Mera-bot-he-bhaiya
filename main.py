import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

WELCOME_MSG = """
✨🔥 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐊𝐃 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐁𝐎𝐓 🔥✨

👋 𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐚𝐫 {name}

📢 𝐓𝐨 𝐠𝐞𝐭 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐀𝐏𝐊  
𝐉𝐨𝐢𝐧 𝐨𝐮𝐫 𝐕𝐈𝐏 𝐏𝐫𝐞𝐝𝐢𝐜𝐭𝐢𝐨𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥𝐬.

━━━━━━━━━━━━━━━

👨‍💻 𝐒𝐮𝐩𝐩𝐨𝐫𝐭  
👉 @KD_HACK_MANAGER
"""

CHANNEL1 = "https://t.me/+aoDlPRCfetFhYjBl"
CHANNEL2 = "https://t.me/+PWJj3BbQ0XRhNDk1"
CHANNEL3 = "https://t.me/+XLWGmVfslSQ2MTJl"

DM_LINK = "https://t.me/KD_HACK_MANAGER?text=HELLO%20BHAI%20MUJHE%20PREMIUM%20APK%20CHAHIYE"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    keyboard = [

        [InlineKeyboardButton("📢 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 1", url=CHANNEL1)],
        [InlineKeyboardButton("📢 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 2", url=CHANNEL2)],
        [InlineKeyboardButton("📢 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 3", url=CHANNEL3)],

        [InlineKeyboardButton("🔥📥 𝐆𝐄𝐓 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐀𝐏𝐊 🔓🔥", url=DM_LINK)]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        WELCOME_MSG.format(name=user.first_name),
        reply_markup=reply_markup
    )


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot Running...")

    app.run_polling()


if __name__ == "__main__":
    main()
