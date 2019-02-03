### DIEVAL Corentin REY Thibaud
### Pi approximation

# Imports
from random import random

import matplotlib.pyplot as plt
import math
import numpy as np

# Fonction Serie Inverses Carres
# 1.
from numpy.matlib import rand


def SerieInvCarrees(N):
    S = 0
    for k in range(1, N + 1):
        S += 1 / (k ** 2)
    return S


# 2.
def MethodeSerieInvCarres(N):
    s = SerieInvCarrees(N)
    return math.sqrt(6 * s)


# Fonction Serie Inverses Carres Impairs
# 3.
def SerieInvCarresImpairs(N):
    S = 0
    for k in range(0, N + 1):
        S += 1 / ((2 * k + 1) ** 2)
    return S


# 4.
def MethodeSerieInvCarresImpairs(N):
    s = SerieInvCarresImpairs(N)
    return math.sqrt(8 * s)


# 5.
# Representation de deux graphes : |MethodeSerieXXX(N) - PI|

def graph_method_xxx(min, max):
    x = np.arange(min, max + 1, 1)
    y1 = []
    y2 = []
    for k in range(min, max + 1):
        y1.append(MethodeSerieInvCarres(k))
        y2.append(MethodeSerieInvCarresImpairs(k))

    plt.plot(x, y1, y2)
    plt.show()


def method_serie_ramanujan(n):
    S = 0
    for k in range(0, n + 1):
        S += (math.factorial(4 * k) / math.factorial(k) ** 4) * (1103 + (26390 * k)) / (4 * 99) ** (4 * k)
    return ((2 * math.sqrt(2) / 9801) * S) ** (-1)


def monte_carlo(n):
    fig, ax = plt.subplots()
    k = 0

    for i in range(1, n + 1):
        x, y = random(), random()
        if x ** 2 + y ** 2 > 1:
            color = 'red'
        else:
            color = 'green'
            k += 1

        ax.scatter(x, y, c=color, s=10, label=color, alpha=1, edgecolors='none')

    # ax.legend()
    ax.grid(True)

    plt.show()
    return 4*k/n
