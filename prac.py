import random

# -----------------------------------------
# Palabras de cada nivel (solo listas)
# -----------------------------------------
palabras_nivel_1 = ["gato", "pezs", "luna", "casa"]
palabras_nivel_2 = ["camion", "planeta", "carcel", "escoba"]
palabras_nivel_3 = ["elefante", "cuaderno", "trompeta", "sandwich"]

# -----------------------------------------
# Muestra la palabra con huecos
# -----------------------------------------
def mostrar_huecos(lista_letras):
    print(" ".join(lista_letras))

# -----------------------------------------
# Convierte palabra en lista de "_"
# -----------------------------------------
def crear_solucion(palabra):
    solucion = []
    for _ in palabra:
        solucion.append("_")
    return solucion

# -----------------------------------------
# Pide letra válida
# -----------------------------------------
def pedir_letra():
    letra = input("Introduce una letra: ").lower()
    while len(letra) != 1 or not letra.isalpha():
        letra = input("Introduce SOLO UNA letra válida: ").lower()
    return letra

# -----------------------------------------
# Elige palabra aleatoria SIN random.choice
# -----------------------------------------
def elegir_palabra(lista_palabras):
    indice = random.randint(0, len(lista_palabras) - 1)
    return lista_palabras[indice]

# -----------------------------------------
# Juega un nivel y devuelve si se ha completado
# -----------------------------------------
def jugar_nivel(palabra, vidas):
    solucion = crear_solucion(palabra)
    usadas = []  # letras ya dichas

    print("\nLa palabra que debes encontrar tiene", len(palabra), "letras:")
    mostrar_huecos(solucion)

    while "_" in solucion and vidas > 0:
        letra = pedir_letra()

        # Si ya se dijo → FALLO
        if letra in usadas:
            print("¡Esa letra ya la dijiste! Pierdes 1 vida.")
            vidas -= 1
            print("Vidas:", vidas)
            continue
        else:
            usadas.append(letra)

        # Comprobar si la letra está
        acierto = False
        for i in range(len(palabra)):
            if palabra[i] == letra:
                solucion[i] = letra
                acierto = True

        if acierto:
            vidas += 1
            print("¡Muy bien! Has acertado. +1 vida")
        else:
            vidas -= 1
            print("Letra incorrecta. -1 vida")

        mostrar_huecos(solucion)
        print("Vidas:", vidas)

    return vidas, "_" not in solucion


# -----------------------------------------
# JUEGO PRINCIPAL
# -----------------------------------------
vidas = 10
nivel = 1

print("=== JUEGO DEL AHORCADO ===")
print("Comienzas con", vidas, "vidas.")

while nivel <= 3 and vidas > 0:

    if nivel == 1:
        palabra = elegir_palabra(palabras_nivel_1)
    elif nivel == 2:
        palabra = elegir_palabra(palabras_nivel_2)
    else:
        palabra = elegir_palabra(palabras_nivel_3)

    print("\n----------------------------")
    print("        NIVEL", nivel)
    print("----------------------------")

    vidas, completado = jugar_nivel(palabra, vidas)

    if not completado:
        print("\nHas perdido todas tus vidas… ¡FIN DEL JUEGO!")
        exit()

    print("\n¡Has completado el nivel", nivel, "!")
    nivel += 1

# Final del juego
if vidas > 0:
    print("\n¡¡FELICIDADES!! Has completado los 3 niveles. ¡HAS GANADO!")
