#统计正向正态云模型中云滴所占比例

import numpy as np
from time import time

def plot_cloud_model(Ex, En, He, n):
    # Ex = 0      # 期望
    # En = 1      # 熵
    # He = 0.1    # 超熵
    # n = 500     # 云滴个数

    Y = np.zeros((1, n))
    np.random.seed(int(time()))
    X = np.random.normal(loc=En, scale=He, size=n)
    Y = Y[0]  # 什么作用？？？

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for i in range(n):
        np.random.seed(int(time()) + i + 1)
        Enn = X[i]
        X[i] = np.random.normal(loc=Ex, scale=np.abs(Enn), size=1)
        Y[i] = np.exp(-(X[i] - Ex) * (X[i] - Ex) / (2 * Enn * Enn))

        if (Ex-0.67*En) <= X[i] <= Ex+0.67*En :
            count1 += 1
            count2 += 1
        elif Ex-En <= X[i] <= Ex+En :
            count2+=1
        elif (Ex-2*En <= X[i] <= Ex-En) | (Ex+En <= X[i] <= Ex+2*En):
            count3+=1
        elif (Ex-3*En <= X[i] <= Ex-2*En) | (Ex+2*En <= X[i] <= Ex+3*En):
            count4+=1

    rate1 = count1 / n
    rate2 = count2 / n
    rate3 = count3 / n
    rate4 = count4 / n

    return rate1, rate2,rate3,rate4

rate1, rate2,rate3,rate4 = plot_cloud_model(0,1,0.2,5000)
print("骨干元素[Ex-0.67En，Ex+0.67En]内云滴对定性概念的贡献为：",rate1*100,"%  （期望贡献度：22.33%）")
print("基本元素[Ex-En，Ex+En]内云滴对定性概念的贡献为：",rate2*100,"%  （期望贡献度：33.33%）")
print("外围元素[Ex-2En，Ex-En]和[Ex+En，Ex+2En]内云滴对定性概念的贡献为：",rate3*100,"%  （期望贡献度：27.18%）")
print("弱外围元素[Ex-3En，Ex-2En] 和[Ex+2En，Ex+3En]内云滴对定性概念的贡献为：",rate4*100,"%  （期望贡献度：4.3%）")
