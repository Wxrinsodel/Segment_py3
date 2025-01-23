import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 100)  
f_x1 = x**2        # f(x) = x^2 
f_x2 = x * np.sin(2 * x)  # f(x) = x * sin(2*x)
f_x3 = np.arctan(x)     # f(x) = arctan

#
plt.plot(x, f_x1, label='f(x) = x^2 ', color='green')
plt.plot(x, f_x2, label='f(x) = x * sin(2*x)', color='red')
plt.plot(x, f_x3, label='f(x) = arctg(x)', color='Blue')


plt.title('Graphs of f(x) = x^2, f(x) = x * sin(2*x), and f(x) = arctg(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.grid()
plt.show()
