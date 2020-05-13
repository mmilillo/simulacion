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

		# update velocity
		#not_crossed_y = (self.state[:, 1] > 0)
		#self.state[not_crossed_y, 3] += dt * -9.8


		# update positions
		self.state[:, :2] += dt * self.state[:, 2:]

		# check for crossing boundary
		#crossed_x1 = (self.state[:, 0] < self.bounds[0] + self.size) indica si cruza ejex
		#crossed_x2 = (self.state[:, 0] > self.bounds[1] - self.size) indica si cruza ejex
		#crossed_y1 = (self.state[:, 1] < self.bounds[2] + self.size) indica si cruza eje y
		#crossed_y2 = (self.state[:, 1] > self.bounds[3] - self.size) indica si cruza eje y

		x_p1 = self.state[0, 0]
		y_p1 = self.state[0, 1]
		vx_p1 = self.state[0, 2]
		vy_p1 = self.state[0, 3]

		no_es_x_p1 = self.state[:, 0] != self.state[0, 0]
		no_es_y_p1 = self.state[:, 1] != self.state[0, 1]

		es_x_p1 = self.state[:, 0] == self.state[0, 0]
		es_y_p1 = self.state[:, 1] == self.state[0, 1]

		choco_X_p1 = (abs(self.state[:, 0] - x_p1)) <= (self.size *2 )
		choco_Y_p1 = (abs(self.state[:, 1] - y_p1)) <= (self.size *2 )

		#modifico velocidad de las que chocan con p1, componente x del vector
		self.state[choco_X_p1 & choco_Y_p1 & no_es_x_p1, 2] = (vx_p1 * -1)




		crossed_y = (self.state[:, 1] < 0)

		#self.state[crossed_x1 | crossed_x2, 2] *= -1
		#self.state[crossed_y1 | crossed_y2, 3] *= -1
		#self.state[impactoConParticulaUno, 2] =  self.state[0, 2]
		#self.state[impactoConParticulaDos, 2] =  self.state[1, 2]
		#self.state[crossed_y, 2] = 0 #lo frena en el eje x

		mat = np.array(self.state)


#------------------------------------------------------------
# set up initial state
init_state = np.zeros((2,4),dtype=float)

#particula 1 
init_state[0, 0] = 10 #inicio en x
init_state[0, 1] = 5 # inicio en y
init_state[0, 2] = 5 #componente de x
init_state[0, 3] = 0 #componente de y

#particula 2 
init_state[1, 0] = 20 #inicio en x
init_state[1, 1] = 0 # inicio en y
init_state[1, 2] = 0 #componente de x
init_state[1, 3] = 0 #componente de y

box = ParticleBox(init_state, size=2.5)
dt = 1. / 30 # 30fps

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-10, 300), ylim=(-10, 100))
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





