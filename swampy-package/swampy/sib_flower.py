# Flower excercise (4.2) from Week 0

# Name: Pat Byrnes (PMByrnes)


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob
# Stuck on this - used the answer code to see what the author's methodology was.

from polygon import *

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)

def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

# Flower 1
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

# Flower 2
move(bob, 100)
flower(bob, 10, 40.0, 80.0)

# Flower 3
move(bob, 100)
flower(bob, 20, 140.0, 20.0)

wait_for_user()					

