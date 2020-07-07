import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math as math
import heapq

#comentarios:
# A continuacion se detalla el esqueleto de la primera parte del trabajo de Teoria de Colas. El modelo que seguiremos es el de un supermercado con una cola y multiples servidores (o cajas de atencion) 
# prefijo de las variables:
#	f: float
#	i: int
#	v*: vector o lista de tipo *
# c: instancia de una clase

def distribucionExponencial(lamda):
    # implemetntacion de la practica 3
    num = np.random.random_sample()
    resultado = ( (- 1 / lamda) * (math.log( 1 - num)))
    return resultado


class Cliente:
	def __init__(self, fTiempoLlegada):
                # inicializa las variables y setea el tiempo de llegada del cliente
                self.tiempoDeLlegada = fTiempoLlegada
                self.tiempoInicioAtencion = 0
                self.tiempoSalida = 0

	def setTiempoInicioAtencion(self,fTiempoInicioAtencion):
                # setter del tiempo del inicio de atencion del cliente
                self.tiempoInicioAtencion = fTiempoInicioAtencion

	def setTiempoSalida(self, fTiempoSalida):
	        # setter del tiempo de salida del cliente
                self.tiempoSalida = fTiempoSalida
		
class Sistema:
	def __init__(self, fTasaLlegadaClientes, vfTasasAtencionServidores):
                # inicializa: la tasa de llegada de clientes, el tiempo global
                # crea la cola de clientes
                # crea la lista de servidores (llama al metodo creacionServidores)
                # crea la bolsa de eventos
                self.tiempoGlobal = 0
                self.tasaLlegadaClientes = fTasaLlegadaClientes
                self.tasasAtencionServidores = vfTasasAtencionServidores
                self.colaClientes = []
                self.listaServidores = []
                self.creacionServidores()    
                self.bolsaEventos = []
                heapq.heapify(self.bolsaEventos)

	def creacionServidores(self):
	        # crea la lista de servidores respetando la respectivas tasa de 
                for x in range(len(self.tasasAtencionServidores)):
                        self.listaServidores.append(Servidor(self.tasasAtencionServidores[x]))

	
	def crearEventoProximoCliente(self): 
                # genera un evento de tipo EventoProximoCliente 
                # agregarlo a la bolsa de eventos
                evento = EventoProximoCliente(self.tiempoGlobal + distribucionExponencial(self.tasaLlegadaClientes), self)
                heapq.heappush(self.bolsaEventos, evento)

	
	def ingresoCliente(self): 
                # callback para la clase EventoProximoCliente.procesar
                # corresponde a la llegada efectiva del cliente
                # 1) crea el Cliente
                # 2) agrega el cliente a la cola
                # 3) crea el nuevo evento de llegada del proximo cliente (llama a self.crarEventoProximoCliente())
                # 4) agrega el evento a la bolsa de eventos
                print(self.tiempoGlobal)
                cliente = Cliente(self.tiempoGlobal)
                self.colaClientes.append(cliente)
                self.crearEventoProximoCliente()

	def avanzarTiempo(self, fTiempo): 
                self.tiempoGlobal = fTiempo
              
		
	def procesar(self):
                self.crearEventoProximoCliente() # 1) crea el eventoProximoCliente del 1er. cliente
                while(True):
                        evento = heapq.heappop(self.bolsaEventos) # 2) saca el proximo evento de la bolsa de eventos
                        evento.procesar() # 3) procesa el evento (via polimorfismo)
                        for s in self.listaServidores: #4) for s in self.servidores
                                if (not s.estaOcupado()) and len(self.colaClientes) > 0  :# 5) si el servidor esta desocupado y hay algun cliente en la cola
                                        cliente = self.colaClientes.pop(0) # 6) desencolar el primer cliente de la cola
                                        eventoFinAtencion = s.inicioAtencion(self.tiempoGlobal,cliente) # 7) llama al metodo servidor.inicioAtencion
                                        heapq.heappush(self.bolsaEventos, eventoFinAtencion) # 8) agregar a la bolsa de eventos el evento de FinAtencion



	
class Servidor:
	def __init__(self,fTasaAtencionServidor):
	        # inicializa variables
                self.tasaAtencionServer = fTasaAtencionServidor
                self.ocupado = False
                self.tiempoSalidaCliente = 0
		
	def estaOcupado(self):
                # flag: devuelve "true" si el servidor esta ocupado, y "false" si no
                if self.ocupado == True:
                        return True		
                else:
                        return False

	def inicioAtencion(self, fTiempoGlobal,cCliente):
                # setea el servidor en "ocupado"
                # setea el tiempo de inicio atencion del cliente
                # crea y devuelve el EventoFinAtencion
                self.ocupado = True
                cCliente.setTiempoInicioAtencion(fTiempoGlobal)
                print('se esta atendiendo cliente')
                return EventoFinAtencion(fTiempoGlobal + self.tasaAtencionServer, self)


	def finAtencion(self,fTiempo):
                # callback para EventoFinAtencion.procesar
                # setea el tiempo de salida del cliente
                # setea la servidor es desocupado
                self.tiempoSalidaCliente = fTiempo
                self.ocupado = False
                print('se atendio cliente')


class Cola:
	def __init__(self):
                # crea la lista que representara la cola de clientes
                self.colaDeCliente = []
	
	def cantClientes(self):
	        # devuelve la cantidad de clientes que hay en la cola
                return len(self.colaDeCliente)

	def llegaCliente(self,cCliente):
	        # agregar el cliente a la cola
                self.colaDeCliente.append(cCliente)
		
	def proximoCliente(self):
	        # devuelve el primer cliente de la cola (si hay alguno)
                return self.colaDeCliente.pop()

# clase base de los eventos 	
class Evento:
	def __init__(self, fTiempo):
	        # setea el tiempo de ocurrencia futura del evento
		self.instanteDeTiempoEnQueOcurre = fTiempo

	# metodo "lower than" para comparar 2 eventos
	def __lt__(self, other):
		return self.instanteDeTiempoEnQueOcurre < other.instanteDeTiempoEnQueOcurre
	
	# metodo "gerater than" para comparar 2 eventos
	def __gt__(self, other):
		return self.instanteDeTiempoEnQueOcurre > other.instanteDeTiempoEnQueOcurre

	# metodo abstracto (debe ser implementado por las subclases)
	def procesar(self):
		pass

#evento correspondiente a la futura finalizacion de atencion de un cliente por parte de un servidor
class EventoFinAtencion(Evento):
	
	def __init__(self, fTiempo, cServidor):
                #llama al constructor de la superclase
                #setea el servidor
                super().__init__(fTiempo)
                self.servidor = cServidor
                	
	def procesar(self):
	        # llama a servidor.finAtencion
                self.servidor.finAtencion(self.instanteDeTiempoEnQueOcurre)

#evento correspondiente a la futura llegada del proximo cliente
class EventoProximoCliente(Evento):
	def __init__(self, fTiempo, cSistema):
                #llama al constructor de la susperclase
                #setea el sistema (notar que recibe el sistema como parametro)
                super().__init__(fTiempo)
                self.sistema = cSistema
	
	def procesar(self):
	        # llama al callback sistema.ingresoCliente()
                self.sistema.avanzarTiempo(self.instanteDeTiempoEnQueOcurre) 
                print('llego cliente')
                self.sistema.ingresoCliente()
      
##arranca todo
#las personas llegan en promedio 2 por minuto, landa = 1/2
sistema = Sistema(0.5,[2,1.5,3])
sistema.procesar()