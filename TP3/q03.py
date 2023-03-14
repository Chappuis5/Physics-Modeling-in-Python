# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# Paramètres initiaux
x0 = 1
y0 = 0
k1 = 1
k2 = 0.1*k1
t0 = 0 
dt = 0.2
tmax = 20
npas = int(tmax/dt)

t = np.arange(t0,tmax + dt, dt)
x=np.empty(len(t))
y=np.empty(len(t)) 
x[0]=x0
y[0]=0     
                                     

# Boucle Euler

for i in range(len(t)-1):
    x[i + 1] = (x[i] - x[i]*k1*dt)
    y[i+1] = (y[i]+x[i]*k1*dt-y[i]*k2*dt)


analytique = (k1*x0)*((np.exp(-k1*t))-np.exp(-k2*t))/(k2-k1)
                 
plt.plot(t, x, label='x')
plt.plot(t, y, label='y')
plt.plot(t, x0*np.exp(-k1*t), 'k', label='analytique x')
plt.plot(t, analytique, 'k', label='analytique y')
plt.xlabel('temps')
plt.ylabel('N(t)')
plt.title('q03')
plt.grid()
plt.legend()
plt.savefig('q03.pdf')
plt.show()


