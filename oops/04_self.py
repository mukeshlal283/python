class Employee:
    
    company = "google"
    def getSalary(self, signature):
        print(f"harry working in {self.company} at {self.salary}\n{signature} ")

harry = Employee()  #define object
#harry.getSalary()   if "self" not in function it show wierd error said 1 argument given see answer below 
#harry.getSalary() # == Employee.getSalary(harry) it actually written as this and work, harry is argument
                    # "self" means this
#Employee.getSalary(harry) #it work same 

harry.salary = 500000
harry.getSalary("thanks!")
