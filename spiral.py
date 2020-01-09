from vpython import *
from random import random
import time

scene.width = 1920
scene.height = 1080

class Asteroid():
    def __init__(self):
        self.mass = 1
        self.x = random()*1000
        self.y = random()*1000
        self.z = random()*1000
        self.xVel = random()*100
        self.yVel = random()*100
        self.zVel = random()*100
        self.sphere = sphere(pos=vector(self.x, self.y, self.z), radius=self.mass, color=color.red)

debree = []

for _ in range(20):
    debree.append(Asteroid())

# for d1 in debree:
  #   for d2 in debree:
    #     d1.x += self.xVel * t
     #    d1.y += self.yVel * t
       #  d1.z += self.zVel * t
        

   #  time.sleep(10)
        
