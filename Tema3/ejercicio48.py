matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

for fila in matriz:
    for elemento in fila:
        if elemento < 0:
            elemento = elemento * (-1)
        print(elemento, end = " ")
