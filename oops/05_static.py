# in this we don't want "self" 
# we just write simple function

class Employee:

    @staticmethod      #so we use "staticmethod" if you write "self" then error
    def greet():
        print("good morning")

harry = Employee()
harry.greet()  #== Employee.greet()