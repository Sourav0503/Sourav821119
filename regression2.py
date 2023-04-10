import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
x = np.linspace(0, 100, 101)
y = 0.1*np.exp(0.3*x) + 0.1*np.random.random(len(x))
plt.figure(figsize = (20,16))
plt.plot(x, y, 'b.')
plt.xlabel('x')
plt.ylabel('y')
plt.show()