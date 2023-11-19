from multiprocessing import Process, Manager
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

if __name__ == "__main__":
    with Manager() as manager:
        matriz = manager.list()
        matriz.append([5,8,1])
        matriz.append([2,7])
        print(matriz)
        p = Process(target = ordenar_matriz, args=(matriz,))
        p.start()
        p.join()
        print(ordenar_matriz(matriz))