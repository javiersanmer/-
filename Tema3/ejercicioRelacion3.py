def emparejar(aleatorio1: list, aleatorio2: list):
    while len(tenistas_top_8) != 0:
        jugador1 = aleatorio1.pop(0)
        jugador2 = aleatorio2.pop(-1)
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

emparejar(tenistas_top_8, tenistas_top_8)