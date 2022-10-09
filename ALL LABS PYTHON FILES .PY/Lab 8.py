
print('\n\n')
print("========Exercise 1 & 2=========")
# Ex1
# Implement a program to create two BMI objects. First one for John Doe, aged 18 years, weighing 145 pounds and having a height of 70 inches. Other for Peter King, aged 50 years, weighing 215 pounds, and having a height of 70 inches. The program then shows the BMI value with status for both the objects along with the name.


class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def getBMI(self):
        return self.__weight / (self.__height / 100) ** 2

    def getStatus(self):
        if self.getBMI() < 18.5:
            return "Underweight"
        elif self.getBMI() < 25:
            return "Normal"
        elif self.getBMI() < 30:
            return "Overweight"
        else:
            return "Obese"

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getWeight(self):
        return self.__weight

    def getHeight(self):
        return self.__height

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setWeight(self, weight):
        self.__weight = weight

    def setHeight(self, height):
        self.__height = height

    def __str__(self):
        return "Name: {}, Age: {}, Weight: {}, Height: {}, BMI: {}, Status: {}".format(self.__name, self.__age, self.__weight, self.__height, self.getBMI(), self.getStatus())

# Ex2

obj1 = BMI("John Doe", 18, 145, 70)
obj2 = BMI("Peter King", 50, 215, 70)
print(obj1)
print(obj2)




print('\n\n')
print("========Exercise 3=========")
# An n-sided regular polygon’s sides all have the same length and all of its angles have the same degree (i.e., the polygon is both equilateral and equiangular). Design a class named RegularPolygon that contains:
# ■ A private int data field named n that defines the number of sides in the polygon.
# ■ A private float data field named side that stores the length of the side.
# ■ A private float data field named x that defines the x-coordinate of the center of the polygon with default value 0
# A private float data field named y that defines the y-coordinate of the center of the polygon with default value 0.
# ■ A constructor that creates a regular polygon with the specified n (default 3), side (default 1), x (default 0), and y (default 0).
# ■ The accessor and mutator methods for all data fields.
# ■ The method getPerimeter() that returns the perimeter of the polygon.
# ■ The method getArea() that returns the area of the polygon. The formula for computing the area of a regular polygon is
# Area=  (n × s^2)/(4 × tan⁡〖π/n〗 )
import math
# Exercise 3
class RegularPolygon:
    def __init__(self, n=3, l=1, x=0, y=0):
        self.__n = n
        self.__l = l
        self.__x = x
        self.__y = y

    def setN(self, n):
        self.__n = n

    def setL(self, l):
        self.__l = l

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getY(self):
        return self.__y

    def getX(self):
        return self.__x

    def getL(self):
        return self.__l

    def getN(self):
        return self.__n

    def getPerimeter(self):
        return self.__n * self.__l

    def getArea(self):
        return self.__n * self.__l ** 2 / 4 * math.tan(math.pi / self.__n)

    def __str__(self):
        return "n: {}, l: {}, x: {}, y: {}".format(self.__n, self.__l, self.__x, self.__y)


poly = RegularPolygon()
poly.setN(6)
poly.setL(4)
poly.setX(5.6)
poly.setY(7.8)
print(poly)
print(poly.getPerimeter())
print(poly.getArea())
poly2 = RegularPolygon(10, 4, 5.6, 7.8)
print(poly2)
print(poly2.getPerimeter())
print(poly2.getArea())



print('\n\n')
print("========Exercise 4=========")
# Exercise 4

# Write a test program that creates three RegularPolygon objects, created using RegularPolygon(), using RegularPolygon(6, 4) and RegularPolygon(10, 4, 5.6, 7.8). For each object, display its perimeter and area.

import math


class RegularPolygon:
    def __init__(self, n=0, l=0, x=0, y=0):
        self.n = n
        self.l = l
        self.x = x
        self.y = y

    def perimeter(self):
        return self.n * self.l * math.pi

    def area(self):
        return self.n * self.l ** 2 / 4 * math.tan(math.pi / self.n)

    def __str__(self):
        return "n: {}, l: {}, x: {}, y: {}".format(self.n, self.l, self.x, self.y)


obj1 = RegularPolygon()
obj2 = RegularPolygon(6, 4)
obj3 = RegularPolygon(10, 4, 5.6, 7.8)
print(obj1)
print(obj2)
print(obj3)
