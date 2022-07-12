'''x = "is awesome"

def myfunction():
    global x
    x = "good"
    print("python " + x)

myfunction()
print("pyhton " + x)'''


'''mylist = ["apple", "banana", "papaya", "watermelon"]
mylist.append("juice")
mylist2 = ["watermelon", 12, 90.01, True]
#mylist.extend(mylist2)
mylist.sort()'''

"""fno = input("enter the first number = ")
sno = input("enter the second number = ")
add = int(fno) + int(sno)
txt = "sum of two number = {} "
print("answer" + str(add))"""

"""a = input("a = ")
b = input("b = ")
if b > a:
    print("b is greater than a")
elif b == a:
    print("both are equal")
else:
    print("a is greater than b")"""

"""i = 1
while i < 10:
    print(i)
    if i == 6:
        break
    i+=1"""


"""def my_function(fname, age):
    txt = "my name is {} and my age is {} "
    print(txt.format(fname, age))

my_function("mukesh", 22)"""


"""class Person():
    def _init_(self, n, a):
        self.name = n
        self.age = a

p1 = Person("mukesh", "twentytwo")

print(p1.name)
print(p1.age)"""

"""def the_function(food):
    for x in food:
        print(x)

fruits = ["apple", "mangoes", "banana", "watermelons"]

the_function(fruits)"""

"""a = int(input("enter the first number = "))
b = int(input("enter the second number = "))

print("the sum of two number is", a%b)
print(type(a))"""

'''para = """the camel called the ship of the desert because they can survive 
and they can easily move on sand as they are paddedd feet. """

print(para.endswith("feet"))
print(para[0:-1])
print(type(para))'''

"""a = input("enter your name")
print("good morning " + a)"""

'''para = """hello, how are you 'name'
    you are pass!
    date = 'date'"""
a = input("enter your good name = ")
b = input("enter date = ")
para = para.replace("'name'", a)
para = para.replace("'date'", b)
print(para)'''

'''a = input("enter the fruit")
b = input("enter the fruit")
c = input("enter the fruit")
d = input("enter the fruit")
e = input("enter the fruit")
f = input("enter the fruit")

mylist = [a, b, c, d, e, f]
print(mylist)'''

"""a = (1, 0, 3, 8, 0, 4, 0, 4, 0)
print(a)
print(type(a))
b = a.count(0)
print(b)"""

                                   #project --> print greatest number from four numbers
"""
a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))
d = int(input("enter the number"))

if(a>d):
    f1=a
else:
    f1=d

if(b>c):
    f2=b
else:
    f2=c

if(f1>f2):
    print("greatest number is : ", f1)
else:
    print("greatest number is : ", f2)"""


                                                   #projeact --> fail or pass
"""
a =  int(input("enter math marks : "))
b = int(input("enter science marks : "))
c = int(input("enter hindi marks : "))

if(a<33 or b<33 or c<33):
    print("you rae fail because less than 33")
elif((a+b+c)/3 < 40):
    print("you are fail because total less than 40")
else:
    print("congrts! you are passed")"""

                                                        #project --> spam or not

'''txt = input("enter the txt\n")

if("make money fast" in txt):
    spam = True
elif("click here" in txt):
    spam = True
elif("download this" in txt):
    spam = True
else:
    spam = False

if(spam):
    print("alert! it's a spam")
else:
    print("no spam")'''

                                           #check username is 10 chracter or not
'''
a = input("enter the username : \n")

if(len(a) < 10):
    print("username must be 10 or more character")
else:
    print("ok")'''



                                    #project --> check name present in list or not
'''a = ["mukesh", "golak", "ajay", "yogender", "atul", "ambuj"]
name = input("enter the name : \n")

if name in a:
    print("present in list")
else:
    print("absent")'''

                                #project --> grade
'''marks = int(input("enter the marks : "))

if(marks >= 90 and marks <= 100):
    print("excellent")
elif(marks >= 80 and marks < 90):
    print("A+")
elif(marks >= 70 and marks < 80):
    print("B")
elif(marks >= 60 and marks < 70):
    print("C")
elif(marks >= 50 and marks < 60):
    print("D")
elif(marks < 80):
    print("F")'''

                                
                                #project --> while loop
'''i = 0
while(i<=10):
    print("yes " + str(i))
    i=i+1
'''

                            #project --> print list value using while loop
'''
mylist = ["apple", "mangoes", "banana", "strawberry", "chiko", "watermelon"]

#print(len(mylist))

i = 0
while(i<len(mylist)):
    print(mylist[i])
    i = i+1'''

               #SAME PROJECT USING FOR LOOP     
'''mylist = ["apple", "mangoes", "banana", "strawberry", "chiko", "watermelon"]

for i in mylist:
    print(i)'''

                        #project --> use range in for loop
'''for i in range(10):
    print(i)
print()
for i in range(1, 10):   #we use i twice because first one is end
    print(i)
print()             # range means from 1 to 10
for i in range(1, 10, 2):
    print(i)
print()'''


                        # --> use else in for loop
'''for i in range(10):
    print(i)
else:
    print("DONE")
'''

                        # --> using break tag in for loop
'''for i in range(10):
    print(i)
    if(i == 5):
        break
else:
    print("DONE")'''        #else not work beacuse range not going to 10 it break at 5 


                          #project --> using continue in loop
'''for i in range(10):
    if (i == 5):
        continue           #it skip 5 used in print even or odd number
    print(i)'''

                         #project --> make table
'''n = int(input("enter the number = "))
for i in range(1, 11):
    a = n*i                                 
    print(str(n)+"*"+str(i)+" = " ,a)  

print()

for i in range(1, 11):
    a = n*i
    print(f"{n}*{i}={a}")          #this is called //fstring   
'''

                                    # priject --> greet start with "S"
list1 = ["Harry", "Soham", "Sachin", "Rahul"]

for name in list1:
    if name.startswith("S"):            #startwith is keyword
        print("hello " + name)
