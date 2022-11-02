class Rectangle:
  def __init__(self,x,y,h,w):
    self.x = x
    if self.x < 0:
      self.x = 0
    self.y = y
    if self.y < 0:
      self.y = 0
    self.height = h
    if self.height < 0:
      self.height = 0
    self.width = w
    if self.width < 0:
      self.width = 0
    
  def __str__(self):
    output = "(x:{},y:{})height:{},width:{}".format(self.x,self.y,self.height,self.width)
    return(output)
