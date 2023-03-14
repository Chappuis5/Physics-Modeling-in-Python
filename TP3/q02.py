# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x0 = 500
k1 = 1
t0=0 
dt = 0.1
tmax = 10
npas = int(tmax/dt)


t = np.arange(t0,tmax+dt, dt) # Variation du temps
t2=np.linspace(t0, tmax, npas+1) 
x=np.empty(len(t)) # Concentrations
x[0]=x0 # Concentration initiale
                                     


for i in range(len(t)-1):
    x[i + 1] = (x[i] - x[i]*k1*dt)

analytique = x0*np.exp(-t)

plt.plot(t, x, label="Methode d'Euler")
plt.plot(t, analytique, label='Solution analytique')
plt.xlabel('temps')
plt.ylabel('N(t)')
plt.title('q02')
plt.grid()
plt.legend()
plt.savefig('q02.pdf')
plt.show()


