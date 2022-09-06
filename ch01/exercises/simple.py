# print(10 * 5)
# print(10 ** 2)
# print(15 / 10)
# print(15 // 10)
# print(-15 // 10)
# print(15 % 10)
# print(10 % 15)
# print(10 % 10)
# print(0 % 10)
# print(10 / 15)
#the issue with (10/15) is that the answer is a repeating decimal but it ends in the code.
rate = float(input("what is the Euro to US Dollar conversion rate? "))

amount = float(input("How much would you like to exchange? "))

total = rate * amount

result = total - 3

print("your exchanged amount is $", result)
