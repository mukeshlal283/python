# use of __init__ it call first even we don't call it

class Employee:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
        print(f"employee is created")

    def getDetail(self):
        print(f"the name of employee is {self.name} ")
        print(f"the age of employee is {self.age} ")
        print(f"the department of employee is {self.department} ")        

harry = Employee("mukesh", 26, "programmer") #if you run till line no. 8 init function call automatically

harry.getDetail()