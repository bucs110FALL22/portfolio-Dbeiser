class QBlock:
  def __init__(self):
    self.hit = False #when hit by player becomes true and releases object
    self.broken = False #whne true, q_block will become brick
    self.object = "Fire Flower" #this q_block has a fire flower object

class Mario:
  def __init__(self):
    self.moving = False #mario starts not moving,when true it starts his walk animation)
    self.power = False #mario starts with no power2
    self.is_touching = False #sees if mario is touching aything

class Goomba:
  def __init__(self):
    self.alive = True #checks if goomba is still alives
    self.squish = False #sees if the goomba is being squished by an object
    self.dmg = 1 #the amount of dmg the goomba does.