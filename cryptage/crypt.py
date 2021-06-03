# coding:utf-8
from constantes import *

class Cryptage:
    """Classe permettant de cryptage de fichier ou de message"""

    def __init__(self):
        pass

    def lockMess(self, message, clef):
        """Methode permettant de crypter un message et retourne le message crypter
        Paramètre: message à crypter et la clé de chiffrement"""

        return self.lock(message, clef)

    def lockFile(self, path, clef):
        """Methode permettant de crypter un fichier en retournant une liste.
        Paramètre: Chemin menant au fichier et la clé de chiffrement"""

        try:
            clef = int(clef)
            file = open(path, 'r+')
            content = file.readlines()
            list_crypt = []
            file.close()

            # recupere chaque ligne, la crypte et l'ajoute a liste crypter
            for line in content:
                line_crypt = self.lock(line, clef)
                list_crypt.append(line_crypt)

            return list_crypt

        except FileNotFoundError:
            return None
        except ValueError:
            raise ValueError("The clef is not int ")
        except:
            raise Exception

    def lock(self, message, clef):

        message_crypter = ''

        clef = int(clef)  # conversion de la clé en entier (etait en chaine de carrctère au paravant)

        # on verifie les numeroos des lettres et on les additionnent avec la clef
        for lettre in message:
            # recuperation des lettres et leurs indices dans la variables alphabets
            for numero_lettre, lettre_alpha in alphabets.items():
                # on verifie si on a la bonne lettre
                if lettre == lettre_alpha:
                    # ajout de la clé au numero de la lettre
                    numero_lettre = numero_lettre + clef
                    # on verifie dabord si l'addition ne depasse par les nombres de lettres
                    while numero_lettre > len(alphabets) - 1:
                        # on prend la difference le numero de la lettre trouvé et le nombre de lettre dans notre alphabets
                        numero_lettre = numero_lettre - len(alphabets)  # notre alphabets commence avec l'indice 0

                    # on ajoute la lettre crypter à notre message crypter
                    message_crypter += alphabets[numero_lettre]

        return message_crypter

if __name__ == '__main__':
    cryptage = Cryptage()
