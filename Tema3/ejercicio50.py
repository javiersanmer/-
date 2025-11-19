matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]

vocales = "AEIOU"
contador = 0
for fila in matriz:
    for animal in fila:
        if animal[0] in vocales:
            contador +=1
    
print(contador)