from tkinter import *

class Config:
    def __init__(self):
        pass
    class Interface:
        def __init__(self):
            self.Title_SOFT = "AntiPlagiarism 1.0"
            self.PATH_ICON = "icon.ico"
            self.Resolution = "1270x720"
            self.BackGround = "black"


config = Config()
interface = config.Interface()



raiz = Tk()
raiz.title(interface.Title_SOFT)
raiz.focus()
raiz.resizable(False, False)
raiz.iconbitmap(interface.PATH_ICON)
raiz.geometry(interface.Resolution)
raiz.config(bg = interface.BackGround)
raiz.mainloop()
