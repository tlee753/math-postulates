def onSegment(p, q, r):
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    return False


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    if (val == 0):
        return 0
    
    if val > 0:
        return 1
    else:
        return 2


def doIntersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if (o1 != o2 and o3 != o4):
        return True

    if (o1 == 0 and onSegment(p1, p2, q1)):
        return True

    if (o2 == 0 and onSegment(p1, q2, q1)):
        return True

    if (o3 == 0 and onSegment(p2, p1, q2)):
        return True

    if (o4 == 0 and onSegment(p2, q1, q2)):
        return True

    return False
    


from random import randint

maxX = 100
maxY = 100
iterations = 1000

connections = []

for _ in range(iterations):
    p1 = (randint(0, maxX), randint(0, maxY))
    q1 = (randint(0, maxX), randint(0, maxY))

    # check if the points all differ

    intersectBool = False
    for connection in connections:
        if doIntersect(p1, q1, connection[0], connection[1]):
            intersectBool = True

    if not intersectBool:
        connections += [[p1, q1]]
    
print(len(connections))

import pylab as pl
from matplotlib import collections as mc

lines = [[(0, 1), (1, 1)], [(2, 3), (3, 3)], [(1, 2), (1, 3)]]

lc = mc.LineCollection(connections, linewidths=2)
fig, ax = pl.subplots()
ax.add_collection(lc)
ax.autoscale()

pl.show()


"""
connect two random points
biological limit?

"""