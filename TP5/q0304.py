import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
import time

L = 20.0  # Longueur du côté de la surface carrée
R = 0.4  # Rayon de la particule de gaz
MAX_TRIES = 1000  # Nombre d'essais invalides consécutifs nécéssaires pour l'arrêt de la simulation.


def collision(x1, y1, x2, y2, R, L):
    """
    Retourne True si les deux particules se touchent, False sinon.
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) < 2 * R


def coord(l, r):
    """
    Retourne une coordonnée aléatoire le long d'une ligne de longueur L.
    Les particules ayant un rayon R, il ne faut pas que la particule touche le bord de la surface.
    """
    # On choisit un nombre aléatoire entre 0 et 1. On multiplie ce nombre par la longueur de la ligne,
    # à laquelle on retire le diamètre de la particule pour retirer la zone où les particules toucheraient le bord.
    # On ajoute finalement le rayon au résultat final pour que les particules ne touchent pas le bord gauche.
    return (np.random.rand() * (L - 2 * R)) + R


def remplissage(l, r, max_tries):
    n_max = math.floor((L ** 2) / (math.pi * (
                R ** 2)))  # Nombre de particules théorique maximum sur la surface. On arrondit à l'entier inférieur car on ne peut pas placer de parties de particules sur la surface.
    # print("Nombre de particules théorique maximum sur la surface:", n_max)

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
            x[n] = x_new
            y[n] = y_new
            n += 1
            echecs = 0
        else:
            echecs += 1

    return x[:n], y[:n], n


def simulation(l, r, max_tries, m):
    start = time.time()
    print(f"Début d'une simulation de particules de rayon {r} sur une surface de longueur {l}.")
    print(f"Le nombre maximal d'essais invalides consécutifs est {max_tries}. On effectue {m} simulations.")
    n_list = np.empty(m)
    for i in range(m):
        print(f"simulation n°{i + 1}/{m}")
        x, y, n = remplissage(l, r, max_tries)
        n_list[i] = n
    n_mean = np.mean(n_list)
    moyenne_fraction_surface = n_mean * math.pi * r ** 2 / l ** 2
    total_time = time.time() - start
    print(
        f"Fin de la simulation.\nTemps total: {round(total_time, 3)} secondes.\nNombre moyen de particules sur la surface: {n_mean}.")
    print(f"Moyenne de la fraction de surface occupée par les particules: {moyenne_fraction_surface}.")

    # calculer l'écart-type
    ecart_type = np.std(n_list)
    print(f"Ecart-type: {ecart_type}.")
    # écart type de la fraction de surface occupée par les particules
    ecart_type_fraction_surface = ecart_type * moyenne_fraction_surface
    print(f"Ecart-type de la fraction de surface occupée par les particules: {ecart_type_fraction_surface}.")

    return moyenne_fraction_surface


mfs = simulation(L, R, MAX_TRIES, 20)