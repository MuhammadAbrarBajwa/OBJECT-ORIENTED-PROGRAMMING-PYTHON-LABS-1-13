
print('\n')
print("======== Exercise 1 & 2=========")
#Exercise 1
# Following UML diagram represent an Employee class and Salaried Employee and Hourly Employee classes being inherited from it


from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, cnic):
        self.__name = name
        self.__cnic = cnic
    @abstractmethod
    def monthlySalary(self):
        pass
    
    def getDetails(self):
        return "Name: {}, CNIC: {}, Monthly Salary: {}".format(self.__name, self.__cnic, self.monthlySalary())


class SalariedEmployee(Employee):
    def __init__(self, name,cnic, weeklySalary):
        super().__init__(name, cnic)
        self.__weeklySalary = weeklySalary
    def monthlySalary(self):
        return self.__weeklySalary * 4
    def getDetails(self):
        return super().getDetails()    

class HourlyEmployee(Employee):
    def __init__(self, name,cnic, wage,hours):
        super().__init__(name, cnic)
        self.__wage = wage
        self.__hours = hours
    def monthlySalary(self):
        return self.__wage * self.__hours * 4
    def getDetails(self):
        return super().getDetails()


print('\n')
print("======== Salaried Employee =========")
#SalariedEmployee
name=input("Enter Name: ")
cnic=input("Enter CNIC: ")
weeklySalary=input("Enter weekly salary: ")
weeklySalary = float(weeklySalary)
obj = SalariedEmployee(name, cnic, weeklySalary)
print('\n',obj.getDetails())

print('\n')
print("======== Hourly Employee =========")
#HourlyEmployee
name=input("Enter Name: ")
cnic=input("Enter CNIC: ")
wage=input("Enter wage: ")
hours=input("Enter hours: ")
wage = float(wage)
hours = float(hours)
obj = HourlyEmployee(name, cnic, wage, hours)
print('\n',obj.getDetails())




print('\n')
print("======== Exercise 3 & 4=========")
#Following UML Class diagram represent classes for an Undergraduate and a Graduate student both being inherited from the Student class. For an undergraduate student, the grade would be ‘Pass’ if the test score is greater than or equals to 60, and ‘Fail’ otherwise. However, for a graduate student the grade would be ‘Pass’ if the test score is greater than or equal to 70, and ‘Fail’ otherwise
#Manager’s monthly earning is equal to the basic salary plus house allowance
#CEO’s monthly earning is equal to the basic salary plus house allowance and medical allowance
#Developer’s monthly earning is equal to the basic salary 


##Exercise 3
#Write Python code for defining the classes



class Employee(ABC):
    def __init__(self, name, cnic, basicSalary):
        self.__name = name
        self.__cnic = cnic
        self.__basicSalary = basicSalary
    def getName(self):
        return self.__name
    def getCnic(self):
        return self.__cnic
    def getBasicSalary(self):
        return self.__basicSalary

    def setBasicSalary(self, basicSalary):
        self.__basicSalary = basicSalary

    @abstractmethod
    def monthlyEarnings(self):
        pass

   

    

class Manager(Employee):
    def __init__(self, name, cnic, basicSalary, department, houseAllowance):
        super().__init__(name, cnic, basicSalary)
        self.__department = department
        self.__houseAllowance = houseAllowance

    #accessors
    def getDepartment(self):
        return self.__department
    def getHouseAllowance(self):
        return self.__houseAllowance
    
    #mutators
    def setDepartment(self, department):
        self.__department = department
    def setHouseAllowance(self, houseAllowance):
        self.__houseAllowance = houseAllowance

    def monthlyEarnings(self):
        return self.getBasicSalary() + self.getHouseAllowance()


class CEO(Employee):
    def __init__(self, name, cnic, basicSalary, department, houseAllowance, medicalAllowance):
        super().__init__(name, cnic, basicSalary)
        self.__department = department
        self.__houseAllowance = houseAllowance
        self.__medicalAllowance = medicalAllowance
    #accessors
    def getDepartment(self):
        return self.__department
    def getHouseAllowance(self):
        return self.__houseAllowance
    def getMedicalAllowance(self):
        return self.__medicalAllowance
    #mutators
    def setDepartment(self, department):
        self.__department = department
    def setHouseAllowance(self, houseAllowance):
        self.__houseAllowance = houseAllowance
    def setMedicalAllowance(self, medicalAllowance):
        self.__medicalAllowance = medicalAllowance

    def monthlyEarnings(self):
        return self.getBasicSalary() + self.getHouseAllowance() + self.getMedicalAllowance()

class Developer(Employee):
    def __init__(self, name, cnic, basicSalary, technology):
        super().__init__(name, cnic, basicSalary)
        self.__technology = technology
    #accessors
    def getTechnology(self):
        return self.__technology
    #mutators
    def setTechnology(self, technology):
        self.__technology = technology

    def monthlyEarnings(self):
        return self.getBasicSalary()



# Implement a program to create three employees
# Given the user input, initialize each of them as either a Manager, a CEO, or a Developer
# Display Monthly Earnings for all the employees
# Revise particulars of employees as follows
# •	Increase Basic Salary by 10%
# •	Increase House Allowance by 7%
# •	Increase Medical Allowance by 5%
# Display Monthly Earnings of all the employees after the revision

print('\n')
print("======== Manager =========")
name=input("Enter Name: ")
cnic=input("Enter CNIC: ")
basicSalary=input("Enter Basic  Salary: ")
department=input("Enter Basic  Department: ")
houseAllowance=input("Enter houseAllowance: ")

basicSalary = float(basicSalary)
houseAllowance = float(houseAllowance)

obj = Manager(name, cnic, basicSalary, department, houseAllowance)
print('Name: ',obj.getName())
print('Cnic: ',obj.getCnic())
print('Basic Salary: ',obj.getBasicSalary())
print('Department: ',obj.getDepartment())
print('House Allowance: ',obj.getHouseAllowance())
print('Monthly Earnings: ',obj.monthlyEarnings())

obj.setBasicSalary(float(obj.getBasicSalary()) * 1.1)
obj.setHouseAllowance(float(obj.getHouseAllowance()) * 1.07)

print(obj.monthlyEarnings())

print('\n')
print("======== CEO =========")
name=input("Enter Name: ")
cnic=input("Enter CNIC: ")
basicSalary=input("Enter Basic  Salary: ")
department=input("Enter Basic  Department: ")
houseAllowance=input("Enter house Allowance: ")
medicalAllowance=input("Enter Medical Allowance: ")

obj1 = CEO(name, cnic, basicSalary, department, houseAllowance, medicalAllowance)
print('Name: ',obj1.getName())
print('CNIC: ',obj1.getCnic())
print('Basic Salary: ',obj1.getBasicSalary())
print('Department: ',obj1.getDepartment())
print('House Allowance: ',obj1.getHouseAllowance())
print('Medical Allowance: ',obj1.getMedicalAllowance())
print('Monthly Earnings: ',obj1.monthlyEarnings())

obj1.setBasicSalary(float(obj1.getBasicSalary()) * 1.1)
obj1.setHouseAllowance(float(obj1.getHouseAllowance()) * 1.07)
obj1.setMedicalAllowance(float(obj1.getMedicalAllowance()) * 1.05)

print(obj1.monthlyEarnings())

print('\n')
print("======== Developer =========")
name=input("Enter Name: ")
cnic=input("Enter CNIC: ")
basicSalary=input("Enter Basic  Salary: ")
technology=input("Enter Technology: ")

obj = Developer(name, cnic, basicSalary, technology)
print('Name: ',obj.getName())
print('CNIC: ',obj.getCnic())
print('Basic Salary: ',obj.getBasicSalary())
print('Technology: ',obj.getTechnology())
print('Earnings: ',obj.monthlyEarnings())

obj.setBasicSalary(float(obj.getBasicSalary()) * 1.1)


print(obj.monthlyEarnings())





    






