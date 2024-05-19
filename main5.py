import requests
from bs4 import BeautifulSoup
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Ваш токен телеграм-бота
TOKEN = '6498617644:AAFi_8scmYXMfAY2a_onMR_jJ3Kgo0iMpOw'

# Функция для получения данных о книгах с сайта
def get_book_data():
    url = "https://bookhouse.kg/kg/catalog/2/39/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find_all('div', class_='book-inner uk-card uk-card-default uk-card-hover book_inner_padding uk-margin')

    books = []
    for item in data:
        name = item.find('div', class_="uk-width-1-1 uk-padding-top-10").text.strip()
        price = item.find('span').text
        url_img = "https://bookhouse.kg" + item.find("img").get("src")
        books.append({
            'name': name,
            'price': price,
            'image_url': url_img
        })

    return books

# Команда для показа книг
async def show_books(update: Update, context: ContextTypes.DEFAULT_TYPE):
    book_data = get_book_data()
    if book_data:
        for book in book_data:
            message = f"Название: {book['name']}\nЦена: {book['price']}\nИзображение: {book['image_url']}"
            await update.message.reply_text(message)
    else:
        await update.message.reply_text("Не удалось получить данные о книгах.")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['Фантастика и фэнтези']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        'Добро пожаловать в книжный магазин BookHouse.kg! Нажмите на кнопку, для просмотра книг раздела Фантастика и фэнтези.',
        reply_markup=reply_markup
    )

# Обработчик нажатия на кнопку
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == 'Фантастика и фэнтези':
        await show_books(update, context)

# Основная функция для настройки и запуска бота
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button_handler))

    app.run_polling()

if __name__ == '__main__':
    main()