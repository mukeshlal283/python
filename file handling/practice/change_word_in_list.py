# change word one or more at same time through list in list.txt (file)

list = ["donkey", "fool", "idiot"]

with open("list.txt") as f:
    con = f.read()

for word in list:
    con = con.replace(word, "$@##$@%")
    with open("list.txt", "w") as f:
        f.write(con)
    




'''hello 
how are you
you know 
you look like a donkey
uderstand you idiot
you are fool'''