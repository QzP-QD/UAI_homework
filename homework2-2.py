#两个云端模型均固定期望和熵，按照相同补偿增加超熵，动态变化

import numpy as np
import matplotlib.pyplot as plt
from time import time

def plot_cloud_model(Ex, En, He, n, num, color=''):
    # Ex = 0      # 期望
    # En = 1      # 熵
    # He = 0.1    # 超熵
    # n = 500     # 云滴个数

    Y = np.zeros((1, n))
    np.random.seed(int(time()))
    X = np.random.normal(loc=En, scale=He, size=n)
    Y = Y[0]

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = True

    fig = plt.figure(len(plt.get_fignums()))
    ax = fig.add_subplot(1, 4, num + 1)

    for i in range(n):
        np.random.seed(int(time()) + i + 1)
        Enn = X[i]
        X[i] = np.random.normal(loc=Ex, scale=np.abs(Enn), size=1)
        Y[i] = np.exp(-(X[i] - Ex) * (X[i] - Ex) / (2 * Enn * Enn))

    ax.scatter(X, Y, s=5, alpha=0.5, c=color, marker='o', label='云图1')
    title = '期望:%.2f,熵:%.2f,超熵:%.2f,云滴数:%d' % (Ex, En, He, n)
    ax.set_title(title)
    ax.legend(loc='best')
    ax.set_xlabel('指标值')
    ax.set_ylabel('确定度')
    ax.grid(True)
    plt.show()

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def updateX(He):
    Ex = 0
    En = 1
    n = 1000
    np.random.seed(int(time()))
    X1 = np.random.normal(loc=En, scale=He, size=n)
    X2 = np.random.normal(loc=En, scale=He, size=n)
    for i in range(n):
        np.random.seed(int(time()) + i + 1)
        Enn1 = X1[i]
        Enn2 = X2[i]
        X1[i] = np.random.normal(loc=Ex, scale=np.abs(Enn1), size=1)
        X2[i] = np.random.normal(loc=Ex, scale=np.abs(Enn2), size=1)

    return X1,X2

fig = plt.figure(len(plt.get_fignums()))
ax = fig.add_subplot(1, 1, 1)

plt.ion()
for i in range(200):
    plt.cla()
    He = i
    X1,X2= updateX(He)

    title = '期望:%.2f,熵:%.2f,超熵:%.2f,云滴数:%d' % (0, 1, He, 500)
    plt.title(title)
    plt.grid(True)

    plt.scatter(X1, X2, s=5, alpha=0.5, c='r', marker='o', label='云图1')
    plt.pause(0.02)

plt.ioff()
plt.show()
