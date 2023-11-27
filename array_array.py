import multiprocessing as mp
import numpy as np
import ctypes as c

def CreateArray(n,m):
    mp_arr=mp.Array('i',n*m)
#    arr = np.frombuffer(mp_arr.get_obj())  #This command must be corrected. Thanks to GabrielC
    arr = np.frombuffer(mp_arr.get_obj(),c.c_int)  # mp_arr and arr share the same memory
    # make it two-dimensional
    print('np array len=',len(arr))
    b = arr.reshape((n, m))  # b and arr share the same memory
    return b

def addData(array):
    n,m=np.shape(array)
    i=0
    for nn in range(n):
        for mm in range(m):
            array[nn][mm]=i
            i=i+1
    print(array)

if __name__=='__main__':
    with mp.Manager() as manager:
        Myarray=CreateArray(3,4)
        p1=mp.Process(target=addData,args=(Myarray,))
        p1.start()
        p1.join()
        print(Myarray)