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

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)


Z = X * Y

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis',)


fig.colorbar(surf, shrink=0.5, aspect=5)


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('f(x,y) = x*y')

plt.tight_layout()
plt.show()
