"""Fichier contenant toute les fonctions du programme crypto"""

import tkinter
from tkinter import filedialog
from tkinter import messagebox
from cryptage import *


def recupContentFile(crypt, entry_path):
    """Chargé de recuperer le chemin menant au fichier"""
    file_path = entry_path.get()

    # crypt est un boolean

    # crypt vaut vrai alors on crypte le fichier
    if crypt:
        cryptFile(file_path, 2)
        displayMess("Votre fichier à bien été crypter", 'Crypter')
    # crypt vaut faut c'est a dire qu'on veut decrypter
    else:
        decryptFile(file_path, 2)
        displayMess("Votre fichier à bien été decrypter", 'Decrypter')

def recupFile(entry_path):
    """Permet de recuperer le contenue du fichier entrer"""

    filename = filedialog.askopenfilename(title='Ouvrir votre document', filetypes=[('txt files','.txt'),('all files,', '.*')])

    entry_path.delete(0, tkinter.END)
    entry_path.insert(0, filename)


def cryptFile(file_path, clef):
    """Fonction permettant de crypter un fichier"""

    try:
        file = open(file_path, 'r+')
    except FileNotFoundError: # le fichier n'a pas été rétrouvé
        displayMess("Le fichier n'a pas été rétrouver", 'Non Trouvé')
        return 0

    content = file.readlines()

    list_crypt = []

    # recupere chaque ligne, la crypte et l'ajoute a liste crypter
    for line in content:
        line_crypt = cryptage(line, clef)
        list_crypt.append(line_crypt)

    file.close()

    # sauvegarde du fichier
    saveFile(file_path, list_crypt)

def decryptFile(file_path, clef):
    """Fonction permettant de crypter un fichier"""

    try:
        file = open(file_path, 'r+')
    except FileNotFoundError: # le fichier n'a pas été rétrouvé
        displayMess("Le fichier n'a pas été rétrouver", 'Non Trouvé')
        return 0

    content = file.readlines()

    list_decrypt = []

    for paragraph in content:
        paragraph_decrypt = decryptage(paragraph, clef)
        list_decrypt.append(paragraph_decrypt)

    file.close()

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