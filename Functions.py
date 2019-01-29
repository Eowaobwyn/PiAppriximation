### DIEVAL Corentin Rey Thibaud
### Pi approximation

#Imports
import numpy as np
import matplotlib.pyplot as plt
import math


# Fonction Serie Inverses Carrés
# 1.
def SerieInvCarrees(N):
    S = 0
    for k in range(1, N+1):
        S += 1/(k**2)
    return S

# 2.
def MethodeSerieInvCarres(N):
    s = SerieInvCarrees(N)
    return math.sqrt(6*s)

# Fonction Serie Inverses Carrés Impairs
# 3.
def SerieInvCarresImpairs(N):
    S = 0
    for k in range(0, N+1):
        S += 1/((2*k+1)**2)
    return S

# 4.
def MethodeSerieInvCarresImpairs(N):
    s = SerieInvCarresImpairs(N)
    return math.sqrt(8*s)

# 5.
# Représentation de deux graphes : |MethodeSerieXXX(N) - PI|

def GraphMethodeXXX(min, max):
    x = []
    for k in range(min, max+1):
        x.append(k)
    y = MethodeSerieInvCarres(x)
    plt.plot(x, y)
    plt.show()

