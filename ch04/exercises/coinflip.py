import turtle
import random
window = turtle.Screen()
# while True:

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
distance = 10
angle = 90
is_in_screen = True

colors = ["purple", "orange","green"]

while is_in_screen:
  coin = random.randrange(0,2)
  if coin == 0:
    t.left(angle)
  else:
    t.right(angle)
  t.forward(distance)
  
  
  turtlex = t.xcor()
  turtley = t.ycor()

  x_range = window.window_width()/2
  y_range = window.window_height()/2

  t.color(colors[0])
  colors.append(colors.pop(0))
  if abs(turtlex) > x_range or abs(turtley) > y_range:
    is_in_screen = False

window.exitonclick()