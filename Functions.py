### DIEVAL Corentin Rey Thibaud
### Pi approximation

# Imports
import matplotlib.pyplot as plt
import math
import numpy as np


# Fonction Serie Inverses Carres
# 1.
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
    x = np.arange(min, max+1, 1)
    y1 = []
    y2 = []
    for k in range(min, max + 1):
        y1.append(MethodeSerieInvCarres(k))
        y2.append(MethodeSerieInvCarresImpairs(k))

    plt.plot(x, y1, y2)
    plt.show()
