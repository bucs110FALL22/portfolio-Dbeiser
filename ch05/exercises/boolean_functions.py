def percentage_to_letter(score):
  if score >= 90:
    return("A")
  elif 80 <= score < 90:
    return("B")
  elif 70 <= score < 80:
    return("C")
  elif 60 <= score < 70:
    return("D")
  else:
    return("F")
def is_passing(grade):
  if grade == "A" or grade == "B" or grade == "C":
    return(True)
  else:
    return(False)

score = float(input("What is you score: "))

letter_grade =percentage_to_letter(score)

pass_fail =is_passing(str(letter_grade))

print("your final letter grade was a", letter_grade,)
if pass_fail == True:
  print("You Passed!")
else:
  print("you Failed")