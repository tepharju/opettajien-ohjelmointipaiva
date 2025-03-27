# Satunnaiskävelijän havainnollistus 3D

import matplotlib.pyplot as plt
import random

x = 0
y = 0
z = 0

x_lista = [x]
y_lista = [y]
z_lista = [z]

for i in range(2000):
    
    x = x + random.choice([-1,1])
    y = y + random.choice([-1,1])
    z = z + random.choice([-1,1])
    
    x_lista.append(x)
    y_lista.append(y)
    z_lista.append(z)
    
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(x_lista,y_lista, z_lista, marker = ".")
plt.show()


