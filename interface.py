####################################
#         => Crypto <=

# nom du fichier => interface.py

# date de creation => 05/02/2021
# date dernier modif => 26/05/2021
# role: Contient la classe Interface et les differentes methodes en reference avec l'interface

#  =>Par MISTIGRIX658<=

import tkinter
import pickle
from tkinter import filedialog
from functools import partial
from cryptage import *
from tkinter import messagebox
from functions import *
from constantes import *

# definition de la classe
class Interface:

    def __init__(self, window):

        self.window = window

    def loadScreen(self):
        self.window.mainloop()

    def home(self):
        """Acceuil du programme permettant d'aller d'une session à une autre"""
        self.interfaceClean()
        img = tkinter.PhotoImage(file='image_acceuil.gif')

        canvas = tkinter.Canvas(self.window, width=1000, height=544)
        canvas.place(x=0, y=0)

        canvas.create_image(0, 0, anchor='nw', image=img)

        #label = tkinter.Label(self.window, text="Bienvenue sur Crypto", font=("Courrier", 20), bg='black', fg='white')
        #label.pack()

        frame = tkinter.Frame()
        frame_button_message = tkinter.Frame()
        frame_button_file = tkinter.Frame()

        # boutons en rapport avec le cryptage et le decryptage de message
        button_crypt_mess = tkinter.Button(self.window, text='Cryptage de Message', bg='blue', fg='white', command=self.interfaceCryptage, width=width_button, height=height_button, font=font_default)
        button_crypt_mess.place(x=200, y=150)
        button_decrypt_mess = tkinter.Button(self.window, text='Decryptage de Message', bg='blue', fg='white', command=self.interfaceDecryptage, width=width_button, height=height_button, font=font_default)
        button_decrypt_mess.place(x=200, y=230)

        # boutons en rapport avec le cryptage et decryptage de fichier
        button_crypt_file = tkinter.Button(self.window, text='Cryptage de Fichier', bg='blue', fg='white',command=self.interfaceCryptFile, width=width_button, height=height_button,font=font_default)
        button_crypt_file.place(x=400, y=150)
        button_decrypt_file = tkinter.Button(self.window, text='Decryptage de Fichier', bg='blue', fg='white', command=self.interfaceDecryptFile, width=width_button, height=height_button, font=font_default)
        button_decrypt_file.place(x=400, y=230)


        bouton_quitte = tkinter.Button(self.window, text='Quitter', bg='blue', fg='white', command=self.window.destroy, width=10, height=2, font=font_default)
        bouton_quitte.place(x=690, y=370)

        label_version = tkinter.Label(self.window, text=f"by MISTIGRIX version {program_version}", font=('Courrier', 8))
        label_version.place(x=5, y=410)

        self.loadScreen()


    # on definit une methode pour nettoyé la fenetre
    def interfaceClean(self):
        """permet de supprimer tous ce qui a été creer à l'ecran"""
        for c in self.window.winfo_children():
            c.destroy()

    # definir une methode pour affiche une bar de menu
    def bar(self):

        menu_bar = tkinter.Menu(self.window)

        menu_bar.add_cascade(label='Acceuil', command=self.home)

        # creation d'un premier menu

        menu_message = tkinter.Menu(menu_bar, tearoff=0)
        menu_message.add_command(label="Crypter", command=self.interfaceCryptage)  # ajout de la commande
        menu_message.add_command(label="Decrypter", command=self.interfaceDecryptage)  # ajout de la commande
        menu_bar.add_cascade(label='Message', menu=menu_message)

        menu_fichier = tkinter.Menu(menu_bar, tearoff=0)
        menu_fichier.add_command(label='Crypter', command=self.interfaceCryptFile)
        menu_fichier.add_command(label='Decrypter', command=self.interfaceDecryptFile)
        menu_bar.add_cascade(label='Fichier', menu=menu_fichier)

        menu_bar.add_cascade(label='Quitter', command=self.window.destroy)

        self.window.config(menu=menu_bar)


    # methode pour creer l'image
    
    #definition de l'interface de cryptage
    def interfaceCryptage(self):
        self.interfaceClean()

        self.window.config(bg='#4065A4')

        self.bar()

        label_title = tkinter.Label(self.window, text="SESSION DE CRYPTAGE", font=('Helvetica', 20), bg='#4065A4', fg='white')
        label_title.pack()

        # creation des champs

        # on met le premier champs et son label dans un premier frame
        label_mess = tkinter.Label(self.window, text='Entrer le message ici:', font=('Courrier', 15), bg='#4065A4', fg='white')
        label_mess.place(x=2, y=100)

        self.insert_mess = tkinter.Entry(self.window, bg='#4065A4', font=('Helvetica', 20), fg='white', width=30)
        self.insert_mess.place(x=300, y=100)

        # on met le second champs dans un second frame
        label_clef = tkinter.Label(self.window, text="Entrer la clé de chiffrement ici:", font=('Courrier', 15), bg='#4065A4',fg='white')
        label_clef.place(x=2, y=150)

        self.insert_clef = tkinter.Entry(self.window, bg='#4065A4', font=('Helvetica', 20), fg='white', width=30)
        self.insert_clef.place(x=300, y=150)

        # le bouton de commande pour pouvoir crypter le message
        button_crypter = tkinter.Button(self.window, text='Crypter', command=self.recupEntryCryptage, bg='#4065A4', font=('Helvetica', 20), fg='white')
        button_crypter.place(x=600, y=200)

        # le dernier champs pour pouvoir afficher le message crypter
        label_affiche = tkinter.Label(self.window, text="Le message crypter est:", font=('Courrier', 15),bg='#4065A4', fg='white', width=30)
        label_affiche.place(x=2, y=300)

        self.affiche = tkinter.Entry(self.window, bg='#4065A4', font=('Helvetica', 20), fg='white', width=30)
        self.affiche.place(x=300, y=300)

    # definir une methode permettant de pouvoir recuperer les valeurs entrer par l'utilisateur
    def recupEntryCryptage(self):
        message = self.insert_mess.get()
        clef = self.insert_clef.get()

        message_crypte = cryptage(message, clef)
        self.affiche.delete(0, 10)
        self.affiche.insert(0, message_crypte)

    def interfaceDecryptage(self):


        self.interfaceClean()

        self.bar()

        label_title = tkinter.Label(self.window, text="SESSION DE DECRYPTAGE", font=('Helvetica', 20), bg='#4065A4', fg='white')
        label_title.pack()

        # creation des champs

        # on met le premier champs et son label dans un premier frame
        label_mess = tkinter.Label(self.window, text='Entrer le message ici:', font=('Courrier', 15), bg='#4065A4',
                                   fg='white')
        label_mess.place(x=2, y=100)

        self.insert_mess = tkinter.Entry(self.window, bg='#4065A4', font=('Helvetica', 20), fg='white', width=30)
        self.insert_mess.place(x=300, y=100)

        # on met le second champs dans un second frame
        label_clef = tkinter.Label(self.window, text="Entrer la clé de dechiffrement ici:", font=('Courrier', 15),
                                   bg='#4065A4', fg='white')
        label_clef.place(x=2, y=150)

        self.insert_clef = tkinter.Entry(self.window, bg='#4065A4', font=('Helvetica', 20), fg='white', width=30)
        self.insert_clef.place(x=300, y=150)

        # le bouton de commande pour pouvoir crypter le message
        button_decrypter = tkinter.Button(self.window, text='Decrypter', command=self.recupEntryDecryptage, bg='#4065A4',
                                        font=('Helvetica', 20), fg='white')
        button_decrypter.place(x=600, y=200)

        # le dernier champs pour pouvoir afficher le message crypter
        label_affiche = tkinter.Label(self.window, text="Le message decrypter est:", font=('Courrier', 15), bg='#4065A4',
                                      fg='white', width=30)
        label_affiche.place(x=2, y=300)

        self.affiche = tkinter.Entry(self.window, bg='#4065A4', font=('Helvetica', 20), fg='white', width=30)
        self.affiche.place(x=300, y=300)

    # definir une methode permettant de recuperer les saisirs du decryptage et le décrypter
    def recupEntryDecryptage(self):

        message = self.insert_mess.get()
        clef = self.insert_clef.get()

        message_decrypte = decryptage(message, clef)
        self.affiche.delete(0, tkinter.END)
        self.affiche.insert(0, message_decrypte)

    def interfaceCryptFile(self):
        """Interface pour crypter les fichiers texte"""

        self.interfaceClean()
        self.bar()

        frame = tkinter.Frame(self.window, bg='#4065A4')

        self.entry_path = tkinter.Entry(frame, font=('Courrier', 15), bg='#4065A4',
                                      fg='white', width=30)
        self.entry_path.pack()
        self.button_file = tkinter.Button(frame, text='Choisir un fichier', font=('Courrier', 15), bg='#4065A4',
                                      fg='white', width=30, command=partial(recupFile, self.entry_path))
        self.button_file.pack()

        file = self.entry_path.get()

        tkinter.Button(frame, text='Crypter le fichier', font=('Courrier', 15), bg='#4065A4',
                                      fg='white', width=30, command=partial(recupContentFile, True, self.entry_path)).pack()

        frame.pack(expand=True)


    def interfaceDecryptFile(self):
        """interface pour decrypter les fichiers texte"""

        self.interfaceClean()
        self.bar()

        self.interfaceClean()
        self.bar()

        frame = tkinter.Frame(self.window, bg='#4065A4')

        self.entry_path = tkinter.Entry(frame, font=('Courrier', 15), bg='#4065A4',
                                        fg='white', width=30)
        self.entry_path.pack()
        self.button_file = tkinter.Button(frame, text='Choisir un fichier', font=('Courrier', 15), bg='#4065A4',
                                          fg='white', width=30, command=partial(recupFile, self.entry_path))
        self.button_file.pack()

        tkinter.Button(frame, text='Decrypter le fichier', font=('Courrier', 15), bg='#4065A4',
                       fg='white', width=30, command=partial(recupContentFile, False, self.entry_path)).pack()

        frame.pack(expand=True)

