import random
def mostrarHuecos(palabra, letraAcierto):
    huecos = []
    for letra in palabra:
        if letra in letraAcierto:
            huecos.append(letra)
        else:
            huecos.append("_")
    print(huecos)

def pideLetra():
    letra = input("Introduce una letra: ")
    return letra

def menuJuego(vidas, palabra, letraAcierto):
    print(f"Tienes {vidas} vidas")
    print("Palabra que debes encontrar: ")
    mostrarHuecos(palabra, letraAcierto)

def mostrarLista(lista):
    for elemento in lista:
        print(elemento, end=" ")
    
def eligePalabra(nNivel):
    nivel1 = ["TAZA", "GATO", "LORO", "MESA"]
    nivel2 = ["PARTIR", "ESPERA", "SUFRIR", "PYTHON" ]       
    nivel3 = ["PELICULA", "CANGREJO", "RATON", "SOMBRERO", "TORNILLO"]
    
    if nNivel == 1:
        listaNivel = nivel1
    elif nNivel == 2:
        listaNivel = nivel2
    elif nNivel == 3:
        listaNivel = nivel3

    palabraAleatoria = random.randint(0, len(listaNivel) - 1)
    return listaNivel[palabraAleatoria]

def vidasTotales(letrasAcierto,letraRepetida,palabra, letra, vidas):
    if letra in letrasAcierto or letra in letraRepetida:
        print("Ya has probado")
        vidas -=1
    else:
        encontrado = False
        for i in palabra:
            if i == letra:
                encontrado = True
                break
        
        if encontrado:
            print("Has encontrado una letra! Te sumo una vida")
            letrasAcierto.append(letra)
            vidas += 1
        else:
            print("Has fallado :(, pierdes una vida")
            vidas -= 1
    return vidas

def palabraCompletada(palabra, letraAcierto):
    completada = True
    for p in palabra:
        if p not in letraAcierto:
            completada = False
    return completada

def jugar(palabra, vidas):
    letrasAcierto = []
    letraRepetida = []

    while vidas > 0:
        menuJuego(vidas, palabra, letrasAcierto)
        letra = pideLetra()
        vidas = vidasTotales(letrasAcierto,letraRepetida,palabra, letra, vidas)


        if palabraCompletada(palabra, letrasAcierto):
            print("Enhorabuena has encontrado la palabra: ")
            for p in palabra:
                print(p, end= " ")
            break
    
    if vidas == 0:
        print("Has perdido, la palabra era: ")
        for p in palabra:
            print(p, end= " ")
    return vidas