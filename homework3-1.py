import numpy  as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import matplotlib as mpl

pointx = [1,8,4,2,6]
pointy = [2,1,6,3,4]

def singal_effect(x, y, i):
    xp = pointx[i]
    yp = pointy[i]
    dis = (x - xp)**2 + (y -yp)**2
    return np.exp(-(dis))

x = np.arange(-10,10,0.1)
y = np.arange(-10,10,0.1)

X,Y = np.meshgrid(x,y)
Z = singal_effect(X, Y, 0)
size = len(Z)
Zfinal = [0]*size

for i in range(len(pointx)):
    Z = singal_effect(X, Y, i)
    for j in range(size):
        Zfinal[j] += Z[j]

plt.figure(figsize=(10,6))
plt.grid(True)
plt.contour(X,Y,Zfinal)
plt.scatter(pointx,pointy,s=10)
plt.show()
