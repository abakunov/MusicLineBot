import telebot
token = "691808572:AAGxVfNlK7EzwMHjxm0P0zY0s99pDat3wMY"
telebot.apihelper.proxy = {'https': 'socks5://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Ну привет")
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Ботик для Валентина, напиши привет.")
    else:
        bot.send_message(message.chat.id, "Бро, напиши /help.")


bot.polling(none_stop=True, timeout=60)
