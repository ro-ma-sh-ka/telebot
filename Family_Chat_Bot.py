from datetime import datetime
import telebot
from work_with_db import save_new_member, family_list
from telebot import types

name = ''
surname = ''
birthday = 0

bot_commands = {
    "/help": "list of commands",
    "/hello": "new member introduction",
    "/who_is_there": "list of members",
    "/weather": "weather forcast"
}

bot = telebot.TeleBot('5333274566:AAHtr0A9EhJO9wGcBTbGbN1uzacEb33B0us')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    """the function receives a text message and manage it according to the list of commands"""
    if message.text == '/hello':
        bot.send_message(message.chat.id, "Hello, my friend! I'm your FamilyBot. What is your name?")
        bot.register_next_step_handler(message, get_name)
    elif message.text == "/who_is_there":
        bot.send_message(message.chat.id, "Who we are:")
        result = family_list()
        for row in result:
            bot.send_message(message.chat.id, f"{row[0]}, {row[1]}, {row[2]}")
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'I can:')
        for key, value in bot_commands.items():
            bot.send_message(message.chat.id, f"{key}: {value}")
    elif message.text == '/weather':
        bot.send_message(message.chat.id, "https://rp5.ru/")


def get_name(message):
    """the function receives a name and launches get_surname function"""
    global name
    name = message.text
    bot.send_message(message.chat.id, f'Hi {name}! What is your surname?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    """the function receives surname and launches get_birthday function"""
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, f"Hi {name} {surname}! Nice to meet you. When's your birthday (dd.mm.YYYY)?")
    bot.register_next_step_handler(message, get_birthday)


def get_birthday(message):
    """the function receives birthday and launches keyboard to confirm the data of user"""
    global birthday
    birthday = message.text
    # while birthday == 0:
    #     try:
    #         birthday = int(message.text)
    #     except Exception:
    #         bot.send_message(message.chat.id, 'Use numbers please!')

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='yes', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='no', callback_data='no')
    keyboard.add(key_no)
    question = f'{name} {surname}, {birthday}. Correct?'
    bot.send_message(message.chat.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    """
    the function work on user click with
    yes - save new member
    no - ask to repeat
    """
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, "I'll remember you")
        save_new_member(name, surname, birthday, datetime.now())
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, "It's impossible! Say '/hello' again and introduce yourself!")
