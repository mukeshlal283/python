# use "with" statement 
#so you do not need to use "close()" function at the end

with open("sample.txt", "a") as f:
    a = f.write(" ...hello i create using 04_use_with_stat.py program")

#print(a)
'''
if you do not use 'print' statement it will also run
'''