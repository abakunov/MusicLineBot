import telebot
token = "691808572:AAGxVfNlK7EzwMHjxm0P0zY0s99pDat3wMY"
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.form_user.id, "Ну привет")
    elif message.text == "/help":
        bot.send_message(message.form_user, "Ботик для Валентина, напиши привет.")
    else:
        bot.send_message(message.from_user.id, "Бро, напиши /help.")


bot.polling(none_stop=True, interval=0)