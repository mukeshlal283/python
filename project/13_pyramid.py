num = int(input("enter the number = "))

'''for i in range(num):
    print(("x" * (num - i)) + ("*" * i))'''

for i in range(1, num+1):

    for j in range(1, (num+1)-i):
        print(" ", end="")

    for j in range(1, i+1):
        print("* ", end = "")

    print()

