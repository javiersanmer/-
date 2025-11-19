import random
#3 niveles iguales, lo unico q cambia es el len. Haz una funcion para nivel y lo unico a cambiar sea longitud

def eligePalabra():
    if nNivel == 1:
        palabras = ["Illo", "Fohs", "Payo", "Loco"]
    elif nNivel == 1:
        palabras = ["sadfg", "sdfg", "dsfgfg", "dsfg"]
    elif nNivel == 1:
        palabras = ["dfgsdsfg", "dfgsdsd", "dsfgsdfg", "sdfgfsdg"]
    
    palabraAleatoria = random.randint(0, len(palabras) - 1)
    return palabras[palabraAleatoria]
def ahorcado():
    solucion = []
    for _ in len(palabra):
        solucion.append(palabra())
    print(solucion)
    
def menuJuego():
    for nNivel in range(1,4):
        print("-------------------")
        print(f"Nivel {nNivel}")
        print("-------------------")
        print("La palabra que debes encontrar: ")
    palabra = eligePalabra(nNivel)
    solucion = ahorcado(palabra)

def jugar():
    eligePalabra()