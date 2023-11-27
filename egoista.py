import multiprocessing as mp
import numpy as np
import ctypes as c
import random

def CreateArray(n,m,shared_array):
   shared_array = np.frombuffer(shared_array.get_obj(),c.c_int) # array unidimensional
   print('np array len=',len(shared_array))
   shared_array = np.array(shared_array).reshape((n,m)) # b and arr share the same memory
   return shared_array

if __name__=='__main__':
   with mp.Manager() as manager:
       shared_array = mp.Array('i',10*10)
       p1 = mp.Process(target = CreateArray, args=(10,10,shared_array))
       p1.start()
       p1.join()
       shared_array = np.frombuffer(shared_array.get_obj(), dtype=np.int).reshape((10,10))
       print(shared_array)
