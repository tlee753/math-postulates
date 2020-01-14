from random import randint
from math import sqrt
import numpy as np


mapRange = 200
asteroidSize = int(sqrt(mapRange))
asteroidAmount = int(mapRange**2/asteroidSize**2)

impacts = []

for i in range(asteroidAmount):
    while True:
        x = randint(0, mapRange)
        y = randint(0, mapRange)
        # r = randint(1, asteroidSize) # uniform random
        r = int(np.random.normal(0.5, 0.1, 1) * asteroidSize) # guassian

        if sqrt((x - mapRange/2)**2 + (y - mapRange/2)**2) < mapRange/2:
            break

    impacts.append( [x, y, r, i] )
    impacts.sort(key = lambda x:x[3])

    properlyAdded = False
    while not properlyAdded:
        properlyAdded = True

        for j in impacts:
            for k in impacts:
                dist = sqrt((j[0] - k[0])**2 + (j[1] - k[1])**2)
                combRad = j[2] + k[2]

                if dist <= combRad:
                    if j[3] == k[3]:
                        continue
                    elif j[3] < k[3]:
                        k[3] = j[3]
                        properlyAdded = False
                    else:
                        j[3] = k[3]
                        properlyAdded = False


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
colors = ["magenta", "red", "orange", "gold", "chocolate", "green", "violet", "blue", "purple", "gray", "silver", "maroon", "brown", "teal", "pink", "beige", "navy", "white", "lime", "cyan", "lightgreen"]

for impact in impacts:
    circle = plt.Circle((impact[0], impact[1]), color=colors[impact[3]%len(colors)], radius=impact[2])
    ax.add_patch(circle)
    ax.text(impact[0], impact[1], impact[3], color="white")
    
plt.axis('scaled')
plt.show()
