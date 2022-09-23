import turtle #1. import modules
import random
import pygame
import math

# Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
#first part of A
mrandom = random.randrange(1,100)
lrandom = random.randrange(1,100)

michelangelo.fd(mrandom)
leonardo.fd(lrandom)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
#second part of A
for i in range(10):
  mrandom = random.randrange(1,100)
  print(mrandom)
  lrandom = random.randrange(1,100)
  michelangelo.fd(mrandom)
  leonardo.fd(lrandom)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


window.exitonclick()

# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode((500, 500))
coords = []
num_sides = 65
side_length = 100
offset = 150
black =[0,0,0]
for nums in range(num_sides):
  theta = (2.0 * math.pi * nums / num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x, y))
pygame.draw.polygon(window, "purple", coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill(black)

#equalat triangle
coords = []
num_sides = 3
side_length = 100
offset = 150

for nums in range(num_sides):
  theta = (2.0 * math.pi * nums / num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x, y))
pygame.draw.polygon(window, "purple", coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill(black)

#square
coords = []
num_sides = 4
side_length = 100
offset = 150

for nums in range(num_sides):
  theta = (2.0 * math.pi * nums / num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x, y))
pygame.draw.polygon(window, "purple", coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill("black")

#hexagon
coords = []
num_sides = 6
side_length = 100
offset = 150

for nums in range(num_sides):
  theta = (2.0 * math.pi * nums / num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x, y))
pygame.draw.polygon(window, "purple", coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill("black")

#nonagon
coords = []
num_sides = 9
side_length = 100
offset = 150

for nums in range(num_sides):
  theta = (2.0 * math.pi * nums / num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x, y))
pygame.draw.polygon(window, "purple", coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill("black")

#circle

coords = []
num_sides = 360
side_length = 100
offset = 150

for nums in range(num_sides):
  theta = (2.0 * math.pi * nums / num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x, y))
pygame.draw.polygon(window, "purple", coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill("black")