import telebot
from telebot import types
from fantasy_parser import get_books
from proza_parser import get_books1
from poema_parser import get_books2
from sbornic_parser import get_books3
from detectiv_parser import get_books4
from classica_parser import get_books5

token = 'ИСПОЛЬЗУЙТЕ ТОКЕН ВАШЕГО ТЕЛЕГРАМ БОТА И ВСТАВЬТЕ СЮДА'
bot = telebot.TeleBot(token=token, parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Добро пожаловать в раздел ХУДОЖЕСТВЕННАЯ ЛИТЕРАТУРА книжного магазина BookHouse.kg!')
    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    btn1 = types.KeyboardButton('Фантастика и фэнтези')
    btn2 = types.KeyboardButton('Проза')
    btn3 = types.KeyboardButton('Поэма')
    btn4 = types.KeyboardButton('Сборник')
    btn5 = types.KeyboardButton('Детективы, Триллеры')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(chat_id=message.chat.id, 
                     text='Выберите жанр книг',
                     reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Фантастика и фэнтези')
def handle_fantasy(message):
    books = get_books()
    for book in books:
        text = f'*{book["name"]}*\n' \
               f'Автор: {book["author_name"]}\n' \
               f'Цена: {book["price"]}\n' \
               f'[Изображение]({book["url_img"]})'
        bot.send_message(chat_id=message.chat.id, 
                         text=text, 
                         parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == 'Проза')
def handle_proza(message):
    books = get_books1()
    for book in books:
        text = f'*{book["name"]}*\n' \
               f'Автор: {book["author_name"]}\n' \
               f'Цена: {book["price"]}\n' \
               f'[Изображение]({book["url_img"]})'
        bot.send_message(chat_id=message.chat.id, 
                         text=text, 
                         parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == 'Поэма')
def handle_poema(message):
    books = get_books2()
    for book in books:
        text = f'*{book["name"]}*\n' \
               f'Автор: {book["author_name"]}\n' \
               f'Цена: {book["price"]}\n' \
               f'[Изображение]({book["url_img"]})'
        bot.send_message(chat_id=message.chat.id, 
                         text=text, 
                         parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == 'Сборник')
def handle_sbornic(message):
    books = get_books3()
    for book in books:
        text = f'*{book["name"]}*\n' \
               f'Автор: {book["author_name"]}\n' \
               f'Цена: {book["price"]}\n' \
               f'[Изображение]({book["url_img"]})'
        bot.send_message(chat_id=message.chat.id, 
                         text=text, 
                         parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == 'Детективы, Триллеры')
def handle_detectiv(message):
    books = get_books4()
    for book in books:
        text = f'*{book["name"]}*\n' \
               f'Автор: {book["author_name"]}\n' \
               f'Цена: {book["price"]}\n' \
               f'[Изображение]({book["url_img"]})'
        bot.send_message(chat_id=message.chat.id, 
                         text=text, 
                         parse_mode='Markdown')


bot.polling()