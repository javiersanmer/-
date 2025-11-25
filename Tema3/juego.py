import funciones
vidas = 10
nNivel = 1
maxNivel = 3

while nNivel <= maxNivel and vidas > 0:
    print("-------------------")
    print(f"Nivel {nNivel}")
    print("-------------------")

    palabra =  funciones.eligePalabra(nNivel)
    vidas = funciones.jugar(palabra, vidas)
    
    if funciones.palabraCompletada(palabra, [p for p in palabra if p in palabra]):
        if nNivel == maxNivel:
            print("Has GANADOOO")
            break
        else:
            print(f"Sube al nivel {nNivel + 1}")
            nNivel += 1
    else:
        print("Has perdido")
        break




