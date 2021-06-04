from interface import Interface
from functions import *
import tkinter

window = tkinter.Tk()

# empêche de pouvoir augmenter ou reduire la fenetre
window.resizable(width=False, height=False)

# essai de centrer la fenetre
geo = centerWindow(window)
window.geometry(geo)

window.title("Crypto")
window.iconbitmap("icon.ico")
window.config(bg='#4065A4')

interface = Interface(window)

interface.home()

window.mainloop()
