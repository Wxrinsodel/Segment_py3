import matplotlib.pyplot as plt
import numpy as np

"""
x = np.linspace(-10, 10, 100)  
f_x1 = x**2        # f(x) = x^2 
f_x2 = x * np.sin(2 * x)  # f(x) = x * sin(2*x)
f_x3 = np.arctan(x)     # f(x) = arctan

#
plt.plot(x, f_x1, label='f(x) = x^2 ', color='green', linestyle='solid', marker='_')
plt.plot(x, f_x2, label='f(x) = x * sin(2*x)', color='red', linestyle='dashed', marker='_')
plt.plot(x, f_x3, label='f(x) = arctg(x)', color='Blue', linestyle='dotted', marker='_')


plt.title('Graphs of f(x) = x^2, f(x) = x * sin(2*x), and f(x) = arctg(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.grid()
plt.show()

"""

bars = np.loadtxt('values_for_bars.csv', delimiter=',')


unique, counts = np.unique(bars, return_counts=True)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(unique, counts)
plt.title('Bar Plot of Unique Values')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()