import telebot
import songsearcher

token = "691808572:AAGxVfNlK7EzwMHjxm0P0zY0s99pDat3wMY"
telebot.apihelper.proxy = {'https': 'socks5://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    mes = message.text.lower()
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
                bot.send_audio(message.chat.id, audio=open(songsearcher.vk(musician, compose), 'rb'))

        else:
            bot.send_message(message.chat.id, "#music Введите исполнитель - композиция")


bot.polling(none_stop=True, timeout=60)
