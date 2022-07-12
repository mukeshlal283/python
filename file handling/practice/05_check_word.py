 # 'r' is default
f = open("sample_03.txt")
a = f.read()

word = input("write the word = ")

if word in a:
    print("in list")
else:
    print("not in list")