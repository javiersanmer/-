matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]
sumTotal1 = sumTotal2 = 0

for fila in matriz:
    for elemento in fila:
        sumTotal1 += elemento

print(sumTotal1)

for fila in matriz:
    sumTotal2 += sum(fila)
print(sumTotal2)