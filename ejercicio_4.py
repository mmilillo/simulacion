import numpy as np

import matplotlib.pyplot as plt
from matplotlib import animation, rc
import math

class ParticleBox:
	def __init__(self,
				 init_state = [[1, 0, 0, -1],
							   [-0.5, 0.5, 0.5, 0.5],
							   [-0.5, -0.5, -0.5, 0.5]],
				 bounds = [-10, 1000, -10, 200],
				 size = 0.04):
		self.init_state = np.asarray(init_state, dtype=float)
		self.size = size
		self.state = self.init_state.copy()
		self.time_elapsed = 0
		self.bounds = bounds

	def step(self, dt):
		"""step once by dt seconds"""
		self.time_elapsed += dt

		# update positions, el 2 es sin incluir
		self.state[:, :2] += dt * self.state[:, 2:]

		cantidad_listas = int(self.state.size / 4)

		#inicializo matriz temporal
		mat_tmp = np.zeros((cantidad_listas, 16)) # Matriz de ceros
		mat_tmp[:,:4] = self.state[:,:]

		#actualizo estdos
		for i in range (0, cantidad_listas ): 
			x_p = self.state[i, 0]
			y_p = self.state[i, 1]
			vx_p = self.state[i, 2]
			vy_p = self.state[i, 3]

			no_es_x_p = self.state[:, 0] != self.state[i, 0]
			no_es_y_p = self.state[:, 1] != self.state[i, 1]

			es_x_p = self.state[:, 0] == self.state[i, 0]
			es_y_p = self.state[:, 1] == self.state[i, 1]

			choco_X_p = (abs(self.state[:, 0] - x_p)) <= (self.size *2) 
			choco_Y_p = (abs(self.state[:, 1] - y_p)) <= (self.size *2)

			puntos_a_modificar = choco_X_p & choco_Y_p & (no_es_x_p | no_es_y_p )

			### PASO 1 CONSEGUIR LAS COMPONENTES X E Y DE LA NORMAL ###

			#diferencia entre las componentes velocidad osea la normal
			mat_tmp[puntos_a_modificar , 4] = (self.state[puntos_a_modificar, 2] -  vx_p) #x
			mat_tmp[puntos_a_modificar , 5] = (self.state[puntos_a_modificar, 3] -  vy_p) #y

			### PASO 2 CONSEGUIR EL VECTOR UNITARIO NORMAL
			
			#la suma de los cuadrados de los componentes de la normal
			mat_tmp[puntos_a_modificar , 6] = (mat_tmp[puntos_a_modificar, 4] **2 +  mat_tmp[puntos_a_modificar, 5] ** 2)**(1.0/2)

			#componentes del verctor unitario normal
			mat_tmp[puntos_a_modificar , 7] = mat_tmp[puntos_a_modificar , 4] / mat_tmp[puntos_a_modificar , 6] #x
			mat_tmp[puntos_a_modificar , 8] = mat_tmp[puntos_a_modificar , 5] / mat_tmp[puntos_a_modificar , 6] #y

			### PUNTO 3 CONSEGUIR EL VECTOR UNITARIO TANGENCIAL
			# mat_tmp[puntos_a_modificar , 8] 		#x
			# mat_tmp[puntos_a_modificar , 7] *-1 	#y

			### PUNTO 4 CONSEGUIR LOS VECTORES DE VELOCIDAD INICIAL EN COMPONENTE X E Y (ya tenemos el dato)

			### PUNTO 5 PROYECCION NORMAL, es un escalar (multiplicadorNormal = velocidad p * Vun = (5,0) * (1,0) = 5)
			mat_tmp[puntos_a_modificar , 9] =  (mat_tmp[puntos_a_modificar , 2] * mat_tmp[puntos_a_modificar , 7]) + (mat_tmp[puntos_a_modificar , 3] * mat_tmp[puntos_a_modificar , 8])


			### PUNTO 5 PROYECCION tangencial, es un escalar (multiplicadorTangencial = velocidad p * Vtu = (5,0) * (0,-1) = 0)
			mat_tmp[puntos_a_modificar , 10] = (mat_tmp[puntos_a_modificar , 2] * mat_tmp[puntos_a_modificar , 8]) + (mat_tmp[puntos_a_modificar , 3] * mat_tmp[puntos_a_modificar , 7] * -1)

			### actualizo las velocidades finales depsues del choque
			# vpx = vectarTangencialx + normal de la otra particula x
			# vpy = vectarTangencialy + normal de la otra particula y

			## vector tangencial (x,y) = Vtp1 (escalar) * vut
			mat_tmp[puntos_a_modificar , 11] = mat_tmp[puntos_a_modificar , 8] * mat_tmp[puntos_a_modificar , 10] # x tangencial
			mat_tmp[puntos_a_modificar , 12] = mat_tmp[puntos_a_modificar , 7] * mat_tmp[puntos_a_modificar , 10] * -1 # y tangencial

			## vector normal (va el de la particula con la que choco) = componente normal (escalar) de la particula con la cual choco * Vun

			#esto seria la constante
			mat_tmp[puntos_a_modificar , 13] = (vx_p * mat_tmp[puntos_a_modificar , 7] ) + (vy_p * mat_tmp[puntos_a_modificar , 8])
			
			#componente de la velocidad en la direccion normal de la otra particula
			mat_tmp[puntos_a_modificar , 14] = mat_tmp[puntos_a_modificar , 13] * mat_tmp[puntos_a_modificar , 7] #x
			mat_tmp[puntos_a_modificar , 15] = mat_tmp[puntos_a_modificar , 13] * mat_tmp[puntos_a_modificar , 8] #y

			mat_tmp[puntos_a_modificar , 2] = mat_tmp[puntos_a_modificar , 11] + mat_tmp[puntos_a_modificar , 14]
			mat_tmp[puntos_a_modificar , 3] = mat_tmp[puntos_a_modificar , 12] + mat_tmp[puntos_a_modificar , 15]
		
		self.state = mat_tmp[:,:4]

#------------------------------------------------------------
# set up initial state
init_state = np.zeros((2,4),dtype=float)

#particula 1 
init_state[0, 0] = 50 #inicio en x
init_state[0, 1] = 50 # inicio en y
init_state[0, 2] = 0 #componente de x
init_state[0, 3] = 5 #componente de y

#particula 2 
init_state[1, 0] = 50 #inicio en x
init_state[1, 1] = 100 # inicio en y
init_state[1, 2] = 0 #componente de x
init_state[1, 3] = -1 #componente de y

box = ParticleBox(init_state, size=6)
dt = 1. / 30 # 30fps

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-10, 100), ylim=(-300, 300))
particles, = ax.plot([], [], 'bo', ms=5)

# initialization function: plot the background of each frame
def init():
	global box
	particles.set_data([], [])
	return particles,

# animation function.  This is called sequentially
def animate(i):
  global box, dt, ax, fig
  box.step(dt)

  particles.set_data(box.state[:, 0], box.state[:, 1])
  particles.set_markersize(5)
  return particles,
	

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=2, blit=True)
rc('animation', html='jshtml')
anim
plt.show()
