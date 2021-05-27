####################################
#         => Crypto <=

# date de creation => 05/02/2021
# date dernier modif => 27/02/2021
# role: La base elle même du programme permet de faire appel à d'autre fonction ou methode

#         =>Par MISTIGRIX658<=

import tkinter
from interface import Interface

window = tkinter.Tk()

# personnalistaion de la fenetre
window.geometry("800x435")
# empêche de pouvoir augmenter ou reduire la fenetre
window.maxsize(width=800, height=435)
window.minsize(width=800, height=435)

window.title("Crypto")
window.iconbitmap("icon.ico")
window.config(bg='#4065A4')

interface = Interface(window)

interface.home()

window.mainloop()
