from vpython import *
from random import random


scene.width = 1920
scene.height = 1080

mapBound = 1e10
velBound = 1e4
sizeScalar = 1e10
gravConstant = 6.674 * 10**-11

class Asteroid():
    def __init__(self):
        self.mass = 1e25

        self.x = random()*mapBound*2 - mapBound
        self.y = random()*mapBound*2 - mapBound 
        self.z = random()*mapBound*2 - mapBound

        self.xVel = random()*velBound*2 - velBound
        self.yVel = random()*velBound*2 - velBound
        self.zVel = random()*velBound*2 - velBound

        self.velocity = vector(self.xVel, self.yVel, self.zVel)
        self.momentum = self.velocity * self.mass
        self.sphere = sphere(pos=vector(self.x, self.y, self.z), radius=1*sizeScalar)
        
        self.vecForce = vector(0,0,0)

 #       print(self.sphere.pos)
#        print(self.velocity)

debree = []
for _ in range(2):
    debree.append(Asteroid())

deltaT = 50
t = 0
while t < 100000:
    rate(20)

    for d1 in debree:
        for d2 in debree:
            if d1.sphere.pos == d2.sphere.pos:
                continue
            pos = d1.sphere.pos - d2.sphere.pos
            print(pos)
            magPos = mag(pos)
            magForce = (gravConstant*d1.mass*d2.mass)/(magPos)**2 
            d1.vecForce += -magForce*(pos/magPos)
            print(d1.vecForce)

        d1.momentum += d1.vecForce*deltaT  
        d1.velocity = d1.momentum/d1.mass 
        d1.sphere.pos += d1.velocity*deltaT
    
#        break
    
    t += deltaT
#    break

print("fin")
