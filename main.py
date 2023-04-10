import telebot
from telebot import types
from philosophers import Philisophers

bot = telebot.TeleBot('5458668855:AAGWvtUKH999Mr9DwNwZaKNqBb3jw6xmTbQ')


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnSite = types.KeyboardButton('Что может бот?')
    markup.row(btnSite)
    btn1 = types.KeyboardButton('Материалисты')
    btn2 = types.KeyboardButton('Идеалисты')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, 'Привет! Чтобы работать с ботом, необходимо нажимать кнопки,'
                                      ' расположенные под клавиатурой.',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Что может бот?":
        bot.send_message(message.chat.id, 'Данный бот может поведать пользователю о взглядах и трудах восьми выдающихся'
                                          ' философов Древней Греции.\n'
                                          'Помимо этого он может рассказать биографию выбранного философа (подробность '
                                          'излагаемой информации может колебаться в зависимости от доступной на '
                                          'сегодняшний день информации).')
    elif message.text == "Материалисты" or message.text == "К материалистам":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btnBack = types.KeyboardButton('Вернуться в главное меню')
        btn1 = types.KeyboardButton('Гераклит')
        btn2 = types.KeyboardButton('Демокрит')
        btn3 = types.KeyboardButton('Эпикур')
        btn4 = types.KeyboardButton('Фалес')
        markup.row(btnBack)
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Перехожу к материалистам...', reply_markup=markup)
    elif message.text == "Идеалисты" or message.text == "К идеалистам":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btnBack = types.KeyboardButton('Вернуться в главное меню')
        btn1 = types.KeyboardButton('Пифагор')
        btn2 = types.KeyboardButton('Сократ')
        btn3 = types.KeyboardButton('Платон')
        btn4 = types.KeyboardButton('Аристотель')
        markup.row(btnBack)
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Перехожу к идеалистам...', reply_markup=markup)
    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnSite = types.KeyboardButton('Что может бот?')
        markup.row(btnSite)
        btn1 = types.KeyboardButton('Материалисты')
        btn2 = types.KeyboardButton('Идеалисты')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Возвращаюсь в начало...', reply_markup=markup)
    elif message.text == "Гераклит":
        file = open('./geraklit.png', 'rb')
        Philisophers.philosopher = "Geraklit"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnBack = types.KeyboardButton("К материалистам")
        btnBio = types.KeyboardButton("Биография")
        bot.send_photo(message.chat.id, file)
        markup.row(btnBack)
        markup.row(btnBio)
        bot.send_message(message.chat.id, Philisophers.GERAKLIT_VIEWS + Philisophers.GERAKLIT_WORKS,
                         reply_markup=markup)
    elif message.text == "Демокрит":
        file = open('./274px-Democritus2.jpg', 'rb')
        Philisophers.philosopher = "Demokrit"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnBack = types.KeyboardButton("К материалистам")
        btnBio = types.KeyboardButton("Биография")
        bot.send_photo(message.chat.id, file)
        markup.row(btnBack)
        markup.row(btnBio)
        bot.send_message(message.chat.id, Philisophers.DEMOKRIT_VIEWS + Philisophers.DEMOKRIT_WORKS,
                         reply_markup=markup)
    elif message.text == "Эпикур":
        file = open('./Epikur.jpg', 'rb')
        Philisophers.philosopher = "Epikur"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnBack = types.KeyboardButton("К материалистам")
        btnBio = types.KeyboardButton("Биография")
        bot.send_photo(message.chat.id, file)
        markup.row(btnBack)
        markup.row(btnBio)
        bot.send_message(message.chat.id, Philisophers.EPIKUR_VIEWS + Philisophers.EPIKUR_WORKS,
                         reply_markup=markup)
    elif message.text == "Фалес":
        file = open('./Fales.jpg', 'rb')
        Philisophers.philosopher = "Fales"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnBack = types.KeyboardButton("К материалистам")
        btnBio = types.KeyboardButton("Биография")
        bot.send_photo(message.chat.id, file)
        markup.row(btnBack)
        markup.row(btnBio)
        bot.send_message(message.chat.id, Philisophers.FALES_VIEWS + Philisophers.FALES_WORKS,
                         reply_markup=markup)
    elif message.text == "Пифагор":
        file = open('./Pifagor.jpg', 'rb')
        Philisophers.philosopher = "Pifagor"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnBack = types.KeyboardButton("К идеалистам")
        btnBio = types.KeyboardButton("Биография")
        bot.send_photo(message.chat.id, file)
        markup.row(btnBack)
        markup.row(btnBio)
        bot.send_message(message.chat.id, Philisophers.PIFAGOR_VIEWS + Philisophers.PIFAGOR_WORKS,
                         reply_markup=markup)
    elif message.text == "Сократ":
        file = open('./Socrates.jpg', 'rb')
        Philisophers.philosopher = "Socrates"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnBack = types.KeyboardButton("К идеалистам")
        btnBio = types.KeyboardButton("Биография")
        bot.send_photo(message.chat.id, file)
        markup.row(btnBack)
        markup.row(btnBio)
        bot.send_message(message.chat.id, Philisophers.SOCRATES_VIEWS + Philisophers.SOCRATES_WORKS,
                         reply_markup=markup)
    elif message.text == "Платон":
        file = open('./Plato.jpg', 'rb')
        Philisophers.philosopher = "Plato"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnBack = types.KeyboardButton("К идеалистам")
        btnBio = types.KeyboardButton("Биография")
        bot.send_photo(message.chat.id, file)
        markup.row(btnBack)
        markup.row(btnBio)
        bot.send_message(message.chat.id, Philisophers.PLATO_VIEWS + Philisophers.PLATO_WORKS,
                         reply_markup=markup)
    elif message.text == "Аристотель":
        file = open('./Aristotle.jpg', 'rb')
        Philisophers.philosopher = "Aristotle"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnBack = types.KeyboardButton("К идеалистам")
        btnBio = types.KeyboardButton("Биография")
        bot.send_photo(message.chat.id, file)
        markup.row(btnBack)
        markup.row(btnBio)
        bot.send_message(message.chat.id, Philisophers.ARISTOTLE_VIEWS + Philisophers.ARISTOTLE_WORKS,
                         reply_markup=markup)
    elif message.text == "Биография":
        if Philisophers.philosopher == "Geraklit":
            bot.send_message(message.chat.id, Philisophers.GERAKLIT_BIO)
        elif Philisophers.philosopher == "Demokrit":
            bot.send_message(message.chat.id, Philisophers.DEMOKRIT_BIO)
        elif Philisophers.philosopher == "Epikur":
            bot.send_message(message.chat.id, Philisophers.EPIKUR_BIO)
        elif Philisophers.philosopher == "Fales":
            bot.send_message(message.chat.id, Philisophers.FALES_BIO)
        elif Philisophers.philosopher == "Pifagor":
            bot.send_message(message.chat.id, Philisophers.PIFAGOR_BIO)
        elif Philisophers.philosopher == "Socrates":
            bot.send_message(message.chat.id, Philisophers.SOCRATES_BIO)
        elif Philisophers.philosopher == "Plato":
            bot.send_message(message.chat.id, Philisophers.PLATO_BIO)
        elif Philisophers.philosopher == "Aristotle":
            bot.send_message(message.chat.id, Philisophers.ARISTOTLE_BIOp1)
            bot.send_message(message.chat.id, Philisophers.ARISTOTLE_BIOp2)


bot.polling(none_stop=True)
