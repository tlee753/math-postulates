from __future__ import division
from vpython import *

# SCENE
scene.width = 1920
scene.height = 1080

# CONSTANTS
mEarth = 6e24
mCraft = 15e3
mMoon = 7e22
G = 6.7e-11
deltat = 60

# OBJECTS
earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
moon = sphere(pos=vector(4e8, 0, 0), radius=1.75e6, color=color.white)
craft = sphere(pos=vector(-59520000, -2944000, 0), radius = 3e4, color=color.red)
trail = curve(color=craft.color)
Fnet_tangent_arrow = arrow(pos=craft.pos, axis=vector(0, 0, 0), color=color.yellow)
Fnet_perp_arrow = arrow(pos=craft.pos, axis=vector(0, 0, 0), color=color.magenta)

# VISUALS
scene.range=20*earth.radius
scene.autoscale = 0

# INITIAL CONDITIONS
t = 0
vCraft = vector(505, 2718, 0)
pCraft = mCraft*vCraft

# CALCULATIONS
while t <= 700800:
    # Loop parameters
    rate(100)
    #scene.center = craft.pos
    #scene.range = craft.radius*200

    # Momentum initial
    p_init = mag(pCraft)
    
    # Gravitational force of Earth on craft
    posToEarth = craft.pos-earth.pos
    magPosToEarth = mag(posToEarth)
    unitVecEarth = posToEarth/magPosToEarth
    forceVecEarth = (-G*mCraft*mEarth*unitVecEarth)/(magPosToEarth**2)
    
    # Gravitational force of Moon on craft
    posToMoon = craft.pos-moon.pos
    magPosToMoon = mag(posToMoon)
    unitVecMoon = posToMoon/magPosToMoon
    forceVecMoon = (-G*mCraft*mMoon*unitVecMoon)/(magPosToMoon**2)
    
    # Updating craft
    netForce = forceVecEarth + forceVecMoon
    pCraft = pCraft + (netForce)*deltat
    vCraft = pCraft/mCraft
    craft.pos = craft.pos + (vCraft*deltat)

    # Momentum final
    p_final = mag(pCraft)

    # Arrow axis vector
    unitVecPCraft = norm(pCraft)
    Fnet_tangent = ((p_final - p_init)/(deltat))*(unitVecPCraft)
    Fnet_perp = netForce - Fnet_tangent

    # Net force arrow
    Fnet_tangent_arrow.pos = craft.pos
    Fnet_tangent_arrow.axis = Fnet_tangent*1e5
    Fnet_perp_arrow.pos = craft.pos
    Fnet_perp_arrow.axis = Fnet_perp*5e4
    
    # Trail
    trail.append(pos=craft.pos)
    
    # Collisions
    if magPosToEarth < earth.radius:
        print("Collision with Earth")
        break
    if magPosToMoon < moon.radius:
        print("Collision with Moon")
        break

    # Printing kinematic values
    if t % 7008 == 0:
        print("netforce", netForce)
        # print()
        # print(t)
        # print(craft.pos)
        # print(vCraft)
        # print(netForce)
        # print()

    # Printing for formula
    """
    if t % 10000 ==0:
        print "\nThe time is ", t
        print "The magnitude of the momentum is ", mag(pCraft)
        print "The magnitude of the velocity is ", mag(vCraft)
        print "The magnitude of the perpendicular componenet is ", mag(Fnet_perp)
        print "The magnitude of the seperation vector is ", mag(posToEarth)
        print "The kissing cirlce is ", (mag(pCraft)*mag(vCraft))/mag(Fnet_perp) 
    """
    
    # Time
    t = t + deltat
    
print('Calculations finished after ',t,'seconds')

# RECORDED INITIAL CONDITIONS
"""
To crash into moon
vCraft = vector(5e3, 3.3e3, 0)

Figure eight around moon
vCraft = vector(1e2, 3e3, 0)

To Crash into Earth
vCraft = vector(0, 3270, 0)
"""
