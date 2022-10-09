

# The Fan class
# Design a class named Fan to represent a fan. The class contains:
# ■ Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
# ■ A private int data field named speed that specifies the speed of the fan.
# ■ A private bool data field named on that specifies whether the fan is on (the default is False).
# ■ A private float data field named radius that specifies the radius of the fan.
# ■ A private string data field named color that specifies the color of the fan.
# ■ The accessor and mutator methods for all four data fields.
# ■ A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).

class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed = SLOW, radius = 5, color = "blue", on = False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, speed):
        self.__speed = speed

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getOn(self):
        return self.__on

    def setOn(self, on):
        self.__on = on
        
print("============= fan ===========\n")
fan1 = Fan(Fan.FAST, 10, "yellow", True)
fan2 = Fan(Fan.MEDIUM,5 , "blue", False)

print("fan1's speed is", fan1.getSpeed(), "radius is", fan1.getRadius(), "color is", fan1.getColor(), "and on is", fan1.getOn())
print("fan2's speed is", fan2.getSpeed(), "radius is", fan2.getRadius(), "color is", fan2.getColor(), "and on is", fan2.getOn())

# The Account class
# Design a class named Account that contains:
# ■ A private int data field named id for the account.
# ■ A private float data field named balance for the account.
# ■ A private float data field named annualInterestRate that stores the current interest rate.
# ■ A constructor that creates an account with the specified id (default 0), initial balance (default 100), and annual interest rate (default 0).
# ■ The accessor and mutator methods for id, balance, and annualInterestRate.
# ■ A method named getMonthlyInterestRate() that returns the monthly interest rate.
# ■ A method named getMonthlyInterest() that returns the monthly interest.
# ■ A method named withdraw that withdraws a specified amount from the account.
# ■ A method named deposit that deposits a specified amount to the account.

print("\n")
print("============= Account ===========\n")

class Account:
    def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12

    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self,amount):
        self.__balance += amount


account = Account(1122, 20000, 4.5)
account.withdraw(2500)
account.deposit(3000)
print("id is", account.getId(), "balance is", account.getBalance(), "monthly interest rate is", account.getMonthlyInterestRate(), "monthly interest is", account.getMonthlyInterest())
