class Person:
     
    country = "India"
    
    def takeBreath(self):
        print("i am breathing ... ")

class Employee (Person):

    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary} ")

    def takeBreath(self):
        print("i am employee and how are you")

class Programmer (Employee):

    company = "fiver"

    def getSalary(self):
        print("no salary")

p = Person()
e = Employee()
pr = Programmer()

p.takeBreath()
e.takeBreath()
pr.takeBreath()



