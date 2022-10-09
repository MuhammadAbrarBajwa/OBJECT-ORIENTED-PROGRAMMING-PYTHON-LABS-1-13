


#1.	Write a program that prompts the user to enter three integers and displays them in increasing order.
print("=================Task 1=================")
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

if a>b and a>c:
    if b>c:
        print(c,b,a)
    else:
        print(b,c,a)
elif b>a and b>c:
    if a>c:
        print(c,a,b)
    else:
        print(a,c,b)
else:
    if a>b:
        print(b,a,c)
    else:
        print(a,b,c)

#2.	Write a program that reads an unspecified number of integers, determines how many positive and negative values have been read, and computes the total and average of the input values (not counting the zero). The program ends with the input 0. Display the average as a floating-point number
print("=================Task 2=================")
i = int( input ("Enter an interger, the input ends if it is 0: "))
count_pos = 0
count_neg = 0
total = 0
if (i != 0):
    while (i != 0):
        if (i > 0):
            count_pos += 1
        elif (i < 0):
            count_neg += 1
        total += i
        i = int( input ("Enter an interger, the input ends if it is 0: "))
        count = count_pos + count_neg
        average = total / count
    print ("The number of positives is", count_pos)
    print ("The number of negatives is", count_neg)
    print ("The total is", total)
    print ("The average is", float(average))
else:
    print ("You didn't enter any number.")


print("\n=================Task 3=================")
#3.	Write a program that displays the following table. (Note: 1 kilogram is 2.2 pounds)
print('Kilograms\tPounds')
for i in range(1,200,2):
    print(f'{i}\t\t{i*2.2}')


print("\n=================Task 4=================")
# 4.	Revise the scissor, rock, paper game to let the user play continuously until either the user or the computer wins more than two times

import random
user_won=0
comp_won=0
tie = 0
while True:
     bot = random.randint(1,3)
     if bot == 1:
         bot = "rock"
     elif bot == 2:
         bot = "paper"
     elif bot == 3:
         bot = "scissors"

     user=input("Enter rock paper or scissors: ")
     print("Computer Chose: Rock paper or Scissors ",bot)
     if user == bot:
         result = "Tie"
         tie += 1
     else:
         if user == "rock" and bot == "scissors":
             result = "Bot Won, User Lose"
             user_won += 1
         elif user == "paper" and bot == "rock":
             result = "Bot Won, User Lose"
             user_won += 1
         elif user == "scissors" and bot == "paper":
             result = "Bot Won, User Lose"
             user_won += 1
         elif bot == "rock" and user == "scissors":
             result = "Bot Won, User Lose"
             comp_won += 1
         elif bot == "paper" and user == "rock":
             result = "Bot Won, User Lose"
             comp_won += 1
         elif bot == "scissors" and user == "paper":
             result = "Bot Won, User Lose"
             comp_won += 1

     print(result)
     print("User Won:",user_won)
     print("Bot Won:",comp_won)
     print("Tie:", tie)
     if user_won > 2:
         print("!!!USER WON!!!")
         break
     elif comp_won > 2:
         print("!!!BOT WON!!!")
         break
     elif tie > 2:
          print ("!!!TIE!!!")
          break

    
    
#5.	Write a program that reads integers, finds the largest of them, and counts its occurrences. Assume that the input ends with number 0. Suppose you entered 3 5 2 5 5 5 0; the program finds that the largest number is 5 and the occurrence count for 5 is 4.
print("\n=================Task 5=================")
num = int(input('Enter a number: '))
max = num
count = 0
while num!=0:
    if num>max:
        max = num
        count = 1
    elif num==max:
        count+=1
    num = int(input('Enter a number: '))
print(f'The largest number is {max} and the occurrence count for {max} is {count}')

print("\n=================Task 6=================")
#6 6.	Use nested loops that display the following pattern

# 1					
# 1	2				
# 1	2	3			
# 1	2	3	4		
# 1	2	3	4	5	
# 1	2	3	4	5	6

for i in range(1,7):
    for j in range(1,i+1):
        print(j,end='\t')
    print()
