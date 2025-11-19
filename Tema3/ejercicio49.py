matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]
mayor = matriz[0][0]
for fila in matriz:
    for j in fila:
        if len(mayor) < len(j):
            mayor = j
    
print(mayor)