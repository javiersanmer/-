def devuelve(matriz: list[list[int]]):
    matriz = [[1, 2, 3],
              [4, 5, 6],
              [7, 8 ,9]
              ]
    
    for filas in matriz:
        filas = len(matriz)
        for columnas in filas:
            columnas = len(matriz[0])
    return [filas][columnas]
