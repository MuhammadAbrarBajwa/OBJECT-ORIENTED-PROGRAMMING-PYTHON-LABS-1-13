

print('\n\n')
print("======== Exercise 1 and 2 =========")
#Exercise 1
class GeometricShape:
    def __init__(self,color):
        self.__color = color
    def getColor(self):
        return self.__color
    def getPerimeter(self):
        pass
    def getArea(self):
        pass



class Rectangle(GeometricShape):
    def __init__(self, w=1, l=1, color=None):
        super().__init__(color)
        self.__w = w
        self.__l = l
    def setW(self, w):
        self.__w = w
    def setL(self, l):
        self.__l = l
    def getW(self):
        return self.__w
    def getL(self):
        return self.__l
    def getPerimeter(self):
        return 2 * (self.__w + self.__l)
    def getArea(self):
        return self.__w * self.__l


#Exercise 2
width, height, color = input("Enter width, height and color respectively: ").split(" ")
width = float(width)
height = float(height)
color = str(color)
obj = Rectangle(width, height, color)
print("Perimeter:", obj.getPerimeter())
print("Area:", obj.getArea())
print("Color:", obj.getColor())


print('\n\n')
print("======== Exercise 3 & 4 =========")
#Exercise 3
# classes for an Undergraduate and a Graduate student both being inherited from the Student class. For an undergraduate student, the grade would be ‘Pass’ if the test score is greater than or equals to 60, and ‘Fail’ otherwise. However, for a graduate student the grade would be ‘Pass’ if the test score is greater than or equal to 70, and ‘Fail’ otherwise

class Student:
    def __init__(self, name, score,grade):
        self.__name = name
        self.__testScore = score
        self.__grade = grade
    def getName(self):
        return self.__name
    def getScore(self):
        return self._score
    def getGrade(self):
        return self.__grade
    def setTestScore(self, score):
        self.__testScore = score
    def getTestScore(self):
        return self.__testScore
    def computeGrade(self):
        pass

class Undergraduate(Student):
    def __init__(self, name, score, grade):
        super().__init__(name, score, grade)
    def computeGrade(self):
        if self.getTestScore() >= 60:
            self.setTestScore('Pass')
        else:
            self.setTestScore('Fail')
    def __str__(self):
        return "Name: {}, Score: {}, Grade: {}".format(self.getName(), self.getTestScore(), self.getTestScore())

class Graduate(Student):
    def __init__(self, name, score, grade):
        super().__init__(name, score, grade)
    def computeGrade(self):
        if self.getTestScore() >= 60:
            self.setTestScore('Pass')
        else:
            self.setTestScore('Fail')
    def __str__(self):
        return "Name: {}, Score: {}, Grade: {}".format(self.getName(), self.getTestScore(), self.getTestScore())

name, score = input("Enter name and score: ").split(" ")
score = float(score)
obj = Undergraduate(name, score, "")
obj.computeGrade()
print(obj)
name, score = input("Enter name and score: ").split(" ")
score = float(score)
obj = Graduate(name, score, "")
obj.computeGrade()
print(obj)

