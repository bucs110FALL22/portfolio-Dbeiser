import turtle
window = turtle.Screen()
def draweqshape (numsides,side_length):
  t = turtle.Turtle()
  t.color("green")
  angle = 360/numsides
  for i in range(numsides):
    t.fd(side_length)
    t.rt(angle)
  window.exitonclick()
draweqshape(8,50)