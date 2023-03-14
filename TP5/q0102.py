import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np

L = 20.0 # Longueur du côté de la surface carrée
R = 0.4 # Rayon de la particule de gaz
MAX_TRIES = 1000 # Nombre d'essais invalides consécutifs nécéssaires pour l'arrêt de la simulation.


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

def visualiser(x, y, n):
    circles = [plt.Circle((xi, yi), radius=R, linewidth=0, color="b") for xi, yi in zip(x, y)]
    c = matplotlib.collections.PatchCollection(circles)
    plt.scatter(x, y, s=1)  # nécessaire pour avoir les bons axes
    plt.axis("scaled")  # pour un avoir un carré et pas un rectangle
    plt.gca().add_collection(c)  # tracer la collection de cercles
    plt.title("graph0102")
    plt.savefig("graph0102.png")
    plt.show()

X, Y, N = remplissage(L, R, MAX_TRIES)
print(N)
visualiser(X, Y, N)

