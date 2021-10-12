import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.9, 0.95, 0.01)
f = x**3 + 12*x - 12

plt.plot(x,f)
plt.grid(True)
plt.show()
