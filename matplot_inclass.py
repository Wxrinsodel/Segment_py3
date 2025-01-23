import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 100)  
f_x = np.arctan(x)     # f(x) = arctan

#
plt.plot(x, f_x, label='f(x) = arctg(x)', color='red')


plt.title('Graphs of f(x) = arctg(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.grid()
plt.show()
