import turtle
window = turtle.Screen()
my_turtle = turtle.Turtle()
CIRCLE_DEGREES = 360
numsides = int(input("how many sides? "))
length = int(input("how long are the sides? "))
angle = CIRCLE_DEGREES/(numsides)

my_turtle = turtle.shape("turtle")
my_turtle = turtle.color("blue")

for i in range(numsides):
  my_turtle = turtle.fd(length)
  my_turtle = turtle.rt(angle)


window.exitonclick()