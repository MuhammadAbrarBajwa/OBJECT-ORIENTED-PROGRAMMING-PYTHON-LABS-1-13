

def gcd(n,d):
    n1 = abs(n)
    n2 = abs(d)

    k = 1
    while k <= n1 and k <= n2:
        if n1%k==0 and n2%k==0:
            gcd = k

        k += 1

    return gcd

class Rational:
    def __init__(self,numerator=1,denominator=0):
        if denominator == 0:
            raise RuntimeError("Denominator cannot be zero")
        else:
            divisor = gcd(numerator,denominator)
            self.__numerator = (1 if denominator > 0 else -1) * int(numerator / divisor)
            self.__denominator = int(abs(denominator) / divisor)

    def getNumerator(self):
        return self.__numerator

    def getDenominator(self):
        return self.__denominator

    def __add__(self,secondRational):
        n = self.__numerator * secondRational.getDenominator() + self.__denominator * secondRational.getNumerator()
        d = self.__denominator * secondRational.getDenominator()
        return Rational(n,d)

    def __sub__(self, secondRational):
        n = self.__numerator * secondRational.getDenominator() - self.__denominator * secondRational.getNumerator()
        d = self.__denominator * secondRational.getDenominator()
        return Rational(n,d)

    def __mul__(self, secondRational):
        n = self.__numerator * secondRational.getNumerator()
        d = self.__denominator * secondRational.getDenominator()
        return Rational(n,d)


    def __float__(self):
        return self.__numerator / self.__denominator

    def __int__(self):
        return int(self.__float__())

    def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        else:
            return str(self.__numerator) + "/" + str(self.__denominator)

    def __lt__(self, secondRational):
        return self.__cmp__(secondRational) < 0.0

    def __le__(self, secondRational):
        return self.__cmp__(secondRational) <= 0.0

    def __gt__(self, secondRational):
        return self.__cmp__(secondRational) > 0.0

    def __ge__(self, secondRational):
        return self.__cmp__(secondRational) >= 0.0

    def __cmp__(self, secondRational):
        temp = self.__sub__(secondRational)
        if temp.getNumerator()>0:
            return 1
        elif temp.getNumerator()<0:
            return -1
        else:
            return 0




class GeometricObject:
    def __init__(self,color="green",filled=True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self,color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self,filled):
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + " and filled: " + str(self.__filled)

class Triangle(GeometricObject):
    def __init__(self,side1=1.0,side2=1.0,side3=1.0):
        super().__init__()
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            self.__side1 = side1
            self.__side2 = side2
            self.__side3 = side3
        else:
            raise RuntimeError("The three given sides cannot form a triangle")

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return (s*(s-self.__side1)*(s-self.__side2)*(s-self.__side3)) ** 0.5

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return f"Triangle\n\nSide1: " + str(self.__side1) + " side2: " + str(self.__side2) + " side3: " + str(self.__side3)



class TriangleError(RuntimeError):
    def __init__(self,side1,side2,side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    def __str__(self):
        return "Error! The three given sides cannot form a triangle"

    
r1 = Rational(4,2)
r2 = Rational(2,3)
r3 = r1 + r2
print(r3)
r3 = r1 - r2
print(r3)
r3 = r1 * r2
print(r3)
print(float(r3))
print(r3)
print(r1 < r2)

tr = Triangle(1,1,1)
print(tr)
print(tr.getArea())
print(tr.getPerimeter())

r = Rational(1,0)

