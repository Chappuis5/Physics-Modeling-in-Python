# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
#from numba import njit
import time

start = time.time()

#@njit
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

#@njit
def deriv(t, y , w):
   dy = np.empty(2, dtype=np.float64)
   dy[0] = y[1]
   dy[1] = -w**2*y[0]*dt
   return dy
 
y0 = 1
v0 = 1
w = 5
t0 = 0 
dt = 0.01
tmax = 50

npas = int((tmax-t0) / dt) + 1
t = np.linspace(t0, tmax, npas, dtype=np.float64)


y = np.empty((2,npas), dtype=np.float64)
y[0,0] = y0
y[1,0] = v0



#@njit
def calcul_position():
    for i in range(1, npas):
         y[:,i] = rk4(y[:,i-1], i, dt, deriv, -w**2)
    return y[0,:]


pos=calcul_position()

end=time.time()
duree = end-start
print("Temps d'execution : ", duree)

plt.plot(t,pos, label='rk4')
plt.xlabel('temps')
plt.ylabel('erreur')
plt.title('q12')
plt.grid()
plt.legend()
plt.savefig('q12.pdf')
plt.show()