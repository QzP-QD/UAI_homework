#画出He从0到正无穷（10000）变化时的形状变化

import numpy as np
import matplotlib.pyplot as plt
from time import time

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = True

def updateXY(He):
    Ex = 0
    En = 1
    n = 5000
    Y = np.zeros((1, n))
    np.random.seed(int(time()))
    X = np.random.normal(loc=En, scale=He, size=n)
    Y = Y[0]
    for i in range(n):
        np.random.seed(int(time()) + i + 1)
        Enn = X[i]
        X[i] = np.random.normal(loc=Ex, scale=np.abs(Enn), size=1)
        Y[i] = np.exp(-(X[i] - Ex) * (X[i] - Ex) / (2 * Enn * Enn))

    return X,Y

fig = plt.figure(len(plt.get_fignums()))
ax = fig.add_subplot(1, 1, 1)

plt.ion()
for i in range(200):
    plt.cla()
    He = i*5
    X, Y = updateXY(He)
    title = '期望:%.2f,熵:%.2f,超熵:%.2f,云滴数:%d' % (0, 1, He, 500)
    plt.title(title)

    plt.xlim((-1000, 1000))
    plt.ylim((0, 1))

    plt.grid(True)
    plt.scatter(X, Y, s=5, alpha=0.5, c='r', marker='o', label='云图1')
    plt.pause(0.02)

plt.ioff()
plt.show()
