import numpy as np

def sort_matrix_in_place(matrix):
   # Ordenar la matriz en su lugar
   matrix.sort()

   return matrix

# Definir una matriz
matrix = np.array([[21, 20], [26, 7]])

# Llamar a la función
sorted_matrix = sort_matrix_in_place(matrix)

# Imprimir la matriz ordenada
print(sorted_matrix)
