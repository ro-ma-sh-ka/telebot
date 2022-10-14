import telebot
from work_with_db import save_new_member, family_list
from telebot import types

name = ''
surname = ''
age = 0

bot_commands = {
    "/help": "list of commands",
    "/hello": "new member introduction",
    "/who_is_there": "list of members",
    "/weather": "weather forcast"
}

bot = telebot.TeleBot('5333274566:AAHtr0A9EhJO9wGcBTbGbN1uzacEb33B0us')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == '/hello':
        bot.send_message(message.from_user.id, "Hello, my friend! I'm your FamilyBot. What is your name?")
        bot.register_next_step_handler(message, get_name)
    elif message.text == "/who_is_there":
        bot.send_message(message.from_user.id, "Who we are:")
        result = family_list()
        for row in result:
            bot.send_message(message.from_user.id, f"{row[0]}, {row[1]}, {row[2]}")
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'I can:')
        for key, value in bot_commands.items():
            bot.send_message(message.from_user.id, f"{key}: {value}")
    elif message.text == '/weather':
        bot.send_message(message.from_user.id, "https://rp5.ru/")
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
    bot.send_message(message.from_user.id, f"Hi {name} {surname}! Nice to meet you. When's your birthday?")
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
        save_new_member(name, age)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, "It's impossible! Say '/hello' again and introduce yourself!")