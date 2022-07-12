
file = open("sample.txt", "r")
a = file.read()
print(a)
file.close()

'''
    'r' means read and 'r' is default don't need to write
    'w' means write
    'a' means append
    'ab' open in binary
    'at' open in text but t is fefault so you don't need to write 't', fist three
         has 't' default

'''

#you can also write this method
#open("sample.txt", "r").read()