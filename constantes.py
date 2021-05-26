####################################
#         => Crypto <=

# nom du fichier => constante.py

# date de creation => 06/02/2021
# date dernier modif => 07/02/2021
# role: Contient toute les constantes du programme

#  =>Par MISTIGRIX658<=

import string


all_letters = list(string.ascii_letters + string.punctuation)

alphabets = {}

i = 0

while i != len(all_letters):
    alphabets[i] = all_letters[i]
    i+=1

width_button = 20
height_button = 3

font_default = ('courrier', 10)