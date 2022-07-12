#use static method to print hello

class Calculator:

    def __init__(self, number):
        self.number = number
        print("number is", number)

    def square(self):
        print(f"square = {self.number ** 2}")

    def squareRoot(self):
        print(f"square'root = {self.number ** 0.5}")

    def cube(self):
        print(f"cube = {self.number ** 3}")

    @staticmethod
    def greet(name):
        print("hello", name)

a = input("enter your name = ")
b = int(input("enter the number = "))
newnum = Calculator(b)
newnum.square()
newnum.squareRoot()
newnum.cube()
newnum.greet(a)