
def sum(n):
    
    num = 0

    for i in range(1, n+1):

        num = num + i

    return num

def recursion(number):   #using recursion

    if number == 0 or number == 1:
        return 1
    return number + recursion(number - 1)

print(sum(5))
print(recursion(5))