import random
answer = random.ranrange(1,11)
print(answer)
guess = input("pick a number from 1-10: ")
guess_counter = 2
while guess_counter < 2: 
  if guess == answer:
    print("correct")
  else: 
      if guess > answer:
          guess = input("so close but just to high, try again: ")
          guess_counter + 1
        else: guess = input("so close but just to low, try again: ")
              guess_counter +1
print("oh no, u didnt guess")