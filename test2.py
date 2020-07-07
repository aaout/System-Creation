import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def func0(x, y):
    return -x - 1/2 * y + 4
def func1(x, y):
    return -2 * x - y + 6
def func2(x, y):
    return - 3/2 * x - 3 * y + 9

x = np.arange(-10, 10, 0.5)
y = np.arange(-10, 10, 0.5)

X, Y = np.meshgrid(x, y)
Z_0 = func0(X, Y)
Z_1 = func1(X, Y)
Z_2 = func2(X, Y)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
ax.plot_wireframe(X, Y, Z_0, color = 'red')
ax.plot_wireframe(X, Y, Z_1, color = 'blue')
ax.plot_wireframe(X, Y, Z_2, color = 'green')
plt.show()
