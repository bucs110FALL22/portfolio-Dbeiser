def rstar_pyramid():
  rows =int(input("how many rows of stars:"))
  while rows != 0:
    print(rows * "*")
    rows  -= 1
def star_pyramid():
  rows =int(input("how many rows of stars:"))
  rows += 1
  num_in_row = 1
  while num_in_row != rows :
    if num_in_row == rows:
      rows = 0
    print(num_in_row * "*")
    num_in_row += 1
    
star_pyramid()
rstar_pyramid()