import telebot
import songsearcher
import getpass
import get_admin

token = "691808572:AAGxVfNlK7EzwMHjxm0P0zY0s99pDat3wMY"
telebot.apihelper.proxy = {'https': 'socks5://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot(token)
pass_input = False


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
                        bot.send_message(message.chat.id, "Исполнитель - "+musician)
                        bot.send_message(message.chat.id, "Композиция - "+compose)
                        links = songsearcher.yandex(musician, compose)
                        for link in links:
                            bot.send_message(message.chat.id, link)
                        filename, duration, icon = songsearcher.vk(musician, compose)
                        bot.send_audio(message.chat.id, audio=open(filename, 'rb'), performer=musician, title=compose, duration=duration)

                else:
                    bot.send_message(message.chat.id, "#music Введите исполнитель - композиция")
    else:
        if mes == getpass.return_pass():
            get_admin.add_admin(message.chat.id, message.chat.username)
        else:
            bot.send_message(message.chat.id, "Неверный пароль")
        pass_input = False


bot.polling(none_stop=True)
