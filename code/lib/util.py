from shutil import rmtree  # Remove foldes with files
from datetime import datetime  # Devuelve fecha y hora actual
import random  # Genera numeros
import string  # Lib genera textos
import os  # Lib para copiar archivos


class Util:
    @staticmethod
    def create_folder(path):  # crea una carpeta siempre en cuando no exista la carpeta
        try:  # Intenta crear la dirección
            os.makedirs(path)
            print("[CreateFolders] - Exito al crear la ruta: " + path)
        except:
            print("[CreateFolders] - La carpeta ya existe: " + path)

    @staticmethod
    def delete_folder(folder):
        try:
            rmtree(folder)
            print("[CreateFolders] Success remove folder and files: " + folder)
        except:
            print("[CreateFolders] Mistake while was remove folder and files" + folder)

    @staticmethod
    def delete_file(path):
        try:
            os.remove(path)
            print("[ScreenShot] Delete Sucess")
        except:
            print("[ScreenShot] There was a mistake while erasing file")

    @staticmethod
    def current_time():
        T = datetime.now()
        # Ejem: Saturday 19 de February 01 24 AM
        return T.strftime("%A") + " " + T.strftime("%d") + " de " + T.strftime("%B") + " " + T.strftime(
            "%I") + " " + T.strftime("%M") + " " + T.strftime("%p")

    @staticmethod
    def current_time_short():
        T = datetime.now()
        # Ejem: 19 Feb 01-33AM
        return T.strftime("%d") + " " + T.strftime("%b") + " " + T.strftime("%I") + "-" + T.strftime("%M") + "" + T.strftime("%p")

    @staticmethod
    def get_month():
        return datetime.now().strftime("%B")

    @staticmethod
    def random_char(number=4):  # Genera letras aleatorias [Longitud según el argumento]
        return ''.join(random.choice(string.ascii_letters) for x in range(number))

    @staticmethod
    def delete_cache(path):
        try:
            os.removedirs(path)
            try:
                os.remove(path)
            except:
                pass
        except:
            pass

    @staticmethod
    def split_string(n, st):
        lst = ['']
        for i in str(st):
            l = len(lst) - 1
            if len(lst[l]) < n:
                lst[l] += i
            else:
                lst += [i]
        return lst

    @staticmethod
    def last_command(command):
        # obtiene el texto que va luego del comando
        # /dir hola
        # return 'hola'
        split = command.split(' ')
        only_command = len(split[0])
        return command[only_command + 1:len(command)].strip()