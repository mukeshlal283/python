class Employee:
    
    company = "google"

    def showDetails(self):
        print("this is an employee")

class Programmer(Employee):

    language = "python"

    def getLanguage(self):
        print(f"the language is {self.language} ")

    def showDetails(self):
        print("this is an programmer")

a = Employee()
a.showDetails()

b = Programmer()
b.getLanguage()
b.showDetails()
print(b.language)