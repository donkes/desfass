import telebot

bot = telebot.TeleBot("1661060770:AAGat9EmC-ubj7UmN7KAAajTjINDz7NKxhw", parse_mode=None)

@bot.message_handler(content_types = ['text'])
def send_welcome(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, "Howdy, how are you doing?")

bot.polling(none_stop = True, interval = 0)
