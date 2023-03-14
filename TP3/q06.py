# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


#Méthode de Euler

# Première étape : fonction deriv
def deriv(t, y , w):
   dy = np.empty(2) # Création d'un tableau de taille 2
   dy[0] = y[1] 
   dy[1] = -w**2*y[0]*dt # acceleration de l'oscillateur harmonique
   return dy 


# Deuxième étape : fonction euler
def euler(y, t, dt, deriv, w):
    dy = deriv(t,y,w)
    y = y + dy*dt # Un seul pas de temps
    return y

 
# paramètres initiaux
y0 =0
v0=10
w=5
t0=0 
dt = 0.01
tmax = 50


# Création du tableau temps
npas = int((tmax-t0) / dt) + 1 # nombre de pas
t = np.linspace(t0, tmax, npas) # tableau de temps

# Programme complet pour l'oscillateur harmonique


# construction des tableaux et initialisation de paramètres
y = np.empty((2, npas))
y[0,0] = y0
y[1,0] = v0

for i in range(1, npas): # boucle sur les pas de temps
    y[:,i] = euler(y[:,i-1], i, dt, deriv, -w**2) # calcul de la position et de la vitesse
    
# affichage de la trajectoire
plt.figure()
plt.plot(t, y[0,:])
plt.xlabel('temps')
plt.ylabel('position')
plt.title('q06')
plt.grid()
plt.savefig('q06.pdf')
plt.show()
   



    
    


                                     


