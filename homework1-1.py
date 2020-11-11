#画出云模型点阵图和收敛曲线（动态）————He在小于En/3附近有效果

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
    Y = Y[0]  # 什么作用？？？

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
plt.rcParams['axes.unicode_minus'] = True

def updateXY(He):
    Ex = 0
    En = 1
    n = 5000
    Y = np.zeros((1, n))
    Y1 = np.zeros((1, n))
    Y2 = np.zeros((1, n))
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
    He = i/10
    X,Y= updateXY(He)

    X1 = np.linspace(-10,10,100)
    Y1 = np.exp(-(X1 - 0)**2 / (2 * (1 + 3 * He)**2))
    Y2 = np.exp(-(X1 - 0)**2 / (2 * (1 - 3 * He)**2))

    title = '期望:%.2f,熵:%.2f,超熵:%.2f,云滴数:%d' % (0, 1, He, 500)
    plt.title(title)
    plt.xlim((-10, 10))
    plt.ylim((0, 1))
    plt.grid(True)

    plt.plot(X1, Y1,label='linear')
    plt.plot(X1, Y2,label='quadratic')
    plt.scatter(X, Y, s=5, alpha=0.5, c='r', marker='o', label='云图1')
    plt.pause(0.02)

plt.ioff()
plt.show()
