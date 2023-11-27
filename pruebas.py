import random
def creacion_matriz(matriz):
    for i in range(100):
        matriz.append([])
        for j in range (100):
            matriz[i].append(random.randint(0,100))


matriz = []
creacion_matriz(matriz)
print(matriz)