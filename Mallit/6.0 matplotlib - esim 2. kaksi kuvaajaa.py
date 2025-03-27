import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig = plt.figure()

ax1 = plt.subplot(2,1,1) #rivit, sarakkeet, monesko kuva
ax2 = plt.subplot(2,1,2)

ax1.grid()

ax1.plot(x,y1,color="r")
ax2.plot(x,y2,color="b")

ax1.set_title('Sini')
ax2.set_title('Kosini')

fig.tight_layout()

fig.savefig('tallennettu_kuva.png')
fig.show()

