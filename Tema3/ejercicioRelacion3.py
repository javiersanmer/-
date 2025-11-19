import random
def emparejar(lista: list[str]):
    while len(lista) > 0:
        n1 = random.randint(0, len(lista) - 1)
        jugador1 = lista.pop(n1)

        n2 = random.randint(0, len(lista) - 1)
        jugador2 = lista.pop(n2)
        print(f"{jugador1} vs {jugador2}")

tenistas_top_8 = [
    "Jannik Sinner",      # 11,330 puntos
    "Alexander Zverev",   # 8,135 puntos
    "Carlos Alcaraz",     # 7,410 puntos
    "Taylor Fritz",       # 4,900 puntos
    "Casper Ruud",        # 4,480 puntos
    "Daniil Medvedev",    # 3,930 puntos
    "Novak Djokovic",     # 3,900 puntos
    "Álex de Miñaur"      # 3,735 puntos
]

emparejar(tenistas_top_8.copy())
