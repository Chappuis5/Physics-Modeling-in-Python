# TP2
# Marches aléatoires

# 2.1 : Nombres aléatoires

from turtle import width
import numpy as np
import matplotlib.pyplot as plt
import math

rng = np.random.default_rng(seed=12345)
for i in range(10):
    print(rng.random())
for i in range(10):
    print(rng.integers(low=1, high=6,endpoint=True))

# 2) Il est souhaitable et important de pouvoir reproduire les séquences de nombres aléatoires afin de garantir une reproductibilité des résultats.

print("------------------------------------------------------")

rng = np.random.default_rng()
for i in range(10):
    print(rng.random())
for i in range(10):
    print(rng.integers(low=1, high=6,endpoint=True))

# 3) On constate que retirer l'argument de la seed force numpy �  générer une graine aléatoire �  chaque fois, ne permettant pas d'assurer la reproductibilité des séquences d'une exécution �  l'autre du programme.


# 4)
def nombre_aleatoire(min, max):
    return rng.random() * (max - min) + min

print("------------------------------------------------------")

for i in range(10):
    print(nombre_aleatoire(1, i))

print("------------------------------------------------------")

# 5)
def pile_ou_face():
    return -1 if rng.random() < 0.5 else 1

print("------------------------------------------------------")

for i in range(10):
    print(pile_ou_face())

print("------------------------------------------------------")

# 2.2 : Marches aléatoires

# 2.2.1 : Marche aléatoire �  pas discrets

# 6)

rng = np.random.default_rng(seed=12345)
def simulation_marche_10_pas():
    # creates a numpy array of 10 elements picked randomly from 1 or -1 without any loop
    steps = np.where(rng.integers(2, size=10)==0, -1, 1)
    # adds a zero at the beginning of the array
    steps = np.insert(steps, 0, 0)
    # creates another array containing the position of the walker at each step
    sum = np.cumsum(steps)
    # display the final position 
    print(f"Final position : {sum[-1]}")
    return sum

# nparr = simulation_marche_10_pas()
# print(nparr)
# plt.plot(nparr)
# plt.xlabel("pas")
# plt.ylabel("position")
# plt.show()

# 7)
def simulation_marche_x_pas(npas):
    # creates a numpy array of x elements picked from the pile_ou_face function
    steps = np.where(rng.integers(2, size=npas)==0, -1, 1)
    # adds a zero at the beginning of the array
    steps = np.insert(steps, 0, 0)
    # creates another array containing the position of the walker at each step
    sum = np.cumsum(steps)
    # display the final position 
    print(f"Final position : {sum[-1]}")
    return sum


nparr = simulation_marche_x_pas(30)
print(nparr)
plt.plot(nparr)
plt.xlabel("pas")
plt.ylabel("position")
# plt.show() # uncomment this line to display the plot.

# On constate bel et bien que la marche aléatoire est la même en utilisant une graine fixée.

# 8)
print("------------------------------------------------------")

def marche(npas):
    steps = np.where(rng.integers(2, size=npas)==0, -1, 1)
    sum = np.cumsum(steps)
    return sum[-1] # returns final position

rng = np.random.default_rng()

def etude_marche(NMARCHES, npas):
    positions = np.array([marche(npas) for i in range(NMARCHES)])
    print(positions)

    mean = 1/NMARCHES * np.sum(positions)
    avg = math.sqrt( 1/NMARCHES * np.sum((positions - mean)**2) - mean**2)

    print(f"Etude de {NMARCHES} marches aléatoires de {npas} pas:")
    # print(mean, avg) # print and standard deviation "by hand"
    print(np.mean(positions), np.std(positions)) # print and standard deviation with numpy

etude_marche(10000, 10)

# on constate bien que nos calculs reproduisent bien les résultats des fonctions numpy.mean et numpy.std.

# etude_marche(10000, 50)
# etude_marche(10000, 100)
# etude_marche(10000, 200)
# etude_marche(10000, 400)
# etude_marche(10000, 800)
# etude_marche(10000, 1600)
# etude_marche(10000, 3200)
# etude_marche(10000, 6400)

# On constate que plus on augmente le nombre de pas, plus l'écart-type augmente. On constate également que la moyenne s'éloigne globalement de plus en plus de zéro.

def histogramme(NMARCHES, npas):
    positions = np.array([marche(npas) for i in range(NMARCHES)])
    plt.clf()
    plt.title(f"Probabilité de finir sur une position x\n pour une marche aléatoire de {npas} pas.")
    plt.hist(positions, bins=positions.size, density=True, width=1)
    plt.xlabel("Position")
    plt.ylabel("Probabilité")
    plt.show()

# histogramme(1000, 100)
# histogramme(1000, 200)
# histogramme(1000, 400)

# On constate que cette distribution tend vers une loi normale quand n augmente.


# 2.2.2 : Marche aléatoire �  pas continus

# 12)

print("------------------------------------------------------")

def marche_pas_aleatoire(npas):
    # creates a numpy array containing random values between -1 and 1
    steps = rng.random(size=npas) * 2 - 1
    print(steps)
    # adds a zero at the beginning of the array
    steps = np.insert(steps, 0, 0)
    # creates another array containing the position of the walker at each step
    sum = np.cumsum(steps)
    # display the final position 
    print(f"Final position : {sum[-1]}")
    return sum

# plt.clf()
# nparr = marche_pas_aleatoire(30)
# print(nparr)
# plt.plot(nparr)
# plt.xlabel("pas")
# plt.ylabel("position")
# plt.show()


def marche_pas_lorentz(npas):
    # creates a numpy array containing random values between -1 and 1 distributed according to a Lorentzian distribution
    steps = rng.standard_cauchy(size=npas) * 2 - 1
    print(steps)
    # adds a zero at the beginning of the array
    steps = np.insert(steps, 0, 0)
    # creates another array containing the position of the walker at each step
    sum = np.cumsum(steps)
    # display the final position 
    print(f"Final position : {sum[-1]}")
    return sum

plt.clf()
nparr = marche_pas_lorentz(1000)
plt.plot(nparr)
plt.xlabel("pas")
plt.ylabel("position")
# plt.show()


# la distribution obtenue grâce �  la loie de Lorentz voit apparaître de grosses perturbations de temps �  autre, l�  où les autres distributions sont plus prévisibles.

# 2.3 : Pour aller plus loin 

# 15)

def marche_pas_gaussienne(npas):
    steps = rng.normal(loc=0, scale=1, size=npas)

    steps = np.insert(steps, 0, 0)
    sum = np.cumsum(steps)
    print(f"Final position : {sum[-1]}")
    return sum

plt.clf()
nparr = marche_pas_gaussienne(1000)
plt.plot(nparr)
plt.xlabel("pas")
plt.ylabel("position")
# plt.show()


def histogramme_gaussien(NMARCHES, npas):
    positions = np.array([marche_pas_gaussienne(npas)[-1] for i in range(NMARCHES)])
    plt.clf()
    plt.title(f"Probabilité de finir sur une position x\n pour une marche aléatoire de {npas} pas.")
    plt.hist(positions, bins=positions.size, density=True, width=1)
    plt.xlabel("Position")
    plt.ylabel("Probabilité")
    plt.show()

# histogramme_gaussien(1000, 1000)

print("------------------------------------------------------")


# 16)

def marche_2d(npas):
    # Let's create an array containing random values between "L", "R", "U" and "D"
    steps = rng.choice(["L", "R", "U", "D"], size=npas)
    # "L" => x - 1
    # "R" => x + 1
    # "U" => y + 1
    # "D" => y - 1
    # Admitting starting position is 0,0, let's calculate the final position of the walker
    countL = np.count_nonzero(steps == "L")
    countR = np.count_nonzero(steps == "R")
    countU = np.count_nonzero(steps == "U")
    countD = np.count_nonzero(steps == "D")
    x = countL - countR
    y = countU - countD
    print(f"Final position : {x}, {y}")
    distance = np.sqrt(x**2 + y**2)
    print(f"Distance : {distance}")
    return x, y

def scatter_2d(NMARCHES, npas):
    """
    On décide d'utiliser un scatter plot pour cette représentation.
    """
    arrays = np.array([marche_2d(npas) for i in range(NMARCHES)])
    arrX = arrays[:, 0]
    arrY = arrays[:, 1]
    plt.clf()
    plt.title(f"Distribution des positions finales (x,y)\n pour {NMARCHES} marches aléatoires de {npas} pas.")
    plt.scatter(arrX, arrY)
    plt.xlabel("Position x")
    plt.ylabel("Position y")
    plt.show()

# scatter_2d(1000, 10000)

# création d'un programme qui simule deux marches aléatoires en 2D : une avec une répartition uniforme (Autant de chances d'avoir n'importe quelle valeur entre -1 et 1)
# et une avec une répartition de Lorentz.
# Dans ce programme, on ne fonctionne plus avec des pas discrets (valeur dans {-1, 1}), mais avec des pas contenus dans [-1, 1] selon une certaine répartition.
# Comme on utilise plus de pas discrets, on admet donc que le point se déplace dans les deux directions �  chaque pas.


def comparaison_trajectoire(npas):
    # répartition uniforme
    stepsX = rng.random(size=npas) * 2 - 1
    stepsY = rng.random(size=npas) * 2 - 1
    posX = np.cumsum(stepsX)
    posY = np.cumsum(stepsY)

    # répartition de Lorentz
    stepsX = rng.standard_cauchy(size=npas) * 2 - 1
    stepsY = rng.standard_cauchy(size=npas) * 2 - 1
    posX2 = np.cumsum(stepsX)
    posY2 = np.cumsum(stepsY)

    plt.clf()
    plt.title(f"Comparaison des trajectoires\n pour {npas} pas.")
    plt.subplot(1, 2, 1)
    plt.plot(posX, posY, label="Trajectoire uniforme")
    plt.scatter(posX[-1], posY[-1], label="Position finale", color="red")
    plt.xlabel("Position x")
    plt.ylabel("Position y")
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(posX2, posY2, label="Trajectoire de Lorentz")
    plt.scatter(posX2[-1], posY2[-1], label="Position finale", color="red")
    plt.xlabel("Position x")
    plt.ylabel("Position y")
    plt.legend()
    plt.show()

comparaison_trajectoire(1000)
