import multiprocessing as mp
import numpy as np
import ctypes as c

def CreateArray(n, m, shared_array):
   shared_array = np.frombuffer(shared_array, c.c_int) # array unidimensional
   print('np array len=',len(shared_array))
   shared_array = shared_array.reshape((n,m)) # b and arr share the same memory
   print(shared_array,'gatisimo')
   return shared_array

if __name__=='__main__':
   with mp.Manager() as manager:
       shared_array = mp.sharedctypes.RawArray('i',10*10)
       p1 = mp.Process(target = CreateArray, args=(10,10,shared_array))
       p1.start()
       p1.join()
       print(shared_array[:])
