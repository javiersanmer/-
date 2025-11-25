import funciones
vidas = 10
nNivel = 1
maxNivel = 3
victoria = False
while nNivel <= maxNivel and vidas > 0:
    palabra =  funciones.eligePalabra(nNivel)
    victoria = funciones.jugar(palabra, vidas, nNivel)
    
    if victoria:
        if nNivel == maxNivel:
            print("Has GANADOOO")
            break
        else:
            print(f"Sube al nivel {nNivel + 1}")
            nNivel += 1
    else:
        print("Has perdido")
        break




