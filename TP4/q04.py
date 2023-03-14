import numpy as np
import matplotlib.pyplot as plt
from rk4 import rk4


y0 = np.radians(10)
y02 = np.radians(9.999)
v0 = 0
v02 = 0
t0 = 0
dt = 0.05
tmax = 100
npas = int((tmax - t0) / dt) + 1
t = np.linspace(t0, tmax, npas)


def deriv(t, y, params):
    dy = np.empty_like(y)
    dy[0] = y[1]
    dy[1] = -params[0] * y[1] - params[1] * np.sin(y[0]) + params[2] * np.sin(params[3] * t)
    return dy


params = [0.5, 1, 1.5, 2/3]
y = np.empty((2, npas))
y[0, 0] = y0
y[1, 0] = v0
y1 = np.empty((2, npas))
y1[0, 0] = y02
y1[1, 0] = v02

for i in range(1, npas):
    y[:, i] = rk4(t[i], dt, y[:, i - 1], deriv, params)
    y1[:, i] = rk4(t[i], dt, y1[:, i - 1], deriv, params)
    if y[0, i] < -np.pi:
        y[0, i] = y[0, i] + 2 * np.pi
    elif y[0, i] > np.pi:
        y[0, i] = y[0, i] - 2 * np.pi
    if y1[0, i] < -np.pi:
        y1[0, i] = y1[0, i] + 2 * np.pi
    elif y1[0, i] > np.pi:
        y1[0, i] = y1[0, i] - 2 * np.pi
    diff = np.absolute(y[0] - y1[0])

plt.semilogy(t, diff, "-")

plt.suptitle("Valeur absolue de la différence entre les deux theta(t)")
plt.title("Echelle semi-logarithmique")
plt.xlabel('temps')
plt.ylabel('theta(t)')
plt.grid()
plt.legend()
plt.savefig('graph04.pdf')
plt.show()
