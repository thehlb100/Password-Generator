#Password generator
from random import randint, sample
import tkinter as tk


# The code snippet you provided is creating a simple GUI (Graphical User Interface) using the Tkinter
# library in Python. Here's a breakdown of what each part of the code is doing:
window = tk.Tk()
Titulo = tk.Label(text = 'Generador de contraseñas - made by TheHlb100', bg = 'Green', foreground= 'White')
Titulo.pack()

texto_Digitos = tk.Label(text = 'Introduce el número de digitos de la contraseña')
texto_Digitos.pack()


def generadorLimpio(digitos):
    """
    The function generates a random string of digits with a specified length.
    
    :param digitos: The parameter `digitos` in the `generadorLimpio` function represents the number of
    digits you want in the generated password. This function generates a random password of the
    specified length using digits 0-9
    :return: A string of random digits of the specified length is being returned.
    """
    num = "0123456789"
    union = sample(num, digitos)
    pwd = "".join(union)
    return pwd

def calcular():
    """
    The function calculates a password based on the number of digits inputted and displays it using a
    Tkinter label.
    """
    digits_input = int(entrada_Digitos.get())
    pwd = generadorLimpio(digits_input)
    print (f'TU contraseña es {pwd}')
    print('Generator made by TheHLB100')
    salida = tk.Label(text =f'Tu contraseña es {pwd}')
    salida.pack()



entrada_Digitos = tk.Entry()
entrada_Digitos.pack()
boton_Calcular = tk.Button(text = 'Calcular', command = calcular)
boton_Calcular.pack()

window.mainloop()
# The `window.pack()` line in the code is attempting to call the `pack()` method on the `window`
# object. However, in this context, it seems to be misplaced as the `pack()` method is typically used
# to organize and display widgets within a container, not on the window itself.
window.pack()