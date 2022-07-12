num = int(input("enter the number = "))
con = True

for i in range(2, num):
    if(num%i == 0):
        con = False
        break

if con:
    print("this is prime number")
else:
    print("this is not a prime number")