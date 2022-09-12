import turtle
window = turtle.Screen()
my_turtle = turtle.Turtle()
numsides = int(input("how many sides? "))
print(numsides)
length = int(input("how long are the sides? "))
angle = 360/(numsides)
my_turtle = turtle.shape("turtle")
my_turtle = turtle.color("blue")
for i in range(numsides):
  my_turtle = turtle.fd(length)
  my_turtle = turtle.rt(angle)
window.exitonclick()