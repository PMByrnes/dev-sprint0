# Polygon excercise from Week 0

# Name: Pat Byrnes (PMByrnes)


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

#Exercise #2
#1
def square():
    for i in range(4):
        fd(bob, 100)
        lt(bob)

print square()

#2
def square(Turtle, length):
    for i in range(4):
        fd(Turtle, length)
        lt(Turtle)

print square(bob, 50)

#3
def poly(Turtle, length, n):
    ang = 360/n
    n = 360/ang
    for i in range(n):
        fd(Turtle, length)
        lt(Turtle, ang)

print poly(bob, 75, 5)


#Exercise #3
#1
def poly(Turtle, length, n):
    ang = 360/n
    n = 360/ang
    for i in range(n):
        fd(Turtle, length)
        lt(Turtle, ang)

def circle(Turtle, radius):
    circumference = 2*3.14159*radius
    n = int(round(circumference))
    poly(Turtle, 1.0, n)

circle(bob, 25)


#2 - I used the code from the book to get an idea, then went back and reworked the exercise.

def polyline(Turtle, n, length, ang):
    for i in range(n):
        fd(Turtle, length)
        lt(Turtle, ang)

def arc(Turtle, radius, ang):
    arc_length = 2 * 3.14159 * radius * (ang / 360)
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(ang) / n
    polyline(Turtle, n, step_length, step_angle)

print arc(bob, 25, 90)


wait_for_user()					
