# Este es un programa de ejemplo de cómo debería incorporarse la visualización del sistema de Teoría de Colas desarrollado en la primera parte del TP
# Modificar y completar todo lo que consideren necesario

import time
import curses
from curses import wrapper
import TP4P1
import TCparte2

#inicialize curses
#stdscra = curses.initscr()

def imprimirTitulo(screen):
	screen.addstr(0,0,'Servidores (X = ocupado, " " = desocupado)')
	print("prueba")
	
def imprimirDatos(screen, estadistica, sistema):
	servidores = 100
	
	fila = 1
	columna = 1
	for i in range(servidores):
		screen.addstr(fila,columna,'{:02d}: |   | '.format(i))
		if fila % 20 == 0:
			fila = 1
			columna += 20
		else:
			fila += 1
		
	screen.addstr(22,0,'Cantidad de clientes en espera (en la cola): {}'.format(sistema.cantidadActualClientesEnCola()))
	screen.addstr(23,0,'Cantidad de mediciones: {}'.format(estadistica.cantMediciones))
	screen.addstr(24,0,'Tiempo global: {}'.format(sistema.tiempoGlobal))
	screen.addstr(26,0,'L: {}'.format(estadistica.L()))
	screen.addstr(27,0,'Lq: {}'.format(estadistica.Lq()))
	screen.addstr(26,50,'W: {}'.format(estadistica.W()))
	screen.addstr(27,50,'Wq: {}'.format(estadistica.Wq()))
		

def actualizarEstadoServidores(screen,servidores):
	#servidores = 100
	fila = 1
	columna = 7

	for servidor in servidores:
		if servidor.estaOcupado():
			screen.addstr(fila,columna,'X')
		else: 
			screen.addstr(fila,columna,' ')
		if fila % 20 == 0:
			fila = 1
			columna += 20
		else:
			fila += 1


def iniciar(screen):
	#1) inicialización de variables	

	arrayServidores = []
	for i in range(100):
		arrayServidores.append(20)

	#2.1) crear instancia de estadistica
	estadistica = TCparte2.Estadistica()

	#2.2) crear instancia de sistema	
	sistema = TP4P1.Sistema(100,arrayServidores)

	#3) llegada 1er. cliente
	#sistema.ingresoCliente()
	sistema.crearEventoProximoCliente()

	imprimirTitulo(screen)	

	#imprimirDatos(screen, estadistica, sistema)
	
	terminar = False
	
	i = 0
	while(not terminar):
		screen.nodelay(True)

		sistema.procesar()

		estadistica.procesar(sistema)	

		imprimirDatos(screen, estadistica, sistema)

		actualizarEstadoServidores(screen,sistema.listaServidores)
		

		time.sleep(0.5)
		
		i += 1
		#terminar con la tecla "f"
		if (screen.getch() == ord('f')):
			terminar = True

wrapper(iniciar)
