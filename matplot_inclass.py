import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)  
f_x = x**2          # f(x) = x^2 

plt.plot(x, f_x, label='f(x) = x^2', color='blue')

plt.title('Graphs of f(x) = x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.grid()
plt.show()
