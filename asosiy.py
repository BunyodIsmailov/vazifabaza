import telebot
from transliterate import to_cyrillic,to_latin



TOKEN = "Your token"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum,Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda  message:True)
def echo_all(message):
    msg = message.text

    if msg==to_latin(msg):
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    #javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob)


bot.polling()

