import matplotlib.pyplot as plt
import numpy as np
import math

e = math.e
print e

dx = 0.1
x = np.arange(-5, 5, dx)

y_e = e ** x
y_de = (e ** (x + dx) - e ** x) / dx

plt.plot(x, y_e)
plt.plot(x, y_de)
plt.show()
