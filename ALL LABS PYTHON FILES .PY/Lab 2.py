#Task 1 
from math import *
#input
length = int(input("Length"))
radius = int(input("Radius"))

#formula
area = radius * radius * pi
volume = area * length

#print
print("The area of the given Radius is: ",area)
print("The Volume is: ",volume)

#Task 2
#input
minutes=eval(input("enter minutes: "))

#Converting
years =minutes / 525600
days =(minutes % 525600) / 1440

#print
print(minutes , " minutes is approximately " , years, " years and " , days , " days")

#Task 3
M = int(input("Enter amount of water in kilograms "))
finalTemperature = int(input("Enter Final Temperature in degrees Celsius: "))
initialTemperature = int(input("Enter Initial Temperature in degrees Celsius: "))

#Compute
Q = M * (finalTemperature - initialTemperature ) * 4184
#print
print("energy in joules: ",Q)


# Task 4
n = int(input("Enter a 4 digit integer: "))
reverse = 0
while (n > 0):
    a = n % 10
    reverse = reverse * 10 + a
    n = n // 10
print(reverse)


# Task 5
Weight = int(input("Enter your weight in Pound "))
Height = int(input("Enter your Height in Inches "))

BMI = (Weight / Height**2) * 703
print("The BMI for the given Weight and Height is: ",BMI)


# Task 6

no_of_seconds_in_year = 365*24*60*60
birthsperyear = no_of_seconds_in_year/7
deathsperyear = no_of_seconds_in_year/13
immigrantsperyear = (no_of_seconds_in_year/45)
x= int(input("Enter an year"))
population_rate = x*(birthsperyear + deathsperyear - immigrantsperyear)
print(birthsperyear, int(birthsperyear) , 'are the number of births per year')
print(deathsperyear, int(deathsperyear), 'are the number of deaths per year')
print(immigrantsperyear, int(immigrantsperyear), 'are the number of immigrants per year')
print(population_rate, 'population to that year')
