from multiprocessing import Pool
import subprocess
import os
import time
import signal

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

def function_to_run(x, y, z):
    # Aquí va el código que quieres ejecutar en paralelo
    print(f"PID: {os.getpid()}")
    
    time.sleep(15)
    obtener_informacion_proceso(os.getpid())
    return x + y + z

if __name__ == "__main__":
    pool = Pool() # Crea un pool de procesos
    # Crea una lista de triples de números
    numbers = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15)]
    # Usa starmap para aplicar function_to_run a cada triple de números
    results = pool.starmap(function_to_run, numbers)
    # Imprime los resultados
    print(results)
