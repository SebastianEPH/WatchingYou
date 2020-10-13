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
# Frame
frame = Frame()
frame.pack(side="left", anchor="s" )#fill= "x")
frame.config(bg="red")
frame.config(width="520", height="320")
frame.config(bd=5)
frame.config()
#frame.config(relief="groove")
frame.config(relief="sunken")
#frame.config(cursor="hand2")    # Mano señalando
frame.config(cursor="pirate")    # Mano señalando
Label(frame, text="Registro de teclas a tiempo real:", bg="red", font=("Arial", 10), fg="white").place(x=510/3, y=5)

# Frame2
frame2 = Frame()
frame2.pack(side="right", anchor="s")#fill= "x")
frame2.config(bg="red")
frame2.config(width="520", height="320")
frame2.config(bd=5)
#frame2.config(relief="groove")
frame2.config(relief="sunken")
#frame2.config(cursor="hand2")    # Mano señalando
frame2.config(cursor="pirate")    # Mano señalando
Label(frame2, text="Administrador de Tareas", bg="red", font=("Arial", 10), fg="white").place(x=510/3, y=5)


# WebCam
imagen = PhotoImage(file= "monitor1.png" )
img_webcam = Label(raiz, image = imagen).place(x=510/3, y=5)

# title
Label(raiz,
      text="Anti Plagiarism 1.0",
      bg="black",
      font=("Arial", 15),
      fg="white").pack()

# Cuadro de control
background = "black"
color = "white"
font = "Arial"
x_ = 13
y_ = 20

# State
Label(raiz,text="ESTADO ACTUAL", bg="black", font=("Arial", 11), fg="white").place(x=x_, y = 60)
# State-Item
item1 = Label(raiz, text="- WebCam: No habilitado", bg=background, font=(font, 10), fg=color).place(x=x_ + 2, y=65 + y_)
item2 = Label(raiz, text="- Registrador de Teclas: Habilitado", bg=background, font=(font, 10), fg=color).place(x=x_ + 2, y=65 + (y_ * 2))
item3 = Label(raiz, text="- Metadata: Activado", bg=background, font=(font, 10), fg=color).place(x=x_ + 2, y=65 + (y_ * 3))
item4 = Label(raiz, text="- WebCam: No habilitado", bg=background, font=(font, 10), fg=color).place(x=x_ + 2, y=65 + +(y_ * 4))












raiz.mainloop()
