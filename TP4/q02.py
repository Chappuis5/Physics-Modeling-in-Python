import numpy as np
import matplotlib.pyplot as plt
from rk4 import rk4

###PARAMETRES###
q = [0, 1, 1]
f = [0, 0, 1]
y0 = np.radians(10)
v0 = 0
t0 = 0
dt = 0.05
tmax = 20
npas = int((tmax - t0)/dt) + 1
t = np.linspace(t0, tmax, npas)


def deriv(t, y, params):
    dy = np.empty_like(y)
    dy[0] = y[1]
    dy[1] = -params[0] * y[1] - params[1] * y[0] + params[2] * np.sin(params[3] * t)
    return dy


for x, z in zip(q, f): #On parcourt les deux listes simultanément
    params = [x, 1, z, 2/3]
    y = np.empty((2, npas))
    y[0, 0] = y0
    y[1, 0] = v0

    for i in range(1, npas):
        y[:, i] = rk4(t[i], dt, y[:, i - 1], deriv, params)

    plt.plot(y[0,:], y[1,:], label = f'q = {x}, Fe = {z}')
    plt.suptitle("Trajectoire dans l'espace des phases")
    plt.title("Pendule libre, amorti, et amorti avec excitation")
    plt.xlabel("theta(t)'")
    plt.ylabel("theta(t)")
    plt.grid()
    plt.legend()
    plt.savefig('graph02.pdf')
plt.show()



