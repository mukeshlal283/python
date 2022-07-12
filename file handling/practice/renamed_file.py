#renaming a file

import os

with open("sample2.txt") as f:
    content = f.read()

with open("renaming_file.txt", "w") as f:
    f.write(content)

os.remove("sample2.txt")        #for remove filesa
