def multiplyer(m1,m2):
  product = 0
  for i in range(m2):
    product += m1
  return product
  
def raiser(r1,exponent):
  ans_expo = r1
  for i in range(exponent -1):
    ans_expo *= r1
  return ans_expo
  
def square(square_num):
  ans_Square = multiplyer(square_num,square_num)
  return(ans_Square)
  
def main():
  num1 = 3
  num2 = 4
  fun1 = multiplyer(num1,num2)
  print(fun1)
  fun2 = raiser(num1,num2)
  print(fun2)
  fun3 = square(num1)
  print(fun3)


main()
  