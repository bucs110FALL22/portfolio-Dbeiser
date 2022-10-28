import turtle
window = turtle.Screen()

def draw_petals(sides,out_color,in_color,t):
  '''
  evenley creates petals until object is closed
  ----args----
  sides:(int) the number of petals
  out_color:(str) outline color
  in_color:(str) fill color
  t:(class) brings the turtle into the function 
  ----return----
  petal_radius:(float) the radius of the petals
  circle_angle:(float) the angle of the petals
  
  '''
  SIZE = 100
  HALF_CIRCLE = 180
  QUARTER_CIRCLE = 90
  
  petal_radius = SIZE/sides
  petal_angle = (HALF_CIRCLE/(sides))
  turn_angle = (petal_angle * (sides)) - petal_angle
  circle_angle = (QUARTER_CIRCLE)
  t.color(out_color,in_color)
  
  for i in range(sides):
    t.begin_fill()
    t.circle(petal_radius,circle_angle)
    t.lt(petal_angle)
    t.circle(petal_radius,circle_angle)
    t.rt(turn_angle)
    t.end_fill()
    
  return(petal_radius,circle_angle)
def draw_stem(sides,radius,circle_angle,out_color,in_color,t):
 
  '''
  creates a stem and leaf from the origin of the flower
  ----args----
  sides(int): makes the radius of the stem bigger 
  radius(float) radius of the stem
  circle_angle(float) angle of the stem
  out_color:(str) outline color
  in_color:(str) fill color
  t:(class) brings the turtle into the function 
  ----return----
  None
  
  '''
  CIRCLE_LENGTH = 120
  RAD_SIZE= 2

  
  t.color(out_color,in_color)
  t.circle((-(radius/ RAD_SIZE)* sides),CIRCLE_LENGTH)
  t.begin_fill()
  t.circle(radius * RAD_SIZE,circle_angle)
  t.lt(90)
  t.circle(radius * RAD_SIZE,circle_angle)
  t.end_fill()
  t.lt(45)
  t.circle(((radius/RAD_SIZE)* sides),CIRCLE_LENGTH)





def draw_sun (color_fill,size,t,):
  '''
  creates a sun in the right corner of the screen
  ---args---
  color_fill:(str) fill color
  size:(int) size of the sun
  t:(class) brings the turtle into the function
  ---return---
  none
  '''
  SUN_COORD = 75
  t.penup()
  t.goto(SUN_COORD,SUN_COORD)
  t.color(color_fill)
  t.pendown()
  t.begin_fill()
  t.circle(size)
  t.end_fill()


def main():
  t = turtle.Turtle()
  
  SIDES = 9
  SIZE = 50
  RED = "red"
  GREEN = "green"
  YELLOW = "yellow"
  stem_radius,circle_angle = draw_petals(SIDES,GREEN,RED,t)
  draw_stem(SIDES,stem_radius,circle_angle,GREEN,RED,t)
  draw_sun(YELLOW,SIZE,t)
main()
window.exitonclick()