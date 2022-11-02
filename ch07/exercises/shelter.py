import time

class Animal:
  def  __init__(self,name,animal_type):
    self.name = name
    self.animal_type  = animal_type
    self.adopted = False
    self.adopted_date = ""
    self.id = id(self)
    self.arival = time.strftime("%d/%m/%Y")
  def set_adopted(self):
    self.adopted = True
    self.adopted_date = time.strftime("%d/%m/%Y")
  def __str__(self):
    result_str = f"{self.name}[{self.animal_type}]"
    result_str += f"\narrived:{self.arival}"
    result_str += f"\nadopted:{self.adopted_date}"
    return(result_str)
george = Animal("George","dog")
george.set_adopted()
print(george)