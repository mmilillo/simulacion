
#comentarios:
# A continuacion se detalla el esqueleto de la clase Estadistica del trabajo de Teoria de Colas. 
# Esta clase debería ser incorporada al trabajo desarrollado en la primera parte del TP.
# Agregar todos los métodos que sean necesarios para el cálculo de las estadísticas.

# prefijo de las variables:
#	f: float
#	i: int
#	v*: vector o lista de tipo *
#   c: instancia de una clase
import TP4P1

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
		# cada determinada cantidad de pasadas sumo cuantos habia en el sistema
		self.cantidadTotalClientesTotalEnSistema = 0

		#agregado por mi
		# cada determinada cantidad de pasadas sumo cuantos habia en la cola
		self.cantidadClientesTotalEnCola = 0
		
		#cada vez sumo a self.cantidadClientesTotalEnCola y self.CantidadTotalClientesTotalEnSistema le sumo 1
		self.cantMediciones = 0
		
	def W(self):
		if self.cantClientesAtendidos > 0:
			return self.tiempoTotalClientesEnSistema / self.cantClientesAtendidos
		else:
			return 0
		#W: tiempo promedio que paso un cliente en el sistema
		
	def Wq(self):
		if self.cantClientesQueEsperaron > 0:
			return self.tiempoTotalClientesEnCola / self.cantClientesQueEsperaron
		else:
			return 0
		#Wq: tiempo promedio que paso un cliente en la cola
		
	def L(self):
		return self.cantidadTotalClientesTotalEnSistema / self.cantMediciones
		#L: promedio de clientes en el sistema
		
	def Lq(self):
		return self.cantidadClientesTotalEnCola / self.cantMediciones
		#Lq: promedio de clientes en la cola
	
	def procesar(self, sistema):
		self.cantMediciones += 1

		self.tiempoTotalClientesEnSistema = self.tiempoTotalClientesEnSistema + sistema.acumuladorTiempoClientesEnSistema
		self.tiempoTotalClientesEnCola = self.tiempoTotalClientesEnCola + sistema.acumuladorTiempoClientesEnCola

		self.cantClientesAtendidos = self.cantClientesAtendidos + sistema.clientesAtendidos
		self.cantClientesQueEsperaron = self.cantClientesQueEsperaron + sistema.cantClientesQueEsperaron

		self.cantidadTotalClientesTotalEnSistema += sistema.cantidadActualClientesEnSistema()
		self.cantidadClientesTotalEnCola += sistema.cantidadActualClientesEnCola()



	
