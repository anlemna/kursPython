import telebot
from telebot import types
import datetime
import sqlite3

bot = telebot.TeleBot('6734717056:AAFks9Mi0lTILW0CECZQlF_YDUwj3NTZk-4')



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton('Сегодня')
    markup.row(btn1)
    btn2=types.KeyboardButton('Завтра')
    btn3 = types.KeyboardButton('На неделю')
    markup.row(btn2, btn3)
    btn4 = types.KeyboardButton('Файл с полным расписанием')
    markup.row(btn4)
    bot.send_message(message.chat.id, 'Привет, всё таки решил сходить на пары?', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text=='Файл с полным расписанием':
        file = open('./FITKBos2023.xls', 'rb')
        bot.send_document(message.chat.id, file)
        bot.send_message(message.chat.id, 'Что, долгов уже понабрал и преподов ищешь?')
        bot.register_next_step_handler(message, on_click)

    elif message.text=='Сегодня':
        today = datetime.date.isoweekday(datetime.date.today())

        if today == 1:
            today_word = "Понедельник"
            bot.send_message(message.chat.id, today_word)
            db = sqlite3.connect('table.db')
            c = db.cursor()
            c.execute('SELECT * FROM monday')
            monday = c.fetchall()
            info = ''
            for el in monday:
                info +=f'{el[0]}\n {el[1]}\n\n'
            db.close()
            bot.send_message(message.chat.id, info)
            bot.register_next_step_handler(message, on_click)

        if today == 2:
            today_word = "Вторник"
            bot.send_message(message.chat.id, today_word)
            db = sqlite3.connect('table.db')
            c = db.cursor()
            c.execute('SELECT * FROM tuesday')
            monday = c.fetchall()
            info = ''
            for el in monday:
                info +=f'{el[0]}\n {el[1]}\n\n'
            db.close()
            bot.send_message(message.chat.id, info)
            bot.register_next_step_handler(message, on_click)

        if today == 3:
            today_word = "Среда"
            bot.send_message(message.chat.id, today_word)
            db = sqlite3.connect('table.db')
            c = db.cursor()
            c.execute('SELECT * FROM wednesday')
            monday = c.fetchall()
            info = ''
            for el in monday:
                info +=f'{el[0]}\n {el[1]}\n\n'
            db.close()
            bot.send_message(message.chat.id, info)
            bot.register_next_step_handler(message, on_click)

        if today == 4:
            today_word = "Четверг"
            bot.send_message(message.chat.id, today_word)
            db = sqlite3.connect('table.db')
            c = db.cursor()
            c.execute('SELECT * FROM thursday')
            monday = c.fetchall()
            info = ''
            for el in monday:
                info +=f'{el[0]}\n {el[1]}\n\n'
            db.close()
            bot.send_message(message.chat.id, info)
            bot.register_next_step_handler(message, on_click)

        if today == 5:
            today_word = "Пятница"
            bot.send_message(message.chat.id, today_word)
            db = sqlite3.connect('table.db')
            c = db.cursor()
            c.execute('SELECT * FROM friday')
            monday = c.fetchall()
            info = ''
            for el in monday:
                info +=f'{el[0]}\n {el[1]}\n\n'
            db.close()
            bot.send_message(message.chat.id, info)
            bot.register_next_step_handler(message, on_click)

        if today == 6:
            today_word = "Суббота"
            bot.send_message(message.chat.id, today_word)
            db = sqlite3.connect('table.db')
            c = db.cursor()
            c.execute('SELECT * FROM saturday')
            monday = c.fetchall()
            info = ''
            for el in monday:
                info +=f'{el[0]}\n {el[1]}\n\n'
            db.close()
            bot.send_message(message.chat.id, info)
            bot.register_next_step_handler(message, on_click)

        if today == 7:
            today_word = "Воскресенье"
            bot.send_message(message.chat.id, today_word)
            bot.send_message(message.chat.id, 'Выходной!')
            bot.register_next_step_handler(message, on_click)


    elif message.text=='Завтра':
        today = datetime.date.isoweekday(datetime.date.today())
        tomorrow = today + 1

        if tomorrow == 2:
            today_word = "Вторник"
            bot.send_message(message.chat.id, today_word)
            db = sqlite3.connect('table.db')
            c = db.cursor()
            c.execute('SELECT * FROM tuesday')
            monday = c.fetchall()
            info = ''
            for el in monday:
                info +=f'{el[0]}\n {el[1]}\n\n'
            db.close()
            bot.send_message(message.chat.id, info)
            bot.register_next_step_handler(message, on_click)

        if tomorrow == 3:
            today_word = "Среда"
            bot.send_message(message.chat.id, today_word)
            db = sqlite3.connect('table.db')
            c = db.cursor()
            c.execute('SELECT * FROM wednesday')
            monday = c.fetchall()
            info = ''
            for el in monday:
                info +=f'{el[0]}\n {el[1]}\n\n'
            db.close()
            bot.send_message(message.chat.id, info)
            bot.register_next_step_handler(message, on_click)

        if tomorrow == 4:
            today_word = "Четверг"
            bot.send_message(message.chat.id, today_word)
            db = sqlite3.connect('table.db')
            c = db.cursor()
            c.execute('SELECT * FROM thursday')
            monday = c.fetchall()
            info = ''
            for el in monday:
                info +=f'{el[0]}\n {el[1]}\n\n'
            db.close()
            bot.send_message(message.chat.id, info)
            bot.register_next_step_handler(message, on_click)

        if tomorrow == 5:
            today_word = "Пятница"
            bot.send_message(message.chat.id, today_word)
            db = sqlite3.connect('table.db')
            c = db.cursor()
            c.execute('SELECT * FROM friday')
            monday = c.fetchall()
            info = ''
            for el in monday:
                info +=f'{el[0]}\n {el[1]}\n\n'
            db.close()
            bot.send_message(message.chat.id, info)
            bot.register_next_step_handler(message, on_click)

        if tomorrow == 6:
            today_word = "Суббота"
            bot.send_message(message.chat.id, today_word)
            db = sqlite3.connect('table.db')
            c = db.cursor()
            c.execute('SELECT * FROM saturday')
            monday = c.fetchall()
            info = ''
            for el in monday:
                info +=f'{el[0]}\n {el[1]}\n\n'
            db.close()
            bot.send_message(message.chat.id, info)
            bot.register_next_step_handler(message, on_click)

        if tomorrow == 7:
            today_word = "Воскресенье"
            bot.send_message(message.chat.id, today_word)
            bot.send_message(message.chat.id, 'Выходной!')
            bot.register_next_step_handler(message, on_click)

        if tomorrow == 8:
            today_word = "Понедельник"
            bot.send_message(message.chat.id, today_word)
            db = sqlite3.connect('table.db')
            c = db.cursor()
            c.execute('SELECT * FROM monday')
            monday = c.fetchall()
            info = ''
            for el in monday:
                info +=f'{el[0]}\n {el[1]}\n\n'
            db.close()
            bot.send_message(message.chat.id, info)
            bot.register_next_step_handler(message, on_click)


    elif message.text=='На неделю':
        bot.send_message(message.chat.id, 'Итак, узнаем, сколько дней ты будешь учиться...')

        bot.send_message(message.chat.id, 'Понедельник')
        db = sqlite3.connect('table.db')
        c = db.cursor()
        c.execute('SELECT * FROM monday')
        monday = c.fetchall()
        info = ''
        for el in monday:
            info += f'{el[0]}\n {el[1]}\n\n'
        db.close()
        bot.send_message(message.chat.id, info)

        bot.send_message(message.chat.id, 'Вторник')
        db = sqlite3.connect('table.db')
        c = db.cursor()
        c.execute('SELECT * FROM tuesday')
        monday = c.fetchall()
        info = ''
        for el in monday:
            info += f'{el[0]}\n {el[1]}\n\n'
        db.close()
        bot.send_message(message.chat.id, info)

        bot.send_message(message.chat.id, 'Среда')
        db = sqlite3.connect('table.db')
        c = db.cursor()
        c.execute('SELECT * FROM wednesday')
        monday = c.fetchall()
        info = ''
        for el in monday:
            info += f'{el[0]}\n {el[1]}\n\n'
        db.close()
        bot.send_message(message.chat.id, info)

        bot.send_message(message.chat.id, 'Четверг')
        db = sqlite3.connect('table.db')
        c = db.cursor()
        c.execute('SELECT * FROM thursday')
        monday = c.fetchall()
        info = ''
        for el in monday:
            info += f'{el[0]}\n {el[1]}\n\n'
        db.close()
        bot.send_message(message.chat.id, info)

        bot.send_message(message.chat.id, 'Пятница')
        db = sqlite3.connect('table.db')
        c = db.cursor()
        c.execute('SELECT * FROM friday')
        monday = c.fetchall()
        info = ''
        for el in monday:
            info += f'{el[0]}\n {el[1]}\n\n'
        db.close()
        bot.send_message(message.chat.id, info)

        bot.send_message(message.chat.id, 'Суббота')
        db = sqlite3.connect('table.db')
        c = db.cursor()
        c.execute('SELECT * FROM saturday')
        monday = c.fetchall()
        info = ''
        for el in monday:
            info += f'{el[0]}\n {el[1]}\n\n'
        db.close()
        bot.send_message(message.chat.id, info)

        bot.register_next_step_handler(message, on_click)

    else:
        bot.send_message(message.chat.id, 'Я не понимаю тебя! Нажми на одну из кнопок ниже')
        bot.register_next_step_handler(message, on_click)
        
bot.polling(none_stop=True)