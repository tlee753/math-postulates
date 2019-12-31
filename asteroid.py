# amount of asteroids
# range of sizes
# range of map
    # round map to remove pi and only have scale factor with asteroid size
# distribution of impacts
    # uniform random
    # bell
    # power function

from random import randint
from math import sqrt
import numpy as np


mapRange = 20
asteroidSize = 2
asteroidAmount = int(mapRange**2/asteroidSize**2)
# print(asteroidAmount)
# ^ some function that will give me the same global coverage area based on scale factor between upper two params
# reliant on overlap, overlap factor probably scales well
# pi is factored out

impacts = []

c = 0

for i in range(asteroidAmount):
    while True:
        x = randint(0, mapRange)
        y = randint(0, mapRange)
        # r = randint(1, asteroidSize) # uniform random
        r = int(np.random.normal(0.5, 0.1, 1) * asteroidSize) # guassian

        if sqrt((x - mapRange/2)**2 + (y - mapRange/2)**2) < mapRange/2:
            break

    c += 1
    v = c # cluster identifier
    
    impacterView = [x, y, r, v]

    for impact in impacts:
        ival1 = sqrt((x - impact[0])**2 + (y - impact[1])**2)
        ival2 = float(r + impact[2])
        if ival1 <= ival2:
            if impact[3] < v:
                for i in range(len(impacts)):
                    if impacts[i][3] == v:
                        impacts[i][3] = impact[3]      # fix these three lines    
            if v < impact[3]:
                for i in range(len(impacts)):
                    if impacts[i][3] == impact[3]:
                        impacts[i][3] = v
            

    impacts.append( [x, y, r, v] )



import matplotlib.pyplot as plt

plt.figure(figsize=(15,10))
ax = plt.gca()
colors = ["pink", "red", "orange", "yellow", "green", "cyan", "blue", "purple", "gray", "brown", "black"]

for impact in impacts:
    circle = plt.Circle((impact[0], impact[1]), color=colors[impact[3]%len(colors)], radius=impact[2])
    ax.add_patch(circle)

plt.axis('scaled')
plt.show()

