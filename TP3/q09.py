
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#Méthode d'Euler

# Première étape : fonction deriv

def deriv(t, y , w):
   dy = np.empty(2)
   dy[0] = y[1]
   dy[1] = -w**2*y[0]*dt
   return dy


# Deuxième étape : fonction d'euler

def euler(y, t, dt, deriv, w):
    dy = deriv(t,y,w)
    return ( y + dy*dt )

y0 =1
v0=1
w=5
t0=0 
dt = 0.001
tmax =15

npas = int((tmax-t0) / dt) + 1 # nombre de pas
t = np.linspace(t0, tmax, npas) # tableau de temps


y = np.empty((2,npas)) # construction des tableaux et initialisation de paramètres
y[0,0] = y0 
y[1,0] = v0

for i in range(1, npas): # boucle sur les pas de temps
    y[:,i] = euler(y[:,i-1], i, dt, deriv, -w**2) # calcul de la position et de la vitesse

erreur = y[:i]-np.cos(np.sqrt(w)*t) # erreur relative

plt.subplot(2,1,1)
plt.plot(t,y[0,:],label='Euler dt=0,001')
plt.plot(t, np.cos(np.sqrt(w)*t), label='Solution exacte')
plt.xlabel('temps')
plt.ylabel('erreur')
plt.title('q09')
plt.grid()
plt.legend()
plt.subplot(212)
plt.plot(t,erreur[0,:],label='erreur')
plt.xlabel('temps')
plt.ylabel('erreur')

plt.grid()
plt.legend()

plt.savefig('q09.pdf')
plt.show()