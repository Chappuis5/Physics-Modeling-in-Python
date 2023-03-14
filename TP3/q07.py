# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# Méthode d'Euler

# Première étape : fonction deriv

def deriv_elec(t, y):
   dy = np.empty(4)
   dy[0] = (1 + y[1])
   dy[1] = -y[0]
   dy[2] = y[0]
   dy[3] = y[1]
   return dy


# Deuxième étape : fonction Euler

def euler(y, t, dt, deriv):
    dy = deriv(t,y)
    y = y + dy*dt
    return y

t0=0 
dt = 0.01
tmax = 100

npas = int((tmax-t0) / dt) + 1
t = np.linspace(t0, tmax, npas)


# Programme complet pour l'oscillateur harmonique

y = np.empty((4,npas))
y[0,0] = 10
y[1,0] = 5
y[2,0] = 5
y[3,0] = 10

for i in range(1, npas): 
    y[:,i] = euler(y[:,i-1], i, dt, deriv_elec) # calcul de la position et de la vitesse
    
    
# affichage de la trajectoire
plt.figure()
plt.plot(y[2,:], y[3,:])
plt.title('q07')
plt.grid()
plt.savefig('q07.pdf')
plt.show()