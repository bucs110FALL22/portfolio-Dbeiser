import random

answer = (int(random.randrange(1,11)))
# guess = int(input("pick a number from 1-10: "))
for i in range(3): 
  guess = int(input("pick a number from 1-10: "))
  if guess == answer:
    print("correct")
    break
  elif guess > answer:
    print("so close but just to high, try again: ")
    
  else: 
    print("so close but just to low, try again: ")
   
