import os
import shutil


class ExplorerFiles:
    @staticmethod
    def list_dir(path):
        final = ''
        try:
            for file in os.listdir(path) : # u or b
                final = final + '=> '+file+' \n'
        except:
            final = 'Hubo un error, Quizas La ruta no existe'

        return final

    @staticmethod
    def create_folder(path):
        os.makedirs(path)

    @staticmethod
    def remove_folder(path):
        shutil.rmtree(path)

    @staticmethod
    def remove_file(path):
        os.remove(path)

    @staticmethod
    def move(path1, path2):
        shutil.move(path1, path2)

    @staticmethod
    def exist(path):
        return os.path.exists(path)

    @staticmethod
    def is_file(path):
        return os.path.isfile(path)