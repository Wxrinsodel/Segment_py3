import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 100)  
f_x = x * np.sin(2 * x)       # f(x) = x * sin(2*x)

#
plt.plot(x, f_x, label='f(x) = x * sin(2*x)', color='red')


plt.title('Graphs of f(x) = x * sin(2*x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.grid()
plt.show()
