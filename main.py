import telebot
from telebot import types

name = ''
surname = ''
age = 0

bot = telebot.TeleBot('5654927191:AAFjk0m0BPTfXViNkK2rHJeahRVIYIJTBqM')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == '/hello':
        bot.send_message(message.from_user.id, 'Hello, my friend! What is your name?')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Say "/hello"')


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, f'Hi {name}! What is your surname?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, f'Greate {name} {surname}! How old are you?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Use numbers please!')

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='yes', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='no', callback_data='no')
    keyboard.add(key_no)
    question = f'{name} {surname}, {age}. Correct?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, "I'll remember you")
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, "It's impossible! Try again!")


bot.polling(none_stop=True, interval=0)
