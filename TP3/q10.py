# -*- coding: utf-8 -*-

from q08 import rk2
import numpy as np
import matplotlib.pyplot as plt

def deriv(t, y , w):
   dy = np.empty(2)
   dy[0] = y[1]
   dy[1] = -w**2*y[0]*dt
   return dy

y0 =1
v0=1
w=5
t0=0 
dt = 0.01
tmax = 10

npas = int((tmax-t0) / dt) + 1 # nombre de pas
t = np.linspace(t0, tmax, npas) # vecteur des temps


y = np.empty((2,npas)) # construction des tableaux et initialisation de paramètres
y[0,0] = y0 
y[1,0] = v0


for i in range(1, npas): # boucle sur les pas de temps
    y[:,i] = rk2(y[:,i-1], i, dt, deriv, -w**2) # calcul de la position et de la vitesse

analytique = np.cos(np.sqrt(w)*t)
erreur = y[:i]-analytique # erreur relative

plt.subplot(2,1,1)
plt.plot(t,y[0,:],label='rk2')
plt.plot(t, analytique, label='Solution analytique')
plt.xlabel('temps')
plt.ylabel('erreur')
plt.title('q10')
plt.grid()
plt.legend()
plt.subplot(2,1,2)
plt.plot(t,erreur[0,:],label='erreur')
plt.xlabel('temps')
plt.ylabel('erreur')
plt.grid()
plt.legend()
plt.savefig('q10.pdf')
plt.show()