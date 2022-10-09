
from random import randint as r
print("=======Task 1===========")
# Task 1
a = r(1, 10)
b = r(1, 10)
print(a, "-", b, "=", "?")
ans = int(input("Enter your answer: "))
if ans == a - b:
    print("Correct")
else:
    print("Incorrect")

print("=======Task 2===========")
# Task 2
weight = float(input("Enter your weight in pound: "))
height = float(input("Enter your height in inches: "))
weight = weight * 0.453592
height = height * 0.0254
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9 and bmi > 18.5:
    print("Normal")
elif bmi < 29.9 and bmi > 25:
    print("Overweight")
elif bmi > 30:
    print("Obese")

print("=======Task 3===========")
#Task 3
year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a leap year")

print("=======Task 4===========")
#Task 4
toss = r(0, 1)
ans = int(input("Enter 0 for heads and 1 for tails: "))
if ans == toss:
    print("Correct")
else:
    print("Incorrect")

print("=======Task 5===========")
#Task 5
user = int(input("Enter 0 for rock, 1 for paper, 2 for scissors: "))
computer = r(0, 2)
if user == computer:
    print("Draw")
elif user == 0 and computer == 1:
    print("Computer wins")
elif user == 1 and computer == 2:
    print("Computer wins")
elif user == 2 and computer == 0:
    print("Computer wins")
else:
    print("User wins")

print("=======Task 6===========")
#Task 6
user = int(input("Enter your lottery number: "))
computer = r(10, 20)
if user == computer:
    print("You win $10,000")
elif user % 10 == computer % 10:
    print("You win $3,000")
elif user % 100 == computer % 100:
    print("You win $1,000")
else:
    print("You win nothing")
