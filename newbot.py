from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ваш токен бота
TOKEN = '7426050288:AAHPrFBaNlMDSNiOYfp2V2cYT2caMg_Wj1U'
# URL вашего WebApp
WEB_APP_URL = 'https://coin-dusky-psi.vercel.app/'

async def send_welcome_message(update: Update, username: str) -> None:
    message = (
        f'Welcome, @{username}! 🎉 Start your journey with us and enjoy <b>daily gifts</b>! '
        'Tap daily to collect coin prizes, which will be added directly to your. 🚀'
    )
    await update.message.reply_text(message, parse_mode='HTML')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Получаем username пользователя
    username = update.effective_user.username or update.effective_user.first_name  # Используем username, если он есть, иначе - имя
    
    # Отправляем приветственное сообщение
    await send_welcome_message(update, username)
    
    # Создаем кнопку с правильным форматом
    keyboard = [[InlineKeyboardButton("Lets go ☀️", web_app={"url": WEB_APP_URL})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправляем сообщение с кнопкой
    await update.message.reply_text('Select an action:', reply_markup=reply_markup)

def main() -> None:
    # Создаем приложение и передаем ему токен вашего бота
    application = ApplicationBuilder().token(TOKEN).build()

    # Регистрация обработчика команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
