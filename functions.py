"""Fichier contenant toute les fonctions du programme crypto"""

import tkinter
from cryptage.crypt import Cryptage
from cryptage.decrypt import Decryptage
from tkinter import filedialog
from tkinter import messagebox


def recupContentFile(crypt, entry_path, entry_clef):
    """Chargé de recuperer le chemin menant au fichier"""
    file_path = entry_path.get()
    clef = entry_clef.get()
    clef = int(clef)

    # crypt est un boolean

    # crypt vaut vrai alors on crypte le fichier
    if crypt:
        cryptFile(file_path, clef)
        displayMess("Votre fichier à bien été crypter", 'Crypter')
    # crypt vaut faut c'est a dire qu'on veut decrypter
    else:
        decryptFile(file_path, clef)
        displayMess("Votre fichier à bien été decrypter", 'Decrypter')

def recupFile(entry_path):
    """Permet de recuperer le contenue du fichier entrer"""

    filename = filedialog.askopenfilename(title='Ouvrir votre document', filetypes=[('txt files','.txt'),('all files,', '.*')])

    entry_path.delete(0, tkinter.END)
    entry_path.insert(0, filename)


def cryptFile(file_path, clef):

    cryptage = Cryptage()
    list_crypt = cryptage.lockFile(file_path, clef)

    # sauvegarde du fichier
    saveFile(file_path, list_crypt)

def decryptFile(file_path, clef):

    decryptage = Decryptage()
    list_decrypt = decryptage.unLockFile(path=file_path, clef=clef)

    saveFile(file_path, list_decrypt)


def saveFile(name_file, content):
    """Sauvegarde le fichier"""
    file = open(name_file, 'w')
    file.write('\n'.join(content))
    file.close()

def displayMess(message, title=''):
    """Affiche des messages d'alerte"""

    box = messagebox.Message()

    box.show(title=title, message=message)