from cx_Freeze import *

setup(
    name = 'Crypto',
    version = '1',
    description = 'Programme de cryptage de message avec clé de chiffrement et dechiffrement',
    executables = [Executable('Crypto.py')]
)
