alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

mediaBaja= 0
alumnoBajo = alumnos[0]
for alumno in alumnos:
    nombre = alumno[0]
    notas = alumno[1:]
    media = sum(notas)/ len(notas)
    if media < mediaBaja:
        mediaBaja = media
        alumnoBajo = alumno
print(f"El alumno con la {media} más baja es {alumnoBajo}")