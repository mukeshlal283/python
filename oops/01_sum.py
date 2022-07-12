from numbers import Number
import numbers


class Number:
    def sum(self):
        return self.a + self.b

num = Number()
num.a = 1
num.b = 2
print(num.sum())
