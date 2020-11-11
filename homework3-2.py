from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy

pointx = [1,8,4,2,6]
pointy = [2,1,6,3,4]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def singal_effect(x, y, i):
    xp = pointx[i]
    yp = pointy[i]
    # xp = 4
    # yp = 5
    dis = (x - xp)**2 + (y -yp)**2
    return numpy.exp(-(dis))

radise = 0
radis += singal_effect()


u = numpy.linspace(0, 2*numpy.pi, 100)
v = numpy.linspace(0, numpy.pi, 100)
x = numpy.outer(numpy.cos(u), numpy.sin(v))
y = numpy.outer(numpy.sin(u), numpy.sin(v))
z = numpy.outer(numpy.ones(numpy.size(u))*radise, numpy.cos(v))
# Make data
# x = 10 * np.outer(np.cos(u), np.sin(v))
# y = 10 * np.outer(np.sin(u), np.sin(v))
# z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
ax.plot_surface(x, y, z, color='b')

plt.show()