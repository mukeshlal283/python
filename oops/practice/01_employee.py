
#add info of employee

class Employee:

    company = "google"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getInfo(self):
        print(f"name is {self.name} and age is {self.age}, company : {self.company}")

harry = Employee("harry", 24)
suman = Employee("suman", 28)
harry.getInfo()
suman.getInfo()