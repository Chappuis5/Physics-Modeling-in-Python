import numpy as np
import matplotlib.pyplot as plt
from rk4 import rk4

###PARAMETRES###
fmin = 2.55
fmax = 2.9
y0 = (10*np.pi)/180
v0 = 0
t0 = 0
dt = (2 * np.pi)/(200 * 2/3)
df = 0.005
tmin = 20
nb_min = int(tmin / dt)+1
iterations = 100
npas = int((fmax - fmin) / df) + 1
npas2 = nb_min + iterations * 200
t = np.arange(0, npas2 * dt, dt)

force = np.zeros((npas, iterations))

f = fmin
ct = 0

valeurs = np.zeros((npas, iterations))

def deriv(t, y, params):
    dy = np.empty_like(y)
    dy[0] = y[1]
    dy[1] = -params[0] * y[1] - params[1] * np.sin(y[0]) + params[2] * np.sin(params[3] * t)
    return dy

while f < fmax:
    index = 0
    force[ct, :] = f
    params = [0.5, 1, f, 2 / 3]
    y = np.empty((2, npas2))
    y[0, 0] = y0
    y[1, 0] = v0

    for i in range(1, npas2):

        y[:, i] = rk4(t[i], dt, y[:, i - 1], deriv, params)

        if y[0, i] < -np.pi:
            y[0, i] = y[0, i] + 2 * np.pi

        elif y[0, i] > np.pi:
            y[0, i] = y[0, i] - 2 * np.pi

        elif i > nb_min:
            if i % 200 == 0:
                valeurs[ct, index] = y[0, i]
                index = index + 1
    ct = ct + 1
    f = f + df

plt.figure()
plt.scatter(force, valeurs, marker='.', alpha=0.5)
plt.xlabel('f(N)')
plt.ylabel('theta()')
plt.axhline(y=0, color='k', linestyle=':')
plt.title('Diagramme de bifurcation')
plt.grid()


plt.savefig('graph05.pdf')
plt.show()
