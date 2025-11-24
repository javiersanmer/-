import random
#3 niveles iguales, lo unico q cambia es el len. Haz una funcion para nivel y lo unico a cambiar sea longitud

def mostrarHuecos(palabra, letraAcierto):
    huecos = []
    for letra in palabra:
        if letra in letraAcierto:
            huecos.append(letra)
        else:
            huecos.append("_")
    return huecos

def pideLetra():
    letra = input("Introduce una letra: ")  
    letraFinal = letra.lower()
    return letraFinal

def menuJuego(nNivel, vidas, palabra, letrasAcierto):
    print("-------------------")
    print(f"Nivel {nNivel}")
    print("-------------------")
    print(f"Tienes {vidas}")
    print("La palabra que debes encontrar: ")
    
    for letra in palabra:
        if letra in letrasAcierto:
            print(letra, end=" ")
        else:
            print("_",end = " ")
    print("")

def mostrarLista(lista):
    for elemento in lista:
        print(elemento, end=" ")
    
def eligePalabra(nNivel):
    if nNivel == 1:
        palabra =["Illo", "Fohs", "Payo", "Loco"]
    elif nNivel == 2:
        palabra = ["sadfg", "sdfg", "dsfgfg", "dsfg"]
    elif nNivel == 3:
        palabra = ["dfgsdsfg", "dfgsdsd", "dsfgsdfg", "sdfgfsdg"]
    
    palabraAleatoria = random.randint(0, len(palabra) - 1)
    return palabra[palabraAleatoria]

def vidasTotales(letrasAcierto,palabra, letra, vidas):
    if letra in palabra:
        print("Has encontrado una letra!!! Te sumo una vida")
        vidas += 1
        letrasAcierto.append(letra)
    else:
        print("Has fallado :(, pierdes una vida")
        vidas -= 1
    return vidas


def jugar(palabra, vidas):
    letrasAcierto = []

    while vidas > 0:
        letra = pideLetra()
        vidas = vidasTotales(letrasAcierto,palabra, letra, vidas)

        completada = True
        for letraPalabra in palabra:
            if letraPalabra not in letrasAcierto:
                completa = False
        if completada:
            print("Has completado una palabra")
            return True
    return False