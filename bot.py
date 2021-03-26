import sys
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import json


token="1798461535:AAHeZOMG3V_xhIxyJJL9WbYzDZgS6YDat54"


def start(bot, update):
    try:
        username=update.message.from_user.name
        message="Bienvenido "+ username
        messages="Este es un bot identificador de billetes "  
        update.message.reply_text(message)
        update.message.reply_text(messages)
            
    except Exception as error:
        print("Error 001 {}".format(error.args[0]))

def echo(bot, update):
    try:
        text=update.message.text
        update.message.reply_text(text)
    except Exception as error:
        print("Error 002 {}".format(error.args[0]))

def help(bot, update):
    try:
        message="Puedes enviar imagenes a este bot para reconocer el valor de tu billete"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 003 {}".format(error.args[0]))

def error(bot, update, error):
    try:
        print(error)
    except Exception as e:
        print("Error 004 {}".format(e.args[0]))

def getImagen(bot, update):
    try:
        message="Enviando imagen..."
        update.message.reply_text(message)

        file= bot.getFile(update.message.photo[-1].file_id)
        id=file.file_id
        filename= os.path.join("downloads/","{}.jpg".format(id))
        file.download(filename)
        message="Imagen enviada"
        update.message.reply_text(message)
        message="Reconociendo billete..."
        update.message.reply_text(message)                   
        imagenfile={"myfile":open(filename,'rb')}
        resultado = requests.post("https://8080-chocolate-goldfish-r32akb8f.ws-us03.gitpod.io/imagen", files=imagenfile)
        update.message.reply_text(resultado.text)
        
    except Exception as error:
        print("Error 005 {}".format(e.args[0]))
    

def identificar(bot,filename):
    try:
        message="Identificando..."
        update.message.reply_text(message)       
        imagenes= {'myfile':filename}
        
        resultado = requests.post("https://8080-chocolate-goldfish-r32akb8f.ws-us03.gitpod.io/imagen", myfile=imagenes)
        billete=resultado.json()
        items=billete[list(billete.keys())[0]]
        for i in items:
            descripcion= i["Respuesta"]
        message=descripcion
        update.message.reply_text(message)
    except Exception as error:
        print("Error 0 {}".format(e.args[0]))
        
def main():
    try:
        updater=Updater(token)
        dp=updater.dispatcher
        
        dp.add_handler(CommandHandler("start",start))
        dp.add_handler(CommandHandler("help",help))
        dp.add_handler(MessageHandler(Filters.text, echo))
        dp.add_handler(MessageHandler(Filters.photo, getImagen))
        dp.add_error_handler(error)
       
        updater.start_polling()
        
        updater.idle()
        print("Bot listo")
    except Exception as e:
        print("Error 010 {}".format(e.args[0]))

if __name__=="__main__":
    try:
        main()
    except Exception as error:
        print("Error 011 {}".format(e.args[0]))