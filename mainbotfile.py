import telebot
import songsearcher
import getpass
import get_admin
import Genius
import chekmat
import os
from pymongo import MongoClient


token = "691808572:AAGxVfNlK7EzwMHjxm0P0zY0s99pDat3wMY"
telebot.apihelper.proxy = {'https': 'socks5://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot(token)
pass_input = False

client = MongoClient('mongodb+srv://hhsl:As123456@mempedia-ptiit.mongodb.net/test?retryWrites=true&w=majority')
with client:
    db = client.mempedia
    nl = db.musicline
    queue = nl.queue


@bot.message_handler(commands=['me'])
def me(message):
    admins = open('admins.txt', 'r').read()

    if message.from_user.username in admins:
        file = open('god.txt', 'w')
        file.write(str(message.from_user.id))
        file.close()


@bot.message_handler(commands=['admin'])
def admin(message):
    global pass_input
    if get_admin.is_admin(message.chat.id):
        pass
    else:
        bot.send_message(message.chat.id, 'Введите пароль')
        pass_input = True


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global pass_input
    file = open('god.txt', 'r')
    god = int(file.read())
    mes = message.text.lower()
    if not(pass_input):
        if "/admin" in mes:
            if get_admin.is_admin(message.chat.id):
                pass
            else:
                bot.send_message(message.chat.id, 'Введите пароль')
                pass_input = True
        else:
            if "#music" in mes:
                mes = mes.replace("#music", "")
                c = mes.count(" - ")
                f = True
                if c:
                    if c > 1:
                        bot.send_message(message.chat.id, "Неверный формат ввода")
                        f = False
                    else:
                        musician, compose = mes.split(" - ")
                        musician, compose = musician.strip(), compose.strip()
                    if f:
                        data = Genius.find_out(musician, compose)
                        links = songsearcher.yandex(musician, compose)
                        if links:
                            bot.send_message(god, links)
                        else:
                            bot.send_message(message.chat.id, "Песня отсутствует на Яндекс.Музыке")
                        filename, duration, icon = songsearcher.vk(musician, compose)
                        if filename is not None:
                            bot.send_audio(god, audio=open(filename, 'rb'), performer=musician, title=compose, duration=duration)
                            os.remove(filename)
                        else:
                            bot.send_message(message.chat.id, "Песня отсутвует в Вконтакте")
                        if data == {}:
                            f = False
                        else:
                            f = True
                        queue.insert_one({'musician': musician, 'song': compose, "user": message.from_user.username,
                                          'istext': f})
                        if links is not None or filename is not None:
                            with client:
                                queue.insert_one({'musician': musician, 'song': compose, "user": message.from_user.username,'istext': data == {}})
                            if data != {}:
                                ismat = chekmat.CheckMat(data['text'])
                                if ismat:
                                    bot.send_message(god, "В песне есть мат")
                                else:
                                    bot.send_message(god, "В песне нет мата")
                            else:
                                bot.send_message(god, "Неизвестно, есть ли в песне мат")
                else:
                    bot.send_message(message.chat.id, "#music Введите исполнитель - композиция")
    else:
        if mes == getpass.return_pass():
            get_admin.add_admin(message.from_user.id, message.from_user.username)
        else:
            bot.send_message(message.from_user.id, "Неверный пароль")
        pass_input = False


bot.polling(none_stop=True)
