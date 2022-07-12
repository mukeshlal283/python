
def greatest_number(num1, num2, num3):

    if(num1 > num2):
        if(num1 > num3):
            return num1
        else:
            return num3

    else:
        if(num2 > num3):
            return num2
        else:
            return num3

num1 = int(input("enter the number = "))
num2 = int(input("enter the number = "))
num3 = int(input("enter the number = "))

g = greatest_number(num1, num2, num3)
print("the greatest number is = ", g)