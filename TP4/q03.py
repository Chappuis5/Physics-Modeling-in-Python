import numpy as np
import matplotlib.pyplot as plt
from rk4 import rk4

###PARAMETRES###
f = [1.4, 1.44, 1.465, 1.5]
y0 = np.radians(10)
v0 = 0
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


for x in f:
    params = [0.5, 1, x, 2/3]
    y = np.empty((2, npas))
    y[0, 0] = y0
    y[1, 0] = v0

    for i in range(1, npas):
        y[:, i] = rk4(t[i], dt, y[:, i - 1], deriv, params)
        if y[0, i] < -np.pi:
            y[0, i] = y[0, i] + 2 * np.pi
        elif y[0, i] > np.pi:
            y[0, i] = y[0, i] - 2 * np.pi


    plt.plot(t, y[0, :], label="f = ""{0}".format(x))
    plt.title("q03")
    plt.xlabel('temps(s)')
    plt.ylabel('theta(rad)')
plt.grid()
plt.legend()
plt.savefig('graph03.pdf')
plt.show()
