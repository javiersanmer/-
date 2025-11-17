import funciones
vidas = 10
nNivel = 1
while True:
    funciones.menuJuego()
    funciones.ahorcado()
    if nNivel == 1:
        print("['_', '_', '_', '_']")
        letra = input("Inserta una letra: ")
        palabraResuelta = funciones.palabra()
        print(palabraResuelta)
