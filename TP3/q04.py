# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x0 = 0
v0 = 10
w = 5
t0 = 0 
dt = 0.005
tmax = 10000

x=np.empty(tmax)                  
v=np.empty(tmax) 
x[0]=x0                             
v[0]=v0     

for i in range(1,tmax):
    x[i] = (x[i-1] + v[i-1]*dt)
    v[i] = (v[i-1]-x[i-1]*(w**2)*dt)

plt.plot(x)
plt.xlabel('temps')
plt.ylabel('position')
plt.title('q04')
plt.grid()
plt.savefig('q04.pdf')
plt.show()


