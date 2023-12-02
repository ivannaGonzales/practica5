from multiprocessing import Pool
import subprocess
import os
import time
import signal
import numpy as np

def store_pids():
  pid_array = []
  while True:
      pid = input("Ingrese un PID (o 'q' para terminar): ")
      if pid.lower() == 'q':
          break
      pid_array.append(int(pid))
  return pid_array

def ejecucion_comandos():
    while (True):
        pass

def obtener_informacion_proceso_2(pid):
   comando = f"ps -p {pid} -o psr pid,ppid,cmd,%mem,%cpu"
   proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   salida, error = proceso.communicate()
   if error:
       print(f"Error al obtener información del proceso: {error}")
   else:
       print(salida.decode())

def obtener_informacion_proceso(pid):

    #
    # Ejecuta el comando una vez
    #
    #
    #Ir ejecutando el comando progresivamente
    #
    while not es_proceso_terminado(pid):
        comando = f"ps -p {pid} -o pid,ppid,cmd,psr,%mem,%cpu"
        proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida, error = proceso.communicate(timeout=1)
        if error:
            print(f"Error al obtener información del proceso: {error}")
            break
        elif salida:
            print(salida.decode())
        time.sleep(1) # Espera un segundo antes de verificar nuevamente

    print('Proceso terminado')

def obtener_informacion_todos_procesos(pids):
    for pid in pids:
        obtener_informacion_proceso(pids)

def es_proceso_terminado(pid):
   try:
       os.kill(pid, 0)
   except OSError:
       return True
   else:
       return False

def bubble_sort(matriz):
    # Aquí va el código que quieres ejecutar en paralelo
    print('inicio ',matriz,' matriz')
    print(f"PID: {os.getpid()}")
    comando = f"ps -p {os.getpid()} -o pid,ppid,cmd,psr,%mem,%cpu"
    proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida, error = proceso.communicate(timeout=1)
    if error:
        print(f"Error al obtener información del proceso: {error}")
    elif salida:
        print(salida.decode())
    n = len(matriz)
    for i in range(n-1):
       for j in range(n-i-1):
           if(matriz[j] > matriz[j+1]):
                matriz[j], matriz[j+1] = matriz[j+1], matriz[j]
    return matriz

if __name__ == "__main__":
    # Crea una lista de triples de números
    # Usa starmap para aplicar function_to_run a cada triple de números
    filas = np.random.randint(0,100,size=(4,100000))
    print(filas)
    start_time = time.time()
    pool = Pool() # Crea un pool de procesos
    results = pool.map(bubble_sort, filas)
    end_time = time.time() 
    # Imprime los resultados
    print(results)
    execution_time = end_time - start_time
    print(f"El programa se ejecutó en: {execution_time} segundos")