# Absorption de particules sur une surface
import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
import time
from numba import njit

L = 20.0  # Longueur du côté de la surface carrée
R = 0.4  # Rayon de la particule de gaz
MAX_TRIES = 10000  # Nombre d'essais invalides consécutifs nécéssaires pour l'arrêt de la simulation.
R_SURF = 0.05
U = 10.0


@njit
def collision(x1, y1, x2, y2, R, L):
    """
    Retourne True si les deux particules se touchent, False sinon.
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) < 2 * R


@njit
def coord(l, r):
    """
    Retourne une coordonnée aléatoire le long d'une ligne de longueur L.
    Les particules ayant un rayon R, il ne faut pas que la particule touche le bord de la surface.
    """
    # On choisit un nombre aléatoire entre 0 et 1. On multiplie ce nombre par la longueur de la ligne,
    # à laquelle on retire le diamètre de la particule pour retirer la zone où les particules toucheraient le bord.
    # On ajoute finalement le rayon au résultat final pour que les particules ne touchent pas le bord gauche.
    return (np.random.rand() * (L - 2 * R)) + R


@njit
def dist_latt(x, y):
    return math.sqrt((x - np.rint(x)) ** 2 + (y - np.rint(y)) ** 2)


def visualiser(x, y, n):
    circles = [plt.Circle((xi, yi), radius=R, linewidth=0, color="b") for xi, yi in zip(x, y)]
    c = matplotlib.collections.PatchCollection(circles)
    plt.scatter(x, y, s=1)  # nécessaire pour avoir les bons axes
    plt.axis("scaled")  # pour un avoir un carré et pas un rectangle
    plt.gca().add_collection(c)  # tracer la collection de cercles
    plt.savefig("visualisation.png")
    plt.show()

@njit
def remplissage_structure(l, r, max_tries, r_surf, u, t):
    n_max = math.floor((L ** 2) / (math.pi * (
                R ** 2)))  # Nombre de particules théorique maximum sur la surface. On arrondit à l'entier inférieur car on ne peut pas placer de parties de particules sur la surface.
    n = 0  # Nombre de particules sur la surface
    echecs = 0  # Nombre d'essais invalides consécutifs
    x = np.empty(n_max)  # Tableau des positions x des particules
    y = np.empty(n_max)  # Tableau des positions y des particules

    while echecs <= max_tries:
        x_new = coord(l, r)
        y_new = coord(l, r)
        libre = True
        for i in range(n):
            if collision(x_new, y_new, x[i], y[i], R, L):
                libre = False
                break
        if libre:
            # C'est cette partie qui change : cette fois ci on ajoute une condition de probabilité basée sur la position de la particule par rapport
            # aux atomes de la surface.
            # On calcule la distance entre la particule et l'atome
            distance = dist_latt(x_new, y_new)
            # Si la distance est inférieure à r_surf, la particule s'absorbe dans tous les cas, sinon on effectue un test de probabilités basé sur la température et u.

            if distance < r_surf or t * math.log(np.random.rand()) < -u:
                x[n] = x_new
                y[n] = y_new
                n += 1
                echecs = 0
            else:  # Sinon c'est un échec
                echecs += 1
        else:
            echecs += 1

    return x[:n], y[:n], n


def simulation_structure(l, r, max_tries, r_surf, u, m):
    start = time.time()
    print(
        f"Début d'une simulation de particules de rayon {r} sur une surface de longueur {l}. AVEC SURFACE STRUCTURÉE.")
    print(
        f"Le nombre maximal d'essais invalides consécutifs est {max_tries}. On effectue des simulations avec une température de 0°K à 10°K avec un pas de 0.5°K.")
    print(f"On effectue {m} simulations par pas de température.")

    moyennes = np.empty(20)
    temperatures = [i * 0.5 for i in range(0, 20)]
    for i in range(20):
        temperature = i * 0.5
        n_list = np.empty(m)
        for j in range(m):
            # print(f"Simulation pour {temperature}°K. Essai {j+1} sur {m}.")
            X, Y, N = remplissage_structure(l, r, max_tries, r_surf, u, temperature)
            n_list[j] = N
        n_mean = np.mean(n_list)
        moyennes[i] = n_mean

    end = time.time()
    print(f"Fin de la simulation. Temps d'exécution : {end - start} secondes.")
    # On effectue une courbe des moyennes d'espace occupé par rapport à la température.
    plt.plot(temperatures, moyennes)
    plt.xlabel("Température (°K)")
    plt.ylabel("Moyenne d'espace occupé par les particules")
    plt.title("courbe moyenne espace occupé")
    plt.savefig("graph10.png")
    plt.show()


simulation_structure(L, R, 10000, R_SURF, U, 100)