import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import keyboard

#### OBJECTIVES ####

# 1 establish the stability in the phase space of ants, birds, and cats
# 2 establish reasonable values of constants in differential equations
# 3 vary cat and bird initial conditions to minimise piss over time

#### /OBJECTIVES ###

# simulation
dt = 0.1				# timestep (unit = days)
ae = 100					# anteater population
time = 0				# current time in simulation

# variables
ants = 1E6					# population of ants
birds = 100					# population of birds
cats = 5					# population of cats
piss = 1.5E6					# quantity of piss (ml)

# constants
A = 1E-3				# prob of a bird eating an ant per unit time
B = 1E-3				# prob of an anteater eating an ant per unit time
C = 1E-6				# 1/ amount of piss per unit time required per ant to reproduce
D = 5E-5				# prob of a bird being eaten by a cat per unit time
E = 5E-7				# 1/ number of ants per unit time required per bird to reproduce
F = 6E-5				# 1/ number of birds per unit time required per cat to reproduce
G = 0.075				# calorific requirements of a cat per unit time (in units of birds)
H = 1000				# piss output per cat per unit time
I = 200					# piss output per anteater per unit time
J = 0.01				# piss consumption per ant per unit time

K = 0.1E1 				# calorific requirements of a bird per unit time (in units of ants)
L = 0.01				# calorific requirements of a ant per unit time (in units of piss)
M = 10					# piss output per bird

fig = plt.figure(figsize=(12,9))

ax = fig.add_subplot(211, projection='3d')
ax2 = fig.add_subplot(212)

fig2 = plt.figure(figsize=(7,12))
ants_plot = fig2.add_subplot(311)
bird_plot = fig2.add_subplot(312)
cats_plot = fig2.add_subplot(313)

ants_plot.set_ylabel('Ant population',fontsize=16,labelpad=10)
bird_plot.set_ylabel('Bird population',fontsize=16,labelpad=10)
cats_plot.set_ylabel('Cat population',fontsize=16,labelpad=10)
cats_plot.set_xlabel('Time',fontsize=16,labelpad=10)

ax.set_xlabel('Ant population',fontsize=16,labelpad=10)
ax.set_ylabel('Bird population',fontsize=16,labelpad=10)
ax.set_zlabel('Cat population',fontsize=16,labelpad=10)

ax2.set_xlabel('Time',fontsize=16)
ax2.set_ylabel('Piss',fontsize=16)

plt.ion()
plt.show()

while time < 500:

	ants += ((piss*C - A*birds - B*ae - L)*ants)*dt
	birds += (E*ants - D*cats - K)*birds*dt
	cats += (F*birds*cats - G*cats)*dt
	piss += (H*cats + I*ae + M*birds - J*ants - 0.01*piss)*dt

	if ants < 0: ants = 0
	if birds < 0: birds = 0
	if cats < 0: cats = 0
	if piss < 0: piss = 0

	timeprint = '%s' % float('%.1g' % time)
	print('time=',timeprint,' ants=',ants,' birds=',birds,' cats=',cats,' piss=',piss)

	ax.scatter(ants,birds,cats,color='crimson',s=5)
	ax2.scatter(y=piss,x=time,color='brown',s=1)

	ants_plot.scatter(y=ants,x=time,color='black',s=1)
	bird_plot.scatter(y=birds,x=time,color='blue',s=1)
	cats_plot.scatter(y=cats,x=time,color='orange',s=1)

	plt.pause(0.01)

	time += dt

