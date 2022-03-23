import time
import threading

# acquired es como sem_wait() y release es como sem_post() en C.


class filosofo(threading.Thread):
	semaforo = threading.Lock()  # Creamos el semaforo.
	situacion = []
	cubiertos = []

	def __init__(self, index):
		super().__init__()
		self.id = index
		filosofo.situacion.append('filosofando')
		# Se inicializa en 0 para evitar que todos entren a comer a l mismo tiempo
		filosofo.cubiertos.append(threading.Semaphore(0))
		print("Filosofo[" + str(self.id + 1) + "] esta pensando")

	def comer(self):
		print("Filosofo[" + str(self.id + 1) + "] esta comiendo")
		time.sleep(2)
		print("Filosofo[" + str(self.id + 1) + "] ya termino de comer")

# Toma los cubiertos verificando la situacion de los filosofos de los lados.
	def tomar(self):
		filosofo.semaforo.acquire()
		filosofo.situacion[self.id] = 'esperando'
		self.verificar_situacion(self.id)
		filosofo.semaforo.release()
		filosofo.cubiertos[self.id].acquire()

  # Suelta los cubiertos y avisa que lo hara
	def soltar(self):
		filosofo.semaforo.acquire()
		filosofo.situacion[self.id] = 'filosofando'
		self.verificar_situacion(self.filosofo_izquierda(self.id))
		self.verificar_situacion(self.filosofo_derecha(self.id))
		filosofo.semaforo.release()

  # Verifica que los filosofos de los sus lados esten o no comiendo.
	def verificar_situacion(self, i):
		if filosofo.situacion[i] == 'esperando':
			if filosofo.situacion[self.filosofo_izquierda(i)] != 'comiendo' and filosofo.situacion[self.filosofo_derecha(i)] != 'comiendo':
				filosofo.situacion[i] = 'comiendo'
				filosofo.cubiertos[i].release()

	def filosofo_derecha(self, i):
		if 0 > (i-1):
			return 4
		else:
			return (i-1)

	def filosofo_izquierda(self, i):
		if 4 < (i+1):
			return 0
		else:
			return (i+1)

	def run(self):
		time.sleep(1)
		self.tomar()
		self.comer()
		self.soltar()


def inicio(cantidadComer):
	for i in range(cantidadComer):
		print(str(i) + ' Ronda')
		lista = []
		for i in range(5):
		  lista.append(filosofo(i))

	    for f in lista:
		  f.start() 
		
		for f in lista:
		  f.join()

inicio(3)



