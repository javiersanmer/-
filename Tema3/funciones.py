import random
#3 niveles iguales, lo unico q cambia es el len. Haz una funcion para nivel y lo unico a cambiar sea longitud
def palabra():
    nNivel = 1
    if nNivel == 1:
        pAleatoria = random.randint(0,3)
        match pAleatoria:
            case 1:
                return "Illo"
            case 2: 
                return "Fooh"
            case 3: 
                return "Payo"

def ahorcado():
    solucion = []
    for _ in len(palabra):
        solucion.append(palabra())
    print(solucion)
    
def menuJuego():
    nNivel = 1
    print("-------------------")
    print(f"Nivel {nNivel}")
    print("-------------------")
    print("La palabra que debes encontrar: ")
