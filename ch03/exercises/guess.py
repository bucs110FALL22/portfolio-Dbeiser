import random

answer = (int(random.randrange(1,11)))
print(answer)
# guess = int(input("pick a number from 1-10: "))
guess_counter = 0
while guess_counter < 2: 
  guess = int(input("pick a number from 1-10: "))
  if guess == answer:
    print("correct")
    guess_counter =+ 3
  elif guess > answer:
    print("so close but just to high, try again: ")
    guess_counter =+ 1
  else: 
    print("so close but just to low, try again: ")
    guess_counter =+ 1
    print(guess_counter)
