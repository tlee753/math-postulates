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

import matplotlib.pyplot as plt

plt.figure(figsize=(15,10), facecolor="black")
ax = plt.gca()

ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white') 
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.yaxis.label.set_color('white')
ax.xaxis.label.set_color('white')
ax.title.set_color('white')
ax.set_facecolor('xkcd:black')
colors = ["magenta", "red", "orange", "goldenrod", "green", "violet", "blue", "purple", "gray", "brown", "teal"]



mapRange = 20
asteroidSize = 3
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

    properlyAdded = False
    while not properlyAdded:

        properlyAdded = True

        for i in range(len(impacts)):
            ival1 = sqrt((x - impacts[i][0])**2 + (y - impacts[i][1])**2)
            ival2 = float(r + impacts[i][2])
            if ival1 <= ival2:
                if impacts[i][3] < v:
                    v = impacts[i][3]
                    properlyAdded = False
                elif v < impacts[i][3]:
                    for j in range(len(impacts)):
                        if impacts[j][3] == impacts[i][3]:
                            impacts[j][3] = v
                    properlyAdded = False

        impacts.sort(key = lambda x:x[3])
        # print(impacts)
            

    impacts.append( [x, y, r, v] )
    circle = plt.Circle((x, y), color=colors[v%len(colors)], radius=r)
    ax.add_patch(circle)
    ax.text(x, y, v, color="white")    
    plt.axis('scaled')
    plt.savefig("hello.jpg")
#    plt.show()


