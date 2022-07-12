
# print line number where is "python"

content = True
i=1

with open("log.txt") as f:
    while content:              #loop in file until f.readline evaluate true
        content = f.readline()  #until f.readline evaluate true
            #if all line are read it be false and loop end
        if "python" in content.lower():#read as lower because or case sensitive (check_log.py)
            print(f"yes, it present on line number {i} ")
            print(content) #print line where "python" is present
            print(i)

        i+=1
