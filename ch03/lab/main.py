import turtle #1. import modules
import random
import pygame
import math

#Part A
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
michelangelo.down()
leonardo.down()
mrandom = random.randrange(1,100)
lrandom = random.randrange(1,100)
michelangelo.down()
leonardo.down()
michelangelo.fd(mrandom)
leonardo.fd(lrandom)
michelangelo.up() 
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
michelangelo.down()
leonardo.down()
#second part of A
for i in range(10):
  mrandom = random.randrange(1,100)
  print(mrandom)
  lrandom = random.randrange(1,100)
  michelangelo.fd(mrandom)
  leonardo.fd(lrandom)
michelangelo.up() 
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
michelangelo.down()
leonardo.down()


window.exitonclick()

# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()


