# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def rk4(y, t, dt, deriv, params):
    """
      /*-----------------------------------------
      sous programme de resolution d'equations
      differentielles du premier ordre par
      la methode de Runge-Kutta d'ordre 4
      x = abscisse, une valeur scalaire, par exemple le temps
      dx = pas, par exemple le pas de temps
      y = valeurs des fonctions au temps t(i), c'est un tableau numpy de taille n
      avec n le nombre d'équations différentielles du 1er ordre
      
      rk4 renvoie les nouvelles valeurs de y pour t(i+1)
      
      deriv = variable contenant le nom du
      sous-programme qui calcule les derivees
      deriv doit avoir trois arguments: deriv(x,y,params) et renvoyer 
      un tableau numpy dy de taille n 
      ----------------------------------------*/
    """
    #  /* d1, d2, d3, d4 = estimations des derivees
    #    yp = estimations intermediaires des fonctions */  
    ddt = dt/2.0       #         /* demi-pas */
    d1 = deriv(t,y,params)   #       /* 1ere estimation */          
    yp = y + d1*ddt
    #    for  i in range(n):
    #        yp[i] = y[i] + d1[i]*ddx
    d2 = deriv(t+ddt,yp,params)     #/* 2eme estimat. (1/2 pas) */
    yp = y + d2*ddt    
    d3 = deriv(t+ddt,yp,params)  #/* 3eme estimat. (1/2 pas) */
    yp = y + d3*dt    
    d4 = deriv(t+dt,yp,params)     #  /* 4eme estimat. (1 pas) */
    #/* estimation de y pour le pas suivant en utilisant
    #  une moyenne ponderee des derivees en remarquant
    #  que : 1/6 + 1/3 + 1/3 + 1/6 = 1 */
    return y + dt*( d1 + 2*d2 + 2*d3 + d4 )/6  


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
    y[:,i] = rk4(y[:,i-1], i, dt, deriv, -w**2) # calcul de la position et de la vitesse

analytique = np.cos(np.sqrt(w)*t)
erreur = y[:i]-analytique # erreur relative

plt.subplot(2,1,1)
plt.plot(t,y[0,:],label='rk4')
plt.plot(t, analytique, label='Solution analytique')
plt.xlabel('temps')
plt.ylabel('erreur')
plt.title('q11')
plt.grid()
plt.legend()
plt.subplot(2,1,2)
plt.plot(t,erreur[0,:],label='erreur')
plt.xlabel('temps')
plt.ylabel('erreur')
plt.grid()
plt.legend()
plt.savefig('q11.pdf')
plt.show()