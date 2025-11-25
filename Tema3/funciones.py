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

def vidasTotalesYletras(letrasAcierto,letraRepetida,palabra, letra, vidas):
    if letra in letrasAcierto or letra in letraRepetida:
        print("Ya has probado")
        vidas -=1
        return vidas

    encontrado = False
    for i in palabra:
        if i == letra:
            encontrado = True
            break
    
    if encontrado and letra not in letrasAcierto:
        print("Has encontrado una letra! Te sumo una vida")
        vidas += 1
        letrasAcierto.append(letra)
    else:
        print("Has fallado :(, pierdes una vida")
        vidas -= 1
    return vidas


def jugar(palabra, vidas, nNivel):
    letrasAcierto = []
    letraRepetida = []

    while vidas > 0:
        menuJuego(nNivel, vidas, palabra, letrasAcierto)
        letra = pideLetra()
        vidas = vidasTotalesYletras(letrasAcierto,letraRepetida,palabra, letra, vidas)

        completado = False
        for i in palabra:
            if i == letra:
                encontrado = True
            break

        if completado:
            print("Has completado una palabra")
            return True
    return False