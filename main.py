from tkinter import *

alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabetoMayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
longitudAlfabeto = len(alfabeto)

#Función para asignar valores
def set_text(text, input):
    input.delete(0,END)
    input.insert(0,text)
    return

#funcion para encriptar
def desencriptar(ventanaMensaje, mensaje, llave, resultado):
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
    set_text(textoEncriptado, resultado)

#funcion para encriptar
def encriptar(mensaje, llave, resultado):
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
    set_text(textoEncriptado, resultado)

#Función de asignación de opción
def ejecutarOpcion(opcion, mensaje, llave, resultado):
    if opcion == "Encriptar":
        encriptar(mensaje, llave, resultado)
    else:
        desencriptar(mensaje, llave, resultado)

#funcion para crear ventana de encriptar/desencriptar
def ventanaMensaje(opcion):
    #Ventana
    ventanaMensaje = Toplevel(ventana)
    ventanaMensaje.title(f"Guia 2 - {opcion}")
    ventanaMensaje.geometry("500x250")
    ventanaMensaje.resizable(0,0)
    ventanaMensaje.protocol("WM_DELETE_WINDOW", disable_event)
    ventanaMensaje.focus_set()

    #Ingreso de datos
    Label(ventanaMensaje, text="Ingresa el mensaje:").place(x=50, y=50)
    Label(ventanaMensaje, text="Ingresa la llave:").place(x=50, y=100)
    mensaje = Entry(ventanaMensaje)
    mensaje.place(x=175, y=50)
    llave = Entry(ventanaMensaje)
    llave.place(x=175, y=100)

    #Resultados
    resultado = Entry(ventanaMensaje)
    resultado.place(x=175, y=200)
    Button(ventanaMensaje, text = opcion, command= lambda: ejecutarOpcion(opcion, mensaje.get(), int(llave.get()), resultado)).place(x=50, y=150)
    Label(ventanaMensaje, text="Resultado:").place(x=50, y=200)    

    #Botón Salir
    Button(ventanaMensaje, text = "Salir", command= lambda: salir(ventanaMensaje)).place(x=400, y=200)
    ventana.withdraw()

#Método para cerrar las ventanas
def salir(vModal):
    vModal.withdraw()
    ventana.deiconify()

def disable_event():
    pass

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