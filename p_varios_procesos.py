import multiprocessing as mp
import numpy as np
import ctypes as c

def CreateArray(n, m, shared_array):
   shared_array[:] = np.arange(n*m).astype(np.int)

def addData(n, m, shared_array):
   arr = np.frombuffer(shared_array.get_obj(), c.c_int)
   arr = arr.reshape((n, m))

   i = 0
   for nn in range(n):
       for mm in range(m):
           arr[nn][mm] = i
           i = i + 1
   print(arr)

if __name__ == '__main__':
   with mp.Manager() as manager:
       shared_array = manager.Array('i', range(12)) # Crear un array compartido con 12 elementos

       p1 = mp.Process(target=CreateArray, args=(3, 4, shared_array))
       p1.start()
       p1.join()

       p2 = mp.Process(target=addData, args=(3, 4, shared_array))
       p2.start()
       p2.join()

       print(shared_array)
