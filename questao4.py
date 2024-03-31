import random

def embaralhar_string(s):
    s = s.lower()
    caracteres = list(s)
    random.shuffle(caracteres)
    string_embaralhada = ''.join(caracteres)
    return string_embaralhada

palavra = "Python"
palavra_embaralhada = embaralhar_string(palavra)
print("Palavra original:", palavra)
print("Palavra embaralhada:", palavra_embaralhada)
