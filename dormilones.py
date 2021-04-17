import time
import threading #hilos para concurrencia
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class Contador:
  def iniciar(self):
    self.inicio = time.perf_counter()

  def finalizar(self):
    self.fin = time.perf_counter()

  def imprimir(self):
    logging.info(f'Pasaron {self.fin - self.inicio} segundos')


def dormir():
  time.sleep(1) #duerme por 1 seg


contador = Contador()

# ejemplo clásico secuencial
contador.iniciar() #19:57:50

dormir()
dormir()

contador.finalizar() #19:57:52
contador.imprimir() #2 seg


# ejemplo con threads
contador.iniciar()

t1 = threading.Thread(target=dormir)
t2 = threading.Thread(target=dormir)

t1.start()
t2.start()

contador.finalizar()
contador.imprimir() #¿qué va a tirar en la consola?


# ejemplo con threads, pero esperando que terminen
contador.iniciar()

t1 = threading.Thread(target=dormir)
t2 = threading.Thread(target=dormir)

t1.start()
t2.start()


t1.join() #esperá a que termine el lanzamiento del hilo t1
t2.join()

contador.finalizar()
contador.imprimir()


# Pregunta: ¿por qué los segundos que pasaron son 2, 0 y 1 respectivamente?
# * 2 segundos: Determinado por las funciones dormir().
# * 0 segundo: Porque los hilos se ejecutan de forma independiente, las funciones se ejecutan una después de la otra
# sin perder tiempo.
# * 1 segundo: porque entre las funciones iniciar() y finalizar se encuentran los hilos con el método join() el cual
# indica que la secuencia debe esperar hasta que finalicen los hilos.

# Pregunta: ¿cuántos hilos o threads hay en cada caso?
# 1er caso: 1 hilo de forma secuencial (1).
# 2do caso: 1 hilo llamante y 2 hilos llamados (3).
# 3er caso: 1 hilo llamante y 2 hilos llamados (3).

# Pregunta: los últimos dos ejemplos tienen 3 threads cada uno, ¿cuál sería la diferencia entonces?
# El primero de los 3 threads se ejecutan de forma paralela.
# El segundo con los 3 threads primero se ejecuta el hilo llamante, espera a que terminen los dos hilos llamados y
# una vez finalizados estos el llamante continua y finaliza la ejecución.

