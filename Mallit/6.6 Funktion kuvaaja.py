import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 9, 1000)
y = np.sqrt(x)

fig = plt.figure() # uusi kuvaympäristö

ax = plt.subplot() # lisätään kuvaan koordinaatisto

ax.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x,y)
ax.set_title('y = sqrt(x)')

fig.show()

