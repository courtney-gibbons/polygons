import turtle
drew = turtle.Turtle()

#triangle
#drew.forward(120)
#drew.right(120)
#drew.forward(120)
#drew.right(120)
#drew.forward(120)

#any polygon
#n = input('How many sides on the polygon? ')
#numTriangles = int(n)-2
#interiorAngles = numTriangles*180
#eachAngle = interiorAngles/int(n)
#angle = 180 - eachAngle
#for _ in range(int(n)):
#    drew.forward(60)
#    drew.right(angle)

#any polygon centered
import math
n = input('How many sides on the polygon? ')
numTriangles = int(n)-2
interiorAngles = numTriangles*180
eachAngle = interiorAngles/int(n)
#print(eachAngle)
angle = 180 - eachAngle
#print(angle)
angleStart = eachAngle/2
#print(angleStart)
side = 60
radius = (side/2)/math.cos(math.radians(eachAngle/2))
#print(radius)
drew.penup()
drew.left(angleStart)
drew.forward(radius)
drew.right(angleStart)
drew.pendown()
for _ in range(int(n)):
    drew.right(angle)
    drew.forward(side)
