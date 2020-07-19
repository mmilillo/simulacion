
#comentarios:
# A continuacion se detalla el esqueleto de la clase Estadistica del trabajo de Teoria de Colas. 
# Esta clase debería ser incorporada al trabajo desarrollado en la primera parte del TP.
# Agregar todos los métodos que sean necesarios para el cálculo de las estadísticas.

# prefijo de las variables:
#	f: float
#	i: int
#	v*: vector o lista de tipo *
#   c: instancia de una clase

class Estadistica:
	def __init__(self):
		#acumulador del tiempo total que pasaron los clientes en el sistema
		self.tiempoTotalClientesEnSistema = 0 #cliente.TiempoSalida - cliente.tiempoLlegada
		
		#acumulador del tiempo total que pasaron los clientes en la cola
		self.tiempoTotalClientesEnCola = 0 # cliente.tiempoInicioAtencion - cliente.TiempoLlegada
		
		#acumulador de clientes que fueron atendidos
		self.cantClientesAtendidos = 0 # cuando terminan de atender a alguen ++
		
		#acumulador de clientes que esperaron en la cola
		self.cantClientesQueEsperaron = 0 # cuando empiezan a atender ++

		#agregado por mi
		self.CantidadTotalClientesTotalEnSistema = 0 

		#agregado por mi
		self.cantidadClientesTotalEnCola = 0
		
		self.cantMediciones = 0
		
	def W(self):
		#W: tiempo promedio que paso un cliente en el sistema
		
	def Wq(self):
		#Wq: tiempo promedio que paso un cliente en la cola
		
	def L(self, sistema):
		#L: promedio de clientes en el sistema
		
	def Lq(self,cola):
		#Lq: promedio de clientes en la cola
	
