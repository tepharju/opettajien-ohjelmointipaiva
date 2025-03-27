# Satunnaiskävelijän havainnollistus

import matplotlib.pyplot as plt
import random

x = 0
y = 0

x_lista = [x]
y_lista = [y]

for i in range(10000):
    
    x = x + random.choice([-1,1])
    y = y + random.choice([-1,1])
    
    x_lista.append(x)
    y_lista.append(y)
    
fig, ax = plt.subplots()

ax.grid()

plt.scatter(x_lista,y_lista, marker=".")
plt.show()


