import funciones
vidas = 10
nNivel = 1
maxNivel = 3
victoria = False
while nNivel <= maxNivel and vidas > 0:
    palabra =  funciones.eligePalabra(nNivel)
    funciones.menuJuego(nNivel, vidas, palabra, [])

    vidas = funciones.jugar(palabra, vidas)
    victoria = funciones.jugar(palabra, vidas)
    
    if victoria:
        if nNivel == maxNivel:
            print("Has GANADOOO")
            break
        else:
            print(f"Sube al nivel {nNivel + 1}")
            nNivel += 1
    else:
        print("Malo")




