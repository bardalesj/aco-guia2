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
def encriptar(mensaje, llave):
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
    print(textoEncriptado)
    print(textoAscii(textoEncriptado))
    print(textoBinario(textoEncriptado))
    print(textoHexadecimal(textoEncriptado))
    return textoEncriptado

#funcion para crear ventana de encriptar/desencriptar
def ventanaMensaje(opcion):
    ventanaMensaje = Toplevel(ventana)
    ventanaMensaje.title(f"Guia 2 - {opcion}")
    ventanaMensaje.geometry("500x250")
    ventanaMensaje.resizable(0,0)
    ventanaMensaje.focus_set()
    Label(ventanaMensaje, text="Ingresa el mensaje:").place(x=50, y=50)
    Label(ventanaMensaje, text="Ingresa la llave:").place(x=50, y=100)
    mensaje = Entry(ventanaMensaje)
    mensaje.place(x=175, y=50)
    llave = Entry(ventanaMensaje)
    llave.place(x=175, y=100)
    Button(ventanaMensaje, text = opcion, command= lambda: encriptar(mensaje.get(), int(llave.get()))).place(x=50, y=150)


#ventana para el menu
ventana = Tk()
ventana.title("Guia 2 - Arquitectura")
ventana.geometry("350x100")
ventana.resizable(0,0)
cabecera = Label(ventana, text = "Método César").pack()

#creacion de botones del menu
opcionEncriptar = Button(ventana, text="Encriptar Mensaje", command= lambda: ventanaMensaje("Encriptar")).place(x = 50, y = 50)
opcionDesencriptar = Button(ventana, text="Desencriptar Mensaje", command= lambda: ventanaMensaje("Desencriptar")).place(x = 200, y = 50)

ventana.mainloop()