alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]
total = 0
contador = 0
for alumno in alumnos:
    nombre = alumno[0]
    notas = alumno[1:]

    total += sum(notas)
    contador += len(notas)

print(total/contador)