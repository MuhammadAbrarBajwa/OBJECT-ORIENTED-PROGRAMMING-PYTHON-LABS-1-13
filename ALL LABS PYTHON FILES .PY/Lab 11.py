

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, cnic):
        self.__name = name
        self.__cnic = cnic

   
    def getCnic(self):
        return self.__cnic

    def getName(self):
        return self.__name
    
    @abstractmethod
    def monthlySalary(self):
        pass

    def getDetails(self):
        return (self.__name, self.__cnic, self.monthlySalary())


class SalariedEmployee(Employee):
    def __init__(self, name, cnic, weeklySalary):
        super().__init__(name, cnic)
        self.__weeklySalary = weeklySalary

    def monthlySalary(self):
        return self.__weeklySalary * 4

    def getDetails(self):
        return super().getDetails()


class HourlyEmployee(Employee):
    def __init__(self, name, cnic, wage, hours):
        super().__init__(name, cnic)
        self.__wage = wage
        self.__hours = hours

    def monthlySalary(self):
        if self.__hours > 40:
            return 40 * self.__wage + (self.__hours - 40) * self.__wage * 1.5
        return self.__wage * self.__hours

    def getDetails(self):
        return super().getDetails()



salaried = []
hourly = []
while True:
    print('1. Add an Employee')
    print('2. Show Employee Details')
    print('3. Terminate an Employee')
    print('4. Display Employee Register')
    print('5. Exit the Application')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        print('1. Salaried Employee')
        print('2. Hourly Employee')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            print()
            name = input('Enter name: ')
            cnic = input('Enter cnic: ')
            weeklySalary = int(input('Enter weekly salary: '))
            if cnic in [i.getCnic() for i in salaried] or cnic in [i.getCnic() for i in hourly]:
                print('Employee already exists')
            else:

                salaried.append(SalariedEmployee(name, cnic, weeklySalary))
                print('Salaried Employee added successfully')
                print()
        elif choice == 2:
            print()
            name = input('Enter name: ')
            cnic = input('Enter cnic: ')
            wage = int(input('Enter wage: '))
            hours = int(input('Enter hours: '))
            if cnic in [i.getCnic() for i in hourly] or cnic in [i.getCnic() for i in salaried]:
                print('Employee already exists')
            else:
                hourly.append(HourlyEmployee(name, cnic, wage, hours))
                print("Hourly Employee Added")
                print()
    elif choice == 2:
        print()
        cnic = input('Enter cnic: ')
        for emp in salaried:
            if emp.getCnic() == cnic:
                print(emp.getDetails())
                break
        print()
        for emp in hourly:
            if emp.getCnic() == cnic:
                print(emp.getDetails())
                break
        print()
    
    elif choice == 3:
        print()
        cnic = input('Enter cnic: ')
        if cnic in [i.getCnic() for i in salaried]:
            for emp in salaried:
                if emp.getCnic() == cnic:
                    salaried.remove(emp)
                    print('Employee terminated')
                    break
        elif cnic in [i.getCnic() for i in hourly]:
            print()
            for emp in hourly:
                if emp.getCnic() == cnic:
                    hourly.remove(emp)
                    print('Employee terminated')
                    break
            print()
        else:
            print('Employee not found')
            print()

    elif choice == 4:
        print()
        print('Salaried Employees:')
        print("Name","CNIC","Monthly Salary")
        for emp in salaried:
            print(emp.getDetails())
        print()
        print('Hourly Employees:')
        print("Name","CNIC","Monthly Salary")
        for emp in hourly:
            print(emp.getDetails())
        print()
    elif choice == 5:
        break

    else:
        print('Invalid choice')
