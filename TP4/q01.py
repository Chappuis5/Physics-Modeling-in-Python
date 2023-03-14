import numpy as np
import matplotlib.pyplot as plt
from rk4 import rk4

###PARAMETRES###
q = [1, 2, 5]
y0 = np.radians(10)
v0 = 0
t0 = 0
dt = 0.05
tmax = 20
npas = int((tmax - t0) / dt) + 1
t = np.linspace(t0, tmax, npas)

def deriv(t, y, params):
    dy = np.empty_like(y)
    dy[0] = y[1]
    dy[1] = -params[0] * y[1] + params[1] * y[0] #Equation linéarisée
    return dy


for x in q: #boucle pour parcourir la liste de valeurs d'amortissement
    params = [x, -1]
    y = np.empty((2, npas))
    y[0, 0] = y0
    y[1, 0] = v0

    for i in range(1, npas):
        y[:, i] = rk4(i, dt, y[:, i - 1], deriv, params)

    plt.plot(t, y[0, :], label="q = ""{0}".format(x))
    plt.title("Evolution de θ(t) en fonction de différentes valeurs d'amortissement")
    plt.xlabel('temps')
    plt.ylabel('theta(t)')
    plt.grid()
    plt.legend()
    plt.savefig('graph01.pdf')
plt.show()
