##Este script genera un numero de passwords que le indiquemos, con unos caracteres que tambien le indiquemos
##y en el que nos cifra cada contraseña con varios tipos de hashes

import random
import string
import hashlib
import os

num_passwords = int(input("\nIndica el número de contraseñas que quieres generar: "))
num_caracteres = int(input("Indica el númeor de caracteres que tendrán las contraseñas (min -> 8/max -> 64): "))
tipo_hash = input("Indica el tipo de hash que quieres (md5/sha1/sha256/sha512): ")

letras = string.ascii_letters
numeros = string.digits
caracteres = string.punctuation

def generar_passwords(num_caracteres, num_passwords, tipo_hash):

    if num_caracteres < 8 or num_caracteres > 64:
        print("Por favor, introduce un número de caracteres entre 8 y 64.")
        return
    characters = letras + numeros + caracteres

    for i in range(num_passwords):

        salt = os.urandom(32)

        password = ''.join(random.choice(characters) for _ in range(num_caracteres))

        salted_passwords = salt + password.encode()
        hashed_passwords = hashlib.new(tipo_hash, salted_passwords).hexdigest()
        print(f"\nPassword {i + 1} --> {password}")
        print(f"Password hashed --> {hashed_passwords}")
        

generar_passwords(num_caracteres, num_passwords, tipo_hash)





