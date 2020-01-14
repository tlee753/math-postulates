from vpython import *
from random import random


scene.width = 1920
scene.height = 1080
# scene.range = 1e8
scene.autoscale = 1
# scene.autozoom = 1
scene.autocenter = 1

numAsteroids = 100
mapBound = 1e8
velBound = 1e4
arrowScalar = 1e-18
gravConstant = 6.674e-11

colors = [color.white, color.magenta, color.cyan, color.green, color.yellow, color.orange, color.red]

class Asteroid():
    def __init__(self, id):
        self.mass = 1e25
        self.radius = 6.4e6
        self.id = 0
        self.collisions = 0

        self.x = random()*mapBound*2 - mapBound
        self.y = random()*mapBound*2 - mapBound 
        self.z = random()*mapBound*2 - mapBound

        self.xVel = random()*velBound*2 - velBound
        self.yVel = random()*velBound*2 - velBound
        self.zVel = random()*velBound*2 - velBound

        self.velocity = vector(self.xVel, self.yVel, self.zVel)
        self.momentum = self.velocity * self.mass
        
        self.sphere = sphere(pos=vector(self.x, self.y, self.z), radius=self.radius)
        self.forceArrow = arrow(pos=self.sphere.pos, axis=vector(0,0,0), color=color.green)

        self.vecForce = vector(0,0,0)

debree = []
for i in range(numAsteroids):
    debree.append(Asteroid(i+1))

deltaT = 10
t = 0
while t < 10000000:
    rate(1000)

    for d1 in debree:
        if d1.mass == 0:
            continue
        d1.vecForce = vector(0, 0, 0)

        for d2 in debree:
            if d2.mass == 0:
                continue
            if d1.sphere.pos == d2.sphere.pos:
                continue
            pos = d1.sphere.pos - d2.sphere.pos
            magPos = mag(pos)
            if magPos < d1.sphere.radius:
                d1.mass += d2.mass
                d1.collisions += d2.collisions + 1
                d1.sphere.color = colors[d1.collisions%len(colors)]
                d2.mass = 0
                d2.sphere.visible = False
                d2.forceArrow.visible = False
                continue
            d1.vecForce += (-gravConstant*d1.mass*d2.mass*(pos/magPos))/(magPos**2) 

        d1.momentum += d1.vecForce*deltaT  
        d1.velocity = d1.momentum/d1.mass 
        d1.sphere.pos += d1.velocity*deltaT
        # d1.forceArrow.pos = d1.sphere.pos
        # d1.forceArrow.axis = d1.vecForce*arrowScalar

    t += deltaT

print("fin")
