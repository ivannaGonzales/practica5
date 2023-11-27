from multiprocessing import Process, Manager, parent_process
import os 
import random
import numpy as np
def flatten_matriz(matriz):
   return [elemento for sublista in matriz for elemento in sublista]

def quick_sort(lista):
   if len(lista) <= 1:
       return lista
   else:
       pivot = lista[0]
       left = [x for x in lista[1:] if x < pivot]
       right = [x for x in lista[1:] if x >= pivot]
       return quick_sort(left) + [pivot] + quick_sort(right)

def reordenar_matriz(lista, filas, columnas):
   return [lista[i:i + columnas] for i in range(0, len(lista), columnas)]


def ordenar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz = flatten_matriz(matriz)
    matriz = quick_sort(matriz)
    matriz = reordenar_matriz(matriz, filas, columnas)
    return matriz

def creacion_matriz(matriz):
    pass


if __name__ == "__main__":
    with Manager() as manager:
        matriz = manager.Array('d',np.ones((5, 5)))
        #arr = Array('i', range(10))
        proceso_creacion_matriz = Process (target = creacion_matriz, args = (matriz,))
        proceso_creacion_matriz.start()
        proceso_creacion_matriz.join()
        print(matriz)