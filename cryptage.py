####################################
#         => Crypto <=
#nom du fichier=>cryptage.py
# date de creation => 06/02/2021
# date dernier modif => 07/02/2021
# role: contient les fonctions de cryptage
#         =>Par MISTIGRIX658<=

from constantes import *

def cryptage(mess, clef):
    """Fonction permettant de crypter un message en l'additionnant avec sa clé de chiffrement"""

    message_crypter = ''

    clef = int(clef) # conversion de la clé en entier (etait en chaine de carrctère au paravant)

    # on verifie les numeroos des lettres et on les additionnent avec la clef
    for lettre in mess:
        #recuperation des lettres et leurs indices dans la variables alphabets
        for numero_lettre, lettre_alpha in alphabets.items():
            #on verifie si on a la bonne lettre
            if lettre == lettre_alpha:
                # ajout de la clé au numero de la lettre
                numero_lettre = numero_lettre + clef
                # on verifie dabord si l'addition ne depasse par les nombres de lettres
                if numero_lettre > len(alphabets)-1:
                    # on prend la difference le numero de la lettre trouvé et le nombre de lettre dans notre alphabets
                    numero_lettre = numero_lettre - len(alphabets) # notre alphabets commence avec l'indice 0

                # on ajoute la lettre crypter à notre message crypter
                message_crypter += alphabets[numero_lettre]


    # renvoi de notre message crypter
    return message_crypter


def decryptage(mess, clef):
    """Fonction permettant de decrypter un message crypter par la fonction cryptage"""

    message_decrypter = ''
    numero_decrypte = 0

    clef = int(clef)  # conversion de la clé en entier (etait en chaine de carrctère au paravant)

    # on verifie les numeroos des lettres et on les additionnent avec la clef
    for lettre in mess:
        # recuperation des lettres et leurs indices dans la variables alphabets
        for numero_lettre, lettre_alpha in alphabets.items():
            # on verifie si on a la bonne lettre
            if lettre == lettre_alpha:
                # on soustrait sa clé
                numero_decrypte = numero_lettre - clef
                if numero_decrypte < 0:
                    numero_decrypte = numero_decrypte + len(alphabets)

                message_decrypter += alphabets[numero_decrypte]

    return message_decrypter

