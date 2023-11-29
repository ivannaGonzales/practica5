import subprocess
import time
import os
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

if __name__ == '__main__':
    pid = int(input("Ingrese un PID: "))
    obtener_informacion_proceso(pid)# Reemplaza 137117 con el PID del proceso que quieres obtener

