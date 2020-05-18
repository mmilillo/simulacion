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
		not_crossed_y = (self.state[:, 1] > 0)
		self.state[not_crossed_y, 3] += dt * -9.8


		# update positions
		self.state[:, :2] += dt * self.state[:, 2:]

		# check for crossing boundary
		#crossed_x1 = (self.state[:, 0] < self.bounds[0] + self.size)
		#crossed_x2 = (self.state[:, 0] > self.bounds[1] - self.size)
		#crossed_y1 = (self.state[:, 1] < self.bounds[2] + self.size)
		#crossed_y2 = (self.state[:, 1] > self.bounds[3] - self.size)
		crossed_y = (self.state[:, 1] < 0)
		

		#self.state[crossed_x1 | crossed_x2, 2] *= -1
		#self.state[crossed_y1 | crossed_y2, 3] *= -1
		self.state[crossed_y, 3] = 0 #lo frena en el eje y
		self.state[crossed_y, 2] = 0 #lo frena en el eje x

		mat = np.array(self.state)


#------------------------------------------------------------
# set up initial state
init_state = np.zeros((1,4),dtype=float)

#arranca de 50 m de altura 
# dispara a 200ms cn aguno de 30°
# sin(30) = cat op / hip (200 ms) = 100 ms = componente en  y
# cos(30) = cat adj / hip (200 ms) = 172 ms = componente en  x

init_state[0, 0] = 0 #inicio en x
init_state[0, 1] = 50 # inicio en y
init_state[0, 2] = 172 #componente de x
init_state[0, 3] = 100 #componente de y

box = ParticleBox(init_state, size=2.5)
dt = 1. / 30 # 30fps

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-10, 5000), ylim=(-10, 1000))
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
                               frames=800, interval=2, blit=True)
rc('animation', html='jshtml')
anim
plt.show()