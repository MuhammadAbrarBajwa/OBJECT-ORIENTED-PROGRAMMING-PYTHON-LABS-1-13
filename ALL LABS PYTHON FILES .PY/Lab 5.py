

# 1.	Write a function that computes the sum of the digits in an integer. Use the following function header

# def sumDigits(n):

# Write a test program that prompts the user to enter an integer and displays the sum of all its digits.
print("===== Task 1=========")
def sumDigits(n):
    total = 0
    while n!=0:
        total += n%10
        n = n//10
    return total

num = int(input('Enter a number: '))
print(sumDigits(num))

#2.	Write the following function to display three numbers in increasing order

# def displaySortedNumbers(num1, num2, num3):

# Write a test program that prompts the user to enter three numbers and invokes the function to display them in increasing order
print("===== Task 2=========")
def displaySortedNumbers(num1, num2, num3):
    if num1>num2 and num1>num3:
        if num2>num3:
            print(num3,num2,num1)
        else:
            print(num2,num3,num1)
    elif num2>num1 and num2>num3:
        if num1>num3:
            print(num3,num1,num2)
        else:
            print(num1,num3,num2)
    else:
        if num1>num2:
            print(num2,num1,num3)
        else:
            print(num1,num2,num3)
    return ''
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
displaySortedNumbers(num1,num2,num3)

# 3.	Write the following function to display an integer in reverse order.

# def reverse(number):

# Write a test program that prompts the user to enter an integer and displays its reversal
print("===== Task 3=========")
def reverse(number):
    rev = 0
    while number!=0:
        rev = rev*10 + number%10
        number = number//10
    return rev

num = int(input('Enter a number: '))
print(reverse(num))
# 4.	Write the following function which returns True if the number is a palindrome.

# def isPalindrome(number):

# A number is a palindrome if its reversal is the same as itself. Write a test program that prompts the user to enter an integer and reports whether the integer is a palindrome.
# Hint: Use the reverse function to implement isPalindrome
print("===== Task 4=========")
def isPalindrome(number):
    rev = 0
    temp = number
    while number!=0:
        rev = rev*10 + number%10
        number = number//10
    if temp==rev:
        return True
    else:
        return False
    
num = int(input('Enter a number: '))
print(isPalindrome(num))

#5.	Write a function that returns the number of days in a year using the following header

# def numberOfDaysInAYear(year):

# Write a test program that displays the number of days in the year from 2010 to 2020
print("===== Task 5=========")

def numberOfDaysInAYear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return 366
    else:
        return 365
    
years=0
for i in range(2010,2021):
    print(f'{i} has {numberOfDaysInAYear(i)} days')
    years = years + int(numberOfDaysInAYear(i))
print('the number of days in the year from 2010 to 2020: ',years)
#6.	Write a function that converts milliseconds to hours, minutes, and seconds using the following header

# def convertMilli(millis):

# The function returns three strings each for hours, minutes, and seconds. For example, convertMillis(5500) returns the strings ‘0’, ‘0’, and ‘5’, convertMillis(100000) returns the strings ‘0’, ‘1, ’40’, and convertMillis(555550000) returns the strings ‘154, ’19’, and ’10’

# Write a test program that prompts the user to enter a value for milliseconds and displays a string in the format of hours:minute:seconds
print("===== Task 6=========")
def convertMilli(millis):
    sec = millis//1000
    min = sec//60
    hour = min//60
    sec = sec%60
    min = min%60
    return hour,min,sec

millis = int(input('Enter milliseconds: '))
hour,min,sec = convertMilli(millis)
print(f'{hour}:{min}:{sec}')
