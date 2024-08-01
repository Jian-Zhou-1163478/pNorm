import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg, inf

v = [inf, 2, 1]  #
v = [inf,20,10,5,3,2,1,0.7,0.5,0.4,0.3,0.2,0.1,0.001]

scalar=5
v = [inf,20]
v1=np.linspace(10, 2, 10*scalar)
v2=np.linspace(2, 1, 5*scalar)
v0=np.linspace(1, 0, 10*scalar)
v.extend(v1)
del v[-1]
v.extend(v2)
del v[-1]
v.extend(v0)

#v = [inf, 2, 1] #, 0.5, 0.3, 0.1]
#print(v)
L = len(v)
if L > 13:
    L = 13

def scale_up(x, y=3):
    return x+scalar*0.005


def plotUnitCircle(v):
    """ plot some 2D vectors with p-norm < 1 """
    plt.axis('equal')
    plt.axhline(0, color='black', alpha=.5, dashes=[2, 4], linewidth=1)
    plt.axvline(0, color='black', alpha=0.5, dashes=[2, 4], linewidth=1)
    w1 = np.linspace(-1, 1, 250)
    w2 = np.linspace(-1, 1, 250)
    min_v = min(v)
    max_v = max(v)
    patch = []
    for i, p in enumerate(v):
        if p == inf:
            c = 0  # 1-((p-min_v)/(max_v-min_v))
        else:
            c = i/(len(v)-1) #1 - ((p - min_v) / 20)  # (max_v-min_v))
        print(i, p, c)
        if len(patch) <= L and i % (round(len(v)/L)) == 0:
            patch.append(mpatches.Patch(color=(c, c, c), label=str(p)[0:4]))
        for value1 in w1:
            for value2 in w2:
                x = np.array((value1, value2))
                temp = linalg.norm(x, p)
                if temp < 1:
                    if p > 10:
                        if temp > 0.95: #scale_up(0.95,0.05):
                            plt.plot(x[0], x[1], marker='.', color=(c, c, c), alpha=1.0)
                    elif p > 1:
                        if temp > scale_up(0.9):
                            plt.plot(x[0], x[1], marker='.', color=(c, c, c), alpha=1.0)
                    elif p > 0.5:
                        if temp > scale_up(0.85):
                            plt.plot(x[0], x[1], marker='.', color=(c, c, c), alpha=1.0)
                    elif p > 0.3:
                        if temp > scale_up(0.6,5):
                            plt.plot(x[0], x[1], marker='.', color=(c, c, c), alpha=1.0)
                    else:
                        plt.plot(x[0], x[1], marker='.', color=(c, c, c), alpha=1.0)
    # ([-1.5, 1.5, -1.5, 1.5])
    plt.legend(handles=patch)
    plt.show()


# print(len(v)//L)
'''
Uncomment below to execute the plot function. Be cautious!
This programme is able to consume up to 20G mem for some scalar value.
'''
#plotUnitCircle(v)
#print(L,round(len(v) / L))
