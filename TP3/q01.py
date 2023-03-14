# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import math


# On fixe les valeurs par défaut

x0 = 1
k = 1
dt = 0.01
tmax = 10
npas = int(tmax/dt)


# On fixe les valeurs initiales
x=[x0]
t = [0]
exact=[x0]
diff=[0]

# Boucle pour la solution avec Euler
for i in range(npas-1):
    newT = t[-1] + dt
    newX = x[-1] - x[-1]*k*dt
    exactX = x0*math.exp((-newT)*k) # Pour la solution analytique
    difference = newX-exactX
    t.append(newT)
    x.append(newX)
    exact.append(exactX)
    diff.append(difference)   
                 
# On affiche les résultats
plt.subplot(2, 1, 1)
plt.plot(t, x, label='Approximation Euler')
plt.plot(t, exact, label='Solution analytique')
plt.xlabel('temps')
plt.ylabel('N(t)')
plt.title('q01')
plt.grid()
plt.legend()

plt.subplot(2,1,2)
plt.plot(t, diff, label = "Différence")
plt.grid()
plt.xlabel('temps')
plt.ylabel('Différence')

plt.savefig("q01.pdf")
plt.show()

