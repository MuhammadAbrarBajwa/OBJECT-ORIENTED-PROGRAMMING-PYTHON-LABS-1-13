

print('Exercise 1 & 2')
print('\n')

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance(self,Point):
        return ((self.x-Point.x)**2+(self.y-Point.y)**2)**0.5


class Quadrilateral:
    def __init__(self,p1,p2,p3,p4):
        self.vertex1=p1
        self.vertex2=p2
        self.vertex3=p3
        self.vertex4=p4

    def __str__(self):
        return f"{self.vertex1.x},{self.vertex1.y} {self.vertex2.x},{self.vertex2.y} {self.vertex3.x},{self.vertex3.y} {self.vertex4.x},{self.vertex4.y}"
    
    def getPerimeter(self):
        return self.vertex1.distance(self.vertex2)+self.vertex2.distance(self.vertex3)+self.vertex3.distance(self.vertex4)+self.vertex4.distance(self.vertex1)
    
    def isSquare(self):
        return self.vertex1.distance(self.vertex2)==self.vertex2.distance(self.vertex3)==self.vertex3.distance(self.vertex4)==self.vertex4.distance(self.vertex1)

p1, p2 = input("Enter p1 and p2: ").split(" ")
p3, p4 = input("Enter p3 and p4: ").split(" ")
p5, p6 = input("Enter p5 and p6: ").split(" ")
p7, p8 = input("Enter p7 and p8: ").split(" ")



vertex1=Point(int(p1),int(p2))
vertex2=Point(int(p3),int(p4))
vertex3=Point(int(p5),int(p6))
vertex4=Point(int(p7),int(p8))

quad=Quadrilateral(vertex1,vertex2,vertex3,vertex4)
print(quad)
print(quad.getPerimeter())
print(quad.isSquare())




print('\n')
print('Exercise 3 & 4')

class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name}, ({self.email})"

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def __str__(self):
        return f"Book[title={self.title}, Author[name={self.author.name}, email={self.author.email}], price={self.price}]"


author=Author("Tatsuki Fujimoto","fujimoto@gmail.com")
book=Book("Chainsaw Man",author,1000)
print(book)

