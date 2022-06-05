import tkinter as tk
from tkinter import *

alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabetoMayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
longitudAlfabeto = len(alfabeto)

#funcion para convertir texto a ascii
def textoAscii(texto):
    return ' '.join(list(map(str,map(ord, texto))))

#funcion para convertir texto a binario
def textoBinario(texto):
    return ' '.join(format(ord(c), 'b') for c in texto)

#funcion para convertir texto a hexadecimal   
def textoHexadecimal(texto):
    texto = texto.encode('utf-8')
    return texto.hex()

#funcion para encriptar
def desencriptar(mensaje, llave, resultado):
    print(mensaje)
    textoDesencriptado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            textoDesencriptado += letra
            continue
        valor_letra = ord(letra)
        # Suponemos que es minúscula, así que esto comienza en 97(a) y se usará el alfabeto en minúsculas
        alfabeto_a_usar = alfabeto
        limite = 97  # Pero si es mayúscula, comienza en 65(A) y se usa en mayúsculas
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabetoMayusculas

        # Rotamos la letra, ahora hacia la izquierda
        posicion = (valor_letra - limite - llave) % longitudAlfabeto

        # Convertimos el entero resultante a letra y lo concatenamos
        textoDesencriptado += alfabeto_a_usar[posicion]
    resultadoASCII.set(textoAscii(textoDesencriptado))
    resultadoBinario.set(textoBinario(textoDesencriptado))
    resultadoHexa.set(textoHexadecimal(textoDesencriptado))
    resultadoChar.set(textoDesencriptado)

#funcion para encriptar
def encriptar(mensaje, llave, ventana):
    print(mensaje)
    textoEncriptado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            textoEncriptado += letra
            continue
        valorLetra = ord(letra)
        alfabetoAUsar = alfabeto
        limite = 97
        if letra.isupper():
            limite = 65
            alfabetoAUsar = alfabetoMayusculas
        posicion = (valorLetra - limite + llave) % longitudAlfabeto
        textoEncriptado += alfabetoAUsar[posicion]
    resultadoASCII.set(textoAscii(textoEncriptado))
    resultadoBinario.set(textoBinario(textoEncriptado))
    resultadoHexa.set(textoHexadecimal(textoEncriptado))
    resultadoChar.set(textoEncriptado)

#Función de asignación de opción
def ejecutarOpcion(opcion, mensaje, llave, ventana):
    if opcion == "Encriptar":
        encriptar(mensaje, llave, ventana)
    else:
        desencriptar(mensaje, llave, ventana)

#funcion para crear ventana de encriptar/desencriptar
def ventanaMensaje(opcion):
    #Ventana
    ventanaMensaje = Toplevel(ventana)
    ventanaMensaje.title(f"Guia 2 - {opcion}")
    ventanaMensaje.geometry("500x450")
    ventanaMensaje.resizable(0,0)
    ventanaMensaje.protocol("WM_DELETE_WINDOW", disable_event)
    ventanaMensaje.focus_set()

    #Ingreso de datos
    Label(ventanaMensaje, text="Ingresa el mensaje:").place(x=50, y=50)
    Label(ventanaMensaje, text="Ingresa la llave:").place(x=50, y=100)
    mensaje = Entry(ventanaMensaje)
    mensaje.place(x=175, y=50)
    llave = Entry(ventanaMensaje, validate="key", validatecommand=(validation, "%S"))
    llave.place(x=175, y=100)
    Button(ventanaMensaje, text = opcion, command= lambda: ejecutarOpcion(opcion, mensaje.get(), int(llave.get()), ventana)).place(x=50, y=150)

    #Resultados
    Label(ventanaMensaje, text="Resultado ASCII:").place(x=50, y=200)
    txtASCII = Entry(ventanaMensaje, width = 50, state="readonly", textvariable=resultadoASCII).place(x=175, y=200)

    Label(ventanaMensaje, text="Resultado Binario:").place(x=50, y=250)
    txtBinario = Entry(ventanaMensaje, width = 50, state="readonly", textvariable=resultadoBinario).place(x=175, y=250)    

    Label(ventanaMensaje, text="Resultado Hexadecimal:").place(x=50, y=300)
    txtHexa = Entry(ventanaMensaje, width = 50, state="readonly", textvariable=resultadoHexa).place(x=175, y=300)

    Label(ventanaMensaje, text="Resultado char:").place(x=50, y=350)
    txtChar = Entry(ventanaMensaje, width = 50, state="readonly", textvariable=resultadoChar).place(x=175, y=350)
    
    #Botón Salir
    Button(ventanaMensaje, text = "Salir", command= lambda: salir(ventanaMensaje)).place(x=400, y=400)
    ventana.withdraw()

#Método para cerrar las ventanas
def salir(vModal):
    resultadoASCII.set("")
    resultadoBinario.set("")
    resultadoHexa.set("")
    resultadoChar.set("")
    vModal.withdraw()
    ventana.deiconify()

def disable_event():
    pass

def only_numbers(char):
    return char.isdigit()

#ventana para el menu
ventana = Tk()
ventana.title("Guia 2 - Arquitectura")
ventana.geometry("350x100")
ventana.resizable(0,0)
cabecera = Label(ventana, text = "Método César").pack()

validation = ventana.register(only_numbers)

resultadoASCII = tk.StringVar()
resultadoBinario = tk.StringVar()
resultadoHexa = tk.StringVar()
resultadoChar = tk.StringVar()

#creacion de botones del menu
opcionEncriptar = Button(ventana, text="Encriptar Mensaje", command= lambda: ventanaMensaje("Encriptar")).place(x = 50, y = 50)
opcionDesencriptar = Button(ventana, text="Desencriptar Mensaje", command= lambda: ventanaMensaje("Desencriptar")).place(x = 200, y = 50)

ventana.mainloop()