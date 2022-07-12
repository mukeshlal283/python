with open("list.txt") as f:
    content = f.read()

#copy content of "list.txt" and paste in "copy.txt"

with open("copy.txt", "w") as f:
    f.write(content)