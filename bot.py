import sys
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import classify as classify


token="1798461535:AAHeZOMG3V_xhIxyJJL9WbYzDZgS6YDat54"


def start(bot, update):
    try:
        name = update.message.from_user.name
        message = "Hola " + name
        update.message.reply_text(message)
    except Exception as e:
        print("Error 003 {}".format(e.args[0]))

def help(bot, update):
    try:
        username = update.message.from_user.username
        update.message.reply_text('Hola {}, por favor envia una imagen para clasificarla'.format(username))
    except Exception as e:
        print("Error 004 {}".format(e.args[0]))

def analize (bot, update):
    try:
        message = "Recibiendo imagen"
        update.message.reply_text(message)
        print(message)

        photo_file = bot.getFile(update.message.photo[-1].file_id)
        id_user = update.message.from_user.id
        id_file = photo_file.file_id
        id_analisis = str(id_user) + "-" + str(id_file)

        filename = os.path.join('downloads/', '{}.jpg'.format(id_analisis))
        photo_file.download(filename)
        message = "Imagen recibida, analizando, por favor espera unos segundos"
        update.message.reply_text(message)
        print(message)

        resultado = classify.Classify.machineLearning(filename)
        print(resultado)
        update.message.reply_text(resultado)
        print("esperando otra imagen...")
    except Exception as e:
        print("Error 005 {}".format(e.args[0]))


def echo(bot, update):
    try:
        update.message.reply_text(update.message.text)
        print("Recibiendo texto...")
        print("esperando por otro texto...")
        print(update.message.from_user)
    except Exception as e:
        print("Error 006 {}".format(e.args[0]))

def error(bot, update, error):
    try:
        logger.warn('Update "%s" caused error "%s"' % (update, error))
    except Exception as e:
        print("Error 007 {}".format(e.args[0]))

def main():
    try:
        print('ClassifyImagesBot init token')

        updater = Updater(token)
        dp = updater.dispatcher

        print('ClassifyImagesBot init dispatcher')

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        dp.add_handler(MessageHandler(Filters.text, echo))
        dp.add_handler(MessageHandler(Filters.photo, analize))

        dp.add_error_handler(error)

        updater.start_polling()
        print('ClassifyImagesBot listo')
        updater.idle()
    except Exception as e:
        print("Error 008 {}".format(e.message))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Error 009: {}".format(e.args[0]))