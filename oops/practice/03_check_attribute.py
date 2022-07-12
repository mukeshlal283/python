class Fruits:

    a = "apple"  #class attribute

obj = Fruits()
obj.a = "banana"  #instance attribute

print(Fruits.a)  #apple  --not change
print(obj.a)     #banana --change

'''to change value of class attriubute
--> Fruits.a = "chiko"'''