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
nl = client.musicline
queue = nl.queue


@bot.message_handler(commands=['line'])
def line(message):
    line = list(queue.find())
    if len(line) > 9:
        line = line[-10:]
    for i in range(len(line)):
        p = line[i]

        if p['user'] != None:
            bot.send_message(message.from_user.id, (f'<a href="tg://user?id={p["user"]}">{p["firstname"]}</a>' + ': ' + str(i + 1) + '. ' + p['musician'] + ' -' + p['song']), parse_mode="HTML")
        else:
            bot.send_message(message.from_user.id, ('Someone ' + str(i + 1) + '. ' + p['musician'] +' -' + p['song']))


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
                        if data == {}:
                            author = musician
                            song = compose
                        else:
                            author = data['artist']
                            song = data['song']
                        links = songsearcher.yandex(author, song)
                        if links:
                            bot.send_message(god, links)
                        else:
                            bot.send_message(message.chat.id, "Песня отсутствует на Яндекс.Музыке😔")
                        filename, duration, icon = songsearcher.vk(author, song)
                        if filename is not None:
                            bot.send_audio(god, audio=open(filename, 'rb'), performer=author, title=song, duration=duration)
                            os.remove(filename)
                        else:
                            bot.send_message(message.chat.id, "Песня отсутвует в Вконтакте🤔")
                        if links is not None or filename is not None:
                            queue.insert_one({'musician': author, 'song': song, "user": message.from_user.id, 'firstname': message.from_user.first_name + ' ' + message.from_user.last_name,
                                              'url': data['url'] if 'url' in data else None})
                            if data != {}:
                                bot.send_message(god, data['url'])
                                ismat = chekmat.CheckMat(data['text'])
                                if ismat:
                                    bot.send_message(god, "В песне есть мат😡")
                                else:
                                    bot.send_message(god, "В песне нет мата🤗")
                            else:
                                bot.send_message(god, "Неизвестно, есть ли в песне мат🤔")
                else:
                    bot.send_message(message.chat.id, "#music Введите исполнитель - композиция")
    else:
        if mes == getpass.return_pass():
            get_admin.add_admin(message.from_user.id, message.from_user.username)
        else:
            bot.send_message(message.from_user.id, "Неверный пароль")
        pass_input = False


bot.polling(none_stop=True)
