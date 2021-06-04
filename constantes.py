import string

all_letters = list(string.ascii_letters + string.punctuation + string.digits + ' ') # creation d'une liste de carractere
alphabets = {}
i = 0

while i != len(all_letters):
    alphabets[i] = all_letters[i]
    i+=1

width_button = 20
height_button = 3
font_default = ('courrier', 10)
program_version = '1.2.0'
PASS_CHAR = '*'
