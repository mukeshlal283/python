
def factorial_iter(num):

    fact = 1
    for i in range(1, num+1):
    
        fact = fact * i
    
    return fact

def factorial_recursive(num):

    if num == 1 or num == 0:
        return 1

    return num * factorial_recursive(num-1)
# n * factorial(n-1)   n=5
# 5 * factorial(4)
# 5 * [4 * factorial(3)]
# 5 * 4 * [3 * factorial(2)]
# 5 * 4 * 3 * [2 * factorial(1)]  see if n == 1 it be 1  
# 5 * 4 * 3 * 2 * 1


#print(factorial_iter(5))
print(factorial_recursive(5))
