from vpython import *
from random import random


scene.width = 1920
scene.height = 1080
scene.range = 1e8
scene.autoscale = 0

mapBound = 1e8
velBound = 1e8
sizeScalar = 1e10
gravConstant = 6.674e-11

class Asteroid():
    def __init__(self, id):
        self.mass = 1e25
        self.radius = 6.4e8
        self.id = 0

        self.x = random()*mapBound*2 - mapBound
        self.y = random()*mapBound*2 - mapBound 
        self.z = 0 #random()*mapBound*2 - mapBound

        self.xVel = random()*velBound*2 - velBound
        self.yVel = random()*velBound*2 - velBound
        self.zVel = 0 # random()*velBound*2 - velBound

        self.velocity = vector(self.xVel, self.yVel, self.zVel)
        self.momentum = self.velocity * self.mass
        
        self.sphere = sphere(pos=vector(self.x, self.y, self.z), radius=self.radius)
        # self.forceArrow = arrow(pos=self.sphere.pos, axis=vector(0,0,0), color=color.green)

        self.vecForce = vector(0,0,0)

debree = []
for i in range(20):
    debree.append(Asteroid(i+1))

deltaT = 50
t = 0
while t < 10000000:
    rate(100)

    for d1 in debree:
        d1.vecForce = vector(0, 0, 0)

        for d2 in debree:
            if d1.sphere.pos == d2.sphere.pos:
                continue
            pos = d1.sphere.pos - d2.sphere.pos
            magPos = mag(pos)
            d1.vecForce += (-gravConstant*d1.mass*d2.mass*(pos/magPos))/(magPos**2) 

            # print("vecforce", d1.vecForce)
        # d1.forceArrow.axis = d1.vecForce
        d1.momentum += d1.vecForce*deltaT  
        d1.velocity = d1.momentum/d1.mass 
        d1.sphere.pos += d1.velocity*deltaT

    t += deltaT

print("fin")
