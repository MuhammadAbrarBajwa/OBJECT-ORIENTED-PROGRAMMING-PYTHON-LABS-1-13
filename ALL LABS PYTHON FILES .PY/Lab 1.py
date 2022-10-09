

print("Hello, Python!")






word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is made up of multiple lines and sentences."""


print(word)
print(sentence)
print(paragraph)



print("\n")

print("Task 1\n")
x=int(input("enter the radius: "))
compute =(3.14*x*x)
print(compute)

print("\n")

print("Task 2 \n")
first=input("Enter your first name: ")
last=input("Enter your last name: ")
print(last,"",first)

print("\n")


print("Task 3\n")
y=int(input("enter the number: "))
even =y%2
if even ==0:
    print("It is even number!")
else:
    print("It is odd number!")

print("\n")

print("Task 4\n")
number=int(input("Enter a number:"))
sumofinteger=0
while(number>0):
    digits=number%10
    sumofinteger=sumofinteger+digits
    number=number//10
print("The sum of the digits in an integer:",sumofinteger)

