#Password generator
from random import randint, sample

print ("Bienvenido al generador de contraseñas aleatorias")
print ('''
De cúantos dígitos quieres generar tu contraseña?
       ''')

digits_input = int(input())

def generadorLimpio(digitos):
    num = "0123456789"
    union = sample(num, digitos)
    pwd = "".join(union)
    return pwd

pwd = generadorLimpio(digits_input)

print(pwd)

