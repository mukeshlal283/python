class Employee:

    company = "google"            #this is class attribute    
#Class Attribute 
'''direct link to class like "company" for all employee 
so it apply on all instances(company's employee)'''

goku = Employee()                  #object instantation
gohan = Employee()                 #same 

print(goku.company)
print(gohan.company)

Employee.company = "Meta"         #changing class Attribute
print(goku.company)
print(gohan.company)

goku.company = "apple"           #this is intance attribute (objects attribute)
goku.salary = "300"               #instance var.
print(goku.company)
print(goku.salary)