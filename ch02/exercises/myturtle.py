import turtle
window = turtle.Screen()
my_turtle = turtle.Turtle()
length = 50
angle = (90)
my_turtle = turtle.color("green")
my_turtle = turtle.shape("turtle")
for i in range(4):
  my_turtle = turtle.fd(length)
  my_turtle = turtle.rt(angle)

my_turtle = turtle.up()
my_turtle = turtle.fd(70)
my_turtle = turtle.color("grey")
my_turtle = turtle.down()
for i in range(4):
  my_turtle = turtle.fd(length)
  my_turtle = turtle.rt(angle)
window.exitonclick()