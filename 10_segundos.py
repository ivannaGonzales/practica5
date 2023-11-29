from multiprocessing import Process
import time

def proceso():
  print("Inicio del proceso")
  time.sleep(20) # Espera durante 10 segundos
  print("Hola")

if __name__ == '__main__':
  p = Process(target=proceso)
  p.start()
  print(f"El PID del proceso es {p.pid}")
  p.join()
