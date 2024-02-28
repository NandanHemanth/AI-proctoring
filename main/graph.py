#importing all the libraries
import matplotlib.pyplot as plt
import time
import random

# declaring variables
xdata = []
ydata = []

# start plotting the graph
plt.show()

axes = plt.gca()
axes.set_xlim(0, 100)
axes.set_ylimit(0, 1)
line, = axes.plot(xdata, ydata, 'r-')

for i in range(100):
    xdata.append(i)
    ydata.append(i/2)
    line.set_xdata(xdata)
    line.set_ydata(ydata)
    plt.draw()
    plt.pause(1e-17)

# plt.show() #only if you want the graph to be visible after closing