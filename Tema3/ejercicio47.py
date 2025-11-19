matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]
posi= 0
posj = 0
for i, fila in enumerate(matriz):
    for j, elemento in enumerate(fila):
        if elemento == 5:
            posi = i
            posj = j
print(f"El número 5 se encuentra en las fila {posi} y columna {posj}")

for fila in matriz:
    for elemento in fila:
        if matriz.count(5)>0:
            posi = i
            posj = fila.index(5)

print(f"El número 5 se encuentra en las fila {posi} y columna {posj}")