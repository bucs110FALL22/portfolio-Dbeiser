import turtle
window = turtle.Screen()
numsides = int(input("how many sides: "))
side_length = int(input("how long the sides: "))
def draweqshape (numsides,side_length):
  t = turtle.Turtle()
  t.color("green")
  angle = 360/numsides
  for i in range(numsides):
    t.fd(side_length)
    t.rt(angle)
  window.exitonclick()
draweqshape(numsides,side_length)