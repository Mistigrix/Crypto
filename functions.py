"""Fichier contenant toute les fonctions du programme crypto"""

import tkinter
from tkinter import filedialog
from tkinter import messagebox
from cryptage import *


def recupContentFile(crypt, entry_path):
    """"""
    file_path = entry_path.get()

    if crypt:
        cryptFile(file_path, 2)
        displayMess("Le fichier à bien été crypter vers le fichier fichierCrypter.txt", 2)
    else:
        decryptFile(file_path, 2)
        displayMess("Le fichier à bien été crypter vers le fichier fichierCrypter.txt", 2)

def recupFile(entry_path):
    """Permet de recuperer le contenue du fichier entrer"""

    filename = filedialog.askopenfilename(title='Ouvrir votre document', filetypes=[('txt files','.txt'),('all files,', '.*')])

    try:
        fichier = open(filename, 'r')
        content = fichier.read()
        fichier.close()
    except FileNotFoundError:
        displayMess("Le fichier n'a pas été rétrouver", 'Non Trouvé')

    entry_path.delete(0, tkinter.END)
    entry_path.insert(0, filename)


def cryptFile(file_path, clef):
    """Fonction permettant de crypter un fichier"""

    try:
        file = open(file_path, 'r+')
    except FileNotFoundError:
        displayMess("Le fichier n'a pas été rétrouver", 'Non Trouvé')
        return 0

    content = file.readlines()

    list_crypt = []

    for paragraph in content:
        paragraph_crypt = cryptage(paragraph, clef)
        list_crypt.append(paragraph_crypt)

    file.close()

    saveFile('fichierCrypter.txt', list_crypt)

def decryptFile(file_path, clef):
    """Fonction permettant de crypter un fichier"""

    file = open(file_path, 'r+')

    content = file.readlines()

    list_decrypt = []

    for paragraph in content:
        paragraph_decrypt = decryptage(paragraph, clef)
        list_decrypt.append(paragraph_decrypt)

    file.close()

    saveFile('fichierDecrypter.txt', list_decrypt)


def saveFile(name_file, content):
    """"""
    file = open(name_file, 'w')

    file.write('\n'.join(content))

    file.close()

def displayMess(self, message, title=''):
    """Affiche des messages d'alerte"""

    box = messagebox.Message()

    box.show(title=title, message=message)