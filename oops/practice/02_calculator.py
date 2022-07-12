import numbers


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

newnum = Calculator(2)
newnum.square()
newnum.squareRoot()
newnum.cube()
