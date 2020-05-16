import numpy as np

import matplotlib.pyplot as plt
from matplotlib import animation, rc

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

		# update positions
		self.state[:, :2] += dt * self.state[:, 2:]

		cantidad_listas = int(self.state.size / 4)

		#inicializo matriz temporal
		mat_tmp = np.zeros((cantidad_listas, 8)) # Matriz de ceros
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
			choco_Y_p = (abs(self.state[:, 1] - y_p)) <= (self.size *2 )

			#punto_a_actualizar = choco_X_p & choco_Y_p & (no_es_x_p | no_es_Y_p )
			### PASO 1 CONSEGUIR LAS COMPONENTES X E Y DE LA NORMAL ###

			#diferencia entre las componentes x de velocidad
			mat_tmp[choco_X_p & choco_Y_p & (no_es_x_p | no_es_y_p ) , 4] = (self.state[choco_X_p & choco_Y_p & no_es_x_p, 2] -  vx_p)

			#diferencia entre las componentes y de velocidad
			mat_tmp[choco_X_p & choco_Y_p & (no_es_x_p | no_es_y_p ) , 5] = (self.state[choco_X_p & choco_Y_p & no_es_x_p, 3] -  vy_p)

			### PASO 2 CONSEGUIR EL VECTOR UNITARIO NORMAL
			#mat_tmp[choco_X_p & choco_Y_p & (no_es_x_p | no_es_Y_p ) , 6] = 

		print(mat_tmp)

		self.state = mat_tmp[:,:4]

#------------------------------------------------------------
# set up initial state
init_state = np.zeros((2,4),dtype=float)

#particula 1 
init_state[0, 0] = 50 #inicio en x
init_state[0, 1] = 5 # inicio en y
init_state[0, 2] = 5 #componente de x
init_state[0, 3] = 0 #componente de y

#particula 2 
init_state[1, 0] = 100 #inicio en x
init_state[1, 1] = 5 # inicio en y
init_state[1, 2] = -1 #componente de x
init_state[1, 3] = 0 #componente de y

box = ParticleBox(init_state, size=0.125)
dt = 1. / 30 # 30fps

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-10, 300), ylim=(-10, 10))
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





